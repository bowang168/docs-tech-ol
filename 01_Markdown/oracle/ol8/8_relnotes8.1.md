---
title: "Release Notes for Oracle Linux 8.1"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.1"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol8"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

Release Notes for Oracle Linux 8.1

F21672-11

September 2022

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 8 Release Notes for Oracle Linux 8.1

F21672-11

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2019, 2022, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.1/ol8.1-Preface.html -->

[Oracle Linux 8: Release Notes for Oracle Linux 8.1](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.1/) provides information about the new
features and known issues in the Oracle Linux 8.1 release. The information applies to
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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.1/ol8-AboutOracleLinux8.html -->

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

### Supported Architectures

The following architectures are supported in Oracle Linux 8:

- Intel `x86_64`
- AMD 64-bit

Note:

The 64-bit Arm (aarch64) platform can be installed as a
developer preview release in Oracle Linux 8. See
<unresolvable-reference.html#ol8-arm-only>.

### Shipped Kernel

The Oracle Linux 8.1 release ships with the
`kernel-4.18.0-147.el8` Red Hat Compatible Kernel
(RHCK) kernel package.

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

Note:

Oracle Linux 8 (aarch64) is available as a developer preview on Oracle Linux 8.0 and
Oracle Linux 8.1. The developer preview images for Oracle Linux 8 for the 64-bit Arm
(aarch64) platform are available at <https://www.oracle.com/linux/downloads/linux-beta8-downloads.html>.

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.1/ol8-NewFeaturesandChanges.html -->

This chapter describes the new features, major enhancements, bug fixes, and other changes
that are included in this release of Oracle Linux 8.

### Installation and Image Creation

Oracle Linux 8.1 introduces the following notable installation and image
creation features and improvements:

- Ability to disable modules during a kickstart installation

  You can now disable a module during a kickstart
  installation to prevent packages from that module from
  being installed. Use the following command to disable a
  module during a kickstart installation:

  ```
  sudo module --name=module-name --stream=stream-name--disable
  ```
- New `repo.git` blueprint section added to
  `lorax-composer`

  The new `repo.git` blueprint section
  enables you to include extra files in your image build.
  Note that the files must be hosted in a git repository
  that is accessible from the
  `lorax-composer` build server.
- Image builder includes image creation capability for more cloud
  providers

  Image Builder has been expanded in Oracle Linux 8.1 to include
  other cloud providers for which it can create an image.
  For example, you can now create and deploy images on
  Google Cloud and Alibaba Cloud, as well as run custom
  instances on these platforms.

### Red Hat Compatible Kernel

The following notable features, enhancements, and changes apply
to the Red Hat Compatible Kernel (RHCK) that is shipped with
Oracle Linux 8.1.

