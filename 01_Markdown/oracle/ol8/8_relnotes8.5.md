---
title: "Release Notes for Oracle Linux 8.5"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.5"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol8"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

Release Notes for Oracle Linux 8.5

F48681-10

November 2022

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 8 Release Notes for Oracle Linux 8.5

F48681-10

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2021, 2022, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.5/ol8.5-Preface.html -->

[Oracle Linux 8: Release Notes for Oracle Linux
8.5](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.5/) provides information about the new
features and known issues in the Oracle Linux 8.5 release. The information applies to
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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.5/ol8-AboutOracleLinux8.html -->

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

For the x86\_64 platform, Oracle Linux 8.5 ships with the following default kernel packages:

- `kernel-4.18.0-348.el8`: (Red Hat Compatible Kernel (RHCK))
- `kernel-uek-5.4.17-2136.300.7.el8uek`: (Unbreakable Enterprise
  Kernel Release 6 (UEK R6))

  For new installations, the UEK kernel is automatically enabled and installed. It also
  becomes the default kernel on first boot.

  Starting with the Oracle Linux 8.5 release, Unbreakable Enterprise Kernel Release 7 (UEK
  R7) is also available as an additional installation option.

Note:

For the 64-bit Arm (aarch64) platform, Oracle Linux ships only with the UEK kernel.

The Oracle Linux release is tested as a bundle, as shipped on the installation media image.
When installed from the installation media image, the kernel's version included in the image
is the minimum version that is supported. Downgrading kernel packages is not supported, unless
recommended by Oracle Support.

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

Oracle Linux 8 releases earlier than Oracle Linux 8.7 ship with UEK R6 as the default
kernel.

Starting with Oracle Linux 8.5, you also have the option of installing UEK R7. From Oracle
Linux 8.7 onward, UEK R7 is the default kernel.

Oracle provides Remote
Direct Memory Access (RDMA) packages for use with UEK R6 and UEK R7. The RDMA feature
enables direct memory access between two systems that are connected by a network. RDMA
facilitates high-throughput and low-latency networking in clusters.

To use RDMA
features, you must first install the Oracle-supported RDMA packages. To do so, ensure that
your system is subscribed to the appropriate channels on ULN or that you have enabled the
appropriate repositories on the Oracle Linux yum server.

RDMA With UEK R6

If you
are subscribed to ULN, enable the following channels:

- `ol8_x86_64_UEKR6`
- `ol8_x86_64_baseos_latest`
- `ol8_x86_64_appstream`
- `ol8_x86_64_UEKR6_RDMA`

Note that if your system is newly registered on ULN, it is already subscribed to
the `ol8_x86_64_UEKR6`, `ol8_x86_64_baseos_latest`, and
`ol8_x86_64_appstream` channels by default. However, you must explicitly
subscribe to the `ol8_x86_64_UEKR6_RDMA` channel prior to installing RDMA
packages.

If you are using the Oracle Linux yum server, enable the following
repositories:

- `ol8_UEKR6`
- `ol8_baseos_latest`
- `ol8_appstream`
- `ol8_UEKR6_RDMA`

Note that if your system already uses the Oracle Linux yum server, the
`ol8_UEKR6`, `ol8_baseos_latest`, and
`ol8_appstream` repositories are enabled by default. However, you must
explicitly enable the `ol8_UEKR6_RDMA` repository prior to installing RDMA
packages.

For additional information about RDMA, including any known issues, see
[Unbreakable Enterprise Kernel: Release Notes for
Unbreakable Enterprise Kernel Release 6 Update 3](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.3/).

RDMA With UEK R7

If you are subscribed to ULN, enable the following channels:

- `ol8_x86_64_UEKR7`
- `ol8_x86_64_baseos_latest`
- `ol8_x86_64_appstream`
- `ol8_x86_64_UEKR7_RDMA`

Note that if your system is newly registered on ULN, it is already subscribed to
the `ol8_x86_64_UEKR6`, `ol8_x86_64_baseos_latest`, and
`ol8_x86_64_appstream` channels by default. You should disable
`ol8_x86_64_UEKR6` and then explicitly subscribe to the
`ol8_x86_64_UEKR7_RDMA` and `ol8_x86_64_UEKR7_RDMA`
channels prior to installing RDMA packages.

If you are using the Oracle Linux yum
server, enable the following repositories:

- `ol8_UEKR7`
- `ol8_baseos_latest`
- `ol8_appstream`
- `ol8_UEKR7_RDMA`

Note that if your system already uses the Oracle Linux yum server, the
`ol8_UEKR6`, `ol8_baseos_latest`, and
`ol8_appstream` repositories are enabled by default. You should disable
`ol8_UEKR6` and then explicitly subscribe to the
`ol8_UEKR7_RDMA` and `ol8_UEKR7_RDMA` repositories prior
to installing RDMA packages.

