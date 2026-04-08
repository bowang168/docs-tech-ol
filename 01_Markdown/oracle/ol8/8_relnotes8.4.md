---
title: "Release Notes for Oracle Linux 8.4"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.4"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol8"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

Release Notes for Oracle Linux 8.4

F41354-09

November 2022

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 8 Release Notes for Oracle Linux 8.4

F41354-09

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2021, 2022, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.4/ol8.4-Preface.html -->

[Oracle Linux 8: Release Notes for Oracle Linux
8.4](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.4/) provides information about the new
features and known issues in the Oracle Linux 8.4 release. The information applies to
both x86\_64 and 64-bit Arm (aarch64) architectures. This document might be updated after
it is released.

### Conventions

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| boldface | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| italic | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |

### Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility
Program website at <https://www.oracle.com/corporate/accessibility/>.

For information about the accessibility of the Oracle Help Center, see the Oracle
Accessibility Conformance Report at <https://www.oracle.com/corporate/accessibility/templates/t2-11535.html>.

### Access to Oracle Support for Accessibility

Oracle customers that have purchased support have access to electronic support through My
Oracle Support. For information, visit <https://www.oracle.com/corporate/accessibility/learning-support.html#support-tab>.

### Diversity and Inclusion

Oracle is fully committed to diversity and inclusion. Oracle respects and values having a
diverse workforce that increases thought leadership and innovation. As part of our
initiative to build a more inclusive culture that positively impacts our employees,
customers, and partners, we are working to remove insensitive terms from our products and
documentation. We are also mindful of the necessity to maintain compatibility with our
customers' existing technologies and the need to ensure continuity of service as Oracle's
offerings and industry standards evolve. Because of these technical constraints, our effort
to remove insensitive terms is ongoing and will take time and external cooperation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.4/ol8-AboutOracleLinux8.html -->

The current Oracle Linux 8 release contains new features and enhancements that improve
performance in different areas including automation and management, security and compliance,
container management, and developer tools. These enhancements are especially designed to make
the operating system adaptable to different types of deployment from strictly on-premises
installations, hybrid deployments that combine on-premises and cloud installations, and full
cloud deployment.

### System Requirements and Limitations

To determine whether your hardware is supported on the current Oracle Linux 8 release, check
the Hardware Certification List at <https://linux.oracle.com/hardware-certifications>. Note that hardware is listed as it
becomes available and is validated.

Note that Oracle Linux 8 for the aarch64 platform is primarily engineered for use with
Ampereâ¢ eMAGâ¢-based EVK platform and the Marvell ThunderX2®
processor. Other hardware may be supported and added to the Hardware Certification List in
future.