- Early Kdump

  The early Kdump feature enables the crash kernel and
  `initramfs` to load early so that
  `vmcore` can be captured early enough to
  also include information about early crashes. More details
  about `early kdump` can be found in the
  `/usr/share/doc/kexec-tools/early-kdump-howto.txt`
  file. See also Working With Kernel
  Dumps in
  [Oracle
  Linux 8: Monitoring and Tuning a
  System](https://docs.oracle.com/en/operating-systems/oracle-linux/8/monitoring/index.html).
- `ipcmni_extend` kernel command-line parameter added

  The new `ipcmni_extend` kernel
  command-line parameter extends a number of unique System V
  Inter-process Communication (IPC) identifiers from the
  current maximum of 32 KB (15 bits), up to 16 MB (24 bits).
  This enhancement enables users with applications that
  produce a large amount of shared memory segments to create
  a stronger IPC identifier, without exceeding the 32 KB
  limit.

  It should be noted that in some cases, use of the
  `ipcmni_extend` parameter can result in
  minor performance issues. You should therefore only use this
  parameter in situations where applications require more than
  32 KB of a unique IPC identifier.
- Persistent memory initialization code includes parallel initialization

  The inclusion of parallel initialization to the persistent
  memory initialization code greatly reduces the overall
  memory initialization time on systems that have large
  amounts of persistent memory. As a result, these systems
  boot much faster.
- Optane DC memory systems include capability for EDAC reports

  With this update, EDAC (Error Detection and Correction)
  properly reports memory corrected/uncorrected events with
  the accurate memory module information. Previously, EDAC
  did not properly report these events if the memory address
  was within a NVDIMM module.

  This update also includes the Memory Mode for Optane DC
  Persistent Memory technology.
- TPM tool updated to version 2.0

  The `tpm2-tools` user-space tool has been
  updated to version 2.0. This version of the Trusted
  Platform Module (TPM) tool provides fixes for several
  defects.
- `UBSan`  utility enabled in the debug kernel

  The Undefined Behavior Sanitizer
  (`UBSan`) utility has been enabled in the
  debug kernel to enable the system to more easily detect
  certain types of bugs that previously went undetected; for
  example, in the case of compiler optimization, where
  subtle, obscure bugs might appear.
- `bpftrace` language added

  Oracle Linux 8.1 includes the `bpftrace` language,
  a high-level tracing language for extended Berkeley Packet
  Filter (eBPF) that is used for very specific tracing
  tasks. A significant benefit of using
  `bpftrace` is that you can accomplish the
  same outcome with one line in `bpftrace`,
  as compared to an entire page of code that mixes the
  Python and C languages in the BPF Compiler Collection
  (BCC) library.
- `kernel-rt` source tree matches latest Oracle Linux tree

  Sources for the `kernel-rt` source tree have
  been upgraded so that they are based on the latest RHCK
  kernel source tree. This change provides a number of bug
  fixes and enhancements over the previous version.
- `ssdd` test added for Real Time 8

  This update includes the `ssdd` test for
  Real Time 8, which is used for stress testing of the
  tracing subsystem. The test runs multiple tracing threads
  to verify that locking is correct within the tracing
  system.

### Corosync and Pacemaker Included in Oracle Linux 8.1.

The Corosync version 3.0.2 and Pacemaker version 2.0.2 software
packages are included in Oracle Linux 8.1. This software is used for
clustering and high availability.

### Cockpit Web Console

In Oracle Linux 8.1, the following features, enhancements, and changes
for the Cockpit web console are introduced:

- Capability for SMT configuration by using the Cockpit web console

  Oracle Linux 8.1 includes capability for Simultaneous
  Multi-Threading (SMT) configuration, which also includes
  the ability to disable SMT in the Cockpit web console.
  This added capability enables you to mitigate a class of
  CPU security vulnerabilities, such as Microarchitectural
  Data Sampling and L1 Terminal Fault Attack.

  Note:

  When SMT is disabled on the system, options for SMT are
  not displayed in the Cockpit web console. See
  [Oracle® Linux: Simultaneous Multithreading Notice](https://docs.oracle.com/en/operating-systems/oracle-linux/notice-smt/) for more details.
- Services page improvements

  To improve the user experience in this update, the web
  console's Services page has been updated to include a
  search box that enables you to search services by name and
  description. Other improvements include the following:
  service states have been merged into one list, and the
  switcher buttons that were located at the top of the page
  have been replaced with tabs.
- Networking page updated with new firewall settings

  Additional firewall settings have been added to the web
  console's Networking page, including capability for the
  following: adding and removing zones, adding and removing
  services to arbitrary zones, and custom port configuration
  for the `firewalld` services.
- Improvements to Virtual Machines page

  Several improvements have been made to the web console's
  Virtual Machines page. For example, in this update, you
  can do the following:

  - Manage various types of storage pools.
  - Configure autostart for a virtual machine (VM).
  - Import existing `qcow` images.
  - Install VMs by using PXE boot.
  - Change a VM's memory allocation.
  - Pause and resume a VM.
  - Configure cache characteristics.
  - Change the boot order for a VM.

### Compilers and Developer Tools

Oracle Linux 8.1 introduces the following feature enhancements and
changes for compilers and developer tools.

#### GCC Toolset 9

Oracle Linux 8.1 introduces the GCC Toolset 9, which is an Application
Stream that is distributed in the form of a Software
Collection in the `appstream_beta`
repository. The GCC Toolset is similar to the Oracle Linux Developer
Toolset.

The GCC Toolset 9 contains up-to-date versions of the
following developer tools:

- GCC version 9.1.1
- GDB version 8.3
- Valgrind version 3.15.0
- SystemTap version 4.1
- Dyninst version 10.1.0
- `binutils` version 2.32
- `elfutils` version 0.176
- `dwz` version 0.12
- `make` version 4.2.1
- `strace` version 5.1
- `ltrace`version 0.7.91

To install the toolset, use the following command:

```
sudo dnf install gcc-toolset-9
```

You can run a tool from GCC Toolset 9 by using the following
command:

```
scl enable gcc-toolset-9 tool
```

Use the following command to run a shell session, where tool
versions from the GCC Toolset 9 take precedence over system
versions of the same tools:

```
scl enable gcc-toolset-9 bash
```

#### Compiler Toolsets Updated

The following compiler toolsets have been updated. These
toolsets are distributed as Application Streams in Oracle Linux 8.1:

- Clang and LLVM toolset upgraded to version 8.0.0

  This toolset provides the LLVM compiler infrastructure
  framework, the Clang compiler for the C and C++
  languages, the LLDB debugger, and related tools for code
  analysis, to version 8.0.0
- Rust toolset upgraded to version 1.35

  This toolset provides the Rust programming language
  compiler (`rustc`), the
  `cargo` build tool and dependency
  manager, and any required libraries.
- Go toolset upgraded to version 1.12.6

  This toolset provides the Go (`golang`)
  programming language tools and libraries.

#### SystemTap Updated to Version 4.1

The SystemTap instrumentation tool has been updated to
upstream version 4.1 in this update. This version of SystemTab
provides several improvements over the previous version of the
tool, including the following:

- The eBPF runtime backend can now handle more features of
  the scripting language, such as string variables and rich
  formatted printing.
- Translator performance improvements.
- More types of data in optimized C code can be extracted by
  using DWARF4 debuginfo constructs.

#### elfutils Updated to Version 0.176

The `elfutils` packages have been updated to
version 0.176 in this update. This version of
`elfutils` provides numerous bug fixes and
resolves the following vulnerabilities:

- CVE-2019-7146
- CVE-2019-7149
- CVE-2019-7150
- CVE-2019-7664
- CVE-2019-7665

#### Date Formatting for Japanese Reiwa Era Updated

In Oracle Linux 8.1, the GNU C Library has been updated to include
correct Japanese era name formatting for the Reiwa era
(effective May 1st, 2019). Also, the time-handling API data,
which includes the data that is used by the
`strftime` and `strptime`
functions, has been updated. As a result, all APIs now
correctly print the Reiwa era, including when
`strftime` is used with one of the era
conversion specifiers, such as `%EC`,
`%EY`, or `%Ey`.

### Database

This release of Oracle Linux 8 ships with version 8.0 of the MySQL database software.

### File Systems and Storage

Oracle Linux 8.1 introduces the following notable file systems and
storage features, enhancements, and changes:

- Btrfs file system removed from RHCK

  The Btrfs file system is removed from RHCK in Oracle Linux 8. As
  such, you cannot create or mount Btrfs file systems when
  using this kernel. Also, any Btrfs user-space packages
  that are provided are not supported with RHCK.
- OCFS2 file system removed from RHCK

  The Oracle Cluster File System version 2 (OCFS2) file
  system is removed from RHCK in Oracle Linux 8. As such, you cannot
  create or mount OCFS2 file systems when using this kernel.
  Also, any OCFS2 user-space packages that are provided are
  not supported with RHCK.
- Data Integrity Field/Data Integrity Extension available in Oracle Linux 8.1

  The Data Integrity Field/Data Integrity Extension
  (DIF/DIX) feature is available on configurations where the
  hardware vendor has qualified the configuration and which
  includes that host bus adapter (HBA) and storage array
  configuration. The DIF/DIX feature is enabled and disabled
  on the storage device. The method that is used to activate
  the feature on storage devices is device-dependent.

  Note:

  DIF/DIX is not available for use on the boot device or on
  virtualized guests. Using the Automatic Storage Management
  library (ASMLib) when DIF/DIX is enabled is also not
  supported.
- VDO Ansible module moved to Ansible packages

  In this update, the VDO Ansible module is provided by the
  `ansible` package and is located in
  `/usr/lib/python3.6/site-packages/ansible/modules/system/vdo.py`.
  In previous updates, the module was provided by the
  `vdo` RPM package and was located in
  `/usr/share/doc/vdo/examples/ansible/vdo.py`.

  Note that the `vdo` package continues to
  distribute the Ansible playbook.
- Aero adapters

  The following two Aero adapters are included in Oracle Linux 8.1:

  - PCI ID `0x1000:0x00e2` and
    `0x1000:0x00e6`. These adapters are
    controlled by the `mpt3sas` driver.
  - PCI ID `0x1000:Ox10e5` and
    `0x1000:0x10e6`. These adapters are
    controlled by the `megaraid_sas`
    driver.

  Previously, these adapters were available as a Technology
  Preview only.

### Infrastructure Services

Oracle Linux 8.1 introduces the following infrastructure services
features, enhancements, and changes:

- Chrony updated to version 3.5

  The `chrony` packages have been updated
  to version 3.5. This version of Chrony provides several
  bug fixes and enhancements over the previous version. Some
  of the more notable changes include the following:

  - More accurate synchronization of the system clock with
    hardware timestamping in the kernel.
  - Important improvements to hardware timestamping.
  - The range of available polling intervals has been
    extended.
  - NTP sources include a filter option.
- Tuned updated to version 2.12

  The `tuned` packages are updated to
  version 2.12 in this update. This version of Tuned
  provides several bug fixes and enhancements over the
  previous version. Some of the more notable changes include
  the following:

  - An issue related to the handling of removed and
    re-attached devices has been fixed.
  - Negation of a CPU list has been added.
  - The `sysctl` tool is replaced by a new
    implementation that is specific to Tuned. This change
    improves the performance of the run-time kernel
    parameter.

### Memory Mode Technology for Intel Optane DC Persistent Memory Feature Added

Memory Mode for the Intel Optane DC Persistent Memory technology
has been added in Oracle Linux 8.1. This technology is transparent to the
operating system and does not require any special drivers or
specific certification.

### Networking

This release of Oracle Linux 8 introduces the following features, enhancements, and
improvements.

#### PMTU Discovery and Route Redirection for VXLANs and GENEVE Tunnels Added

In this update, the kernel can handle Internet Control Message
Protocol (ICMP) "Destination Unreachable" and "Redirect
Message" errors. The kernel can also handle ICMPv6 "Packet Too
Big" and "Destination Unreachable" messages for Virtual
Extensible LAN (VXLAN) and Generic Network Virtualization
Encapsulation (GENEVE) tunnels, which is done by adjusting the
PMTU and modifying forwarding information. As a result, PMTU
discovery and route redirection features are now provided for
VXLAN and GENEVE tunnels.

#### XDP and Networking eBPF Features Updated to Version 5.0

As of this update, the XDP and the networking eBPF features in
the `kernel` package have been updated to
version 5.0. This feature version provides a number of bug
fixes and enhancements over the previous version, including
the following: improvements to BPF programs for better
interaction with the TCP/IP stack, flow dissection, a wider
range of `bpf` helpers, and access to new map
types. XDP changes include the availability of XDP metadata to
`AF_XDP sockets`.

### Security

Oracle Linux 8.1 introduces the following security features,
enhancements, and changes.

#### SELinux Features

Oracle Linux 8.1 introduces the following features, changes, and
improvements for SELinux:

- SELinux user-space tools updated to version 2.9

  The following SELinux user-space tools have been updated
  to version 2.9: `libsepol`,
  `libselinux`,
  `libsemanage`,
  `policycoreutils`,
  `checkpolicy`, and
  `mcstrans`. This version of the SELinux
  user-space tools provides several bug fixes and
  enhancements over the previous version.
- SETools updated to version 4.2.2

  As of this update, the SETools collection and libraries
  have been updated to version 4.2.2. This version of the
  tools include several improvements over the previous
  version, including the removal of source policy
  references from manual pages (loading of source policies
  is no longer supported) and a fix for a performance
  regression in alias loading.
- `bpf` SELinux policy class added

  The new `bpf` SELinux policy class is
  introduced in this update. This class enables you to
  control the Berkeley Packet Filter (BPF) flow through
  SElinux and also enables the inspection and simple
  manipulation of Extended Berkeley Packet Filter (eBPF)
  programs and maps that are controlled by SELinux.
- `boltd_t` SELinux type added

  The new `boltd_t` SELinux type confines
  the `boltd` system daemon that is used
  to manage Thunderbolt 3 devices. The
  `boltd` daemon now runs as a confined
  service in SELinux enforcing mode.
- `selinux-policy` packages updated to version 3.14.3

  The `selinux-policy` package is updated
  to version 3.14.3 in this update. This version of the
  package provides a number of bug fixes and enhancements
  over the previous version, including the allowance of
  additional rules.
- "SELinux: Class not defined in policy" errors no longer displayed on
  system boot.

  An issue in Oracle Linux 8 that produced errors similar to the
  following in the `/var/log/messages`
  file when booting in either SELinux permissive mode or
  enforcing mode has been resolved:

  ```
  SELinux:  Class bpf not defined in policy.
  SELinux:  Class xdp_socket not defined in policy.
  SELinux: the above unknown classes and permissions will be allowed
  ```

#### OpenScap Features

Oracle Linux 8.1 introduces the following features, changes, and
improvements for OpenScap.

- OpenSCAP updated to version 1.3.1

  In Oracle Linux 8.1, the `openscap` packages
  have been updated to version 1.3.1. This version of
  OpenSCAP provides many bug fixes and enhancements over
  the previous version.
- OpenSCAP includes SCAP version 1.3

  Oracle Linux 8.1 includes the OpenSCAP suite, which supports data
  streams that conform to the latest version of the SCAP
  standard (SCAP 1.3). You can use SCAP 1.3 data streams
  the same way that you use SCAP 1.2 data streams, with no
  additional usability restrictions.
- `scap-security-guide` packages updated to version
  0.1.44

  The `scap-security-guide` packages have
  been updated to version 0.1.44 in this update. This
  version of the packages provides several bug fixes and
  enhancements over the previous version. Most notably, \*
  SCAP content conforms to the latest version of the SCAP
  standard, and SCAP 1.3 \* SCAP content supports UBI
  images.

#### SSH Features

The following new OpenSSH and SSH features, enhancements, and
changes are included in Oracle Linux 8.1:

- OpenSSH updated to version 8.0p1

  In Oracle Linux 8.1, the `openssh` packages have
  been updated to version 8.0p1. This version of OpenSSH
  provides several bug fixes and enhancements over the
  previous version, including the following:

  - Default RSA key size increased to 3072 bits for the
    `ssh-keygen` tool
  - Support for the `ShowPatchLevel`
    configuration option has been removed.
  - Numerous GSSAPI key exchange code fixes applied,
    including a fix for some Kerberos clean-up tasks.
  - Fall back to the `sshd_net_t` SELinux
    context has been removed.
  - `Match final` blocks added.
  - Minor issues with the `ssh-copy-id`
    command have been fixed.
  - Fixes for several Common Vulnerabilities and Exposures
    (CVE) related to the `scp` utility,
    namely the following: CVE-2019-6111, CVE-2018-20685,
    and CVE-2019-6109.
- `libssh` complies with the system-wide crypto-policies

  In Oracle Linux 8.1, the `libssh` client and
  server now automatically load the
  `/etc/libssh/libssh_client.config` and
  `/etc/libssh/libssh_server.config`
  files, respectively. With the automatic loading of the
  configuration file, `libssh` can use
  the system-wide cryptographic settings that are set by
  `crypto-policies`. This change
  simplifies control over the set of cryptographic
  algorithms that are used by applications.

#### New udica Package

Udica is a tool for generating SELinux policies for
containers. You can use Udica to create a tailored security
policy, which provides better control of how a container
accesses host system resources. This capability enables you to
harden container deployments against security violations,
while simplifying and maintaining regulatory compliance.

### virt-manager Application Deprecated

The Virtual Machine Manager application
(`virt-manager`) is deprecated in Oracle Linux 8.1.
Oracle recommends that you use the Cockpit web console to manage
virtualization in a GUI. Note that some features in Oracle Linux 8 might
only be accessible by using either
`virt-manager` or the command line.

### Technology Preview

For the Red Hat Compatible Kernel in the current Oracle Linux release, the following
features are under technology preview:

#### aarch64 only: VNC Remote Console

In this release, the Virtual Network Computing (VNC) remote
console is available as a technology preview on the 64-bit Arm
platform only. The remaining components of
the graphics stack are unverified on this platform.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.1/ol8-KnownIssues.html -->

This chapter lists known issues in the current Oracle Linux 8 release. The list covers issues
that might affect both x86 and aarch64 platforms. In the list, additional issues that are
specific only to aarch64 platforms are labeled `aarch64 only:`.

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

#### rhnreg\_ks register command might fail if python3-rhn-virtualization-host package is installed

Beginning with Oracle Linux 8.1, using the
`rhnreg_ks` command to register a system with the Unbreakable Linux Network
(ULN)might fail if the `python3-rhn-virtualization-hosts` package is installed
on the system. This issue has been observed when the `libvirtd` service is not
running.

To work around this issue, ensure that the `libvirtd` packages are installed
on your system and that the service is enabled and running prior to issuing the
`rhnreg_ks` command.

(Bug ID 30366521)

#### ULN registration wizard not displayed on first boot after an installation

On new installations of Oracle Linux 8, the ULN registration
wizard that presents the options to register with ULN and to use Oracle Ksplice is not
displayed on first boot.

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

To successfully install Oracle Linux 8 on an Oracle VM
VirtualBox guest, where the graphical installation program is used and the default
`Server with GUI` environment is selected, you must set the guest to use the
VMSVGA graphics controller and configure the guest with at least 64MB of memory. Otherwise,
the graphical display is unable to start correctly.

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

### Running dnf update glusterfs-\* command fails to upgrade previously installed packages

If `glusterfs-*.i686` packages exist
on an Oracle Linux 8 system which you then upgrade to the next update version, running the
`dnf update glusterfs*` command later fails to upgrade GlusterFS
packages.

As a workaround, first remove the `glusterfs-*.i686` packages from
the system, and then run the `dnf update glusterfs*` command.

(Bug ID 30279840)

### Cockpit web console Services page unable to search services by state

The Services page for the Cockpit web console has been updated to
enable you to search services by name, description, and state. This new functionality works as
expected for filtering services by Name and Description; however, if you attempt to filter
services by State, an error indicating there are no matching results is produced.

(Bug ID 30286168)

### libstorage package conflict causes dnf groupinstall command to fail

Running the `dnf groupinstall` command can
cause an installation to fail. This issue is due to a conflict
with a core dependency package
(`libstoragemgmt`), where a conflict exists
between i686 and `x86_64` packages.

As a workaround, specify the `--nobest` option
when running the `dnf groupinstall` command,
which allows you to install packages for either build
architecture and thus avoid this conflict, for example:

```
sudo dnf groupinstall "Server with GUI" --nobest
sudo dnf group update "Server with GUI"
```

(Bug ID 30882591)

### Oracle Linux 8 does not recognize SAS controllers on older Oracle Sun hardware

The Oracle Linux 8 installer does not recognize some Serial Attached SCSI (SAS) controllers
that are found in older Oracle Sun server models. If you attempt to install Oracle Linux 8 on
these server models, the installer does not recognize the local disk and the installation
fails. Examples of these server models include, but are not limited to, the following: Oracle
Sun Fire X4170 M2 Server, Oracle Sun Fire X4170 M3 Server, Oracle Sun OVCA X3-2 Server, and
the Oracle Sun X4-2 Server.

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

A bug in the Oracle Linux 8 code causes Retropline support to not be
displayed in the output of the `modinfo -F
retpoline` command, even though the
`CONFIG_RETPOLINE` flag is set to
`Y`, for example:

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

#### aarch64 only: Kdump sometimes fails on ThunderX2 and X-Gene 3 platforms

System hangs might occur during a crash kernel boot on ThunderX2 and X-Gene 3 platforms that
are running Oracle Linux 8 (aarch64). This issue has been observed at different stages of the
boot process. Consequently, Kdump might not work as expected on this hardware.

(Bug IDs 30339519, 30339571)

#### aarch64 only: Excessive write activity inside a guest can crash the guest kernel

In an environment where a guest system is performing excessive
write activity to `/dev/stdout`, subsequent
repeated suspend and resume operations on the same guest can
cause the guest kernel to crash. Furthermore, the guest kernel
can also crash when reverts from a snapshot state that had
excessive write activity on `/dev/stdout` to
an idle snapshot state occur.

This issue is related to a patch that is present in the guest
kernel for the 64-bit Arm platform and is currently under
investigation. A fix is likely to be provided in a subsequent
errata release.

(Bug ID 30423465)

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

The following are known issues for the Podman container
management tool in this release of Oracle Linux 8.

#### Executing podman attach --latest causes panic if no containers are available

If you execute `podman attach --latest` and
no containers exist in your environment, a runtime error
occurs:

```
panic: runtime error: index out of range
...
```

Note that this error no longer occurs as soon as there are
containers in the environment. Running the command when there
are no containers is meaningless.

(Bug ID 29882537)

#### Requirements for using the default podman detach key sequence

The default key sequence that you use to detach a container
(`CTRL+P`, `CTRL+Q`)
requires a console that can handle detachment
(`pseudo-tty`), as well as an input channel
for passing control signals (`stdin`).
Otherwise, you cannot create a container, attach it with the
`podman attach -l` command, and then quit or
detach the container by using the default key sequence, as
documented in the `podman-attach(1)` manual

page.

To ensure that you can use the default
`CTRL+P`, `CTRL+Q` key
sequence to detach a container, use either of the following
methods to create a container:

- Create a container in the background:

  ```
  podman run --rm -t -d container-registry.oracle.com/os/oraclelinux:7 top -b
  ```

  You can then use the `podman attach -l`
  command to attach the container and the
  `CTRL+P`, `CTRL+Q` key
  sequence to detach the container.
- Create a container interactively:

  ```
  podman run --rm -t -i container-registry.oracle.com/os/oraclelinux:7 top -b
  ```

  The interactive method creates the container and
  automatically attaches it. You can then use the
  `CTRL+P`, `CTRL+Q` key
  sequence to detach the container.

  For more information, see the `podman(1)`
  and `podman-attach(1)` manual pages.

(Bug ID 29882852)

#### Authentication error displayed when attempting to pull an image and not specifying its correct name

If you attempt to pull an image by running the `podman
pull`
image-name command,
but you do not specify the correct or full name of the image,
an authentication error occurs.

For example, the following error is displayed because
`oracle:latest` was specified as the name of
the image instead of `oraclelinux:latest`,
which is the correct name for the image:

```
Trying to pull registry.redhat.io/oracle:latest...Failed
Trying to pull quay.io/oracle:latest...Failed
Trying to pull docker.io/oracle:latest...Failed
error pulling image "oracle:latest": unable to pull oracle:latest: 3 errors
occurred:

* Error determining manifest MIME type for
docker://registry.redhat.io/oracle:latest: unable to retrieve auth token:
invalid username/password
* Error determining manifest MIME type for docker://quay.io/oracle:latest:
Error reading manifest latest in quay.io/oracle: error parsing HTTP 404
response body: invalid character '<' looking for beginning of value:
"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\">\n<title>404 Not
Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the
server.  If you entered the URL manually please check your spelling and try
again.</p>\n"
* Error determining manifest MIME type for docker://oracle:latest: Error
reading manifest latest in docker.io/library/oracle: errors:
denied: requested access to the resource is denied
unauthorized: authentication required
```

To prevent this error from occurring, always specify the
correct image name with the `podman pull`
command.

(Bug ID 29894231)

#### Oracle Container Registry unable to service requests to search catalog

Attempts to search for an image in the Oracle Container
Registry by using the `podman search` command
fail with an authorization error, even if you are logged into
the registry:

```
ERRO[0001] error getting search results from v2 endpoint
"container-registry.oracle.com", status code 401 (Unauthorized)
...
```

The issue is related to how Oracle Container Registry handles
token requests for access to "/v2/\_catalog". The
`podman search` command only requests a token
for ping-level access and not for catalog access.

There is currently no workaround for this issue.

(Bug ID 29942671)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.1/ol8.0-PackageChangesfromtheUpstreamRelease.html -->

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

- `oraclelinux-release-el8`
- `oraclelinux-release`
- `oracle-backgrounds`
- `oracle-logos`
- `oracle-logos-httpd`
- `oracle-logos-ipa`
- `shim-ia32`
- `shim-x64`

#### Added Binary Packages for AppStream by Oracle:

No binary packages were added to AppStream by Oracle.

#### Added Binary Packages for CodeReady Linux Builder by Oracle

No binary packages were added to CodeReady Linux Builder by Oracle.

#### Modified BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been modified:

- `python3-dnf-plugin-versionlock`
- `sudo`
- `python3-dnf-plugins-core`
- `dnf-plugins-core`
- `autofs`
- `binutils`
- `boom-boot`
- `boom-boot-conf`
- `boom-boot-grub2`
- `bpftool`
- `chrony`
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
- `libitm`
- `libkcapi`
- `libmicrohttpd`
- `libnsl`
- `libquadmath`
- `libreport`
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
- `python3-hawkey`
- `python3-iscsi-initiator-utils`
- `python3-kmod`
- `python3-libdnf`
- `python3-libs`
- `python3-perf`
- `python3-policycoreutils`
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
- `stunnel`
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
- `xfsprogs`
- `xfsprogs-devel`

#### Modified Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `cups-filters-devel`
- `dnf-plugin-spacewalk`
- `gcc-plugin-devel`
- `glibc-benchtests`
- `glibc-nss-devel`
- `glibc-static`
- `gpgme`
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
- `tog-pegasus`

#### Modified AppStream Binary Packages

The following binary packages from the AppStream upstream release have been modified:

- `abrt`
- `abrt-java-connector`
- `anaconda`
- `anaconda-core`
- `anaconda-dracut`
- `anaconda-gui`
- `anaconda-install-env-deps`
- `anaconda-tui`
- `anaconda-user-help`
- `anaconda-widgets`
- `ansible-freeipa`
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
- `cups-filters`
- `cups-filters-libs`
- `dnf-plugin-spacewalk`
- `efi-rpm-macros`
- `firefox`
- `firewalld`
- `gcc`
- `gcc-c++`
- `gcc-gdb-plugin`
- `gcc-gfortran`
- `gcc-offload-nvptx`
- `git-clang-format`
- `glibc-utils`
- `gnome-abrt`
- `gnome-initial-setup`
- `gnome-settings-daemon`
- `golang`
- `gpgme`
- `httpd`
- `httpd-devel`
- `httpd-filesystem`
- `httpd-manual`
- `httpd-tools`
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
- `nvml`
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
- `ruby-libs`
- `rubygem-abrt`
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
- `spacewalk-abrt`
- `spacewalk-usix`
- `thunderbird`
- `tog-pegasus`
- `tuned-gtk`
- `tuned-utils`
- `tuned-utils-systemtap`
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
- `kpatch`
- `libcxl`
- `libica`
- `libocxl`
- `libreport-plugin-rhtsupport`
- `libreport-rhel`
- `libreport-rhel-anaconda-bugzilla`
- `libreport-rhel-bugzilla`
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
- `python3-syspurpose`
- `qclib`
- `redhat-backgrounds`
- `redhat-logos`
- `redhat-logos-httpd`
- `redhat-logos-ipa`
- `redhat-support-lib-python`
- `redhat-support-tool`
- `s390utils`
- `servicelog`
- `shim-ia32`
- `shim-x64`
- `subscription-manager`
- `subscription-manager-cockpit`
- `subscription-manager-initial-setup-addon`
- `subscription-manager-migration`
- `subscription-manager-migration-data`
- `subscription-manager-plugin-container`
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
- `redhat-logos-httpd`
- `redhat-logos-ipa`
- `redhat-support-lib-python`
- `redhat-support-tool`
- `rhsm-gtk`
- `SLOF`
- `subscription-manager-initial-setup-addon`
- `subscription-manager-migration`
- `subscription-manager-migration-data`
- `subscription-manager-plugin-ostree`
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
- `cups-filters`
- `dnf-plugin-spacewalk`
- `efi-rpm-macros`
- `firefox`
- `firewalld`
- `gcc`
- `gnome-abrt`
- `gnome-initial-setup`
- `gnome-settings-daemon`
- `golang`
- `gpgme`
- `httpd`
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
- `nvml`
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
- `spacewalk-abrt`
- `spacewalk-usix`
- `thunderbird`
- `tog-pegasus`
- `virt-manager`
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
- `texlive-etoolbox`
- `toolbox`
- `virtio-win`
- `virt-who`