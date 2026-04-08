---
title: "Release Notes for Oracle Linux 8.7"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol8"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

Release Notes for Oracle Linux 8.7

F71105-04

January 2023

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 8 Release Notes for Oracle Linux 8.7

F71105-04

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2022, 2023, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7/ol8.7-Preface.html -->

[Oracle Linux 8: Release Notes for Oracle Linux
8.7](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7/) provides information about the new features
and known issues in the Oracle Linux 8.7 release. The information applies to both x86\_64 and
64-bit Arm (aarch64) architectures. This document might be updated after it is released.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7/ol8-AboutOracleLinux8.html -->

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

On the x86\_64 platform, Oracle Linux 8.7 release ships with the following default kernel
packages:

- `kernel-4.18.0-425.3.1.el8` (Red Hat Compatible Kernel (RHCK))
- `kernel-uek-5.15.0-3.60.5.1.el8uek` (Unbreakable Enterprise Kernel
  Release 7 (UEK R7))

  For new installations, the UEK R7 is automatically enabled and installed. It also
  becomes the default kernel on first boot.

  On the aarch64 platform, Oracle Linux ships with the UEK kernel only.

  Important:

  If you are upgrading from a previous Oracle Linux 8 version, the kernel is not
  automatically upgraded to UEK R7. See [Installation and Update Changes](ol8-NewFeaturesandChanges.html#ol8-features-install).

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7/ol8-NewFeaturesandChanges.html -->

This chapter describes the new features, major enhancements, bug fixes, and other changes
that are included in this release of Oracle Linux 8.

### Installation and Update Changes

- Instructions when performing system updates

  If you are performing a fresh Oracle Linux 8.7 installation from an ISO image, then after
  the installation completes, the UEK R7 kernel is automatically enabled. However, if the
  system has been registered on ULN, then the UEK R6 ULN channel is enabled by default. See
  [UEK R7 ULN Channel Not Enabled After ULN Registration](ol8-KnownIssues.html#topic_zmp_5ng_mvb)
  for instructions on the steps to complete in this case.

  UEK R7 includes many new features including security and performance enhancements. For
  more details, see [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 7 (5.15.0-0.30)](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/).

  If you choose to use RHCK as your default kernel instead of UEK, ensure that you disable
  UEK repositories or channels on yum or ULN, respectively. For more information about
  switching to RHCK, see Managing Kernels and System Boot in [Oracle Linux 8: Managing Core System Configuration](https://docs.oracle.com/en/operating-systems/oracle-linux/8/osmanage/).

  In the case of updates, switching to UEK R7 is not automatic. If you are upgrading from a
  prior release of Oracle Linux 8, your system will continue to run with the kernel that is
  already installed.

  If your system is currently using UEK R6, the following provides instructions for
  upgrading to UEK R7:

  - Updating by using yum

    When you update to Oracle Linux 8.7, the previous kernel is preserved. At the same
    time, the UEK R7 yum repository is also added to your configuration. To move to the
    latest kernel, run the following commands, depending on the platform you are
    using:

    - On x86\_64 systems:

      ```
      sudo dnf config-manager --disable ol8_UEKR6
      sudo dnf config-manager --enable ol8_UEKR7
      sudo dnf install -y kernel-uek
      sudo dnf update
      ```
    - On aarch64 systems:

      ```
      sudo dnf config-manager -enable ol8_UEKR7
      sudo dnf install -y kernel-uek
      sudo dnf update
      ```
  - Updating by using ULN

    Similar to the previous scenario, the previous kernel is preserved. However, your
    subscriptions might change as a result. You should log in to <https://linux.oracle.com> and ensure that the
    channels that are enabled as well as disabled match what you intend for the updated
    kernel.
  - Users of the aarch64 platform

    In the UEK R7 implementation, the default base page size has changed from 64 KB to 4
    KB. Therefore, updating to UEK R7 might require additional preparations especially in
    connection with prior existing file systems. See the section Information About
    Upgrading From a Previous Oracle Linux or UEK Release to UEK R7 in [Unbreakable Enterprise Kernel: Release Notes for
    Unbreakable Enterprise Kernel Release 7 (5.15.0-0.30)](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/).

  After setting the default kernel, you can further configure kernel boot parameters so
  that these parameters are applied at every system boot. For instructions, see [Oracle Linux 8: Managing Core System Configuration](https://docs.oracle.com/en/operating-systems/oracle-linux/8/osmanage/).

### Operating System and Software Management

The following operating system and software management features and enhancements are
introduced in Oracle Linux 8.7:

- Maximum error file size option available in Rsyslog

  You can now specify a byte-size value for the new
  `action.errorfile.maxsize` option, which prevents the Rsyslog error file
  from exceeding the specified size. Once the maximum file size is reached, further writes
  are prevented to protect the system from excessive file system usage.

### Shells and Command-Line Tools

The following shells and command-line interface (CLI) tools features and improvements are
introduced in Oracle Linux 8.7:

- The `xmlstarlet` package is available in a supported repository

  The `xmlstarlet` package was previously available in the
  `ol8_developer_EPEL` repository, but is now available in the supported
  `ol8_appstream` repository. This package contains utilities that are
  frequently used on the command line to perform common operations on XML files that other
  command line tools are unable to do easily by taking advantage of XPath syntax to properly
  locate, add or modify information within the file.

### Compilers and Development Toolsets

Oracle Linux 8.7 introduces the following features, enhancements, and changes to compilers
and development toolsets.

- Rust Toolset is updated to version 1.62.1

  - You can now use tuple, slice, and struct patterns as the left-hand side of an
    assignment. For example, a tuple assignment can swap two variables:

    ```
    (a, b) = (b, a);
    ```

    Note that
    destructuring assignments with operators such as `+=` are not
    allowed.
  - Inline assembly is available on x86\_64 and aarch64 using the
    `core::arch::asm!` macro.
  - Enums can derive the `Default` trait with an explicitly annotated
    `#[default]` variant.
  - An optimized `futex`-based implementation is used for
    `Mutex`, `CondVar`, and `RwLock`, to
    replace pthreads.
  - Custom exit codes from `main`, including user-defined types that use
    the `Termination` trait, can be used.
  - Cargo supports more control over dependency features. The `dep:`
    prefix can refer to an optional dependency without exposing that as a feature, and a
    `?` only enables a dependency feature if that dependency is enabled
    elsewhere, like `package-name?/feature-name`.
  - A new `cargo add` sub-command for adding dependencies to
    `Cargo.toml` is available.For more details, please see consecutive upstream release announcements, including
  [Rust 1.59.0](https://blog.rust-lang.org/2022/02/24/Rust-1.59.0.html), [Rust 1.60.0](https://blog.rust-lang.org/2022/04/07/Rust-1.60.0.html),[Rust 1.61.0](https://blog.rust-lang.org/2022/05/19/Rust-1.61.0.html),[Rust 1.62.0](https://blog.rust-lang.org/2022/06/30/Rust-1.62.0.html) and [Rust 1.62.1](https://blog.rust-lang.org/2022/07/19/Rust-1.62.1.html).
- LLVM Toolset is updated to version 14.0.0

  - On 64-bit x86, support for `AVX512-FP16` instructions has been added.
  - Support for the Armv9-A, Armv9.1-A and Armv9.2-A architectures has been added.

  This version also includes the following changes in `clang`:

  - `if consteval` for `C++2b` is now implemented.
  - `AVX512-FP16` instructions have been added for the x86\_64 architecture.
  - The `-E -P` preprocessor output now always omits blank lines, matching
    GCC behavior. Previously, up to 8 consecutive blank lines could appear in the output.
  - Support `-Wdeclaration-after-statement` with `C99` and
    later standards, and not just C89, matching GCCâs behavior. A notable use case is
    supporting style guides that forbid mixing declarations and code, but want to move to
    newer C standards.

  For more information, see the [LLVM Toolset](https://releases.llvm.org/14.0.0/docs/ReleaseNotes.html) and [Clang](https://releases.llvm.org/14.0.0/tools/clang/docs/ReleaseNotes.html) upstream release notes.
- Maven 3.8 is now available as a new module stream

  Maven 3.8 as a new `maven:3.8` module stream.

### GCC Toolset 12

Oracle Linux 8.7 provides the GCC Toolset 12, which is an Application Stream that is
distributed in the form of a Software Collection in the `AppStream` repository.
The GCC Toolset is similar to the Oracle Linux Developer Toolset. See <unresolvable-reference.html#ol8-features-developer> for
additional information about changes to compilers and developer toolsets in this release.

The following notable updates to tooling are included in the GCC Toolset 12:

- GCC Toolset 12 supports `_FORTIFY_SOURCE` level 3

  Use the `-D_FORTIFY_SOURCE=3` in the compiler command line when
  building with GCC version 12 or later to improve coverage of source code fortification
  and the security of your applications.
- `binutils` updated to version 2.38

  The
  `binutils` package now supports options that display or warn about the
  presence of multibyte characters, making it easier to create software that is compatible
  with a wide range of languages.

  The `readelf` and
  `objdump` tools automatically follow links to separate
  `debuginfo` files, making it easier to debug programs. This behavior
  can be disabled by using the `--debug-dump=no-follow-links` option for
  `readelf` or the `--dwarf=no-follow-links` option for
  `objdump`.
- Annobin updated to version 10.79

  A new command line option for
  `annocheck` tells it to avoid using the `debuginfod`
  service if it is unable to find debug information in another way. This option can help
  improve performance if the `debuginfod` server is unavailable. Binaries
  built by the Rust 1.18 compiler are now supported by `annocheck`. Annobin
  sources can alternatively be built using `meson` and `ninja`
  if these tools are preferred over `configure` and `make`.
- `gdb` updated to version 11.2

  This update includes many changes to functionality including the addition of several
  new commands and options as well as several feature enhancements. For a complete list of
  updates, see the GDB upstream release notes at <https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;a=blob_plain;f=gdb/NEWS;hb=gdb-11.2-release>.

GCC Toolset 12 is available as an Application Stream within the `AppStream`
repository, in the form of a Software Collection.

To install this toolset, use the following command:

```
sudo dnf install gcc-toolset-12
```

If you previously installed this toolset, use the following
command to upgrade to the latest version:

```
sudo dnf upgrade gcc-toolset-12
```

To run a tool from GCC Toolset 12, use the following command:

```
scl enable gcc-toolset-12 tool
```

The following command initiates a shell session, where tool versions from the GCC Toolset 12
take precedence over system versions of the same tools:

```
scl enable gcc-toolset-12 bash
```

### Database

This release of Oracle Linux 8 ships with version 8.0 of the MySQL database software.

### Dynamic Programming Languages, Web and Database Servers

Oracle Linux 8.7 includes several feature changes and improvements for dynamic programming
languages and web and database servers. Note that this release also introduces several new and
improved module streams:

- Ruby 3.1.2 available as a new module stream

  Ruby 3.1.2 is available in a new `ruby:3.1` module stream. This version
  of Ruby includes several enhancements and performance improvements over the
  `ruby:3.0` module stream, including:

  - An auto-complete feature and a documentation dialog included in the
    `Interactive Ruby` (IRB) utility.
  - New `debug` and `error_highlight` gems to provide
    improved performance, more functionality and more granular control.
  - Values in the hash literal data types and keyword arguments can now be omitted
  - Parentheses can now be omitted in one-line pattern matching and the pin operator
    (`^`) now accepts an expression in pattern matching.
  - YJIT, a new experimental in-process Just-in-Time (JIT) compiler, is now available on
    the AMD and Intel 64-bit architectures
  - The Method Based Just-in-Time Compiler (MJIT) includes several performance
    improvements including an increase in the default maximum JIT cache value for large
    workloads like Rails.
- Mercurial 6.2 available as a new module stream

  Mercurial 6.2 is now available as a new `mercurial:6.2` module stream.
  This version includes several notable changes when compared to the
  `mercurial:4.8` module stream, including:

  - Python 2 is no longer compatible with this version of Mercurial. Mercurial is
    compatible with Python 3.6 or later.
  - A new `-i` option, which enables you to delete ignored files instead
    of untracked files is available for the `hg purge` and `hg
    clean` commands.
  - The `--from <revision>` and `--to
    <revision>` arguments can now be used with the
    `hg diff` and `hg extdiff` commands and a new internal
    merge utility, `internal:mergediff`, is now available.
  - New repositories use The Zstandard (ZSTD) compression by default.
  - A new way of specifying required extensions is now available that makes it impossible
    for Mercurial to start if the required extensions are not found.
  - A new `mercurial-chg` utility is available, which provides a C wrapper
    for the `hg` command. When you use the `chg` command, the
    wrapper is used to provide significant performance improvements.

### File Systems and Storage

Oracle Linux 8.7 provides the following file systems and storage features, enhancements, and
changes:

- Btrfs removed
  from RHCK. The Btrfs file system is removed from RHCK in Oracle Linux 8. As
  such, you cannot create or mount Btrfs file systems when using this kernel. Also,
  note that any Btrfs user space packages that are provided are not supported with
  RHCK.

  Note:

  Support for the Btrfs file system is enabled in UEK R7 and UEK R6. Starting with
  Oracle Linux 8.3, you have the option to create a Btrfs root file system during an
  installation, as well as select Btrfs as the file system type when formatting devices.
  See [Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/) for more information about this feature.

  For more information about managing a Btrfs root file system, see [Oracle Linux 8: Managing Local File Systems](https://docs.oracle.com/en/operating-systems/oracle-linux/8/fsadmin/).

  For changes that have been made to Btrfs in UEK R6, see [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 6 Update 3 (5.4.17-2136)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.3/).

  For changes to Btrfs in UEK R7, see [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 7 (5.15.0-0.30)](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/).
- OCFS2
  removed from RHCK. The Oracle Cluster File System version 2 (OCFS2) file
  system is removed from RHCK in Oracle Linux 8. As such, you cannot create or mount
  OCFS2 file systems when using this kernel. Also, any OCFS2 user space packages that
  are provided are not supported with RHCK.

  Note:

  OCFS2 is fully supported with UEK R6 and UEK R7 in Oracle Linux 8.7.
- `nfsrahead` utility added

  The `nfsrahead` utility, used to modify the `readahead`
  value for NFS mounts, is now available. This utility can help to improve NFS
  performance.
- `rpcctl` command displays SunRPC connection information

  The `rpcctl` command now displays and allows you to show information, add
  and remove objects in the SunRPC `sysfs` files.
- Device Mapper Multipath configuration can be configured per protocol

  You
  can now configure Device Mapper multipath device paths on a per-protocol basis, allowing
  for the optimal configuration of multipath devices accessible through multiple protocols.
  Edit the `multipath.conf` file to specify protocol override configuration.

  ```
  overrides {
          protocol {
                  type "scsi:fcp"
                  dev_loss_tmo 70
                  fast_io_fail_tmo 10
                  eh_deadline 360
          }
          protocol {
                  type "scsi:iscsi"
                  fast_io_fail 120
          }
  }
  ```

  The mandatory `type` attribute is used to match path devices for the
  protocol. The `type` attribute can be set to: `scsi:fcp`,
  `scsi:spi`, `scsi:ssa`, `scsi:sbp`,
  `scsi:srp`, `scsi:iscsi`, `scsi:sas`,
  `scsi:adt`, `scsi:ata`, `scsi:unspec`,
  `ccw`, `cciss`, `nvme`, or
  `undef`. The path device protocol can be determined by running:
  `multipathd show paths format "%d %P"`. Attributes in a matching
  protocol subsection take precedence over attributes in the rest of the overrides section. If
  there are multiple matching protocol subsections, later entries take precedence.

### High Availability and Clusters

The following high availability and clustering features are included in Oracle Linux 8.7:

- `pcs stonith update-scsi-devices` allows updates to multipath SCSI
  devices without restarting the cluster

  The `pcs stonith update-scsi-devices` command can be used to update
  fencing on a cluster by using multipath devices without requiring a restart of other
  cluster resources running on the same node. For example:

  ```
  sudo pcs stonith update-scsi-devices <mpath-fence-dev> set <device-path>
  sudo pcs stonith update-scsi-devices <mpath-fence-dev> add <device-path>
  sudo pcs stonith update-scsi-devices <mpath-fence-dev> remove <device-path>...
  ```
- Pacemaker clusters have UUIDs

  The `pcs` command generates a UUID that you can use to uniquely
  identify the cluster when it is created. The UUID is displayed when you run the
  `pcs cluster config [show]` command. You can add a UUID to an existing
  cluster or regenerate a UUID if one already exists by running `pcs cluster config
  uuid generate`.
- The `multiple-active` resource parameter now accepts a value of
  `stop_unexpected`

  The `multiple-active` resource parameter determines recovery behavior
  when a resource is active on more than one node when it should not be. By default, this
  situation requires a full restart of the resource, even if the resource is running
  successfully where it should be. With this update, the `multiple-active`
  resource parameter accepts a value of `stop_unexpected`, which allows you
  to specify that only unexpected instances of a multiply-active resource are stopped. It
  is the userâs responsibility to verify that the service and its resource agent can
  function with extra active instances without requiring a full restart.
- Pacemaker `allow-unhealthy-node` resource meta-attribute
  added

  The `allow-unhealthy-node` resource meta-attribute can be set to
  `true` to ensure that the resource is not forced off a node due to
  degraded node health. This feature allows the health agent to continue to run on an
  unhealthy node so that the cluster is able to automatically detect when the node becomes
  healthy again, before moving resources back to the node.
- Pacemaker includes Access Control Lists (ACLs) for system groups

  In addition to the ACLs that were previously allows for individual users, Pacemaker
  includes ACLs for system groups to facilitate role-based access controls. The
  `pcs acl group` command can now be used to apply ACLs to system groups.
  For example, to create a read-only ACL for the pcs\_ro\_group system
  group:

  ```
  sudo pcs acl group create pcs_ro_group readonly
  ```
- Pacemaker `--output-format=cmd` option generates command line output
  to recreate fence devices and resources

  Use the `--output-format=cmd` option when running the `pcs
  stonith config` command to generate output of the `pcs`
  commands that you must run on a different system to reconfigure fence devices. You can
  also use this option with the `pcs resource config` command to get a list
  of command to run to reconfigure resources on an alternate system.

### Infrastructure Services

Oracle Linux 8.7 introduces several version updates to infrastructure and command-line
tools, including the following features:

- `samba` rebased to version 4.16.1

  The `samba` packages have been upgraded to upstream version 4.16.1,
  which provides bug fixes and enhancements over the previous version:

  - By default, the `smbd` process automatically starts the new
    `samba-dcerpcd` process on demand to serve Distributed Computing
    Environment / Remote Procedure Calls (DCERPC). Note that Samba 4.16 and later always
    requires `samba-dcerpcd` to use DCERPC. If you disable the `rpc
    start on demand helpers` setting in the `[global]` section in
    the `/etc/samba/smb.conf` file, you must create a
    `systemd` service unit to run `samba-dcerpcd` in
    standalone mode.
  - The Cluster Trivial Database (CTDB) `recovery master` role has been
    renamed to `leader`. As a result, the following `ctdb`
    sub-commands have been renamed:

    - `recmaster` to `leader`
    - `setrecmasterrole` to `setleaderrole`
  - The CTDB `recovery lock` configuration has been renamed to
    `cluster lock`.
  - CTDB now uses leader broadcasts and an associated timeout to determine if an
    election is required.

  Note that the server message block version 1 (SMB1) protocol is deprecated since Samba
  4.11 and will be removed in a future release.

  Back up the database files before starting Samba. When the `smbd`,
  `nmbd`, or `winbind` services start, Samba automatically
  updates its `tdb` database files. Note that Red Hat does not support
  downgrading `tdb` database files.

  After updating Samba, verify the `/etc/samba/smb.conf` file using the
  `testparm` utility.

  For further information about notable changes, read the [upstream release notes](https://www.samba.org/samba/history/samba-4.16.0.html) before updating.

### Security

Oracle Linux 8.7 introduces the following security features, enhancements, and changes:

- NSS no longer supports RSA keys shorter than 1023 bits

  Network Security Services (NSS) libraries are updated to set the minimum key size for
  all RSA operations from 128 to 1023 bits. NSS can no longer generate, sign or verify or
  encypt or decrypt information with RSA keys shorter than 1023 bits.
- SCAP Security Guide updated to 0.1.63

  The SCAP Security Guide (SSG) provides new compliance rules for `sysctl`,
  `grub2`, `pam_pwquality`, and build time kernel
  configuration.
- STIG profile in Oracle Linux 8 is better aligned with DISA STIG

  A DISA STIG profile for Oracle Linux 8 is included in the
  `scap-security-guide` package. This profile is aligned to DISA Oracle
  Linux 8 STIG V1R3 and covers new or updated rules related to the handling of account
  passwords, password quality, checking of home partition mount points, and the
  configurations of `sysctl`. These updated rules ensure greater compliance
  with the DISA's STIG requirements.
- `scap-security-guide` rules for mount options no longer fail if
  `/tmp` and `/var/tmp` partitions do not exist

  SSG rules that previously reported a `fail` result if the
  `/tmp` and `/var/tmp` partitions did not exist on a system
  have been updated to only report a failure if the partitions exist but the system has the
  wrong mount options.
- `fapolicyd` is updated to 1.1.3

  The `fapolicyd` software framework is updated to version 1.1.3 to include
  several enhancements including a change to use the OpenSSL library as the cryptographic
  engine for hash computation and a facility to allow rules to match the parent process ID
  (PPID) of a subject. A fix to the `fagenrules --load` command is also
  included.
- `opencryptoki` is updated to version 3.18.0

  This version includes the following improvements:

  - Default to Federal Information Processing Standards (FIPS) compliant token data
    format (tokversion = 3.12).
  - Enabled restricting usage of mechanisms and keys using a global policy.
  - Enabled statistics counting of mechanism usage.
  - The `ICA/EP11` tokens can use `libica` library version
    4.
  - The `p11sak` tool allows setting different attributes for public and
    private keys.
  - The `C_GetMechanismList` does not return
    `CKR_BUFFER_TOO_SMALL` in the EP11 token.

### Virtualization

The following virtualization features, enhancements, and changes are introduced in Oracle
Linux 8.7:

- `open-vm-tools` updated to 12.0.5

  In this updated version of the open source implementation of VMware Tools, support has
  been added for the Salt Minion tool which is managed through guest OS variables.
- ESXi hypervisor and SEV-ES is now supported

  If you are running Oracle Linux 8.4 or later on VMware's ESXi hypervisor, you
  can now enable the AMD Secure Encrypted Virtualization-Encrypted State (SEV-ES)
  feature to secure your virtual machines. This feature was previously introduced
  as a Technology Preview, but is now fully supported.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7/ol8-TechnologyPreview.html -->

For the Red Hat Compatible Kernel in the current Oracle Linux 8 release, the following
features are under technology preview:

### kexec Fast Reboot

The `kexec fast reboot` feature is available
as a technology preview feature in Oracle Linux 8. This feature
significantly speeds up the boot process by enabling the
kernel to boot directly into the second kernel without having
to first pass through the Basic Input/Output System (BIOS). To
use this feature, load the `kexec` module
first, then reboot the system.

### SGX Available

Software Guard Extensions (SGX) is an Intel technology for
protecting software code and data from disclosure and
modification. The Linux kernel partially supports SGX v1 and
v1.5; version 1 enables platforms by using the Flexible Launch
Control mechanism to use the SGX technology.

### DAX File System Available

In this
release, the DAX file system is available as a Technology Preview for the ext4 and XFS
file systems. DAX enables an application to directly map persistent memory into its
address space. The system must have some form of persistent memory available to use DAX.
Persistent memory can be in the form of one or more Non-Volatile Dual In-line Memory
Modules (NVDIMMs). In addition, a file system that supports DAX must be created on the
NVDIMMs; the file system must be mounted with the `dax` mount option.
Then, an `mmap` of a file on the dax-mounted file system results in a
direct mapping of storage into the applicationâs address space.

### NVMe/TCP available

NVMe over Fabrics
TCP host and the target drivers are included in RHCK as a technology preview in this
release.

Note:

Support for NVMe/TCP is already available in Unbreakable Enterprise Kernel Release
6.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7/ol8-DeprecatedFeatures.html -->

This chapter lists features and functionalities that are deprecated in Oracle Linux 8. While
these features might be currently included and operative in the release, support is not
guaranteed in future major releases. Thus, they should not be used in new Oracle Linux 8
deployments.

### Installation

The following installation related features and functionalities are deprecated in Oracle
Linux 8.

#### Kickstart Commands

- `auth` or `authconfig`
- `device`
- `deviceprobe`
- `dmraid`
- `install`
- `lilo`
- `lilocheck`
- `mouse`
- `multipath`
- `bootloader --upgrade`
- `ignoredisk --interactive`

  Using the `--interactive` option causes a fatal installation error. You
  must remove this option from your kickstart files.
- `partition --active`
- `reboot --kexec`

Even though specific options are listed as deprecated, the base command and the other options
remain available and operative.

### Software Management

The following features and functionalities related to software management are deprecated
in Oracle Linux 8.

#### rpmbuild --sign

Using `rpmbuild --sign` can cause a fatal error in the system. Use the
`rpmsign` command instead.

#### kernelopts Environment Variable

The `kernelopts` environment variable stores the defined kernel command
line parameters for systems that use the GRUB2 bootloader. The variable was stored in
the `/boot/grub2/grubenv` file for each kernel boot entry. The variable
is deprecated and kernel command line parameters are stored in the Boot Loader
Specification (BLS) snippet as a replacement.

### Shells and Command Lines

The following shell and command line components are deprecated in Oracle Linux 8.

#### OpenEXR

As a consequence of the OpenEXR deprecation, the `EXR` image format is no
longer supported in the `imagecodex` module.

#### Dump Utility

With this removal of support for the `dump` utility, use other commands to
back up file systems, for example, `tar`, `dd`, or
`bacula`.

The `restore` component of the `dump` package remains
supported and available as a separate `restore` package.

#### ABRT Tool

The Automatic Bug Reporting Tool (ABRT) is used to detect and report application crashes.
Instead of this tool, use the `systemd-coredump` tool for logging and
storing core dumps that are generated when program crash.

#### ReaR Crontab

The `/etc/cron.d/rear` crontab is deprecated in the `rear`
package. The crontab utility monitors for any changes in the disk layout and runs
`rear mkrescue` if changes are detected. If you require the
`rear` functionality, configure the ReaR utility to run
periodically.

#### SQLite in Bacula

Support is deprecated for SQLite as a database backend of the Bacula backup system. You
should migrate to one of the backends that Bacula supports, such as PostgreSQL or
MySQL.

#### hidepid=n Option

As a `mount` option, `hidepid=n` controls
access to `/proc/[pip]`. The option is incompatible with the
`systemd` infrastructure and might cause certain `systemd`
services to generate SELinux AVC denial messages, which would inhibit completion of other
operations.

#### udev Utility

The deprecated `/usr/lib/udev/rename_device` tool for renaming network devices
should no longer be used in this release.

#### row Command

Use of the deprecated `/usr/bin/row` command in future Oracle Linux
releases might generate errors.

### Security

The following security related features and functionalities are deprecated in Oracle Linux
8.

#### NSS SEED Ciphers

Support for TLS cipher suites that use a SEED cipher is deprecated in the Network
Security Services (NSS) library from Mozilla. If your setup relies on SEED ciphers, you
should enable support for other cipher suites in preparation for the complete removal of
SEED ciphers from NSS.

#### TLS 1.0 and TLS 1.1

These two protocols are disabled in the `DEFAULT` system-wide cryptographic
policy level. If you require these protocols, switch the policy to the `LEGACY`
level as follows:

```
sudo update-crypto-policies --set LEGACY
```

#### DSA

Authentication mechanisms that are based on the deprecated Digital Signature Algorithm (DSA)
keys no longer work in the default configuration. OpenSSH clients do not accept DSA host keys
even when the system-wide cryptographic policy level is set to `LEGACY`.

#### SSL2 Client Hello

Secure Socket Layer 2's `Client Hello` message used to be supported by earlier
versions of the Transport Layer Security (TLS) protocol. Being deprecated in the NSS library,
this feature is now disabled by default.

If your application requires support for `Client Hello`, enable the
feature by using the `SSL_ENABLE_V2_COMPATIBLE_HELLO` API.

#### TPM 1.2

The Trusted Platform Module (TPM) is updated to 2.0 with multiple improvements. However,
the updated version is not backward compatible with earlier versions. Consequently,
version 1.2 is deprecated.

#### crypto-policies

The introduction of scopes for `crypto-policies` directives in custom policies
has resulted in the deprecation of the following derived properties of
`crypto-policies`:

- `tls_cipher`
- `ssh_cipher`
- `ssh_group`
- `ike_protocol`
- `sha1_in_dnssec`

Use of the `protocol` property now requires a scope. For more information,
see the `crypto-policieis(7)` manual page.

#### Runtime disabling of SELinux

Setting the `SELINUX=disabled` option in `/etc/selinux/config`
to disable SELinux at runtime has deprecated support. If you use only this option to disable
SELinux, then SELinux remains enabled but with no loaded policy.

To completely disable SELinux, add the `selinux=0` parameter to the kernel
command line.

#### ipa SELinux module

This module is no longer maintained and hence removed from the
`selinux-policy` package. The functionality is now included in the
`ipa-selinux` package.

#### fapolicyd.rules

Policies for allowing and denying execution rules used to be specified in the
`/etc/fapolicyd/fapolicyd.rules` file. This file is being replaced by
files inside the `/etc/fapolicyd/rules.d` directory.

The `fagenrules` script now merges all component rule files in this
directory to the `/etc/fapolicyd/compiled.rules` file. Rules in
`/etc/fapolicyd/fapolicyd.trust` are still processed by the
`fapolicyd` framework but only for ensuring backward compatibility.

### Networking

The following network related features and functionalities are deprecated in Oracle Linux
8.

#### Network Scripts

Network scripts are no longer available by default. New versions of `ifup`
and `ifdown` scripts call the NetworkManager service through the
`nmcli` tools. Therefore, to run these scripts in Oracle Linux 8, the
NetworkManager service must be running.

Other commands in `/sbin/ifup-local`, `ifdown-pre-local`, and
`ifdown-local` scripts are ignored. If you manually install the legacy
`network-scripts` package and use the scripts, a warning is displayed about
their deprecated state.

#### dropwatch Tool

Instead of the `dropwatch` tool, use the the replacement `perf`
command line tool in future Oracle Linux deployments, which provides the same
functionality.

#### cgdcbxd Package

The deprecated control group data center bridging exchange daemon (`cgdcbxd`)
monitors data center bridging (DCB) netlink events and manages the `net_prio
control` gropu subsystem. Support for this feature might be removed.

#### xinetd Service

The `xinetd` service is replaced by `systemd`.

#### WEP Wi-Fi Connection

Instead of using this connection method, use the Wi-Fi Protected Access 3 (WPA3) or WPA2
connection methods.

#### xt\_u32 Module

The `xt_32` module enables users to match arbitrary 32 bits in the packet
header or payload for their `iptables`. Because this module is
unsupported, migrate to the `nftables` packet filtering framework.

First, change your firewall to use `iptables` with native matches to
incrementally replace individual rules. Then, use the
`iptables-translate` command and accompanying utilities to migrate to
`nftables`. If the `iptables` rules have no native
match in `nftables`, use the raw payload matching feature of
`nftables` instead.

For more information, aee the raw payload expression section in the
`nft(8)` manual page.

### Kernel

The following kernel related features and functionalities are deprecated in Oracle Linux
8.

#### crash-ptdump-command Package

This package is a `ptdump` extension module for the crash utility. The package
is not maintained upstream and is consequently deprecated in this Oracle Linux 8 release.

#### Using Diskless Boot for installing Oracle Linux for Real Time 8

Diskless boot can risk introducing network latency in real-time workloads. Therefore, this
feature for installing Oracle Linux for Real Time 8 is deprecated.

#### Linux firewire subsystems and associated user space comonents

The `firewire` subsystem provides interfaces to use and maintain any resources
on the IEEE 1394 bus. This subsystem is deprecated in the `kernel`
package and likewise, associated user space components that are provided by the
`libavc1394`, `libdc1394`, and
`libram1394` packages.

#### rdma-rxe Driver

Software Remote Direct Memory Access over Converged Ethernet (Soft-RoCE), or RXE,
emulates RDMA. Because of instability issues, this driver is now deprecated.

### File Systems and Storage

The following features and functionalities related to file systems and storage are deprecated
in Oracle Linux 8.

#### VDO Write Modes

- `sync`
- `async-unsafe`
- `auto`

In place of these modes, `async` is the recommended write mode to use.

#### cramfs Kernel Module

In place of the deprecated `cramfs` kernel module, use
`squashfs`, which is the recommended replacement.

#### VDO Manager

The VDO Manager is deprecated and is replaced by the LVM-VDO integration. To create VDO
volumes, preferably use the `lvcreate` command instead.

You can use the `/usr/sbin/lvm_import_vdo` script in the `lvm2`
package to convert existing volumes that were created with the VDO Manager. In this manner,
these volumes can be managed through the LVM-VDO integration.

#### elevator Kernel Command

The `elevator` kernel command line parameter sets the disk scheduler for all
devices. If you require a different scheduler than what the kernel automatically selects, use
`udev` rule or the TuneD service to configure your preferred scheduler.

#### LVM Mirror

Instead of the deprecated LVM `mirror` segment type, use LVM RAID 1 devices
with the `raid1` segment type for similar functionality.

#### peripety Package

The `peripety` package is deprecated. The Peripety storage event
notification daemon parses system storage logs into structured storage events to enable
you investigate storage issues.

### High Availability and Clusters

The following features and functionalities that related to high availability and clusters
are deprecated in Oracle Linux 8.

#### pcs Commands Support for clufter Tool

The `clufter` tool is used for analyzing cluster configuration formats.
The `pcs` commands that support the `clufter` tool are
deprecated. Using these commands generate a warning about their deprecations. Sections
that are related to these commands are removed from the `pcs` help
display as well as the `pcs(8)` manual page.

Specifically, the following commands are deprecated:

- `pcs config import-cman`
- `pcs config export`

### Compilers and Development Tools

The following compilers and development tools are deprecated in Oracle Linux 8.

#### libdwarf Library

In place of the deprecated `libdwarf` library, use the
`elfutils` and `libdw` libraries for applications that
need to process ELF/DWARF files.

As an alternative to the `libdwarf-tools dwarfdump` program, you can use
the `binutils readelf` program or the `elfutils
eu-readelf` program. Both programs can be used by passing the
`--debug-dump` flag.

#### gdb.i686 Packages

These packages were distributed in earlier Oracle Linux releases to support 32-bit
versions of the GNU Debugger (GDB). With the removal of support for 32-bit hardware,
these packages are no longer supported or available. The 64-bit version of GDB in
`gdb.x86_64` packages can debug 32-bit applications.

### Desktop

The following desktop related features and functionalities are deprecated in Oracle Linux
8.

#### libgnome-keyring Library

The `libgnome-keyring`library is deprecated in favor of the
`libsecret` library, which is more compliant with security
standards.

#### Motif Toolkit

The Motif widget tool is deprecated, including the following packages:

- `motif`
- `openmotif`
- `openmotif21`
- `openmotif22`

Likewise, the `motif-static` package has been removed. In place of Motif,
use the GTK toolkit.

### Virtualization

The following virtualization related features and functionalities are deprecated in Oracle
Linux 8.

#### Web Console Translation Support

The web console no longer performs translations for languages whose available
translations are less than 50% of the console's translatable strings. For these
languages, the user interface will be in English.

#### virsh iface-\* Commands

`virsh iface-*` commands such as `virsh iface-start`,
`virsh iface-destroy`, and so on are deprecated. To configure and
manage host network connections, use instead the NetworkManager tool and its related
management applications, for example `nmcli`.

#### Virtual Machine Manager

In place of the deprecated Virtual Machine Manager (`virt-manager`), use
the web console, otherwise known as Cockpit.

#### Virtual Machine Snapshots

Support for creating snapshots of VMs is limited only to those that do not use UEFI
firmware. However, the operation might cause the QEMU monitor to become blocked and
affects hypervisor operations.

As an alternative, use external snapshots.

#### Cirrus VGA Virtual GPU Type

The Cirrus VGA GPU device is deprecated and support for it might be removed in KVM
virtual machines. In its place, use `stdvga`,
`virtio-vga`, or `qxi` devices.

#### Signatures Using SHA-1

The use of SHA1-based signatures to perform SecureBoot image verification on UEFI
(PE/COFF) executables is deprecated. Instead, use signatures that are based on SHA-2 or
later.

#### SPICE Remote Display Protocol

With the deprecation of the SPICE remote display protocol, the functionality of attaching
smart card readers to virtual machines (VMs) will be provided by third party remote
virtualization solutions.

Additionally, the deprecation of this protocol has the following consequences:

- For remote console access, use the VNC protocol.
- For advanced remote display functions, use third party tools such as RDP, HP RGS, or
  Mechdyne TGX.

### Containers

The following features and functionalities that are related to containers are deprecated in
Oracle Linux 8.

#### container-tools Modules

The `container-tools:1.0` and `container-tools:2.0` modules
are deprecated and no longer support security updates.

Use newer supported stable module streams, such as `container-tools:3.0`
instead.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7/ol8-KnownIssues.html -->

This chapter lists known issues in the current Oracle Linux 8 release. The list covers issues
that might affect both x86 and aarch64 platforms. In the list, additional issues that are
specific only to aarch64 platforms are labeled `aarch64 only:`.

The following guides provide additional information about known issues that related to
specific Oracle Linux components:

- Podman container management tool: [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/)
- System and Oracle Cloud Infrastructure instance upgrade using Leapp: [Oracle Linux 8: Performing System Upgrades With Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/8/leapp/)

### Installation and Upgrade Issues

The following are known installation and upgrade issues for
Oracle Linux 8.6.

#### UEK R7 ULN Channel Not Enabled After ULN Registration

After Oracle Linux 8.7 is newly installed, UEK R7 is installed as the default kernel.
However, if the system is registered on ULN, the UEK R6 ULN channel is enabled by
default. To obtain security updates for the default kernel on an Oracle Linux 8.7, the
ULN subscriptions must be manually updated to disable the UEK R6 channel and to enable
the UEK R7 channel. See [Installation and Update Changes](ol8-NewFeaturesandChanges.html#ol8-features-install) for more information on this change.

Log into <https://linux.oracle.com> with your ULN user name and password and click on
the Systems tab to select the system that you have registered to ULN. Go to the Manage Subscriptions page and update the channel
subscriptions for the system. For example, disable access to the
`ol8_x86_64_UEKR6`, and enable access to the
`ol8_x86_64_UEKR7` channel. Click on Save
Subscriptions to save your changes.

(Bug ID 34711928)

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

#### Package conflict between usbguard-1.0.0-2.el8.i686 and usbguard-1.0.0-8.el8.x86\_64 on Oracle Linux 8 upgrades

Beginning with Oracle Linux 8.5, when you upgrade Oracle Linux 8 with both the
`ol8_baseos_latest` and `ol8_appstream` yum repositories
enabled, a conflict between the `usbguard-1.0.0-2.el8.i686` and
`usbguard-1.0.0-8.el8.x86_64` packages occurs.

The following error is produced:

```
Problem: package usbguard-1.0.0-8.el8.x86_64 conflicts with usbguard
provided by usbguard-1.0.0-2.el8.i686
  - cannot install the best candidate for the job
  - problem with installed package usbguard-1.0.0-2.el8.i686
(try to add '--allowerasing' to command line to replace conflicting packages
or '--skip-broken' to skip uninstallable packages or '--nobest' to use not
only best candidate packages)
```

This conflict occurs because in Oracle Linux 8.6 and later releases, the
`usbguard-1.0.0-2.el8.i686` and the
`usbguard-1.0.0-8.el8.x86_64` packages conflict with each other and could no
longer be installed together, unlike in previous Oracle Linux 8 releases.

To work around this issue, remove the
`usbguard-1.0.0-2.el8.i686` package from your
Oracle Linux 8 system prior to upgrading to the current release.

(Bug ID 34097708)

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

#### aarch64 only: Installer displays error: 'Failed to set new efi boot target' on systems with a multipath-enabled NVMe controller"

The Oracle Linux 8.7 installer displays the following error on
aarch64 systems that have a multipath-enabled NVMe controller:

```
Failed to set new efi boot target . This is most likely a kernel or firmware bug.
```

To work around this issue, disable native multipath support
for the installation at boot time by adding the
`nvme_core.multipath=N` command-line argument
on the target system.

(Bug IDs 34233800, 34215333, 31758304)

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

However, this issue is fixed in UEK R7. Therefore, to work around this issue, enable the UEK
R7 yum repository or ULN channel, and then install UEK R7. Reboot the system after the
installation.

(Bug ID 32005190)

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

(Bug ID 31274238, 34211826, 34312626)

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

### Certain SEV guest configurations might cause hypervisor CPU soft-lockup warnings

On older generation AMD systems that are based on the AMD Rome processors, such as E2 and
E3 systems, a guest with more than 350GB memory that is configured to use Secure
Encrypted Virtualization (SEV) memory encryption can trigger a CPU soft-lockup warning
on the hypervisor host during guest boot or shutdown operations.

The time that is needed to flush the pinned memory that is being encrypted is
proportional to the amount of guest memory. However, with larger amounts of memory in
excess of 350GB, the time on the CPU to flush the memory becomes excessive, which
consequently triggers a warning. After the memory is flushed, the hypervisor resumes
normal operations.

Newer systems that are based on the AMD Milan processor, such as E4 systems, have
hardware support that can minimize the time required for flushing the memory. Therefore,
the CPU soft-hang issue is not encountered.

As a workaround, if a SEV enabled guest with more then 350GB of memory is required,
create the guest on a system that is based on the AMD Milan processor. If you are using
systems with the AMD Rome processor, limit the guest memory to less than 350GB if the
guest is configured with SEV memory encryption.

(Bug ID 34050377)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.7/ol8-PackageChangesfromtheUpstreamRelease.html -->

The following sections list the changes to binary and source
packages from the upstream release.

### Changes to Binary Packages

This section contains information about the removed, modified, and new binary packages in this release. For information about the source package changes, see [Changes to Source Packages](ol8-PackageChangesfromtheUpstreamRelease.html#ol8-packages-source) .

#### Added Binary Packages for BaseOS by Oracle

The following binary packages have been added to BaseOS by Oracle:

- `bcache-tools`
- `btrfs-progs`
- `dtrace`
- `iwlax2xx-firmware`
- `kernel-uek`
- `kernel-uek-core`
- `kernel-uek-debug`
- `kernel-uek-debug-core`
- `kernel-uek-debug-devel`
- `kernel-uek-debug-modules`
- `kernel-uek-debug-modules-extra`
- `kernel-uek-devel`
- `kernel-uek-doc`
- `kernel-uek-modules`
- `kernel-uek-modules-extra`
- `linux-firmware-core`
- `NetworkManager-config-connectivity-oracle`
- `ocfs2-tools`
- `oracle-backgrounds`
- `oracle-indexhtml`
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

The following binary packages have been added to CodeReady Linux Builder by Oracle:

- `qemu-kvm-tests`
- `shim-unsigned-ia32`

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
- `ctdb`
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
- `expat`
- `expat-devel`
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
- `glib2`
- `glib2-devel`
- `glib2-fam`
- `glib2-tests`
- `glibc`
- `glibc-all-langpacks`
- `glibc-common`
- `glibc-devel`
- `glibc-doc`
- `glibc-gconv-extra`
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
- `iwlax2xx-firmware`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `kmod-libs`
- `kmod-redhat-oracleasm`
- `krb5-devel`
- `krb5-libs`
- `krb5-pkinit`
- `krb5-server`
- `krb5-server-ldap`
- `krb5-workstation`
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
- `libkadm5`
- `libkcapi`
- `libkcapi-hmaccalc`
- `liblsan`
- `libnsl`
- `libquadmath`
- `libreport-filesystem`
- `libsmbclient`
- `libsss_autofs`
- `libsss_certmap`
- `libsss_idmap`
- `libsss_nss_idmap`
- `libsss_simpleifp`
- `libsss_sudo`
- `libstdc++`
- `libtsan`
- `libubsan`
- `libwbclient`
- `libxslt`
- `libzstd`
- `libzstd-devel`
- `linux-firmware`
- `linux-firmware-core`
- `mcelog`
- `microcode_ctl`
- `mozjs52`
- `mozjs60`
- `NetworkManager`
- `NetworkManager-adsl`
- `NetworkManager-bluetooth`
- `NetworkManager-config-connectivity-oracle`
- `NetworkManager-config-server`
- `NetworkManager-dispatcher-routing-rules`
- `NetworkManager-initscripts-updown`
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
- `python3-openipmi`
- `python3-policycoreutils`
- `python3-rtslib`
- `python3-samba`
- `python3-samba-test`
- `python3-sss`
- `python3-sssdconfig`
- `python3-sss-murmur`
- `python3-test`
- `python3-urllib3`
- `redhat-release`
- `samba`
- `samba-client`
- `samba-client-libs`
- `samba-common`
- `samba-common-libs`
- `samba-common-tools`
- `samba-krb5-printing`
- `samba-libs`
- `samba-pidl`
- `samba-test`
- `samba-test-libs`
- `samba-winbind`
- `samba-winbind-clients`
- `samba-winbind-krb5-locator`
- `samba-winbind-modules`
- `samba-winexe`
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
- `unzip`
- `vim-minimal`
- `yum`
- `yum-utils`

#### Modified Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `anaconda-widgets-devel`
- `crash-devel`
- `cups-filters-devel`
- `dconf-devel`
- `dotnet-sdk-3.1-source-built-artifacts`
- `dotnet-sdk-5.0-source-built-artifacts`
- `dotnet-sdk-6.0-source-built-artifacts`
- `dotnet-sdk-7.0-source-built-artifacts`
- `fwupd-devel`
- `galera`
- `gcc-plugin-devel`
- `gcc-toolset-10-gcc-plugin-devel`
- `glib2-doc`
- `glib2-static`
- `glibc-benchtests`
- `glibc-nss-devel`
- `glibc-static`
- `guile-devel`
- `iscsi-initiator-utils-devel`
- `Judy`
- `Judy-devel`
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
- `libcephfs2`
- `libcephfs-devel`
- `libdnf-devel`
- `librados-devel`
- `libradosstriper1`
- `libradosstriper-devel`
- `librbd-devel`
- `libreoffice-sdk`
- `libreoffice-sdk-doc`
- `libsmbclient-devel`
- `libsss_nss_idmap-devel`
- `libstdc++-static`
- `libvirt`
- `libvirt-client`
- `libvirt-daemon`
- `libvirt-daemon-config-network`
- `libvirt-daemon-config-nwfilter`
- `libvirt-daemon-driver-interface`
- `libvirt-daemon-driver-network`
- `libvirt-daemon-driver-nodedev`
- `libvirt-daemon-driver-nwfilter`
- `libvirt-daemon-driver-secret`
- `libvirt-daemon-driver-storage`
- `libvirt-daemon-driver-storage-core`
- `libvirt-daemon-driver-storage-disk`
- `libvirt-daemon-driver-storage-iscsi`
- `libvirt-daemon-driver-storage-iscsi-direct`
- `libvirt-daemon-driver-storage-logical`
- `libvirt-daemon-driver-storage-mpath`
- `libvirt-daemon-driver-storage-scsi`
- `libvirt-devel`
- `libvirt-docs`
- `libvirt-libs`
- `libvirt-nss`
- `libvirt-wireshark`
- `libwbclient-devel`
- `mariadb`
- `mariadb-backup`
- `mariadb-common`
- `mariadb-devel`
- `mariadb-embedded`
- `mariadb-embedded-devel`
- `mariadb-errmsg`
- `mariadb-gssapi-server`
- `mariadb-oqgraph-engine`
- `mariadb-server`
- `mariadb-server-galera`
- `mariadb-server-utils`
- `mariadb-test`
- `mozjs52-devel`
- `mozjs60-devel`
- `NetworkManager-libnm-devel`
- `nss_hesiod`
- `ocaml-libguestfs`
- `ocaml-libguestfs-devel`
- `OpenIPMI-devel`
- `openscap-engine-sce-devel`
- `PackageKit`
- `PackageKit-glib-devel`
- `parted-devel`
- `python3-mpich`
- `samba-devel`
- `sanlock-devel`
- `sblim-cmpi-devel`
- `sendmail-milter-devel`
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
- `ansible-pcp`
- `aspnetcore-runtime-3.0`
- `aspnetcore-runtime-3.1`
- `aspnetcore-runtime-5.0`
- `aspnetcore-runtime-6.0`
- `aspnetcore-runtime-7.0`
- `aspnetcore-targeting-pack-3.0`
- `aspnetcore-targeting-pack-3.1`
- `aspnetcore-targeting-pack-5.0`
- `aspnetcore-targeting-pack-6.0`
- `aspnetcore-targeting-pack-7.0`
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
- `containernetworking-plugins`
- `containers-common`
- `cpp`
- `crash`
- `cups-filters`
- `cups-filters-libs`
- `dbus-devel`
- `dbus-x11`
- `dconf`
- `delve`
- `dnf-plugin-spacewalk`
- `dotnet`
- `dotnet-apphost-pack-3.0`
- `dotnet-apphost-pack-3.1`
- `dotnet-apphost-pack-5.0`
- `dotnet-apphost-pack-6.0`
- `dotnet-apphost-pack-7.0`
- `dotnet-host`
- `dotnet-hostfxr-3.0`
- `dotnet-hostfxr-3.1`
- `dotnet-hostfxr-5.0`
- `dotnet-hostfxr-6.0`
- `dotnet-hostfxr-7.0`
- `dotnet-runtime-3.0`
- `dotnet-runtime-3.1`
- `dotnet-runtime-5.0`
- `dotnet-runtime-6.0`
- `dotnet-runtime-7.0`
- `dotnet-sdk-3.0`
- `dotnet-sdk-3.1`
- `dotnet-sdk-5.0`
- `dotnet-sdk-6.0`
- `dotnet-sdk-7.0`
- `dotnet-targeting-pack-3.0`
- `dotnet-targeting-pack-3.1`
- `dotnet-targeting-pack-5.0`
- `dotnet-targeting-pack-6.0`
- `dotnet-targeting-pack-7.0`
- `dotnet-templates-3.0`
- `dotnet-templates-3.1`
- `dotnet-templates-5.0`
- `dotnet-templates-6.0`
- `dotnet-templates-7.0`
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
- `eth-tools-basic`
- `eth-tools-fastfabric`
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
- `gcc-plugin-annobin`
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
- `gcc-toolset-11-gdb`
- `gcc-toolset-11-gdb-doc`
- `gcc-toolset-11-gdb-gdbserver`
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
- `gcc-toolset-12-gdb`
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
- `idm-pki-acme`
- `idm-pki-base`
- `idm-pki-base-java`
- `idm-pki-ca`
- `idm-pki-kra`
- `idm-pki-server`
- `idm-pki-symkey`
- `idm-pki-tools`
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
- `Judy`
- `kernel-rpm-macros`
- `kernelshark`
- `ksh`
- `leapp-upgrade-el8toel9`
- `leapp-upgrade-el8toel9-dep`
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
- `libguestfs-appliance`
- `libguestfs-bash-completion`
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
- `libvirt-wireshark`
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
- `netstandard-targeting-pack-2.1`
- `NetworkManager-cloud-setup`
- `nginx`
- `nginx-all-modules`
- `nginx-filesystem`
- `nginx-mod-devel`
- `nginx-mod-http-image-filter`
- `nginx-mod-http-perl`
- `nginx-mod-http-xslt-filter`
- `nginx-mod-mail`
- `nginx-mod-stream`
- `npm`
- `openchange`
- `openscap`
- `openscap-devel`
- `openscap-engine-sce`
- `openscap-python3`
- `openscap-scanner`
- `openscap-utils`
- `open-vm-tools`
- `open-vm-tools-desktop`
- `open-vm-tools-salt-minion`
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
- `python2-debug`
- `python2-devel`
- `python2-libs`
- `python2-test`
- `python2-tkinter`
- `python2-tools`
- `python3-abrt`
- `python3-abrt-addon`
- `python3-abrt-container-addon`
- `python3-abrt-doc`
- `python3-blivet`
- `python3-blockdev`
- `python3-clang`
- `python3-dnf-plugin-modulesync`
- `python3-dnf-plugin-spacewalk`
- `python3-idle`
- `python3-idm-pki`
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-ipatests`
- `python3-kickstart`
- `python3-libguestfs`
- `python3-libreport`
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
- `ruby-libguestfs`
- `samba-vfs-iouring`
- `sanlk-reset`
- `sanlock`
- `scap-security-guide`
- `scap-security-guide-doc`
- `scap-workbench`
- `sendmail`
- `sendmail-cf`
- `sendmail-doc`
- `sendmail-milter`
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
- `sssd-idp`
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
- `tuned-profiles-postgresql`
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
- `WALinuxAgent`
- `WALinuxAgent-udev`
- `wget`
- `xdg-desktop-portal`
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
- `redhat-indexhtml`
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
- `coreos-installer`
- `coreos-installer-bootinfra`
- `coreos-installer-dracut`
- `insights-client`
- `libreport-plugin-rhtsupport`
- `libreport-rhel`
- `libreport-rhel-anaconda-bugzilla`
- `libreport-rhel-bugzilla`
- `redhat-backgrounds`
- `redhat-cloud-client-configuration`
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

The following binary packages from the CodeReady Linux Builder upstream release have been removed:

- `asio`
- `Cython`
- `Cython-debugsource`
- `galera-debuginfo`
- `galera-debugsource`
- `hivex-debuginfo`
- `hivex-debugsource`
- `Judy-debuginfo`
- `Judy-debugsource`
- `libiscsi-debuginfo`
- `libiscsi-debugsource`
- `libiscsi-utils-debuginfo`
- `libnbd-debuginfo`
- `libnbd-debugsource`
- `libserf-debuginfo`
- `libserf-debugsource`
- `libvirt-client-debuginfo`
- `libvirt-daemon-debuginfo`
- `libvirt-daemon-driver-interface-debuginfo`
- `libvirt-daemon-driver-network-debuginfo`
- `libvirt-daemon-driver-nodedev-debuginfo`
- `libvirt-daemon-driver-nwfilter-debuginfo`
- `libvirt-daemon-driver-secret-debuginfo`
- `libvirt-daemon-driver-storage-core-debuginfo`
- `libvirt-daemon-driver-storage-disk-debuginfo`
- `libvirt-daemon-driver-storage-iscsi-debuginfo`
- `libvirt-daemon-driver-storage-iscsi-direct-debuginfo`
- `libvirt-daemon-driver-storage-logical-debuginfo`
- `libvirt-daemon-driver-storage-mpath-debuginfo`
- `libvirt-daemon-driver-storage-scsi-debuginfo`
- `libvirt-dbus-debuginfo`
- `libvirt-dbus-debugsource`
- `libvirt-debuginfo`
- `libvirt-debugsource`
- `libvirt-libs-debuginfo`
- `libvirt-nss-debuginfo`
- `libvirt-python-debugsource`
- `libvirt-wireshark-debuginfo`
- `mariadb-backup-debuginfo`
- `mariadb-debuginfo`
- `mariadb-debugsource`
- `mariadb-embedded-debuginfo`
- `mariadb-gssapi-server-debuginfo`
- `mariadb-oqgraph-engine-debuginfo`
- `mariadb-server-debuginfo`
- `mariadb-server-utils-debuginfo`
- `mariadb-test-debuginfo`
- `mod_dav_svn-debuginfo`
- `nbdfuse-debuginfo`
- `netcf-debuginfo`
- `netcf-debugsource`
- `netcf-libs-debuginfo`
- `ocaml-hivex-debuginfo`
- `ocaml-libguestfs-debuginfo`
- `ocaml-libnbd-debuginfo`
- `perl-hivex-debuginfo`
- `perl-Sys-Virt-debuginfo`
- `perl-Sys-Virt-debugsource`
- `pybind11`
- `pytest`
- `python39-Cython-debuginfo`
- `python3-hivex-debuginfo`
- `python3-libnbd-debuginfo`
- `python3-libvirt-debuginfo`
- `python3x-pyparsing`
- `python-atomicwrites`
- `python-attrs`
- `python-iniconfig`
- `python-more-itertools`
- `python-packaging`
- `python-pluggy`
- `python-py`
- `python-wcwidth`
- `ruby-hivex-debuginfo`
- `SLOF`
- `subversion-debuginfo`
- `subversion-debugsource`
- `subversion-devel-debuginfo`
- `subversion-gnome-debuginfo`
- `subversion-libs-debuginfo`
- `subversion-perl-debuginfo`
- `subversion-ruby-debuginfo`
- `subversion-tools-debuginfo`
- `utf8proc-debuginfo`
- `utf8proc-debugsource`

### Changes to Source Packages

This section contains information about the removed, modified, and new source packages in this release. For information about the binary package changes, see [Changes to Binary Packages](ol8-PackageChangesfromtheUpstreamRelease.html#ol8-packages-binary) .

#### Added Source Packages for BaseOS by Oracle

The following source packages have been added to the BaseOS by Oracle:

- `bcache-tools`
- `btrfs-progs`
- `dtrace`
- `kernel-uek`
- `ocfs2-tools`
- `oracle-indexhtml`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`

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
- `expat`
- `firewalld`
- `fuse`
- `fwupd`
- `fwupdate`
- `gcc`
- `glib2`
- `glibc`
- `grub2`
- `grubby`
- `iptables`
- `iscsi-initiator-utils`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `kmod-redhat-oracleasm`
- `krb5`
- `ksc`
- `libdnf`
- `libkcapi`
- `libreport`
- `libxslt`
- `linux-firmware`
- `mcelog`
- `microcode_ctl`
- `mozjs52`
- `mozjs60`
- `NetworkManager`
- `nvmetcli`
- `opa-ff`
- `opa-fm`
- `OpenIPMI`
- `os-prober`
- `parted`
- `policycoreutils`
- `polkit`
- `procps-ng`
- `python3`
- `python-configshell`
- `python-rtslib`
- `python-urllib3`
- `redhat-release`
- `samba`
- `sanlock`
- `selinux-policy`
- `shim`
- `sos`
- `sssd`
- `systemd`
- `trace-cmd`
- `tuned`
- `unzip`
- `vim`
- `zstd`

#### Modified AppStream Source Packages

The following source packages from the AppStream upstream release have been modified:

- `abrt`
- `abrt-java-connector`
- `anaconda`
- `anaconda-user-help`
- `ansible-pcp`
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
- `dconf`
- `delve`
- `dnf-plugins-core`
- `dnf-plugin-spacewalk`
- `dotnet3.0`
- `dotnet3.1`
- `dotnet5.0`
- `dotnet6.0`
- `dotnet7.0`
- `eclipse`
- `eclipse-ecf`
- `eclipse-emf`
- `efi-rpm-macros`
- `eth-tools`
- `fapolicyd`
- `firefox`
- `firewalld`
- `gcc`
- `gcc-toolset-10-gcc`
- `gcc-toolset-11-binutils`
- `gcc-toolset-11-gcc`
- `gcc-toolset-11-gdb`
- `gcc-toolset-12-gdb`
- `gdb`
- `glibc`
- `gnome-boxes`
- `gnome-session`
- `gnome-themes-standard`
- `guile`
- `httpd`
- `icedtea-web`
- `initial-setup`
- `ipa`
- `Judy`
- `ksh`
- `leapp-repository`
- `libblockdev`
- `libguestfs`
- `libreoffice`
- `libreport`
- `libreswan`
- `libvirt`
- `libxslt`
- `llvm`
- `lorax`
- `lorax-templates-rhel`
- `mecab-ipadic`
- `mpich`
- `NetworkManager`
- `nginx`
- `nodejs`
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
- `python-blivet`
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
- `samba`
- `sanlock`
- `sblim-cmpi-devel`
- `scap-security-guide`
- `scap-workbench`
- `sendmail`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `skopeo`
- `sos-collector`
- `spacewalk-backend`
- `spacewalk-oscap`
- `spacewalk-remote-utils`
- `spacewalk-usix`
- `spice-streaming-agent`
- `sssd`
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
- `xdg-desktop-portal`
- `xsane`
- `zstd`

#### Modified Source Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `anaconda`
- `ceph`
- `crash`
- `cups-filters`
- `dconf`
- `dotnet3.1`
- `dotnet5.0`
- `dotnet6.0`
- `dotnet7.0`
- `fwupd`
- `galera`
- `gcc`
- `gcc-toolset-10-gcc`
- `glib2`
- `glibc`
- `guile`
- `iscsi-initiator-utils`
- `Judy`
- `kmod`
- `libblockdev`
- `libdnf`
- `libguestfs`
- `libreoffice`
- `libvirt`
- `mariadb`
- `mozjs52`
- `mozjs60`
- `mpich`
- `NetworkManager`
- `OpenIPMI`
- `openscap`
- `PackageKit`
- `parted`
- `samba`
- `sanlock`
- `sblim-cmpi-devel`
- `sendmail`
- `sssd`
- `tog-pegasus`

#### Removed BaseOS Source Packages

The following source packages from the BaseOS upstream release have been removed:

- `kpatch`
- `libica`
- `redhat-indexhtml`
- `redhat-logos`
- `subscription-manager`

#### Removed AppStream Source Packages

The following source packages from the AppStream upstream release have been removed:

- `ansible-collection-microsoft-sql`
- `ansible-collection-redhat-rhel_mgmt`
- `coreos-installer`
- `insights-client`
- `libica`
- `redhat-cloud-client-configuration`
- `redhat-logos`
- `redhat-support-lib-python`
- `redhat-support-tool`
- `rhc`
- `rhc-worker-playbook`
- `rt-tests`
- `spice-client-win`
- `spice-qxl-wddm-dod`
- `spice-vdagent-win`
- `subscription-manager`
- `subscription-manager-migration-data`
- `toolbox`
- `virtio-win`
- `virt-who`