CPU, memory, disk and file system limits for all Oracle Linux releases are described in
[Oracle Linux: Limits](https://docs.oracle.com/en/operating-systems/oracle-linux/limits/).

### Available Architectures

The release is available on the following platforms:

- Intel 64-bit (x86\_64)
- AMD 64-bit (x86\_64)
- 64-bit Arm (aarch64)

The Arm platform is only supported with Unbreakable Enterprise Kernel Release (UEK).

### Shipped Kernels

For the x86\_64 platform, Oracle Linux 8.4 ships with the following default kernel packages:

- `kernel-4.18.0-305.el8`: Red Hat Compatible Kernel (RHCK)
- `kernel-uek-5.4.17-2102.201.3.el8uek`: Unbreakable Enterprise
  Kernel Release 6 (UEK R6)

  For new installations, the UEK kernel is automatically enabled and installed. It also
  becomes the default kernel on first boot.

  For the 64-bit Arm (aarch64) platform, Oracle Linux ships only with the UEK kernel.

The Oracle Linux release is tested as a bundle, as shipped on the installation media image.
When installed from the installation media image, the minimum kernel version that is supported
is the kernel that is included in the image. Downgrading kernel packages is not supported,
unless recommended by Oracle Support.

### About the Unbreakable Enterprise Kernel

The Unbreakable Enterprise Kernel (UEK) is a Linux kernel
built by Oracle and supported through Oracle Linux support.
UEK is tested on Arm (aarch64), Intel x86, and AMD x86
(x86\_64) platforms. Each release contains additional features,
bug fixes, and updated drivers to provide support for key
functional requirements, improve performance, and optimize the
kernel for use on Oracle products such as Oracle's Engineered
Systems, Oracle Cloud Infrastructure, and large enterprise
deployments for Oracle customers.

Typically, a UEK release contains changes to the kernel ABI
relative to a previous UEK release. These changes require
recompilation of third-party kernel modules on the system. To
minimize impact on interoperability during releases, the
Oracle Linux team works closely with third-party vendors
regarding hardware and software that have dependencies on
kernel modules. Thus, before installing the latest UEK
release, verify its support status with your application
vendor.

The kernel ABI for a UEK release remains unchanged in all
subsequent updates to the initial release.

The kernel source code for UEK is available after the initial release through a public git
source code repository at <https://github.com/oracle/linux-uek>.

For more information about UEK such as tutorials, notices, and
release notes of different UEK versions, go to
[Unbreakable Enterprise Kernel documentation](https://docs.oracle.com/en/operating-systems/uek/).

### User Space Compatibility

Oracle Linux maintains user space compatibility with Red Hat Enterprise Linux (RHEL) that is
independent of the kernel version that underlies the operating system. Existing applications
in user space continue to run unmodified on UEK R6 and UEK R7, with no required
recertifications for RHEL certified applications.

### Obtaining Installation Images

The following installation images for the current Oracle Linux 8 release are available:

- Full ISO of Oracle Linux for typical on-premise
  installations
- Boot ISO of Oracle Linux for network installations
- Boot ISO of the supported UEK release for installing on
  hardware that is supported only on UEK
- Source DVDs

You can download these images from the following locations. Note
that the images in these locations are for both the x86\_64 and
aarch64 platforms, unless indicated otherwise:

- Oracle Software Delivery Cloud at <https://edelivery.oracle.com>
- Oracle Linux yum server at <https://yum.oracle.com/oracle-linux-downloads.html>

To prepare a downloaded image for installing Oracle Linux, see [Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/).

For information about the available ISOs for the three most recent updates to the Oracle
Linux releases, refer to <https://yum.oracle.com/oracle-linux-isos.html>.

For developers who are making use of the Raspberry Pi hardware platform, Oracle provides an
unsupported developer release image, which includes the firmware that is required to boot this
platform. For more information about making use of the Raspberry Pi hardware platform, see
[Install Oracle Linux on a Raspberry Pi](https://docs.oracle.com/en/learn/oracle-linux-install-rpi/).

Note:

Aside from installation ISOs, you can also use Oracle Linux
images to create compute instances on Oracle Cloud
Infrastructure. For information about these images, see the
release notes for the specific image that you are using on the
[Oracle
Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/images/) page.

To use Oracle Linux on Oracle Cloud Infrastructure, see <https://docs.oracle.com/iaas/oracle-linux/home.htm>.

### Upgrading From Oracle Linux 7 to Oracle Linux 8

You can upgrade an Oracle Linux 7 system to the latest Oracle Linux 8 release by
using the `leapp` utility. For step-by-step
instructions, as well as information about any known issues that
you might encounter when upgrading your system, see
[Oracle Linux 8: Performing System Upgrades With Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/8/leapp/).

### Installing Oracle-Supported RDMA Packages

Oracle Linux 8 ships with UEK R6 as the default kernel.

Oracle provides Remote Direct Memory Access (RDMA) packages for use with UEK R6. The RDMA
feature enables direct memory access between two systems that are connected by a network. RDMA
facilitates high-throughput and low-latency networking in clusters.

To use RDMA features, you must first install the Oracle-supported RDMA packages. To do so,
ensure that your system is subscribed to the appropriate channels on ULN or that you have
enabled the appropriate repositories on the Oracle Linux yum server.

RDMA With UEK R6

If you are subscribed to ULN, enable the following channels:

- `ol8_x86_64_UEKR6`
- `ol8_x86_64_baseos_latest`
- `ol8_x86_64_appstream`
- `ol8_x86_64_UEKR6_RDMA`

Note that if your system is newly registered on ULN, it is already subscribed to the
`ol8_x86_64_UEKR6`, `ol8_x86_64_baseos_latest`, and
`ol8_x86_64_appstream` channels by default. However, you must explicitly
subscribe to the `ol8_x86_64_UEKR6_RDMA` channel prior to installing RDMA
packages.

If you are using the Oracle Linux yum server, enable the following repositories:

- `ol8_UEKR6`
- `ol8_baseos_latest`
- `ol8_appstream`
- `ol8_UEKR6_RDMA`

Note that if your system already uses the Oracle Linux yum server, the
`ol8_UEKR6`, `ol8_baseos_latest`, and
`ol8_appstream` repositories are enabled by default. However, you must
explicitly enable the `ol8_UEKR6_RDMA` repository prior to installing RDMA
packages.

For more information about RDMA, including any known issues, see the [Unbreakable Enterprise Kernel: Release Notes for
Unbreakable Enterprise Kernel Release 6 (5.4.17-2011)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.4/ol8-NewFeaturesandChanges.html -->

This chapter describes the new features, major enhancements, bug fixes, and other changes
that are included in this release of Oracle Linux 8.

### Installation

The following notable change has been made to the graphical
installation program in Oracle Linux 8.4:

Graphical Installation Program Displays Warnings About Deprecated Kernel
Boot Arguments

All graphical installation program boot arguments that do not
contain the `inst.` prefix, such as
`ks`, `stage2`,
`repo`, and so on, have been deprecated since
Oracle Linux 7. These arguments will be removed in the next major Oracle Linux
release.

Starting with Oracle Linux 8.4, warning messages are displayed by the
graphical installation program whenever any boot arguments that
do not include the `inst.` prefix are used, as
appropriate.

For example, the following warnings are displayed in
`dracut` when booting the installation:

```
ks has been deprecated. All usage of Anaconda boot arguments
without the inst. prefix have been deprecated and will be removed in a future
major release. Please use inst.ks instead.
```

When the installation program is started in a terminal window,
the following warnings are displayed:

```
Deprecated boot argument ks must be used with the inst. prefix.
Please use inst.ks instead. Anaconda boot arguments without inst.
prefix have been deprecated and will be removed in a future major release.
```

### Red Hat Compatible Kernel

The following notable features, enhancements, and changes apply
to the Red Hat Compatible Kernel (RHCK) that is shipped with
Oracle Linux 8.4 on the x86\_64 platform.

For more information about the Unbreakable Enterprise Kernel Release 6 (UEK R6) release that is
shipped with , see the [Unbreakable Enterprise Kernel: Release Notes for
Unbreakable Enterprise Kernel Release 6 Update 2 (5.4.17-2102)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.2/).

- bcc updated to version 0.16.0

  The `bcc` package has updated to version
  0.16.0. This version of the package includes several
  improvements over the previous version.
- Berkeley Packet Filter updated to version 5.9

  The following, related Berkeley Packet Filter (BPF)
  packages are updated in this release:

  - `bpf` packages have been updated to
    version 5.9.
  - `bpftrace` packages have been updated
    to version 0.11.0 .
  - `lipbpf` packages have been updated to
    version 0.2.0.1 .
- cgroups implementation for the slab memory controller

  This release introduces a new implementation of the slab
  memory controller for the control groups
  (`cgroups`) technology. The slab memory
  controller improves slab utilization, as well as enables a
  shift in memory accounting from the page level to the
  object level. Note that this change eliminates each set of
  duplicated per-CPU and per-node slab caches for each
  memory control group, as well as establishes one, common
  set of per-CPU and per-node slab caches for all memory
  control groups. With this change, you can achieve a
  significant drop in the total kernel memory footprint and
  observe positive effects on memory fragmentation.
- CPU hotplug in hv\_24x7 and hv\_gpci PMUs support

  A change that enables PMU counters to correctly react to
  the hot-plugging of a CPU is introduced in this release.
  Now, if a `hv_gpci` event counter is
  running on a CPU that becomes disabled, the counting
  redirects to another CPU.
- EDAC module included

  This release includes the Error Detection and Correction
  (EDAC) kernel module, which is set in 8th and 9th
  generation Intel Core Processors (CoffeeLake). The EDAC
  kernel module primarily handles Error Code Correction
  (ECC) memory and detects and reports PCI bus parity
  errors.
- dwarves updated to version 1.19.1

  The `dwarves` package has been updated to
  version 1.19.1. This version of the package provides
  multiple bug fixes and enhancements over the previous
  version, as well as new way of checking functions from the
  DWARF debug data by using related
  `ftrace` entries to ensure that a subset
  of `ftrace` functions is generated.
- Free memory page feature added

  The Oracle Linux 8 host kernel is capable of returning memory pages
  that are not used by its VMs back to the hypervisor. This
  feature change improves the stability and resource
  efficiency of the host. Note that in order for memory page
  returning to work, it must be configured in the VM, and
  the VM must also use the `virtio_baloon`
  device.
- hwloc updated to version 2.2.0

  The `hwloc` package has been updated to
  version 2.2.0. With this change, `hwloc`
  can report details on Nonvolatile Memory Express (NVMe)
  drives, including total disk size, as well as sector size.
- ima-evm-utils updated to version 1.3.2

  The `ima-evm-utils` package has been
  updated version 1.3.2 to provide multiple bug fixes and
  enhancements, including the following changes:

  - Handling of the Trusted Platform Module (TPM2)
    multi-banks feature.
  - Extension of the boot aggregate value to Platform
    Configuration Registers (PCRs) 8 and 9.
  - Preloaded OpenSSL engine by using a command-line
    interface (CLI) parameter.
  - Intel Task State Segment (TSS2) PCR reading.
  - Support for the original Integrity Measurement
    Architecture (IMA) template.

  Note:

  Both the `libimaevm.so.0` and
  `libimaevm.so.2` libraries are part of
  `ima-evm-utils`. As such, using
  `libimaevm.so.0` has no effect if more
  recent applications use `libimaevm.so.2`.
- kabi\_whitelist package renamed to kabi\_stablelist

  The `kabi_whitelist` package has been
  renamed `kabi_stablelist`. This change
  was made in accordance with Oracle's commitment to
  replacing problematic and potentially offensive language.

  Note:

  A similar renaming has already taken place in the UEK R6
  release, per Bug ID 31783146.
- kdump enhancement for configuring VLAN tagged team interface

  In this release, you can configure a Virtual Local Area
  Network (VLAN) tagged team interface for
  `kdump`. This improvement enables
  `kdump` to use a VLAN tagged team
  interface to dump a `vmcore` file.
- kmod-redhat-oracleasm package added

  The `kmod-redhat-oracleasm` package has
  been added in this release. This package provides the
  kernel module part of the ASMLib utility. Oracle Automated
  Storage Management (ASM) is a data volume manager for
  Oracle databases. ASMLib is an optional utility that you
  can use on Oracle Linux systems to manage Oracle ASM
  devices.
- Levelling of IMA and EVM features across supported CPU architectures

  All CPU architectures, with the exception of the 64-bit
  ARM (aarch64) platform, have a similar level of feature
  support for Integrity Measurement Architecture (IMA) and
  Extended Verification Module (EVM) technologies. Note that
  the enabled functionalities are different for each CPU
  architecture. The following significant updates decrease
  the level of feature difference in IMA and EVM to ensure
  that user space applications behave the same across all
  supported CPU architectures:

  - Enabling of IMA appraise and trusted keyring.
  - AMD64 and Intel 64 include specific architecture policy
    in secure boot state.
  - IBM Power System (little-endian) includes specific
    architecture policy in secure and trusted boot state.
  - SHA-256 is the default hash algorithm for all supported
    architectures.
  - For all architectures, the measurement template has
    changed to IMA-SIG, and the template includes the
    signature bits when present. Its format is:
    `d-ng`|`n-ng`|`sig`.
- libbpf updated to version 0.2.0.1

  The `libbpf` package has been updated to
  version 0.2.0.1.
- perf improvements

  The following `perf` tool improvements
  are introduced in Oracle Linux 8.4:

  - Ability to add or remove tracepoints from a running
    collector.
  - Support for circular buffers that use specified events
    to trigger snapshots.
  - The `perf` script can record and
    display trace data with absolute timestamps. Note that
    to display trace data with absolute timestamps, the data
    must be recorded with the clock ID specified.
  - Top sorting order improvement.
- Proactive compaction included as disabled-by-default

  Proactive compaction regularly initiates memory compaction
  work prior to a request for allocation being made, which
  increases the chances that memory allocation requests find
  the physically contiguous blocks of memory without the
  requirement that memory compaction produce them on-demand.
  As a result, latency for specific memory allocation
  requests is lowered.

  Be aware that proactive compaction can result in increased
  compaction activity; which in turn, can result in serious,
  system-wide impact due to the fact that memory pages
  belonging to different processes are moved and remapped. For
  this reason, enabling proactive compaction requires the
  utmost care to ensure that latency spikes in applications
  are avoided.

  Note:

  Users who are running a UEK R6 release can explore using
  the `memoptimizer` user space daemon to
  manage proactive free memory for proactive compaction.
- Time namespace added

  Oracle Linux 8 includes the time namespace. This feature enables
  the system monotonic and boot-time clocks to work with
  per-namespace offsets on the AMD64, Intel 64, and 64-bit
  ARM (aarch64) architectures. Time namespace works well for
  changing the date and time inside Linux containers, as
  well as for making in-container adjustments of clocks
  after restoration from a checkpoint. This change enables
  you to independently set time for an individual container.

### Extended Berkeley Packet Filter

The Extended Berkeley Packet Filter (eBPF) feature is an
in-kernel virtual machine (VM) that enables code execution in
the kernel space, which takes place in the restricted sandbox
environment that has access to a limited set of functions. The
VM executes a special assembly-like code.

The following eBPF features are included in Oracle Linux 8.4:

- BPF Compiler Collection

  The BPF Compiler Collection (BCC) package provides tools
  for I/O analysis, networking, and monitoring of Oracle
  Linux operating systems that are using eBPF.
- BCC library

  The BCC library enables the development of tools that are
  similar to the those that are provided in the BCC tools
  package.
- eBPF for Traffic control

  The eBPF for the Traffic control (`tc`)
  feature enables programmable packet processing inside the
  kernel network data path.
- eXpress Data Path

  The eXpress Data Path (XDP) feature, which provides access
  to received packets before the kernel networking stack
  processes them, is supported under specific conditions.
- libbpf package

  The `libbpf` package is crucial for
  BPF-related applications such as
  `bpftrace` and
  `bpf`/`xdp` development.
- xdp-tools package

  The `xdp-tools` package contains user
  space support utilities for the XDP feature. The XDP
  feature is supported on both the AMD and Intel 64-bit
  architectures.

### Software Management

The following software management features and improvements are
introduced in this release:

- createrepo\_c package update and program improvement

  The `createrepo_c` packages have been
  updated to version 0.16.2. This version of the
  `createrepo_c` program includes an
  improvement that enables the program to automatically add
  modular metadata to repositories. In previous
  implementations, running the
  `createrepo_c` program on Oracle Linux 8 packages
  to create a new repository did not include modular
  repodata in this repository, which consequently caused
  various problems with repositories.

  With this change, the `createrepo_c`
  program does the following:

  - Scans for modular metadata.
  - Merges the found module YAML files into a single,
    modular document, `modules.yaml`.
  - Automatically adds the document to the repository.

  Because the adding of modular metadata to repositories is
  now automatic, you no longer need to perform the extra step
  of running the `modyfirepo_c` command to
  add modular metadata to repositories.
- Capability for mirror transaction between systems within DNF

  This change enables you to store and replay a transaction
  within DNF.

  To store a transaction from DNF history into a JSON file,
  use the `dnf history store`.

  To replay the transaction later one the same machine, or on
  a different one, use the `cnf history
  replay` command.

  Note that comps groups operations storing and replaying is
  supported. Module operations are not yet supported; and, as
  such, they are not stored or replayed.
- protect\_running\_kernel configuration option added

  You can use the new
  `protect_running_kernel` configuration
  option to control whether the package that corresponds to
  the running version of the kernel is protected from
  removal. This change provides the ability to disable
  protection of the running kernel.
- sos tools updated

  Oracle Linux 8.4 includes an updated `sos` RPM. As
  part of this change, the
  `/usr/sbin/sosreport` binary is
  deprecated. Note that this command continues to function
  as a legacy supported feature; however, the command is now
  redirected to the `sos report` command.
  For additional information, see
  <https://github.com/sosreport/sos>.

### GCC Toolset 10 Updates

Oracle Linux 8.4 provides the GCC Toolset 10, which is an Application
Stream that is distributed in the form of a Software Collection
in the `AppStream` repository. The GCC Toolset
is similar to the Oracle Linux Developer Toolset.

In Oracle Linux 8.4, the GCC compiler is updated to the upstream version.
This change provides multiple bug fixes.

The following tools and versions are included in this release:

- GCC version 10.2.1
- GDB version 9.2
- Valgrind version 3.16.0
- SystemTap version 4.4
- Dyninst version 10.2.1
- `binutils` version 2.35
- `elfutils` version 0.182
- `dwz` version 0.12
- `make` version 4.2.1
- `strace` version 5.7
- `ltrace` version 0.7.91
- `annobin` version 9.29

The GCC Toolset 10 is available as an Application Stream within
the `AppStream` repository, in the form of a
Software Collection.

To install this toolset, run the following command as the
`root` user:

```
sudo dnf install gcc-toolset-10
```

To run a tool from GCC Toolset 10, use the following command:

```
scl enable gcc-toolset-10 tool
```

The following command runs a shell session, where tool versions
from the GCC Toolset 10 take precedence over system versions of
the same tools:

```
scl enable gcc-toolset-10 bash
```

### Database

This release of Oracle Linux 8 ships with version 8.0 of the MySQL database software.

### Dynamic Programming Languages, Web, and Database Servers

Oracle Linux 8.4 includes the following feature changes and improvements
for dynamic programming languages, and web and database servers.
Note that this release also introduces the following new and
improved module streams:

- python39 module stream

  Python 3.9, which is provided by the new module
  `python39` module stream and the
  `ubi8/python-39` container image, is
  included in this release and replaces the previous
  `python38` module stream.
- swig:4.0 module stream

  Oracle Linux 8.4 includes Simplified Wrapper and Interface
  Generator (SWIG) version 4.0, which is available as the
  `swig:4.0` module stream.
- subversion:1.14 module stream

  The `subversion:1.14` module stream has
  been added in this release. Subversion 1.14 is the most
  recent Long Term Support (LTS) release.
- redis:6 module stream

  The `redis:6` module stream is available
  in this release. Redis 6 is an advanced key-value store
  that replaces the previous Redis 5 version.
- mysql-selinux package

  The new `mysql-selinux` package has been
  added in this release. The package includes an SELinux
  module that provides rules for the MySQL database. This
  package is installed by default with the database server.
  Note that the moduleâs priority is set to
  `200`.
- python-PyMySQL package

  The python-PyMySQL package, which provides the pure-Python
  MySQL client library, has been updated to version 0.10.1.
  This package is included in the
  `python36`, `python38`,
  and `python39` modules.
- python3-pyodbc package

  The `python3-pyodbc` package is included
  in this release. The `pyodbc` Python
  module provides access to Open Database Connectivity
  (ODBC) databases. The module implements the Python DB API
  2.0 specification, which can be used with third-party ODBC
  drivers. Capability has been added for using the
  Performance Co-Pilot (`pcp`) to monitor
  performance of the SQL Server.
- micropipenv package

  The new `micropipenv` package is
  available is this release. This package provides a
  lightweight wrapper for the `pip` package
  installer to support `Pipenv` and
  `Poetry` lock files. The
  `micropipenv` package is distributed in
  the AppStream repository and is provided under
  Compatibility level 4.
- py3c-devel and py3c-docs packages

  Oracle Linux 8.4 includes two new packages:
  `py3c-devel` and
  `py3c-docs`. These packages simplify the
  porting of C extensions to Python 3 and include a detailed
  guide and set of macros for easier porting.

  Note:

  These packages are distributed through the unsupported
  CodeReady Linux Builder (CLB) Repository.
- mod\_fcgid module can pass up to 1024 environment variables to FCGI
  server process

  The `mod_fcgid` module for the Apache
  HTTP Server can pass up to 1024 environment variables to a
  FastCGI (FCGI) server process. Note that the previous
  limit of 64 environment variables could cause applications
  running on the FCGI server to malfunction.
- perl-IO-String distributed through AppStream repository

  Starting with this release, the
  `perl-IO-String` package is distributed
  through the supported AppStream repository. This package
  provides the `Perl IO::String` module.
  Previously, the `perl-IO-String` package
  was only made available in the unsupported CLB repository.
- quota-devel package

  The new `quota-devel` package provides
  header files for implementing the quota Remote Procedure
  Call (RPC) service.

  Note:

  This package is distributed through the unsupported
  CodeReady Linux Builder (CLB) Repository.

### File Systems and Storage

Oracle Linux 8.4 provides the following file systems and storage
features, enhancements, and changes:

- Btrfs removed from RHCK

  The Btrfs file system is removed from RHCK in Oracle Linux 8. As
  such, you cannot create or mount Btrfs file systems when
  using this kernel. Also, any Btrfs user space packages
  that are provided are not supported with RHCK.

  Note:

  Support for the Btrfs file system is enabled in UEK R6.
  Starting with Oracle Linux 8.3, during an installation, you have
  the option to create a Btrfs root file system, as well as
  select Btrfs as the file system type when formatting
  devices. See [Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/) for more information about
  this feature.

  For more information about managing the Btrfs root file
  system, see [Oracle Linux 8: Managing Local File Systems](https://docs.oracle.com/en/operating-systems/oracle-linux/8/fsadmin/).

  For more information about the enhancements that have been
  made to Btrfs in UEK R6, see [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 6 Update 2 (5.4.17-2102)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.2/).
- OCFS2 removed from RHCK

  The Oracle Cluster File System version 2 (OCFS2) file
  system is removed from RHCK in Oracle Linux 8. As such, you cannot
  create or mount OCFS2 file systems when using this kernel.
  Also, any OCFS2 user space packages that are provided are
  not supported with RHCK.

  Note:

  OCFS2 is fully supported with UEK R6 in Oracle Linux 8.4.
- NVMe/TCP included as a Technology Preview

  NVMe over Fabrics TCP host and the target drivers are
  included in RHCK as a Technology Preview.

  Note:

  NVMe/TCP is already supported in Unbreakable Enterprise Kernel Release 6.
- Capability for creating swap partition 16 TiB in size during
  installation added

  In this release, for automatic partitioning, the installer
  continues to create a swap partition of maximum 128 GB.
  However, in the case of manual partitioning, you can
  create a swap partition of 16 TiB. Previously, during an
  Oracle Linux 8installation, the installer created a swap partition
  of maximum 128 GB for automatic and manual partitioning.
- Capability for surprise removal of NVMe devices added

  This improvement enables you to surprise remove NVMe
  devices from the Oracle Linux operating system without
  notifying the operating system in advance. This feature
  enhances the serviceability of NVMe devices due to the
  fact that no additional steps are required to prepare the
  devices for orderly removal, thus eliminating server
  downtime and ensuring the availability of servers.

  Take special note of the following additional important
  information and requirements for using this feature:

  - Surprise removal of NVMe devices requires that you be
    running UEK R6 or RHCK,
    `kernel-4.18.0-193.13.2.el8_2.x86_64`,
    or later.
  - Be aware of any additional hardware platform
    requirements that may exist.
  - Ensure that the software that is running on the platform
    supports the successful surprise removal of NVMe
    devices.
  - The surprise removal of an NVMe device that is critical
    to the system's operation is not
    supported. For example, you cannot remove an NVMe device
    that contains the operating system or a swap partition.
- API for mounting file systems added

  This release introduces a new API for mounting file
  systems based on an internal kernel structure called a
  filesystem context (`struct fs_context`).
  This change provides greater flexibility for communicating
  mount parameters between user space, the VFS, and the file
  system. The following system calls for operating on the
  file system context are provided:

  - `fsopen()`: Creates a blank file system
    configuration context within the kernel for the file
    system that is named in the `fsname`
    parameter, adds it to creation mode, and then attaches
    it to a file descriptor, which it then returns.
  - `fsmount()`: Takes the file descriptor
    that is returned by `fsopen()` and
    creates a mount object for the file system root that is
    specified there.
  - `fsconfig()`: Supplies parameters to
    and issues commands against a file system configuration
    context, as set up by the `fsopen(2)`
    or `fspick(2)` system calls.
  - `fspick()`: Ceates a new file system
    configuration context within the kernel and then
    attaches a pre-existing superblock to it so that it can
    be reconfigured.
  - `move_mount()`: Moves a mount from one
    location to another. This call can also be used to
    attach an unattached mount that is created by
    `fsmount()` or
    `open_tree()`, with the
    `OPEN_TREE_CLONE` system call.
  - `open_tree()`: Picks the mount object
    that is specified by the pathname, attaches it to a new
    file descriptor, or clones it, and then attaches the
    clone to the file descriptor.

  Note:

  Note that the former API, which is based on the
  `mount()` system call, is still
  supported.

  For more information, see the
  `Documentation/filesystems/mount_api.txt`
  file in the kernel source tree.

### High Availability and Clusters

The following high availability and clustering features are
included in Oracle Linux 8.4:

- Noncritical resources in colocation constraints support added

  This improvement enables you to configure a colocation
  constraint in such a way that if the dependent resource
  of the constraint reaches its migration threshold for
  failure, Pacemaker leaves the resource offline and keeps
  the primary resource on its current node rather than
  attempting to move both resources to another node. This
  change in behavior is implemented through the following
  options and feature changes:

  - New `influence` option. You can set
    this option to `true` or
    `false`. When the influence
    colocation option has a value of
    `false`, Pacemaker avoids moving the
    primary resource as a result of the status of the
    dependent resource. In this case, if the dependent
    resource reaches its migration threshold for failures,
    it stops if the primary resource is active and can
    remain on its current node.
  - Resources include a `critical`
    meta-attribute, which you can also set to
    `true` or `false`.
    The value of the `critical` resource
    meta-attribute determines the default value of the
    influence option for all colocation constraints that
    involve a resource as a dependent resource. The value
    of the `critical` resource meta
    option is set to `true` by default,
    which determines that the default value of the
    influence option is `true`, thus
    preserving the previous behavior where Pacemaker
    attempted to keep both resources active.
- New number data type for Pacemaker rules added

  As of this update, PCS includes a data type of
  `number` that you can use when defining
  Pacemaker rules in any PCS command that accepts rules.
  Note that Pacemaker rules implement
  `number` as a double-precision,
  floating-point number and `integer` as
  a 64-bit integer.
- Ability to specify a custom clone ID during creation of clone resource
  or promotable clone resource

  By default, during the process of creating a clone
  resource or a promotable clone resource, the clone
  resource is named `resource-id-clone`;
  but, if that ID is already in use, PCS adds a suffix
  -integer that starts with an integer value of
  `1`, which is then incremented by one
  for each additional clone. In this release, you can
  override this default by specifying a name for a clone
  resource ID or a promotable clone resource ID by
  specifying the `clone-id` option when
  creating a clone resource with the `pcs resource
  create` or `pcs resource
  clone` command.
- New commands for managing Corosync configuration

  This release introduces the following new commands for
  displaying and modifying Corosync configuration:

  - Capability for printing the contents of the
    `corosync.conf`file in several output
    formats by using the new `pcs cluster
    config` [`show`] command has
    been added. Note that by default, the `pcs
    cluster config` command uses the text output
    format, which displays the Corosync configuration in a
    human-readable form using the same structure and
    option names as the `pcs cluster
    setup` and `pcs cluster
    config` update commands.
  - Capability for modifying the parameters of the
    `corosync.conf`  file by using the
    new `pcs cluster config update`
    command. For example, you can use the command to
    increase the `totem` token to avoid
    fencing during temporary system unresponsiveness.
- You can change the configuration of the Corosync crypto
  cipher and hash by using the `pcs cluster config
  update` command. Previously, you could only
  configure Corosync traffic encryption when creating a new
  cluster. In addition, you can change the Corosync
  `authkey` by using the `pcs
  cluster authkey corosync` command.
- New crypt resource agent for shared and encrypted CFS2 file systems

  A new `crypt` resource agent has been
  added to Oracle Linux High Availability. You can use the
  `crypt` resource agent to configure a
  LUKS encrypted block device, which you can then use to
  provide shared and encrypted GFS2 file systems. Note
  that use of the `crypt` resource is
  currently only supported with GFS2 file systems.

### Infrastructure Services

Oracle Linux 8.4 introduces several version updates to infrastructure and
command-line tools, including the following:

- postfix-3.5.8 behavior change

  In this release, the `postfix-3.5.8`
  update behavior differs from the default upstream
  `postfix-3.5.8` behavior. This change in
  behavior is for backward compatibility purposes. For the
  default upstream postfix-3.5.8 behavior, you can use the
  following commands:

  ```
  postconf info_log_address_format=external
  ```

  ```
  sudo postconf smtpd_discard_ehlo_keywords=
  ```

  ```
  sudo postconf rhel_ipv6_normalize=yes
  ```

  Refer to the
  `/usr/share/doc/postfix/README-RedHat.txt`
  file for more details about this change.
- Bind updated to version 9.11.26

  The `bind` package is updated to version
  9.11.26 in this release. This version of Bind provides
  several bug fixes and enhancements over the previous
  version.
- ghostscript updated to version 9.27

  This version of `ghostscript` provides
  fixes for several vulnerabilities.
- Tuned updated to version 2.15-1

  The `tuned` packages have been updated to
  version 2.15-1. Tuned 2.15-1 includes an added
  `service` plugin for Linux services
  control and an improved `scheduler`
  plugin.
- dnstap improvement

  DNSTAP includes an advanced method for monitoring and
  logging the details of incoming name queries. The feature
  also records sent answers from the named service. DNSTAP
  provides a means of performing continuous logging of
  detailed, incoming queries without impacting the
  performance penalty. The new
  `dnstap-read` utility enables you to
  analyze the queries that are running on a different
  system.
- SpamAssassin updated to version 3.4.4.

  In this release, the `SpamAssassin`
  package has been updated to version 3.4.4. Two notable
  improvements include a new `OLEVBMacro`
  plugin and the addition of the following new functions:
  `check_rbl_ns`,
  `check_rbl_rcvd`,
  `check_hashbl_bodyre`, and
  `check_hashbl_uris`.
- Capability for changing key algorithm by using OMAP added

  This enhancement provides users with a way to change the
  key algorithm by using the `omshell`
  command. The key algorithm was previously hard coded as
  `HMAC-MD5`. This method is no longer
  considered secure.
- Sendmail provides capability for TLSFallbacktoClear configuration

  With this improvement, if the outgoing TLS connection
  fails, the sendmail client falls back to plaintext. This
  change addresses TLS compatibility problems with the other
  parties. Note that Oracle ships Sendmail with the
  `TLSFallbacktoClear` option disabled by
  default.
- tcpdump capable of capturing of RDMA traffic

  The ability to capture RDMA traffic by using the
  `tcpdump` command is enabled in this
  release. This feature change enables you to capture and
  analyze offloaded RDMA traffic. As a result, you can also
  use the `tcpdump` command to view
  RDMA-capable devices, capture RoCE and VMA traffic, and
  analyze its content.

### Networking

Oracle Linux 8.4 introduces the following features, enhancements, and
changes:

- NetworkManager updated to version 1.30.0

  This release introduces updated
  `NetworkManager` packages. Version 1.30.0
  of `NetworkManager` includes numerous bug
  fixes and improvements over the previous version,
  including the following notable new features, options, and
  connection properties:

  - `ipv4.dhcp-reject-servers` connection
    property. This new property defines which DHCP server
    IDs `NetworkManager` should reject
    lease offers.
  - `ipv4.dhcp-vendor-class-identifier`
    connection property. This new property sends a custom
    Vendor Class Identifier DHCP option value.
  - The `active_slave` bond option is
    deprecated in this release. You can set the primary
    option in the controller connection instead.
  - The `nm-initrd-generator` utility
    changes, including support for MAC addresses to indicate
    interfaces. The utility generator also supports creating
    InfiniBand connections.
  - `NetworkManager-wait-online` timeout
    service is increased to 60 seconds.
  - `ipv4.dhcp-client-id=ipv6-duid`
    connection property has been added and is compliant with
    [RFC4361](https://tools.ietf.org/html/rfc4361).
  - `ethtool` offload features added.
  - WPA3 Enterprise Suite-B 192-bit mode support added.
  - Virtual Ethernet (`veth`) devices
    added.
- iproute2 utility includes traffic control actions for adding MPLS
  headers before the Ethernet header

  The `iproute2` utility includes three new
  traffic control (`tc`) actions. These
  actions facilitate the implementation of Layer-2 Virtual
  Private Networks (L2VPNs) by adding Multi-protocol Label
  Switching (MPLS) labels before Ethernet headers. You can
  use the following actions while adding `tc
  filters` to network interfaces:

  Note:

  Because the MPLS feature is provided in Oracle Linux 8.4 as a
  Technology Preview, all of the `tc`
  actions that are described here are also provided as an
  unsupported Technology Preview.

  - `mac_push`: The
    `act_mpls` module provides this action
    to add MPLS labels before the original Ethernet header.
  - `push_eth`: The
    `act_vlan` module provides this action
    to build an Ethernet header at the beginning of the
    packet.
  - `pop_eth`: The
    `act_vlan` module provides this action
    to drop the outer Ethernet header.

  For further details, see the `tc-mpls(8)`
  and `tc-vlan(8)` manual pages.
- nmstate API fully supported

  The Nmstate API that was previously provided as a
  Technology Preview only is fully supported in this
  release. The `nmstate` packages include a
  library and the `nmstatectl` CLI that you
  can use to manage host network settings in a declarative
  manner. The networking state is described by a predefined
  schema. Note that both the reporting of the current state,
  as well as any changes to the desired, state conform to
  this schema.
- bareudp device support for encapsulating MPLS traffic over UDP tunnel
  included as Technology Preview

  As of this update, support for the
  `bareudp` device is available as a
  Technology Preview with the `ip link`
  command. The feature provides L3 encapsulation tunnelling
  capability for routing traffic with different L3
  protocols, such as unicast and multicast MPLS and
  IPv4/IPv6 inside a UDP tunnel. You can start routing MPLS
  packets in UDP by adding `tc` filters and
  actions.

  For more information about creating
  `bareudp` devices, see the
  `ip-link(8)` manual page.
- AF\_XDP socket feature included as Technology Preview

  The Address Family eXpress Data Path (AF\_XDP) socket
  feature is available as a Technology Preview in . AF\_XDP
  is designed for high-performance packet processing. The
  feature accompanies XDP and grants efficient redirection
  of programmatically selected packets to user space
  applications for further processing.

### Security

Oracle Linux 8.4 introduces the following security features,
enhancements, and changes:

- Clevis updated to version 15

  The `clevis` packages have been updated
  to version 15. This version of Clevis provides numerous
  bug fixes and other enhancements over the previous
  version, including the following notable changes:

  - `clevis` produces a generic initramfs
    and no longer automatically adds the
    `rd.neednet=1` parameter to the kernel
    command line.
  - Proper handling of incorrect configurations that use an
    `sss` pin. Also, the `clevis
    encrypt sss` subcommand returns outputs that
    indicate the cause of errors.
- fapolicyd updated to version 1.0.2

  The updated `fapolicyd` packages in this
  release provide numerous bug fixes and enhancements over
  the previous version, including the following features:

  - New `integrity` configuration option
    for enabling integrity checks by comparing file sizes
    and SHA-256 hashes, and by using the Integrity
    Measurement Architecture (IMA) subsystem.
  - Improved `fapolicyd` RPM plugin, which
    registers any system update that is handled by either
    the YUM package manager or the RPM Package Manager.
  - Rules can contain GID in subjects.
  - Ability to include rule numbers in debug and
    `syslog` messages.
- libreswan updated to version 4.3

  Updated `libreswan` packages are
  introduced in this release. Version 4.3 of
  `libreswan` provides several fixes and
  improvements for IKE, IKEv2, IPSec, as well as the
  following other notable improvements:

  - IPsec VPN support for TCP transport

    The updated `libreswan` package adds
    support for IPsec-based VPN over TCP encapsulation,
    per
    [RFC
    8229](https://tools.ietf.org/html/rfc8229). This improvement helps
    establish IPsec virtual private networks (VPNs) on
    networks that prevent traffic through the
    Encapsulating Security Payload (ESP) and UDP features.
    This enhancement enables you to configure VPN servers
    and clients to use TCP, either as a fallback or as the
    main VPN transport protocol.
  - Libreswan support for IKEv2 for Labeled IPsec

    In this release, the Libreswan Internet Key Exchange
    (IKE) implementation includes Internet Key Exchange
    version 2 (IKEv2) support of Security Labels for
    IPsec. This enhancement enables the upgrade of systems
    that use security labels with IKEv1 to IKEv2.
- OpenSCAP packages updated to version 1.3.4

  OpenSCAP version 1.3.4 provides a fix for memory issues
  and leaks, as well as other fixes for issues that resulted
  in systems with large amounts of files to run out of
  memory. Other notable changes include the following:

  - OpenSCAP treats GPFS as a remote file system.
  - Proper handling of OVALs with circular dependencies
    between definitions.
  - Improved `yamfilecontent`: updated
    `yam-filter`, as well as extended the
    schema and probe so that it can work with a set of
    values in maps.
  - Numerous warnings for GCC and Clang fixed.
  - Platform elements in XCCDF files properly resolve in
    accordance with the XCCDF specification.
  - Improved compatibility with the uClibc library.
  - Improved local and remote file system detection methods.
  - The `dpkginfo` probe can use
    `pkgCacheFile` rather than manually
    opening the cache.
  - OpenSCAP scan report is a valid HTML5 document.
- New RPM plugin that notifies fapolicyd about changes

  A new RPM plugin that notifies
  `fapolicyd` about any changes during RPM
  transactions has been added. The RPM plugin replaces the
  YUM plugin because its functionality is not limited to YUM
  transactions, while also accounting for any changes made
  by RPM.
- scap-security-guide packages updated to 0.1.54

  The `scap-security-guide` packages have
  been updated to version 0.1.54. The updated version
  provides several bug fixes and improvements over the
  previous version, including an updated Operating System
  Protection Profile, a family of profiles that are based on
  ANSSI BP-028 recommendations.
- scap-workbench can scan remote systems with sudo privileges

  As of this update, the `scap-workbench`
  GUI includes support for scanning remote systems by using
  passwordless `sudo` access. This
  improvement reduces the security risk that is imposed by
  supplying `root`'s credentials.

  Caution:

  Exercise caution when using this feature. Oracle
  recommends dedicating a well-secured user account that is
  solely designated for the OpenSCAP scanner.

### Web Console Includes Graphical Performance Analysis Capability

The web console includes graphical performance analysis
capability in this release. With this enhancement, the system
graphs page has been replaced with a new
View details and
history page, which is dedicated to analyzing the
performance of a system.

You can view performance metrics from the
Overview page by clicking
View details and history. The
page displays information about current metrics and historical
events, based on the Utilization Saturation and the Errors (USE)
method.

### Technology Preview

For the Red Hat Compatible Kernel in the current Oracle Linux 8 release, the following
features are under technology preview:

#### Multi-protocol Label Switching for TC

Multi-protocol Label Switching (MPLS) is available as a technology preview. This feature
is an in-kernel data-forwarding mechanism that routes the traffic flow across enterprise
networks. In an MPLS network, the router that receives packets decides the further route
of the packets, based on the labels that are attached to the packet. With the usage of
labels, the MPLS network has the ability to handle packets with particular
characteristics.

#### aarch64 only: VNC Remote Console

In this release, the Virtual Network Computing (VNC) remote
console is available as a technology preview on the 64-bit Arm
platform only. The remaining components of
the graphics stack are unverified on this platform.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.4/ol8-KnownIssues.html -->

This chapter lists known issues in the current Oracle Linux 8 release. The list covers issues
that might affect both x86 and aarch64 platforms. In the list, additional issues that are
specific only to aarch64 platforms are labeled `aarch64 only:`.

The following guides provide additional information about known issues that related to
specific Oracle Linux components:

- Podman container management tool: [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/)
- System and Oracle Cloud Infrastructure instance upgrade using Leapp: [Oracle Linux 8: Performing System Upgrades With Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/8/leapp/)

### Installation and Upgrade Issues

The following are known installation and upgrade issues that
have been encountered in this release of Oracle Linux 8.

#### "Warning: The unit file, source configuration file or drop-ins of pmlogger.service changed on disk. Run 'systemctl daemon-reload' to reload units" warning during upgrade

When upgrading from Oracle Linux 8.4 to Oracle Linux 8.5, with the appropriate
Oracle Linux 8 repositories enabled, the following warning is emitted:

```
Warning: The unit file, source configuration file or drop-ins of
pmlogger.service changed on disk. Run 'systemctl daemon-reload' to reload
units.
```

This warning can be safely ignored, as the upgrade completes
successfully.

(Bug ID 32852356)

#### Messages referring to tmpfiles.d/ files appear during upgrade

During an upgrade from Oracle Linux
8.5 to Oracle Linux 8.6, and with the appropriate Oracle Linux 8 repositories enabled, the
`dnf upgrade` command displays messages similar to the following:

```
Running scriptlet: systemd-239-44.0.1.el8.x86_64                    
4550/4550
[/usr/lib/tmpfiles.d/dnssec-trigger.conf:1] Line references path below legacy
directory /var/run/, updating /var/run/dnssec-trigger â /run/dnssec-trigger;
please update the tmpfiles.d/ drop-in file accordingly.
[/usr/lib/tmpfiles.d/krb5-krb5kdc.conf:1] Line references path below legacy
directory /var/run/, updating /var/run/krb5kdc â /run/krb5kdc; please update
the tmpfiles.d/ drop-in file accordingly.
[/usr/lib/tmpfiles.d/nss-pam-ldapd.conf:2] Line references path below legacy
directory /var/run/, updating /var/run/nslcd â /run/nslcd; please update the
tmpfiles.d/ drop-in file accordingly.
[/usr/lib/tmpfiles.d/pesign.conf:1] Line references path below legacy
directory /var/run/, updating /var/run/pesign â /run/pesign; please update
the tmpfiles.d/ drop-in file accordingly.
[/usr/lib/tmpfiles.d/portreserve.conf:1] Line references path below legacy
directory /var/run/, updating /var/run/portreserve â /run/portreserve; please
update the tmpfiles.d/ drop-in file accordingly.
.
.
.
```

These messages can be safely ignored, as the upgrade or
package installation completes successfully.

As an alternative workaround, update the configuration by following the instructions in the
message. Change the legacy `var/run/`<...> directory
path to `/run/`<...>.

(Bug ID 32852433)

#### Installation on Oracle 6.4 TB NVMe SSD device fails because mkfs.xfs cannot mount file system

Attempting to perform a fresh installation of Oracle Linux 8.5 on an
Oracle 6.4 TB NVMe SSD device will fail. This issue occurs
because the
`mkfs.xfs` command
cannot mount the file system. This failure is related to a
problem with the `xfsprogs`
package version that is in RHCK, with the root cause of the
issue being an NVMe SSD firmware bug.

To work around the issue, do not use the Oracle 6.4 TB NVMe
SSD as a boot disk.

An alternative option is to install Oracle Linux 8.2 and then upgrade
to Oracle Linux 8.5.

(Bug ID 32823840)

#### "/sbin/ldconfig: /lib64/libsmbldap.so.2 is not a symbolic link" messages returned during upgrade

When upgrading from Oracle Linux 8.3 to Oracle Linux 8.4, with the appropriate
Oracle Linux 8 repositories enabled, the `dnf upgrade`
command returns the following error message numerous times
during the upgrade process:

```
sbin/ldconfig: /lib64/libsmbldap.so.2 is not a symbolic link
```

These warnings can be safely ignored, as the upgrade completes
successfully.

(Bug ID 32846091)

#### Installer automatically enables Ethernet over USB network interface during a PXE installation

During a Preboot
Execution Environment (PXE) installation of Oracle Linux 8, the installer automatically
enables the Ethernet over USB network interface with the `bootproto=dhcp` and
`ONBOOT=yes` parameters. These default settings causes the
`NetworkManager` service to fail to start.

To prevent this issue from occurring, or to resolve the issue
if you have already encountered it, use one of the following
workarounds:

- Prior to installation, disable the
  `ONBOOT` parameter for the Ethernet over
  USB network interface in the kickstart file, as follows:

  ```
  network --bootproto=dhcp --device=enp0s20f0u8u3c2 --onboot=off --ipv6=auto
  ```
- During installation, on the Network & Host Name
  screen, do not select the Connect
  automatically with priority check box to
  connect automatically on every reboot for the Ethernet
  over USB network interface.
- If you have already encountered this issue, then after the installation, change the
  network configuration setting for the Ethernet over USB network interface to
  `ONBOOT=no`. Then reboot the system.

(Bug ID 31888490)

#### Interactive text-based installation wizard unable to complete when an alternate language is selected

If you selected an alternate language while
using the text-based installer to install the OS, you cannot proceed with the installation.
The installation is blocked with [!] flags for Software Selection and Installation
Destination regardless of what you have set for these two options.

However, this issue does not occur if you are performing an installation by using the
default English language selection or by using the graphical installation program.

(Bug IDs 30535416, 29648703)

#### Graphical installation program fails to produce error when an unacceptable Kdump value is entered

A minor upstream usability error affects the graphical installation program
during the configuration of Kdump.

If you specify an unacceptable value when manually configuring the Kdump memory reservation,
you can click `Done` to return to the Installation Summary screen. The
installer does not generate a warning or error message. Instead, the installer automatically
resets the value either to the last known acceptable value or the default value of 512 MB,
which enables the installation to succeed. However, because this corrected setting is not
displayed on the screen, you might not become aware that your specified value was ignored.

This issue does not occur with the text-based installer, which correctly returns an error if
you enter an unacceptable value and prevents you from continuing.

(Bug IDs 31133351, 31182708)

#### Graphical installation program does not display the reserved memory that is manually set for Kdump

A minor usability error affects the graphical installation program
during the configuration of Kdump. If you manually change the default memory size that is
reserved for Kdump, the new setting is not displayed when the screen is refreshed. Instead,
only the values for the total system memory and usable system memory are displayed.
Consequently, the limits for the parameter "Memory to be reserved (Mb)" become unknown for
future Kdump configuration.

Note:

The default setting `auto` for Kdump memory reservation is adequate as the
kernel determines what size to use when it boots

(Bug IDs 31133287 and 31182699)

#### Scriptlet-related error for microcode\_ctl might be displayed during upgrade

A scriplet-related
error message might be displayed during an upgrade of an Oracle Linux 8 release to its next
version. When you run the `dnf update` command, an output similar to the
following might appear:

```
  Running scriptlet: tuned-2.13.0-6.0.2.el8.noarch                            
             1089/1089
  Running scriptlet: microcode_ctl-4:20191115-4.el8.x86_64                    
             1089/1089
realpath: weak-updates/kmod-kvdo/vdo/kvdo.ko: No such file or directory
realpath: weak-updates/kmod-kvdo/uds/uds.ko: No such file or directory
dracut: installkernel failed in module kernel-modules-extra
warning: %posttrans(microcode_ctl-4:20191115-4.el8.x86_64) scriptlet failed,
exit status 1

Error in POSTTRANS scriptlet in rpm package microcode_ctl
  Running scriptlet: libgcc-8.3.1-4.5.0.7.el8.x86_64                          
             1089/1089
  Running scriptlet: glibc-common-2.28-101.0.1.el8.x86_64                    
             1089/1089
  Running scriptlet: info-6.5-6.el8.x86_64                                    
             1089/1089
```

This error message is displayed if you use the Server with GUI environment to install Oracle
Linux 8 and then you reboot the server by using RHCK. This installation method installs the
kernel dependent, `kmod-kvdo` package or module, which is a different version
in the previous Oracle Linux 8 release.

However, you can safely ignore the message because the `kmod-kvdo` package is
successfully installed during the upgrade process.

Note:

This error does not occur if you install the Minimal Install
base environment or if you boot the server with UEK R6 or
UEK R7.

(Bug ID 31292199)

#### rhnreg\_ks register command might fail if python3-rhn-virtualization-host package is installed

Beginning with
Oracle Linux 8.1, using the `rhnreg_ks` command to register a system with the
Unbreakable Linux Network (ULN)might fail if the
`python3-rhn-virtualization-hosts` package is installed on the system. This
issue has been observed when the `libvirtd` service is not running.

To work around this issue, ensure that the `libvirtd` packages are installed
on your system and that the service is enabled and running prior to issuing the
`rhnreg_ks` command.

(Bug ID 30366521)

#### Presence of beignet package could result in dependency issue during an upgrade

While upgrading a system to the current Oracle Linux 8 release,
you might encounter a dependency issue if the `beignet` package exists on the
system to be upgraded.

This issue exists specifically in cases where you upgrade systems running Oracle Linux 8.2 or
earlier releases to the current Oracle Linux version. In these earlier releases, the
`beginet` package requires earlier versions of the
`clang-libs` package.

However, the `beignet` package is currently not available for Oracle Linux
8.4 and later Oracle Linux 8 releases. Therefore, the issue does not exist for these
cases.

To work around this issue, remove the `beignet` package from the system prior
to upgrading to the current Oracle Linux 8 release.

(Bug ID 31213935)

#### ULN registration wizard not displayed on first boot after an installation

On new
installations of Oracle Linux 8, the ULN registration wizard that presents the options to
register with ULN and to use Oracle Ksplice is not displayed on first boot.

As an alternative, you can register with ULN after the installation completes. For
instructions, see <https://linux.oracle.com/>.

(Bug ID 29933974)

#### Graphics controller requirements for an installation on an Oracle VM VirtualBox guest

To successfully
install Oracle Linux 8 on an Oracle VM VirtualBox guest, where the graphical installation
program is used and the default `Server with GUI` environment is selected, you
must set the guest to use the VMSVGA graphics controller and configure the guest with at least
64MB of memory. Otherwise, the graphical display is unable to start correctly.

Beginning with Oracle VM VirtualBox 6.0, the VMSVGA graphics controller is the default
controller for guests running Linux operating systems. This issue is more likely to appear if
install Oracle Linux 8 on an existing guest that was created on an earlier Oracle VM
VirtualBox release. To configure Oracle Linux 8 guests, Oracle recommends that you use Oracle
VM VirtualBox 6.0 or later.

(Bug ID 30004543)

#### Spurious "hwcap directive ignored" messages appear during upgrade and when running ldconfig

Spurious messages that are similar to the following might be
emitted during a system update from Oracle Linux 8.4 to Oracle Linux 8.5:

```
/sbin/ldconfig:/etc/ld.so.conf.d/kernel-5.4.17-2102.201.3.el8uek.x86_64.conf:6: hwcap
directive ignored
```

These messages are the result of a change in kernel
configuration for UEK and can be safely ignored.

Note that this issue also occurs on subsequent runs of the
`ldconfig` command or for any service or
process that triggers the `ldconfig` command.
The messages can also be safely ignored in these cases.

(Bug ID 32816428)

#### Systemd daemon reload messages during system update of gssproxy package

Warnings are emitted when updating the
`gssproxy-0.8.0-16` and
`nfs-utils-1:2.3.3-41` packages to
`gssproxy-0.8.0-19` and
`nfs-utils-1:2.3.3-46`. The warnings are
triggered by the `nfs-utils` package update
and appear as follows and are an indication that you must
reload Systemd daemons:

```
Warning: The unit file, source configuration file or drop-ins of
gssproxy.service changed on disk. Run 'systemctl daemon-reload' to reload
units.
```

You can ignore these warning messages, as the services are
restarted later in the transaction.

(Bug ID 32831687)

### Removing container-selinux package might also remove the selinux-policy-targeted package

If you remove the `container-selinux`
package from the system after installing the current Oracle Linux 8 release, the
`selinux-policy-targeted` package might also be removed.

When this problem occurs, you might also see an error message about being unable to load
SELinux policy.

To avoid this issue, use the following syntax with the `dnf remove`
command:

```
sudo dnf remove container-selinux --setopt=exclude=selinux-policy-targeted
```

(Bug ID 32860334)

### Running dnf update glusterfs-\* command fails to upgrade previously installed packages

If
`glusterfs-*.i686` packages exist on an Oracle Linux 8 system which you then
upgrade to the next update version, running the `dnf update glusterfs*` command
later fails to upgrade GlusterFS packages.

As a workaround, first remove the `glusterfs-*.i686` packages from
the system, and then run the `dnf update glusterfs*` command.

(Bug ID 30279840)

### Updating libss package might fail if libss-devel package is installed

The `libss` package might fail to update if the
`libss-devel` package is installed on the system.

This issue persists if UEK R6 is enabled. However, after updating the kernel and enabling UEK
R7, the issue is no longer encountered.

To work around this issue, first remove the `libss-devel` package from the
system. Then, install the corresponding version of this package from the Oracle Linux 8 Distro
Builder developer repository (`ol8_distro_builder`).For example, you can run
the following command:

```
sudo dnf --enablerepo=ol8_distro_builder install libss-devel
```

Note:

The `ol8_distro_builder` repository is an unsupported developer repository.
You should only enable it for this particular installation action, rather than enabling it
globally.

(Bug ID 32005190)

### Options for configuring disk cache characteristics during VM creation unavailable in web console

Some options for configuring disk cache characteristics in the
web console are currently not available when you are creating a
new VM or before the installation starts. For disks that are
already added to a VM or when adding a new disk to an already
running system, these configuration options are available in the
web console.

As an alternative solution, and before the installation begins, use the
`virt-manager` CLI or a similar CLI to configure disk cache
characteristics for a newly added disk as well for disks that already exist in the VM.

Oracle recommends that you should use Oracle Linux Virtualization Manager for more complex
virtualization requirements. For more information, see <https://docs.oracle.com/en/virtualization/oracle-linux-virtualization-manager/>.

(Bug ID 30301271)

### ACPI error messages displayed on Dell EMC PowerEdge Server during boot

During a system
boot of an Intel-based Dell EMC PowerEdge Server, error messages similar to the following
might be displayed if the Dell Active Power Controller (DAPC) setting is enabled in the BIOS:

```
kernel: ACPI Error: No handler for Region [SYSI] (0000000061df8ef3) [IPMI] (20190816/evregion-132)
kernel: ACPI Error: Region IPMI (ID=7) has no handler (20190816/exfldio-265)
kernel: ACPI Error: Aborting method \_SB.PMI0._GHL due to previous error (AE_NOT_EXIST) (20190816/psparse-531)
kernel: ACPI Error: Aborting method \_SB.PMI0._PMC due to previous error (AE_NOT_EXIST) (20190816/psparse-531)
kernel: ACPI Error: AE_NOT_EXIST, Evaluating _PMC (20190816/power_meter-743)
```

To work around this issue, disable the `apci_power_meter` kernel module as
follows:

```
echo "blacklist acpi_power_meter" >> /etc/modprobe.d/hwmon.conf
```

After disabling the `apci_power_meter` kernel
module, reboot the system for the change to take effect.

For environments that do not require the DAPC feature, as an
alternative workaround, you can disable the DAPC BIOS setting.

(Bug ID 32105233)

### Oracle Linux 8 does not recognize SAS controllers on older Oracle Sun hardware

The Oracle Linux 8
installer does not recognize some Serial Attached SCSI (SAS) controllers that are found in
older Oracle Sun server models. If you attempt to install Oracle Linux 8 on these server
models, the installer does not recognize the local disk and the installation fails. Examples
of these server models include, but are not limited to, the following: Oracle Sun Fire X4170
M2 Server, Oracle Sun Fire X4170 M3 Server, Oracle Sun OVCA X3-2 Server, and the Oracle Sun
X4-2 Server.

The following SAS controllers are removed from the
`mpt2sas` driver in RHCK:

- SAS2004, PCI ID 0x1000:0x0070
- SAS2008, PCI ID 0x1000:0x0072
- SAS2108\_1, PCI ID 0x1000:0x0074
- SAS2108\_2, PCI ID 0x1000:0x0076
- SAS2108\_3, PCI ID 0x1000:0x0077
- SAS2116\_1, PCI ID 0x1000:0x0064
- SAS2116\_2, PCI ID 0x1000:0x0065
- SSS6200, PCI ID 0x1000:0x007E

The following SAS controllers are removed from the
`megaraid_sas` driver in RHCK:

- Dell PERC5, PCI ID 0x1028:0x15
- SAS1078R, PCI ID 0x1000:0x60
- SAS1078DE, PCI ID 0x1000:0x7C
- SAS1064R, PCI ID 0x1000:0x411
- VERDE\_ZCR, PCI ID 0x1000:0x413
- SAS1078GEN2, PCI ID 0x1000:0x78
- SAS0079GEN2, PCI ID 0x1000:0x79
- SAS0073SKINNY, PCI ID 0x1000:0x73
- SAS0071SKINNY, PCI ID 0x1000:0x71

The workaround for this issue to use the Unbreakable Enterprise Kernel Release 6 (UEK R6) boot
ISO, and then run UEK R6 with Oracle Linux 8, as these controllers are
supported in the Unbreakable Enterprise Kernel release.

(Bug ID 29120478)

### File System Issues

The following are known file systems issues that have been
encountered in this release of Oracle Linux 8.

#### Btrfs file system not supported on RHCK

The Btrfs file system is removed from RHCK in Oracle Linux 8, which
means you cannot create or mount this file system when using
this kernel. Also, any Btrfs user space packages that are
provided are not supported with RHCK.

Support for the Btrfs file system is enabled in UEK R7 and
UEK R6. Starting with Oracle Linux 8.3, during an installation, you
have the option to create a Btrfs root file system, as well as
select Btrfs as the file system type when formatting devices.

For further details about these changes, see the following
documentation:

- For information about creating a Btrfs root file system
  during an installation, see [Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/).
- For information about managing the Btrfs file system, see
  [Oracle Linux 8: Managing Local File Systems](https://docs.oracle.com/en/operating-systems/oracle-linux/8/fsadmin/).
- For the latest information about other enhancements that
  have been made to Btrfs in UEK R6, see
  [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 6 Update 3 (5.4.17-2136)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.3/).

  For information about UEK R7, see
  [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 7 (5.15.0-0.30)](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/).

#### OCFS2 file system not supported on RHCK

The OCFS2 file system is removed from RHCK in Oracle Linux 8, which
means you cannot create or mount this file system when using
this kernel. Also, OCFS2 user space packages that are provided
are not supported with RHCK.

Note that support for OCFS2 file systems is enabled in UEK R7
and UEK R6. For the latest information and other enhancements
that have been made to OCFS2 in UEK R6, see
[Unbreakable Enterprise Kernel: Release Notes for
Unbreakable Enterprise Kernel Release 6 Update 3 (5.4.17-2136)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.3/). See also [Unbreakable Enterprise Kernel: Release Notes for
Unbreakable Enterprise Kernel Release 7 (5.15.0-0.30)](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/).

#### ext4: Frequent or repeated system shutdowns can cause file system corruption

If a system that is using the `ext4` file system is repeatedly
or frequently shut down, the file system might become corrupted. This issue is difficult to
replicate and is therefore considered to be a corner-case issue. The issue exists in the
upstream code and proposed patches are currently under review.

(Bug ID 27547113)

### Kernel Issues

The following are known kernel issues that have been encountered
in this release of Oracle Linux 8.

#### Default kernel for KVM guest snapshots might not be interchangeable

Creating a KVM guest snapshot
that uses one kernel and then reverting the snapshot to switch to another kernel might cause
various `virsh` commands to fail, as shown in the following examples. The
switch can be from RHCK to UEK or vice-versa.

```
sudo virsh start myGuest --console
```

```
error: Failed to start domain myGuest
error: operation failed: guest CPU doesn't match specification: missing
features: md-clear
```

Running the following command produces similar errors:

```
sudo virsh snapshot-revert myGuest mySnapshot1 --force
```

```
error: operation failed: guest CPU doesn't match specification: missing
features: ibpb,amd-ssbd
```

However, this issue is not encountered if you are interchanging kernel versions from the
same vendor.

To avoid this issue, ensure that you guest snapshots use the same kernel on which they were
initially created.

(Bug ID 30561489)

#### KVM guests boot with "amd64\_edac\_mod: Unknown symbol" errors on AMD 64-bit platforms

The following errors might be displayed repeatedly when KVM
guests are booting on 64-bit AMD hosts:

```
[   12.474069] amd64_edac_mod: Unknown symbol amd_register_ecc_decoder (err [ 120)
[   12.474083] amd64_edac_mod: Unknown symbol amd_report_gart_errors (err 0)
[   12.852250] amd64_edac_mod: Unknown symbol amd_unregister_ecc_decoder (err 0)
[   12.852297] amd64_edac_mod: Unknown symbol amd_register_ecc_decoder (err 0)
.
.
.
```

These errors occur because the module code for the kernel
erroneously returns `-EEXIST` for modules
that failed to load and are in the process of being removed
from the module list. The `amd64_edac_mod`
module will not be loaded in a VM. These errors can be
ignored, as they do not impact functionality in any way.

This issue occurs on Oracle Linux 8 hosts that are running RHCK only and is not
encountered on UEK R6 hosts.

(Bug ID 29853602)

#### Output of modinfo command does not show Retpoline support

A bug in the
Oracle Linux 8 code causes Retropline support to not be displayed in the output of the
`modinfo -F retpoline` command, even though the
`CONFIG_RETPOLINE` flag is set to `Y`, for example:

```
sudo modinfo -F retpoline
/usr/lib/modules/4.18.0-80.el8.x86_64/kernel/sound/usb/usx2y/snd-usb-us122l.ko
.xz
```

The `CONFIG_RETPOLINE=Y` flag is still
required to add and display Retpoline support. If the
parameter is enabled, the kernel builds with a retpoline
capable compiler.

To confirm that the `CONFIG_RETPOLINE` flag is enabled, search
for the parameter in the kernel's `config-kernel`
configuration file, for example:

```
cat /boot/config-5.4.17-2011.7.4.el8uek.x86_64 | grep RETPOLINE.
```

```
CONFIG_RETPOLINE=y
```

(Bug ID 29894295)

#### Kdump might fail on some AMD hardware

Kdump might fail on some AMD hardware that is running the current Oracle
Linux release. Impacted hardware includes the AMD EPYC CPU servers.

To work around this issue, modify the `/etc/sysconfig/kdump` configuration
file and remove the `iommu=off` command-line option from the
`KDUMP_COMMANDLINE_APPEND` variable. Restart the `kdump`
service for the changes to take effect.

(Bug ID 31274238, 34034614, 34211826)

#### Limitations of the LVM dm-writecache caching method

The new LVM `dm-writecache` caching method
has certain limitations that do not exist with the
`dm-cache` method, including the following:

- Cannot attach or detach `dm-writecache`
  when a logical volume is active.
- Cannot take a snapshot of a logical volume when the
  logical volume is using `dm-writecache`.
- Must use a `dm-writecache` block size
  that matches the existing file system block size when
  attaching `dm-writecache` to an inactive
  logical volume.
- Cannot resize a logical volume when
  `dm-writecache` is attached to the
  volume.
- Cannot use `pvmove` commands on devices
  that are used with `dm-writecache`.
- Cannot use logical volumes with
  `dm-writecache` when using thin pools or
  the virtual data optimizer (VDO).

For more information about the `dm-writecache` caching method, see the File
Systems and Storage features section of [Oracle Linux 8: Release Notes for Oracle Linux
8.2](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.2/). See
also the `lvmcache(7)` manual page.

### tracepath6 does not parse destination IPv6 address correctly

Running the `tracepath6` command fails to parse the destination IPv6 address
correctly. Consequently, the tool traces a route to the wrong host.

To work around this issue, use a tool with similar capabilities to the
`tracepath6` command.

(Bug ID 29540588)

### Running nohup prevents ssh command from executing

On an Oracle Linux 8 system, running the
`nohup` command such as given in the following example might cause
`ssh` command issues.

```
/usr/bin/nohup ./myscript > nohup.out &
```

If you attempt to remotely connect to that same system by using the `ssh`
command, the command hangs.

To work around this issue, modify the `nohup` command syntax as
follows:

```
/usr/bin/nohup ./myscript > nohup.out 2>&1 &
```

(Bug ID 30287091)

### Restarting firewalld service results in SSH connection timeout

Restarting the `firewalld` service
leads to an SSH connection timeout on the terminal from which the service was started. Note
that other SSH terminals remain connected.

(Bug ID 29478124)

### Error: "mcelog service does not support this processor"

An error indicating that the `mcelog` service
does not support the processor can appear in the system log on
systems with AMD processors, such as some Oracle Server
hardware. The message might be displayed as follows:

```
mcelog: ERROR: AMD Processor family
23: mcelog does not support this processor.  Please use the edac_mce_amd
module instead.
```

The `mcelog` daemon is a service that is used on x86\_64
platforms to log and handle hardware error messaging. On AMD systems, the
`edac_mce_amd` kernel module handles machine exception logging. Therefore,
AMD systems do not require the `mcelog` daemon. This error should be downgraded
to a warning.

(Bug ID 29501190)

### Power button defaults to ACPI Suspend mode

By default, the Oracle Linux 8 graphical user interface (GUI) console
mode treats the hardware power button as the equivalent of the
ACPI "Sleep" button, which puts the system into low-power sleep
mode. This behavior is specific to the GNOME desktop
environment.

In previous Oracle Linux releases, the hardware power button initiated a
system shutdown. To ensure that Oracle Linux 8 behaves the same way, do
the following:

1. Create a file named
   `/etc/dconf/db/local.d/01-shutdown-button-action`
   with following content:

   ```
   [org/gnome/settings-daemon/plugins/power]
   power-button-action='interactive'
   ```
2. Create a file named
   `/etc/dconf/db/local.d/locks/01-power` with
   the following content:

   ```
   /org/gnome/settings-daemon/plugins/power/power-button-action
   ```
3. Run the following command:

   ```
   sudo dconf update
   ```
4. Log out of the desktop environment and then log back in for
   the new settings to take effect.

(Bug ID 25597898)

### Podman Issues

For information about known issues with the Podman container management tool in Oracle Linux
8, refer to Known Issues chapter of the [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).

### TLS 1.3 not supported for NSS in FIPS Mode

TLS 1.3 is enabled by default in Oracle Linux 8. Applications that are
built with NSS do not support connections that require TLS 1.3
in FIPS mode. To make such connections work, disable FIPS mode
or use TLS 1.2.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.4/ol8-PackageChangesfromtheUpstreamRelease.html -->

The following sections list the changes to binary and source
packages from the upstream release.

### Changes to Binary Packages

This section contains information about the removed, modified, and new binary packages in this release. For information about the source package changes, see [Changes to Source Packages](ol8-PackageChangesfromtheUpstreamRelease.html#ol8-packages-source) .

#### Added Binary Packages for BaseOS by Oracle

The following binary packages have been added to BaseOS by Oracle:

- `bcache-tools`
- `btrfs-progs`
- `dtrace`
- `kernel-uek`
- `kernel-uek-debug`
- `kernel-uek-debug-devel`
- `kernel-uek-devel`
- `kernel-uek-doc`
- `libasan6`
- `ocfs2-tools`
- `oracle-backgrounds`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`
- `oracle-logos-httpd`
- `oracle-logos-ipa`

#### Added Binary Packages for AppStream by Oracle:

The following binary packages have been added to AppStream by Oracle:

- `dtrace-devel`
- `dtrace-testsuite`
- `libblockdev-btrfs`

#### Added Binary Packages for CodeReady Linux Builder by Oracle

No binary packages were added to CodeReady Linux Builder by Oracle.

#### Modified BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been modified:

- `autofs`
- `binutils`
- `boom-boot`
- `boom-boot-conf`
- `boom-boot-grub2`
- `chkconfig`
- `chrony`
- `cockpit`
- `cockpit-bridge`
- `cockpit-doc`
- `cockpit-system`
- `cockpit-ws`
- `coreutils`
- `coreutils-common`
- `coreutils-single`
- `dbus`
- `dbus-common`
- `dbus-daemon`
- `dbus-libs`
- `dbus-tools`
- `dracut`
- `dracut-caps`
- `dracut-config-generic`
- `dracut-config-rescue`
- `dracut-live`
- `dracut-network`
- `dracut-squash`
- `dracut-tools`
- `efibootmgr`
- `efi-filesystem`
- `firewalld`
- `firewalld-filesystem`
- `fuse`
- `fuse3`
- `fuse3-devel`
- `fuse3-libs`
- `fuse-common`
- `fuse-devel`
- `fuse-libs`
- `fwupd`
- `fwupdate`
- `fwupdate-efi`
- `fwupdate-libs`
- `glibc`
- `glibc-all-langpacks`
- `glibc-common`
- `glibc-devel`
- `glibc-headers`
- `glibc-langpack-aa`
- `glibc-langpack-af`
- `glibc-langpack-agr`
- `glibc-langpack-ak`
- `glibc-langpack-am`
- `glibc-langpack-an`
- `glibc-langpack-anp`
- `glibc-langpack-ar`
- `glibc-langpack-as`
- `glibc-langpack-ast`
- `glibc-langpack-ayc`
- `glibc-langpack-az`
- `glibc-langpack-be`
- `glibc-langpack-bem`
- `glibc-langpack-ber`
- `glibc-langpack-bg`
- `glibc-langpack-bhb`
- `glibc-langpack-bho`
- `glibc-langpack-bi`
- `glibc-langpack-bn`
- `glibc-langpack-bo`
- `glibc-langpack-br`
- `glibc-langpack-brx`
- `glibc-langpack-bs`
- `glibc-langpack-byn`
- `glibc-langpack-ca`
- `glibc-langpack-ce`
- `glibc-langpack-chr`
- `glibc-langpack-cmn`
- `glibc-langpack-crh`
- `glibc-langpack-cs`
- `glibc-langpack-csb`
- `glibc-langpack-cv`
- `glibc-langpack-cy`
- `glibc-langpack-da`
- `glibc-langpack-de`
- `glibc-langpack-doi`
- `glibc-langpack-dsb`
- `glibc-langpack-dv`
- `glibc-langpack-dz`
- `glibc-langpack-el`
- `glibc-langpack-en`
- `glibc-langpack-eo`
- `glibc-langpack-es`
- `glibc-langpack-et`
- `glibc-langpack-eu`
- `glibc-langpack-fa`
- `glibc-langpack-ff`
- `glibc-langpack-fi`
- `glibc-langpack-fil`
- `glibc-langpack-fo`
- `glibc-langpack-fr`
- `glibc-langpack-fur`
- `glibc-langpack-fy`
- `glibc-langpack-ga`
- `glibc-langpack-gd`
- `glibc-langpack-gez`
- `glibc-langpack-gl`
- `glibc-langpack-gu`
- `glibc-langpack-gv`
- `glibc-langpack-ha`
- `glibc-langpack-hak`
- `glibc-langpack-he`
- `glibc-langpack-hi`
- `glibc-langpack-hif`
- `glibc-langpack-hne`
- `glibc-langpack-hr`
- `glibc-langpack-hsb`
- `glibc-langpack-ht`
- `glibc-langpack-hu`
- `glibc-langpack-hy`
- `glibc-langpack-ia`
- `glibc-langpack-id`
- `glibc-langpack-ig`
- `glibc-langpack-ik`
- `glibc-langpack-is`
- `glibc-langpack-it`
- `glibc-langpack-iu`
- `glibc-langpack-ja`
- `glibc-langpack-ka`
- `glibc-langpack-kab`
- `glibc-langpack-kk`
- `glibc-langpack-kl`
- `glibc-langpack-km`
- `glibc-langpack-kn`
- `glibc-langpack-ko`
- `glibc-langpack-kok`
- `glibc-langpack-ks`
- `glibc-langpack-ku`
- `glibc-langpack-kw`
- `glibc-langpack-ky`
- `glibc-langpack-lb`
- `glibc-langpack-lg`
- `glibc-langpack-li`
- `glibc-langpack-lij`
- `glibc-langpack-ln`
- `glibc-langpack-lo`
- `glibc-langpack-lt`
- `glibc-langpack-lv`
- `glibc-langpack-lzh`
- `glibc-langpack-mag`
- `glibc-langpack-mai`
- `glibc-langpack-mfe`
- `glibc-langpack-mg`
- `glibc-langpack-mhr`
- `glibc-langpack-mi`
- `glibc-langpack-miq`
- `glibc-langpack-mjw`
- `glibc-langpack-mk`
- `glibc-langpack-ml`
- `glibc-langpack-mn`
- `glibc-langpack-mni`
- `glibc-langpack-mr`
- `glibc-langpack-ms`
- `glibc-langpack-mt`
- `glibc-langpack-my`
- `glibc-langpack-nan`
- `glibc-langpack-nb`
- `glibc-langpack-nds`
- `glibc-langpack-ne`
- `glibc-langpack-nhn`
- `glibc-langpack-niu`
- `glibc-langpack-nl`
- `glibc-langpack-nn`
- `glibc-langpack-nr`
- `glibc-langpack-nso`
- `glibc-langpack-oc`
- `glibc-langpack-om`
- `glibc-langpack-or`
- `glibc-langpack-os`
- `glibc-langpack-pa`
- `glibc-langpack-pap`
- `glibc-langpack-pl`
- `glibc-langpack-ps`
- `glibc-langpack-pt`
- `glibc-langpack-quz`
- `glibc-langpack-raj`
- `glibc-langpack-ro`
- `glibc-langpack-ru`
- `glibc-langpack-rw`
- `glibc-langpack-sa`
- `glibc-langpack-sah`
- `glibc-langpack-sat`
- `glibc-langpack-sc`
- `glibc-langpack-sd`
- `glibc-langpack-se`
- `glibc-langpack-sgs`
- `glibc-langpack-shn`
- `glibc-langpack-shs`
- `glibc-langpack-si`
- `glibc-langpack-sid`
- `glibc-langpack-sk`
- `glibc-langpack-sl`
- `glibc-langpack-sm`
- `glibc-langpack-so`
- `glibc-langpack-sq`
- `glibc-langpack-sr`
- `glibc-langpack-ss`
- `glibc-langpack-st`
- `glibc-langpack-sv`
- `glibc-langpack-sw`
- `glibc-langpack-szl`
- `glibc-langpack-ta`
- `glibc-langpack-tcy`
- `glibc-langpack-te`
- `glibc-langpack-tg`
- `glibc-langpack-th`
- `glibc-langpack-the`
- `glibc-langpack-ti`
- `glibc-langpack-tig`
- `glibc-langpack-tk`
- `glibc-langpack-tl`
- `glibc-langpack-tn`
- `glibc-langpack-to`
- `glibc-langpack-tpi`
- `glibc-langpack-tr`
- `glibc-langpack-ts`
- `glibc-langpack-tt`
- `glibc-langpack-ug`
- `glibc-langpack-uk`
- `glibc-langpack-unm`
- `glibc-langpack-ur`
- `glibc-langpack-uz`
- `glibc-langpack-ve`
- `glibc-langpack-vi`
- `glibc-langpack-wa`
- `glibc-langpack-wae`
- `glibc-langpack-wal`
- `glibc-langpack-wo`
- `glibc-langpack-xh`
- `glibc-langpack-yi`
- `glibc-langpack-yo`
- `glibc-langpack-yue`
- `glibc-langpack-yuw`
- `glibc-langpack-zh`
- `glibc-langpack-zu`
- `glibc-locale-source`
- `glibc-minimal-langpack`
- `grub2-common`
- `grub2-efi-aa64-modules`
- `grub2-efi-ia32`
- `grub2-efi-ia32-cdboot`
- `grub2-efi-ia32-modules`
- `grub2-efi-x64`
- `grub2-efi-x64-cdboot`
- `grub2-efi-x64-modules`
- `grub2-pc`
- `grub2-pc-modules`
- `grub2-tools`
- `grub2-tools-efi`
- `grub2-tools-extra`
- `grub2-tools-minimal`
- `grubby`
- `iptables`
- `iptables-arptables`
- `iptables-devel`
- `iptables-ebtables`
- `iptables-libs`
- `iptables-services`
- `iptables-utils`
- `iscsi-initiator-utils`
- `iscsi-initiator-utils-iscsiuio`
- `iwl1000-firmware`
- `iwl100-firmware`
- `iwl105-firmware`
- `iwl135-firmware`
- `iwl2000-firmware`
- `iwl2030-firmware`
- `iwl3160-firmware`
- `iwl3945-firmware`
- `iwl4965-firmware`
- `iwl5000-firmware`
- `iwl5150-firmware`
- `iwl6000-firmware`
- `iwl6000g2a-firmware`
- `iwl6000g2b-firmware`
- `iwl6050-firmware`
- `iwl7260-firmware`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `kmod-libs`
- `kmod-redhat-oracleasm`
- `ksc`
- `libasan`
- `libatomic`
- `libatomic-static`
- `libdnf`
- `libertas-sd8686-firmware`
- `libertas-sd8787-firmware`
- `libertas-usb8388-firmware`
- `libertas-usb8388-olpc-firmware`
- `libgcc`
- `libgfortran`
- `libgomp`
- `libgomp-offload-nvptx`
- `libipa_hbac`
- `libitm`
- `libkcapi`
- `libkcapi-hmaccalc`
- `liblsan`
- `libnsl`
- `libquadmath`
- `libreport-filesystem`
- `libsss_autofs`
- `libsss_certmap`
- `libsss_idmap`
- `libsss_nss_idmap`
- `libsss_simpleifp`
- `libsss_sudo`
- `libstdc++`
- `libtsan`
- `libubsan`
- `libxml2`
- `libxslt`
- `linux-firmware`
- `mcelog`
- `microcode_ctl`
- `mokutil`
- `mozjs52`
- `mozjs60`
- `nscd`
- `nss_db`
- `ntsysv`
- `nvmetcli`
- `opa-address-resolution`
- `opa-basic-tools`
- `opa-fastfabric`
- `opa-fm`
- `opa-libopamgt`
- `OpenIPMI`
- `OpenIPMI-lanserv`
- `OpenIPMI-libs`
- `OpenIPMI-perl`
- `oracle-backgrounds`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`
- `oracle-logos-httpd`
- `oracle-logos-ipa`
- `os-prober`
- `parted`
- `platform-python`
- `policycoreutils`
- `policycoreutils-dbus`
- `policycoreutils-devel`
- `policycoreutils-newrole`
- `policycoreutils-python-utils`
- `policycoreutils-restorecond`
- `polkit`
- `polkit-devel`
- `polkit-docs`
- `polkit-libs`
- `python3-boom`
- `python3-configshell`
- `python3-firewall`
- `python3-hawkey`
- `python3-iscsi-initiator-utils`
- `python3-libdnf`
- `python3-libipa_hbac`
- `python3-libs`
- `python3-libsss_nss_idmap`
- `python3-libxml2`
- `python3-openipmi`
- `python3-policycoreutils`
- `python3-rtslib`
- `python3-sss`
- `python3-sssdconfig`
- `python3-sss-murmur`
- `python3-test`
- `python3-urllib3`
- `redhat-indexhtml`
- `redhat-release`
- `sanlock-lib`
- `selinux-policy`
- `selinux-policy-devel`
- `selinux-policy-doc`
- `selinux-policy-minimum`
- `selinux-policy-mls`
- `selinux-policy-sandbox`
- `selinux-policy-targeted`
- `shim-ia32`
- `shim-x64`
- `sos`
- `sos-audit`
- `sssd`
- `sssd-ad`
- `sssd-client`
- `sssd-common`
- `sssd-common-pac`
- `sssd-dbus`
- `sssd-ipa`
- `sssd-kcm`
- `sssd-krb5`
- `sssd-krb5-common`
- `sssd-ldap`
- `sssd-libwbclient`
- `sssd-nfs-idmap`
- `sssd-polkit-rules`
- `sssd-proxy`
- `sssd-tools`
- `sssd-winbind-idmap`
- `systemd`
- `systemd-container`
- `systemd-devel`
- `systemd-journal-remote`
- `systemd-libs`
- `systemd-pam`
- `systemd-tests`
- `systemd-udev`
- `target-restore`
- `tuned`
- `tuned-profiles-atomic`
- `tuned-profiles-compat`
- `tuned-profiles-cpu-partitioning`
- `tuned-profiles-mssql`
- `tuned-profiles-oracle`
- `vim-minimal`

#### Modified Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `crash-devel`
- `cups-filters-devel`
- `gcc-plugin-devel`
- `glibc-benchtests`
- `glibc-nss-devel`
- `glibc-static`
- `guile-devel`
- `iscsi-initiator-utils-devel`
- `kmod-devel`
- `libblockdev-crypto-devel`
- `libblockdev-devel`
- `libblockdev-fs-devel`
- `libblockdev-loop-devel`
- `libblockdev-lvm-devel`
- `libblockdev-mdraid-devel`
- `libblockdev-part-devel`
- `libblockdev-swap-devel`
- `libblockdev-utils-devel`
- `libblockdev-vdo-devel`
- `libbytesize-devel`
- `libcephfs2`
- `libcephfs-devel`
- `librados-devel`
- `libradosstriper1`
- `libradosstriper-devel`
- `librbd-devel`
- `libreoffice-sdk`
- `libreoffice-sdk-doc`
- `libsss_nss_idmap-devel`
- `libstdc++-static`
- `mozjs52-devel`
- `mozjs60-devel`
- `nss_hesiod`
- `ocaml-libguestfs`
- `ocaml-libguestfs-devel`
- `OpenIPMI-devel`
- `openscap-engine-sce-devel`
- `PackageKit-glib-devel`
- `parted-devel`
- `sanlock-devel`
- `sblim-cmpi-devel`
- `shim-unsigned-ia32`
- `shim-unsigned-x64`
- `tog-pegasus-devel`

#### Modified AppStream Binary Packages

The following binary packages from the AppStream upstream release have been modified:

- `abrt`
- `abrt-addon-ccpp`
- `abrt-addon-coredump-helper`
- `abrt-addon-kerneloops`
- `abrt-addon-pstoreoops`
- `abrt-addon-vmcore`
- `abrt-addon-xorg`
- `abrt-cli`
- `abrt-cli-ng`
- `abrt-console-notification`
- `abrt-dbus`
- `abrt-desktop`
- `abrt-gui`
- `abrt-gui-libs`
- `abrt-java-connector`
- `abrt-libs`
- `abrt-plugin-machine-id`
- `abrt-plugin-sosreport`
- `abrt-tui`
- `adwaita-gtk2-theme`
- `anaconda`
- `anaconda-core`
- `anaconda-dracut`
- `anaconda-gui`
- `anaconda-install-env-deps`
- `anaconda-tui`
- `anaconda-user-help`
- `anaconda-widgets`
- `aspnetcore-runtime-3.0`
- `aspnetcore-runtime-3.1`
- `aspnetcore-targeting-pack-3.0`
- `aspnetcore-targeting-pack-3.1`
- `authd`
- `autocorr-af`
- `autocorr-bg`
- `autocorr-ca`
- `autocorr-cs`
- `autocorr-da`
- `autocorr-de`
- `autocorr-en`
- `autocorr-es`
- `autocorr-fa`
- `autocorr-fi`
- `autocorr-fr`
- `autocorr-ga`
- `autocorr-hr`
- `autocorr-hu`
- `autocorr-is`
- `autocorr-it`
- `autocorr-ja`
- `autocorr-ko`
- `autocorr-lb`
- `autocorr-lt`
- `autocorr-mn`
- `autocorr-nl`
- `autocorr-pl`
- `autocorr-pt`
- `autocorr-ro`
- `autocorr-ru`
- `autocorr-sk`
- `autocorr-sl`
- `autocorr-sr`
- `autocorr-sv`
- `autocorr-tr`
- `autocorr-vi`
- `autocorr-zh`
- `binutils-devel`
- `blivet-data`
- `buildah`
- `buildah-tests`
- `clang`
- `clang-analyzer`
- `clang-devel`
- `clang-libs`
- `clang-tools-extra`
- `cloud-init`
- `cockpit-composer`
- `cockpit-machines`
- `cockpit-packagekit`
- `cockpit-pcp`
- `cockpit-session-recording`
- `cockpit-storaged`
- `compat-libgfortran-48`
- `compat-libpthread-nonshared`
- `composer-cli`
- `containernetworking-plugins`
- `containers-common`
- `cpp`
- `crash`
- `cups-filters`
- `cups-filters-libs`
- `dbus-devel`
- `dbus-x11`
- `delve`
- `dnf-plugin-spacewalk`
- `dotnet`
- `dotnet-apphost-pack-3.0`
- `dotnet-apphost-pack-3.1`
- `dotnet-host`
- `dotnet-hostfxr-3.0`
- `dotnet-hostfxr-3.1`
- `dotnet-runtime-3.0`
- `dotnet-runtime-3.1`
- `dotnet-sdk-3.0`
- `dotnet-sdk-3.1`
- `dotnet-targeting-pack-3.0`
- `dotnet-targeting-pack-3.1`
- `dotnet-templates-3.0`
- `dotnet-templates-3.1`
- `eclipse-ecf-core`
- `eclipse-ecf-runtime`
- `eclipse-emf-core`
- `eclipse-emf-runtime`
- `eclipse-emf-xsd`
- `eclipse-equinox-osgi`
- `eclipse-jdt`
- `eclipse-p2-discovery`
- `eclipse-pde`
- `eclipse-platform`
- `eclipse-swt`
- `efi-srpm-macros`
- `firefox`
- `firewall-applet`
- `firewall-config`
- `gcc`
- `gcc-c++`
- `gcc-gdb-plugin`
- `gcc-gfortran`
- `gcc-offload-nvptx`
- `gcc-toolset-10-gcc`
- `gdb`
- `gdb-doc`
- `gdb-gdbserver`
- `gdb-headless`
- `git-clang-format`
- `glibc-utils`
- `gnome-boxes`
- `gnome-themes-standard`
- `golang`
- `golang-bin`
- `golang-docs`
- `golang-misc`
- `golang-race`
- `golang-src`
- `golang-tests`
- `grafana-pcp`
- `guile`
- `httpd`
- `httpd-devel`
- `httpd-filesystem`
- `httpd-manual`
- `httpd-tools`
- `icedtea-web`
- `icedtea-web-javadoc`
- `initial-setup`
- `initial-setup-gui`
- `ipa-client`
- `ipa-client-common`
- `ipa-client-epn`
- `ipa-client-samba`
- `ipa-common`
- `ipa-python-compat`
- `ipa-server`
- `ipa-server-common`
- `ipa-server-dns`
- `ipa-server-trust-ad`
- `kernel-rpm-macros`
- `ksh`
- `libblockdev`
- `libblockdev-crypto`
- `libblockdev-dm`
- `libblockdev-fs`
- `libblockdev-kbd`
- `libblockdev-loop`
- `libblockdev-lvm`
- `libblockdev-lvm-dbus`
- `libblockdev-mdraid`
- `libblockdev-mpath`
- `libblockdev-nvdimm`
- `libblockdev-part`
- `libblockdev-plugins-all`
- `libblockdev-swap`
- `libblockdev-utils`
- `libblockdev-vdo`
- `libcmpiCppImpl0`
- `libguestfs`
- `libguestfs-bash-completion`
- `libguestfs-benchmarking`
- `libguestfs-devel`
- `libguestfs-gfs2`
- `libguestfs-gobject`
- `libguestfs-gobject-devel`
- `libguestfs-inspect-icons`
- `libguestfs-java`
- `libguestfs-java-devel`
- `libguestfs-javadoc`
- `libguestfs-man-pages-ja`
- `libguestfs-man-pages-uk`
- `libguestfs-rescue`
- `libguestfs-rsync`
- `libguestfs-tools`
- `libguestfs-tools-c`
- `libguestfs-xfs`
- `libitm-devel`
- `libquadmath-devel`
- `librados2`
- `librbd1`
- `libreoffice-base`
- `libreoffice-calc`
- `libreoffice-core`
- `libreoffice-data`
- `libreoffice-draw`
- `libreoffice-emailmerge`
- `libreoffice-filters`
- `libreoffice-gdb-debug-support`
- `libreoffice-graphicfilter`
- `libreoffice-gtk3`
- `libreoffice-help-ar`
- `libreoffice-help-bg`
- `libreoffice-help-bn`
- `libreoffice-help-ca`
- `libreoffice-help-cs`
- `libreoffice-help-da`
- `libreoffice-help-de`
- `libreoffice-help-dz`
- `libreoffice-help-el`
- `libreoffice-help-en`
- `libreoffice-help-es`
- `libreoffice-help-et`
- `libreoffice-help-eu`
- `libreoffice-help-fi`
- `libreoffice-help-fr`
- `libreoffice-help-gl`
- `libreoffice-help-gu`
- `libreoffice-help-he`
- `libreoffice-help-hi`
- `libreoffice-help-hr`
- `libreoffice-help-hu`
- `libreoffice-help-id`
- `libreoffice-help-it`
- `libreoffice-help-ja`
- `libreoffice-help-ko`
- `libreoffice-help-lt`
- `libreoffice-help-lv`
- `libreoffice-help-nb`
- `libreoffice-help-nl`
- `libreoffice-help-nn`
- `libreoffice-help-pl`
- `libreoffice-help-pt-BR`
- `libreoffice-help-pt-PT`
- `libreoffice-help-ro`
- `libreoffice-help-ru`
- `libreoffice-help-si`
- `libreoffice-help-sk`
- `libreoffice-help-sl`
- `libreoffice-help-sv`
- `libreoffice-help-ta`
- `libreoffice-help-tr`
- `libreoffice-help-uk`
- `libreoffice-help-zh-Hans`
- `libreoffice-help-zh-Hant`
- `libreoffice-impress`
- `libreofficekit`
- `libreoffice-langpack-af`
- `libreoffice-langpack-ar`
- `libreoffice-langpack-as`
- `libreoffice-langpack-bg`
- `libreoffice-langpack-bn`
- `libreoffice-langpack-br`
- `libreoffice-langpack-ca`
- `libreoffice-langpack-cs`
- `libreoffice-langpack-cy`
- `libreoffice-langpack-da`
- `libreoffice-langpack-de`
- `libreoffice-langpack-dz`
- `libreoffice-langpack-el`
- `libreoffice-langpack-en`
- `libreoffice-langpack-es`
- `libreoffice-langpack-et`
- `libreoffice-langpack-eu`
- `libreoffice-langpack-fa`
- `libreoffice-langpack-fi`
- `libreoffice-langpack-fr`
- `libreoffice-langpack-ga`
- `libreoffice-langpack-gl`
- `libreoffice-langpack-gu`
- `libreoffice-langpack-he`
- `libreoffice-langpack-hi`
- `libreoffice-langpack-hr`
- `libreoffice-langpack-hu`
- `libreoffice-langpack-id`
- `libreoffice-langpack-it`
- `libreoffice-langpack-ja`
- `libreoffice-langpack-kk`
- `libreoffice-langpack-kn`
- `libreoffice-langpack-ko`
- `libreoffice-langpack-lt`
- `libreoffice-langpack-lv`
- `libreoffice-langpack-mai`
- `libreoffice-langpack-ml`
- `libreoffice-langpack-mr`
- `libreoffice-langpack-nb`
- `libreoffice-langpack-nl`
- `libreoffice-langpack-nn`
- `libreoffice-langpack-nr`
- `libreoffice-langpack-nso`
- `libreoffice-langpack-or`
- `libreoffice-langpack-pa`
- `libreoffice-langpack-pl`
- `libreoffice-langpack-pt-BR`
- `libreoffice-langpack-pt-PT`
- `libreoffice-langpack-ro`
- `libreoffice-langpack-ru`
- `libreoffice-langpack-si`
- `libreoffice-langpack-sk`
- `libreoffice-langpack-sl`
- `libreoffice-langpack-sr`
- `libreoffice-langpack-ss`
- `libreoffice-langpack-st`
- `libreoffice-langpack-sv`
- `libreoffice-langpack-ta`
- `libreoffice-langpack-te`
- `libreoffice-langpack-th`
- `libreoffice-langpack-tn`
- `libreoffice-langpack-tr`
- `libreoffice-langpack-ts`
- `libreoffice-langpack-uk`
- `libreoffice-langpack-ve`
- `libreoffice-langpack-xh`
- `libreoffice-langpack-zh-Hans`
- `libreoffice-langpack-zh-Hant`
- `libreoffice-langpack-zu`
- `libreoffice-math`
- `libreoffice-ogltrans`
- `libreoffice-opensymbol-fonts`
- `libreoffice-pdfimport`
- `libreoffice-pyuno`
- `libreoffice-ure`
- `libreoffice-ure-common`
- `libreoffice-wiki-publisher`
- `libreoffice-writer`
- `libreoffice-x11`
- `libreoffice-xsltfilter`
- `libreport`
- `libreport-anaconda`
- `libreport-cli`
- `libreport-gtk`
- `libreport-newt`
- `libreport-plugin-bugzilla`
- `libreport-plugin-kerneloops`
- `libreport-plugin-logger`
- `libreport-plugin-mailx`
- `libreport-plugin-reportuploader`
- `libreport-plugin-ureport`
- `libreport-web`
- `libreswan`
- `libstdc++-devel`
- `libstdc++-docs`
- `libvirt`
- `libvirt-admin`
- `libvirt-bash-completion`
- `libvirt-client`
- `libvirt-daemon`
- `libvirt-daemon-config-network`
- `libvirt-daemon-config-nwfilter`
- `libvirt-daemon-driver-interface`
- `libvirt-daemon-driver-network`
- `libvirt-daemon-driver-nodedev`
- `libvirt-daemon-driver-nwfilter`
- `libvirt-daemon-driver-qemu`
- `libvirt-daemon-driver-secret`
- `libvirt-daemon-driver-storage`
- `libvirt-daemon-driver-storage-core`
- `libvirt-daemon-driver-storage-disk`
- `libvirt-daemon-driver-storage-gluster`
- `libvirt-daemon-driver-storage-iscsi`
- `libvirt-daemon-driver-storage-iscsi-direct`
- `libvirt-daemon-driver-storage-logical`
- `libvirt-daemon-driver-storage-mpath`
- `libvirt-daemon-driver-storage-rbd`
- `libvirt-daemon-driver-storage-scsi`
- `libvirt-daemon-kvm`
- `libvirt-devel`
- `libvirt-docs`
- `libvirt-libs`
- `libvirt-lock-sanlock`
- `libvirt-nss`
- `libxml2-devel`
- `libxslt-devel`
- `llvm`
- `llvm-devel`
- `llvm-doc`
- `llvm-googletest`
- `llvm-libs`
- `llvm-static`
- `llvm-test`
- `llvm-toolset`
- `lorax`
- `lorax-composer`
- `lorax-lmc-novirt`
- `lorax-lmc-virt`
- `lorax-templates-generic`
- `lorax-templates-rhel`
- `lua-guestfs`
- `mecab-ipadic`
- `mecab-ipadic-EUCJP`
- `mod_ldap`
- `mod_proxy_html`
- `mod_session`
- `mod_ssl`
- `nbdkit`
- `nbdkit-bash-completion`
- `nbdkit-basic-filters`
- `nbdkit-basic-plugins`
- `nbdkit-curl-plugin`
- `nbdkit-devel`
- `nbdkit-example-plugins`
- `nbdkit-gzip-plugin`
- `nbdkit-linuxdisk-plugin`
- `nbdkit-python-plugin`
- `nbdkit-server`
- `nbdkit-ssh-plugin`
- `nbdkit-vddk-plugin`
- `nbdkit-xz-filter`
- `netstandard-targeting-pack-2.1`
- `nginx`
- `nginx-all-modules`
- `nginx-filesystem`
- `nginx-mod-http-image-filter`
- `nginx-mod-http-perl`
- `nginx-mod-http-xslt-filter`
- `nginx-mod-mail`
- `nginx-mod-stream`
- `openchange`
- `openscap`
- `openscap-devel`
- `openscap-engine-sce`
- `openscap-python3`
- `openscap-scanner`
- `openscap-utils`
- `open-vm-tools`
- `open-vm-tools-desktop`
- `open-vm-tools-sdmp`
- `osinfo-db`
- `pacemaker-cluster-libs`
- `pacemaker-libs`
- `pacemaker-schemas`
- `PackageKit`
- `PackageKit-command-not-found`
- `PackageKit-cron`
- `PackageKit-glib`
- `PackageKit-gstreamer-plugin`
- `PackageKit-gtk3-module`
- `perl-Sys-Guestfs`
- `perl-XML-Parser`
- `pesign`
- `pki-base`
- `pki-base-java`
- `pki-ca`
- `pki-kra`
- `pki-server`
- `pki-symkey`
- `pki-tools`
- `platform-python`
- `platform-python-debug`
- `platform-python-devel`
- `plymouth`
- `plymouth-core-libs`
- `plymouth-graphics-libs`
- `plymouth-plugin-fade-throbber`
- `plymouth-plugin-label`
- `plymouth-plugin-script`
- `plymouth-plugin-space-flares`
- `plymouth-plugin-throbgress`
- `plymouth-plugin-two-step`
- `plymouth-scripts`
- `plymouth-system-theme`
- `plymouth-theme-charge`
- `plymouth-theme-fade-in`
- `plymouth-theme-script`
- `plymouth-theme-solar`
- `plymouth-theme-spinfinity`
- `plymouth-theme-spinner`
- `podman`
- `podman-docker`
- `podman-remote`
- `podman-tests`
- `policycoreutils-gui`
- `policycoreutils-sandbox`
- `pykickstart`
- `python2`
- `python2-backports`
- `python2-debug`
- `python2-devel`
- `python2-libs`
- `python2-test`
- `python2-tkinter`
- `python2-tools`
- `python2-urllib3`
- `python38-urllib3`
- `python3-abrt`
- `python3-abrt-addon`
- `python3-abrt-container-addon`
- `python3-abrt-doc`
- `python3-blivet`
- `python3-clang`
- `python3-dnf-plugin-spacewalk`
- `python3-idle`
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-kickstart`
- `python3-libguestfs`
- `python3-libreport`
- `python3-pki`
- `python3-rhncfg`
- `python3-rhncfg-actions`
- `python3-rhncfg-client`
- `python3-rhncfg-management`
- `python3-rhn-check`
- `python3-rhn-client-tools`
- `python3-rhnlib`
- `python3-rhnpush`
- `python3-rhn-setup`
- `python3-rhn-setup-gnome`
- `python3-sanlock`
- `python3-spacewalk-backend-libs`
- `python3-spacewalk-oscap`
- `python3-spacewalk-usix`
- `python3-test`
- `python3-tkinter`
- `rear`
- `redhat-lsb`
- `redhat-lsb-core`
- `redhat-lsb-cxx`
- `redhat-lsb-desktop`
- `redhat-lsb-languages`
- `redhat-lsb-printing`
- `redhat-lsb-submod-multimedia`
- `redhat-lsb-submod-security`
- `redhat-rpm-config`
- `rhel-system-roles`
- `rhncfg`
- `rhncfg-actions`
- `rhncfg-client`
- `rhncfg-management`
- `rhn-check`
- `rhn-client-tools`
- `rhn-custom-info`
- `rhnlib`
- `rhnpush`
- `rhnsd`
- `rhn-setup`
- `rhn-setup-gnome`
- `rpmdevtools`
- `rsyslog`
- `rsyslog-crypto`
- `rsyslog-doc`
- `rsyslog-elasticsearch`
- `rsyslog-gnutls`
- `rsyslog-gssapi`
- `rsyslog-kafka`
- `rsyslog-mmaudit`
- `rsyslog-mmjsonparse`
- `rsyslog-mmkubernetes`
- `rsyslog-mmnormalize`
- `rsyslog-mmsnmptrapd`
- `rsyslog-mysql`
- `rsyslog-omamqp1`
- `rsyslog-pgsql`
- `rsyslog-relp`
- `rsyslog-snmp`
- `rsyslog-udpspoof`
- `ruby-libguestfs`
- `sanlk-reset`
- `sanlock`
- `scap-security-guide`
- `scap-security-guide-doc`
- `scap-workbench`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `setroubleshoot-server`
- `skopeo`
- `skopeo-tests`
- `sos-collector`
- `spacewalk-oscap`
- `spacewalk-remote-utils`
- `spacewalk-usix`
- `spice-streaming-agent`
- `systemtap`
- `systemtap-client`
- `systemtap-devel`
- `systemtap-exporter`
- `systemtap-initscript`
- `systemtap-runtime`
- `systemtap-runtime-java`
- `systemtap-runtime-python3`
- `systemtap-runtime-virtguest`
- `systemtap-runtime-virthost`
- `systemtap-sdt-devel`
- `systemtap-server`
- `thunderbird`
- `tog-pegasus`
- `tog-pegasus-libs`
- `tuned-gtk`
- `tuned-utils`
- `tuned-utils-systemtap`
- `vim-common`
- `vim-enhanced`
- `vim-filesystem`
- `vim-X11`
- `virt-dib`
- `virt-install`
- `virt-manager`
- `virt-manager-common`
- `virt-p2v-maker`
- `virt-v2v`
- `WALinuxAgent`
- `wget`
- `xsane`
- `xsane-common`
- `xsane-gimp`

#### Removed BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been removed:

- `NetworkManager-config-connectivity-redhat`
- `dnf-plugin-subscription-manager`
- `grub2-ppc64le-modules`
- `kpatch`
- `kpatch-dnf`
- `python3-subscription-manager-rhsm`
- `python3-syspurpose`
- `redhat-logos`
- `redhat-logos-httpd`
- `redhat-release-eula`
- `rhsm-icons`
- `subscription-manager`
- `subscription-manager-cockpit`
- `subscription-manager-plugin-ostree`
- `subscription-manager-rhsm-certificates`

#### Removed AppStream Binary Packages

The following binary packages from the AppStream upstream release have been removed:

- `insights-client`
- `libreport-plugin-rhtsupport`
- `libreport-rhel`
- `libreport-rhel-anaconda-bugzilla`
- `libreport-rhel-bugzilla`
- `redhat-backgrounds`
- `redhat-logos-ipa`
- `redhat-support-lib-python`
- `redhat-support-tool`
- `rhc`
- `rhc-worker-playbook`
- `rhsm-gtk`
- `rt-tests`
- `spice-client-win-x64`
- `spice-client-win-x86`
- `spice-qxl-wddm-dod`
- `spice-vdagent-win-x64`
- `spice-vdagent-win-x86`
- `subscription-manager-initial-setup-addon`
- `subscription-manager-migration`
- `subscription-manager-migration-data`
- `toolbox`
- `toolbox-tests`
- `virtio-win`
- `virt-who`

#### Removed CodeReady Linux Builder Binary Packages

No binary packages were removed from CodeReady Linux Builder by Oracle.

### Changes to Source Packages

This section contains information about the removed, modified, and new source packages in this release. For information about the binary package changes, see [Changes to Binary Packages](ol8-PackageChangesfromtheUpstreamRelease.html#ol8-packages-binary) .

#### Added Source Packages for BaseOS by Oracle

The following source packages have been added to the BaseOS by Oracle:

- `bcache-tools`
- `btrfs-progs`
- `dtrace`
- `kernel-uek`
- `ocfs2-tools`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`

#### Added Source Packages for AppStream by Oracle

The following source packages have been added to AppStream by Oracle:

- `dtrace`

#### Modified BaseOS Source Packages

The following source packages from the BaseOS upstream release have been modified:

- `autofs`
- `binutils`
- `boom-boot`
- `chkconfig`
- `chrony`
- `cockpit`
- `coreutils`
- `dbus`
- `dracut`
- `efibootmgr`
- `efi-rpm-macros`
- `firewalld`
- `fuse`
- `fwupd`
- `fwupdate`
- `gcc`
- `glibc`
- `grub2`
- `grubby`
- `iptables`
- `iscsi-initiator-utils`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `kmod-redhat-oracleasm`
- `ksc`
- `libdnf`
- `libkcapi`
- `libreport`
- `libxml2`
- `libxslt`
- `linux-firmware`
- `mcelog`
- `microcode_ctl`
- `mokutil`
- `mozjs52`
- `mozjs60`
- `nvmetcli`
- `opa-ff`
- `opa-fm`
- `OpenIPMI`
- `os-prober`
- `parted`
- `policycoreutils`
- `polkit`
- `python3`
- `python-configshell`
- `python-rtslib`
- `python-urllib3`
- `redhat-indexhtml`
- `redhat-release`
- `sanlock`
- `selinux-policy`
- `shim`
- `sos`
- `sssd`
- `systemd`
- `tuned`
- `vim`

#### Modified AppStream Source Packages

The following source packages from the AppStream upstream release have been modified:

- `abrt`
- `abrt-java-connector`
- `anaconda`
- `anaconda-user-help`
- `authd`
- `binutils`
- `buildah`
- `ceph`
- `clang`
- `cloud-init`
- `cockpit-appstream`
- `cockpit-composer`
- `cockpit-session-recording`
- `compat-libgfortran-48`
- `containernetworking-plugins`
- `crash`
- `cups-filters`
- `dbus`
- `delve`
- `dnf-plugin-spacewalk`
- `dotnet3.0`
- `dotnet3.1`
- `eclipse`
- `eclipse-ecf`
- `eclipse-emf`
- `efi-rpm-macros`
- `firefox`
- `firewalld`
- `gcc`
- `gcc-toolset-10-gcc`
- `gdb`
- `glibc`
- `gnome-boxes`
- `gnome-themes-standard`
- `golang`
- `grafana-pcp`
- `guile`
- `httpd`
- `icedtea-web`
- `initial-setup`
- `ipa`
- `ksh`
- `libblockdev`
- `libguestfs`
- `libreoffice`
- `libreport`
- `libreswan`
- `libvirt`
- `libxml2`
- `libxslt`
- `llvm`
- `lorax`
- `lorax-templates-rhel`
- `mecab-ipadic`
- `nbdkit`
- `nginx`
- `openchange`
- `openscap`
- `open-vm-tools`
- `osinfo-db`
- `pacemaker`
- `PackageKit`
- `perl-XML-Parser`
- `pesign`
- `pki-core`
- `plymouth`
- `podman`
- `policycoreutils`
- `pykickstart`
- `python2`
- `python3`
- `python-backports`
- `python-blivet`
- `python-urllib3`
- `rear`
- `redhat-lsb`
- `redhat-rpm-config`
- `rhel-system-roles`
- `rhncfg`
- `rhn-client-tools`
- `rhn-custom-info`
- `rhnlib`
- `rhnpush`
- `rhnsd`
- `rpmdevtools`
- `rsyslog`
- `sanlock`
- `sblim-cmpi-devel`
- `scap-security-guide`
- `scap-workbench`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `skopeo`
- `sos-collector`
- `spacewalk-backend`
- `spacewalk-oscap`
- `spacewalk-remote-utils`
- `spacewalk-usix`
- `spice-streaming-agent`
- `systemtap`
- `thunderbird`
- `tog-pegasus`
- `tuned`
- `vim`
- `virt-manager`
- `virt-p2v`
- `WALinuxAgent`
- `wget`
- `xsane`

#### Modified Source Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `ceph`
- `crash`
- `cups-filters`
- `gcc`
- `glibc`
- `guile`
- `iscsi-initiator-utils`
- `kmod`
- `libblockdev`
- `libguestfs`
- `libreoffice`
- `libvirt`
- `mozjs52`
- `mozjs60`
- `OpenIPMI`
- `openscap`
- `PackageKit`
- `parted`
- `sanlock`
- `sblim-cmpi-devel`
- `sssd`
- `tog-pegasus`

#### Removed BaseOS Source Packages

The following source packages from the BaseOS upstream release have been removed:

- `kpatch`
- `redhat-logos`
- `subscription-manager`
- `subscription-manager-migration-data`

#### Removed AppStream Source Packages

The following source packages from the AppStream upstream release have been removed:

- `insights-client`
- `redhat-support-lib-python`
- `redhat-support-tool`
- `rhc`
- `rhc-worker-playbook`
- `rt-tests`
- `spice-qxl-wddm-dod`
- `subscription-manager-migration-data`
- `toolbox`
- `virtio-win`
- `virt-who`