For additional information about RDMA, including any
known issues, see [Unbreakable Enterprise Kernel: Release Notes for Unbreakable
Enterprise Kernel Release 7](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.5/ol8-NewFeaturesandChanges.html -->

This chapter describes the new features, major enhancements, bug fixes, and other changes
that are included in this release of Oracle Linux 8.

### Installation

The following installation changes are introduced in Oracle Linux 8.5:

- Capability for overriding official repositories added

  The `osbuild-composer` backend includes a
  set of official repositories that are defined in the
  `/usr/share/osbuild-composer/repositories`
  directory by default; but, it does not inherit the system
  repositories that are located in the
  `/etc/yum.repos.d/` directory. However,
  in this release, you can override the official
  repositories by defining overrides in the
  `/etc/osbuild-composer/repositories`
  directory. As a result. the files that are located in this
  directory take precedence over those in the
  `/usr` directory.
- Graphical installation program displays warnings about deprecated kernel
  boot arguments

  Graphical installation program boot arguments that do not
  contain the `inst.` prefix, such as
  `ks`, `stage2`,
  `repo`, and so on, are deprecated as of
  Oracle Linux 7, with the intent to remove these arguments in the
  next major Oracle Linux release.

  Starting with Oracle Linux 8.4, warning messages are displayed by the
  graphical installation program whenever any boot arguments
  that do not contain the `inst.` prefix are
  used, as appropriate.

  For example, the following warnings are displayed in
  `dracut` when booting the installation:

  ```
  ks has been deprecated. All usage of Anaconda boot arguments
  without the inst. prefix have been deprecated and will be removed in a future
  major release. Please use inst.ks instead.
  ```

  When the installation program has started in a terminal
  window, the following warnings are displayed:

  ```
  Deprecated boot argument ks must be used with the inst. prefix.
  Please use inst.ks instead. Anaconda boot arguments without inst.
  prefix have been deprecated and will be removed in a future major release.
  ```

### Red Hat Compatible Kernel

The following notable features, enhancements, and changes apply
to the Red Hat Compatible Kernel (RHCK) that is shipped with
Oracle Linux 8.5 on the x86\_64 platform.

For the latest information about Unbreakable Enterprise Kernel Release 6 (UEK R6), which is
shipped with Oracle Linux 8.5, see [Unbreakable Enterprise Kernel: Release Notes for
Unbreakable Enterprise Kernel Release 6 Update 3 (5.4.17-2136)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.3/).

#### schedutil CPU governor available in RHCK and UEK R6

In Oracle Linux 8.5, the `schedutil` CPU frequency
governor is available for both RHCK and UEK R6. This feature
leverages utilization data from the CPU scheduler to
appropriately adjust CPU frequency settings and performance
state. The `schedutil` governor is capable of
accessing the schedulerâs internal data structures directly
and can control how the CPU raises and lowers its frequency in
response to system load.

Note that the `schedutil` governor feature is
not enabled by default and must be manually enabled.

#### igc Driver Included

The `igc` Intel 2.5G Ethernet Linux wired
local area network (LAN) driver, which was previously
introduced in Oracle Linux 8.1 as a technology preview, is supported on
all architectures, starting with Oracle Linux 8.4. Note that the
`ethtool` command that is used to control
network driver and hardware settings also includes support for
`igc` wired LANs.

#### EDAC for Intel Sapphire Rapids Processors Enabled

This enhancement provides Error Detection And Correction
(EDAC) device support for Intel Sapphire Rapids processors.
EDAC mainly handles Error Code Correction (ECC) memory and
detects and reports PCI bus parity errors.

Note that this feature is already enabled in Unbreakable Enterprise Kernel Release 6.

### Software Management

The following software management features and enhancements are
introduced in Oracle Linux 8.5:

- RPM includes read-only support for sqlite database back end

  When inspecting other root directories, such as
  containers, you might want to query an RPM that is based
  on the `sqlite` database backend. Oracle Linux 8.5
  includes read-only support for the RPM
  `sqlite` database back end, which means
  you can query the packages that are installed in a
  container directly from the Oracle Linux 8 host.

  To perform this type of query with Podman, mount the
  containerâs file system by using `podman
  mount` command, then run the `rpm
  -qa` command with the `--root`
  option and point to the mounted location.

  Note that RPM on Oracle Linux 8 continues to use the Berkeley DB
  database (`bdb`) back end.
- libmodulemd updated to version 2.13.0

  The `libmodulemd` packages have been
  updated to version 2.13.0. This version of
  `libmodulemd` includes fixes for several
  issues with the `modulemd-validator`
  command, as well as the following improvements over the
  previous version:

  - Capability for delisting demodularized packages from a
    module.
  - Capability for validating
    `modulemd-packager-v3` documents by
    specifying the new -`-type` option with
    the `modulemd-validator` command.
  - Fortified parsing integers.
- sslverifystatus added to dnf configuration

  Starting with this release, enabling the
  `sslverifystatus` option causes the
  `dnf` command to each server certificate
  revocation status by using the Certificate Status Request
  TLS extension (OCSP stapling). As a result, when a revoked
  certificate is encountered, the `dnf`
  command refuses the download from its server.
- libcomps-devel package moved to ol8\_codeready\_builder repository

  The `libcomps-devel` package was moved by upstream from the
  `ol8_baseos` repository to the `ol8_codeready_builder`
  repository between Oracle Linux 8.4 and Oracle Linux 8.5. If you were using this package
  previously, you may need to enable the `ol8_codeready_builder` repository
  to resolve any potential update issues.

### Shells and Command-Line Tools

The following shells and command-line tools features and
improvements are introduced in Oracle Linux 8.5:

- Errors when restoring LVM with thin pools is fixed

  This enhancement enables Relax-and-Recover (ReaR) to
  detect when thin pools and other logical volume types with
  kernel metadata, such as RAIDs and caches, are used in a
  volume group (VG). ReaR then switches to a mode where it
  recreates all of the logical volumes (LVs) in the VG by
  using `lvcreate` commands. Thus, LVM with
  thin pools are restored without producing any errors.

  Note:

  The new method does not preserve all the LV properties,
  such as LVM UUIDs. Before you use ReaR in a production
  environments, you should test restoring from the backup to
  determine whether the recreated storage layout matches the
  requirements.
- FCoE option changed to rd.fcoe

  The `rd.nofcoe=0` command has been
  changed to `rd.fcoe` in Oracle Linux 8.5. In
  previous releases, the
  `dracut.cmdline(7)` manual page
  documented using the `rd.nofcoe=0`
  command to turn off Fibre Channel over Ethernet (FCoE).
  Starting with this release, you should use the
  `rd.fcoe=0` command to disable FCoE.
- lsvpd updated to version 1.7.12

  The `lsvpd` package has been updated to
  version 1.7.12 in this release. Notable bug fixes and
  enhancements in this version of `lsvpd`
  include the following:

  - UUID property added in `sysvpd`.
  - Improvements to the NVMe firmware version.
  - Fix for the PCI device manufacturer parsing logic.
  - Added `recommends clause` to the
    `lsvpd` configuration file.
- modulemd-tools package added

  The `modulemd-tools` package is
  introduced in Oracle Linux 8.5. This package provides tools for
  parsing and generating `modulemd` YAML
  files. To install the package, use the `dnf
  install modulemd-tools` command.
- opencryptoki updated to version 3.16.0

  The `opencryptoki` package has been
  updated to version 3.16.0 in this release. This version of
  `opencryptoki` includes several bug fixes
  and the following improvements over the previous version:

  - Improvements to the `protected-key`
    option and support for `attribute-bound
    keys` in the EP11 core processor
  - Improvements to the import and export of secure key
    objects in the `cycle-count-accurate`
    (CCA) processor.
- ppc64-diag updated to version 2.7.1

  The `ppc64-diag` package has been updated
  to version 2.7.7 in this release. This version of
  `ppc64-diag` includes the following
  improvements:

  - Unit test cases have been improved.
  - UUID property is added in `sysvpd`.
  - The `rtas_errd` service does not run in
    Linux containers.
  - Obsolete logging options removed from the
    `systemd` service files.
- ReaR updated to version 2.6

  The ReaR feature has been updated to version 2.6 in this
  release. This version of ReaR includes several notable
  improvements over the previous version.

### Compilers and Development Toolsets

Oracle Linux 8.5 introduces the following features, enhancements, and
changes to compilers and development toolsets.

- Go Toolset updated to version 1.16.6

  The Go Toolset has been updated to version 1.16.6. The
  following are some of the notable changes that have been
  made:

  - The `GO111MODULE` environment variable
    is set to `on` by default. You can
    revert this setting by changing the variable's value to
    `auto`.
  - The Go linker uses less resources and improves code
    robustness and maintainability. This improvement applies
    to all supported architectures and operating systems.
  - A new `embed` package has been added.
    With this package, you can access embedded files while
    compiling programs.
  - All of the functions of the `io/ioutil`
    package have been moved to the `io` and
    `os` packages. You an still use the
    `io/ioutil` package; however, the
    `io` and `os` packages
    provide better definitions.
  - The Delve debugger has been updated to version 1.6.0.
    This version of the Delve debugger supports the Go
    1.16.7 Toolset.
- Rust Toolset updated to version 1.54.0

  The Rust Toolset has been updated to version 1.54.0. This
  version of the Rust Toolset included the following
  changes:

  - The Rust standard library is available for the
    `wasm32-unknown-unknown` target. This
    enhancement enables you to generate WebAssembly
    binaries, including newly stabilized intrinsics.
  - Rust includes the `IntoIterator`
    implementation for arrays. This enhancement enables you
    to use the `IntoIterator` trait to
    iterate over arrays by value and pass arrays to methods.
    Note, however, that the
    `array.into_iter()` still iterates
    values by reference until the 2021 edition of Rust.
  - The syntax for `or` patterns allows for
    nesting anywhere in the pattern, for example,
    `Pattern(1|2)` can be used instead of
    `Pattern(1)|Pattern(2)`.
  - Unicode identifiers can contain all valid identifier
    characters, as defined in the Unicode Standard Annex
    #31.
  - Methods and trait implementations have been stabilized.
  - Incremental compilation has been reenabled by default.
- LLVM Toolset updated to version 12.0.1

  The LLVM Toolset has been updated to version 12.0.1. A new
  compiler was added and several changes were made to
  existing compilers. The following are the notable changes
  that were made in this version of the tool:

  - The new `-march=x86-64-v[234]` complier
    flag has been added.
  - The `-fasynchronous-unwind-tables`
    compiler flag, which is part of the
    `clang` compiler, is the default on
    Linux AArch64/PowerPC.
  - The `clang` compiler includes support
    for the C++20 likelihood attributes.
  - The new `tune-cpu` function attribute
    has been added. This function attribute enables
    microarchitectural optimizations to be applied
    independently from the `target-cpu`
    attribute or TargetMachine CPU.
  - The new sanitizer,
    `-fsanitize=unsigned-shift-base`, has
    been added to the integer sanitizer,
    `-fsanitize=integer`, for improved
    security.
  - Code generation on PowerPC targets has been optimized.
  - The WebAssembly back end is now enabled in LLVM. This
    enhancments enables you to generate WebAssembly binaries
    with LLVM and Clang.
  - For debugging .NET applications, use the
    `lldb` debugger. For other languages,
    use the `gdb` debugger.
- CMake updated to version 3.20.2

  CMake has been updated to version 3.20.2. Notable changes
  that are included in this version of CMake include the
  following:

  - C++23 compiler modes can be specified by using the
    `CXX_STANDARD`,
    `CUDA_STANDARD`, and
    `OBJCXX_STANDARD` target properties or
    by using the `cxx_std_23` meta-feature
    of the compile features function.
  - CUDA language support allows the NVIDIA CUDA compiler to
    be a symbolic link.
  - Intel oneAPI NextGen LLVM compilers are supported with
    the `IntelLLVM` compiler ID.
  - CMake can facilitate cross compiling for Android by
    merging with the Android NDKâs toolchain file.
  - When using `cmake(1)` to generate a
    project build system, unknown command-line arguments
    that begin with a hyphen are rejected.
- GCC Toolset 11: dwz suppors DWARF 5

  Staring with GCC Toolset 11, `dwz`
  includes support for DWARF 5.
- SystemTap updated to verison 4.5

  SystemTap has been updated to to version 4.5. This version
  of SystemTap includes several bug fixes and other
  improvements, including the following:

  - 32-bit floating-point variables are automatically
    widened to double variables. As a result, they can be
    accessed directly as `$context`
    variables.
  - `enum` values can be accessed as
    `$context` variables.
  - The BPF uconversions tapset has been extended to include
    more tapset functions for accessing values in user
    space, such as `user_long_error()`.
  - Concurrency control is significantly improved to provide
    more stable operatiosn on large servers.
- elfutils updated to version 0.185

  The `elfutils` packages have been updated
  to version 0.185. Several bug fixes and the following
  notable improvements have been made in this version:

  - The `eu-elflint` and
    `eu-readelf` tools can recognize and
    show the `SHF_GNU_RETAIN` and
    `SHT_X86_64_UNWIND` flags on ELF
    sections.
  - The `DEBUGINFOD_SONAME` macro is added
    to `debuginfod.h`. You can use this
    macro with the `dlopen` function to
    load the `libdebuginfod.so` library
    dynamically from an application.
  - The `debuginfod_set_verbose_fd`
    function has been added to the
    `debuginfod-client` library. This
    function enhances the
    `debuginfod_find_*` queries
    functionality by redirecting the verbose output to a
    separate file.
  - Setting the `DEBUGINFOD_VERBOSE`
    environment variable shows additional information about
    to which servers the `debuginfod`
    client is connected, as well HTTP responses of those
    servers.
  - The `debuginfod` server includes a new
    thread-busy metric and more detailed error metrics,
    which makes it easier to inspect processes that run on
    the `debuginfod` server.
  - The `libdw` library transparently
    handles the `DW_FORM_indirect` location
    value, which enables the
    `dwarf_whatform` function to return the
    actual FORM of an attribute.
  - The `debuginfod-client` library stores
    negative results in a cache, and client objects can
    reuse an existing connection, which reduces network
    traffic.
- Valgrind updated to version 3.17.0

  Valgrind has been updated to version 3.17.0. This version
  of Valgrind introduces several bug fixes and enhancements.
  A few of the more notable improvements include the
  following: Valgrind can read DWARF Version 5 debugging
  format, support for debugging queries to the
  `debuginfod` server, and partial support
  for ARMv8.2 processor instructions.
- New pcp-ss PCP utility

  The new `pcp-ss` PCP utility is added in
  this release. The utility reports socket statistics that
  are collected by the `pmdasockets(1)`
  PMDA. The command is compatible with several
  `ss` command-line options and reporting
  formats. The utility also provides the advantages of local
  and remote monitoring, in live mode and historical replay,
  from a previously recorded PCP archive.
- PCP updated to 5.3.1

  The Performance Co-Pilot (PCP) package has been updated to
  version 5.3.1. This release includes bug fixes,
  enhancements, and new features, including the following:
  scalability improvements, resolved memory leaks in the
  `pmproxy` service and the
  `libpcp_web` API library, a new
  `pcp-ss` tool for historical socket
  statistics, improvements to the
  `pcp-htop` tool, and extensions to the
  over-the-wire PCP protocol, which supports higher
  resolution timestamps.
- pcp-container package updated to version 5.3.1

  The `pcp-container` package has been
  updated to version 5.3.1 in this release.
- grafana package updated to version 7.5.9

  The `grafana` package has been updated to
  version 7.5.9 in this release. Notable new features
  enhancements include the following: a new time series
  panel (beta), a new pie chart panel (beta), altering
  support for Loki, and multiple new query transformations.
- grafana-container package updated to version 7.5.9

  The `grafana-container` packages have
  been updated to version 7.5.9 in this release. Notable new
  features enhancements include the following:

  - The `grafana` package is updated to
    version 7.5.9.
  - The `grafana-pcp` package is updated to
    version 3.10.
  - The container includes support for the
    `GF_INSTALL_PLUGINS` environment
    variable for installing custom Grafana plugins at
    container start-up.
- grafana-pcp package updated to version 3.10.0

  The `grafana-pcp` package has been
  updated to version 3.1.0. Notable improvements include the
  following:

  - Performance Co-Pilot (PCP) Vector Checklist dashboards
    use a new time series panel, show units in graphs, and
    contain updated help texts.
  - Addition of the `pmproxy` URL and
    `hostspec` variables to PCP Vector Host
    Overview and PCP Checklist dashboards.
  - All dashboards display datasource selection.
  - Marking all included dashboards as read-only.
  - Added compatibility with Grafana 8.

### GCC Toolset 11

Oracle Linux 8.5 provides the GCC Toolset 11, which is an Application
Stream that is distributed in the form of a Software Collection
in the `AppStream` repository. The GCC Toolset
is similar to the Oracle Linux Developer Toolset.

In Oracle Linux 8.5, the GCC compiler is updated to the upstream version.
The following tools have been updated since GCC Toolset 10:

- GCC version 11.1.1
- GDB version 10.1
- Valgrind version 3.17.0
- SystemTap version 4.5
- Dyninst version 10.2.1
- `binutils` version 2.36.1
- `elfutils` version 0.184
- `dwz` version 0.14
- `annobin` version 9.69

See [Compilers and Development Toolsets](ol8-NewFeaturesandChanges.html#ol8-features-developer) for further details
about notable changes that have been made to some of the tools
that are in GCC Toolset 11.

The GCC Toolset 11 is available as an Application Stream within
the `AppStream` repository, in the form of a
Software Collection.

To install this toolset, use the following command:

```
sudo dnf install gcc-toolset-11
```

To run a tool from GCC Toolset 11, use the following command:

```
scl enable gcc-toolset-11 tool
```

The following command initiates a shell session, where tool
versions from the GCC Toolset 11 take precedence over system
versions of the same tools:

```
scl enable gcc-toolset-11 bash
```

### Database

This release of Oracle Linux 8 ships with version 8.0 of the MySQL database software.

### Dynamic Programming Languages, Web, and Database Servers

Oracle Linux 8.5 includes several feature changes and improvements for
dynamic programming languages and web and database servers. Note
that that this release also introduces several new and improved
module streams:

- ruby:3.0 module stream added

  Oracle Linux 8.5 includes Ruby version 3.0.2 in a new
  `ruby:3.0` module stream. Ruby 3.0.2
  includes several performance improvements, bug and
  security fixes, and new features, compared with Ruby
  version 2.7 that was previously available. This version of
  Ruby includes the following significant features:

  - Concurrency and parallelism features.
  - Static analysis features.
  - Pattern matching with the `case/in`
    expression is no longer experimental.
  - One-line pattern matching has been redesigned. This
    feature is an experimental feature.
  - The find pattern is added as an experimental feature.
  - Pasting of long code to the `Interactive Ruby
    Shell (IRB)` is significantly faster.
  - The `measure` command has been added to
    IRB for time measurement.
  - Changes to keyword arguments, which are now separated
    from other arguments.
  - The default directory for user-installed gems has
    changed to `$HOME/.local/share/gem/`,
    unless the `$HOME/.gem/` directory
    already exists.
- Default separator for Python urllib parsing functions has changed

  The default separator for the
  `urllib.parse.parse_qsl` and
  `urllib.parse.parse_qs` functions has
  been changed from the ampersand (`&`)
  and semicolon (`;`) to just an ampersand.
  These changes were made to mitigate the Web Cache
  Poisoning CVE-2021-23336 in the Python
  `urllib` library.

  This change, which was introduced in Python 3.6 with
  Oracle Linux 8.4, is now being backported to Python 3.8 and Python
  2.7. Note that Python 3.9 is unaffected, as it already
  includes the new default separator.

  Note:

  Because this change is potentially backwards incompatible,
  you have the option to configure the behavior in Python
  packages, where the default separator has been changed.
  Note also that the affected `urllib`
  parsing functions emit a warning if it is detected that a
  customerâs application is affected by the change.
- Python ipaddress module changes

  The Python `ipaddress` module has been
  updated to reject IPv4 addresses with leading zeros, with
  an `AddressValueError: Leading zeros are not
  permitted` error. This change was made to
  mitigate CVE-2021-299221.

  This change was introduced in `python38`
  and `python39` modules. Note that previous
  Python modules are not impacted by CVE-2021-299221.

  If you rely on the previous behavior, you can pre-process
  your IPv4 address inputs to strip the leading zeros off as
  follows:

  ```
  >>> def reformat_ip(address): return '.'.join(part.lstrip('0') if part != '0' else part for part in address.split('.'))
  >>> reformat_ip('0127.0.0.1')
  '127.0.0.1'
  ```

  To strip off the leading zeros with an explicit loop for
  readability, use the following:

  ```
  def reformat_ip(address):
      parts = []
      for part in address.split('.'):
          if part != "0":
              part = part.lstrip('0')
          parts.append(part)
      return '.'.join(parts)
  ```
- php:7.4 module stream updated to version 7.4.19

  The PHP scripting language, which is included in the
  `php:7.4` module stream, has been updated
  to version 7.4.19 in this release. With this update,
  multiple security and bug fixes have been implemented.
- pg\_repack package added

  The new `pg_repack` has been added to the
  `postgresql:12` and
  `postgresql:13` modules. This package
  provides a `PostgreSQL` extension that
  enables you remove bloat from tables and indexes, as well
  as optionally restore the physical order of clustered
  indexes.
- nginx:1.20 module added

  The `nginx 1.20` web and proxy server is
  available as the `nginx:1.20` module
  stream in Oracle Linux 8.5. This version provides numerous bug
  fixes, security fixes, enhancements, and new features over
  the previous version, including the following:

  - Support for the client SSL certificate validation with
    Online Certificate Status Protocol (OCSP).
  - Support for cache clearing, based on the minimum amount
    of free space. Note that this feature is implemented as
    the `min_free` parameter of the
    `proxy_cache_path` directive.

  Other notable changes in the `nginx:1.20`
  module include enhanced directives, such as the
  `ssl_conf_command` and
  `ssl_reject_handshake` , and
  `proxy_cookie_flags`, as well as improved
  support for HTTP/2.
- squid:4 module updated to version 4.15

  The `Squid` proxy sserver, which is
  available in the`squid:4` module stream
  has been updated to version 4.15. This update includes
  several bug and security fixes over the previous version.
- quota command supports HPE XFS

  This change enables users of HPE XFS to monitor and manage
  user and group disk usage by using the
  `quota`.
- mutt updated to version 2.0.7

  The Mutt email client has been updated to version 2.0.7 in
  this release. This version of `mutt`
  provides a number of enhancements and bug fixes, as well
  as added supported for the following:

  - The `OAuth 2.0` authorization protocol
    by using the `XOAUTH2` mechanism. Mutt
    also supports the `OAUTHBEARER`
    authentication mechanism for the IMAP, POP, and SMTP
    protocols.
  - Domain-literal email addresses such as
    `user@[IPv6:fcXX:â¦â]`
  - New `$imap_deflate` variable that
    supports `COMPRESS=DEFLATE`
    compression. Note that this variable is disabled by
    default.
  - `$ssl_starttls` variable no longer
    controls aborting an unencrypted IMAP
    `PREAUTH` connection. Instead, use the
    `$ssl_force_tls` variable if you rely
    on the `STARTTLS` process.

  Note:

  After updating to the new Mutt version, the
  `ssl_force_tls` configuration variable
  still defaults to `no`, which is designed
  prevent problems in existing environments. Note also in
  the upstream version of Mutt,
  `ssl_force_tls` is enabled by default.

### File Systems and Storage

Oracle Linux 8.5 provides the following file systems and storage
features, enhancements, and changes:

- Btrfs removed from RHCK

  The Btrfs file system is removed from RHCK in Oracle Linux 8. As
  such, you cannot create or mount Btrfs file systems when
  using this kernel. Also, note that any Btrfs user space
  packages that are provided are not supported with RHCK.

  Note:

  Support for the Btrfs file system is enabled in UEK R6;
  starting with Oracle Linux 8.3, you have the option to create a
  Btrfs root file system during an installation, as well as
  select Btrfs as the file system type when formatting
  devices. See [Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/) for more information about
  this feature.

  For more information about managing a Btrfs root file
  system, see [Oracle Linux 8: Managing Local File Systems](https://docs.oracle.com/en/operating-systems/oracle-linux/8/fsadmin/).

  For the latest enhancements that have been made to Btrfs
  in UEK R6, see [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 6 Update 3 (5.4.17-2136)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.3/).
- OCFS2 removed from RHCK

  The Oracle Cluster File System version 2 (OCFS2) file
  system is removed from RHCK in Oracle Linux 8. As such, you cannot
  create or mount OCFS2 file systems when using this kernel.
  Also, any OCFS2 user space packages that are provided are
  not supported with RHCK.

  Note:

  OCFS2 is fully supported with UEK R6 in Oracle Linux 8.5.
- NVMe/TCP included as a Technology Preview

  NVMe over Fabrics TCP host and the target drivers are
  included in RHCK as a technology preview in this release.

  Note:

  Support for NVMe/TCP is already available in Unbreakable Enterprise Kernel Release 6.

### High Availability and Clusters

The following high availability and clustering features are
included in Oracle Linux 8.5:

- Local mode version for pcs cluster setup command added

  Support for the local mode version of the `pcs
  cluster setup` command has been added in this
  release.
- fence\_watchdog agent enables watchdog-only SBD configuration on subset
  of cluster nodes

  This release includes a new
  `fence_watchdog` agent for configuring a
  watchdog-only SBD setup. Because this capability did not
  exist previously, it prevented the use of SBD in a cluster
  where some nodes supported it, but others (most often
  remote nodes) required some other form of fencing.
- pcs command for updating SCSI fencing device

  A new `pcs` command for updating a SCSI
  fencing device without causing the restart of all other
  resources has been added.
- Reduced output display option added to pcs resoure safe-disable command

  The reduced output display option has been added to the
  `pcs resource safe-disable` command
- pcs command accepts Promoted and Unpromoted role names

  With this update, the `pcs` command
  accepts the `Promoted` and
  `Unpromoted` role names.
- pcs resoure status display commands added

  This update introduces new `pcs` resource
  status display commands.
- LVM volume group flag added

  A new LVM volume group flag for controlling
  auto-activation has been added in this release.

### Infrastructure Services

Oracle Linux 8.5 introduces several version updates to infrastructure and
command-line tools, including the following features:

- linuxptp updated to version 3.1

  The `linuxptp` package has been updated
  to version 3.1. Notable enhancements include the
  `ts2phc` program for synchronizing the
  Precision Time Protocol (PTP) hardware clock to Pulse Per
  Second (PPS) signal, and added support for the automotive
  profile and client event monitoring.
- chrony updated to version 4.1

  The `chrony` package has been updated to
  version 4.1 in this release. Notable changes in this
  version of `chrony` include the
  following:

  - Added support for Network Time Security (NTS)
    authentication.
  - The Authenticated Network Time Protocol (NTP) sources
    are trusted over non-authenticated NTP sources by
    default in this update. To restore the original
    behavior, add the `autselectmode
    ignore` argument to the
    `chrony.conf` file.
  - Support is no longer available for authentication with
    the following `RIPEMD` keys:
    `RMD128`, `RMD160`,
    `RMD256`, and
    `RMD320`.
  - Support for long, non-standard MACs in NTPv4 packets is
    no longer available. If you are using the
    `chrony 2.x`,
    `non-MD5/SHA1` keys, you need to
    configure `chrony` by using the
    `version 3` option.
- PowerTop updated to version 2.14

  PowerTop has been updated to version 2.14 in this release.
  This update provides support for the Alder Lake, Sapphire
  Rapids, and Rocket Lake platforms.
- kdumpctl updated to provide an estimate utility

  The `kdumpctl` command features an
  `estimate` subcommand. Running the
  `kdumpctl estimate` command provides a
  recommended `crashkernel` value that is
  based on the current kdump setup and includes additional
  details on memory usage.
- Intel® QuickAssist Technology Library user space package updated to
  version 21.05

  The Intel® QuickAssist Technology Library (QATlib) user
  space package and the `qatlib` user space
  libraries that allow access to Intel QuickAssist devices
  and expose the Intel QuickAssist APIs, have been updated
  to version 21.05.
- Tuned moves unnecessary IRQs to housekeeping CPUs

  Network device drivers such as `i40e`,
  `iavf`, and `mlx5`
  evaluate online CPUs to determine the number of queues and
  `MSIX` vectors to be created. Previously,
  for low-latency environments consisting of a large number
  of isolated and very few housekeeping CPUs, any attempts
  by Tuned to move these device IRQs to housekeeping CPUs
  failed, due to the per-CPU vector limit.

  With this enhancement, Tuned explicitly adjusts the numbers
  of network device channels, and MSIX vectors, as per the
  housekeeping CPUs. Therefore, all of the device IRQs on the
  housekeeping CPUs can be moved to achieve low latency.

### Graphics Infrastructure

- Intel's Tiger Lake graphics available

  Intel's Tiger Lake graphics is made available in Oracle Linux 8.5
  .

### Networking

Oracle Linux 8.5 introduces the following networking features,
enhancements, and changes:

- firewalld updated to version 0.9.3

  The `firewalld` package has been updated
  to version 0.9.3. This version of
  `firewalld` includes numerous upstream
  bug fixes and improvements over version 0.8.2.

  Notably, this update includes the introduction of the policy object feature that allows
  forward and output filtering for virtual machines (VMs), containers, and zones. For
  further information, see <https://firewalld.org/2020/09/policy-objects-introduction> and <https://firewalld.org/2020/09/policy-objects-filtering-container-and-vm-traffic>.
- NetworkManager updated to version 1.32.10

  `NetworkManager` has been updated to
  version 1.32.10. This version of
  `NetworkManager` includes numerous bug
  fixes and enhancements over the previous version.
- Capability for managing ethtool parameters added to NetworkManager

  In certain cases, you need to explicitly set non
  auto-pause parameters on a specific network interface. In
  this release, `NetworkManager` includes
  capability for pausing the control flow parameters of
  `ethtool` in `nmstate`.
  Previously, `NetworkManager` did not
  include this capability.

  To disable auto negotiation of the pause parameter and
  enable RX/TX pause support explicitly, use the following
  command:

  ```
  sudo nmcli connection modify enp1s0 ethtool.pause-autoneg no ethtool.pause-rx true ethtool.pause-tx true
  ```
- Property for setting physical and virtual interface in promiscuous mode
  added to Network Manager

  The
  `802-3-ethernet.accept-all-mac-addresses`
  property for setting physical and virtual interfaces in
  the `accept all MAC addresses` mode has
  been added to `NetworkManager`. With this
  enhancement, the kernel can accept network packages that
  are targeting current interfacesâ MAC address in the
  `accept all MAC addresses` mode.

  For example, to enable `accept all MAC
  addresses` mode on `eth1`, use the
  following command:

  ```
  sudo nmcli c add type ethernet  ifname eth1 connection.id eth1  802-3-ethernet.accept-all-mac-addresses true
  ```
- nftables can be used as firewall back end in NetworkManager

  This enhancement adds support for the
  `nftables` firewall framework to
  NetworkManager. To switch the default back end from
  `iptables` to
  `nftables`, use the following commands:

### Security

Oracle Linux 8.5 introduces the following security features,
enhancements, and changes:

- crypto-policies updated to 20210617

  The `crypto-policies` packages have been
  updated to the upstream version 20210617. This version of
  `crypto-policies` includes numerou bug
  fixes and improvements over the previous version.
- crypto-policies support for AES-192 ciphers in custom policies

  In Oracle Linux 8.5, the system-wide cryptographic policies include
  support for the following values of the
  `cipher` option in the custom policies
  and subpolicies: `AES-192-GCM`,
  `AES-192-CCM`,
  `AES-192-CTR`, and
  `AES-192-CBC`. With this change, you an
  enable the `AES-192-GCM` and
  `AES-192-CBC` ciphers for the Libreswan
  application, as well as the `AES-192-CTR`
  and `AES-192-CBC` ciphers for the
  `libssh` library and the OpenSSH suite
  through `crypto-policies`.
- CBC ciphers are disabled in the FUTURE cryptographic policy

  IThe `crypto-policies` packages have been
  updated to disable ciphers that use cipher block chaining
  (CBC) mode in the `FUTURE` policy. The
  settings in the `FUTURE` policy should be
  able to withstand near-term future attacks; this change
  reflects the current progress. Consequently, system
  components that respect `crypto-policies`
  cannot use CBC mode when the `FUTURE`
  policy is active.
- gnutls updated to version 3.6.16

  The `gnutls` packages have been updated
  to version 3.6.16. The following notable enhancements and
  bug fixes are included:

  - The `gnutls_x509_crt_export2()`
    function returns `0` value instead of
    the size of the internal base64 blob in the event of
    success. This change aligns with the documentation in
    the `gnutls_x509_crt_export2(3`) manual
    page.
  - Certificate verification failures due to the Online
    Certificate Status Protocol (OCSP) must-stapling not
    being followed are correctly marked with the
    `GNUTLS_CERT_INVALID` flag.
  - Version negotiation for TLS 1.2 has been fixed and TLS
    1.2 can now be correctly disabled. Previously, if TLS
    1.2 was explicitly disabled by using the
    `-VERS-TLS1.2` option, the server
    continued to offer TLS 1.2, even if TLS 1.3 was enabled
- Kernel AVC tracepoint added

  This enhancement introduces a new
  `avc:selinux_audited` kernel tracepoint
  that triggers when an SELinux denial is to be audited.
  This tracepoint provides for a more convenient and
  low-level debugging of SELinux denials. Note that the new
  tracepoint is also available for tools like
  `perf`.
- libreswan updated to version 4.4

  The `libreswan` packages have been
  updated to version 4.4. This version introduces important
  enhancements and bug fixes, including several IKEv2 and
  `pluto` IKE daemon enhancements, most
  notably the following:

  - IKEv2 protocol fixes and enhancements:

    - Fixes for TCP encapsulation in `Transport
      Mode` and host-to-host connections.
    - `--globalstatus` option added to
      the `ipsec whack` command for
      displaying redirect statistics.
    - The `vhost` and
      `vnet` values in the
      `ipsec.conf` configuration file are
      no longer allowed for IKEv2 connections.
  - `pluto` IKE daemon fixes and
    enhancements:

    - Fixes for host-to-host connections that use
      non-standard IKE ports.
    - The `interface-ip=` option is
      disabled because Libreswan does not provide the
      corresponding functionality yet.
    - The `PLUTO_PEER_CLIENT` variable in
      the `ipsec__updown` script for NAT
      in `Transport Mode` is fixed.
    - Set the `PLUTO_CONNECTION_TYPE`
      variable to `transport` or
      `tunnel`.
    - Non-templated wildcard ID connections can now match.
- SCAP Security Guide updated to version 0.1.57

  In Oracle Linux 8.5, the `scap-security-guide`
  packages have been updated to version 0.1.57. This version
  of the SCAP Security Guide provides several bug fixes and
  improvements over the previous version, including the
  following:

  - Performance remediations for Audit improvements

    Performance of remediations for Audit has been
    improved by grouping similar system calls. Previously,
    Audit remediations generated an individual rule for
    each system call tha was audited by the profile. This
    behavior led to large numbers of audit rules, which in
    turn, degraded performance. With this change,
    remediations for Audit can group rules together for
    similar system calls with identical fields into a
    single rule, which improves performance.
  - Profile for ANSSI-BP-028 High level added

    The ANSSI High level profile, which is based on the
    ANSSI BP-028 recommendations from the French National
    Security Agency (ANSSI), is added in this release.
    This additional completes the availability of profiles
    for all ANSSI-BP-028 v1.2 hardening levels in the SCAP
    Security Guide. The new profile enables you to harden
    the system to the recommendations from ANSSI for
    GNU/Linux Systems at the High hardening level. Thus,
    you can configure and automate compliance of your
    Oracle Linux 8 systems to the strictest hardening level by
    using ANSSI Ansible Playbooks and ANSSI SCAP profiles.
- OpenSCAP updated to version 1.3.5

  The OpenSCAP packages have been updated to version 1.3.5.
  This version of OpenSCAP includes numerous fixes and other
  enhancements over the previous version.
- Support for validating digitally signed SCAP source data streams

  To conform with the Security Content Automation Protocol
  (SCAP) 1.3 specifications, OpenSCAP has been updated in
  Oracle Linux 8.5 to enable the validation of digital signatures for
  digitally signed SCAP source data streams. OpenSCAP also
  now validates the digital signature when evaluating a
  digitally signed SCAP source data stream. The signature
  validation is performed automatically while loading the
  file. Data streams with invalid signatures are rejected,
  and OpenSCAP does not evaluate their content. OpenSCAP
  uses the XML Security Library in conjunction with the
  OpenSSL cryptography library to validate the digital
  signature.

  To skip the signature validation, add the
  `--skip-signature-validation` option to the
  `oscap xccdf eval` command.

  Caution:

  OpenSCAP does not address the trustworthiness of
  certificates or public keys that are part of the
  `KeyInfo` signature element, which are
  used to verify the signature. As such, it is important
  that you verify such keys to prevent the evaluation of
  data streams that may have been modified and signed by bad
  actors.
- OpenSSL for encrypting Rsyslog TCP and RELP traffic

  In this release, the OpenSSL network stream driver has
  been added to Rsyslog. This driver implements
  TLS-protected transport by using the OpenSSL library. This
  change provides added functionality, compared to the
  stream driver that uses the GnuTLS library. In addition,
  you can use either OpenSSL or GnuTLS as an Rsyslog network
  stream driver.
- Rsyslog updated to version 8.2102.0-5

  Rsyslog has been updated to version 8.2102.0-5. The
  version of Rsyslog provides numerous improvements over the
  previous version, including the following:

  - Added the `exists()` script function
    for checking whether a variable exists or not, for
    example `$!path!var`
  - Ability to set OpenSSL configuration commands with the
    new `tls.tlscfgcmd` configuration
    parameter for the `omrelp` and
    `imrelp` modules.
  - Added two new rate-limit options to the
    `omfwd` module for rate-limiting
    `syslog` messages that are sent to the
    remote server:

    - `ratelimit.interval`: This option
      specifies the rate-limiting interval in seconds.
    - `ratelimit.burst`: This option
      specifies the rate-limiting burst in the number of
      messages.
  - The `immark` module has been rewritten
    to include various improvements.
  - Added the `max sessions` configuration
    parameter to the `imptcp` module. The
    maximum is measured per-instance, not globally, across
    all instances.
  - Added the `rsyslog-openssl` subpackage.
    This network stream driver implements TLS-protected
    transport by using the OpenSSL library.
  - Added per-minute rate limiting to the
    `imfile` module, with the
    `MaxBytesPerMinute` and
    `MaxLinesPerMinute` options. Note that
    these options accept integer values and limit the number
    of bytes or lines that are allowed to be sent in a
    minute.
  - Capability added to the `imtcp` and
    `omfwd` module to configure a maximum
    depth for the certificate chain verification by using
    the `streamdriver.TlsVerifyDepth`
    option.
- socat updated to version 1.7.4

  The `socat` packages have been updated to
  version 1.7.4. This version of `socat`
  includes numerous bug fixes and improvements over version
  1.7.3.

For information about security features that are related to
networking, see
[Networking](ol8-NewFeaturesandChanges.html#ol8-features-networking).

### Supportability

- SoS supportability feature updated to version 4.1

  The `sos` package for the System of
  Systems (SoS) supportability feature has been updated to
  version 4.1.

### Technology Preview

For the Red Hat Compatible Kernel in the current Oracle Linux 8 release, the following
features are under technology preview:

#### kexec Fast Reboot

The `kexec fast reboot` feature is available
as a technology preview feature in Oracle Linux 8. This feature
significantly speeds up the boot process by enabling the
kernel to boot directly into the second kernel without having
to first pass through the Basic Input/Output System (BIOS). To
use this feature, load the `kexec` module
first, then reboot the system.

#### aarch64 only: VNC Remote Console

In this release, the Virtual Network Computing (VNC) remote
console is available as a technology preview on the 64-bit Arm
platform only. The remaining components of
the graphics stack are unverified on this platform.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.5/ol8-KnownIssues.html -->

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

#### Oracle Linux 8.5 systems with libstoragemgt packages installed cannot be upgraded to Oracle Linux 8.6

The following `libstoragemgmt` packages are
not included in Oracle Linux 8.6:

- `libstoragemgmt-nfs-plugin-clibs-1.8.7-1.el8.x86_64.rpm`
- `libstoragemgmt-nfs-plugin-1.8.7-1.el8.noarch.rpm`

Consequently, if your Oracle Linux 8.5 system includes these packages,
upgrading the system to Oracle Linux 8.6 fails.

To work around this issue, remove these packages from the
system prior to upgrading to Oracle Linux 8.6.

(Bug ID 33545502)

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

The following are known issues for the Podman container
management tool in this release of Oracle Linux 8.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.5/ol8-PackageChangesfromtheUpstreamRelease.html -->

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
- `NetworkManager-config-connectivity-oracle`
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
- `oracle-database-preinstall-21c`
- `python3-dnf-plugin-ulninfo`

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
- `dbxtool`
- `dnf`
- `dnf-automatic`
- `dnf-data`
- `dnf-plugins-core`
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
- `iproute`
- `iproute-tc`
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
- `libgcrypt`
- `libgcrypt-devel`
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
- `libtirpc`
- `libtirpc-devel`
- `libtsan`
- `libubsan`
- `libxml2`
- `libxslt`
- `libzstd`
- `libzstd-devel`
- `linux-firmware`
- `mcelog`
- `microcode_ctl`
- `mokutil`
- `mozjs52`
- `mozjs60`
- `NetworkManager`
- `NetworkManager-adsl`
- `NetworkManager-bluetooth`
- `NetworkManager-config-connectivity-oracle`
- `NetworkManager-config-server`
- `NetworkManager-dispatcher-routing-rules`
- `NetworkManager-libnm`
- `NetworkManager-ovs`
- `NetworkManager-ppp`
- `NetworkManager-team`
- `NetworkManager-tui`
- `NetworkManager-wifi`
- `NetworkManager-wwan`
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
- `procps-ng`
- `procps-ng-i18n`
- `python3-boom`
- `python3-configshell`
- `python3-dnf`
- `python3-dnf-plugin-post-transaction-actions`
- `python3-dnf-plugins-core`
- `python3-dnf-plugin-versionlock`
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
- `trace-cmd`
- `tuned`
- `tuned-profiles-atomic`
- `tuned-profiles-compat`
- `tuned-profiles-cpu-partitioning`
- `tuned-profiles-mssql`
- `tuned-profiles-oracle`
- `vim-minimal`
- `yum`
- `yum-utils`

#### Modified Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `crash-devel`
- `cups-filters-devel`
- `dotnet5.0-build-reference-packages`
- `gcc-plugin-devel`
- `gcc-toolset-10-gcc-plugin-devel`
- `glibc-benchtests`
- `glibc-nss-devel`
- `glibc-static`
- `guile-devel`
- `iproute-devel`
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
- `python3-mpich`
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
- `aspnetcore-runtime-5.0`
- `aspnetcore-targeting-pack-3.0`
- `aspnetcore-targeting-pack-3.1`
- `aspnetcore-targeting-pack-5.0`
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
- `clang-resource-filesystem`
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
- `dotnet-apphost-pack-5.0`
- `dotnet-host`
- `dotnet-hostfxr-3.0`
- `dotnet-hostfxr-3.1`
- `dotnet-hostfxr-5.0`
- `dotnet-runtime-3.0`
- `dotnet-runtime-3.1`
- `dotnet-runtime-5.0`
- `dotnet-sdk-3.0`
- `dotnet-sdk-3.1`
- `dotnet-sdk-5.0`
- `dotnet-targeting-pack-3.0`
- `dotnet-targeting-pack-3.1`
- `dotnet-targeting-pack-5.0`
- `dotnet-templates-3.0`
- `dotnet-templates-3.1`
- `dotnet-templates-5.0`
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
- `fapolicyd`
- `fapolicyd-selinux`
- `firefox`
- `firewall-applet`
- `firewall-config`
- `gcc`
- `gcc-c++`
- `gcc-gdb-plugin`
- `gcc-gfortran`
- `gcc-offload-nvptx`
- `gcc-toolset-10-gcc`
- `gcc-toolset-10-gcc-c++`
- `gcc-toolset-10-gcc-gdb-plugin`
- `gcc-toolset-10-gcc-gfortran`
- `gcc-toolset-10-libasan-devel`
- `gcc-toolset-10-libatomic-devel`
- `gcc-toolset-10-libitm-devel`
- `gcc-toolset-10-liblsan-devel`
- `gcc-toolset-10-libquadmath-devel`
- `gcc-toolset-10-libstdc++-devel`
- `gcc-toolset-10-libstdc++-docs`
- `gcc-toolset-10-libtsan-devel`
- `gcc-toolset-10-libubsan-devel`
- `gcc-toolset-11-binutils`
- `gcc-toolset-11-binutils-devel`
- `gcc-toolset-11-gcc`
- `gcc-toolset-11-gcc-c++`
- `gcc-toolset-11-gcc-gdb-plugin`
- `gcc-toolset-11-gcc-gfortran`
- `gcc-toolset-11-gcc-plugin-devel`
- `gcc-toolset-11-libasan-devel`
- `gcc-toolset-11-libatomic-devel`
- `gcc-toolset-11-libgccjit`
- `gcc-toolset-11-libgccjit-devel`
- `gcc-toolset-11-libgccjit-docs`
- `gcc-toolset-11-libitm-devel`
- `gcc-toolset-11-liblsan-devel`
- `gcc-toolset-11-libquadmath-devel`
- `gcc-toolset-11-libstdc++-devel`
- `gcc-toolset-11-libstdc++-docs`
- `gcc-toolset-11-libtsan-devel`
- `gcc-toolset-11-libubsan-devel`
- `gdb`
- `gdb-doc`
- `gdb-gdbserver`
- `gdb-headless`
- `git-clang-format`
- `glibc-utils`
- `gnome-boxes`
- `gnome-session`
- `gnome-session-kiosk-session`
- `gnome-session-wayland-session`
- `gnome-session-xsession`
- `gnome-themes-standard`
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
- `ipa-selinux`
- `ipa-server`
- `ipa-server-common`
- `ipa-server-dns`
- `ipa-server-trust-ad`
- `kernel-rpm-macros`
- `kernelshark`
- `ksh`
- `libasan6`
- `libblockdev`
- `libblockdev-btrfs`
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
- `mpich`
- `mpich-devel`
- `mpich-doc`
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
- `NetworkManager-cloud-setup`
- `nginx`
- `nginx-all-modules`
- `nginx-filesystem`
- `nginx-mod-http-image-filter`
- `nginx-mod-http-perl`
- `nginx-mod-http-xslt-filter`
- `nginx-mod-mail`
- `nginx-mod-stream`
- `nodejs`
- `nodejs-devel`
- `nodejs-docs`
- `nodejs-full-i18n`
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
- `osbuild-composer`
- `osbuild-composer-core`
- `osbuild-composer-worker`
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
- `pki-acme`
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
- `podman-catatonit`
- `podman-docker`
- `podman-gvproxy`
- `podman-plugins`
- `podman-remote`
- `podman-tests`
- `policycoreutils-gui`
- `policycoreutils-sandbox`
- `pykickstart`
- `python2`
- `python2-debug`
- `python2-devel`
- `python2-libs`
- `python2-test`
- `python2-tkinter`
- `python2-tools`
- `python36`
- `python36-debug`
- `python36-devel`
- `python36-rpm-macros`
- `python3-abrt`
- `python3-abrt-addon`
- `python3-abrt-container-addon`
- `python3-abrt-doc`
- `python3-blivet`
- `python3-blockdev`
- `python3-clang`
- `python3-dnf-plugin-spacewalk`
- `python3-idle`
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-ipatests`
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
- `redfish-finder`
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
- `rsyslog-openssl`
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
- `sysstat`
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
- `WALinuxAgent-udev`
- `wget`
- `xsane`
- `xsane-common`
- `xsane-gimp`
- `zstd`

#### Removed BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been removed:

- `dnf-plugin-subscription-manager`
- `grub2-ppc64le-modules`
- `kpatch`
- `kpatch-dnf`
- `NetworkManager-config-connectivity-redhat`
- `python3-cloud-what`
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

- `ansible-collection-microsoft-sql`
- `ansible-collection-redhat-rhel_mgmt`
- `aspnetcore-runtime-6.0`
- `aspnetcore-targeting-pack-6.0`
- `coreos-installer`
- `coreos-installer-bootinfra`
- `dotnet-apphost-pack-6.0`
- `dotnet-hostfxr-6.0`
- `dotnet-runtime-6.0`
- `dotnet-sdk-6.0`
- `dotnet-sdk-6.0-source-built-artifacts`
- `dotnet-targeting-pack-6.0`
- `dotnet-templates-6.0`
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
- `NetworkManager`

#### Added Source Packages for AppStream by Oracle

The following source packages have been added to AppStream by Oracle:

- `dtrace`
- `oracle-database-preinstall-21c`
- `python3-dnf-plugin-ulninfo`

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
- `dbxtool`
- `dnf`
- `dnf-plugins-core`
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
- `iproute`
- `iptables`
- `iscsi-initiator-utils`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `kmod-redhat-oracleasm`
- `ksc`
- `libdnf`
- `libgcrypt`
- `libkcapi`
- `libmicrohttpd`
- `libreport`
- `libtirpc`
- `libxml2`
- `libxslt`
- `linux-firmware`
- `mcelog`
- `microcode_ctl`
- `mksh`
- `mokutil`
- `mozjs52`
- `mozjs60`
- `NetworkManager`
- `nvmetcli`
- `opa-ff`
- `opa-fm`
- `OpenIPMI`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`
- `os-prober`
- `parted`
- `policycoreutils`
- `polkit`
- `procps-ng`
- `python3`
- `python-configshell`
- `python-kmod`
- `python-rtslib`
- `redhat-indexhtml`
- `redhat-release`
- `sanlock`
- `selinux-policy`
- `shim`
- `sos`
- `sssd`
- `systemd`
- `trace-cmd`
- `tuned`
- `vim`
- `zstd`

#### Modified AppStream Source Packages

The following source packages from the AppStream upstream release have been modified:

- `abrt`
- `abrt-java-connector`
- `anaconda`
- `anaconda-user-help`
- `ansible-freeipa`
- `authd`
- `binutils`
- `buildah`
- `ceph`
- `clang`
- `cloud-init`
- `cockpit-appstream`
- `cockpit-composer`
- `cockpit-podman`
- `cockpit-session-recording`
- `compat-libgfortran-48`
- `crash`
- `cups-filters`
- `dbus`
- `delve`
- `dleyna-connector-dbus`
- `dnf-plugin-spacewalk`
- `dotnet3.0`
- `dotnet3.1`
- `dotnet5.0`
- `eclipse`
- `eclipse-ecf`
- `eclipse-emf`
- `efi-rpm-macros`
- `fapolicyd`
- `firefox`
- `firewalld`
- `gcc`
- `gcc-toolset-10-binutils`
- `gcc-toolset-10-gcc`
- `gcc-toolset-10-gdb`
- `gcc-toolset-10-systemtap`
- `gcc-toolset-11-binutils`
- `gcc-toolset-11-gcc`
- `gcc-toolset-11-gdb`
- `gcc-toolset-11-systemtap`
- `gcc-toolset-9-binutils`
- `gcc-toolset-9-gcc`
- `gcc-toolset-9-gdb`
- `gcc-toolset-9-systemtap`
- `gdb`
- `glibc`
- `gnome-abrt`
- `gnome-boxes`
- `gnome-initial-setup`
- `gnome-session`
- `gnome-themes-standard`
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
- `libvirt-dbus`
- `libxml2`
- `libxslt`
- `llvm`
- `lorax`
- `lorax-templates-rhel`
- `mecab-ipadic`
- `mpich`
- `nbdkit`
- `NetworkManager`
- `NetworkManager-libreswan`
- `nginx`
- `nodejs`
- `openchange`
- `openscap`
- `open-vm-tools`
- `osbuild-composer`
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
- `pyparted`
- `python2`
- `python3`
- `python36`
- `python-blivet`
- `python-podman`
- `python-pydbus`
- `python-systemd`
- `rear`
- `redfish-finder`
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
- `rshim`
- `rsyslog`
- `rubygem-abrt`
- `sanlock`
- `sblim-cmpi-devel`
- `scap-security-guide`
- `scap-workbench`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `skopeo`
- `sos-collector`
- `spacewalk-abrt`
- `spacewalk-backend`
- `spacewalk-oscap`
- `spacewalk-remote-utils`
- `spacewalk-usix`
- `spice-streaming-agent`
- `sysstat`
- `systemtap`
- `thunderbird`
- `tog-pegasus`
- `trace-cmd`
- `tuned`
- `vim`
- `virt-manager`
- `virt-p2v`
- `WALinuxAgent`
- `wget`
- `xsane`
- `zstd`

#### Modified Source Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `ceph`
- `crash`
- `cups-filters`
- `dotnet5.0-build-reference-packages`
- `gcc`
- `gcc-toolset-10-gcc`
- `glibc`
- `guile`
- `iproute`
- `iscsi-initiator-utils`
- `kmod`
- `libblockdev`
- `libguestfs`
- `libreoffice`
- `libvirt`
- `mozjs52`
- `mozjs60`
- `mpich`
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

- `dotnet6.0`
- `insights-client`
- `redhat-logos`
- `redhat-support-lib-python`
- `redhat-support-tool`
- `rhc`
- `rhc-worker-playbook`
- `rt-tests`
- `spice-qxl-wddm-dod`
- `subscription-manager`
- `subscription-manager-migration-data`
- `toolbox`
- `virtio-win`
- `virt-who`