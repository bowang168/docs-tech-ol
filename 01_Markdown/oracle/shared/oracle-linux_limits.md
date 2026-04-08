---
title: "Oracle Linux: Limits"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/limits"
fetched: 2026-03-26
tags:
  - "oracle-linux"
type: "oracle-doc"
sensitivity: public
---

This document describes the minimum and maximum limits for resources available to Oracle Linux users. Often, limits are theoretical in that they haven't been
physically tested and validated, but where a limit is implied by architecture or design, these
are described. Sometimes, other limitations might apply because of vendor hardware, firmware,
or software driver capabilities. Use this document alongside existing Oracle Linux release notes, platform, and hardware documentation for more
specific detail.

All limits described here assume that you're using the latest update level of each Oracle Linux release. Oracle strongly recommends
that whenever possible you update software to the current update level of the operating system
release.

## CPU Limits

A minimum of 2 logical CPUs is recommended for all operating system installs, where
possible.

| Architecture | Oracle Linux 7 | Oracle Linux 8 | Oracle Linux 9 | Oracle Linux 10 |
| --- | --- | --- | --- | --- |
| x86\_64 | Validated: 768  Theoretical: 5,120 | Validated: 768  Theoretical: 8,192 | Validated: 1,792  Theoretical: 8,192 | Validated: 1,792  Theoretical: 8,192 |
| aarch64 | Validated: 160  Theoretical: 4,096 | Validated: 256  Theoretical: 4,096 | Validated: 512  Theoretical: 4,096 | Validated: 512  Theoretical: 4,096 |

## Memory Limits

### Maximum Memory

| Architecture | Oracle Linux 7 | Oracle Linux 8 | Oracle Linux 9 | Oracle Linux 10 |
| --- | --- | --- | --- | --- |
| x86\_64 | Validated: 12 TB  Theoretical: 64 TB | Validated: 24 TB  Theoretical: 64 TB | Validated: 48 TB  Theoretical: 64 TB | 64 TB |
| aarch64 | Validated: 1 TB  Theoretical: 256 TB | Validated: 1.5 TB  Theoretical: 256 TB | Validated: 1.5 TB  Theoretical: 256 TB | Validated: 1.5 TB  Theoretical: 256 TB |

The maximum size of the address space that's available to each process is 128 TB.

### Minimum Required Memory

| Architecture | Oracle Linux 7 | Oracle Linux 8 | Oracle Linux 9 | Oracle Linux 10 |
| --- | --- | --- | --- | --- |
| x86\_64 | 1 GB minimum, 1 GB per logical CPU recommended | 1.5 GB minimum, 1.5 GB per logical CPU recommended | 1.5 GB minimum, 1.5 GB per logical CPU recommended | 2 GB minimum, 2 GB per logical CPU recommended |
| aarch64 | 2 GB | 2 GB | 2 GB | 2 GB |

Note that more memory might be required when performing a network installation. This
additional requirement might only apply during the installation process.

## Minimum Required Disk Space

| Oracle Linux 7 | Oracle Linux 8 | Oracle Linux 9 | Oracle Linux 10 |
| --- | --- | --- | --- |
| 10 GB minimum, 20 GB recommended | 10 GB minimum, 20 GB recommended | 10 GB minimum, 20 GB recommended | 10 GB minimum, 20 GB recommended |

## File System Limits

### Btrfs

| Feature | Oracle Linux 7 | Oracle Linux 8 | Oracle Linux 9 | Oracle Linux 10 |
| --- | --- | --- | --- | --- |
| Maximum file size | Theoretical: 8 EB | Theoretical: 8 EB | Theoretical: 8 EB | Theoretical: 8 EB |
| Maximum file system size | Theoretical: 8 EB | Theoretical: 8 EB | Theoretical: 8 EB | Theoretical: 8 EB |
| Maximum subdirectories | 264 | 264 | 264 | 264 |
| Maximum symlink depth | 40 | 40 | 40 | 40 |
| ACL support | Yes | Yes | Yes | Yes |

### Ext3

| Feature | Oracle Linux 7 | Oracle Linux 8 | Oracle Linux 9 | Oracle Linux 10 |
| --- | --- | --- | --- | --- |
| Maximum file size | 2 TB | 2 TB | 2 TB | 2 TB |
| Maximum file system size | 16 TB | 16 TB | 16 TB | 16 TB |
| Maximum subdirectories | 32,000 | 32,000 | 32,000 | 32,000 |
| Maximum symlink depth | 8 | 40 | 40 | 40 |
| ACL support | Yes | Yes | Yes | Yes |

### Ext4

| Feature | Oracle Linux 7 | Oracle Linux 8 | Oracle Linux 9 | Oracle Linux 10 |
| --- | --- | --- | --- | --- |
| Maximum file size | 16 TB | 16 TB | 16 TB | 16 TB |
| Maximum file system size | 50 TB  Theoretical: 1 EB | 50 TB  Theoretical: 1 EB | 50 TB  Theoretical: 1 EB | 50 TB  Theoretical: 1 EB |
| Maximum subdirectories | 65,000/unlimited | 65,000/unlimited | 65,000/unlimited | 65,000/unlimited |
| Maximum symlink depth | 8 | 40 | 40 | 40 |
| ACL support | Yes | Yes | Yes | Yes |

The limits for the ext4 file system that are described in the preceding table are higher than
the recommended limits and might prove unstable. If you are working with systems on which you
intend to work toward using higher file system sizes or file sizes, it is recommended that you
use either the Btrfs or XFS file system.

### XFS

| Feature | Oracle Linux 7 | Oracle Linux 8 | Oracle Linux 9 | Oracle Linux 10 |
| --- | --- | --- | --- | --- |
| Maximum file size | 500 TB  Theoretical: 8 EB | 8 EB | 8 EB | 8 EB |
| Maximum file system size | 500 TB  Theoretical: 16 EB | 1 PB | 1 PB | 1 PB |
| Maximum subdirectories | unlimited | unlimited | unlimited | unlimited |
| Maximum symlink depth | 8 | 40 | 40 | 40 |
| ACL support | Yes | Yes | Yes | Yes |

### OCFS2

| Feature | Oracle Linux 7 | Oracle Linux 8 | Oracle Linux 9 | Oracle Linux 10 |
| --- | --- | --- | --- | --- |
| Maximum file size | 16 TB  Theoretical: 4 PB | 16 TB  Theoretical: 4 PB | 16 TB  Theoretical: 4 PB | 16 TB  Theoretical: 4 PB |
| Maximum file system size | 16 TB  Theoretical: 4 PB | 16 TB  Theoretical: 4 PB | 16 TB  Theoretical: 4 PB | 16 TB  Theoretical: 4 PB |
| Maximum subdirectories | unlimited | unlimited | unlimited | unlimited |
| Maximum symlink depth | 40 | 40 | 40 | 40 |
| ACL support | Yes | Yes | Yes | Yes |

## Storage

| Feature | Oracle Linux 7 | Oracle Linux 8 | Oracle Linux 9 | Oracle Linux 10 |
| --- | --- | --- | --- | --- |
| Maximum boot LUN size (BIOS) | 2 TB | 2 TB | 2 TB | 2 TB |
| Maximum boot LUN size (UEFI) | 50 TB | 8 EB | 8 EB | 8 EB |
| Maximum number of device paths  Driver dependent and might require further configuration | 10,000 | 10,000 | 10,000 | 10,000 |

GPT and UEFI support are required for LUNs that are larger than 2 TB.

---

[Title and Copyright Information](#copyright-information)

Oracle Linux Limits

F38449-10

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2022, 2025, Oracle and/or its affiliates.