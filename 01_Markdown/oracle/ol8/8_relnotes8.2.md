---
title: "Release Notes for Oracle Linux 8.2"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.2"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol8"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

Release Notes for Oracle Linux 8.2

F31299-15

November 2022

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 8 Release Notes for Oracle Linux 8.2

F31299-15

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2020, 2022, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.2/ol8.2-Preface.html -->

[Oracle Linux 8: Release Notes for Oracle Linux
8.2](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.2/) provides information about the new features
and known issues in the Oracle Linux 8.2 release. The information applies to both x86\_64 and
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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.2/ol8-AboutOracleLinux8.html -->

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

For the x86\_64 platform, Oracle Linux 8.2 ships with the following kernel packages:

- `kernel-4.18.0-193.el8`: Red Hat Compatible Kernel (RHCK)
- `kernel-uek-5.4.17-2011.1.2.el8uek`: Unbreakable Enterprise Kernel
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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.2/ol8.2-NewFeaturesandChanges.html -->

This chapter describes new features, major enhancements, bug fixes, and other changes that
are introduced in Oracle Linux 8.2. These features generally apply to both the x86\_64 and Arm
(aarch64) platforms, unless otherwise noted. For information that applies specifically to the
Arm platform, see <unresolvable-reference.html#ol8-arm-only>.

### Red Hat Compatible Kernel

The following notable features, enhancements, and changes apply
to the Red Hat Compatible Kernel (RHCK) that is shipped with
Oracle Linux 8.2 on the x86\_64 platform.

For more information about the Unbreakable Enterprise Kernel Release 6 (UEK R6) release that is
shipped with Oracle Linux 8.2, refer to the [Unbreakable Enterprise Kernel: Release Notes for
Unbreakable Enterprise Kernel Release 6 (5.4.17-2011)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/).

- kexec-tools documentation includes Kdump FCoE target support

  The documentation for the `kexec-tools`
  now includes Kdump FCoE target support information. This
  enhancement enables users to obtain a better understanding
  of the status and details of `kdump` on
  FCoE target support.
- numactl manual page updated to clarify information about memory usage

  The `numactl(8)` manual page now
  explicitly mentions that the memory usage information
  reflects just the resident pages on the system. This
  change eliminates any possible confusion with regards to
  whether the documented memory usage information refers to
  resident pages or virtual memory.
- rngd can run with non-root privileges

  In this update, the random number generator daemon
  (`rngd`) is capable of running with
  non-root user privileges, which enhances system security.
  The `rngd` daemon checks whether data
  that is supplied by the source of randomness is
  sufficiently random and then stores it in the kernelâs
  random-number entropy pool.
- Secure Boot available by default

  The default value for the `secure=` boot
  option was not set to `auto` in previous
  releases, thereby rendering this feature unavailable. In
  this update, the default value for this boot option is set
  to `auto` and the secure boot feature is
  now available, unless it was previously configured
  otherwise.

### Compilers and Developer Toolsets

Oracle Linux 8.2 introduces the following features, enhancements, and
changes to compilers and developer toolsets.

#### Compiler Toolsets

The following compiler toolsets have been updated. These
toolsets are distributed as Application Streams in Oracle Linux 8.2:

- Clang toolset updated to version 9.0.0

  This toolset has been updated to version 9.0.0. Features
  that are included in this Clang version include the
  following: the LLVM compiler infrastructure framework,
  the Clang compiler for the C and C++ languages, the LLDB
  debugger, and related tools for code analysis.
- Rust toolset updated to version 1.39

  This toolset has been updated to version 1.39. This
  version of the Rust toolset provides the Rust
  programming language compiler
  (`rustc`), the `cargo`
  build tool and dependency manager, as well any required
  libraries.
- Go toolset updated to 1.13.4

  This toolset, which provides the Go
  (`golang`) programming language tools
  and libraries, has been updated to version 1.13.4. This
  version of the Go toolset also includes the
  `Delve` debugger for the Go programming
  language.

#### GCC Toolset 9

Oracle Linux 8.2 provides the GCC Toolset 9, which is an Application
Stream that is distributed in the form of a Software
Collection in the `AppStream` repository. The
GCC Toolset is similar to the Oracle Linux Developer Toolset.

The GCC Toolset 9 contains up-to-date versions of the
following developer tools:

- GCC version 9.2.1
- GDB version 8.3
- Valgrind version 3.15.0
- SystemTap version 4.1
- Dyninst version 10.1.0
- `binutils` version 2.32
- `elfutils` version 0.176
- `dwz` version 0.12
- `make` version 4.2.1
- `strace` version 5.1
- `ltrace` version 0.7.91
- `annobin` version 8.7.9

The GCC Toolset 9 is available as an Application Stream within
the `AppStream` repository, in the form of a
Software Collection.

You can install this toolset as follows:

```
sudo dnf install gcc-toolset-9
```

To run a tool from GCC Toolset 9, use the following command:

```
scl enable gcc-toolset-9 tool
```

The following command runs a shell session, where tool
versions from the GCC Toolset 9 take precedence over system
versions of the same tools:

```
                     scl enable gcc-toolset-9 bash
```

### Database

This release of Oracle Linux 8 ships with version 8.0 of the MySQL database software.

### Dynamic Programming Languages, Web and Database Servers

The following dynamic programming languages, and web and
database features and improvements are introduced in this
update.

#### maven:3.6 Module Included

The `maven:3.6` module stream is included in
Oracle Linux 8.2. The Maven software project management and
comprehension tool includes several bug fixes and enhancements
over the `maven:3.5` stream version that was
included in Oracle Linux 8.

#### mod\_wsgi Installation Changes

