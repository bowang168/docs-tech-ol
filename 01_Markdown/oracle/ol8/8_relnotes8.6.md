---
title: "Release Notes for Oracle Linux 8.6"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.6"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol8"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

Release Notes for Oracle Linux 8.6

F55530-06

November 2022

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 8 Release Notes for Oracle Linux 8.6

F55530-06

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2022, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.6/ol8.6-Preface.html -->

[Oracle Linux 8: Release Notes for Oracle Linux
8.6](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.6/) provides information about the new
features and known issues in the Oracle Linux 8.6 release. The information applies to
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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.6/ol8-AboutOracleLinux8.html -->

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

For the x86\_64 platform, Oracle Linux 8.6 ships with the following default kernel packages:

- `kernel-4.18.0-372.9.1.el8` (Red Hat Compatible Kernel (RHCK))
- `kernel-uek-5.4.17-2136.307.3` (Unbreakable Enterprise Kernel
  Release 6 (UEK R6))

  For new installations, the UEK kernel is automatically
  enabled and installed. It also becomes the default kernel on
  first boot.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.6/ol8-NewFeaturesandChanges.html -->

This chapter describes the new features, major enhancements, bug fixes, and other changes
that are included in this release of Oracle Linux 8.

### Installation

The following installation changes are introduced in Oracle Linux 8.6:

- Image Builder includes capability to customize file system partition on LVM. If
  you have more than one partition, this feature enhancement enables you to create images
  with a customized file system partition on LVM and then resize those partitions at
  runtime. To do so, you would specify a customized file system configuration in your
  blueprint and then create images with the desired disk layout. The default file system
  layout remains unchanged; also, if you use plain images without file system customization,
  the `root` partition is resized by `cloud-init`.

### --secontext Option of strace Enhanced to Include Mismatch Parameter

For
the Red Hat Compatible Kernel (`rhck)`, the `--secontext` option
of the `strace` utility has been enhanced to include a mismatch parameter.
This parameter enables you to print the expected context, along with the actual context upon
mismatch only. The output is separated by double exclamation marks (`!!`), with
the actual context appearing first, followed by the expected context.

### Software Management

The following software management features and enhancements are
introduced in Oracle Linux 8.6:

- New modulesync command for replacing certain workflows. You
  cannot install modular packages in Oracle Linux 8.6 without modular metadata. In previous
  releases, you could use the `dnf` command to download packages, and
  then use the `createrepo_c` command to redistribute those packages.
  With this enhancement, the `modulesync` command is introduced. This
  command is used to ensure the presence of modular metadata, which ensures package
  installability. The command downloads `rpm` packages from modules and then
  creates a repository with modular metadata inside a working directory.
- New --path option added to RPM. In Oracle Linux 8.6, you
  can use the new `--path` option to query packages by specifying a file that
  is currently not installed. This option is similar to the existing `--file`
  option; however, the new option matches packages solely based on the provided path. Note
  that the file specified by that path does not need to exist on disk.

  The `--path` option can be useful when you
  exclude all of the documentation files at installation time
  by specifying the `--nodocs` option with
  the `dnf` command. In this case, you can
  opt to use the `--path` option to display
  the owning package of such an excluded file. The
  `--file` option does not display the
  package because the requested file does not exist.

### Shells and Command-Line Tools

The following shells and command-line interface (CLI) tools
features and improvements are introduced in Oracle Linux 8.6:

- lsvpd package updated to version 1.7.13. The
  `lsvpd` package has been updated to version 1.7.13. This update provides
  some bug fixes and enhancements over the previous version.
- net-snmp-cert gencert tool uses the SHA512 encryption algorithm
  instead of SHA1. The `net-snmp-cert gencert` tool has been
  updated to generate certificates by using SHA512 encryption algorithm. This change
  provides for increased security.
- dnn
  and text modules now available in the opencv package. The `dnn`
  module that contains the Deep Neural Networks for image classification inference, as well
  as the `text` module that is used for scene text detection and recognition
  are now available in the `opencv` package.
- opencryptoki
  package updated to version 3.17.0. The `opencryptoki` package has
  been updated to version 3.17.0. This update provides some bug fixes and enhancements over
  the previous version.
- Capability for excluding certain network interfaces and IP addresses
  when creating a rescue image. The `EXCLUDE_IP_ADDRESSES` variable
  enables you to ignore certain IP addresses, and the `EXCLUDE_NETWORK_INTERFACES` variable enables you to ignore certain network interfaces when creating a rescue
  image.

### Compilers and Development Toolsets

Oracle Linux 8.6 introduces the following features, enhancements, and
changes to compilers and development toolsets.

- Rust Toolset updated to version 1.58.1. This version of the Rust
  Toolset includes the following changes:

  - Rust compiler support has been added for the 2021
    edition of the language, featuring disjoint capture in
    closure, `IntoIterator` for arrays, a
    new Cargo feature resolver, as well as other changes.
  - Cargo support for new custom profiles has been added.
  - Cargo now deduplicates compiler errors.
  - New open range patterns have been added.
  - Captured identifiers in format strings have been added.
- LLVM Toolset updated to version 13.0.1. The LLVM Toolset has been
  updated to version 13.0.1. The following notable changes were made in this version of the
  tool:

  - Clang support added for guaranteed tail calls with
    statement attributes in C++ and
    `attributemusttail` in C.
  - Clang support added for the
    `-Wreserved-identifier` warning, which
    warns developers when using reserved identifiers in
    their code.
  - The Clang `-Wshadow` flag now checks
    for shadowed structured bindings.
  - The Clang `-Wextra` now implies
    `Wnull-pointer-subtraction`.
- Location change for libffi's self-modifying code. In this release,
  libffiâs self-modifying code takes advantage of a feature in the Linux kernel for creating
  a suitable file that is independent of any other file system. As a result of this change,
  libffiâs self-modifying code no longer depends on making part of the file system insecure.
- Command for capturing glibc optimization data added. You can use
  the new `ld.so --list-diagnostics` command to capture data that
  influences `glibc` optimization decisions, such as IFUNC selection and
  `glibc-hwcaps` configuration, in a single machine-readable file.
- GCC Toolset pudated to version 11.2. The GCC Toolsset has been
  updated to version 11.2. See [GCC Toolset 11.2](ol8-NewFeaturesandChanges.html#ol-features-gcc) for
  more information about these changes.
- UTF-8 en\_US@ampm locale with 12-hour clock added. In this release,
  you can use the new UTF-8 `en_US@ampm` locale with a 12-hour clock. You can
  also combine this new locale with other locales by specifying the `LC_TIME`
  environment variable.
- GDB disassembler includes support for new arch14 instructions. In
  this release, GDB is able to disassemble the new arch14 instructions.
- PCP updated to version 5.3.5. The Performance Co-Pilot (PCP) package
  (`pcp`) has been updated to version 5.3.5. Several notable improvements
  are included in this version of PCP, including the following:

  - New `pmieconf(1)` rules for CPU and
    disk saturation.
  - Improved stability and scalability for the
    `pmproxy(1)` service.
  - Improved service latency and robustness for the
    `pmlogger(1)` service.
  - Performance metrics related to electrical power added.
  - New features added to the `pcp-htop(1)`
    utility.
  - Nvidia GPU metrics updated.
  - Linux kernel KVM and networking metrics added.
  - New MongoDB metrics agent added.
  - New sockets metrics agent and
    `pcp-ss(1)` utility added.
  - The `pmcd(1`) and
    `pmproxy(1`) Avahi service advertising
    is disabled by default.
