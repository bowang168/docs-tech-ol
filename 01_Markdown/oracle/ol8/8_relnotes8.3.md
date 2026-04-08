---
title: "Release Notes for Oracle Linux 8.3"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.3"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol8"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

Release Notes for Oracle Linux 8.3

F33984-09

November 2022

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 8 Release Notes for Oracle Linux 8.3

F33984-09

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2020, 2022, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.3/ol8.3-Preface.html -->

[Oracle Linux 8: Release Notes for Oracle Linux
8.3](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.3/) provides information about the new
features and known issues in the Oracle Linux 8.3 release. This document
may be updated after it is released.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.3/ol8-AboutOracleLinux8.html -->

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

For the x86\_64 platform, Oracle Linux 8.3 ships with the following default kernel packages:

- `kernel-4.18.0-240.el8`: Red Hat Compatible Kernel (RHCK)
- `kernel-uek-5.4.17-2011.7.4.el8uek`: Unbreakable Enterprise Kernel
  Release 6 (UEK R6)

  For new installations, the UEK kernel is automatically enabled and installed. It also
  becomes the default kernel on first boot.

  For the 64-bit Arm (aarch64) platform, Oracle Linux ships only with the UEK kernel.

The Oracle Linux release is tested as a bundle, as shipped on the
installation media image. When installed from the installation
media image, the minimum kernel version that is supported is the
kernel that is included in the image. Downgrading kernel packages
is not supported, unless recommended by Oracle Support.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.3/ol8-NewFeaturesandChanges.html -->

This chapter describes the new features, major enhancements, bug fixes, and other changes
that are included in this release of Oracle Linux 8.

### Installation

Oracle Linux 8.3 introduces the following notable features and
improvements to installing and booting a system, and creating
images.