In previous releases, if you attempted to install the
`mod_wsgi` module by using the `dnf
install mod_wsgi` command, the
`python3-mod_wsgi` package was installed. The
introduction of Python 3.8 in Oracle Linux 8.2 requires that you to now
specify which version of `mod_wsgi` you want
to install, as Python 3.6 is also supported in this release.
If you do not specify the `mod_wsgi` version,
an error message is displayed.

For example, if you wanted to install the Python 3.6 version
of `mod_wsgi`, enable the
`python36` module and then install the
package as follows:

```
sudo dnf module enable python36
sudo dnf install python3-mod_wsgi
```

To install the Python 3.8 version of the package enable the
`python38` module and then install the
package as follows:

```
sudo dnf module enable python38 
sudo dnf install python38-mod_wsgi
```

Note:

The `python3-mod_wsgi` and
`python38-mod_wsgi` packages conflict with
each other. This conflict is due to a limitation with the
Apache HTTP Server. As such, only one
`mod_wsgi` module can be installed on a
system at any given time.

#### perl-LDAP and perl-Convert-ASNI Packages Included

Oracle Linux 8.2 includes the `perl-LDAP` and
`perl-Convert-ASN1` packages. The`perl-LDAP` package provides an LDAP client for the
Perl language. Note that the `perl-LDAP`
package requires the `perl-Convert-ASN1`
package. This package encodes and decodes Abstract Syntax
Notation One (ASN.1) data structures by using Basic Encoding
Rules (BER) and Distinguished Encoding Rules (DER).

#### Python 3.8 Introduced

Oracle Linux 8.2 includes Python 3.8, which is provided by a new
`python38` module. Python 3.8 includes
several enhancements over the previous Python 3.6 version,
including improvements to the developer experience and better
performance. Other notable changes include new Python modules
and language features, improved support for optional static
type hints, and updated versions of some packages, such as
`pip`, `requests`, and
`Cython`.

Note that Python 3.6 continues to be supported in Oracle Linux 8. You
can install Python 3.8 and the packages that are built for it
in parallel with Python 3.6, on the same system.

For example, you would install packages from the
`python38` module as follows:

```
sudo dnf install python38
sudo dnf install python38-Cython
```

Running the previous command automatically enables the
`python38:3.8` module.

### File Systems and Storage

Oracle Linux 8.2 provides the following file systems and storage
features, enhancements, and changes:

- Btrfs file system removed from RHCK

  The Btrfs file system is removed from RHCK in Oracle Linux 8. As
  such, you cannot create or mount Btrfs file systems when
  using this kernel. Also, any Btrfs user-space packages
  that are provided are not supported with RHCK.

  Note:

  Support for the Btrfs file system is enabled in UEK R6.
  For more information about other enhancements that have
  been made to Btrfs in UEK R6, see
  [Unbreakable Enterprise Kernel: Release Notes for
  Unbreakable Enterprise Kernel Release 6 (5.4.17-2011)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/).
- OCFS2 file system removed from RHCK

  The Oracle Cluster File System version 2 (OCFS2) file
  system is removed from RHCK in Oracle Linux 8. As such, you cannot
  create or mount OCFS2 file systems when using this kernel.
  Also, any OCFS2 user-space packages that are provided are
  not supported with RHCK.

  Note:

  OCFS2 is fully supported with UEK R6 in Oracle Linux 8.2.
- dm-writecache caching method added for LVM cache volumes

  In this update, Logical Volume Manager (LVM) cache volumes
  include the `dm-writecache` caching
  method, as well as the existing hot-spot
  (`dm-cache`) method.

  The `dm-writecache` method caches write
  operations only. The faster volume,
  typically an SSD or a persistent memory (PMEM) disk, stores
  the write operations first and then migrates these
  operations to the slower disk in the background.

  Use the `lvconvert` command with the
  `--type cache` or `--type
  writecache` option to configure a caching method.

  Note:

  See <unresolvable-reference.html#ol8-issues-31203340> for further
  information about the limitations of this feature.

### Infrastructure Services

Oracle Linux 8.2 introduces the following infrastructure services
features, enhancements, and changes:

- Bind updated to version 9.11.13

  In this update, the `bind` packages have
  been updated to version 9.11.13. This version of Bind
  includes several improvements over the previous version,
  including new features and commands, as well as
  improvements to existing commands and functionality.
- Tuned updated to version 2.13

  The `tuned` packages are updated to
  version 2.13 in this update. This version of Tuned
  provides several bug fixes and enhancements over the
  previous version.

### Networking

Oracle Linux 8.2 introduces the following features, enhancements, and
changes:

- eBPF for Traffic Control kernel subsystem supported

  In this update, the Traffic Control
  (`tc`) kernel subsystem and the
  `tc` tool is capable of attaching to
  extended Berkeley Packet Filtering (eBPF) programs as
  packet classifiers and actions for both the ingress and
  egress queueing disciplines. Note that eBPF for
  `tc` was previously available as a
  technology preview only.
- firewalld updated to version 0.8

  The `firewalld` packages are updated to
  version 0.8 in this update. This version of
  `firewalld` provides several performance
  improvements, including all bug fixes since version 0.7.0.

  Other notable changes include the following:

  - `firewalld` now uses the
    `libnftables` JSON interface, which is
    part of the `nftables` subsystem.
  - Service definitions include a new helper element, which
    replaces module.
  - Custom helpers can now use standard helper modules.
- firewalld service can use connection tracking helpers for services that
  are running on a non-standard port

  The `firewalld` service's user-defined
  helpers can now use standard kernel helper modules. This
  improvement provides the capability for creating
  `firewalld` rules that use connection
  tracking helpers for services that are running on a
  non-standard port.
