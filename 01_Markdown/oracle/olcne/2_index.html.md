---
title: "Release 2"
source_url: "https://docs.oracle.com/en/operating-systems/olcne/2/index.html"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "olcne"
  - "containers"
type: "oracle-doc"
sensitivity: public
---

# Oracle Cloud Native Environment Release 2

---

Oracle Cloud Native Environment (Oracle CNE) is a fully integrated suite for the development and management of cloud-native applications. Oracle CNE is a curated set of open source projects that are based on open standards, specifications and APIs defined by the Open Container Initiative (OCI) and Cloud Native Computing Foundation (CNCF) that can be easily deployed, have been tested for interoperability and for which enterprise-grade support is offered. Oracle CNE delivers a simplified framework for installations, updates, upgrades and configuration of key features for orchestrating microservices.

### Documentation

Read the documentation.

- [Release Notes](relnotes/)
- [Concepts](concepts/)
- [Quick Start](quickstart/)
- [CLI](cli/)
- [Kubernetes Clusters](clusters/)
- [Applications](applications/)
- [Kubernetes](kubernetes/)
- [Oracle Container Host for Kubernetes Image Builder](ockforge/)
- [Upgrade to Release 2](upgrade/)

### Get Started

Discover what's new in Release 2 and learn how to create Kubernetes clusters.

- [What's new in Release 2?](relnotes/new.html)
- [Learn about Release 2 concepts and architecture.](concepts/intro.html)
- [Create a KVM-based Kubernetes cluster using the libvirt provider.](quickstart/intro.html)
- [Create a Kubernetes cluster on Oracle Linux Virtualization Manager.](clusters/olvm_provider_concept.html)
- [Create a Kubernetes cluster on OCI.](clusters/oci_provider_concept.html)
- [Create a Kubernetes cluster on bare metal or other virtual instances, using the Bring Your Own provider.](clusters/byo_provider_concept.html)
- [Upgrade from Release 1.9 to Release 2.](upgrade/)

### Create Kubernetes Clusters

Learn about creating Kubernetes clusters on Oracle CNE using cluster providers. Providers are available for KVM-based clusters (libvirt), Oracle Cloud Infrastructure (OCI) clusters, and Bring Your Own clusters on bare metal or other virtual instances. Also learn how to use an application catalog to install cloud-native applications into a cluster.

- [Install the CLI.](cli/ocne_install_task.html)
- [Learn about cluster deployment options using cluster providers.](clusters/intro_concept.html)
- [Learn about the Oracle Container Host for Kubernetes (OCK) image used to create nodes in a Kubernetes cluster.](clusters/node_images_concept.html)
- [Create a KVM-based Kubernetes cluster using libvirt.](clusters/libvirt_provider_concept.html)
- [Create a Kubernetes cluster on Oracle Linux Virtualization Manager.](clusters/olvm_provider_concept.html)
- [Create a Kubernetes cluster on OCI.](clusters/oci_provider_concept.html)
- [Create a Kubernetes cluster on bare metal or other virtual instances, using the Bring Your Own provider.](clusters/byo_provider_concept.html)
- [Use cluster configuration files to customize clusters.](cli/config_concept.html)
- [Use application catalogs to install cloud-native applications into a cluster.](applications/apps_intro.html)
- [Learn Kubernetes concepts.](kubernetes/kube-about.html)
- [Use the Kubernetes CLI to create and manage containers and services.](kubernetes/kube_using.html)
- [Create a custom OCK image.](ockforge/intro.html)

### Manage Kubernetes Clusters

Learn how to administer Kubernetes clusters throughout their life cycle.

- [Keep clusters up to date with the latest Kubernetes release.](clusters/update_concept.html)
- [Back up clusters.](clusters/backup_concept.html)
- [Analyze a cluster and diagnose potential problems.](clusters/analyze_task.html)