For information about upgrading an Oracle Linux 7 system to the latest Oracle Linux 8
release, see [Upgrading From Oracle Linux 7 to Oracle Linux 8](ol8-AboutOracleLinux8.html#ol8-upgrades).

#### Graphical Installer Improvements

In Oracle Linux 8.3, the Anaconda graphical installer is updated to
version 33.16.3.1. This version of the installer provides
numerous changes and improvements over the previous version of
the installer. Notable changes include the following:

- Installation Program displays supported NVDIMM device
  sector sizes.
- Host name is configured correctly on an installed system
  having IPv6 static configuration.
- Capability for using non-ASCII characters in the disk
  encryption passphrase.
- The GUI installation program displays appropriate
  recommendation for creating a new file system on
  `/boot`, `/tmp`, and all
  `/var` and `/usr` mount
  points, with the exception of
  `/usr/local` and
  `/var/www`.
- Ability to change the LUKS version of the container in the
  Manual Partitioning screen now available.
- Installation program successfully finishes an installation
  without the `btrfs-progs` package.
- Installation program uses the default LUKS2 version for an
  encrypted container by default.
- Installation program no longer crashes when a kickstart
  file puts physical volumes (PVs) of a Logical volume group
  (VG) on an `ignoreddisk` list.

#### GUI Installation Changes

In Oracle Linux 8.3, the graphical installation program has been
updated to include the `Root password` and
`User creation` settings in the Installation
Summary screen. This improvement enables you to configure a
`root` password, as well as create a user
account prior to starting the installation. In previous
releases, you performed this configuration after beginning the
installation process.

For more information about this change, see
[Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/).

### Red Hat Compatible Kernel

The following notable features, enhancements, and changes apply
to the Red Hat Compatible Kernel (RHCK) that is shipped with
Oracle Linux 8.3 on the x86\_64 platform.

For more information about the Unbreakable Enterprise Kernel Release 6 (UEK R6) release that is
shipped with Oracle Linux 8.3, see the [Unbreakable Enterprise Kernel: Release Notes for
Unbreakable Enterprise Kernel Release 6 (5.4.17-2011)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/).

- lshw command provides additional CPU information

  The List Hardware command (`lshw`) now
  displays more CPU information. The CPU version field now
  includes the family, model and stepping details of the
  system processors in numeric format as version:
  family.model.stepping.
- Extended Berkeley Packet Filter added

  Oracle Linux 8.3 includes support for the Extended Berkeley Packet
  Filter (eBPF) in-kernel virtual machine, as well as the tc
  classifier/action code and BCC tools.
- Libbpf support included

  Support for Libbpf is added in this release. The
  `libbpf` package is critical for
  BPF-related applications like `bpftrace`,
  as well as `bpf/xdp` development.
- Mellanox ConnectX-6 Dx network adapter included

  The PCI IDs of the Mellanox ConnectX-6 Dx network adapter
  have been added to the `mlx5_core`
  driver. Oracle Linux now loads the `mlx5_core`
  driver automatically on hosts that use this adapter. This
  feature was previously available as a technology preview
  only.
- tpm2-tools updated to version 4.1.1

  The `tpm2-tools` package is updated to
  version 4.1.1. This version of TPM (Trusted Platform
  Module) 2 provides several command changes, including
  additions, updates, and removals.
- TSX disabled by default

  To improve OS security, the Intel Transactional
  Synchronization Extensions (TSX) technology is now
  disabled by default in the kernel. Note that this change
  only applies to CPUs that support disabling TSX, for
  example, the 2nd Generation Intel Xeon Scalable Processors
  (formerly known as Cascade Lake, with Intel C620 Series
  Chipsets).

### Built-In Default Value for best DNF Configuration Option Set to True

In this release, the built-in `best` DNF
configuration option value is set to `True` by
default.

This change means that DNF will now run with the
`best` configuration option set to
`False` unless you explicitly set it to
`True` in a configuration file. If you have set
the `best=True` option in your DNF
configuration file (`/etc/dnf/dnf.conf`), this
behavior is unchanged. However, if you do not have this option
set in your DNF configuration file, when you run the
`dnf` command to install a package, if the
package is already installed but an update is available, the
command does not attempt to install the update.

To retain the same behavior in your own configuration files,
ensure that the `best=True` option is included.

### Database

This release of Oracle Linux 8 ships with version 8.0 of the MySQL database software.

### Desktop

Oracle Linux 8.3 includes the TigerVNC desktop feature. In this release,
the `tigervnc` packages are updated to version
1.10.1.

### Dynamic Programming Languages, Web and Database Servers

Oracle Linux 8.3 includes the following feature changes and improvements
for dynamic programming languages, and web and database servers.
Note that this release also introduces several new, as well as
improved, module streams:

- Ruby 2.7.1 module stream added

  The new `ruby:2.7` module stream provides
  a number of performance improvements, bug and security
  fixes, and new features over Ruby 2.6, is introduced in
  this release.
- Nodejs:14 module stream added

  The new `node.js 14.4.0` module stream
  provides a number of new features, bug and security fixes,
  and improvements over Node.js 12, the version that was
  distributed in the previous release.
- git packages updated to version 2.27

  In this release, the `git` packages are
  updated to version 2.27.
- python38:3.8 module stream changes

  This release includes the `python38:3.8`
  module stream.
- php:7.4 module stream added

  The new `PHP 7.4` module stream includes
  a number of bug fixes and enhancements over the previous
  7.3 version. The new Foreign Function Interface (FFI)
  experimental extension, which is available in the
  `php-ffi` package, has also been
  introduced in this release. This extension enables you to
  do the following: call native functions, access native
  variables, and create and access data structures defined
  in C libraries.

  Note that the following extensions have been removed:

  - The `wddx` extension has been removed
    from the `php-xml` package
  - The `recode` extension has been removed
    from the `php-recode` package.
- nginx:1.18 module stream added

  This version of the `nginx` web and proxy
  server provides a number of bug fixes, security fixes, as
  well as new features and enhancements over the previous
  1.16 version 1.16.
- perl:5.30 module stream added

  RHEL 8.3 introduces `Perl 5.30`, which provides
  a number of bug fixes and enhancements over the previously
  released `Perl 5.26`. The new version also
  deprecates or removes certain language features.
- perl-libwww-perl:6.34 module stream added

  The new `perl-libwww-perl:6.34` module
  stream includes the `perl-libwww-perl`
  package, which can be used for all versions of Perl that
  are available in Oracle Linux 8. Note that the non-modular
  `perl-libwww-perl` package (available
  since Oracle Linux 8) is obsoleted by the new default
  `perl-libwww-perl:6.34` module stream, as
  that package could not be used with any Perl streams,
  other than version 5.26.
- perl-IO-Socket-SSL:2.066 module stream added

  The new perl-IO-Socket-SSL:2.066 module stream includes
  the perl-IO-Socket-SSL and perl-Net-SSLeay packages. These
  packages are compatible with all of the Perl streams that
  are available in Oracle Linux 8.
- squid:4 module stream updated to version 4.11

  This version of the `Squid` proxy server
  includes the `squid:4` module stream,
  which has been updated from version 4.4 to version 4.11.
  This version of `Squid` provides a number
  of bug and security fixes and various enhancements,
  including new configuration options.
- httpd:2.4 module stream changes

  Several bug fixes and other notable changes to the Apache
  HTTP Server are made available through the
  `httpd:2.4` module stream.
- New CustomLog directive enables logging to journald in httpd

  You can now transfer logs to `journald`
  from the Apache HTTP Server by using the new
  `CustomLog` directive.

### File Systems and Storage

Oracle Linux 8.3 provides the following file systems and storage
features, enhancements, and changes:

- Btrfs removed from RHCK

  The Btrfs file system is removed from RHCK in Oracle Linux 8. As
  such, you cannot create or mount Btrfs file systems when
  using this kernel. Also, any Btrfs user space packages
  that are provided are not supported with RHCK.

  Note:

  Support for the Btrfs file system is enabled in UEK R6.
  Starting with Oracle Linux 8.3, during an installation, you now
  have the option to create a Btrfs root file system, as
  well as select Btrfs as the file system type when
  formatting devices. See [Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/) for more
  information about this feature.

  For more information about managing the Btrfs root file
  system, see [Oracle Linux 8: Managing Local File Systems](https://docs.oracle.com/en/operating-systems/oracle-linux/8/fsadmin/).

  For more information about the enhancements that have been
  made to Btrfs in UEK R6, see [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 6 (5.4.17-2011)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/).
- OCFS2 removed from RHCK

  The Oracle Cluster File System version 2 (OCFS2) file
  system is removed from RHCK in Oracle Linux 8. As such, you cannot
  create or mount OCFS2 file systems when using this kernel.
  Also, any OCFS2 user space packages that are provided are
  not supported with RHCK.

  Note:

  OCFS2 is fully supported with UEK R6 in Oracle Linux 8.3.
- NVMe/TCP available as a Technology Preview

  NVMe over Fabrics TCP host and the target drivers have
  been added to RHCK in this release as a technology
  preview. Note that NVMe/TCP is already supported in
  Unbreakable Enterprise Kernel Release 6.

### GCC Toolset 10

Oracle Linux 8.3 provides the GCC Toolset 9, which is an Application
Stream that is distributed in the form of a Software Collection
in the `AppStream` repository. The GCC Toolset
is similar to the Oracle Linux Developer Toolset.

The GCC Toolset 10 contains up-to-date versions of the following
developer tools:

- GCC version 10.1.1
- GDB version 9.2
- Valgrind version 3.16.0
- SystemTap version 4.3
- Dyninst version 10.1.0
- `binutils` version 2.32
- `elfutils` version 0.180
- `dwz` version 0.12
- `make` version 4.2.1
- `strace` version 5.7
- `ltrace` version 0.7.91
- `annobin` version 9.21

The GCC Toolset 10 is available as an Application Stream within
the `AppStream` repository, in the form of a
Software Collection.

Install this toolset as follows:

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

### High Availability and Clusters

The following high availability and cluster features are
included in Oracle Linux 8.3:

- pacemaker updated to version 2.0.4

  In this release, the Pacemaker is updated to version
  2.0.4. This version of the Pacemaker provides a number of
  bug fixes over the previous version.
- Pacemaker support for recovery by demoting a promoted resource rather
  than fully stopping it

  In this release, you can configure a promotable resource
  in a Pacemaker cluster to ensure that if a promote or
  monitor action fails for that resource or the partition in
  which the resource is running loses quorum, the resource
  is demoted but not fully stopped.
- priority-fencing-delay cluster property added

  Pacemaker includes a the new
  `priority-fencing-delay` cluster
  property. This property enables you to configure a
  two-node cluster to ensure that in a split-brain
  situation, the node with the fewest resources running is
  fenced. This feature is useful in situations where you
  would prefer that the resource continue to be available in
  the unpromoted mode.
- Commands for managing multiple sets of resource and operation defaults
  added

  Commands for managing multiple sets of resource and
  operation defaults are included in this release. These new
  commands enable you to create, list, change, and delete
  multiple sets of resource and operation defaults. Also,
  when creating a set of default values, you can specify a
  rule that contains resource and op expressions. This
  capability enables you to configure a default resource
  value for all resources that are of a particular type. In
  addition, commands that list existing default values now
  include multiple sets of defaults in their output.
- Command for tagging cluster resources added

  You can now tag cluster resources in a Pacemaker cluster
  by using the `pcs tag` command. You can
  also use this command to remove or modify a resource tag,
  or display a tag configuration.

### Infrastructure Services

Oracle Linux 8.3 introduces several version updates to infrastructure
tools, including the following:

- Bind updated to version 9.11

  The `bind` package is updated to version
  9.11. Bind version 9.11 provides several bug fixes and
  enhancements over the previous version. Notable changes
  include increased reliability on systems that have
  multiple CPU cores and more detailed error detection, as
  well as improvements to the `dig` command
  and other tools, which now can print the Extended DNS
  Error (EDE) option, if present.
- Powertop updated to version 2.12

  The `powertop` packages are updated to
  version 2.12. Powertop version 2.12 includes several
  improvements over the previous version.
- Tuned updated to version 2.14.0

  The `tuned` packages are updated to
  version 2.14.0 in this release. Tuned version 2.14.0
  includes the following notable enhancements:

  - New `optimize-serial-console` profile.
  - A post loaded profile is included.
  - A `irqbalance` plugin for handing
    `irqbalance` settings is included.
  - Addition of architecture-specific tuning for Marvell
    ThunderX and AMD based platforms.
  - Scheduler plugin extended to include
    `cgroups-v1` for the CPU affinity
    setting.
- tcpdump updated to version 4.9.3

  The `tcpdump` utility is updated to
  version 4.9.3 to fix some Common Vulnerabilities and
  Exposures (CVEs).
- libpcap utility updated to version 1.9.1

  The `libpcap` utility is updated to
  version 1.9.1 to fix Common Vulnerabilities and Exposures
  (CVEs).
- memcached updated to version 1.5.22

  The `memcached` packages are updated to
  version 1.5.22. This version of Memcached includes several
  notable improvements over the previous version.

### Networking

Oracle Linux 8.3 introduces the following features, enhancements, and
changes:

- firewalld updated to version 0.8.2.

  The `firewalld` packages are updated to
  version 0.8.2 in this release. This version of
  `firewalld` includes a number of bug
  fixes over the previous version.
- IPv4 and IPv6 Netfilter tracking modules merged with nf\_conntrack module

  The `nf_conntrack_ipv4` and
  `nf_conntrack_ipv6` Netfilter connection
  tracking modules have merged with the
  `nf_conntrack` kernel module. A result of
  this change is that blocklisting address family-specific
  modules no longer works. In addition, you can now
  blocklist only the `nf_conntrack` module
  to disable connection tracking support for both IPv4 and
  IPv6.
- NetworkManager updated to version 1.26.0

  This version of `NetworkManager` provides
  several important improvements and changes, including the
  following:

  - `NetworkManager` resets the
    auto-negotiation, speed, and duplex setting to the
    original value when deactivating a device.
  - Wi-Fi profiles now connect automatically if all previous
    activation attempts failed, meaning an initial failure
    to auto -connect does not block the automatism.
  - `nm-settings-nmcli(5)` and
    `nm-settings-dbus(5)` manual pages
    added.
  - Several bridge parameters added.
  - Virtual routing and forwarding (VRF) interfaces added.
  - Opportunistic Wireless Encryption mode (OWE) for Wi-Fi
    networks added.
  - `mcli` utility improvement enables the
    removal of settings by using the
    `nmcli_connection modify` command.
  - `NetworkManager` improved to no longer
    create and activate secondary devices if the primary
    device is missing.
- XDP available as a Technology Preview

  The Express data path (XDP) feature has been added to RHCK
  in this release as a technology preview. XDP is a flexible
  and minimal kernel-based packet transport for high-speed
  networking. Note XDP is already supported in Unbreakable Enterprise Kernel Release 6
  (UEK R6).

### Security

Oracle Linux 8.3 introduces the following security features,
enhancements, and changes:

- CyrusSASL support for channel bindings with SASL/GSSAPI and
  SASL/GSS-SPNEGO plugins

  Support has been added in this release for channel
  bindings by using SASL/GSSAPI and SASL/GSS-SPNEGO plugins.
  When used in the `openldap` libraries,
  the feature provides CyrusSASL with the ability to
  maintain compatibility with and access to Microsoft Active
  Directory and Microsoft Windows systems, which introduce
  mandatory channel binding for LDAP connections.
- gnutls updated to version 3.6.14

  The `gnutls` packages are updated to
  version 3.6.14 in this release. This version of the
  `gnutls` packages include several bug
  fixes and improvements over the previous version.
- Libreswan updated to version 3.32

  In this release, Libreswan has been updated to version
  3.32. This version of Libreswan provides several new
  features and bug fixes, including the following notable
  changes:

  - A separate FIPS 140-2 certification is no longer
    required.
  - Implementation the cryptographic recommendations of RFC
    8247, and changes the preference from SHA-1 and RSA-PKCS
    v1.5 to SHA-2 and RSA-PSS.
  - Support for XFRMi virtual ipsecXX interfaces, which
    simplify the writing of firewall rules.
  - Improvement to the recovery of crashed and rebooted
    nodes in a full-mesh encryption network.
- libseccomp library updated to version 2.4.3

  The `libseccomp` library is updated to
  version 2.4.3. This library provides an interface to the
  `seccomp` syscall filtering mechanism.
  This version of the `libseccomp` library
  also includes a number of bug fixes and enhancements over
  the previous version.
- libcap support for ambient capabilities

  You can now grant ambient capabilities at login, which
  eliminates the need to have `root` access
  for appropriately configured processes.
- libkcapi updated to version 1.2.0

  The `libkcapi` package is updated to
  version 1.2.0. This version of `libkcapi`
  includes minor changes over the previous version.
- libssh library updated to version 0.9.4

  The `libssh` library is updated to
  version 0.9.4. This library implements the SSH protocol.
- setools package updated to version 4.3.0

  The `setools` package is updated to
  version 4.3.0. This package provides a collection of tools
  that facilitates the SELinux policy analysis feature.
  Several bug fixes and enhancements are included in this
  version of the `setools` package.

  Note:

  The `setools` package requires the
  following additional packages:
  `setools-console`,
  `setools-console-analyses`, and
  `setools-gui`.
- stunnel updated to version 5.56

  The `stunnel` encryption wrapper is
  updated to version 5.56. This version of the
  `stunnel` packages includes a number of
  new features and bug fixes, including the following:

  - `ticketKeySecret` and
    `ticketMacSecret` options for
    controlling confidentiality and integrity protection of
    the issued session tickets. These options enable you to
    resume sessions on other nodes in a cluster.
  - `curves` option, which controls the
    list of elliptic curves in OpenSSL 1.1.0 and later.
  - `ciphersuites` option to control the
    list of permitted TLS 1.3 ciphersuites.
  - `sslVersion`,
    `sslVersionMin` and
    `sslVersionMax` for OpenSSL 1.1.0 and
    later added.
- update-crypto-policies and fips-mode-setup relocated to
  crypto-policies-scripts

  In this release, the
  `update-crypto-policies` and
  `fips-mode-setup` scripts are moved to
  the `crypto-policies-scripts` package,
  which is a separate RPM subpackage. This package is
  automatically installed through the Recommends dependency
  on regular installations.

#### SCAP and OpenSCAP Improvements

- OpenSCAP updated to version 1.3.3

  In this release, the `openscap`
  packages are updated to version 1.3.3. This version of
  OpenSCAP includes several bug fixes and improvements
  over the previous version, including the following
  notable changes:

  - `autotailer` script is added. This
    script enables you to generate tailoring files by
    using a CLI.
  - Timezone part is added to the Extensible Configuration
    Checklist Description Format (XCCDF) TestResult start
    and end time stamps.
  - `yamlfilecontent` independent probe
    included as a draft implementation.
  - `urn:xccdf:fix:script:kubernetes` fix
    type introduced in XCCDF
  - Ability to generate the
    `machineconfig` fix added.
  - `oscap-podman` tool can detect
    ambiguous scan targets.
  - `rpmverifyfile` probe can verify
    files from the `/bin` directory.
  - Fixed crashes when complicated regexes are executed in
    the `textfilecontent58` probe.
  - Evaluation characteristics of the XCCDF report are
    consistent with OVAL entities from the
    `system_info` probe.
  - Fixed file-path pattern matching in offline mode in
    the  `textfilecontent58` probe.
  - Fixed infinite recursion in the
    `systemdunitdependency` probe.
- SCAP Workbench tool can generate results-based remediation from tailored
  profiles

  You are now able to generate results-based remediation
  roles from tailored profiles by using the `SCAP
  Workbench` tool.
- scap-security-guide packages updated to version 0.1.50

  The `scap-security-guide` packages have
  been updated to version 0.1.50. These packages contain
  the latest set of security policies for Linux systems,
  as well as bug fixes and several enhancements over the
  previous version improved Ansible content and several
  fixes and improvements to the
  `scap-security-guide` content for
  scanning systems.

#### SELinux Improvements

- fapolicyd packages updated to version 1.0

  The `fapolicyd` package are updated to
  version 1.0. Several bug fixes and enhancements are
  included in this version of the
  `fapolicy` packages.
- fapolicyd includes an SELinux policy in fapolicyd-selinux

  The `fapolicyd` framework now provides
  its own SELinux security policy. The daemon is confined
  under the `fapolicyd_t` domain. The
  policy is installed through the
  `fapolicyd-selinux` subpackage.
- Individual CephFS files and directories can include SELinux labels

  The storing of SELinux labels in the extended attributes
  of files has been enabled in the Ceph File System
  (CephFS). This enhancement enables you to change the
  labels for individual files and SELinux defines the
  labels of any newly created files based on transition
  rules. Any files that were previously unlabeled retain
  the `system_u:object_r:cephfs_t:s0`
  label until explicitly changed.

### Virtualization

The following virtualization features, enhancements, and changes
are included in this release:

- Bochs display device included

  The Bochs display device, which is introduced in this
  release, is more secure than the `stdvga`
  device. Note that all VMs that are compatible with
  `bochs-display`, mainly those that used
  UEFI, will use this device by default.
- virsh guestinfo command option added

  The `virsh guestinfo` command option
  provides the ability to report information about a virtual
  machine (VM), including the following: host name, guest OS
  information, active users, and time zone that is used.

  To enable the `virsh guestinfo` command
  option, install the `qemu-guest-agent`
  package on the guest OS of the target VM. You must also
  enable the `guest_agent` channel in the
  VMâs XML configuration.
- Capability for creating QCOW2 disk images on RBD

  In this release, you can create QCOW2 disk images on RADOS
  Block Device (RBD) storage, which means that VMs are now
  capable of using RBD servers for their storage backends
  with QCOW2 images.

  Note that write performance of QCOW2 disk images on RBD
  storage is currently lower than intended.
- Capability for migrating VMs with disk cache enabled

  The `libvirt` library is compatible with
  disk cache live migration in this release, which now makes
  it possible to live-migrate VMs with disk cache enabled.
- Control Group v2 support added for VMs

  The `libvirt` suite now supports control
  groups v2, which means that VMs hosted on Oracle Linux 8 can now
  take advantage of the resource control capabilities
  provided by Control Group v2.
- IBM POWER 9 XIVE support included

  Support for the External Interrupt Virtualization Engine
  (XIVE) feature of IBM POWER9 to RHEL 8 is included in this
  release. This improvement enables VMs that are running on
  an Oracle Linux 8 hypervisor on an IBM POWER 9 system to use XIVE,
  which improves the performance of I/O-intensive VMs.
- QEMU packed virtqueue layout support

  The packed virtqueue layout that was introduced in
  VirtIO-1.1 is now supported in QEMU. The new format
  enables the exchange of requests by using a more compact
  descriptor representation. This change makes it easier to
  implement `virtIO` on hardware, as well
  as increases system performance.
- QEMU logs include time stamps

  As of this release, all logged QEMU events have a time
  stamp. This improvement enables you to more easily
  troubleshoot your VMs using logs in the
  `/var/log/libvirt/qemu/` directory.
- QEMU/KVM support for discard and write-zeros commands included

  The `discard` and
  `write-zeroes` commands for the
  `virtio-blk` protocol are now supported
  in QEMU/KVM. This change enables VMs to use the
  `virtio-blk` device to discard unused
  sectors of an SSD, fill sectors with zeroes when they are
  emptied, or both. You can use this capability to increase
  SSD performance and also ensure that a drive is securely
  erased.
- QEMU now uses gcrypt library for XTS ciphers

  The QEMU emulator is updated to use the XTS cipher mode
  implementation that is provided by the
  `gcrypt` library. This change improves
  the I/O performance of VMS with host storage that uses
  QEMUâs native LUKS encryption driver.
- macvtap interfaces can be used by VMs in non-privileged sessions

  In this release, VMs can use a pre-existing
  `macvtap` interface that was previously
  created by a privileged process. This change enables VMs
  that are started by the non-privileged user session of
  `libvirtd` to use a
  `macvtap` interface.
- Maximum number of supported VFIO devices increased to 64

  In this release, you can attach up to 64 PCI devices that
  use VFIO to a single VM on an Oracle Linux 8 host. This number is
  increased from up to 32 PCI devices in Oracle Linux 8.2 and
  previous releases.
- nbdkit logging improvement

  In this release, `nbdkit` service logging
  is updated to be less verbose: now, only potentially
  important messages are logged. Also, logs that are created
  during `virt-v2v` conversions are now
  shorter and easier to interpret.
- virsh iothreadset command option added

  You can use the new `virsh iothreadset`
  command option to configure dynamic IOThread polling. This
  additional option makes it possible to set up VMs with
  lower latencies for I/O-intensive workloads at the expense
  of greater CPU consumption for the IOThread. For more
  information and available options, see the
  `virsh(1)` manual page.
- VNNI for BFLOAT16 inputs supported by KVM

  Vector Neural Network Instructions (VNNI) supporting
  `BFLOAT16` inputs, or
  `AVX512_BF16` instructions, are now
  supported by KVM hosts that are running on the 3rd Gen
  Intel Xeon scalable processors (Cooper Lake processors).
  This change enables guest software to se the
  `AVX512_BF16` instructions that reside
  inside VMs which is enabled in the virtual CPU
  configuration.

### Web Console Option for Switching Access Modes

In Oracle Linux 8.3, the Cockpit web console includes a new option for
switching between administrative access mode and limited access
mode, from within a user's session. Click the
Administrative access or
Limited access
indicator in your web console session to switch modes.

### Technology Preview

For the Red Hat Compatible Kernel in the current Oracle Linux 8 release, the following
features are under technology preview:

#### aarch64 only: VNC Remote Console

In this release, the Virtual Network Computing (VNC) remote
console is available as a technology preview on the 64-bit Arm
platform only. The remaining components of
the graphics stack are unverified on this platform.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.3/ol8-KnownIssues.html -->

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

#### Changing installation source results in errors if alternative installation repository is set at boot

If the installer is booted with the `inst.repo` option set,
changing the installation source to use a CD or DVD device within the installer results in an
error that prevents you from continuing the installation, unless you set the source back to
the original source that was set at boot.

If you set the `inst.repo` option to point to
a hard disk and then attempt to change the installation source
inside the installer, the installer displays an error; but,
you can still proceed with the installation.

To avoid these issues, do not set the `inst.repo` option at boot if you do
not intend to use the installation source that is provided. Or, use the
`inst.repo` source that is defined at boot without attempting to change
installation source inside the installer.

(Bug ID 30316179)

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

#### Version of libpcap packages in BaseOS channel does not support RDMA

The `libpcap` packages that are in the BaseOS
channel do not support dumping RDMA sniffer information. After
installing or upgrading to Oracle Linux 8.3, if you require RDMA
functionality, you should run the `dnf
downgrade` command to downgrade your
`libpcap` version so that you can use the
`libpcap` packages that are published to the
`ol8_UEKR6_RDMA` repository, for example:

```
sudo dnf downgrade libpcap
```

(Bug ID 32049290)

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

#### aarch64 only: bcache error on UEK R6 during subsequent attempt to register cache device

An attempt to subsequently register a cache set after removing
it fails with the following error:

```
echo "CACHE_DEV" > /sys/fs/bcache/register
        echo: write error: Invalid argument
```

The following error message is displayed in the `dmesg` output:

```
bcache: register_bcache() error /dev/CACHE_DEV: Not a bcache superblock
```

This issue is related to 64KB page size
(`CONFIG_ARM64_64K_PAGES=y`), which
`bcache` currently does not support.

Because the superblock for the cache device becomes corrupted
during this process, it is not possible to re-register the
device.

To work around this issue, reinstall the `bcache-tools` package and then
create a new `bcache` configuration.

As an alternative, avoid using a `bcache` configuration on Oracle Linux
8 (aarch64) systems.

(Bug ID 30210051)

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

### SAN boot may fail when using an Emulex 32GB FC Adapter

Booting from a multipath attached LUN when using the Emulex 32GB
FC Adapter may fail. Note that booting from single path attached
LUNs are not affected by this issue. To work around the issue,
add the `rd.multipath=1 rd.driver.pre=lpfc`
boot parameter.

For systems with multiple boot disks, such as a local boot disk
and a SAN boot disk, the `rd.driver.pre=lpfc`
option does not guarantee that the SAN attached storage is
discovered first. To avoid booting from devices other than the
SAN, such as from a local disk, additional
`module_blacklist=disk_driver`
boot options are required; for example,
`rd.driver.blacklist=megaraid_sas
module_blacklist=megaraid_sas`.

(Bug ID 31898488)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.3/ol8-PackageChangesfromtheUpstreamRelease.html -->

The following sections list the changes to binary and source
packages from the upstream release.

### Changes to Binary Packages

This section contains information about the removed, modified, and new binary packages in this release. For information about the source package changes, see [Changes to Source Packages](ol8-PackageChangesfromtheUpstreamRelease.html#ol8-packages-source) .

#### Added Binary Packages for BaseOS by Oracle

The following binary packages have been added to BaseOS by Oracle:

- `bcache-tools`
- `btrfs-progs`
- `dtrace`
- `dtrace-devel`
- `dtrace-testsuite`
- `kernel-uek`
- `kernel-uek-debug`
- `kernel-uek-debug-devel`
- `kernel-uek-devel`
- `kernel-uek-doc`
- `ocfs2-tools`
- `oracle-backgrounds`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`
- `oracle-logos-httpd`
- `oracle-logos-ipa`

#### Added Binary Packages for AppStream by Oracle:

The following binary packages have been added to AppStream by Oracle:

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
- `mozjs52`
- `mozjs60`
- `nscd`
- `nss_db`
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
- `iproute-devel`
- `iscsi-initiator-utils-devel`
- `kmod-devel`
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
- `cockpit-dashboard`
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
- `efi-srpm-macros`
- `firefox`
- `firewall-applet`
- `firewall-config`
- `gcc`
- `gcc-c++`
- `gcc-gdb-plugin`
- `gcc-gfortran`
- `gcc-offload-nvptx`
- `gdb`
- `gdb-doc`
- `gdb-gdbserver`
- `gdb-headless`
- `git-clang-format`
- `glibc-utils`
- `gnome-themes-standard`
- `golang`
- `golang-bin`
- `golang-docs`
- `golang-misc`
- `golang-race`
- `golang-src`
- `golang-tests`
- `grafana-pcp`
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
- `python3-rhn-check`
- `python3-rhn-client-tools`
- `python3-rhnlib`
- `python3-rhnpush`
- `python3-rhn-setup`
- `python3-rhn-setup-gnome`
- `python3-sanlock`
- `python3-spacewalk-backend-libs`
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

- `dnf-plugin-subscription-manager`
- `grub2-ppc64le-modules`
- `kpatch`
- `perl-DBI`
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
- `rhsm-gtk`
- `spice-client-win-x64`
- `spice-client-win-x86`
- `spice-qxl-wddm-dod`
- `spice-vdagent-win-x64`
- `spice-vdagent-win-x86`
- `subscription-manager-initial-setup-addon`
- `subscription-manager-migration`
- `subscription-manager-migration-data`
- `toolbox`
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
- `iproute`
- `iptables`
- `iscsi-initiator-utils`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `ksc`
- `libdnf`
- `libkcapi`
- `libreport`
- `libxml2`
- `libxslt`
- `linux-firmware`
- `mcelog`
- `microcode_ctl`
- `mozjs52`
- `mozjs60`
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
- `binutils`
- `buildah`
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
- `efi-rpm-macros`
- `firefox`
- `firewalld`
- `gcc`
- `gdb`
- `glibc`
- `gnome-themes-standard`
- `golang`
- `grafana-pcp`
- `httpd`
- `icedtea-web`
- `initial-setup`
- `ipa`
- `ksh`
- `libguestfs`
- `libreoffice`
- `libreport`
- `libreswan`
- `libvirt`
- `libxml2`
- `libxslt`
- `lorax`
- `lorax-templates-rhel`
- `mecab-ipadic`
- `nbdkit`
- `nginx`
- `openchange`
- `openscap`
- `open-vm-tools`
- `osinfo-db`
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
- `rhn-client-tools`
- `rhn-custom-info`
- `rhnlib`
- `rhnpush`
- `rhnsd`
- `rpmdevtools`
- `sanlock`
- `sblim-cmpi-devel`
- `scap-security-guide`
- `scap-workbench`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `skopeo`
- `sos-collector`
- `spacewalk-backend`
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

- `crash`
- `cups-filters`
- `gcc`
- `glibc`
- `iproute`
- `iscsi-initiator-utils`
- `kmod`
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
- `spice-qxl-wddm-dod`
- `subscription-manager-migration-data`
- `toolbox`
- `virtio-win`
- `virt-who`