- User-space applications can retrieve the netns ID selected by the kernel

  In this update, capability has been added for user-space
  applications to request that the kernel select a new
  `netns` ID and then assign it to a
  network name space. This improvement provides user-space
  applications with a more reliable option for identifying
  the `netlink` ID selected by the kernel.
  You can now specify the `NLM_F_ECHO`
  option when sending an
  `RTM_NETNSIDnetlink` message to the
  kernel. The kernel then returns a
  `netlink` message, which includes the
  `netns` ID, which is set to the value
  that is selected by the kernel
- whois package added

  The `whois` package is included in
  Oracle Linux 8.2. The `whois` package provides
  capability for retrieving information about a specific
  domain name or IP address.

### Podman, Buildah, and Skopeo Container Tools

The `podman`, `buildah`, and
`skopeo` container tools that were introduced
in the Oracle Linux 8 release are supported on both UEK R6 and RHCK in
Oracle Linux 8.2. These tools are compatible with the Open Container
Initiative (OCI) and can be used to manage the same Linux
containers that are produced and managed by Docker and other
compatible container engines. Because these tools are
light-weight and primarily focused on a subset of features, you
can run them minus the overhead of working with a daemon
process. For more details about these tools, see
[Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).

### Security

Oracle Linux 8.2 introduces the following security features,
enhancements, and changes:

- Audit updated to version 3.0-0.14

  The `audit` packages have been updated to
  version 3.0-0.14. This version of Audit provides many bug
  fixes and enhancements over the previous version.
- Audit includes several improvements from kernel v5.5-rc1

  The version of Audit that is provided in this update
  includes several enhancements, bug fixes, and cleanups
  related to the Audit subsystem, many of which were
  introduced between versions 4.18 and 5.5-rc1 of Audit.
- lvmdbusd service confined by SELinux

  In this update, the `lvmdbusd` executable
  file has the `lvm_exec_t` context
  defined. This change means the `lvmdbusd`
  daemon can now be used correctly with SELinux in enforcing
  mode. Previously, the `lvmdbusd` daemon
  could not transition to the `lvm_t`
  context, irrespective of whether the SELinux policy for
  `lvm_t` was defined. The result was that
  the `lvmdbusd` daemon was executed in the
  `unconfined_service_t` domain, with
  SELinux labeling `lvmdbusd` as
  unconfined.
- openssl-pkcs11 updated to version 0.4.10

  The `openssl-pkcs11` package has been
  updated to version 0.4.10. This version of the package
  includes several bug fixes and enhancements over the
  previous version. Note that the
  `openssl-pkcs11` package provides access
  to PKCS #11 modules through the engine interface.
- oscap-podman tool added

  The `openscap` packages have been updated
  to include the new `oscap-podman` tool
  for security and compliance scanning of containers. Note
  that this tool is contained in the
  `openscap-utils` package.
- rsyslog updated to version 8.1911.0

  The `rsyslog` packages have been updated
  to version 8.1911.0, which provides numerous bug fixes and
  enhancements over the previous version.
- SCAP Security Guide includes ACSC Essential Eight and DISA STIG for
  Oracle Linux 8 support

  The `scap-security-guide` packages in
  Oracle Linux 8.2 provides the following new profiles:

  - Australian Cyber Security Centre (ACSC) Essential Eight
    compliance profile aligned to the security baseline
    defined by ACSC
  - [DRAFT] DISA STIG for Oracle Linux 8 compliance profile aligned
    to the STIG security controls published by DISA.

  This improvement enables you to install a system that
  conforms to one of these security baselines.

  Also, you can now use the OpenSCAP suite to check security
  compliance and remediation by using this specification,
  which provides minimum security controls, as defined by
  corresponding baseline.
- SELinux setools-gui and setools-console-analyses packages included

  The `setools-gui` package, which was
  included in Oracle Linux 7, is re-introduced in Oracle Linux 8.2. You can
  use the tool to inspect relations and data flows,
  particularly in multi-level systems with highly
  specialized SELinux policies. You can also use the
  `apol` graphical tool that is available
  with the `setools-gui` package to inspect
  and analyze various aspects of an SELinux policy. In
  addition, you can use the tools that are included with the
  `setools-console-analyses` package to
  analyze domain transitions and SELinux policy information
  flows.
- SELinux improved to enable confined users to manage user session
  services

  Confined users can now manage user sessions. In previous
  releases, confined users could not manage user session
  services, which meant they could not execute the
  `systemctl --user` or `busctl
  --user` commands or work in the web console.
- semanage export able to display customizations related to permissive
  domains

  The `semanage` command, which is part of
  the `policycoreutils` package for
  SELinux, has been improved. You can now use the command to
  display customizations for permissive domains. You can now
  also use the `semanage export` command to
  transfer permissive local modifications between systems.
- semanage includes capability for listing and modifying SCTP and DCCP
  ports

  Oracle Linux 8.2 includes SCTP and DCCP protocol support for the
  `semanage port` command. This enhancement
  enables you to check whether two systems can communicate
  by using SCTP. In addition, the ability to fully enable
  SCTP features to successfully deploy SCTP-based
  applications is also provided. In previous releases, you
  could only list and modify TCP and UDP ports by using the
  `semanage port` command.
- Sudo updated to version 1.8.29-3

  The `sudo` packages have been updated to
  version 1.8.29-3. This version of Sudo includes several
  major changes, bug fixes, and improvements over the
  previous version.
- Udica capable of adding new allow rules generated from SELinux denials
  to existing container policy

  The `udica` command has been improved.
  Now, if a container that is running under a policy
  generated by the `udica` command triggers
  an SELinux denial, the command is able to update the
  policy. You can use the new `-a` or
  `--append-rules` option to append rules
  from an AVC file.

