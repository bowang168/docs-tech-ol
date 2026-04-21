#!/usr/bin/env python3
"""
BM25 Sparse Vector Generator — 中英文混合分词
Shared module for Personal_AI_Brain and Technical_AI_Brain

Generates sparse vectors compatible with Qdrant's sparse vector format.
Uses jieba for Chinese segmentation + basic English tokenization.

Usage:
    from bm25_tokenizer import BM25Tokenizer

    tokenizer = BM25Tokenizer()
    tokenizer.fit(corpus_texts)           # build IDF from corpus
    sparse = tokenizer.encode(query_text) # -> SparseVector(indices, values)

Author: Bo Wang
Created: 2026-04-04
"""

import math
import re
from collections import Counter
from typing import Optional

import jieba
from qdrant_client.models import SparseVector

# Suppress jieba's noisy loading messages
jieba.setLogLevel(20)

# CJK Unicode ranges
_CJK_RE = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]')
_EN_SPLIT_RE = re.compile(r'[a-zA-Z0-9][-a-zA-Z0-9_.]*[a-zA-Z0-9]|[a-zA-Z0-9]+')

# Common stopwords (Chinese + English) — keep short, BM25 IDF handles most of the weighting
STOPWORDS = frozenset({
    # Chinese
    "的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都", "一",
    "一个", "上", "也", "很", "到", "说", "要", "去", "你", "会", "着",
    "没有", "看", "好", "自己", "这", "他", "她", "它", "们", "那",
    "被", "从", "把", "其", "与", "但", "而", "对", "以", "可以",
    # English
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "shall", "can", "need", "dare", "ought",
    "to", "of", "in", "for", "on", "with", "at", "by", "from", "as",
    "into", "through", "during", "before", "after", "above", "below",
    "between", "out", "off", "over", "under", "again", "further", "then",
    "once", "here", "there", "when", "where", "why", "how", "all", "each",
    "every", "both", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very",
    "and", "but", "or", "if", "while", "because", "this", "that", "these",
    "those", "it", "its", "i", "me", "my", "we", "our", "you", "your",
    "he", "him", "his", "she", "her", "they", "them", "their", "what",
    "which", "who", "whom",
})


def tokenize(text: str) -> list[str]:
    """Tokenize mixed Chinese-English text.

    Chinese: jieba cut → filter single chars that are stopwords
    English: split on non-alphanumeric → lowercase
    """
    tokens = []
    text_lower = text.lower()

    # Use jieba for the full text (handles both CJK and passes through English)
    for word in jieba.cut(text_lower):
        word = word.strip()
        if not word:
            continue
        if word in STOPWORDS:
            continue

        # Check if it's a CJK token
        if _CJK_RE.search(word):
            if len(word) >= 1:  # keep single CJK chars (they carry meaning)
                tokens.append(word)
        else:
            # English/number tokens from jieba — re-split to clean up
            for en_tok in _EN_SPLIT_RE.findall(word):
                if en_tok not in STOPWORDS and len(en_tok) >= 1:
                    tokens.append(en_tok)

    return tokens


class BM25Tokenizer:
    """BM25 sparse vector encoder with IDF learned from corpus.

    Parameters:
        k1: Term frequency saturation. Default 1.5
        b: Length normalization. Default 0.75
    """

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.vocab: dict[str, int] = {}   # token -> integer index
        self.idf: dict[int, float] = {}   # index -> IDF score
        self.avg_dl: float = 0.0          # average document length
        self.n_docs: int = 0
        self._fitted = False

    def fit(self, documents: list[str]) -> "BM25Tokenizer":
        """Build vocabulary and IDF from a corpus of documents."""
        self.n_docs = len(documents)
        if self.n_docs == 0:
            self._fitted = True
            return self

        doc_freq: Counter = Counter()  # token -> number of docs containing it
        total_len = 0
        all_tokens_set = set()

        for doc in documents:
            tokens = tokenize(doc)
            total_len += len(tokens)
            unique_tokens = set(tokens)
            for tok in unique_tokens:
                doc_freq[tok] += 1
                all_tokens_set.add(tok)

        self.avg_dl = total_len / self.n_docs if self.n_docs > 0 else 1.0

        # Build vocab: assign integer index to each token
        self.vocab = {tok: idx for idx, tok in enumerate(sorted(all_tokens_set))}

        # Compute IDF: log((N - df + 0.5) / (df + 0.5) + 1)
        for tok, idx in self.vocab.items():
            df = doc_freq.get(tok, 0)
            self.idf[idx] = math.log((self.n_docs - df + 0.5) / (df + 0.5) + 1.0)

        self._fitted = True
        return self

    def encode(self, text: str) -> SparseVector:
        """Encode text into a BM25 sparse vector.

        For unseen tokens (not in vocab from fit), assigns a new index
        and uses a default high IDF (rare term → high weight).
        """
        tokens = tokenize(text)
        if not tokens:
            return SparseVector(indices=[], values=[])

        tf_counter = Counter(tokens)
        dl = len(tokens)

        indices = []
        values = []

        for tok, tf in tf_counter.items():
            idx = self.vocab.get(tok)
            if idx is None:
                # Unseen token: assign next available index, give high IDF
                idx = len(self.vocab)
                self.vocab[tok] = idx
                self.idf[idx] = math.log((self.n_docs + 0.5) / (0.5) + 1.0) if self.n_docs > 0 else 1.0

            idf = self.idf.get(idx, 1.0)
            avg_dl = self.avg_dl if self.avg_dl > 0 else 1.0

            # BM25 score
            numerator = tf * (self.k1 + 1)
            denominator = tf + self.k1 * (1 - self.b + self.b * dl / avg_dl)
            score = idf * (numerator / denominator)

            if score > 0:
                indices.append(idx)
                values.append(round(score, 6))

        return SparseVector(indices=indices, values=values)

    def save(self, path: str):
        """Save tokenizer state to JSON."""
        import json
        state = {
            "k1": self.k1,
            "b": self.b,
            "vocab": self.vocab,
            "idf": {str(k): v for k, v in self.idf.items()},
            "avg_dl": self.avg_dl,
            "n_docs": self.n_docs,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False)

    @classmethod
    def load(cls, path: str) -> "BM25Tokenizer":
        """Load tokenizer state from JSON."""
        import json
        with open(path, "r", encoding="utf-8") as f:
            state = json.load(f)
        t = cls(k1=state["k1"], b=state["b"])
        t.vocab = state["vocab"]
        t.idf = {int(k): v for k, v in state["idf"].items()}
        t.avg_dl = state["avg_dl"]
        t.n_docs = state["n_docs"]
        t._fitted = True
        return t

    @property
    def vocab_size(self) -> int:
        return len(self.vocab)