- pcp-container package updated to version 5.3.5 The
  `pcp-container` package has been updated to version 5.3.5.
- grafana package updated to version 7.5.11. The
  `grafana` package has been updated to version 7.5.11. Notable changes
  include the additional of a new `prepare time series` transformation for
  backward compatibility of panels that do not support the new data frame format. Also,
  CVE-2021-43813 is resolved in this version of Grafana.
- grafana-pcp package updated to version 3.2.0. The
  `grafana-pcp` package has been updated to version 3.2.0. Notable
  improvements include the following:

  - New MS SQL server dashboard for PCP Redis added.
  - Visibility of empty histogram buckets in the PCP Vector
    eBPF/BCC Overview dashboard added.
  - A bug fix for the `metric()` function
    of PCP Redis, where the function did not return all
    metric names.
- js-d3-flame-graph updated to version 4.0.7. The
  `js-d3-flame-graph` package has been updated to version 4.0.7. Notable
  changes include the addition of a new blue and green color scheme and added functionality
  for displaying flame graph context.

### GCC Toolset 11.2

Oracle Linux 8.6 provides the GCC Toolset 11.2, which is an Application
Stream that is distributed in the form of a Software Collection
in the `AppStream` repository. The GCC Toolset
is similar to the Oracle Linux Developer Toolset. See
[Compilers and Development Toolsets](ol8-NewFeaturesandChanges.html#ol8-features-developer) for
additional information about changes to compilers and developer
toolsets in this release.

GCC Toolset 11.2 is available as an Application Stream within
the `AppStream` repository, in the form of a
Software Collection.

To install this toolset, use the following command:

```
sudo dnf install gcc-toolset-11
```

If you previously installed this toolset, use the following
command to upgrade to the latest version:

```
sudo dnf upgrade gcc-toolset-11
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

### Availability of the container-tools:4.0 stable stream in Oracle Linux 8.6

Oracle Linux 8.6 includes the `container-tools:4.0`
stable stream.

### Database

This release of Oracle Linux 8 ships with version 8.0 of the MySQL database software.

### Dynamic Programming Languages, Web, and Database Servers

Oracle Linux 8.6 includes several feature changes and improvements for
dynamic programming languages and web and database servers. Note
that that this release also introduces several new and improved
module streams:

- php:8.0 module stream added. The `php:8.0` module
  stream has been added in Oracle Linux 8.6. `php:8.0` provides several bug
  fixes and enhancements over the 7.4 version, including the following notable features:

  - New named arguments are order-independent and
    self-documented, and enable you to specify only required
    parameters.
  - New attributes enable you to use structured metadata
    with PHPâs native syntax.
  - New union types enable you to use native union type
    declarations that are validated at runtime instead of
    PHPDoc annotations for a combination of types.
  - Internal functions now more consistently raise an Error
    exception instead of warnings if parameter validation
    fails.
  - The Just-In-Time compilation has improved the
    performance.
  - The `Xdebug` debugging and productivity
    extension for PHP have been updated to version 3. This
    version introduces major functionality and configuration
    changes over `Xdebug` version 2.

  To install the `php:8.0` module stream:

  ```
  sudo dnf module install php:8.0
  ```

  If you previously installed `php:7.4`, you
  can switch to the latest version by running the following
  commands:

  ```
  sudo dnf module reset php
  sudo dnf module enable php:8.0
  sudo dnf distro-sync
  ```
- Perl updated to version 5.32. Oracle Linux 8.6 provides Perl version
  5.32. This version of Perl includes a number of bug fixes and enhancements over Perl
  version 5.30, which was distributed in Oracle Linux 8.3. Notable changes include the
  following:

  - Added support for unicode version 13.0 in Perl.
  - Enhancement to the `qr` qoute-like
    operator.
  - `POSIX::mblen()`,
    `mbtowc`, and `wctomb`
    functions work on shift state locales and are
    thread-safe on C99 and higher compilers when executed on
    a platform that includes locale thread-safety. Also, the
    length parameters are now optional.
  - New experimental `isa` infix operator
    for testing whether a given object is an instance of a
    given class or a class that is derived from it.
  - Alpha assertions and scripts are no longer experimental.
  - Feature checks are faster.

    Perl capability for dumping compiled patterns before
    optimization.

  If you previously installed `perl` version
  5.30, you can switch to the latest version by running the
  following commands:

  ```
  sudo dnf module reset perl
  sudo dnf module enable perl:5.32
  sudo dnf distro-sync
  ```

### File Systems and Storage

Oracle Linux 8.6 provides the following file systems and storage
features, enhancements, and changes:

- Btrfs removed
  from RHCK. The Btrfs file system is removed from RHCK in Oracle Linux 8. As
  such, you cannot create or mount Btrfs file systems when using this kernel. Also,
  note that any Btrfs user space packages that are provided are not supported with
  RHCK.

  Note:

  Support for the Btrfs file system is enabled in UEK R7
  and UEK R6. Starting with Oracle Linux 8.3, you have the option to
  create a Btrfs root file system during an installation, as
  well as select Btrfs as the file system type when
  formatting devices. See [Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/) for more
  information about this feature.

  For more information about managing a Btrfs root file
  system, see [Oracle Linux 8: Managing Local File Systems](https://docs.oracle.com/en/operating-systems/oracle-linux/8/fsadmin/).

  For changes that have been made to Btrfs in UEK R6, see
  [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 6 Update 3 (5.4.17-2136)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.3/).

  For changes to Btrfs in UEK R7, see
  [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 7 (5.15.0-0.30)](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/).
- OCFS2
  removed from RHCK. The Oracle Cluster File System version 2 (OCFS2) file
  system is removed from RHCK in Oracle Linux 8. As such, you cannot create or mount
  OCFS2 file systems when using this kernel. Also, any OCFS2 user space packages that
  are provided are not supported with RHCK.

  Note:

  OCFS2 is fully supported with UEK R6 and UEK R7 in
  Oracle Linux 8.6.
- Samba utilities options renamed or removed in version 4.15.
  In version 4.15 of Samba, some utilities have been improved to ensure a consistent
  command-line interface. These changes include several renamed and removed options. To
  avoid any issues after an update to version 4.15 of Samba, you should review any
  scripts that use Samba utilities, and update them accordingly.

  The following is a summary of the Samba changes that are
  introduced in this release:

  - Samba command-line utilities previously silently ignored
    unknown options, whereas now, these utilities
    consistently reject unknown options.
  - Many command-line options have a corresponding
    `smb.conf` variable for controlling the
    default value. To identify whether a command-line option
    has an `smb.conf` variable name, see
    the associated manual pages for the specified utility.
  - Samba utilities now log to standard error
    (`stderr`) by default. Use the
    `--debug-stdout` option to change this
    behavior.
  - The
    `--client-protection=off|sign|encrypt`
    option has been added to the common parser.
  - The following options have been renamed in all
    utilities:

    - `--kerberos` renamed
      `--use-kerberos=required|desired|off`
    - `--krb5-ccache` renamed
      `--use-krb5-ccache=`
      CCACHE
    - `--scope` renamed
      `--netbios-scope=`
      SCOPE
    - `--use-ccache` renamed
      `--use-windbind-ccache`
  - The following options have been removed:

    - `-e` and
      `--encrypt`
    - `-C` removed from
      `-use-winbind-ccache`
    - `-i` removed from
      `-netbios-scope`
    - `-S` and
      `--signing`
  - The following options have been removed (or renamed)
    from the utilities that are listed:

    - `ndrdump`: `-l` no
      longer available for `--load-dso`
    - `net`: `-l` no
      longer available for `--long`
    - `sharesec`: `-V`
      no longer available for
      `--viewsddl`
    - `smbcquotas`:
      `--user` renamed
      `--quota-user`
    - `nmbd`:
      `--log-stdout` renamed
      `--debug-stdout`
    - `smbd`:
      `--log-stdout` renamed
      `--debug-stdout`
    - `winbindd`:
      `--log-stdout` renamed
      `--debug-stdout`

### High Availability and Clusters

The following high availability and clustering features are
included in Oracle Linux 8.6:

- pcmk\_delay\_base parameter accepts different values for different
  modes. You can now specify different values for different nodes when configuring a
  fence device by using the `pcmk_delay_base parameter`. This improvement
  enables a single fence device to be used in a two-node cluster, with a different delay for
  each node, which can prevent a situation where each node attempts to fence the other node
  at the same time.
- Capability added for spcifying automatic removal of location constraint
  following resource move. A new `--autodelete` option has been added
  to the `pcs resource move` command. This option was previously only
  available as a Technology Preview, but it is now fully supported. When you specify this
  option, the location constraint that the command creates is automatically removed after
  the resource has been moved. When you use the `pcs resource move`
  command, it adds a constraint to the resource to prevent it from running on the node on
  which it is currently running.
- Detailed Pacemaker status display for internal errors available. If
  Pacemaker can not execute a resource or fence agent for some reason, such as when the
  agent is not installed or if there has been an internal timeout, the Pacemaker status
  displays now display a detailed exit reason for the internal error.
- Support for special characters inside pcmk\_host\_map values added.
  Support has been added to the `pcmk_host_map` property for special
  characters inside `pcmk_host_map` values by specifying a backslash
  (`\`) in front of the value. For example, to include a space in the host
  alias, you would specify `pcmk_host_map="node3:plug\ 1"`.
- pcs support for OCF Resource Agent API 1.1 standard. The
  `pcs` command now includes support for OCF 1.1 resource and STONITH
  agents. Note that an OCF 1.1 agentâs metadata must comply with the OCF 1.1 schema. If an
  OCF 1.1 agentâs metadata does not comply with the OCF 1.1 schema, the
  `pcs` considers the agent invalid and does not create or update a
  resource of the agent unless you also specify the `--force` option. The
  `pcsd` web interface and `pcs` commands for
  listing agents omit OCF 1.1 agents with invalid metadata from the listing.

  An OCF agent that declares that it implements any OCF
  version other than 1.1, or does not declare a version at
  all, is validated against the OCF 1.0 schema. Validation
  issues are reported as warnings, but is not necessary to
  specify the `--force` option for those
  agents when creating or updating a resource of the agent.

### Infrastructure Services

Oracle Linux 8.6 introduces several version updates to infrastructure and
command-line tools, including the following features:

- New bind9.16 pacakge version 9.16.23 introduced. The
  `bind` component version 9.16.23 is introduced as alternative to version
  9.11.36. This version includes several new features, as well as some removed features,
  including the following:

  - New Key and Signing Policy feature in DNSSEC.
  - New QNAME minimisation to improve privacy.
  - New `validate-except` feature added to
    Permanent.
  - Negative Trust Anchors to temporarily disable DNSSEC
    validation.
  - Response policy zones (RPZ) have been re-factored.
  - New naming conventions for zone types. The
    primary and
    secondary zone types are now used
    as synonyms for master and
    slave
  - New supplementary YAML output mode for the
    `dig`, `mdig`, and
    `delv` commands.
  - Functionality for `filter-aaaa` has
    been moved into separate `filter-a` and
    `filter-aaaa` plugins.
  - New zone type mirror support, per
    [RFC
    8806](https://www.rfc-editor.org/rfc/rfc8806.html).

  The following features have been removed:

  - The `dnssec-enabled` option is removed;
    DNSSEC is now enabled by default; the
    `dnssec-enabled` keywords are no longer
    accepted.
  - The `lwresd` lightweight resolver
    daemon and the `liblwres` light
    resolver library have both been removed.
- Bind component updated to version 9.11.36. The `bind`
  component has been updated to version 9.11.36. This version provides some bug fixes and
  several enhancements, including the following:

  - The `lame-ttl` option has been improved
    for better security.
  - A multiple threads bug affecting RBTDB instances has
    been fixed and no longer results in assertion failure in
    `free_rbtdb()`.
  - ZONEMD RR type implementation updated to match RFC 8976.
  - Maximum supported number of NSEC3 iterations is reduced
    to 150; records with additional iterations are treated
    as insecure.
  - An invalid direction field in an LOC record has been
    fixed so that it no longer results in a failure.
- nginx-mod-devel package added to nginx:1.20 module stream. The
  `nginx-mod-devel` package has been added to the
  `nginx:1.20` module stream in this release. This package includes all of
  the necessary files for building external dynamic modules for `nginx`,
  which includes RPM macros and the `nginx` source code.

### Networking

Oracle Linux 8.6 introduces the following networking features,
enhancements, and changes:

- CleanUpModulesOnExit firewalld global configuration option
  available. This enhancement enables you to set the
  `CleanUpModulesOnExit` option to `no` to stop
  `firewalld` from unloading these kernel modules. Whereas,
  previously, when restarting or shutting down `firewalld`, it
  recursively unloaded kernel modules. As a result, other packages that were attempting to
  use these modules or dependent modules failed.
- hostapd package added. The `hostapd` package is
  available for installation in Oracle Linux 8.6. However note that support for
  `hostapd` is limited to setting up an Oracle Linux 8 host as an 802.1X
  authenticator on an Ethernet network only. Other scenarios, such as wireless access
  points or authenticators in wireless networks, are currently not supported.
- NetworkManager updated to version 1.36.0.`NetworkManager` has been upgraded to version 1.36.0. This version of
  `NetworkManager` includes several enhancements and bug fixes over the
  previous version, most notably the following:

  - Reworking of how layer 3 configurations are handled.
    This enhancement improves the stability, performance,
    and memory usage of `NetworkManager`.
  - The additional of the `blackhole`,
    `unreachable`,
    `prohibit` route types.
  - `NetworkManager` ignores routes
    managed by routing services.
  - Improvements to the Wi-Fi Protected Access version 3
    (WPA3) network security by enabling the hash-to-element
    (H2E) method when generating simultaneous authentication
    of equals (SAE) password elements.
  - The service now correctly handles replies from DHCP
    servers that send duplicate address or mask options.
  - The ability to turn off MAC aging on bridges has been
    added.
  - `NetworkManager` no longer listens for
    `netlink` events for the
    `qdiscs` and `filters`
    traffic control objects.
  - Network bonds support for setting a queue ID for bond
    ports.
- NetworkManager includes support for setting the number of receiving queueus (rx\_queue)
  on OVS-DPDK interfaces. You can use `NetworkManager` to configure the
  `n_rxq` setting of Open vSwitch (OVS) Data Plane Development Kit (DPDK)
  interfaces. Use the `ovs-dpdk.n-rxq` attribute in NetworkManager to set the
  number of receiving queues on OVS-DPDK interfaces.
- nftables framework includes support for nft set elements with attached counters.
  You can now configure the `nftables` framework by using the
  `nft` tool. The kernel enables this tool to count the network
  packets from a given source address with the statement `add @myset {ip saddr
  counter}`. In this release, you can count packets that match a specific criteria
  with a dynamic set and elements with attached counters.
- Restoring large nftables sets requires less memory. The
  `nftables` framework has been enhanced to require significantly less
  memory when restoring large sets. The algorithm that prepares the `netlink`
  message is also improved.

### Security

Oracle Linux 8.6 introduces the following security features,
enhancements, and changes:

- Audit updated to version 3.0.7. The `audit` packages
  have been updated in this release. The updated version of Audit includes several changes
  and improvements, including the following:

  - Added `sudoers` to Audit base rules.
    The `/etc/sudoers` and
    `etc/sudoers.d/` directories have been
    added to Audit base rules, for example, the Payment Card
    Industry Data Security Standard (PCI DSS) and the
    Operating Systems Protection Profile (OSPP). This
    improvement increases security by monitoring
    configuration changes in privileged areas such as
    `sudoers`.
  - Added the `--eoe-timeout` option to the
    `ausearch` command and its analogous
    `eoe_timeout` option to
    `auditd.conf` file, which impacts how
    `ausearch` parses co-located events.
    You can use these options to specify the end of the
    event timeout to avoid problems with parsing co-located
    events. The default value for the end of the event
    timeout is set to two seconds.
- clevis-systemd no longer depends on nc. In this
  release, the `clevis-systemd` package no longer depends on the
  `nc` package. This dependency did not work correctly when used with Extra
  Packages for Enterprise Linux (EPEL).
- fapolicyd framework
  packages updated to version 1.1. Several improvements have been made in this update
  release, including the ability to use the new `rules.d/` and
  `trust.d/` directories, the `fagenrules` script. In
  additional, some new options have been added to the `fapolicyd-cli`
  command.
- libcap packages
  updated to version 2.48. The `libcap` packages have been updated to
  version 2.48. This update provides some bug fixes and enhancements over the previous
  version.
- Libreswan updated to
  version 4.5. Libreswan has been updated to version 4.5. This update provides some
  bug fixes and enhancements over the previous version, including added support for Internet
  Key Exchange version 2 (IKEv2) for Labeled IPsec and childless initiation of IKE Security
  Association (SA).
- libseccomp packages updated to version 2.5.2. The
  `libseccomp` packages have updated to version 2.5.2. This version
  provides several bug fixes and enhancements over the previous version.
- Libssh updated to version 0.9.6. The `libssh` package
  has been updated to version 0.9.6. In this version of Libssh, there are some bug fixes,
  and other enhancements, including the following:

  Support added for multiple identity files, which are now
  processed from the bottom to the top, as listed in the
  `~/.ssh/config` file.

  Parsing of sub-second times in SFTP is fixed.

  A regression for the
  `ssh_channel_poll_timeout()` function,
  where it returned `SSH_AGAIN` unexpectedly,
  is fixed.

  A possible heap-buffer overflow after a key re-exchange is
  fixed
- Support for diffie-hellman-graoup14-sha256 provided in crypto
  policies. In Oracle Linux 8.6, you can use the
  `diffie-hellman-group14-sha256` key exchange (KEX) algorithm for the
  `libssh` library in the Oracle Linux system-wide cryptographic policies.
  This release additionally provides parity with OpenSSH, which also supports the KEX
  algorithm; `libssh` has `diffie-hellman-group14-sha256`
  enabled by defaul, but you can disable it by using a custom crypto policy.
- OpenSSH servers
  include support for drop-in configuration files. Support for the the
  `include` directive has been added to the
  `sshd_config` file, which means you can now include configuration files
  in another directory. This change makes it easier to apply system-specific configurations
  on OpenSSH servers by using automation tools, including the Ansible Engine. The new
  behavior is also more consistent with the capabilities of the `ssh_config`
  file. Also, drop-in configuration files provide for easier organization of different
  configuration files for different uses, for example, for filter incoming connections.
- pcsc-lite packages
  have been updated to version 1.9.5. The `pcsc-lite` packages have
  been updated to version 1.9.5. This version includes many enhancements and bug fixes over
  the previous version. Notable changes include fixes for memory leaks and concurrency
  problems, as well as the following:

  - The `pcscd` daemon no longer
    automatically exits after inactivity when started
    manually.
  - The `pcsc-spy` utility provides support
    for Python 3 and a new `--thread`
    option.
  - The `SCardEndTransaction()` function
    has been improved for better performance.
  - The `poll()` function replaces the
    `select()` function. This function
    allows for file descriptor numbers that are higher than
    `FD_SETSIZE`.
- New --checksum option
  for verifying installed versions of SELinux policy modules. You can use the new
  `--checksum` option of the `semodue` command to
  verify the versions of installed SELinux policy modules. Previously , there was no simple
  way to verify that the installed module is the same version as the module which was
  supposed to be installed.

  You can use the new `semodule -l
  --checksum` command to receive a SHA256 hash for
  the specified module, enabling you to compare it with the
  checksum of the original file, which is faster than
  reinstalling modules.
- SCAP rules include warning message to configure Audit log buffer for
  large systems. SCAP rules now include a warning message to configure Audit log
  buffer for large systems. The
  `xccdf_org.ssgproject.content_rule_audit_basic_configuration` SCAP rule
  displays a performance warning that suggests that users of large systems (where the Audit
  log buffer that is configured by this rule) might be too small and can override the custom
  value. The new warning also describes the process for configuring a larger Audit log
  buffer. This improvement enables users of large systems to remain compliant and have their
  Audit log buffer set correctly.
- SCAP Security Guide
  updated to version 0.1.60. The SCAP Security Guide (SSG) packages have updated to
  version 0.1.60. Notable changes include the following:

  - The
    `xccdf_org.ssgproject.content_enable_fips_mode`
    rule checks only whether FIPS mode has been enabled
    properly. It does not guarantee, however, that system
    components have undergone FIPS certification.
- SSG capability for
  scans and remediations that detect home directories and interactive users. This
  enhancement adds OVAL checks and remediations that detect local interactive users in a
  system and their respective home directories. The SCAP Security Guide (SSG) suite can now
  safely check and remediate all related benchmark requirements, where previously, there was
  no robust solution for covering this gap by using the OVAL language.
- OpenSCAP packages
  updated to version 1.3.6. The OpenSCAP packages have been updated to version 1.3.6.
  This version of OpenSCAP provides numerous enhancements and bug fixes, most notably the
  following:

  - Capability for providing local copies of remote SCAP
    source data stream components by using the
    `--local-files` option has been added.
  - OpenSCAP accepts multiple `--rule`
    arguments on the command line for selecting multiple
    rules.
  - OpenSCAP allows the skipping of evaluation for some
    rules by using the `--skip-rule`
    option.
  - Restricting memory that is consumed by OpenSCAP probes
    can be accomplished by using the
    `OSCAP_PROBE_MEMORY_USAGE_RATIO`
    environment variable.
  - OpenSCAP adds support for the OSBuild Blueprint as a
    remediation type.
  - OpenSCAP includes the ability to consume local files
    instead of remote SCAP source data stream components in
    this release. You can now download and copy the remote
    SCAP source data stream components to the target system
    before performing the OpenSCAP scan and then provide
    them to OpenSCAP by specifying the
    `--local-files` option with the
    `oscap` command. In previous releases,
    you could not perform a complete evaluation of SCAP
    source data streams that contained remote components on
    systems without Internet access, which meant that
    OpenSCAP could not evaluate some of the rules in the
    data streams because the remote components had to be
    downloaded from the Internet.
- SSG support for
  /etc/security/faillock.conf file added. Support for the
  `/etc/security/faillock.conf` file has been added to SSG. This
  enhancement enables SSG to assess and remediate the
  `/etc/security/faillock.conf` file for the definition of
  `pam_faillock` settings. In addition, the
  `authselect` tool can be used to enable the
  `pam_faillock` module to ensure the integrity of `pam`
  files. This change causes the assessment remediation of the `pam_faillock`
  module to be more aligned with the latest versions and best practices.

### New --estimate-only Option for sosreport update Command

This `sos report update` command includes a new
`--estimate-only` option that you can use to
approximate the disk space required for collecting an
`sos report` from an Oracle Linux 8 server. Running the
`sos report --estimate-only` command executes a
dry run of `sos report` and mimics all plugins
consecutively, as well as estimates disk size. Note that because
the final disk space estimation is approximate, it is
recommended that you double the estimated value.

### Windows Server 2022 Guest Support

This release includes support for using Windows Server 2022 as a
guest operating system on KVM virtual machines (VMs).

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

#### SGX Available

Software Guard Extensions (SGX) is an Intel technology for
protecting software code and data from disclosure and
modification. The Linux kernel partially supports SGX v1 and
v1.5; version 1 enables platforms by using the Flexible Launch
Control mechanism to use the SGX technology.

#### DAX File System Available

In this
release, the DAX file system is available as a Technology Preview for the ext4 and XFS
file systems. DAX enables an application to directly map persistent memory into its
address space. The system must have some form of persistent memory available to use DAX.
Persistent memory can be in the form of one or more Non-Volatile Dual In-line Memory
Modules (NVDIMMs). In addition, a file system that supports DAX must be created on the
NVDIMMs; the file system must be mounted with the `dax` mount option.
Then, an `mmap` of a file on the dax-mounted file system results in a
direct mapping of storage into the applicationâs address space.

#### NVMe/TCP available

NVMe over Fabrics
TCP host and the target drivers are included in RHCK as a technology preview in this
release.

Note:

Support for NVMe/TCP is already available in Unbreakable Enterprise Kernel Release
6.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.6/ol8-KnownIssues.html -->

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

#### Oracle Linux 8.5 systems with libguestfs-benchmarking and lld-test packages installed cannot be upgraded to Oracle Linux 8.6

The `libguestfs-benchmarking` and
`lld-test` packages are not included in
Oracle Linux 8.6. Consequently, if your Oracle Linux 8.5 system includes these
packages, upgrading the system to Oracle Linux 8.6 fails.

To work around this issue, remove these packages from the
system prior to upgrading to Oracle Linux 8.6. For example:

```
sudo dnf remove libguestfs-benchmarking lld-test
```

(Bug ID 34122488)

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

The Oracle Linux 8.6 installer displays the following error on aarch64
systems that have a multipath-enabled NVMe controller:

```
Failed to set new efi boot target . This is most likely a kernel or firmware bug.
```

To work around this issue, disable native multipath support
for the installation at boot time by adding the
`nvme_core.multipath=N` command-line argument
on the target system.

(Bug IDs 34215333, 31758304)

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.6/ol8-PackageChangesfromtheUpstreamRelease.html -->

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
- `kernel-uek-debug`
- `kernel-uek-debug-devel`
- `kernel-uek-devel`
- `kernel-uek-doc`
- `linux-firmware-core`
- `NetworkManager-config-connectivity-oracle`
- `ocfs2-tools`
- `oracle-backgrounds`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`
- `oracle-logos-httpd`
- `oracle-logos-ipa`

#### Added Binary Packages for AppStream by Oracle

The following binary packages have been added to AppStream by Oracle:

- `dtrace-devel`
- `dtrace-testsuite`
- `libblockdev-btrfs`
- `oracle-database-preinstall-21c`
- `python3-dnf-plugin-ulninfo`

#### Added Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages have been added to CodeReady Linux Builder by Oracle:

- `dotnet5.0-build-reference-packages`
- `dotnet-sdk-3.1-source-built-artifacts`
- `dotnet-sdk-5.0-source-built-artifacts`
- `ibus-typing-booster-tests`
- `java-11-openjdk-demo-fastdebug`
- `java-11-openjdk-demo-slowdebug`
- `java-11-openjdk-devel-fastdebug`
- `java-11-openjdk-devel-slowdebug`
- `java-11-openjdk-fastdebug`
- `java-11-openjdk-headless-fastdebug`
- `java-11-openjdk-headless-slowdebug`
- `java-11-openjdk-jmods-fastdebug`
- `java-11-openjdk-jmods-slowdebug`
- `java-11-openjdk-slowdebug`
- `java-11-openjdk-src-fastdebug`
- `java-11-openjdk-src-slowdebug`
- `java-11-openjdk-static-libs-fastdebug`
- `java-11-openjdk-static-libs-slowdebug`
- `java-17-openjdk-demo-fastdebug`
- `java-17-openjdk-devel-fastdebug`
- `java-17-openjdk-fastdebug`
- `java-17-openjdk-headless-fastdebug`
- `java-17-openjdk-jmods-fastdebug`
- `java-17-openjdk-src-fastdebug`
- `java-17-openjdk-static-libs-fastdebug`
- `java-1.8.0-openjdk-accessibility-fastdebug`
- `java-1.8.0-openjdk-accessibility-slowdebug`
- `java-1.8.0-openjdk-demo-fastdebug`
- `java-1.8.0-openjdk-demo-slowdebug`
- `java-1.8.0-openjdk-devel-fastdebug`
- `java-1.8.0-openjdk-devel-slowdebug`
- `java-1.8.0-openjdk-fastdebug`
- `java-1.8.0-openjdk-headless-fastdebug`
- `java-1.8.0-openjdk-headless-slowdebug`
- `java-1.8.0-openjdk-slowdebug`
- `java-1.8.0-openjdk-src-fastdebug`
- `java-1.8.0-openjdk-src-slowdebug`
- `leptonica`
- `libcomps-devel`
- `libdnf-devel`
- `libfdt`
- `libmpc-devel`
- `libpciaccess-devel`
- `librepo-devel`
- `librhsm-devel`
- `libsolv-devel`
- `libsolv-tools`
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
- `iwlax2xx-firmware`
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
- `libxslt`
- `libzstd`
- `libzstd-devel`
- `linux-firmware`
- `linux-firmware-core`
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
- `python3-sss`
- `python3-sssdconfig`
- `python3-sss-murmur`
- `python3-test`
- `redhat-indexhtml`
- `redhat-release`
- `sanlock-lib`
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
- `dotnet-sdk-3.1-source-built-artifacts`
- `dotnet-sdk-5.0-source-built-artifacts`
- `fwupd-devel`
- `gcc-plugin-devel`
- `gcc-toolset-10-gcc-plugin-devel`
- `glibc-benchtests`
- `glibc-nss-devel`
- `glibc-static`
- `guile-devel`
- `iscsi-initiator-utils-devel`
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
- `libsss_nss_idmap-devel`
- `libstdc++-static`
- `mozjs52-devel`
- `mozjs60-devel`
- `NetworkManager-libnm-devel`
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
- `aspnetcore-targeting-pack-3.0`
- `aspnetcore-targeting-pack-3.1`
- `aspnetcore-targeting-pack-5.0`
- `aspnetcore-targeting-pack-6.0`
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
- `delve`
- `dnf-plugin-spacewalk`
- `dotnet`
- `dotnet-apphost-pack-3.0`
- `dotnet-apphost-pack-3.1`
- `dotnet-apphost-pack-5.0`
- `dotnet-apphost-pack-6.0`
- `dotnet-host`
- `dotnet-hostfxr-3.0`
- `dotnet-hostfxr-3.1`
- `dotnet-hostfxr-5.0`
- `dotnet-hostfxr-6.0`
- `dotnet-runtime-3.0`
- `dotnet-runtime-3.1`
- `dotnet-runtime-5.0`
- `dotnet-runtime-6.0`
- `dotnet-sdk-3.0`
- `dotnet-sdk-3.1`
- `dotnet-sdk-5.0`
- `dotnet-sdk-6.0`
- `dotnet-targeting-pack-3.0`
- `dotnet-targeting-pack-3.1`
- `dotnet-targeting-pack-5.0`
- `dotnet-targeting-pack-6.0`
- `dotnet-templates-3.0`
- `dotnet-templates-3.1`
- `dotnet-templates-5.0`
- `dotnet-templates-6.0`
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
- `gdb`
- `gdb-doc`
- `gdb-gdbserver`
- `gdb-headless`
- `git-clang-format`
- `glibc-gconv-extra`
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
- `Judy`
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
- `nodejs`
- `nodejs-devel`
- `nodejs-docs`
- `nodejs-full-i18n`
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
- `open-vm-tools-sdmp`
- `osbuild-composer`
- `osbuild-composer-core`
- `osbuild-composer-dnf-json`
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
- `pcp`
- `pcp-conf`
- `pcp-devel`
- `pcp-doc`
- `pcp-export-pcp2elasticsearch`
- `pcp-export-pcp2graphite`
- `pcp-export-pcp2influxdb`
- `pcp-export-pcp2json`
- `pcp-export-pcp2spark`
- `pcp-export-pcp2xml`
- `pcp-export-pcp2zabbix`
- `pcp-export-zabbix-agent`
- `pcp-gui`
- `pcp-import-collectl2pcp`
- `pcp-import-ganglia2pcp`
- `pcp-import-iostat2pcp`
- `pcp-import-mrtg2pcp`
- `pcp-import-sar2pcp`
- `pcp-libs`
- `pcp-libs-devel`
- `pcp-pmda-activemq`
- `pcp-pmda-apache`
- `pcp-pmda-bash`
- `pcp-pmda-bcc`
- `pcp-pmda-bind2`
- `pcp-pmda-bonding`
- `pcp-pmda-bpftrace`
- `pcp-pmda-cifs`
- `pcp-pmda-cisco`
- `pcp-pmda-dbping`
- `pcp-pmda-denki`
- `pcp-pmda-dm`
- `pcp-pmda-docker`
- `pcp-pmda-ds389`
- `pcp-pmda-ds389log`
- `pcp-pmda-elasticsearch`
- `pcp-pmda-gfs2`
- `pcp-pmda-gluster`
- `pcp-pmda-gpfs`
- `pcp-pmda-gpsd`
- `pcp-pmda-hacluster`
- `pcp-pmda-haproxy`
- `pcp-pmda-infiniband`
- `pcp-pmda-json`
- `pcp-pmda-libvirt`
- `pcp-pmda-lio`
- `pcp-pmda-lmsensors`
- `pcp-pmda-logger`
- `pcp-pmda-lustre`
- `pcp-pmda-lustrecomm`
- `pcp-pmda-mailq`
- `pcp-pmda-memcache`
- `pcp-pmda-mic`
- `pcp-pmda-mongodb`
- `pcp-pmda-mounts`
- `pcp-pmda-mssql`
- `pcp-pmda-mysql`
- `pcp-pmda-named`
- `pcp-pmda-netcheck`
- `pcp-pmda-netfilter`
- `pcp-pmda-news`
- `pcp-pmda-nfsclient`
- `pcp-pmda-nginx`
- `pcp-pmda-nvidia-gpu`
- `pcp-pmda-openmetrics`
- `pcp-pmda-openvswitch`
- `pcp-pmda-oracle`
- `pcp-pmda-pdns`
- `pcp-pmda-perfevent`
- `pcp-pmda-podman`
- `pcp-pmda-postfix`
- `pcp-pmda-postgresql`
- `pcp-pmda-rabbitmq`
- `pcp-pmda-redis`
- `pcp-pmda-roomtemp`
- `pcp-pmda-rsyslog`
- `pcp-pmda-samba`
- `pcp-pmda-sendmail`
- `pcp-pmda-shping`
- `pcp-pmda-slurm`
- `pcp-pmda-smart`
- `pcp-pmda-snmp`
- `pcp-pmda-sockets`
- `pcp-pmda-statsd`
- `pcp-pmda-summary`
- `pcp-pmda-systemd`
- `pcp-pmda-trace`
- `pcp-pmda-unbound`
- `pcp-pmda-weblog`
- `pcp-pmda-zimbra`
- `pcp-pmda-zswap`
- `pcp-selinux`
- `pcp-system-tools`
- `pcp-testsuite`
- `pcp-zeroconf`
- `perl-PCP-LogImport`
- `perl-PCP-LogSummary`
- `perl-PCP-MMV`
- `perl-PCP-PMDA`
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
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-ipatests`
- `python3-kickstart`
- `python3-libguestfs`
- `python3-libreport`
- `python3-pcp`
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
- `ruby`
- `ruby-devel`
- `ruby-doc`
- `rubygem-bigdecimal`
- `rubygem-did_you_mean`
- `rubygem-io-console`
- `rubygem-json`
- `rubygem-minitest`
- `rubygem-net-telnet`
- `rubygem-openssl`
- `rubygem-power_assert`
- `rubygem-psych`
- `rubygem-rake`
- `rubygem-rdoc`
- `rubygems`
- `rubygems-devel`
- `rubygem-test-unit`
- `rubygem-xmlrpc`
- `ruby-irb`
- `ruby-libguestfs`
- `ruby-libs`
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
- `coreos-installer`
- `coreos-installer-bootinfra`
- `coreos-installer-dracut`
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
- `libxslt`
- `linux-firmware`
- `mcelog`
- `microcode_ctl`
- `mokutil`
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
- `redhat-indexhtml`
- `redhat-release`
- `sanlock`
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
- `containers-common`
- `crash`
- `cups-filters`
- `dbus`
- `delve`
- `dnf-plugins-core`
- `dnf-plugin-spacewalk`
- `dotnet3.0`
- `dotnet3.1`
- `dotnet5.0`
- `dotnet6.0`
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
- `mariadb`
- `mecab-ipadic`
- `mpich`
- `NetworkManager`
- `nginx`
- `nodejs`
- `openchange`
- `openscap`
- `open-vm-tools`
- `osbuild-composer`
- `osinfo-db`
- `pacemaker`
- `PackageKit`
- `pcp`
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
- `ruby`
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
- `dotnet3.1`
- `dotnet5.0`
- `fwupd`
- `gcc`
- `gcc-toolset-10-gcc`
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
- `mozjs52`
- `mozjs60`
- `mpich`
- `NetworkManager`
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
- `libica`
- `redhat-logos`
- `subscription-manager`

#### Removed AppStream Source Packages

The following source packages from the AppStream upstream release have been removed:

- `ansible-collection-microsoft-sql`
- `ansible-collection-redhat-rhel_mgmt`
- `coreos-installer`
- `insights-client`
- `libica`
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