### User-Agent Header String Improvement

In this update, the `User-Agent` header string
that is normally part of HTTP requests that are made by DNF has
been extended to include information that is read from the
`/etc/os-release` file. See the
`dnf.conf(5)` manual page for more specific
details.

### Virtualization

The following virtualization features, enhancements, and changes
are introduced in this update:

- virt-install returns more helpful message when creating VM from an
  install tree

  The `virt-install` command has been
  improved to include a workaround for an issue that caused
  booting to fail on Oracle Linux 7 and earlier Oracle Linux 8 releases if the
  `--location` option was also specified.
  The command now returns a more helpful message that
  include instructions on how to work around the problem
  should such a failure occur.
- EDK2 updated to version stable201908

  The `EDK2` package has been updated to
  version `stable201908`. This version of
  EDK2 includes several improvements, including support for
  `OpenSSL-1.1.1`. Another notable change
  in this version of EDK2 is that the
  `EDK2` package license has changed from
  `BSD and OpenSSL and MIT` to
  `BSD-2-Clause-Patent and OpenSSL and
  MIT`.
- Nested virtualization capability added for KVM

  This release provides support for nested virtualization on
  kernel-based Virtual Machines (KVMs) that are running on
  an Intel 64 host. This enhancement enables an Oracle Linux 7 or
  Oracle Linux 8 VM that is running on an Oracle Linux 8 physical host to
  perform as a hypervisor, as well as host its own VMs.

  Note:

  On AMD64 systems, nested KVM virtualization continues to
  be a Technology Preview feature.
- virt-manager application deprecated

  The Virtual Machine Manager application
  (`virt-manager`) is deprecated in this
  release. Oracle recommends that you use the Cockpit web
  console to manage virtualization. Note that some features
  in Oracle Linux 8 might still only be accessible by using either
  `virt-manager` or the command line.
- VM snapshots deprecated

  The current mechanism for creating VM snapshots is
  deprecated and not working reliably in this release. It is
  therefore recommended that you do not use snapshots in
  Oracle Linux 8.

### Web Console

Oracle Linux 8.2 introduces the following features, improvements, and
changes for the Cockpit web console:

- Web console login changes

  Starting with this update, you are now automatically
  logged out of your current web console session after 15
  minutes of inactivity. To modify this setting, adjust the
  timeout in minutes by editing the
  `/etc/cockpit/cockpit.conf` file. Another
  change in this update includes optional capability for
  showing the content of banner files on the web console's
  login screen, which is similar to SSH behavior. You must
  configure this functionality in the
  `/etc/cockpit/cockpit.conf` file to use
  it.
- Option for logging into the web console with a TLS client certificate
  added

  You can now configure the web console to log in with a TLS
  client certificate that is provided by a browser or a
  device, such as smart card or a YubiKey.
- Storage page updates

  Creating a new file system in the web console now always
  required a specified mount point. This page also no longer
  offers the "Default" choice when mounting a file system.

  The web console now hides the distinction between the
  `/etc/fstab` and the
  `/proc/mounts` run-time state
  configuration. Any changes that you make in the web console
  apply to both the configuration and the run-time state. In
  the event that the configuration and the run-time state
  differ from each other, the web console issues a warning to
  enable you to more easily synchronize these configurations.
- Virtual Machines page updates

  Several storage improvements have been made to the Virtual
  Machines page, including the following: storage volume
  creation works for all
  `libvirt-supported` types and you can now
  create storage pools on a LVM or iSCSI device. Also, the
  Virtual Machines page includes capability for creating and
  removing virtual network interfaces.
- Web console redesigned to use the PatternFly 4 UI design system

  The PatternFly 4 design is implemented in this update.
  This design provides improved accessibility and also more
  closely matches the OpenShift 4 design. Another important
  feature improvement is a redesigned Overview page that is
  easier to understand. The following additional
  improvements have been made: health information is more
  prominent, resource graphs have been moved to a separate
  page, and the hardware information page is much easier to
  locate. The new design also provides a new Search field in
  the Navigation menu to enable users to more easily locate
  specific pages by using keywords.

### Technology Preview

For the Red Hat Compatible Kernel in the current Oracle Linux 8 release, the following
features are under technology preview:

#### aarch64 only: VNC Remote Console

In this release, the Virtual Network Computing (VNC) remote
console is available as a technology preview on the 64-bit Arm
platform only. The remaining components of
the graphics stack are unverified on this platform.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.2/ol8-KnownIssues.html -->

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

#### Interactive text-based installation wizard unable to complete when an alternate language is selected

If an alternate language is selected during an interactive installation by using the
text-based installer, you cannot progress through all of the steps in the installation wizard.
The installation is blocked with [!] bullets for Software Selection and Installation
Destination, irrespective of what is selected for these two options.

Note that this issue does not occur when performing an installation by using the default
language selection of English or if you are using the graphical installer.

(Bug ID 30535416)

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

#### Syslog Error: Failed to insert module 'ip\_tables': Operation not permitted

During an Oracle Linux 8 installation, the following message can be observed
in the `/var/log/messages:systemd` log:

```
1]: Failed to insert module 'ip_tables': Operation not permitted
```

This error can be safely ignored, as the `ip_tables` kernel module
subsequently and can be verified by running the following command:

```
grep IPTABLES /boot/config*
```

The following output indicates the module loaded successfully:

```
CONFIG_IP_NF_IPTABLES=m
CONFIG_IP6_NF_IPTABLES=m
```

You can also check that the module loaded successfully by running the following command:

```
modinfo ip_tables
```

The output of the previous command indicates the module loaded successfully:

```
filename:      
/lib/modules/4.18.0-32.el8.x86_64/kernel/net/ipv4/netfilter/ip_tables.ko.xz
alias:          ipt_icmp
description:    IPv4 packet filter
author:         Netfilter Core Team <coreteam@netfilter.org>
license:        GPL
rhelversion:    8.0
srcversion:     3967C875058C2EE2475C9C2
depends:        
retpoline:      Y
intree:         Y
name:           ip_tables
vermagic:       4.18.0-32.el8.x86_64 SMP mod_unload modversions
sig_id:         PKCS#7
signer:        
sig_key:        
sig_hashalgo:   md4
signature:      30:82:02:59:06:09:2A:86:48:86:F7:0D:01:07:02:A0:82:02:4A:30:
82:02:46:02:01:01:31:0D:30:0B:06:09:60:86:48:01:65:03:04:02:
01:30:0B:06:09:2A:86:48:86:F7:0D:01:07:01:31:82:02:23:30:82:
02:1F:02:01:01:30:7A:30:62:31:22:30:20:06:03:55:04:0A:0C:19:
4F:72:61:63:6C:65:20:41:6D:65:72:69:63:61:2C:20:49:6E:63:2E:
2C:63:3D:55:53:31:19:30:17:06:03:55:04:03:0C:10:4F:72:61:63:
.
.
.
```

(Bug ID 29500599)

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

#### Installation on KVM guest by using iPXE and iSCSI boot results in incorrect IQN name

After installing Oracle
Linux 8 on a KVM guest by using iPXE and iSCSI boot, the SCSI Qualified Name (IQN) in the
`/etc/iscsi/initiatorname.iscsi` file is not correct.

Note that this incorrect configuration could impact
`kdump` functionality.

The workaround for this issue is to manually modify the
`/etc/iscsi/initiatorname.iscsi` file with
the correct IQN after the installation completes.

(Bug ID 29536715)

#### aarch64 only: Cannot boot from Oracle Linux 8 (aarch64) ISO when using certain devices

Attempts to boot the Oracle Linux 8 (aarch64) installer by using
the ISO might fail. If USB Attached SCSI devices are present, the boot process may drop to a
shell prompt. Examples of such devices include a virtual hard disk drive (HDD), a virtual
CD-ROM, and a memory stick.

You also might encounter an issue during an installation of
Oracle Linux 8 (aarch64), where USB ports are not recognized by the system right after the
kernel takes control of the system, as well as by the installed system. When this problem
occurs, any USB devices that are plugged into the system, such as keyboards and so on, do not
work. In addition, booting images from certain USB-connected drives, such as virtual devices
that are handled by a service processor, for example, MegaRAC SP firmware, does not work.

A workaround is to install an earlier Oracle Linux 8 (aarch64) release by using the ISO
image, and then use the `dnf update` command to update to the current
Oracle Linux 8 (aarch64) release.

Also, this issue does not affect a PXE boot, so as an alternative solution, you can perform
a network-based installation of Oracle Linux 8 (aarch64). See [Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/) for instructions on performing an installation from
the network.

(Bug IDs 31626109, 31678684)

#### aarch64 only: Cannot install Oracle Linux 8 on a host that has a disk with a Btrfs partition

For both GUI-based and text-based installations of Oracle
Linux 8 on the Arm platform, the following error is produced at the start of the installation:

```
** (anaconda:2843): CRITICAL **: 09:49:18.542: The function
'bd_btrfs_list_subvolumes' called, but not implemented!
```

This error prevents you from proceeding with the installation.

To work around this issue, before the installation, remove or format all of the Btrfs
partitions from all of the disks on the host where you are planning to install Oracle Linux 8.

(Bug ID 31160993)

### Running dnf update glusterfs-\* command fails to upgrade previously installed packages

If
`glusterfs-*.i686` packages exist on an Oracle Linux 8 system which you then
upgrade to the next update version, running the `dnf update glusterfs*` command
later fails to upgrade GlusterFS packages.

As a workaround, first remove the `glusterfs-*.i686` packages from
the system, and then run the `dnf update glusterfs*` command.

(Bug ID 30279840)

### Cockpit web console Services page unable to search services by state

The Services page for the Cockpit web console has been updated to
enable you to search services by name, description, and state. This new functionality works as
expected for filtering services by Name and Description; however, if you attempt to filter
services by State, an error indicating there are no matching results is produced.

(Bug ID 30286168)

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

#### Kdump runs out of memory when attempting to mount /sysroot on FC disks that use the Logical Volume Manager

An
issue in Oracle Linux 8 causes Kdump to run out of memory if you attempt to mount
`/sysroot` on a Fibre Channel (FC) disk that uses LVM. This issue is due to a
lack of memory when the `crashkernel` loads.

To resolve the issue, you can do one of the following:

- Override the `crashkernel=auto` boot
  option so that more memory is reserved for Kdump. For
  example, set the kernel boot parameter to
  `crashkernel=512M`.
- Set the Kdump destination to a network location (NFS or
  SSH).

(Bug ID 29840266)

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

#### aarch64 only: Kdump sometimes fails on ThunderX2 and X-Gene 3 platforms

System hangs might occur during a crash kernel boot on ThunderX2 and X-Gene 3 platforms that
are running Oracle Linux 8 (aarch64). This issue has been observed at different stages of the
boot process. Consequently, Kdump might not work as expected on this hardware.

(Bug IDs 30339519, 30339571)

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

### Networking Issues

The following are networking issues that might be encountered in this release of
Oracle Linux 8.

#### tracepath6 does not parse destination IPv6 address correctly

Running the `tracepath6` command fails to parse the destination IPv6 address
correctly. Consequently, the tool traces a route to the wrong host.

To work around this issue, use a tool with similar capabilities to the
`tracepath6` command.

(Bug ID 29540588)

#### Failure to insert ip\_tables module

The `ip_tables` module fails to insert with an 'Operation not
permitted' error. This issue, which is currently under investigation, can occur if SELinux is
in enforcing mode.

A workaround for this issue is to set SELinux to permissive mode, which you can do
temporarily by running the `setenforce 0` command. Or, you can set
SELinux to permissive mode permanently by editing the `/etc/selinux/config`
file and then rebooting the system.

(Bug ID 29517166)

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

### Podman Issues

For information about known issues with the Podman container management tool in Oracle Linux
8, refer to Known Issues chapter of the [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).

### TLS 1.3 not supported for NSS in FIPS Mode

TLS 1.3 is enabled by default in Oracle Linux 8. Applications that are
built with NSS do not support connections that require TLS 1.3
in FIPS mode. To make such connections work, disable FIPS mode
or use TLS 1.2.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.2/ol8.0-PackageChangesfromtheUpstreamRelease.html -->

The following sections list the changes to binary and source
packages from the upstream release.

### Changes to Binary Packages

This section contains information about the removed, modified, and
new binary packages in
this release. For information about the
source package changes,
see [Changes to Source Packages](ol8.0-PackageChangesfromtheUpstreamRelease.html#ol8-packages-source).

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
- `shim-ia32`
- `shim-x64`

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
- `bpftool`
- `chrony`
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
- `efi-rpm-macros`
- `firewalld`
- `fuse`
- `fwupd`
- `fwupdate`
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
- `gpgme`
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
- `grub2-ppc64le-modules`
- `grub2-tools`
- `grub2-tools-efi`
- `grub2-tools-extra`
- `grub2-tools-minimal`
- `grubby`
- `iproute`
- `iproute-tc`
- `iscsi-initiator-utils`
- `iscsi-initiator-utils-iscsiuio`
- `kernel`
- `kernel-abi-whitelists`
- `kernel-core`
- `kernel-cross-headers`
- `kernel-debug`
- `kernel-debug-core`
- `kernel-debug-devel`
- `kernel-debug-modules`
- `kernel-debug-modules-extra`
- `kernel-devel`
- `kernel-doc`
- `kernel-headers`
- `kernel-modules`
- `kernel-modules-extra`
- `kernel-tools`
- `kernel-tools-libs`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `kmod-libs`
- `ksc`
- `libasan`
- `libatomic`
- `libatomic-static`
- `libdnf`
- `libgcc`
- `libgfortran`
- `libgomp`
- `libgomp-offload-nvptx`
- `libipa_hbac`
- `libitm`
- `libkcapi`
- `libmicrohttpd`
- `libnsl`
- `libquadmath`
- `libreport`
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
- `mdadm`
- `mksh`
- `mozjs52`
- `nscd`
- `nss_db`
- `opa-address-resolution`
- `opa-basic-tools`
- `opa-fastfabric`
- `opa-ff`
- `opa-fm`
- `opa-libopamgt`
- `OpenIPMI`
- `openssl`
- `openssl-devel`
- `openssl-libs`
- `openssl-perl`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`
- `os-prober`
- `parted`
- `perf`
- `platform-python`
- `policycoreutils`
- `policycoreutils-dbus`
- `policycoreutils-devel`
- `policycoreutils-newrole`
- `policycoreutils-python-utils`
- `policycoreutils-restorecond`
- `polkit`
- `python3-boom`
- `python3-dnf-plugins-core`
- `python3-dnf-plugin-versionlock`
- `python3-hawkey`
- `python3-iscsi-initiator-utils`
- `python3-kmod`
- `python3-libdnf`
- `python3-libipa_hbac`
- `python3-libs`
- `python3-libsss_nss_idmap`
- `python3-perf`
- `python3-policycoreutils`
- `python3-sss`
- `python3-sssdconfig`
- `python3-sss-murmur`
- `python3-test`
- `python-configshell`
- `python-rtslib`
- `python-urllib3`
- `redhat-indexhtml`
- `redhat-release`
- `redhat-release-eula`
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
- `stunnel`
- `sudo`
- `systemd`
- `systemd-container`
- `systemd-devel`
- `systemd-journal-remote`
- `systemd-libs`
- `systemd-pam`
- `systemd-tests`
- `systemd-udev`
- `tuned`
- `tuned-profiles-atomic`
- `tuned-profiles-compat`
- `tuned-profiles-cpu-partitioning`
- `tuned-profiles-mssql`
- `tuned-profiles-oracle`
- `vim-minimal`
- `xfsprogs`
- `xfsprogs-devel`

#### Modified Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `crash`
- `cups-filters-devel`
- `dnf-plugin-spacewalk`
- `gcc-plugin-devel`
- `glibc-benchtests`
- `glibc-nss-devel`
- `glibc-static`
- `gpgme`
- `iproute`
- `kernel-tools-libs-devel`
- `kmod-devel`
- `libmicrohttpd-devel`
- `libmicrohttpd-doc`
- `libreoffice-sdk`
- `libreoffice-sdk-doc`
- `libstdc++-static`
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
- `libvirt-daemon-driver-secret`
- `libvirt-daemon-driver-storage`
- `libvirt-daemon-driver-storage-core`
- `libvirt-daemon-driver-storage-disk`
- `libvirt-daemon-driver-storage-gluster`
- `libvirt-daemon-driver-storage-iscsi`
- `libvirt-daemon-driver-storage-logical`
- `libvirt-daemon-driver-storage-mpath`
- `libvirt-daemon-driver-storage-rbd`
- `libvirt-daemon-driver-storage-scsi`
- `libvirt-devel`
- `libvirt-docs`
- `libvirt-libs`
- `libvirt-nss`
- `mingw32-binutils`
- `mingw32-cpp`
- `mingw32-gcc`
- `mingw32-gcc-c++`
- `mingw32-openssl`
- `mingw64-binutils`
- `mingw64-cpp`
- `mingw64-gcc`
- `mingw64-gcc-c++`
- `mingw64-openssl`
- `mingw-binutils-generic`
- `mozjs52`
- `mozjs60`
- `nss_hesiod`
- `nvml`
- `ocaml-libguestfs`
- `ocaml-libguestfs-devel`
- `OpenIPMI`
- `openscap-engine-sce-devel`
- `PackageKit-glib-devel`
- `parted`
- `python3-dnf-plugin-spacewalk`
- `python3-rhn-client-tools`
- `python3-rhnlib`
- `qemu-kvm`
- `rhn-client-tools`
- `rhnlib`
- `sanlock-devel`
- `shim-unsigned-x64`
- `sssd`
- `tog-pegasus`

#### Modified AppStream Binary Packages

The following binary packages from the AppStream upstream release have been modified:

- `abrt`
- `abrt-java-connector`
- `adwaita-gtk2-theme`
- `anaconda`
- `anaconda-core`
- `anaconda-dracut`
- `anaconda-gui`
- `anaconda-install-env-deps`
- `anaconda-tui`
- `anaconda-user-help`
- `anaconda-widgets`
- `ansible-freeipa`
- `aspnetcore-runtime`
- `aspnetcore-targeting-pack`
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
- `compat-libgfortran-48`
- `compat-libpthread-nonshared`
- `composer-cli`
- `containernetworking-plugins`
- `containers-common`
- `cpp`
- `crash`
- `cups-filters`
- `cups-filters-libs`
- `delve`
- `dnf-plugin-spacewalk`
- `dotnet`
- `dotnet-apphost-pack`
- `dotnet-host`
- `dotnet-hostfxr`
- `dotnet-runtime`
- `dotnet-sdk`
- `dotnet-targeting-pack`
- `dotnet-templates`
- `efi-rpm-macros`
- `firefox`
- `firewalld`
- `gcc`
- `gcc-c++`
- `gcc-gdb-plugin`
- `gcc-gfortran`
- `gcc-offload-nvptx`
- `gcc-toolset-9-gdb`
- `gcc-toolset-9-gdb-doc`
- `gcc-toolset-9-gdb-gdbserver`
- `gdb`
- `gdb-doc`
- `gdb-gdbserver`
- `gdb-headless`
- `git-clang-format`
- `glibc-utils`
- `gnome-abrt`
- `gnome-initial-setup`
- `gnome-themes-standard`
- `golang`
- `gpgme`
- `grafana-pcp`
- `httpd`
- `httpd-devel`
- `httpd-filesystem`
- `httpd-manual`
- `httpd-tools`
- `icedtea-web`
- `icedtea-web-javadoc`
- `initial-setup`
- `ipa-client`
- `ipa-client-common`
- `ipa-common`
- `ipa-python-compat`
- `ipa-server`
- `ipa-server-common`
- `ipa-server-dns`
- `ipa-server-trust-ad`
- `kernel-rpm-macros`
- `ksh`
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
- `libreoffice-gtk2`
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
- `libxml2`
- `libxslt`
- `lld`
- `llvm`
- `lorax`
- `lorax-composer`
- `lorax-lmc-novirt`
- `lorax-lmc-virt`
- `lorax-templates-generic`
- `lorax-templates-rhel`
- `lua-guestfs`
- `mecab-ipadic`
- `mod_ldap`
- `mod_md`
- `mod_proxy_html`
- `mod_session`
- `mod_ssl`
- `mozjs60`
- `netstandard-targeting-pack`
- `NetworkManager-libreswan`
- `NetworkManager-libreswan-gnome`
- `nginx`
- `nginx-all-modules`
- `nginx-filesystem`
- `nginx-mod-http-image-filter`
- `nginx-mod-http-perl`
- `nginx-mod-http-xslt-filter`
- `nginx-mod-mail`
- `nginx-mod-stream`
- `nmstate`
- `nvml`
- `openchange`
- `openscap`
- `openscap-devel`
- `openscap-engine-sce`
- `openscap-python3`
- `openscap-scanner`
- `openscap-utils`
- `open-vm-tools`
- `open-vm-tools-desktop`
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
- `pki-core`
- `platform-python`
- `platform-python-debug`
- `platform-python-devel`
- `plymouth`
- `podman`
- `podman-docker`
- `podman-manpages`
- `podman-remote`
- `podman-tests`
- `policycoreutils-gui`
- `policycoreutils-sandbox`
- `pykickstart`
- `pyparted`
- `python2`
- `python2-debug`
- `python2-devel`
- `python2-libs`
- `python2-test`
- `python2-tkinter`
- `python2-tools`
- `python3-blivet`
- `python3-clang`
- `python3-idle`
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-kickstart`
- `python3-libguestfs`
- `python3-libnmstate`
- `python3-spacewalk-backend-libs`
- `python3-systemd`
- `python3-test`
- `python3-tkinter`
- `python-blivet`
- `python-urllib3`
- `qemu-kvm`
- `rear`
- `redhat-lsb`
- `redhat-rpm-config`
- `rhn-client-tools`
- `rhn-custom-info`
- `rhnlib`
- `rhnpush`
- `rhnsd`
- `rpmdevtools`
- `rpm-ostree`
- `rpm-ostree-libs`
- `ruby`
- `ruby-devel`
- `ruby-doc`
- `rubygem-abrt`
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
- `spacewalk-abrt`
- `spacewalk-usix`
- `spice-streaming-agent`
- `thunderbird`
- `tog-pegasus`
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

#### Removed BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been removed:

- `dnf-plugin-subscription-manager`
- `grub2-ppc64le-modules`
- `kpatch`
- `python3-subscription-manager-rhsm`
- `python3-syspurpose`
- `redhat-logos`
- `redhat-logos-httpd`
- `redhat-release-eula`
- `rhsm-icons`
- `shim-ia32`
- `shim-x64`
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
- `subscription-manager-initial-setup-addon`
- `subscription-manager-migration`
- `subscription-manager-migration-data`
- `toolbox`
- `virtio-win`
- `virt-who`

#### Removed CodeReady Linux Builder Binary Packages

No binary packages were removed from CodeReady Linux Builder by Oracle.

### Changes to Source Packages

This section contains information about the removed, modified, and
new source packages in
this release. For information about the
binary package changes,
see [Changes to Binary Packages](ol8.0-PackageChangesfromtheUpstreamRelease.html#ol8-packages-binary).

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

No source packages were added to AppStream by Oracle.

#### Modified BaseOS Source Packages

The following source packages from the BaseOS upstream release have been modified:

- `autofs`
- `binutils`
- `boom-boot`
- `chrony`
- `compat-libgfortran-48`
- `coreutils`
- `dbus`
- `dracut`
- `efibootmgr`
- `efi-rpm-macros`
- `firewalld`
- `fuse`
- `fwupd`
- `fwupdate`
- `glibc`
- `gpgme`
- `grub2`
- `grubby`
- `initial-setup`
- `iproute`
- `iscsi-initiator-utils`
- `kernel`
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
- `lorax-templates-rhel`
- `mcelog`
- `mdadm`
- `mksh`
- `mozjs52`
- `opa-ff`
- `opa-fm`
- `OpenIPMI`
- `openscap`
- `openssl`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`
- `osinfo-db`
- `os-prober`
- `parted`
- `policycoreutils`
- `polkit`
- `pykickstart`
- `python3`
- `python-configshell`
- `python-rtslib`
- `python-urllib3`
- `redhat-indexhtml`
- `redhat-lsb`
- `redhat-release`
- `redhat-rpm-config`
- `rpmdevtools`
- `rpm-ostree`
- `selinux-policy`
- `sos`
- `sssd`
- `stunnel`
- `systemd`
- `tuned`

#### Modified AppStream Source Packages

The following source packages from the AppStream upstream release have been modified:

- `abrt`
- `abrt-java-connector`
- `anaconda`
- `anaconda-user-help`
- `buildah`
- `clang`
- `cloud-init`
- `compat-libgfortran-48`
- `containernetworking-plugins`
- `crash`
- `cups-filters`
- `delve`
- `dnf-plugin-spacewalk`
- `dotnet3.1`
- `efi-rpm-macros`
- `firefox`
- `firewalld`
- `gcc`
- `gcc-toolset-9-gdb`
- `gdb`
- `gnome-abrt`
- `gnome-initial-setup`
- `gnome-themes-standard`
- `golang`
- `gpgme`
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
- `lld`
- `llvm`
- `lorax`
- `lorax-templates-rhel`
- `mcelog`
- `mecab-ipadic`
- `mozjs60`
- `nginx`
- `nmstate`
- `nvml`
- `openchange`
- `openscap`
- `openssl`
- `open-vm-tools`
- `osinfo-db`
- `PackageKit`
- `perl-XML-Parser`
- `pesign`
- `pki-core`
- `plymouth`
- `podman`
- `pykickstart`
- `pyparted`
- `python2`
- `python-blivet`
- `python-urllib3`
- `qemu-kvm`
- `rear`
- `redhat-lsb`
- `redhat-rpm-config`
- `rhn-client-tools`
- `rhnlib`
- `rhnpush`
- `rhnsd`
- `rpmdevtools`
- `rpm-ostree`
- `rubygem-abrt`
- `sanlock`
- `scap-security-guide`
- `scap-workbench`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `skopeo`
- `sos-collector`
- `spacewalk-abrt`
- `spacewalk-usix`
- `spice-streaming-agent`
- `thunderbird`
- `tog-pegasus`
- `vim`
- `virt-manager`
- `virt-p2v`
- `WALinuxAgent`
- `wget`
- `xsane`

#### Modified Source Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `gpgme`
- `mozjs52`
- `mozjs60`
- `nvml`
- `OpenIPMI`
- `parted`
- `qemu-kvm`
- `shim-unsigned-x64`
- `tog-pegasus`

#### Removed BaseOS Source Packages

The following source packages from the BaseOS upstream release have been removed:

- `dnf-plugin-subscription-manager`
- `kpatch`
- `libcxl`
- `libica`
- `libical`
- `libocxl`
- `librtas`
- `libservicelog`
- `libvpd`
- `libzfcphbaapi`
- `lsvpd`
- `opal-prd`
- `openssl-ibmca`
- `powerpc-utils`
- `ppc64-diag`
- `python3-subscription-manager-rhsm`
- `qclib`
- `redhat-logos`
- `redhat-logos-httpd`
- `s390utils`
- `servicelog`
- `subscription-manager`
- `subscription-manager-cockpit`
- `subscription-manager-plugin-container`
- `subscription-manager-plugin-ostree`
- `subscription-manager-rhsm-certificates`

#### Removed AppStream Source Packages

The following source packages from the AppStream upstream release have been removed:

- `insights-client`
- `libical-devel`
- `redhat-logos-ipa`
- `redhat-support-lib-python`
- `redhat-support-tool`
- `SLOF`
- `subscription-manager-initial-setup-addon`
- `subscription-manager-migration`
- `subscription-manager-migration-data`
- `toolbox`
- `virtio-win`
- `virt-who`