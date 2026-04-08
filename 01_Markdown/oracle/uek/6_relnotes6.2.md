---
title: "Unbreakable Enterprise Kernel Release 6 Update 2: Release Notes (5.4.17-2102)"
source_url: "https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.2"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "uek"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

Release Notes for Unbreakable Enterprise Kernel Release 6 Update 2

F38480-09

September 2024

---

[Title and Copyright Information](#copyright-information)

Unbreakable Enterprise Kernel Release Notes for Unbreakable Enterprise Kernel Release 6 Update 2

F38480-09

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2021, 2024, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.2/uek6.2-Preface.html -->

[Unbreakable Enterprise Kernel Release 6 Update 2:
Release Notes (5.4.17-2102)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.2/) provides a summary of the new features, changes, and
known issues in the Unbreakable Enterprise Kernel Release 6 Update 2.

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
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.2/uek6.2-NewFeaturesandChanges.html -->

Unbreakable Enterprise Kernel Release 6 (UEK R6) is a heavily tested and optimized operating
system kernel for Oracle Linux 7.7 and later and for Oracle Linux 8.1 and later.
The kernel is developed, built, and tested on the 64-bit Arm
(aarch64), Intel x86, and AMD x86 (x86\_64) platforms. The kernel
is based on the mainline Linux kernel version 5.4.
This release also updates drivers and includes bug and security
fixes.

Oracle actively monitors upstream check-ins and applies critical
bug and security fixes to UEK R6.

UEK R6U2 uses the 5.4.17-2102 version and build of the UEK R6
kernel, which includes security and bug fixes, as well as driver
updates.

UEK R6 uses the same versioning model as the mainline Linux
kernel version. It is possible that some applications might not
understand the 5.4 versioning scheme. However,
regular Linux applications are usually neither aware of nor
affected by Linux kernel version numbers.

UEK R6 maintains compatibility with the Red Hat Compatible
Kernel (RHCK) and does not disable any features that are enabled
in RHCK. Additional features are enabled to provide support for
key functional requirements and patches are applied to improve
performance and optimize the kernel for use on Oracle operating
environments.

The kernel's source code is available through a public git
source code repository at
<https://github.com/oracle/linux-uek>.

### Notable Features and Changes

The following are the major, new features of Unbreakable Enterprise Kernel Release 6 Update 2
(UEK R6U2).

#### Core Kernel Functionality

UEK R6U2 provides equivalent core kernel functionality to
UEK R6, but is updated to the upstream mainline kernel
v5.4.83 release tag and includes upstream LTS bug fixes, with
additional patches to enhance existing functionality and
provide some minor bug fixes and security improvements. Key
changes are specific to functionality that is required for
Oracle Database and other Oracle software.

#### New Slab Memory Controller

This update introduces a new slab memory controller for the
Linux kernel. The new slab memory controller specifically
addresses the low slab utilization issue that existed in the
previous design. Previously, slab allocator internals were
replicated for each memory cgroup and slab caches that were
used by one memory cgroup were dynamically created and
destroyed and could not be shared by other memory cgroups.

The new slab memory controller moves slab accounting from the
page level to the object level, thus enabling all memory
cgroups to use and share a single set of slab caches,
globally. This improvement is particularly beneficial for
systems with a large number of memory cgroups. Note that
upstream reports have indicated a 50% savings in slab memory
usage, per the implementation of this feature.

#### vDPA driver support for Mellanox ConnectX-6 Dx devices added

Support for the vHost Data Path Acceleration (vDPA) framework,
as well as Mellanox CX6-DX VDPA driver, has been added in this
update. When utilized on a host, this feature provides for
high-performance, Virtual I/O Device (VirtIO) acceleration.
This functionality is implemented by the device's hardware,
while preserving the ability to use standard VirtIO drivers on
the virtual machines (VMs) that are running on the host.

#### NVMe improvements and changes

This update provides fixes for most of the bugs that were
present in the 5.9 kernel. Other notable NVMe improvements and
changes that are introduced include the following:

- nvmet: ctrl model and ctrl-id is configurable through subsys attribute

  This change adds a new target `subsys`
  attribute that enables you to optionally specify a model
  name and a `ctrl-did`, which then is
  used in the
  `nvmet_execute_identify_ctrl()`
  function to complete the `nvme_id_ctrl`
  structure.
- nvme: hostid and hostnqn exposed through sysfs for fabrics controllers

  This change enables user space to connect with a custom
  `hostid` and
  `hostnqn`, which can be useful in
  certain cases. Note, however, that there is no way to
  determine what `hostid` is used to
  connect to a given controller.
- nvme-fc/nvmet-fc: FC-NVME-2 disconnect association support added

  This added support improves the error-handling framework
  for NVMe-FC and is enabled in the Emulex
  (`lpfc`) driver.

#### File Systems

The following file system changes are implemented in
UEK R6U2:

- Btrfs

  General upstream patches for security enhancements and
  bug fixes have been applied.
- CIFS

  General upstream bug fix patches have been applied.
  Notably, a fix was applied for an issue that resulted in
  a kernel panic when the CIFS module attempted a
  reconnect to a CIFS server that was unavailable.
- Ext4

  General upstream patches for security enhancements and
  bug fixes have been applied.
- NFS

  General upstream bug fixes and performance enhancements
  have been applied for NFS. Additionally, several fixes
  and improvements were applied for NFS v4.2 Server Side
  Copy functionality which remains available as a
  technical preview.
- OCFS2

  A fix was applied to better handle setting ACLs on the
  file system so that they are made effective immediately
  and any cached ACLs are reset.
- XFS

  General upstream patches for security enhancements and
  bug fixes have been applied.

#### vhost and vhost-scsi Performance Improvements

Kernel improvements have been made in this release to boost
IOPS (input/output operations per second) for a
`vhost` SCSI device over
`dm-multipath`.

Notable changes, fixes, and improvements include the
following:

- Improved error handling for `vhost-scsi`
  to prevent SCSI commands from failing when a SCSI command
  times out in the guest OS.
- A fix to the `vhost-scsi` module's
  multiqueue support so that a single
  `vhost-scsi` device can execute up to
  1024 commands over up to 128 virtqueues.

#### Technical Preview Features

Several features are under investigation and ongoing
development for release within UEK R6. The following features
are available within UEK R6U2 as a technical preview.

- Core Scheduling

  Core scheduling is a feature enabled in the kernel to
  limit trusted tasks to run concurrently on CPU cores
  that share compute resources to help mitigate against
  certain categories of 'core shared cache' processor bugs
  that could cause data leakage and other related
  vulnerabilities. This feature has been enabled in
  UEK R6 since UEK R6U1 as a technical preview and is
  under active development.
- WireGuard

  WireGuard is a faster and more secure replacement for
  IPsec and OpenVPN. New networks are being built with
  modern cryptography from WireGuard rather than legacy
  technologies like IPsec and OpenVPN. WireGuard has been
  enabled as a technical preview in UEK R6 since
  UEK R6U1 and continues to be available as a technical
  preview in the current update release. Several
  improvememnts for WireGuard are included in this update
  release.
- NFS v4.2 Server Side Copy

  NFS v4.2 Server Side Copy functionality is back-ported
  from the upstream kernel and has been available in
  UEK R6 since UEK R6U1 as a technical preview. The
  server-side copy features provide mechanisms that allow
  an NFS client to copy file data on a server or between
  two servers without the data being transmitted back and
  forth over the network through the NFS client. Several
  improvements for this feature are included in this
  update release.

### Driver Updates

The Unbreakable Enterprise Kernel Release 6 supports a large number of hardware and devices. In
close cooperation with hardware and storage vendors, Oracle has
updated several device drivers from the versions in mainline
Linux 5.4.

A complete list of the driver modules included in UEK R6, along
with version information is provided in the appendix at
[Driver Modules in Unbreakable Enterprise Kernel Release 6 (x86\_64)](uek6.2-DriverModulesinUnbreakableEnterpriseKernelRelease6x8664.html#uek-driver-versions-x86_64).

The following new features are noted in the drivers that are
shipped with UEK R6U2:

- Broadcom Emulex LightPulse Fibre Channel SCSI driver

  The Broadcom Emulex LightPulse Fibre Channel SCSI driver,
  `lpfc`, is updated to version 12.8.0.5
  with vendor supplied patches and bug fixes. Notably, a 256
  Gb speed setting is enabled for SCSI Fibre Channel
  transport.
- LSI MPT Fusion SAS 3.0 Device driver

  The LSI MPT Fusion SAS 3.0 Device driver,
  `mpt3sas`, is updated to version
  36.100.00.00 to include vendor supplied patches that bring
  the driver version in line with the upstream kernel
  release.
- QLogic Fibre Channel HBA driver

  The QLogic Fibre Channel HBA driver,
  `qla2xxx` is updated to version
  10.02.00.103-k and includes a large number of vendor
  supplied patches to bring the driver version in line with
  the upstream kernel release.

### Compatibility

Oracle Linux maintains full user space compatibility with Red Hat
Enterprise Linux (RHEL), which is independent of the kernel
version that is running underneath the operating system.
Existing applications in user space continue to run unmodified
on the Unbreakable Enterprise Kernel Release 6 and no re-certifications are needed for RHEL
certified applications.

To minimize impact on interoperability during releases, the Oracle Linux
team works closely with third-party vendors whose hardware and
software have dependencies on kernel modules. The kernel ABI for
UEK R6 remains unchanged in all subsequent updates to the
initial release. In this release, there are changes to the
kernel ABI relative to UEK R5 that require recompilation of
third-party kernel modules on the system. Before installing
UEK R6, verify its support status with your application vendor.

#### Notable changes in kernel headers

Upstream changes to kernel headers may mean that third party
modules do not compile across different kernel versions
without modification to source code. Notably, the
`memcg_cache_params` structure has been moved
from `include/linux/slab.h` to
`mm/slab.h`. This means that code needs to be
refactored to account for the change if you are compiling
across kernel versions.

To solve this problem, so that the code can compile for both
UEK R5 and UEK R6, change header requirements in the source
code. For example, change lines like those in the following
example to what is shown in the second example:

```
#ifdef CONFIG_SLUB
#include <linux/slub_def.h>
#endif
```

```
#if ( LINUX_VERSION_CODE < KERNEL_VERSION(5,4,0) )

#ifdef CONFIG_SLUB
#include <linux/slub_def.h>
#endif

#endif
```

### Certification of UEK R6 for Oracle products

Note that the certification of different Oracle products on
UEK R6 may not be immediately available at the time of a
UEK R6 release. You should always check to ensure that the
product you are using is certified for use on UEK R6 before
upgrading or installing the kernel. Check certification at
<https://support.oracle.com/epmos/faces/CertifyHome>.

Oracle Automatic Storage Management Cluster File System (Oracle
ACFS) certification for different kernel versions is described
in Document ID 1369107.1, which is available at
<https://support.oracle.com/epmos/faces/DocumentDisplay?id=1369107.1>.

Oracle Automatic Storage Management Filter Driver (Oracle ASMFD)
certification for different kernel versions is described in
Document ID 2034681.1, which is available at
<https://support.oracle.com/epmos/faces/DocumentDisplay?id=2034681.1>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.2/uek6-SecurityFixesforCVEs.html -->

This chapter lists security vulnerabilities and exposures (CVEs)
that are specifically addressed in this release. Note that CVEs are
continually handled in patch updates that are made available as
errata builds for the current release. For this reason, it is
absolutely critical that you keep your system up to date with the
latest package updates for this kernel release.

You can keep up to date with the latest CVE information at
<https://linux.oracle.com/cve>.

### List of CVEs fixed in this release

The following list describes the CVEs that are fixed in this
release. The content provided here is automatically generated and
includes the CVE identifier and a summary of the issue. The
associated internal Oracle bug identifiers are also included to
reference work that was carried out to address each issue.

- CVE-2020-14381

  A flaw was found in the Linux kernelâs futex
  implementation. This flaw allows a local attacker to corrupt
  system memory or escalate their privileges when creating a
  futex on a filesystem that is about to be unmounted. The
  highest threat from this vulnerability is to
  confidentiality, integrity, as well as system availability.
  A flaw was found in the Linux kernelâs futex
  implementation. This flaw allows a local attacker to corrupt
  system memory or escalate their privileges when creating a
  futex on a filesystem that is about to be unmounted. The
  highest threat from this vulnerability is to
  confidentiality, integrity, as well as system availability.

  See
  <https://linux.oracle.com/cve/CVE-2020-14381.html>
  for more information.
- CVE-2020-16120

  Overlayfs did not properly perform permission checking when
  copying up files in an overlayfs and could be exploited from
  within a user namespace, if, for example, unprivileged user
  namespaces were allowed. It was possible to have a file not
  readable by an unprivileged user to be copied to a
  mountpoint controlled by the user, like a removable device.
  This was introduced in kernel version 4.19 by commit d1d04ef
  ("ovl: stack file ops"). This was fixed in kernel version
  5.8 by commits 56230d9 ("ovl: verify permissions in
  ovl\_path\_open()"), 48bd024 ("ovl: switch to mounter creds in
  readdir") and 05acefb ("ovl: check permission to open real
  file"). Additionally, commits 130fdbc ("ovl: pass correct
  flags for opening real directory") and 292f902 ("ovl: call
  secutiry hook in ovl\_real\_ioctl()") in kernel 5.8 might also
  be desired or necessary. These additional commits introduced
  a regression in overlay mounts within user namespaces which
  prevented access to files with ownership outside of the user
  namespace. This regression was mitigated by subsequent
  commit b6650da ("ovl: do not fail because of O\_NOATIMEi") in
  kernel 5.11. A flaw was found in the User namespace on an
  overlay filesystem in the Linux Kernel, Where a file with no
  access privilege was able to copy the file to a user defined
  mount point. An attacker with a special user privilege
  locally may lead to a kernel information leak problem. (Bug:
  32046371
  )

  See
  <https://linux.oracle.com/cve/CVE-2020-16120.html>
  for more information.
- CVE-2020-25639

  A NULL pointer dereference flaw was found in the Linux
  kernel's GPU Nouveau driver functionality in versions prior
  to 5.12-rc1 in the way the user calls ioctl
  DRM\_IOCTL\_NOUVEAU\_CHANNEL\_ALLOC. This flaw allows a local
  user to crash the system.A NULL pointer dereference flaw was
  found in the Linux kernelâs GPU Nouveau driver
  functionality in the way the user calls ioctl
  DRM\_IOCTL\_NOUVEAU\_CHANNEL\_ALLOC. This flaw allows a local
  user to crash the system. (Bug: 32591559
  )
- CVE-2020-25656

  A flaw was found in the Linux kernel. A use-after-free was
  found in the way the console subsystem was using ioctls
  KDGKBSENT and KDSKBSENT. A local user could use this flaw to
  get read memory access out of bounds. The highest threat
  from this vulnerability is to data confidentiality. A flaw
  was found in the Linux kernel. A use-after-free was found in
  the way the console subsystem was using ioctls KDGKBSENT and
  KDSKBSENT. A local user could use this flaw to get read
  memory access out of bounds. The highest threat from this
  vulnerability is to data confidentiality.

  See
  <https://linux.oracle.com/cve/CVE-2020-25656.html>
  for more information.
- CVE-2020-27170

  An issue was discovered in the Linux kernel before 5.11.8.
  kernel/bpf/verifier.c performs undesirable out-of-bounds
  speculation on pointer arithmetic, leading to side-channel
  attacks that defeat Spectre mitigations and obtain sensitive
  information from kernel memory, aka CID-f232326f6966. This
  affects pointer types that do not define a ptr\_limit. A flaw
  was found in the Linux kernels eBPF verification code. By
  default accessing the eBPF verifier is only accessible to
  privileged users with CAP\_SYS\_ADMIN. A local user with the
  ability to insert eBPF instructions can use the eBPF
  verifier to abuse a spectre like flaw where they can infer
  all system memory. (Bug: 32656761
  )
- CVE-2020-27171

  An issue was discovered in the Linux kernel before 5.11.8.
  kernel/bpf/verifier.c has an off-by-one error (with a
  resultant integer underflow) affecting out-of-bounds
  speculation on pointer arithmetic, leading to side-channel
  attacks that defeat Spectre mitigations and obtain sensitive
  information from kernel memory, aka CID-10d2bb2e6b1d. A flaw
  was found in the Linux kernels eBPF verification code. By
  default accessing the eBPF verifier is only accessible to
  privileged users with CAP\_SYS\_ADMIN. A flaw that triggers
  Integer underflow when restricting speculative pointer
  arithmetic allows unprivileged local users to leak the
  content of kernel memory. The highest threat from this
  vulnerability is to data confidentiality. (Bug: 32656761
  )
- CVE-2020-28374

  In drivers/target/target\_core\_xcopy.c in the Linux kernel
  before 5.10.7, insufficient identifier checking in the LIO
  SCSI target code can be used by remote attackers to read or
  write files via directory traversal in an XCOPY request, aka
  CID-2896c93811e3. For example, an attack can occur over a
  network if the attacker has access to one iSCSI LUN. The
  attacker gains control over file access because I/O
  operations are proxied via an attacker-selected backstore. A
  flaw was found in the Linux kernelâs implementation of
  the Linux SCSI target host, where an authenticated attacker
  could write to any block on the exported SCSI device backing
  store. This flaw allows an authenticated attacker to send
  LIO block requests to the Linux system to overwrite data on
  the backing store. The highest threat from this
  vulnerability is to integrity. In addition, this flaw
  affects the tcmu-runner package, where the affected SCSI
  command is called. (Bug: 32374281
  )

  See
  <https://linux.oracle.com/cve/CVE-2020-28374.html>
  for more information.
- CVE-2020-28588

  A flaw read uninitialized values in the Linux kernel syscall
  implementation on 32 bit-systems was found in the way user
  reading /proc/self/syscall. A local user could use this flaw
  to read three 64 bits uninitialized values, but cannot
  control which values. The highest threat from this
  vulnerability is to confidentiality.
- CVE-2020-29568

  (Bug: 32253408
  )

  See
  <https://linux.oracle.com/cve/CVE-2020-29568.html>
  for more information.
- CVE-2020-29569

  (Bug: 32260251
  )

  See
  <https://linux.oracle.com/cve/CVE-2020-29569.html>
  for more information.
- CVE-2020-36158

  mwifiex\_cmd\_802\_11\_ad\_hoc\_start in
  drivers/net/wireless/marvell/mwifiex/join.c in the Linux
  kernel through 5.10.4 might allow remote attackers to
  execute arbitrary code via a long SSID value, aka
  CID-5c455c5ab332. A flaw was found in the Linux kernel. The
  marvell wifi driver could allow a local attacker to execute
  arbitrary code via a long SSID value in
  mwifiex\_cmd\_802\_11\_ad\_hoc\_start function. The highest threat
  from this vulnerability is to data confidentiality and
  integrity as well as system availability.

  See
  <https://linux.oracle.com/cve/CVE-2020-36158.html>
  for more information.
- CVE-2020-4788

  IBM Power9 (AIX 7.1, 7.2, and VIOS 3.1) processors could
  allow a local user to obtain sensitive information from the
  data in the L1 cache under extenuating circumstances. IBM
  X-Force ID: 189296. A flaw was found in the Linux kernel.
  IBM Power9 processors can speculatively operate on data
  stored in the L1 cache before it has been completely
  validated. The attack has limited access to memory and is
  only able to access memory normally permissible to the
  execution context. The highest threat from this
  vulnerability is to data confidentiality.
- CVE-2021-20177

  A flaw was found in the Linux kernel's implementation of
  string matching within a packet. A privileged user (with
  root or CAP\_NET\_ADMIN) when inserting iptables rules could
  insert a rule which can panic the system. (Bug: 32372529
  )

  See
  <https://linux.oracle.com/cve/CVE-2021-20177.html>
  for more information.
- CVE-2021-26930

  (Bug: 32492108
  )

  See
  <https://linux.oracle.com/cve/CVE-2021-26930.html>
  for more information.
- CVE-2021-26931

  (Bug: 32492100
  )

  See
  <https://linux.oracle.com/cve/CVE-2021-26931.html>
  for more information.
- CVE-2021-26932

  (Bug: 32492092
  )

  See
  <https://linux.oracle.com/cve/CVE-2021-26932.html>
  for more information.
- CVE-2021-27363

  An issue was discovered in the Linux kernel through 5.11.3.
  A kernel pointer leak can be used to determine the address
  of the iscsi\_transport structure. When an iSCSI transport is
  registered with the iSCSI subsystem, the transport's handle
  is available to unprivileged users via the sysfs file
  system, at
  /sys/class/iscsi\_transport/$TRANSPORT\_NAME/handle. When
  read, the show\_transport\_handle function (in
  drivers/scsi/scsi\_transport\_iscsi.c) is called, which leaks
  the handle. This handle is actually the pointer to an
  iscsi\_transport struct in the kernel module's global
  variables. A flaw was found in the way access to sessions
  and handles was handled in the iSCSI driver in the Linux
  kernel. A local user could use this flaw to leak iSCSI
  transport handle kernel address or end arbitrary iSCSI
  connections on the system. (Bug: 32603378
  )

  See
  <https://linux.oracle.com/cve/CVE-2021-27363.html>
  for more information.
- CVE-2021-27364

  An issue was discovered in the Linux kernel through 5.11.3.
  drivers/scsi/scsi\_transport\_iscsi.c is adversely affected by
  the ability of an unprivileged user to craft Netlink
  messages. A flaw was found in the Linux kernel. An
  out-of-bounds read was discovered in the libiscsi module
  that could lead to reading kernel memory or a crash. The
  highest threat from this vulnerability is to data
  confidentiality as well as system availability. (Bug:
  32603378
  )

  See
  <https://linux.oracle.com/cve/CVE-2021-27364.html>
  for more information.
- CVE-2021-27365

  An issue was discovered in the Linux kernel through 5.11.3.
  Certain iSCSI data structures do not have appropriate length
  constraints or checks, and can exceed the PAGE\_SIZE value.
  An unprivileged user can send a Netlink message that is
  associated with iSCSI, and has a length up to the maximum
  length of a Netlink message. A flaw was found in the Linux
  kernel. A heap buffer overflow in the iSCSI subsystem is
  triggered by setting an iSCSI string attribute to a value
  larger than one page and then trying to read it. The highest
  threat from this vulnerability is to data confidentiality
  and integrity as well as system availability. (Bug: 32603378
  )

  See
  <https://linux.oracle.com/cve/CVE-2021-27365.html>
  for more information.
- CVE-2021-3347

  An issue was discovered in the Linux kernel through 5.10.11.
  PI futexes have a kernel stack use-after-free during fault
  handling, allowing local users to execute code in the
  kernel, aka CID-34b1a1ce1458. A flaw was found in the Linux
  kernel. A use-after-free memory flaw in the Fast Userspace
  Mutexes functionality allowing a local user to crash the
  system or escalate their privileges on the system. The
  highest threat from this vulnerability is to data
  confidentiality and integrity as well as system
  availability. (Bug: 32447185
  )

  See
  <https://linux.oracle.com/cve/CVE-2021-3347.html>
  for more information.
- CVE-2021-3348

  nbd\_add\_socket in drivers/block/nbd.c in the Linux kernel
  through 5.10.12 has an ndb\_queue\_rq use-after-free that
  could be triggered by local attackers (with access to the
  nbd device) via an I/O request at a certain point during
  device setup, aka CID-b98e762e3d71.A use after free flaw in
  the Linux kernel network block device (NBD) subsystem was
  found in the way user calls an ioctl NBD\_SET\_SOCK at a
  certain point during device setup. (Bug: 32447284
  )

  See
  <https://linux.oracle.com/cve/CVE-2021-3348.html>
  for more information.
- CVE-2021-3444

  The bpf verifier in the Linux kernel did not properly handle
  mod32 destination register truncation when the source
  register was known to be 0. A local attacker with the
  ability to load bpf programs could use this gain
  out-of-bounds reads in kernel memory leading to information
  disclosure (kernel memory), and possibly out-of-bounds
  writes that could potentially lead to code execution. This
  issue was addressed in the upstream kernel in commit
  9b00f1b78809 ("bpf: Fix truncation handling for mod32 dst
  reg wrt zero") and in Linux stable kernels 5.11.2, 5.10.19,
  and 5.4.101. A flaw was found in the Linux kernel. The bpf
  verifier does not properly handle mod32 destination register
  truncation when the source register was known to be 0. A
  local attacker with the ability to load bpf programs could
  use this gain out-of-bounds reads in kernel memory leading
  to information disclosure (kernel memory), and possibly
  out-of-bounds writes that could potentially lead to code
  execution. The highest threat from this vulnerability is to
  data confidentiality and integrity as well as system
  availability. (Bug: 32673813
  )


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.2/uek6-KnownIssues.html -->

This chapter describes the known issues for the Unbreakable Enterprise Kernel Release 6.

### Unusable or Unavailable Arm Features

The following features are known to not work, remain untested, or
have issues that cause the feature to be unusable or unavailable
on the 64-bit Arm (aarch64) platform:

- InfiniBand

  InfiniBand hardware is currently not supported for Arm
  architecture using UEK R6.
- FibreChannel

  FibreChannel hardware is currently not supported for Arm
  architecture using UEK R6.
- RDMA

  RDMA and any of its subfeatures are not supported for the
  Arm architecture.
- Secure Boot and Lockdown

  The Secure Boot feature and the Kernel Lockdown
  functionality are not supported or available for the Arm
  architecture.

### Serial port console can crash if the serial port baud rate is too low

On systems that use a physical serial console to monitor system
output, such as on an ILOM console interface, it is possible that
high levels of output can introduce abnormal system behavior such
as kernel deadman timer events that indicate processes are unable
to obtain CPU scheduler time. This is typically experienced if the
serial console speed is set too low and a log level of 6 or higher
is configured for the system. To reduce the likelihood of this
issue occurring, either reduce the log level or configure the
console for the maximum possible baud rate, 115200.

Starting with UEK R6U1, a warning is displayed in the
`dmesg` output if the baud rate is set too low:

```
dmesg | grep -A4 -i baud
```

```
[  369.777802] Serial console is set to the default of 9600 baud. This can
[  369.778852] result in stalls or lockups in error conditions requiring a
[  369.779892] large number of console system messages. Please increase the
[  369.780889] rate to the highest your system will allow (for instance,
115200
[  369.781918] or 57600). See Oracle KM Note 2648582.1 for more information.
```

The current console speed for a running Oracle Linux 7 or Oracle Linux 8 system can
be set for a configured serial port by running:

```
stty -F /dev/ttyS0 speed 115200
```

To change the serial console speed that is used when the system
boots, you must edit the GRUB configuration. Edit
`/etc/sysconfig/grub` in a text editor and append
console=ttyS0,115200
to the line starting with `GRUB_CMDLINE_LINUX`,
for example:

```
GRUB_CMDLINE_LINUX="crashkernel=auto resume=/dev/mapper/linux1-swap rd.lvm.lv=linux1/root \
  rd.lvm.lv=linux1/swap rhgb quiet console=ttyS0,115200"
```

Note that in the above examples, the serial console is assumed to
be ttyS0, you may need to change this
if you have used an alternate serial port.

To update your grub configuration with the changes so that they
are used on the next boot if you are using legacy BIOS, run:

```
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

Alternately, if you are booting by using the Unified Extensible
Firmware Interface (UEFI), run the following command:

```
sudo grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg
```

If you are using Oracle Server hardware, or a system that provides
an ILOM interface to the serial console, make sure that you update
the serial console configuration on the ILOM to match the speed
that you have set within the host operating system. You can set
the serial port on the ILOM CLI by running:

```
sudo set /SP/serial/host pendingspeed=115200 commitpending=true
```

To check the current console port speed on the ILOM, using the
CLI, run:

```
sudo show /SP/serial/host
```

For more information about ILOM configuration, see
<https://docs.oracle.com/cd/E19203-01/820-1188-12/core_ilom_managing.html>.

(Bug ID 30487830, 30439170)

### SELinux "Permission watch" messages displayed

Booting UEK R6 in either the SELinux permissive mode or the
enforcing mode produces messages similar to the following:

```
SELinux:  Permission watch in class filesystem not defined in policy. 
SELinux:  Permission watch in class file not defined in policy. 
SELinux:  Permission watch_mount in class file not defined in policy. 
SELinux:  Permission watch_sb in class file not defined in policy.
SELinux: the above unknown classes and permissions will be allowed
```

These messages are displayed because no definitions currently
exist for these classes in SELinux policy. Per the last line of
the message, classes and permissions are allowed by default; and
therefore, the messages can be safely ignored.

(Bug ID 30687021, 30687021)

### SELinux in enforcing mode with the MLS policy not supported

When SELinux is configured to use the Multilevel Security (MLS)
policy and it is in the enforcing mode, several issues can prevent
normal functioning of the operating system, including permissions
errors when attempting to mount file systems and the likelihood of
a Systemd freeze when booting the operating system.

SELinux in the enforcing mode with the MLS policy is not
supported. Note that you can continue to use SELinux in the
enforcing mode by using the targeted policy.

(Bug ID 30797389, 30609238)

### Spurious xs\_tcp\_setup\_socket: connect messages when using NFS

When using NFS, inaccurate messages regarding socket connection
errors may be emitted. Messages may appear as follows:

```
xs_tcp_setup_socket: connect returned unhandled error -107
```

The underlying connection issue is resolved and any connections
that fail are now automatically reopened. Provided no associated
functional impact is experienced, this error message may be
ignored. Note that this message may also appear as a result of a
genuine ongoing connection issue.

(Bug ID 30339848)

### mstlink command crashes with core dump when used on Oracle Linux 8

The `mstlink` command crashes when run on an
Oracle Linux 8 system running Unbreakable Enterprise Kernel Release 6. The following output is
typical:

```
sudo mstlink -d 13:00.1
```

```
/usr/include/c++/8/bits/stl_vector.h:932: std::vector<_Tp, _Alloc>::reference
std::vector<_Tp, _Alloc>::operator[](std::vector<_Tp, _Alloc>::size_type)
[with _Tp = unsigned int; _Alloc = std::allocator<unsigned int>;
std::vector< Tp, _Alloc>::reference = unsigned int& std::vector<_Tp,
_Alloc>::size_type = long unsigned int]: Assertion '__builtin_expect(__n <
this->size(), true)' failed.
Aborted (core dumped)
```

This issue is related to system-wide hardening changes introduced
upstream and present in Oracle Linux 8. The upstream tools in the
`mstflint` package, including
`mstlink` do not adequately cater for these
hardening changes. Alternate tools can be used to gather and
configure link information, including `ip link`,
`ethtool`, `ifstat`, and
`ibv_devinfo`.

(Bug ID 30993407)

### IOMMU kernel option enabled by default

Starting with UEK R5U1, IOMMU functionality is enabled by default
in the x86\_64 kernel. This change better facilitates single root
input-output virtualization (SR-IOV) and other virtualization
extensions; however, it is also known to result in boot failure
issues on certain hardware that cannot complete discovery when
IOMMU is enabled. The status of this feature no longer appears in
`/proc/cmd` reporting as
`iommu=on`, which means it may need to be
explicitly disabled as a kernel `cmdline` option
if boot failure occurs. As an alternative workaround, you can
disable IOMMU or Intel-Vtd in your system ROM by following your
vendor instructions.

These boot failure issues have been observed on equipment with
certain Broadcom network devices, such HP Gen8 servers. For more
detailed information, see
<https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-c04565693>.

### bnxt\_re: probe error: "RoCE is not supported on this device" reported after installing on certain hardware with Broadcom NetXtreme-C/E bnxt\_en driver

On some hardware that includes the NetXtreme-C/E bnxt\_en driver,
messages similar to the following can be observed in the system
log (`var/log/messages`) immediately following a
fresh installation:

```
grep bnxt /var/log/messages
```

```
Apr 26 12:00:30 ca-ostest644 kernel: Broadcom NetXtreme-C/E driver bnxt_en
v1.10.1
Apr 26 12:00:30 ca-ostest644 kernel: bnxt_en 0000:18:00.0 (unnamed
net_device) (uninitialized): Firmware does not support TC flower offload.
Apr 26 12:00:30 ca-ostest644 kernel: bnxt_en 0000:18:00.0 eth1: Broadcom
BCM57417 NetXtreme-E 10GBase-T Ethernet found at mem 381c01210000, node addr
00:10:e0:d8:33:09
Apr 26 12:00:30 ca-ostest644 kernel: bnxt_en 0000:18:00.0: 63.008 Gb/s
available PCIe bandwidth (8 GT/s x8 link)
Apr 26 12:00:30 ca-ostest644 kernel: bnxt_en 0000:18:00.1 (unnamed
net_device) (uninitialized): Firmware does not support TC flower offload.
Apr 26 12:00:30 ca-ostest644 kernel: bnxt_en 0000:18:00.1 eth2: Broadcom
BCM57417 NetXtreme-E 10GBase-T Ethernet found at mem 381c01200000, node addr
00:10:e0:d8:33:0a
.
.
.
```

The `dmesg` command reports similar messages:

```
dmesg | grep bnxt
```

```
[    2.703443] Broadcom NetXtreme-C/E driver bnxt_en v1.10.1
[    2.720552] bnxt_en 0000:18:00.0 (unnamed net_device) (uninitialized):
Firmware does not support TC flower offload.
[    2.961037] bnxt_en 0000:18:00.0 eth1: Broadcom BCM57417 NetXtreme-E
10GBase-T Ethernet found at mem 381c01210000, node addr 00:10:e0:d8:33:09
[    2.961044] bnxt_en 0000:18:00.0: 63.008 Gb/s available PCIe bandwidth (8
GT/s x8 link)
[    2.986775] bnxt_en 0000:18:00.1 (unnamed net_device) (uninitialized):
Firmware does not support TC flower offload.
[    2.996323] bnxt_en 0000:18:00.1 eth2: Broadcom BCM57417 NetXtreme-E
10GBase-T Ethernet found at mem 381c01200000, node addr 00:10:e0:d8:33:0a
[    2.996331] bnxt_en 0000:18:00.1: 63.008 Gb/s available PCIe bandwidth (8
GT/s x8 link)
[    3.011390] bnxt_en 0000:18:00.0 eno2np0: renamed from eth1
[    3.260089] bnxt_en 0000:18:00.1 eno3np1: renamed from eth2
[    9.038400] bnxt_re: Broadcom NetXtreme-C/E RoCE Driver
[    9.038472] bnxt_en 0000:18:00.0: bnxt_re: probe error: RoCE is not
```

These error messages are reported because RDMA support is disabled
in the `bnxt_en` card's firmware on some Oracle
servers; however, note that the issue does not impact all Broadcom
NetXtreme-C/E cards.

To work around the issue, you must enable RDMA support in the
card's firmware prior to the installation.

(Bug ID 32819934)

### Messages emitted indicating the route cache is full when using IPv6

On some systems, error messages indicating that the route cache is
full, are emitted when using IPv6. An error similar to the
following example may be returned:

```
[ 5523.456447] Route cache is full: consider increasing sysctl
net.ipv[4|6].route.max_size.
```

It is unclear what causes these errors or to what size
`/proc/sys/net/ipv6/route/max_size` should be
increased; but, on a test system, the issue could not be
replicated after running the following command:

```
sudo sysctl net.ipv6.route.max_size=32768
```

Because the issue is currently under investigation, increasing
this value is a viable workaround.

(Bug ID 30976607)

### IPv6 failback fails when using RoCE

The `rdmaip` driver does not send IPv6 address
change notification to RDS, which can delay or prevent IPv6 fail
over when using RoCE. This is apparent when active bonding is
enabled and only occurs for IPv6. The IPv4 failover continues to
work correctly.

When the issue is triggered, the following messages may appear in
the kernel log:

```
kernel: rdmaip: could not add 2001:db8:0:f101::50%4/64 to ens2f0 (port 1)
kernel: IPv6: ens2f0: IPv6 duplicate address 2001:db8:0:f101::50 used by 
        50:6b:4b:cb:ef:23 detected!
```

A fix is in development but is not available at the time of this
release. The fix may become available as an errata update.

(Bug ID 31021418)

### It is not possible to remove the libpcap package

Attempting to remove the `libpcap` package or
performing an action that would attempt to remove the package
results in an error because the dependency chain would require the
removal of the `systemd` package and this would
break the system.

This is expected behavior in Oracle Linux 8; however, the behavior is
mentioned here because in previous Oracle Linux releases, it was possible to remove
the `libpcap` package

In some circumstances, such as when installing the RDMA packages,
`libpcap` may be upgraded to a newer version than
the version provided for the operating system. If you remove these
packages, you may wish to also downgrade the
`libpcap` package to match the highest version
provided for the operating system in the BaseOS channel or
repository. Typically, this might be most easily done by reverting
the installation using the `dnf history undo`
command. See the `DNF(8)` manual page for more
information.

(Bug ID 30979601)

### Network latency may increase on Infiniband fabrics

If the TCP write size is close to the size of the Infiniband (IB)
Maximum Transmission Unit (MTU), applications may experience
higher latencies on packet transfers. For example, the default IB
MTU is 65520 bytes. An application that also uses a TCP write size
between 65520 bytes to 128 KB may experience this issue. The issue
does not appear when applications use larger (for example, 256 KB)
or smaller (for example, 4 KB or 32 KB) TCP write sizes.

Note that Ethernet networks are not affected by this issue.

The default values for the IB MTU and TCP write sizes in Oracle Linux and
UEK R6 do not expose the issue. Applications with modified TCP
window sizes, or systems with modified MTU values, could overlap
and expose this issue.

The workaround for this issue is to tune either the MTU of the IB
interface, or the TCP write size of the application, so that the
TCP write size is smaller than the IB MTU or the TCP write size is
greater than 2x the IB MTU. You can tune MTUs dynamically by using
the `ip link` command. Note that tuning of the
TCP write size is application specific.

(Bug ID 31830430)

### (aarch64) Perf tool can result in application slowdown when profiling some virtualized Arm platforms

Note:

The following issue does not affect bare metal installations.

On virtual machines (VMs) that are running on a multi-socket
aarch64 platform, if the `perf top` or
`perf record` command is invoked, it is possible
that application slowdowns may occur. In certain cases, the
following message is emitted in a terminal window:

```
kernel:watchdog: BUG: soft lockup
```

You can mitigate this problem as follows:

- To avoid lockup situations and reduce probe effect, you can
  specify a sample period by using the `-c`
  flag with the `perf record` command, rather
  than a frequency by using the `-F` flag. For
  example, you would use the `perf record -c`
  command instead of the `perf record -F 100`
  command.
- Do not use the `perf`
  command with the `--all-cpus` flag. Instead,
  specify a minimal number of CPUs by using the `perf
  -C` command.

(Bug ID 32834324)

### (aarch64) Kdump fails to allocate crashkernel memory on some Arm systems

On some 64-bit Arm (aarch64) systems, where insufficient low
contiguous memory is available, Kdump may fail due to the system's
inability to allocate the minimum `crashkernel`
memory that is typically reserved when the `auto`
value is set.

This issue results in Kdump failing to start and the following
errors appearing in the logs:

```
kdumpctl[3812]: No memory reserved for crash kernel
...
systemd[1]: Failed to start Crash recovery kernel arming.
```

To work around this issue, manually set the
`crashkernel` low and high values and attempt to
set a low value that is below 256 MB. For example, replace
`crashkernel=auto` with
`crashkernel=800M,high crashkernel=200M,low`.

(Bug ID 31554906)

### Spurious trace\_printk warning emitted when using RDS or RDMA

When using UEK R6 with RDS or RDMA, the system emits messages
similar to the following:

```
[  136.066002] **********************************************************
[  136.068731] **   NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE   **
[  136.071346] **                                                      **
[  136.074893] ** trace_printk() being used. Allocating extra memory.  **
[  136.078505] **                                                      **
[  136.082337] ** This means that this is a DEBUG kernel and it is     **
[  136.086093] ** unsafe for production use.                           **
[  136.089887] **                                                      **
[  136.093682] ** If you see this message and you are not debugging    **
[  136.097192] ** the kernel, report this immediately to your vendor!  **
[  136.100615] **                                                      **
[  136.104239] **   NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE   **
[  136.108005] **********************************************************
[  136.209499] NET: Registered protocol family 21
[  136.229371] Registered RDS/tcp transport
```

These messages are displayed because the Resilient RDMAIP kernel
module currently uses `trace_print()` for
debugging infrastructure. On RDS/RDMA systems, these messages can
be safely ignored and do not mean that the kernel is unsafe for
production use.

(Bug ID 31066169)

### The ipmctl-monitor package is no longer required to use ipmctl

The `ipmctl-monitor` package is not required for
the `ipmctl` version 2.0 available for UEK R6U2.
If you are updating the system from an earlier version of
`ipmctl` or you attempt to install the
`ipmctl-monitor` package along with other
`ipmctl` utilities, you may see conflicts such as
the following:

```
Error:
 Problem: cannot install both libipmctl-02.00.00.3852-1.0.1.el8.x86_64 and
libipmctl-01.00.00.3467-1.0.1.el8.x86_64
  - package ipmctl-monitor-01.00.00.3467-1.0.1.el8.x86_64 requires
libipmctl.so.3()(64bit), but none of the providers can be installed
  - package ipmctl-monitor-01.00.00.3467-1.0.1.el8.x86_64 requires
libipmctl(x86-64) = 01.00.00.3467-1.0.1.el8, but none of the providers can be
installed
  - cannot install the best candidate for the job
  - conflicting requests
```

If you are updating the system, remove the
`ipmctl-monitor` package before performing the
update:

```
sudo dnf remove ipmctl-monitor
sudo dnf update
```

If you are installing these packages for the first time, do not
include the `ipmctl-monitor` package in your
install command.

(Bug ID 32818557, 32516965)


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.2/uek6-InstallationandAvailability.html -->

You can install Unbreakable Enterprise Kernel Release 6 on Oracle Linux 7.7, or later, and on Oracle Linux 8.1, or
later, by running either the Red Hat Compatible Kernel (RHCK) or
a previous release of the Unbreakable Enterprise Kernel. If you are still running an
older version of Oracle Linux, you must first update your system to the
latest available update release.

Unbreakable Enterprise Kernel Release 6 is supported on x86-64 platforms but not on x86. The
Unbreakable Enterprise Kernel Release 6 is also supported on 64-bit Arm (aarch64) platforms.

### Installation Overview

If you have a subscription to Oracle Unbreakable Linux support,
you can obtain the packages for Unbreakable Enterprise Kernel Release 6 by registering your
system with the Unbreakable Linux Network (ULN) and subscribing
it to additional channels. See [Subscribing to ULN Channels](uek6-InstallationandAvailability.html#ol_sub_uln).

If your system is not registered with ULN, you can obtain most
of the packages from Oracle Linux yum server. See [Enabling Access to Oracle Linux Yum Server Repositories](uek6-InstallationandAvailability.html#ol_sub_pubyum).

Having subscribed your system to the appropriate channels on ULN
or Oracle Linux yum server, upgrade your system. See
[Upgrading Your System](uek6-InstallationandAvailability.html#ol_upgradea_sys).

### Subscribing to ULN Channels

The following procedure assumes that you have already registered
your system with ULN.

To subscribe your system to a channel on ULN:

1. Log in to
   <https://linux.oracle.com>
   with your ULN user name and password.
2. On the Systems tab, click the link named for the system in
   the list of registered machines.
3. On the System Details page, click
   Manage Subscriptions.
4. On the System Summary page, select each of the required
   channels from the list of available channels, then click the
   right arrow to move the channel to the list of subscribed
   channels.
5. Click Save Subscriptions.

For information about using ULN, see [Oracle Linux: Unbreakable Linux Network User's Guide for Oracle Linux 6 and Oracle Linux 7](https://docs.oracle.com/en/operating-systems/oracle-linux/uln-user/) or
[Oracle Linux: Managing Software on Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).

#### Oracle Linux 7

The kernel image and user space packages are available on the
`ol7_x86_64_UEKR6` ULN channel for Oracle Linux 7 on
x86\_64 platforms. For aarch64 platforms, these packages are
available on the `ol7_aarch64_UEKR6` ULN
channel.

#### Oracle Linux 8

Kernel image and user space packages are available on the
following ULN channels for Oracle Linux 8 on x86\_64 platforms:

- `ol8_x86_64_UEKR6`
- `ol8_x86_64_baseos_latest`

Oracle Linux 8 kernel image and user space packages for Oracle Linux 8 (aarch64) are made
available by default on the
`ol8_aarch64_baseos_latest` ULN channel.

### Enabling Access to Oracle Linux Yum Server Repositories

Packages for UEK R6 and associated user space applications are
available on the Oracle Linux yum server at
<https://yum.oracle.com/>.

#### Oracle Linux 7

All kernel image and associated user space packages for Oracle Linux 7
on the x86\_64 and aarch64 platforms are available in the
`ol7_UEKR6` repository.

To enable access to the Oracle Linux 7 repositories on the Oracle Linux yum server, use
`yum-config-manager`. For example, to enable
access to the `ol7_latest` and
`ol7_UEKR6` repositories, run the following:

```
sudo yum-config-manager --enable ol7_latest ol7_UEKR6
```

Note:

You can only use `yum-config-manager` to
enable or disable repositories where you already have a
configuration file for the specified repository. Repository
configurations are typically stored in
`/etc/yum.repos.d`. The repository
configurations required to install UEK on Oracle Linux 7 are
included in the `oraclelinux-release-el7`
package. You may need to update this package to the latest
version to obtain the correct yum repository configuration.

See [Oracle Linux 7: Administrator's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/7/admin/) for more information.

#### Oracle Linux 8

Kernel images and all associated user space packages for Oracle Linux 8
on x86\_64 platforms are available by enabling the
`ol8_UEKR6`,
`ol8_baseos_latest` and
`ol8_addons` repositories.

For aarch64 platforms, these packages are provided by default
within the `ol8_baseos_latest` repository.

To enable access to the Oracle Linux 8 repositories for the x86\_64
platform on the Oracle Linux yum server, use `dnf
config-manager`. For example, to enable access to the
`ol8_baseos_latest`,
`ol8_addons` and `ol8_UEKR6`
repositories, run the following command:

```
sudo dnf config-manager --enable ol8_baseos_latest ol8_addons ol8_UEKR6
```

Note:

You can only use `dnf config-manager` to
enable or disable repositories where you already have a
configuration file for the specified repository. Repository
configurations are typically stored in
`/etc/yum.repos.d`. The repository
configurations required to install UEK on Oracle Linux 8 are
included in the `oraclelinux-release-el8`
package. You may need to update this package to the latest
version to obtain the correct yum repository configuration.

See [Oracle Linux: Managing Software on Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/) for more information.

### Upgrading Your System

To upgrade your system to Unbreakable Enterprise Kernel Release 6:

1. Enable access to the appropriate ULN channels or yum
   repositories as described in [Subscribing to ULN Channels](uek6-InstallationandAvailability.html#ol_sub_uln)
   and [Enabling Access to Oracle Linux Yum Server Repositories](uek6-InstallationandAvailability.html#ol_sub_pubyum). It is good practice to
   disable any other UEK channels or repositories that you
   may have configured previously.
2. After enabling access to the appropriate channels, run the
   following command to upgrade the system to UEK R6 on Oracle Linux 7:

   ```
   sudo yum update
   ```

   Alternatively, run the following command on Oracle Linux 8:

   ```
   sudo dnf update
   ```
3. After upgrading the system, reboot it, selecting the UEK R6
   kernel (version 5.4) if this is not the default
   boot kernel.

For more information about using `yum` and `dnf` to
install updates, see [Oracle Linux: Unbreakable Linux Network User's Guide for Oracle Linux 6 and Oracle Linux 7](https://docs.oracle.com/en/operating-systems/oracle-linux/uln-user/) or [Oracle Linux: Managing Software on Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).

### Installing Oracle-Supported RDMA Packages for x86\_64 platforms

The following procedure describes how to install the RDMA release packages. The instructions
describe how to remove previous existing `oracle-ofed-release` packages and
other previously installed RDMA packages that could cause conflicts during the installation of
the UEK R6 RDMA packages. Note that the `yum` commands used in this
procedure are interchangeable with the `dnf` command available in Oracle
Linux 8.

1. In addition to the ULN channels and yum repositories
   described in [Subscribing to ULN Channels](uek6-InstallationandAvailability.html#ol_sub_uln) and
   [Enabling Access to Oracle Linux Yum Server Repositories](uek6-InstallationandAvailability.html#ol_sub_pubyum), subscribe the system to the
   appropriate RDMA ULN channel or yum repository.

   If you're using the Oracle Linux yum server, enable the `ol7_UEKR6_RDMA`
   repository for Oracle Linux 7; or the `ol8_UEKR6_RDMA` repository for
   Oracle Linux 8. For example, on Oracle Linux 7 run the following command:

   ```
   sudo yum-config-manager --enable ol7_latest ol7_UEKR6 ol7_UEKR6_RDMA
   ```

   On Oracle Linux 8 run the following command:

   ```
   sudo dnf config-manager --enable ol8_baseos_latest ol8_UEKR6 ol8_UEKR6_RDMA
   ```

   If you're subscribed to ULN, you can subscribe to `ol7_x86_64_UEKR6_RDMA`
   for Oracle Linux 7; or `ol8_x86_64_UEKR6_RDMA` for Oracle Linux 8.
2. Remove any existing packages that are related to RDMA, for
   example:

   ```
   sudo yum remove 'ibacm*'
   sudo yum remove 'ib-bonding*'
   sudo yum remove 'ibutils*'
   sudo yum remove 'infiniband-diags*'
   sudo yum remove 'libibacl*'
   sudo yum remove 'libibcm*'
   sudo yum remove 'libibmad*'
   sudo yum remove 'libibumad*'
   sudo yum remove 'libibverbs*'
   sudo yum remove 'libmlx4*'
   sudo yum remove 'librdmacm*'
   sudo yum remove 'libsdp*'
   sudo yum remove 'mlnx-tools'
   sudo yum remove 'mstflint*'
   sudo yum remove 'ofed-docs*'
   sudo yum remove 'ofed-scripts*'
   sudo yum remove 'opensm*'
   sudo yum remove 'oracle-ofed-release*'
   sudo yum remove 'oracle-rdma-release*'
   sudo yum remove 'oracle-rdma-tools'
   sudo yum remove 'perftest*'
   sudo yum remove 'qperf*'
   sudo yum remove 'rdma*'
   sudo yum remove 'rds-tools*'
   sudo yum remove 'sdpnetstat*'
   ```
3. Clean all yum cached files from all enabled repositories:

   ```
   sudo yum clean all
   ```
4. Install the RDMA packages for UEK R6.

   - On Oracle Linux 7, run the following commands:

     ```
     sudo yum install rdma-core
     sudo yum install infiniband-diags
     sudo yum install libibverbs-utils
     sudo yum install librdmacm-utils
     sudo yum install mstflint
     sudo yum install oracle-rdma-tools
     sudo yum install rds-tools
     sudo yum install ibutils
     sudo yum install libibacl
     ```

     - If installing on a bare-metal system, install the
       `infiniband-diags`
       package:

       ```
       sudo yum install infiniband-diags
       ```
     - If installing on a guest VM, install the `infiniband-diags-guest`
       package:

       ```
       sudo yum install infiniband-diags-guest
       ```
   - On Oracle Linux 8, run the following commands:

     ```
     sudo dnf install rdma-core
     sudo dnf install libibverbs-utils
     sudo dnf install librdmacm-utils
     sudo dnf install mlnx-tools
     sudo dnf install mstflint
     sudo dnf install rds-tools
     ```

     - If installing on a bare-metal system, install the
       `infiniband-diags`
       package:

       ```
       sudo dnf install infiniband-diags
       ```
     - If installing on a guest VM, install the `infiniband-diags-guest`
       package:

       ```
       sudo dnf install infiniband-diags-guest
       ```
   - (Optional) If you require the `perftest` package, install the package
     by running:

     ```
     sudo yum install perftest
     ```
   - (Optional) If you require the `qperf` package, install the package by
     running:

     ```
     sudo yum install qperf
     ```
   - (Optional) If you require the `libpcap` package, install the package
     by running:

     ```
     sudo yum install libpcap
     ```
   - (Optional) If you require the `ibacm` package, install the package by
     running:

     ```
     sudo yum install ibacm
     ```
   - (Optional) If you require the `srp_daemon` package, install the
     package by running:

     ```
     sudo yum install srp_daemon
     ```

Each UEK release requires a different set of RDMA packages. If you change the kernel on the
system to a UEK release before UEK R6, remove the existing UEK R6-based RDMA packages before
installing the correct packages for the new kernel.

Caution:

Downgrading UEK versions isn't advisable, except for testing purposes.

### Upgrading Oracle-Supported RDMA Packages for x86\_64 platforms

Typical upgrade of Oracle-supported RDMA package can be achieved
using the `dnf update` or `yum
update` command. Note that the `yum`
commands used in this procedure are interchangeable with the
`dnf` command available in Oracle Linux 8.

If you're upgrading a system where the `oracle-rdma-release` or
`oracle-rdma-release-guest` package is installed and the package version is
lower than version 0.18.1-1 and you intend to upgrade to version 0.18.1-1 or above, you must
first manually remove the `rdma-core-devel` package before performing the
upgrade. Remove this package using the `rpm -e --nodeps` command to
remove the package outside of the standard yum or dnf package manager control and leaving any
dependencies intact, for example:

```
sudo /bin/rpm -e --nodeps rdma-core-devel
sudo yum update
```

If you're upgrading an older system where the `oracle-ofed-release` or
`oracle-ofed-release-guest` package is installed and you intend to upgrade to
`oracle-rdma-release` or `oracle-rdma-release-guest` version
0.18.1-1 or above, you must manually remove development packages that were installed for OFED
before performing the upgrade or installation of the `oracle-rdma-release` or
`oracle-rdma-release-guest` package:

```
sudo /bin/rpm -e --nodeps libibumad-devel libibverbs-devel librdmacm-devel libibmad-devel
sudo yum install oracle-rdma-release-guest
```

Note that these steps are only required for the transition from versions of the
`oracle-rdma-release` and `oracle-rdma-release-guest` packages
prior to 0.18.1-1 to version 0.18.1-1 or later; or for the transition from
`oracle-ofed-release` to `oracle-rdma-release` version
0.18.1-1 or later. These steps aren't required for upgrades after the packages are at version
0.18.1-1 or later.

If the system you have upgraded has the `oracle-rdma-release` or
`oracle-rdma-release-guest` package installed and if the package version is
version 0.31.0-1, then you can remove it because that package no longer serves any
purpose:

```
sudo yum remove oracle-rdma-release*
```


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.2/uek6.2-DriverModulesinUnbreakableEnterpriseKernelRelease6x8664.html -->

This appendix presents all of the driver modules and their version
information as shipped in the current version of UEK R6 (x86\_64).
This appendix is generated automatically. Note that driver versions
and available drivers may change in subsequent errata releases, but
the driver versions will always be the same or later than presented
here.

### `acpi` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `acpi_extlog` |  | Extended MCA Error Log Driver |
| `acpi_ipmi` |  | ACPI IPMI Opregion driver |
| `acpi_pad` |  | ACPI Processor Aggregator Driver |
| `acpi_tad` |  |  |
| `einj` |  | APEI Error INJection support |
| `erst-dbg` |  | APEI Error Record Serialization Table debug support |
| `dptf_power` |  | ACPI DPTF platform power driver |
| `ec_sys` |  | ACPI EC sysfs access driver |
| `nfit` |  |  |
| `sbs` |  | Smart Battery System ACPI interface driver |
| `sbshc` |  | ACPI SMBus HC driver |
| `video` |  | ACPI Video Driver |

### `ata` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `acard-ahci` | 1.0 | ACard AHCI SATA low-level driver |
| `ahci` | 3.0 | AHCI SATA low-level driver |
| `ahci_platform` |  | AHCI SATA platform driver |
| `ata_generic` | 0.2.15 | low-level driver for generic ATA |
| `ata_piix` | 2.13 | SCSI low-level driver for Intel PIIX/ICH ATA controllers |
| `libahci` |  | Common AHCI SATA low-level routines |
| `libahci_platform` |  | AHCI SATA platform library |
| `libata` | 3.00 | Library module for ATA devices |
| `pata_acpi` | 0.2.3 | SCSI low-level driver for ATA in ACPI mode |
| `pata_ali` | 0.7.8 | low-level driver for ALi PATA |
| `pata_amd` | 0.4.1 | low-level driver for AMD and Nvidia PATA IDE |
| `pata_artop` | 0.4.6 | SCSI low-level driver for ARTOP PATA |
| `pata_atiixp` | 0.4.6 | low-level driver for ATI IXP200/300/400 |
| `pata_atp867x` | 0.7.5 | low level driver for Artop/Acard 867x ATA controller |
| `pata_cmd64x` | 0.2.18 | low-level driver for CMD64x series PATA controllers |
| `pata_hpt366` | 0.6.11 | low-level driver for the Highpoint HPT366/368 |
| `pata_hpt37x` | 0.6.23 | low-level driver for the Highpoint HPT37x/30x |
| `pata_hpt3x2n` | 0.3.15 | low-level driver for the Highpoint HPT3xxN |
| `pata_hpt3x3` | 0.6.1 | low-level driver for the Highpoint HPT343/363 |
| `pata_it8213` | 0.0.3 | SCSI low-level driver for the ITE 8213 |
| `pata_it821x` | 0.4.2 | low-level driver for the IT8211/IT8212 IDE RAID controller |
| `pata_jmicron` | 0.1.5 | SCSI low-level driver for Jmicron PATA ports |
| `pata_marvell` | 0.1.6 | SCSI low-level driver for Marvell ATA in legacy mode |
| `pata_netcell` | 0.1.7 | SCSI low-level driver for Netcell PATA RAID |
| `pata_ninja32` | 0.1.5 | low-level driver for Ninja32 ATA |
| `pata_oldpiix` | 0.5.5 | SCSI low-level driver for early PIIX series controllers |
| `pata_pdc2027x` | 1.0 | libata driver module for Promise PDC20268 to PDC20277 |
| `pata_pdc202xx_old` | 0.4.3 | low-level driver for Promise 2024x and 20262-20267 |
| `pata_piccolo` | 0.0.1 | Low level driver for Toshiba Piccolo ATA |
| `pata_rdc` | 0.01 | SCSI low-level driver for RDC PATA controllers |
| `pata_sch` | 0.2 | SCSI low-level driver for Intel SCH PATA controllers |
| `pata_serverworks` | 0.4.3 | low-level driver for Serverworks OSB4/CSB5/CSB6 |
| `pata_sil680` | 0.4.9 | low-level driver for SI680 PATA |
| `pata_sis` | 0.5.2 | SCSI low-level driver for SiS ATA |
| `pata_via` | 0.3.4 | low-level driver for VIA PATA |
| `pdc_adma` | 1.0 | Pacific Digital Corporation ADMA low-level driver |
| `sata_inic162x` | 0.4 | low-level driver for Initio 162x SATA |
| `sata_mv` | 1.28 | SCSI low-level driver for Marvell SATA controllers |
| `sata_nv` | 3.5 | low-level driver for NVIDIA nForce SATA controller |
| `sata_promise` | 2.12 | Promise ATA TX2/TX4/TX4000 low-level driver |
| `sata_qstor` | 0.09 | Pacific Digital Corporation QStor SATA low-level driver |
| `sata_sil` | 2.4 | low-level driver for Silicon Image SATA controller |
| `sata_sil24` |  | Silicon Image 3124/3132 SATA low-level driver |
| `sata_sis` | 1.0 | low-level driver for Silicon Integrated Systems SATA controller |
| `sata_svw` | 2.3 | low-level driver for K2 SATA controller |
| `sata_sx4` | 0.12 | Promise SATA low-level driver |
| `sata_uli` | 1.3 | low-level driver for ULi Electronics SATA controller |
| `sata_via` | 2.6 | SCSI low-level driver for VIA SATA controllers |
| `sata_vsc` | 2.3 | low-level driver for Vitesse VSC7174 SATA controller |

### `atm` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `atmtcp` |  |  |

### `auxdisplay` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `cfag12864b` |  | cfag12864b LCD driver |
| `cfag12864bfb` |  | cfag12864b LCD framebuffer driver |
| `ks0108` |  | ks0108 LCD Controller driver |

### `base` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `regmap-i2c` |  |  |
| `regmap-spi` |  |  |

### `bcma` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `bcma` |  | Broadcom's specific AMBA driver |

### `block` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `aoe` | 85 | AoE block/char driver for 2.6.2 and newer 2.6 kernels |
| `brd` |  |  |
| `cryptoloop` |  | loop blockdevice transferfunction adaptor / CryptoAPI |
| `drbd` | 8.4.11 | drbd - Distributed Replicated Block Device v8.4.11 |
| `floppy` |  |  |
| `loop` |  |  |
| `mtip32xx` | 1.3.1 | Micron RealSSD PCIe Block Driver |
| `nbd` |  | Network Block Device |
| `null_blk` |  |  |
| `oracleasm` | 2.0.8 | Kernel driver backing the Generic Linux ASM Library. |
| `pktcdvd` |  | Packet writing layer for CD/DVD drives |
| `rbd` |  | RADOS Block Device (RBD) driver |
| `skd` |  | STEC s1120 PCIe SSD block driver |
| `sx8` | 1.0 | Promise SATA SX8 block driver |
| `umem` |  | Micro Memory(tm) PCI memory board block driver |
| `virtio_blk` |  | Virtio block driver |
| `xen-blkback` |  |  |
| `xen-blkfront` |  | Xen virtual block device frontend |
| `zram` |  | Compressed RAM Block Device |

### `bluetooth` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `ath3k` | 1.0 | Atheros AR30xx firmware driver |
| `bcm203x` | 1.2 | Broadcom Blutonium firmware driver ver 1.2 |
| `bfusb` | 1.2 | BlueFRITZ! USB driver ver 1.2 |
| `bpa10x` | 0.11 | Digianswer Bluetooth USB driver ver 0.11 |
| `btbcm` | 0.1 | Bluetooth support for Broadcom devices ver 0.1 |
| `btintel` | 0.1 | Bluetooth support for Intel devices ver 0.1 |
| `btmrvl` | 1.0 | Marvell Bluetooth driver ver 1.0 |
| `btmrvl_sdio` | 1.0 | Marvell BT-over-SDIO driver ver 1.0 |
| `btrtl` | 0.1 | Bluetooth support for Realtek devices ver 0.1 |
| `btsdio` | 0.1 | Generic Bluetooth SDIO driver ver 0.1 |
| `btusb` | 0.8 | Generic Bluetooth USB driver ver 0.8 |
| `hci_uart` | 2.3 | Bluetooth HCI UART driver ver 2.3 |
| `hci_vhci` | 1.5 | Bluetooth virtual HCI driver ver 1.5 |

### `cdrom` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `cdrom` |  |  |

### `char` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `hangcheck-timer` | 0.9.1 | Hangcheck-timer detects when the system has gone out to lunch past a certain margin. |
| `amd-rng` |  | H/W RNG driver for AMD chipsets |
| `intel-rng` |  | H/W RNG driver for Intel chipsets |
| `timeriomem-rng` |  | Timer IOMEM H/W RNG driver |
| `via-rng` |  | H/W RNG driver for VIA CPU with PadLock |
| `virtio-rng` |  | Virtio random number driver |
| `ipmi_devintf` |  | Linux device interface for the IPMI message handler. |
| `ipmi_msghandler` | 39.2 | Incoming and outgoing message routing for an IPMI interface. |
| `ipmi_poweroff` |  | IPMI Poweroff extension to sys\_reboot |
| `ipmi_si` |  | Interface to the IPMI driver for the KCS, SMIC, and BT system interfaces. |
| `ipmi_ssif` |  | IPMI driver for management controllers on a SMBus |
| `ipmi_watchdog` |  | watchdog timer based upon the IPMI interface. |
| `lp` |  |  |
| `ppdev` |  |  |
| `tlclk` |  |  |
| `tpm_st33zp24` | 1.3.0 | ST33ZP24 TPM 1.2 driver |
| `tpm_st33zp24_i2c` | 1.3.0 | STM TPM 1.2 I2C ST33 Driver |
| `tpm_atmel` | 2.0 | TPM Driver |
| `tpm_i2c_atmel` |  | Atmel TPM I2C Driver |
| `tpm_i2c_infineon` | 2.2.0 | TPM TIS I2C Infineon Driver |
| `tpm_i2c_nuvoton` |  | Nuvoton TPM I2C Driver |
| `tpm_infineon` | 1.9.2 | Driver for Infineon TPM SLD 9630 TT 1.1 / SLB 9635 TT 1.2 |
| `tpm_nsc` | 2.0 | TPM Driver |
| `uv_mmtimer` |  | SGI UV Memory Mapped RTC Timer |
| `virtio_console` |  | Virtio console driver |

### `cpufreq` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `acpi-cpufreq` |  | ACPI Processor P-States Driver |
| `amd_freq_sensitivity` |  | AMD frequency sensitivity feedback powersave bias for the ondemand governor. |
| `p4-clockmod` |  | cpufreq driver for Pentium(TM) 4/Xeon(TM) |
| `pcc-cpufreq` | 1.10.00 | Processor Clocking Control interface driver |
| `powernow-k8` |  | AMD Athlon 64 and Opteron processor frequency driver. |
| `speedstep-lib` |  | Library for Intel SpeedStep 1 or 2 cpufreq drivers. |

### `crypto` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `n5pf` | 1.2 | Cavium CNN55XX PF Driver1.2 |
| `ccp-crypto` | 1.0.0 | AMD Cryptographic Coprocessor crypto API support |
| `ccp` | 1.1.0 | AMD Secure Processor driver |
| `chcr` | 1.0.0.0 | Crypto Co-processor for Chelsio Terminator cards. |
| `padlock-aes` |  | VIA PadLock AES algorithm support |
| `padlock-sha` |  | VIA PadLock SHA1/SHA256 algorithms support. |
| `qat_c3xxx` | 0.6.0 | Intel(R) QuickAssist Technology |
| `qat_c3xxxvf` | 0.6.0 | Intel(R) QuickAssist Technology |
| `qat_c62x` | 0.6.0 | Intel(R) QuickAssist Technology |
| `qat_c62xvf` | 0.6.0 | Intel(R) QuickAssist Technology |
| `intel_qat` | 0.6.0 | Intel(R) QuickAssist Technology |
| `qat_dh895xcc` | 0.6.0 | Intel(R) QuickAssist Technology |
| `qat_dh895xccvf` | 0.6.0 | Intel(R) QuickAssist Technology |
| `virtio_crypto` |  | virtio crypto device driver |

### `dax` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `device_dax` |  |  |
| `dax_hmem` |  |  |
| `kmem` |  |  |
| `dax_pmem` |  |  |
| `dax_pmem_compat` |  |  |
| `dax_pmem_core` |  |  |

### `dca` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `dca` | 1.12.1 |  |

### `devfreq` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `governor_simpleondemand` |  |  |

### `dma` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `dw_dmac` |  | Synopsys DesignWare DMA Controller platform driver |
| `idma64` |  | iDMA64 core driver |
| `ioatdma` | 5.00 |  |

### `edac` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `amd64_edac_mod` |  | MC support for AMD64 memory controllers - 3.5.0 |
| `e752x_edac` |  | MC support for Intel e752x/3100 memory controllers |
| `edac_mce_amd` |  | AMD MCE decoder |
| `i10nm_edac` |  | MC Driver for Intel 10nm server processors |
| `i3000_edac` |  | MC support for Intel 3000 memory hub controllers |
| `i3200_edac` |  | MC support for Intel 3200 memory hub controllers |
| `i5000_edac` |  | MC Driver for Intel I5000 memory controllers - Ver: 2.0.12 |
| `i5100_edac` |  | MC Driver for Intel I5100 memory controllers |
| `i5400_edac` |  | MC Driver for Intel I5400 memory controllers - Ver: 1.0.0 |
| `i7300_edac` |  | MC Driver for Intel I7300 memory controllers - Ver: 1.0.0 |
| `i7core_edac` |  | MC Driver for Intel i7 Core memory controllers - Ver: 1.0.0 |
| `i82975x_edac` |  | MC support for Intel 82975 memory hub controllers |
| `ie31200_edac` |  | MC support for Intel Processor E31200 memory hub controllers |
| `pnd2_edac` |  | MC Driver for Intel SoC using Pondicherry memory controller |
| `sb_edac` |  | MC Driver for Intel Sandy Bridge and Ivy Bridge memory controllers - Ver: 1.1.2 |
| `skx_edac` |  | MC Driver for Intel Skylake server processors |
| `x38_edac` |  | MC support for Intel X38 memory hub controllers |

### `firewire` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `firewire-core` |  | Core IEEE1394 transaction logic |
| `firewire-net` |  | IP over IEEE1394 as per RFC 2734/3146 |
| `firewire-ohci` |  | Driver for PCI OHCI IEEE1394 controllers |
| `firewire-sbp2` |  | SCSI over IEEE1394 |

### `firmware` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `edd` | 0.16 | sysfs interface to BIOS EDD information |
| `iscsi_ibft` | 0.5.0 | sysfs interface to BIOS iBFT information |
| `qemu_fw_cfg` |  | QEMU fw\_cfg sysfs support |

### `gpio` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `gpio-amdpt` |  | AMD Promontory GPIO Driver |
| `gpio-generic` |  | Driver for basic memory-mapped GPIO controllers |
| `gpio-ich` |  | GPIO interface for Intel ICH series |
| `gpio-viperboard` |  | GPIO driver for Nano River Techs Viperboard |

### `gpu` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `amdgpu` |  | AMD GPU |
| `ast` |  | AST |
| `bochs-drm` |  |  |
| `cirrus` |  |  |
| `drm` |  | DRM shared core routines DRM bridge infrastructure DRM panel infrastructure |
| `drm_kms_helper` |  | DRM KMS helper |
| `drm_vram_helper` |  | DRM VRAM memory-management helpers |
| `gma500_gfx` |  | DRM driver for the Intel GMA500, GMA600, GMA3600, GMA3650 |
| `ch7006` |  | Chrontel ch7006 TV encoder driver |
| `sil164` |  | Silicon Image sil164 TMDS transmitter driver |
| `tda998x` |  | NXP Semiconductors TDA998X HDMI Encoder |
| `i915` |  | Intel Graphics |
| `mgag200` |  | MGA G200 SE |
| `nouveau` |  | nVidia Riva/TNT/GeForce/Quadro/Tesla/Tegra K1+ |
| `qxl` |  | RH QXL |
| `radeon` |  | ATI Radeon |
| `gpu-sched` |  | DRM GPU scheduler |
| `ttm` |  | TTM memory manager subsystem (for DRM device) |
| `udl` |  |  |
| `vgem` |  | Virtual GEM provider |
| `virtio-gpu` |  | Virtio GPU driver |
| `vkms` |  | Virtual Kernel Mode Setting |
| `vmwgfx` | 2.15.0.0 | Standalone drm driver for the VMware SVGA device |

### `hid` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `hid-alps` |  | ALPS HID driver |
| `hid-appleir` |  | HID Apple IR remote controls |
| `hid-asus` |  | Asus HID Keyboard and TouchPad |
| `hid-aureal` |  |  |
| `hid-axff` |  | Force feedback support for ACRUX game controllers |
| `hid-betopff` |  |  |
| `hid-cmedia` |  | CM6533 HID jack controls |
| `hid-corsair` |  | HID driver for Corsair devices |
| `hid-cp2112` |  | Silicon Labs HID USB to SMBus master bridge |
| `hid-dr` |  |  |
| `hid-elan` |  | Driver for HID ELAN Touchpads |
| `hid-elecom` |  |  |
| `hid-elo` |  |  |
| `hid-emsff` |  |  |
| `hid-gaff` |  |  |
| `hid-gembird` |  | HID Gembird joypad driver |
| `hid-gfrm` |  | Google Fiber TV Box remote control driver |
| `hid-gt683r` |  | MSI GT683R led driver |
| `hid-gyration` |  |  |
| `hid-holtek-kbd` |  |  |
| `hid-holtek-mouse` |  |  |
| `hid-holtekff` |  | Force feedback support for Holtek On Line Grip based devices |
| `hid-hyperv` |  | Microsoft Hyper-V Synthetic HID Driver |
| `hid-icade` |  | ION iCade input driver |
| `hid-ite` |  |  |
| `hid-jabra` |  | Jabra USB HID Driver |
| `hid-keytouch` |  |  |
| `hid-kye` |  |  |
| `hid-lcpower` |  |  |
| `hid-led` |  | Simple USB RGB LED driver |
| `hid-lenovo` |  |  |
| `hid-logitech-dj` |  |  |
| `hid-logitech-hidpp` |  |  |
| `hid-multitouch` |  | HID multitouch panels |
| `hid-nti` |  | HID driver for Network Technologies USB-SUN keyboard adapter |
| `hid-ortek` |  |  |
| `hid-penmount` |  | PenMount HID TouchScreen driver |
| `hid-petalynx` |  |  |
| `hid-picolcd` |  | Minibox graphics PicoLCD Driver |
| `hid-pl` |  |  |
| `hid-primax` |  |  |
| `hid-prodikeys` |  |  |
| `hid-rmi` |  | RMI HID driver |
| `hid-roccat-arvo` |  | USB Roccat Arvo driver |
| `hid-roccat-common` |  | USB Roccat common driver |
| `hid-roccat-isku` |  | USB Roccat Isku/FX driver |
| `hid-roccat-kone` |  | USB Roccat Kone driver |
| `hid-roccat-koneplus` |  | USB Roccat Kone[+]/XTD driver |
| `hid-roccat-konepure` |  | USB Roccat KonePure/Optical driver |
| `hid-roccat-kovaplus` |  | USB Roccat Kova[+] driver |
| `hid-roccat-lua` |  | USB Roccat Lua driver |
| `hid-roccat-pyra` |  | USB Roccat Pyra driver |
| `hid-roccat-ryos` |  | USB Roccat Ryos MK/Glow/Pro driver |
| `hid-roccat-savu` |  | USB Roccat Savu driver |
| `hid-roccat` |  | USB Roccat char device |
| `hid-saitek` |  |  |
| `hid-samsung` |  |  |
| `hid-sjoy` |  |  |
| `hid-sony` |  |  |
| `hid-speedlink` |  |  |
| `hid-steelseries` |  |  |
| `hid-sunplus` |  |  |
| `hid-tivo` |  |  |
| `hid-tmff` |  |  |
| `hid-topseed` |  |  |
| `hid-twinhan` |  |  |
| `hid-uclogic` |  |  |
| `hid-waltop` |  |  |
| `hid-wiimote` |  | Driver for Nintendo Wii / Wii U peripherals |
| `hid-xinmo` |  |  |
| `hid-zpff` |  |  |
| `hid-zydacron` |  |  |
| `i2c-hid` |  | HID over I2C core driver |
| `uhid` |  | User-space I/O driver support for HID subsystem |
| `wacom` | v2.00 | USB Wacom tablet driver |

### `hv` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `hv_balloon` |  | Hyper-V Balloon |
| `hv_utils` |  | Hyper-V Utilities |
| `hv_vmbus` |  | Microsoft Hyper-V VMBus Driver |

### `hwmon` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `abituguru` |  | Abit uGuru Sensor device |
| `abituguru3` |  | Abit uGuru3 Sensor device |
| `acpi_power_meter` |  | ACPI 4.0 power meter driver |
| `ad7414` |  | AD7414 driver |
| `ad7418` | 0.4 | AD7416/17/18 driver |
| `adc128d818` |  | Driver for ADC128D818 |
| `adm1021` |  | adm1021 driver |
| `adm1025` |  | ADM1025 driver |
| `adm1026` |  | ADM1026 driver |
| `adm1029` |  | adm1029 driver |
| `adm1031` |  | ADM1031/ADM1030 driver |
| `adm9240` |  | ADM9240/DS1780/LM81 driver |
| `ads7828` |  | Driver for TI ADS7828 A/D converter and compatibles |
| `adt7410` |  | ADT7410/AD7420 driver |
| `adt7411` |  | ADT7411 driver |
| `adt7462` |  | ADT7462 driver |
| `adt7470` |  | ADT7470 driver |
| `adt7475` |  | adt7475 driver |
| `adt7x10` |  | ADT7410/ADT7420, ADT7310/ADT7320 common code |
| `amc6821` |  | Texas Instruments amc6821 hwmon driver |
| `applesmc` |  | Apple SMC |
| `asb100` |  | ASB100 Bach driver |
| `asc7621` |  | Andigilog aSC7621 and aSC7621a driver |
| `asus_atk0110` |  |  |
| `atxp1` | 0.6.3 | System voltages control via Attansic ATXP1 |
| `coretemp` |  | Intel Core temperature monitor |
| `dell-smm-hwmon` |  | Dell laptop SMM BIOS hwmon driver |
| `dme1737` |  | DME1737 sensors |
| `ds1621` |  | DS1621 driver |
| `ds620` |  | DS620 driver |
| `emc1403` |  | emc1403 Thermal Driver |
| `emc2103` |  | SMSC EMC2103 hwmon driver |
| `emc6w201` |  | SMSC EMC6W201 hardware monitoring driver |
| `f71805f` |  | F71805F/F71872F hardware monitoring driver |
| `f71882fg` |  | F71882FG Hardware Monitoring Driver |
| `f75375s` |  | F75373/F75375/F75387 hardware monitoring driver |
| `fam15h_power` |  | AMD Family 15h CPU processor power monitor |
| `fschmd` |  | FSC Poseidon, Hermes, Scylla, Heracles, Heimdall, Hades and Syleus driver |
| `g760a` |  | GMT G760A driver |
| `g762` |  | GMT G762/G763 driver |
| `gl518sm` |  | GL518SM driver |
| `gl520sm` |  | GL520SM driver |
| `hih6130` |  | Honeywell HIH-6130 humidity and temperature sensor driver |
| `hwmon-vid` |  | hwmon-vid driver |
| `i5500_temp` |  | Intel 5500/5520/X58 chipset thermal sensor driver |
| `i5k_amb` |  | Intel 5000 chipset FB-DIMM AMB temperature sensor |
| `ibmaem` |  | IBM AEM power/temp/energy sensor driver |
| `ibmpex` |  | IBM PowerExecutive power/temperature sensor driver |
| `ina209` |  | INA209 driver |
| `ina2xx` |  | ina2xx driver |
| `it87` |  | IT8705F/IT871xF/IT872xF hardware monitoring driver |
| `jc42` |  | JC42 driver |
| `k10temp` |  | AMD Family 10h+ CPU core temperature monitor |
| `k8temp` |  | AMD K8 core temperature monitor |
| `lineage-pem` |  | Lineage CPL PEM hardware monitoring driver |
| `lm63` |  | LM63 driver |
| `lm73` |  | LM73 driver |
| `lm75` |  | LM75 driver |
| `lm77` |  | LM77 driver |
| `lm78` |  | LM78/LM79 driver |
| `lm80` |  | LM80 driver |
| `lm83` |  | LM83 driver |
| `lm85` |  | LM85-B, LM85-C driver |
| `lm87` |  | LM87 driver |
| `lm90` |  | LM90/ADM1032 driver |
| `lm92` |  | LM92/MAX6635 driver |
| `lm93` |  | LM93 driver |
| `lm95234` |  | LM95233/LM95234 sensor driver |
| `lm95241` |  | LM95231/LM95241 sensor driver |
| `lm95245` |  | LM95235/LM95245 sensor driver |
| `ltc2945` |  | LTC2945 driver |
| `ltc4151` |  | LTC4151 driver |
| `ltc4215` |  | LTC4215 driver |
| `ltc4222` |  | LTC4222 driver |
| `ltc4245` |  | LTC4245 driver |
| `ltc4260` |  | LTC4260 driver |
| `ltc4261` |  | LTC4261 driver |
| `max16065` |  | MAX16065 driver |
| `max1619` |  | MAX1619 sensor driver |
| `max1668` |  | MAX1668 remote temperature sensor driver |
| `max197` |  | Maxim MAX197 A/D Converter driver |
| `max6639` |  | max6639 driver |
| `max6642` |  | MAX6642 sensor driver |
| `max6650` |  | MAX6650 sensor driver |
| `max6697` |  | MAX6697 temperature sensor driver |
| `mcp3021` |  | Microchip MCP3021/MCP3221 driver |
| `nct6683` |  | NCT6683D driver |
| `nct6775` |  | Driver for NCT6775F and compatible chips |
| `ntc_thermistor` |  | NTC Thermistor Driver |
| `opbmc` | 1.0 | Oracle Pilot BMC |
| `pc87360` |  | PC8736x hardware monitor |
| `pc87427` |  | PC87427 hardware monitoring driver |
| `pcf8591` |  | PCF8591 driver |
| `adm1275` |  | PMBus driver for Analog Devices ADM1275 and compatibles |
| `lm25066` |  | PMBus driver for LM25066 and compatible chips |
| `ltc2978` |  | PMBus driver for LTC2978 and compatible chips |
| `max16064` |  | PMBus driver for Maxim MAX16064 |
| `max34440` |  | PMBus driver for Maxim MAX34440/MAX34441 |
| `max8688` |  | PMBus driver for Maxim MAX8688 |
| `pmbus` |  | Generic PMBus driver |
| `pmbus_core` |  | PMBus core driver |
| `tps40422` |  | PMBus driver for TI TPS40422 |
| `ucd9000` |  | PMBus driver for TI UCD90xxx |
| `ucd9200` |  | PMBus driver for TI UCD922x, UCD924x |
| `zl6100` |  | PMBus driver for ZL6100 and compatibles |
| `powr1220` |  | POWR1220 driver |
| `sch5627` |  | SMSC SCH5627 Hardware Monitoring Driver |
| `sch5636` |  | SMSC SCH5636 Hardware Monitoring Driver |
| `sch56xx-common` |  | SMSC SCH56xx Hardware Monitoring Common Code |
| `sht15` |  | Sensirion SHT15 temperature and humidity sensor driver |
| `sht21` |  | Sensirion SHT21 humidity and temperature sensor driver |
| `shtc1` |  | Sensirion SHTC1 humidity and temperature sensor driver |
| `sis5595` |  | SiS 5595 Sensor device |
| `smm665` |  | SMM665 driver |
| `smsc47b397` |  | SMSC LPC47B397 driver |
| `smsc47m1` |  | SMSC LPC47M1xx fan sensors driver |
| `smsc47m192` |  | SMSC47M192 driver |
| `thmc50` |  | THMC50 driver |
| `tmp102` |  | Texas Instruments TMP102 temperature sensor driver |
| `tmp103` |  | Texas Instruments TMP103 temperature sensor driver |
| `tmp401` |  | Texas Instruments TMP401 temperature sensor driver |
| `tmp421` |  | Texas Instruments TMP421/422/423/441/442 temperature sensor driver |
| `via-cputemp` |  | VIA CPU temperature monitor |
| `via686a` |  | VIA 686A Sensor device |
| `vt1211` |  | VT1211 sensors |
| `vt8231` |  | VT8231 sensors |
| `w83627ehf` |  | W83627EHF driver |
| `w83627hf` |  | W83627HF driver |
| `w83781d` |  | W83781D driver |
| `w83791d` |  | W83791D driver |
| `w83792d` |  | W83792AD/D driver for linux-2.6 |
| `w83793` |  | w83793 driver |
| `w83795` |  | W83795G/ADG hardware monitoring driver |
| `w83l785ts` |  | W83L785TS-S driver |
| `w83l786ng` |  | w83l786ng driver |

### `i2c` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `i2c-algo-bit` |  | I2C-Bus bit-banging algorithm |
| `i2c-algo-pca` |  | I2C-Bus PCA9564/PCA9665 algorithm |
| `i2c-amd756-s4882` |  | S4882 SMBus multiplexing |
| `i2c-amd756` |  | AMD756/766/768/8111 and nVidia nForce SMBus driver |
| `i2c-amd8111` |  | AMD8111 SMBus 2.0 driver |
| `i2c-cbus-gpio` |  | CBUS I2C driver |
| `i2c-designware-core` |  | Synopsys DesignWare I2C bus adapter core Synopsys DesignWare I2C bus master adapter |
| `i2c-designware-pci` |  | Synopsys DesignWare PCI I2C bus adapter |
| `i2c-designware-platform` |  | Synopsys DesignWare I2C bus adapter |
| `i2c-diolan-u2c` |  | i2c-diolan-u2c driver |
| `i2c-gpio` |  | Platform-independent bitbanging I2C driver |
| `i2c-i801` |  | I801 SMBus driver |
| `i2c-isch` |  | Intel SCH SMBus driver |
| `i2c-ismt` |  | Intel SMBus Message Transport (iSMT) driver |
| `i2c-mlxcpld` |  | Mellanox I2C-CPLD controller driver |
| `i2c-nforce2-s4985` |  | S4985 SMBus multiplexing |
| `i2c-nforce2` |  | nForce2/3/4/5xx SMBus driver |
| `i2c-ocores` |  | OpenCores I2C bus driver |
| `i2c-parport-light` |  | I2C bus over parallel port (light) |
| `i2c-parport` |  | I2C bus over parallel port |
| `i2c-pca-platform` |  | I2C-PCA9564/PCA9665 platform driver |
| `i2c-piix4` |  | PIIX4 SMBus driver |
| `i2c-robotfuzz-osif` |  | RobotFuzz OSIF driver |
| `i2c-scmi` |  | ACPI SMBus CMI driver |
| `i2c-simtec` |  | Simtec Generic I2C Bus driver |
| `i2c-sis5595` |  | SIS5595 SMBus driver |
| `i2c-sis630` |  | SIS630 SMBus driver |
| `i2c-sis96x` |  | SiS96x SMBus driver |
| `i2c-taos-evm` |  | TAOS evaluation module driver |
| `i2c-tiny-usb` |  | i2c-tiny-usb driver v1.0 |
| `i2c-via` |  | i2c for Via vt82c586b southbridge |
| `i2c-viapro` |  | vt82c596 SMBus driver |
| `i2c-viperboard` |  | I2C master driver for Nano River Techs Viperboard |
| `i2c-xiic` |  | Xilinx I2C bus driver |
| `i2c-dev` |  | I2C /dev entries driver |
| `i2c-mux` |  | I2C driver for multiplexed I2C busses |
| `i2c-smbus` |  | SMBus protocol extensions support |
| `i2c-stub` |  | I2C stub driver |
| `i2c-mux-mlxcpld` |  | Mellanox I2C-CPLD-MUX driver |

### `iio` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `industrialio` |  | Industrial I/O core |

### `infiniband` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `ib_cm` |  | InfiniBand CM |
| `ib_core` |  | core kernel InfiniBand API |
| `ib_umad` |  | InfiniBand userspace MAD packet access |
| `ib_uverbs` |  | InfiniBand userspace verbs access |
| `iw_cm` |  | iWARP CM |
| `rdma_cm` |  | Generic RDMA CM Agent |
| `rdma_ucm` |  | RDMA Userspace Connection Manager Access |
| `resilient_rdmaip` |  | Resilient RDMA IP |
| `bnxt_re` |  | Broadcom NetXtreme-C/E RoCE Driver Driver |
| `iw_cxgb3` |  | Chelsio T3 RDMA Driver |
| `iw_cxgb4` |  | Chelsio T4/T5 RDMA Driver |
| `hfi1` |  | Intel Omni-Path Architecture driver |
| `i40iw` |  | Intel(R) Ethernet Connection X722 iWARP RDMA Driver |
| `mlx4_ib` |  | Mellanox ConnectX HCA InfiniBand driver |
| `mlx5_ib` |  | Mellanox Connect-IB HCA IB driver |
| `ib_mthca` |  | Mellanox InfiniBand HCA low-level driver |
| `ocrdma` |  | Emulex OneConnect RoCE Driver 11.0.0.0 |
| `qedr` |  | QLogic 40G/100G ROCE Driver |
| `ib_qib` |  | Intel IB driver |
| `usnic_verbs` |  | Cisco VIC (usNIC) Verbs Driver |
| `vmw_pvrdma` |  | VMware Paravirtual RDMA driver |
| `rdmavt` |  | RDMA Verbs Transport Library |
| `rdma_rxe` |  | Soft RDMA transport |
| `ib_ipoib` |  | IP-over-InfiniBand net driver |
| `ib_iser` |  | iSER (iSCSI Extensions for RDMA) Datamover |
| `ib_isert` |  | iSER-Target for mainline target infrastructure |
| `opa_vnic` |  | Intel OPA Virtual Network driver |
| `ib_srp` |  | InfiniBand SCSI RDMA Protocol initiator |
| `ib_srpt` |  | SCSI RDMA Protocol target driver |

### `input` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `input-polldev` |  | Generic implementation of a polled input device |
| `joydev` |  | Joystick device interfaces |
| `gpio_keys` |  | Keyboard driver for GPIOs |
| `gpio_keys_polled` |  | Polled GPIO Buttons driver |
| `matrix_keypad` |  | GPIO Driven Matrix Keypad Driver |
| `mcs_touchkey` |  | Touchkey driver for MELFAS MCS5000/5080 controller |
| `qt1070` |  | Driver for AT42QT1070 QTouch sensor |
| `qt2160` |  | Driver for AT42QT2160 Touch Sensor |
| `tca6416-keypad` |  | Keypad driver over tca6146 IO expander |
| `matrix-keymap` |  |  |
| `apanel` |  | Fujitsu Application Panel driver |
| `ati_remote2` |  | ATI/Philips USB RF remote driver |
| `atlas_btns` |  | Atlas button driver |
| `cm109` |  | CM109 phone driver |
| `gp2ap002a00f` |  | Sharp GP2AP002A00F I2C Proximity/Opto sensor driver |
| `keyspan_remote` |  | Driver for the USB Keyspan remote control. |
| `pcspkr` |  | PC Speaker beeper driver |
| `powermate` |  | Griffin Technology, Inc PowerMate driver |
| `rotary_encoder` |  | GPIO rotary encoder driver |
| `uinput` |  | User level driver support for input subsystem |
| `xen-kbdfront` |  | Xen virtual keyboard/pointer device frontend |
| `yealink` |  | Yealink phone driver |
| `appletouch` |  | Apple PowerBook and MacBook USB touchpad driver |
| `bcm5974` |  | Apple USB BCM5974 multitouch driver |
| `cyapatp` |  | Cypress APA I2C Trackpad Driver |
| `elan_i2c` |  | Elan I2C/SMBus Touchpad driver |
| `gpio_mouse` |  | GPIO mouse driver |
| `sermouse` |  | Serial mouse driver |
| `synaptics_i2c` |  | Synaptics I2C touchpad driver |
| `synaptics_usb` |  | Synaptics USB device driver |
| `vsxxxaa` |  | Driver for DEC VSXXX-AA and -GA mice and VSXXX-AB tablet |
| `rmi_core` |  | RMI bus RMI F03 module |
| `altera_ps2` |  | Altera University Program PS2 controller driver |
| `arc_ps2` |  | ARC PS/2 Driver |
| `hyperv-keyboard` |  | Microsoft Hyper-V Synthetic Keyboard Driver |
| `ps2mult` |  | TQC PS/2 Multiplexer driver |
| `serio_raw` |  | Raw serio driver |
| `sparse-keymap` |  | Generic support for sparse keymaps |
| `acecad` |  | USB Acecad Flair tablet driver |
| `aiptek` |  | Aiptek HyperPen USB Tablet Driver |
| `gtco` |  | GTCO digitizer USB driver |
| `hanwang` |  | USB Hanwang tablet driver |
| `kbtab` |  | USB KB Gear JamStudio Tablet driver |
| `wacom_serial4` |  | Wacom protocol 4 serial tablet driver |
| `ad7879-i2c` |  | AD7879(-1) touchscreen I2C bus driver |
| `ad7879` |  | AD7879(-1) touchscreen Driver |
| `atmel_mxt_ts` |  | Atmel maXTouch Touchscreen driver |
| `bu21013_ts` |  | bu21013 touch screen controller driver |
| `cy8ctmg110_ts` |  | cy8ctmg110 TouchScreen Driver |
| `dynapro` |  | Dynapro serial touchscreen driver |
| `eeti_ts` |  | EETI Touchscreen driver |
| `elo` |  | Elo serial touchscreen driver |
| `fujitsu_ts` |  | Fujitsu serial touchscreen driver |
| `gunze` |  | Gunze AHL-51S touchscreen driver |
| `hampshire` |  | Hampshire serial touchscreen driver |
| `inexio` |  | iNexio serial touchscreen driver |
| `mk712` |  | ICS MicroClock MK712 TouchScreen driver |
| `mtouch` |  | MicroTouch serial touchscreen driver |
| `penmount` |  | PenMount serial touchscreen driver |
| `touchit213` |  | Sahara TouchIT-213 serial touchscreen driver |
| `touchright` |  | Touchright serial touchscreen driver |
| `touchwin` |  | Touchwindow serial touchscreen driver |
| `tsc2007` |  | TSC2007 TouchScreen Driver |
| `usbtouchscreen` |  | USB Touchscreen Driver |
| `wacom_i2c` |  | WACOM EMR I2C Driver |
| `wacom_w8001` |  | Wacom W8001 serial touchscreen driver |

### `isdn` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `capi` |  | CAPI4Linux: Userspace /dev/capi20 interface |
| `kernelcapi` |  | CAPI4Linux: kernel CAPI layer |
| `avmfritz` | 2.3 |  |
| `hfcmulti` | 2.03 |  |
| `hfcpci` |  |  |
| `hfcsusb` |  |  |
| `isdnhdlc` |  | General purpose ISDN HDLC decoder |
| `mISDNinfineon` | 1.0 |  |
| `mISDNipac` | 2.0 |  |
| `mISDNisar` | 2.1 |  |
| `netjet` | 2.0 |  |
| `speedfax` | 2.0 |  |
| `w6692` | 2.0 |  |
| `l1oip` |  |  |
| `mISDN_core` |  |  |
| `mISDN_dsp` |  |  |

### `leds` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `leds-blinkm` |  | BlinkM RGB LED driver |
| `leds-clevo-mail` |  | Clevo mail LED driver |
| `leds-lm3530` |  | Back Light driver for LM3530 |
| `leds-lp3944` |  | LP3944 Fun Light Chip |
| `leds-lp5521` |  | LP5521 LED engine |
| `leds-lp5523` |  | LP5523 LED engine |
| `leds-lp5562` |  | Texas Instruments LP5562 LED Driver |
| `leds-lp55xx-common` |  | LP55xx Common Driver |
| `leds-lp8501` |  | Texas Instruments LP8501 LED driver |
| `leds-mlxcpld` |  | Mellanox board LED driver |
| `leds-ss4200` |  | Intel NAS/Home Server ICH7 GPIO Driver |
| `ledtrig-audio` |  | LED trigger for audio mute control |
| `ledtrig-backlight` |  | Backlight emulation LED trigger |
| `ledtrig-camera` |  | LED Trigger for Camera Flash/Torch Control |
| `ledtrig-default-on` |  | Default-ON LED trigger |
| `ledtrig-gpio` |  | GPIO LED trigger |
| `ledtrig-heartbeat` |  | Heartbeat LED trigger |
| `ledtrig-oneshot` |  | One-shot LED trigger |
| `ledtrig-timer` |  | Timer LED trigger |
| `ledtrig-transient` |  | Transient LED trigger |

### `md` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `dm-bio-prison` |  | device-mapper bio prison |
| `dm-bufio` |  | device-mapper buffered I/O library |
| `dm-cache-smq` |  | smq cache policy |
| `dm-cache` |  | device-mapper cache target |
| `dm-crypt` |  | device-mapper target for transparent encryption / decryption |
| `dm-delay` |  | device-mapper delay target |
| `dm-era` |  | device-mapper era target |
| `dm-flakey` |  | device-mapper flakey target |
| `dm-integrity` |  | device-mapper target for integrity tags extension |
| `dm-log-userspace` |  | device-mapper userspace dirty log link |
| `dm-log-writes` |  | device-mapper log writes target |
| `dm-log` |  | device-mapper dirty region log |
| `dm-mirror` |  | device-mapper mirror target |
| `dm-mod` |  | device-mapper driver |
| `dm-multipath` |  | device-mapper multipath target |
| `dm-queue-length` |  | (C) Copyright IBM Corp. 2004,2005 All Rights Reserved. device-mapper path selector to balance the number of in-flight I/Os |
| `dm-raid` |  | device-mapper raid0/1/10/4/5/6 target |
| `dm-region-hash` |  | device-mapper region hash |
| `dm-round-robin` |  | device-mapper round-robin multipath path selector |
| `dm-service-time` |  | device-mapper throughput oriented path selector |
| `dm-snapshot` |  | device-mapper snapshot target |
| `dm-switch` |  | device-mapper dynamic path switching target |
| `dm-thin-pool` |  | device-mapper thin provisioning target |
| `dm-verity` |  | device-mapper target for transparent disk integrity checking |
| `dm-writecache` |  | device-mapper writecache target |
| `dm-zero` |  | device-mapper dummy target returning zeros |
| `dm-zoned` |  | device-mapper target for zoned block devices |
| `faulty` |  | Fault injection personality for MD |
| `linear` |  | Linear device concatenation personality for MD |
| `md-cluster` |  | Clustering support for MD |
| `dm-persistent-data` |  | Immutable metadata library for dm |
| `raid0` |  | RAID0 (striping) personality for MD |
| `raid1` |  | RAID1 (mirroring) personality for MD |
| `raid10` |  | RAID10 (striped mirror) personality for MD |
| `raid456` |  | RAID4/5/6 (striping with parity) personality for MD |

### `media` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `b2c2-flexcop` |  | B2C2 FlexcopII/II(b)/III digital TV receiver chip |
| `cx2341x` |  | cx23415/6/8 driver |
| `cypress_firmware` |  | Cypress firmware download |
| `saa7146` |  | driver for generic saa7146-based hardware |
| `saa7146_vv` |  | video4linux driver for saa7146-based hardware |
| `smsdvb` |  | SMS DVB subsystem adaptation module |
| `smsmdtv` |  | Siano MDTV Core module |
| `tveeprom` |  | i2c Hauppauge eeprom decoder driver |
| `videobuf2-common` |  | Media buffer core framework |
| `videobuf2-dma-sg` |  | dma scatter/gather memory handling routines for videobuf2 |
| `videobuf2-dvb` |  |  |
| `videobuf2-memops` |  | common memory handling routines for videobuf2 |
| `videobuf2-v4l2` |  | Driver helper framework for Video for Linux 2 |
| `videobuf2-vmalloc` |  | vmalloc memory handling routines for videobuf2 |
| `dvb-core` |  | DVB Core Driver |
| `a8293` |  | Allegro A8293 SEC driver |
| `af9013` |  | Afatech AF9013 DVB-T demodulator driver |
| `af9033` |  | Afatech AF9033 DVB-T demodulator driver |
| `atbm8830` |  | AltoBeam ATBM8830/8831 GB20600 demodulator driver |
| `au8522_common` |  | Auvitek AU8522 QAM-B/ATSC Demodulator driver |
| `au8522_decoder` |  |  |
| `au8522_dig` |  | Auvitek AU8522 QAM-B/ATSC Demodulator driver |
| `bcm3510` |  | Broadcom BCM3510 ATSC (8VSB/16VSB & ITU J83 AnnexB FEC QAM64/256) demodulator driver |
| `cx22700` |  | Conexant CX22700 DVB-T Demodulator driver |
| `cx22702` |  | Conexant CX22702 DVB-T Demodulator driver |
| `cx24110` |  | Conexant CX24110 DVB-S Demodulator driver |
| `cx24113` |  | DVB Frontend module for Conexant CX24113/CX24128hardware |
| `cx24116` |  | DVB Frontend module for Conexant cx24116/cx24118 hardware |
| `cx24117` | 1.1 | DVB Frontend module for Conexant cx24117/cx24132 hardware |
| `cx24120` |  | DVB Frontend module for Conexant CX24120/CX24118 hardware |
| `cx24123` |  | DVB Frontend module for Conexant CX24123/CX24109/CX24113 hardware |
| `cxd2099` |  | Sony CXD2099AR Common Interface controller driver |
| `cxd2820r` |  | Sony CXD2820R demodulator driver |
| `cxd2841er` |  | Sony CXD2837/38/41/43/54ER DVB-C/C2/T/T2/S/S2 demodulator driver |
| `dib0070` |  | Driver for the DiBcom 0070 base-band RF Tuner |
| `dib0090` |  | Driver for the DiBcom 0090 base-band RF Tuner |
| `dib3000mb` |  | DiBcom 3000M-B DVB-T demodulator |
| `dib3000mc` |  | Driver for the DiBcom 3000MC/P COFDM demodulator |
| `dib7000m` |  | Driver for the DiBcom 7000MA/MB/PA/PB/MC COFDM demodulator |
| `dib7000p` |  | Driver for the DiBcom 7000PC COFDM demodulator |
| `dib8000` |  | Driver for the DiBcom 8000 ISDB-T demodulator |
| `dibx000_common` |  | Common function the DiBcom demodulator family |
| `drx39xyj` |  | Micronas DRX39xxj Frontend |
| `drxd` |  | DRXD driver |
| `drxk` |  | DRX-K driver |
| `ds3000` |  | DVB Frontend module for Montage Technology DS3000 hardware |
| `dvb-pll` |  | dvb pll library |
| `dvb_dummy_fe` |  | DVB DUMMY Frontend |
| `ec100` |  | E3C EC100 DVB-T demodulator driver |
| `gp8psk-fe` | 1.1 | Frontend Driver for Genpix DVB-S |
| `isl6405` |  | Driver for lnb supply and control ic isl6405 |
| `isl6421` |  | Driver for lnb supply and control ic isl6421 |
| `isl6423` |  | ISL6423 SEC |
| `itd1000` |  | Integrant ITD1000 driver |
| `ix2505v` |  | DVB IX2505V tuner driver |
| `l64781` |  | LSI L64781 DVB-T Demodulator driver |
| `lg2160` | 0.3 | LG Electronics LG216x ATSC/MH Demodulator Driver |
| `lgdt3305` | 0.2 | LG Electronics LGDT3304/5 ATSC/QAM-B Demodulator Driver |
| `lgdt3306a` | 0.2 | LG Electronics LGDT3306A ATSC/QAM-B Demodulator Driver |
| `lgdt330x` |  | LGDT330X (ATSC 8VSB & ITU-T J.83 AnnexB 64/256 QAM) Demodulator Driver |
| `lgs8gxx` |  | Legend Silicon LGS8913/LGS8GXX DMB-TH demodulator driver |
| `lnbh25` |  | ST LNBH25 driver |
| `lnbp21` |  | Driver for lnb supply and control ic lnbp21, lnbh24 |
| `lnbp22` |  | Driver for lnb supply and control ic lnbp22 |
| `m88ds3103` |  | Montage Technology M88DS3103 DVB-S/S2 demodulator driver |
| `m88rs2000` | 1.13 | M88RS2000 DVB-S Demodulator driver |
| `mb86a16` |  |  |
| `mb86a20s` |  | DVB Frontend module for Fujitsu mb86A20s hardware |
| `mn88472` |  | Panasonic MN88472 DVB-T/T2/C demodulator driver |
| `mn88473` |  | Panasonic MN88473 DVB-T/T2/C demodulator driver |
| `mt312` |  | Zarlink VP310/MT312/ZL10313 DVB-S Demodulator driver |
| `mt352` |  | Zarlink MT352 DVB-T Demodulator driver |
| `mxl5xx` |  | MaxLinear MxL5xx DVB-S/S2 tuner-demodulator driver |
| `nxt200x` |  | NXT200X (ATSC 8VSB & ITU-T J.83 AnnexB 64/256 QAM) Demodulator Driver |
| `nxt6000` |  | NxtWave NXT6000 DVB-T demodulator driver |
| `or51132` |  | OR51132 ATSC [pcHDTV HD-3000] (8VSB & ITU J83 AnnexB FEC QAM64/256) Demodulator Driver |
| `or51211` |  | Oren OR51211 VSB [pcHDTV HD-2000] Demodulator Driver |
| `rtl2830` |  | Realtek RTL2830 DVB-T demodulator driver |
| `rtl2832` |  | Realtek RTL2832 DVB-T demodulator driver |
| `s5h1409` |  | Samsung S5H1409 QAM-B/ATSC Demodulator driver |
| `s5h1411` |  | Samsung S5H1411 QAM-B/ATSC Demodulator driver |
| `s5h1420` |  | Samsung S5H1420/PnpNetwork PN1010 DVB-S Demodulator driver |
| `s921` |  | DVB Frontend module for Sharp S921 hardware |
| `si2165` |  | Silicon Labs Si2165 DVB-C/-T Demodulator driver |
| `si2168` |  | Silicon Labs Si2168 DVB-T/T2/C demodulator driver |
| `si21xx` |  | SL SI21XX DVB Demodulator driver |
| `sp2` |  | CIMaX SP2/HF CI driver |
| `sp8870` |  | Spase SP8870 DVB-T Demodulator driver |
| `sp887x` |  | Spase sp887x DVB-T demodulator driver |
| `stb0899` |  | STB0899 Multi-Std frontend |
| `stb6000` |  | DVB STB6000 driver |
| `stb6100` |  | STB6100 Silicon tuner |
| `stv0288` |  | ST STV0288 DVB Demodulator driver |
| `stv0297` |  | ST STV0297 DVB-C Demodulator driver |
| `stv0299` |  | ST STV0299 DVB Demodulator driver |
| `stv0367` |  | ST STV0367 DVB-C/T demodulator driver |
| `stv0900` |  | ST STV0900 frontend |
| `stv090x` |  | STV090x Multi-Std Broadcast frontend |
| `stv0910` |  | ST STV0910 multistandard frontend driver |
| `stv6110` |  | ST STV6110 driver |
| `stv6110x` |  | STV6110x Silicon tuner |
| `stv6111` |  | ST STV6111 satellite tuner driver |
| `tc90522` |  | Toshiba TC90522 frontend |
| `tda10021` |  | Philips TDA10021 DVB-C demodulator driver |
| `tda10023` |  | Philips TDA10023 DVB-C demodulator driver |
| `tda10048` |  | NXP TDA10048HN DVB-T Demodulator driver |
| `tda1004x` |  | Philips TDA10045H & TDA10046H DVB-T Demodulator |
| `tda10071` |  | NXP TDA10071 DVB-S/S2 demodulator driver |
| `tda10086` |  | Philips TDA10086 DVB-S Demodulator |
| `tda18271c2dd` |  | TDA18271C2 driver |
| `tda665x` |  | TDA665x driver |
| `tda8083` |  | Philips TDA8083 DVB-S Demodulator |
| `tda8261` |  | TDA8261 8PSK/QPSK Tuner |
| `tda826x` |  | DVB TDA826x driver |
| `ts2020` |  | Montage Technology TS2020 - Silicon tuner driver module |
| `tua6100` |  | DVB tua6100 driver |
| `ves1820` |  | VLSI VES1820 DVB-C Demodulator driver |
| `ves1x93` |  | VLSI VES1x93 DVB-S Demodulator driver |
| `zl10036` |  | DVB ZL10036 driver |
| `zl10039` |  | Zarlink ZL10039 DVB-S tuner driver |
| `zl10353` |  | Zarlink ZL10353 DVB-T demodulator driver |
| `firedtv` |  | FireDTV DVB Driver |
| `cs3308` |  | i2c device driver for cs3308 8-channel volume control |
| `cs5345` |  | i2c device driver for cs5345 Audio ADC |
| `cs53l32a` |  | i2c device driver for cs53l32a Audio ADC |
| `cx25840` |  | Conexant CX25840 audio/video decoder driver |
| `ir-kbd-i2c` |  | input driver for i2c IR remote controls |
| `m52790` |  | i2c device driver for m52790 A/V switch |
| `msp3400` |  | device driver for msp34xx TV sound processor |
| `mt9m111` |  | Micron/Aptina MT9M111/MT9M112/MT9M131 Camera driver |
| `saa6588` |  | v4l2 driver module for SAA6588 RDS decoder |
| `saa6752hs` |  | device driver for saa6752hs MPEG2 encoder |
| `saa7115` |  | Philips SAA7111/SAA7113/SAA7114/SAA7115/SAA7118 video decoder driver |
| `saa7127` |  | Philips SAA7127/9 video encoder driver |
| `saa717x` |  | Philips SAA717x audio/video decoder driver |
| `tda7432` |  | bttv driver for the tda7432 audio processor chip |
| `tvaudio` |  | device driver for various i2c TV sound decoder / audiomux chips |
| `upd64031a` |  | uPD64031A driver |
| `upd64083` |  | uPD64083 driver |
| `vp27smpx` |  | vp27smpx driver |
| `wm8739` |  | wm8739 driver |
| `wm8775` |  | wm8775 driver |
| `mc` |  | Device node registration for media drivers |
| `smssdio` |  | Siano SMS1xxx SDIO driver |
| `b2c2-flexcop-pci` |  | flexcop-pci |
| `bt878` |  |  |
| `bttv` | 0.9.19 | bttv - v4l/v4l2 driver module for bt848/878 based cards |
| `dst` |  | DST DVB-S/T/C/ATSC Combo Frontend driver |
| `dst_ca` |  | DST DVB-S/T/C Combo CA driver |
| `dvb-bt8xx` |  | Bt8xx based DVB adapter driver |
| `cx18-alsa` | 1.5.1 | CX23418 ALSA Interface |
| `cx18` | 1.5.1 | CX23418 driver |
| `altera-ci` |  | altera FPGA CI module |
| `cx23885` | 0.0.4 | v4l2 driver module for cx23885 based TV cards Driver for cx23885 based TV cards |
| `cx88-alsa` | 1.0.0 | ALSA driver module for cx2388x based TV cards |
| `cx88-blackbird` | 1.0.0 | driver for cx2388x/cx23416 based mpeg encoder cards |
| `cx88-dvb` | 1.0.0 | driver for cx2388x based DVB cards |
| `cx88-vp3054-i2c` |  | driver for cx2388x VP3054 design |
| `cx8800` | 1.0.0 | v4l2 driver module for cx2388x based TV cards |
| `cx8802` | 1.0.0 | mpeg driver for cx2388x based TV cards |
| `cx88xx` |  | v4l2 driver module for cx2388x based TV cards input driver for cx88 GPIO-based IR remote controls |
| `ddbridge` | 0.9.33-integrated | Digital Devices PCIe Bridge |
| `dm1105` |  | SDMC DM1105 DVB driver |
| `ivtv` | 1.4.3 | CX23415/CX23416 driver |
| `ivtvfb` |  |  |
| `hopper` |  | HOPPER driver |
| `mantis` |  | MANTIS driver |
| `mantis_core` |  | Mantis PCI DTV bridge driver |
| `ngene` |  | nGene |
| `pluto2` |  | Pluto2 driver |
| `earth-pt1` |  | Earthsoft PT1/PT2 Driver |
| `saa7134-alsa` |  |  |
| `saa7134-dvb` |  |  |
| `saa7134-empress` |  |  |
| `saa7134` | 0, 2, 17 | v4l2 driver module for saa7130/34 based TV cards |
| `saa7164` |  | Driver for NXP SAA7164 based TV cards |
| `budget-av` |  | driver for the SAA7146 based so-called budget PCI DVB w/ analog input and CI-module (e.g. the KNC cards) |
| `budget-ci` |  | driver for the SAA7146 based so-called budget PCI DVB cards w/ CI-module produced by Siemens, Technotrend, Hauppauge |
| `budget-core` |  |  |
| `budget-patch` |  | Driver for full TS modified DVB-S SAA7146+AV7110 based so-called Budget Patch cards |
| `budget` |  | driver for the SAA7146 based so-called budget PCI DVB cards by Siemens, Technotrend, Hauppauge |
| `dvb-ttpci` |  | driver for the SAA7146 based AV110 PCI DVB cards by Siemens, Technotrend, Hauppauge |
| `ttpci-eeprom` |  | Decode dvb\_net MAC address from EEPROM of PCI DVB cards made by Siemens, Technotrend, Hauppauge |
| `tea575x` |  | Routines for control of TEA5757/5759 Philips AM/FM radio tuner chips |
| `ati_remote` |  | ATI/X10 RF USB Remote Control |
| `ene_ir` |  | Infrared input driver for KB3926B/C/D/E/F (aka ENE0100/ENE0200/ENE0201/ENE0202) CIR port |
| `fintek-cir` |  | Fintek LPC SuperIO Consumer IR Transceiver driver |
| `iguanair` |  | IguanaWorks USB IR Transceiver |
| `imon` | 0.9.4 | Driver for SoundGraph iMON MultiMedia IR/Display |
| `imon_raw` |  | Early raw iMON IR devices |
| `ir-imon-decoder` |  | iMON IR protocol decoder |
| `ir-jvc-decoder` |  | JVC IR protocol decoder |
| `ir-mce_kbd-decoder` |  | MCE Keyboard/mouse IR protocol decoder |
| `ir-nec-decoder` |  | NEC IR protocol decoder |
| `ir-rc5-decoder` |  | RC5(x/sz) IR protocol decoder |
| `ir-rc6-decoder` |  | RC6 IR protocol decoder |
| `ir-sanyo-decoder` |  | SANYO IR protocol decoder |
| `ir-sharp-decoder` |  | Sharp IR protocol decoder |
| `ir-sony-decoder` |  | Sony IR protocol decoder |
| `ir-xmp-decoder` |  | XMP IR protocol decoder |
| `ite-cir` |  | ITE Tech Inc. IT8712F/ITE8512F CIR driver |
| `rc-adstech-dvb-t-pci` |  |  |
| `rc-alink-dtu-m` |  |  |
| `rc-anysee` |  |  |
| `rc-apac-viewcomp` |  |  |
| `rc-astrometa-t2hybrid` |  |  |
| `rc-asus-pc39` |  |  |
| `rc-asus-ps3-100` |  |  |
| `rc-ati-tv-wonder-hd-600` |  |  |
| `rc-ati-x10` |  |  |
| `rc-avermedia-a16d` |  |  |
| `rc-avermedia-cardbus` |  |  |
| `rc-avermedia-dvbt` |  |  |
| `rc-avermedia-m135a` |  |  |
| `rc-avermedia-m733a-rm-k6` |  |  |
| `rc-avermedia-rm-ks` |  |  |
| `rc-avermedia` |  |  |
| `rc-avertv-303` |  |  |
| `rc-azurewave-ad-tu700` |  |  |
| `rc-behold-columbus` |  |  |
| `rc-behold` |  |  |
| `rc-budget-ci-old` |  |  |
| `rc-cec` |  |  |
| `rc-cinergy-1400` |  |  |
| `rc-cinergy` |  |  |
| `rc-d680-dmb` |  |  |
| `rc-delock-61959` |  | Delock 61959 remote keytable |
| `rc-dib0700-nec` |  |  |
| `rc-dib0700-rc5` |  |  |
| `rc-digitalnow-tinytwin` |  |  |
| `rc-digittrade` |  |  |
| `rc-dm1105-nec` |  |  |
| `rc-dntv-live-dvb-t` |  |  |
| `rc-dntv-live-dvbt-pro` |  |  |
| `rc-dtt200u` |  |  |
| `rc-dvbsky` |  |  |
| `rc-dvico-mce` |  |  |
| `rc-dvico-portable` |  |  |
| `rc-em-terratec` |  |  |
| `rc-encore-enltv-fm53` |  |  |
| `rc-encore-enltv` |  |  |
| `rc-encore-enltv2` |  |  |
| `rc-evga-indtube` |  |  |
| `rc-eztv` |  |  |
| `rc-flydvb` |  |  |
| `rc-flyvideo` |  |  |
| `rc-fusionhdtv-mce` |  |  |
| `rc-gadmei-rm008z` |  |  |
| `rc-geekbox` |  |  |
| `rc-genius-tvgo-a11mce` |  |  |
| `rc-gotview7135` |  |  |
| `rc-hauppauge` |  |  |
| `rc-hisi-poplar` |  |  |
| `rc-hisi-tv-demo` |  |  |
| `rc-imon-mce` |  |  |
| `rc-imon-pad` |  |  |
| `rc-imon-rsc` |  |  |
| `rc-iodata-bctv7e` |  |  |
| `rc-it913x-v1` |  |  |
| `rc-it913x-v2` |  |  |
| `rc-kaiomy` |  |  |
| `rc-khadas` |  |  |
| `rc-kworld-315u` |  |  |
| `rc-kworld-pc150u` |  |  |
| `rc-kworld-plus-tv-analog` |  |  |
| `rc-leadtek-y04g0051` |  |  |
| `rc-lme2510` |  |  |
| `rc-manli` |  |  |
| `rc-medion-x10-digitainer` |  | Medion X10 RF remote keytable (Digitainer variant) |
| `rc-medion-x10-or2x` |  | Medion X10 OR22/OR24 RF remote keytable |
| `rc-medion-x10` |  |  |
| `rc-msi-digivox-ii` |  |  |
| `rc-msi-digivox-iii` |  |  |
| `rc-msi-tvanywhere-plus` |  |  |
| `rc-msi-tvanywhere` |  |  |
| `rc-nebula` |  |  |
| `rc-nec-terratec-cinergy-xs` |  |  |
| `rc-norwood` |  |  |
| `rc-npgtech` |  |  |
| `rc-odroid` |  |  |
| `rc-pctv-sedna` |  |  |
| `rc-pinnacle-color` |  |  |
| `rc-pinnacle-grey` |  |  |
| `rc-pinnacle-pctv-hd` |  |  |
| `rc-pixelview-002t` |  |  |
| `rc-pixelview-mk12` |  |  |
| `rc-pixelview-new` |  |  |
| `rc-pixelview` |  |  |
| `rc-powercolor-real-angel` |  |  |
| `rc-proteus-2309` |  |  |
| `rc-purpletv` |  |  |
| `rc-pv951` |  |  |
| `rc-rc6-mce` |  |  |
| `rc-real-audio-220-32-keys` |  |  |
| `rc-reddo` |  |  |
| `rc-snapstream-firefly` |  |  |
| `rc-streamzap` |  |  |
| `rc-su3000` |  |  |
| `rc-tango` |  |  |
| `rc-tanix-tx3mini` |  |  |
| `rc-tanix-tx5max` |  |  |
| `rc-tbs-nec` |  |  |
| `rc-technisat-ts35` |  |  |
| `rc-technisat-usb2` |  |  |
| `rc-terratec-cinergy-c-pci` |  |  |
| `rc-terratec-cinergy-s2-hd` |  |  |
| `rc-terratec-cinergy-xs` |  |  |
| `rc-terratec-slim-2` |  |  |
| `rc-terratec-slim` |  |  |
| `rc-tevii-nec` |  |  |
| `rc-tivo` |  |  |
| `rc-total-media-in-hand-02` |  |  |
| `rc-total-media-in-hand` |  |  |
| `rc-trekstor` |  |  |
| `rc-tt-1500` |  |  |
| `rc-twinhan-dtv-cab-ci` |  |  |
| `rc-twinhan1027` |  |  |
| `rc-videomate-m1f` |  |  |
| `rc-videomate-s350` |  |  |
| `rc-videomate-tv-pvr` |  |  |
| `rc-videostrong-kii-pro` |  |  |
| `rc-wetek-hub` |  |  |
| `rc-wetek-play2` |  |  |
| `rc-winfast-usbii-deluxe` |  |  |
| `rc-winfast` |  |  |
| `rc-x96max` |  |  |
| `rc-xbox-dvd` |  |  |
| `rc-zx-irdec` |  |  |
| `mceusb` |  | Windows Media Center Ed. eHome Infrared Transceiver device driver |
| `nuvoton-cir` |  | Nuvoton W83667HG-A & W83677HG-I CIR driver |
| `rc-core` |  |  |
| `rc-loopback` |  | Loopback device for rc-core debugging |
| `redrat3` |  | RedRat3 USB IR Transceiver Driver |
| `serial_ir` |  | Infra-red receiver driver for serial ports. |
| `sir_ir` |  | Infrared receiver driver for SIR type serial ports |
| `streamzap` |  | Streamzap Remote Control driver |
| `ttusbir` |  | TechnoTrend USB IR Receiver |
| `winbond-cir` |  | Winbond SuperI/O Consumer IR Driver |
| `e4000` |  | Elonics E4000 silicon tuner driver |
| `fc0011` |  | Fitipower FC0011 silicon tuner driver |
| `fc0012` | 0.6 | Fitipower FC0012 silicon tuner driver |
| `fc0013` | 0.2 | Fitipower FC0013 silicon tuner driver |
| `fc2580` |  | FCI FC2580 silicon tuner driver |
| `it913x` |  | ITE IT913X silicon tuner driver |
| `m88rs6000t` |  | Montage M88RS6000 internal tuner driver |
| `max2165` |  | Maxim MAX2165 silicon tuner driver |
| `mc44s803` |  | Freescale MC44S803 silicon tuner driver |
| `mt2060` |  | Microtune MT2060 silicon tuner driver |
| `mt2063` |  | MT2063 Silicon tuner |
| `mt20xx` |  | Microtune tuner driver |
| `mt2131` |  | Microtune MT2131 silicon tuner driver |
| `mt2266` |  | Microtune MT2266 silicon tuner driver |
| `mxl5005s` |  | MaxLinear MXL5005S silicon tuner driver |
| `mxl5007t` | 0.2 | MaxLinear MxL5007T Silicon IC tuner driver |
| `qm1d1b0004` |  | Sharp QM1D1B0004 |
| `qm1d1c0042` |  | Sharp QM1D1C0042 tuner |
| `qt1010` | 0.1 | Quantek QT1010 silicon tuner driver |
| `r820t` |  | Rafael Micro r820t silicon tuner driver |
| `si2157` |  | Silicon Labs Si2141/Si2146/2147/2148/2157/2158 silicon tuner driver |
| `tda18212` |  | NXP TDA18212HN silicon tuner driver |
| `tda18218` |  | NXP TDA18218HN silicon tuner driver |
| `tda18250` |  | NXP TDA18250 silicon tuner driver |
| `tda18271` | 0.4 | NXP TDA18271HD analog / digital tuner driver |
| `tda827x` |  | DVB TDA827x driver |
| `tda8290` |  | Philips/NXP TDA8290/TDA8295 analog IF demodulator driver |
| `tda9887` |  |  |
| `tea5761` |  | Philips TEA5761 FM tuner driver |
| `tea5767` |  | Philips TEA5767 FM tuner driver |
| `tua9001` |  | Infineon TUA9001 silicon tuner driver |
| `tuner-simple` |  | Simple 4-control-bytes style tuner driver |
| `tuner-types` |  | Simple tuner device type database |
| `tuner-xc2028` |  | Xceive xc2028/xc3028 tuner driver |
| `xc4000` |  | Xceive xc4000 silicon tuner driver |
| `xc5000` |  | Xceive xc5000 silicon tuner driver |
| `au0828` | 0.0.3 | Driver for Auvitek AU0828 based products |
| `b2c2-flexcop-usb` |  | Technisat/B2C2 FlexCop II/IIb/III Digital TV USB Driver |
| `cx231xx-alsa` |  | Cx231xx Audio driver |
| `cx231xx-dvb` |  | driver for cx231xx based DVB cards |
| `cx231xx` | 0.0.3 | Conexant cx231xx based USB video device driver |
| `dvb-usb-a800` | 1.0 | AVerMedia AverTV DVB-T USB 2.0 (A800) |
| `dvb-usb-af9005-remote` | 1.0 | Standard remote control decoder for Afatech 9005 DVB-T USB1.1 stick |
| `dvb-usb-af9005` | 1.0 | Driver for Afatech 9005 DVB-T USB1.1 stick |
| `dvb-usb-az6027` | 1.0 | Driver for AZUREWAVE DVB-S/S2 USB2.0 (AZ6027) |
| `dvb-usb-cinergyT2` |  | Terratec Cinergy T2 DVB-T driver |
| `dvb-usb-cxusb` |  | Driver for Conexant USB2.0 hybrid reference design |
| `dvb-usb-dib0700` | 1.0 | Driver for devices based on DiBcom DiB0700 - USB bridge |
| `dvb-usb-dibusb-common` |  |  |
| `dvb-usb-dibusb-mb` | 1.0 | Driver for DiBcom USB DVB-T devices (DiB3000M-B based) |
| `dvb-usb-dibusb-mc-common` |  |  |
| `dvb-usb-dibusb-mc` | 1.0 | Driver for DiBcom USB2.0 DVB-T (DiB3000M-C/P based) devices |
| `dvb-usb-digitv` | 1.0-alpha | Driver for Nebula Electronics uDigiTV DVB-T USB2.0 |
| `dvb-usb-dtt200u` | 1.0 | Driver for the WideView/Yakumo/Hama/Typhoon/Club3D/Miglia DVB-T USB2.0 devices |
| `dvb-usb-dtv5100` |  | AME DTV-5100 USB2.0 DVB-T |
| `dvb-usb-dw2102` | 0.1 | Driver for DVBWorld DVB-S 2101, 2102, DVB-S2 2104, DVB-C 3101 USB2.0, TeVii S421, S480, S482, S600, S630, S632, S650, TeVii S660, S662, Prof 1100, 7500 USB2.0, Geniatech SU3000, T220, TechnoTrend S2-4600, Terratec Cinergy S2 devices |
| `dvb-usb-gp8psk` | 1.1 | Driver for Genpix DVB-S |
| `dvb-usb-m920x` | 0.1 | DVB Driver for ULI M920x |
| `dvb-usb-nova-t-usb2` | 1.0 | Hauppauge WinTV-NOVA-T usb2 |
| `dvb-usb-opera` | 0.1 | Driver for Opera1 DVB-S device |
| `dvb-usb-pctv452e` |  | Pinnacle PCTV HDTV USB DVB / TT connect S2-3600 Driver |
| `dvb-usb-technisat-usb2` | 1.0 | Driver for Technisat DVB-S/S2 USB 2.0 device |
| `dvb-usb-ttusb2` | 1.0 | Driver for Pinnacle PCTV 400e DVB-S USB2.0 |
| `dvb-usb-umt-010` | 1.0 | Driver for HanfTek UMT 010 USB2.0 DVB-T device |
| `dvb-usb-vp702x` | 1.0 | Driver for Twinhan StarBox DVB-S USB2.0 and clones |
| `dvb-usb-vp7045` | 1.0 | Driver for Twinhan MagicBox/Alpha and DNTV tinyUSB2 DVB-T USB2.0 |
| `dvb-usb` | 1.0 | A library module containing commonly used USB and DVB function USB DVB devices |
| `dvb-usb-af9015` |  | Afatech AF9015 driver |
| `dvb-usb-af9035` |  | Afatech AF9035 driver |
| `dvb-usb-anysee` |  | Driver Anysee E30 DVB-C & DVB-T USB2.0 |
| `dvb-usb-au6610` | 0.1 | Driver for Alcor Micro AU6610 DVB-T USB2.0 |
| `dvb-usb-az6007` | 2.0 | Driver for AzureWave 6007 DVB-C/T USB2.0 and clones |
| `dvb-usb-ce6230` |  | Intel CE6230 driver |
| `dvb-usb-dvbsky` |  | Driver for DVBSky USB |
| `dvb-usb-ec168` |  | E3C EC168 driver |
| `dvb-usb-gl861` | 0.1 | Driver MSI Mega Sky 580 DVB-T USB2.0 / GL861 |
| `dvb-usb-lmedm04` | 2.07 | LME2510(C) DVB-S USB2.0 |
| `dvb-usb-mxl111sf` | 1.0 | Driver for MaxLinear MxL111SF |
| `dvb-usb-rtl28xxu` |  | Realtek RTL28xxU DVB USB driver |
| `dvb_usb_v2` | 2.0 | DVB USB common |
| `mxl111sf-demod` | 0.1 | MaxLinear MxL111SF DVB-T demodulator driver |
| `mxl111sf-tuner` | 0.1 | MaxLinear MxL111SF CMOS tuner driver |
| `em28xx-alsa` | 0.2.2 | Empia em28xx device driver - audio interface |
| `em28xx-dvb` | 0.2.2 | Empia em28xx device driver - digital TV interface |
| `em28xx-rc` | 0.2.2 | Empia em28xx device driver - input interface |
| `em28xx` | 0.2.2 | Empia em28xx device driver |
| `gspca_gl860` |  | Genesys Logic USB PC Camera Driver |
| `gspca_benq` |  | Benq DC E300 USB Camera Driver |
| `gspca_conex` |  | GSPCA USB Conexant Camera Driver |
| `gspca_cpia1` |  | Vision CPiA |
| `gspca_dtcs033` |  | Scopium DTCS033 astro-cam USB Camera Driver |
| `gspca_etoms` |  | Etoms USB Camera Driver |
| `gspca_finepix` |  | Fujifilm FinePix USB V4L2 driver |
| `gspca_jeilinj` |  | GSPCA/JEILINJ USB Camera Driver |
| `gspca_jl2005bcd` |  | JL2005B/C/D USB Camera Driver |
| `gspca_kinect` |  | GSPCA/Kinect Sensor Device USB Camera Driver |
| `gspca_konica` |  | Konica chipset USB Camera Driver |
| `gspca_main` | 2.14.0 | GSPCA USB Camera Driver |
| `gspca_mars` |  | GSPCA/Mars USB Camera Driver |
| `gspca_mr97310a` |  | GSPCA/Mars-Semi MR97310A USB Camera Driver |
| `gspca_nw80x` |  | NW80x USB Camera Driver |
| `gspca_ov519` |  | OV519 USB Camera Driver |
| `gspca_ov534` |  | GSPCA/OV534 USB Camera Driver |
| `gspca_ov534_9` |  | GSPCA/OV534\_9 USB Camera Driver |
| `gspca_pac207` |  | Pixart PAC207 |
| `gspca_pac7302` |  | Pixart PAC7302 |
| `gspca_pac7311` |  | Pixart PAC7311 |
| `gspca_se401` |  | Endpoints se401 |
| `gspca_sn9c2028` |  | Sonix SN9C2028 USB Camera Driver |
| `gspca_sn9c20x` |  | GSPCA/SN9C20X USB Camera Driver |
| `gspca_sonixb` |  | GSPCA/SN9C102 USB Camera Driver |
| `gspca_sonixj` |  | GSPCA/SONIX JPEG USB Camera Driver |
| `gspca_spca1528` |  | SPCA1528 USB Camera Driver |
| `gspca_spca500` |  | GSPCA/SPCA500 USB Camera Driver |
| `gspca_spca501` |  | GSPCA/SPCA501 USB Camera Driver |
| `gspca_spca505` |  | GSPCA/SPCA505 USB Camera Driver |
| `gspca_spca506` |  | GSPCA/SPCA506 USB Camera Driver |
| `gspca_spca508` |  | GSPCA/SPCA508 USB Camera Driver |
| `gspca_spca561` |  | GSPCA/SPCA561 USB Camera Driver |
| `gspca_sq905` |  | GSPCA/SQ905 USB Camera Driver |
| `gspca_sq905c` |  | GSPCA/SQ905C USB Camera Driver |
| `gspca_sq930x` |  | GSPCA/SQ930x USB Camera Driver |
| `gspca_stk014` |  | Syntek DV4000 (STK014) USB Camera Driver |
| `gspca_stk1135` |  | Syntek STK1135 USB Camera Driver |
| `gspca_stv0680` |  | STV0680 USB Camera Driver |
| `gspca_sunplus` |  | GSPCA/SPCA5xx USB Camera Driver |
| `gspca_t613` |  | GSPCA/T613 (JPEG Compliance) USB Camera Driver |
| `gspca_topro` |  | Topro TP6800/6810 gspca webcam driver |
| `gspca_tv8532` |  | TV8532 USB Camera Driver |
| `gspca_vc032x` |  | GSPCA/VC032X USB Camera Driver |
| `gspca_vicam` |  | GSPCA ViCam USB Camera Driver |
| `gspca_xirlink_cit` |  | Xirlink C-IT |
| `gspca_zc3xx` |  | GSPCA ZC03xx/VC3xx USB Camera Driver |
| `gspca_m5602` |  | ALi m5602 webcam driver |
| `gspca_stv06xx` |  | STV06XX USB Camera Driver |
| `hdpvr` | 0.2.1 | Hauppauge HD PVR driver |
| `pvrusb2` | 0.9.1 | Hauppauge WinTV-PVR-USB2 MPEG2 Encoder/Tuner |
| `pwc` | 10.0.15 | Philips & OEM USB webcam driver |
| `s2255drv` | 1.25.1 | Sensoray 2255 Video for Linux driver |
| `smsusb` |  | Driver for the Siano SMS1xxx USB dongle |
| `stk1160` |  | STK1160 driver |
| `stkwebcam` |  | Syntek DC1125 webcam driver |
| `tm6000-alsa` |  | ALSA driver module for tm5600/tm6000/tm6010 based TV cards |
| `tm6000-dvb` |  | DVB driver extension module for tm5600/6000/6010 based TV cards |
| `tm6000` |  | Trident TVMaster TM5600/TM6000/TM6010 USB2 adapter |
| `dvb-ttusb-budget` |  | TTUSB DVB Driver |
| `ttusb_dec` |  | TechnoTrend/Hauppauge DEC USB |
| `ttusbdecfe` |  | TTUSB DEC DVB-T/S Demodulator driver |
| `usbvision` | 0.9.11 | USBVision USB Video Device Driver for Linux |
| `uvcvideo` | 1.1.1 | USB Video Class driver |
| `zr364xx` | 0.7.4 | Zoran 364xx |
| `tuner` |  | device driver for various TV and TV+FM radio tuners |
| `v4l2-dv-timings` |  | V4L2 DV Timings Helper Functions |
| `v4l2-fwnode` |  |  |
| `videobuf-core` |  | helper module to manage video4linux buffers |
| `videobuf-dma-sg` |  | helper module to manage video4linux dma sg buffers |
| `videobuf-vmalloc` |  | helper module to manage video4linux vmalloc buffers |
| `videodev` |  | Video4Linux2 core driver |

### `memstick` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `memstick` |  | Sony MemoryStick core driver |
| `mspro_block` |  | Sony MemoryStickPro block device driver |
| `jmb38x_ms` |  | JMicron jmb38x MemoryStick driver |
| `r592` |  | Ricoh R5C592 Memstick/Memstick PRO card reader driver |
| `rtsx_pci_ms` |  | Realtek PCI-E Memstick Card Host Driver |
| `rtsx_usb_ms` |  | Realtek USB Memstick Card Host Driver |
| `tifm_ms` |  | TI FlashMedia MemoryStick driver |

### `message` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `mptbase` | 3.04.20 | Fusion MPT base driver |
| `mptctl` | 3.04.20 | Fusion MPT misc device (ioctl) driver |
| `mptfc` | 3.04.20 | Fusion MPT FC Host driver |
| `mptlan` | 3.04.20 | Fusion MPT LAN driver |
| `mptsas` | 3.04.20 | Fusion MPT SAS Host driver |
| `mptscsih` | 3.04.20 | Fusion MPT SCSI Host driver |
| `mptspi` | 3.04.20 | Fusion MPT SPI Host driver |

### `mfd` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `lpc_ich` |  | LPC interface for Intel ICH |
| `lpc_sch` |  | LPC interface for Intel Poulsbo SCH |
| `pcf50633-adc` |  | PCF50633 adc driver |
| `pcf50633-gpio` |  |  |
| `pcf50633` |  | I2C chip driver for NXP PCF50633 PMU |
| `rdc321x-southbridge` |  | RDC R-321x MFD southbridge driver |
| `retu-mfd` |  | Retu MFD driver |
| `si476x-core` |  | API for command exchange for si476x Si4761/64/68 AM/FM MFD core device driver |
| `sm501` |  | SM501 Core Driver |
| `ucb1400_core` |  | Philips UCB1400 driver |
| `viperboard` |  | Nano River Technologies viperboard mfd core driver |
| `vx855` |  | Driver for the VIA VX855 chipset |

### `misc` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `ad525x_dpot-i2c` |  | digital potentiometer I2C bus driver |
| `ad525x_dpot` |  | Digital potentiometer driver |
| `altera-stapl` |  | altera FPGA kernel module |
| `apds9802als` |  | Avago apds9802als ALS Driver |
| `apds990x` |  | APDS990X combined ALS and proximity sensor |
| `bh1770glc` |  | BH1770GLC / SFH7770 combined ALS and proximity sensor |
| `rtsx_pci` |  | Realtek PCI-E Card Reader Driver |
| `rtsx_usb` |  | Realtek USB Card Reader Driver |
| `cb710` |  | ENE CB710 memory card reader driver |
| `at24` |  | Driver for most I2C EEPROMs |
| `eeprom` |  | I2C EEPROM driver |
| `eeprom_93cx6` | 1.0 | EEPROM 93cx6 chip driver |
| `max6875` |  | MAX6875 driver |
| `enclosure` |  | Enclosure Services |
| `hmc6352` |  | hmc6352 Compass Driver |
| `hpilo` | 1.5.0 | hpilo |
| `ics932s401` |  | ICS932S401 driver |
| `isl29003` | 1.0 | ISL29003 ambient light sensor driver |
| `isl29020` |  | Intersil isl29020 ALS Driver |
| `lis3lv02d` |  | ST LIS3LV02Dx three-axis digital accelerometer driver |
| `lis3lv02d_i2c` |  | lis3lv02d I2C interface |
| `mei-me` |  | Intel(R) Management Engine Interface |
| `mei` |  | Intel(R) Management Engine Interface |
| `gru` | 0.85 | SGI GRU Device Driver0.85 |
| `xp` |  | Cross Partition (XP) base |
| `xpc` |  | Cross Partition Communication (XPC) support |
| `xpnet` |  | Cross Partition Network adapter (XPNET) |
| `tifm_7xx1` | 0.8 | TI FlashMedia host driver |
| `tifm_core` | 0.8 | TI FlashMedia core driver |
| `tsl2550` | 1.2 | TSL2550 ambient light sensor driver |
| `vmw_balloon` |  | VMware Memory Control (Balloon) Driver |
| `vmw_vmci` | 1.1.6.0-k | VMware Virtual Machine Communication Interface. |

### `mmc` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `mmc_block` |  | Multimedia Card (MMC) block device driver |
| `mmc_core` |  |  |
| `sdio_uart` |  |  |
| `cb710-mmc` |  | ENE CB710 memory card reader driver - MMC/SD part |
| `cqhci` |  | Command Queue Host Controller Interface driver |
| `rtsx_pci_sdmmc` |  | Realtek PCI-E SD/MMC Card Host Driver |
| `rtsx_usb_sdmmc` |  | Realtek USB SD/MMC Card Host Driver |
| `sdhci-acpi` |  | Secure Digital Host Controller Interface ACPI driver |
| `sdhci-pci` |  | Secure Digital Host Controller Interface PCI driver |
| `sdhci-pltfm` |  | SDHCI platform and OF driver helper |
| `sdhci` |  | Secure Digital Host Controller Interface core driver |
| `tifm_sd` | 0.8 | TI FlashMedia SD driver |
| `usdhi6rol0` |  | Renesas usdhi6rol0 SD/SDIO host driver |
| `ushc` |  | USB SD Host Controller driver |
| `via-sdmmc` |  | VIA SD/MMC Card Interface driver |
| `vub300` |  | VUB300 USB to SD/MMC/SDIO adapter driver |
| `wbsd` |  | Winbond W83L51xD SD/MMC card interface driver |

### `mtd` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `cfi_cmdset_0001` |  | MTD chip driver for Intel/Sharp flash chips |
| `cfi_cmdset_0002` |  | MTD chip driver for AMD/Fujitsu flash chips |
| `cfi_cmdset_0020` |  |  |
| `cfi_probe` |  | Probe code for CFI-compliant flash chips |
| `cfi_util` |  |  |
| `chipreg` |  | Core routines for registering and invoking MTD chip drivers |
| `gen_probe` |  | Helper routines for flash chip probe code |
| `jedec_probe` |  | Probe code for JEDEC-compliant flash chips |
| `map_absent` |  | Placeholder MTD chip driver for 'absent' chips |
| `map_ram` |  | MTD chip driver for RAM chips |
| `map_rom` |  | MTD chip driver for ROM chips |
| `block2mtd` |  | Emulate an MTD using a block device |
| `mtdram` |  | Simulated MTD driver for testing |
| `pmc551` |  | Ramix PMC551 PCI Mezzanine Ram Driver. (C) 1999,2000 Nortel Networks. |
| `ftl` |  | Support code for Flash Translation Layer, used on PCMCIA devices |
| `inftl` |  | Support code for Inverse Flash Translation Layer, used on M-Systems DiskOnChip 2000, Millennium and Millennium Plus |
| `lpddr_cmds` |  | MTD driver for LPDDR flash chips |
| `qinfo_probe` |  | Driver to probe qinfo flash chips |
| `ck804xrom` |  | MTD map driver for BIOS chips on the Nvidia ck804 southbridge |
| `esb2rom` |  | MTD map driver for BIOS chips on the ESB2 southbridge |
| `map_funcs` |  |  |
| `pci` |  | Generic PCI map driver |
| `physmap` |  | Generic configurable MTD map driver |
| `scb2_flash` |  | MTD map driver for Intel SCB2 BIOS Flash |
| `mtd` |  | Core MTD registration and access routines Generic support for concatenating of MTD devices |
| `mtd_blkdevs` |  | Common interface to block layer for MTD 'translation layers' |
| `mtdblock` |  | Caching read/erase/writeback block device emulation access to MTD devices |
| `mtdblock_ro` |  | Simple read-only block device emulation access to MTD devices |
| `mtdoops` |  | MTD Oops/Panic console logger/driver |
| `mtdswap` |  | Block device access to an MTD suitable for using as swap space |
| `nandcore` |  | Generic NAND framework |
| `diskonchip` |  | M-Systems DiskOnChip 2000, Millennium and Millennium Plus device driver |
| `nand` |  | Generic NAND flash driver code NAND software BCH ECC support |
| `nand_ecc` |  | Generic NAND ECC support |
| `nandsim` |  | The NAND flash simulator |
| `nftl` |  | Support code for NAND Flash Translation Layer, used on M-Systems DiskOnChip 2000 and Millennium |
| `ar7part` |  | MTD partitioning for TI AR7 |
| `cmdlinepart` |  | Command line configuration of MTD partitions |
| `redboot` |  | Parsing code for RedBoot Flash Image System (FIS) tables |
| `rfd_ftl` |  | Support code for RFD Flash Translation Layer, used by General Software's Embedded BIOS |
| `sm_ftl` |  | Smartmedia/xD mtd translation layer |
| `ssfdc` |  | Flash Translation Layer for read-only SSFDC SmartMedia card |
| `ubi` | 1 | UBI - Unsorted Block Images |

### `net` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `bonding` | 3.7.1 | Ethernet Channel Bonding Driver, v3.7.1 |
| `c_can` |  | CAN bus driver for Bosch C\_CAN controller |
| `c_can_pci` |  | PCI CAN bus driver for Bosch C\_CAN/D\_CAN controller |
| `c_can_platform` |  | Platform CAN bus driver for Bosch C\_CAN controller |
| `can-dev` |  | CAN device driver interface |
| `cc770` |  | cc770CAN netdevice driver |
| `cc770_platform` |  | Socket-CAN driver for CC770 on the platform bus |
| `m_can` |  | CAN bus driver for Bosch M\_CAN controller |
| `ems_pci` |  | Socket-CAN driver for EMS CPC-PCI/PCIe/104P CAN cards |
| `kvaser_pci` |  | Socket-CAN driver for KVASER PCAN PCI cards |
| `peak_pci` |  | Socket-CAN driver for PEAK PCAN PCI family cards |
| `plx_pci` |  | Socket-CAN driver for PLX90xx PCI-bridge cards with the SJA1000 chips |
| `sja1000` |  | sja1000CAN netdevice driver |
| `sja1000_platform` |  | Socket-CAN driver for SJA1000 on the platform bus |
| `slcan` |  | serial line CAN interface |
| `softing` |  | Softing DPRAM CAN driver |
| `ems_usb` |  | CAN driver for EMS Dr. Thomas Wuensche CAN/USB interfaces |
| `esd_usb2` |  | CAN driver for esd CAN-USB/2 and CAN-USB/Micro interfaces |
| `gs_usb` |  | Socket CAN device driver for Geschwister Schneider Technologie-, Entwicklungs- und Vertriebs UG. USB2.0 to CAN interfaces and bytewerk.org candleLight USB CAN interfaces. |
| `kvaser_usb` |  | CAN driver for Kvaser CAN/USB devices |
| `peak_usb` |  | CAN driver for PEAK-System USB adapters |
| `usb_8dev` |  | CAN driver for 8 devices USB2CAN interfaces |
| `vcan` |  | virtual CAN interface |
| `dummy` | 1.0 |  |
| `eql` |  |  |
| `3c59x` |  | 3Com 3c59x/3c9xx ethernet driver |
| `typhoon` | 1.0 | 3Com Typhoon Family (3C990, 3CR990, and variants) |
| `starfire` | 2.1 | Adaptec Starfire Ethernet driver |
| `acenic` |  | AceNIC/3C985/GA620 Gigabit Ethernet driver |
| `ena` | 2.1.0K | Elastic Network Adapter (ENA) |
| `amd8111e` |  | AMD8111 based 10/100 Ethernet Controller. Driver Version 3.0.7 |
| `pcnet32` |  | Driver for PCnet32 and PCnetPCI based ethercards |
| `amd-xgbe` | 1.0.3 | AMD 10 Gigabit Ethernet Driver |
| `atlantic` | 5.4.17-2102.200.13.el7uek.x86\_64-kern | aQuantia Corporation(R) Network Driver |
| `alx` |  | Qualcomm Atheros(R) AR816x/AR817x PCI-E Ethernet Network Driver |
| `atl1c` | 1.0.1.1-NAPI | Qualcomm Atheros 100/1000M Ethernet Network Driver |
| `atl1e` | 1.0.0.7-NAPI | Atheros 1000M Ethernet Network Driver |
| `atl1` | 2.1.3 | Atheros L1 Gigabit Ethernet Driver |
| `atl2` | 2.2.3 | Atheros Fast Ethernet Network Driver |
| `b44` | 2.0 | Broadcom 44xx/47xx 10/100 PCI ethernet driver |
| `bnx2` | 2.2.6 | QLogic BCM5706/5708/5709/5716 Driver |
| `bnx2x` | 1.713.36-0 | QLogic BCM57710/57711/57711E/57712/57712\_MF/57800/57800\_MF/57810/57810\_MF/57840/57840\_MF Driver |
| `bnxt_en` | 1.10.1 | Broadcom BCM573xx network driver |
| `cnic` | 2.5.22 | QLogic cnic Driver |
| `tg3` | 3.137 | Broadcom Tigon3 ethernet driver |
| `bna` | 3.2.25.1 | QLogic BR-series 10G PCIe Ethernet driver |
| `cxgb` |  | Chelsio 10Gb Ethernet Driver |
| `cxgb3` | 1.1.5-ko | Chelsio T3 Network Driver |
| `cxgb4` | 2.0.0-ko | Chelsio T4/T5/T6 Network Driver |
| `cxgb4vf` | 2.0.0-ko | Chelsio T4/T5/T6 Virtual Function (VF) Network Driver |
| `libcxgb` | 1.0.0-ko | Chelsio common library |
| `enic` | 2.3.0.53 | Cisco VIC Ethernet NIC Driver |
| `de2104x` | 0.7 | Intel/Digital 21040/1 series PCI Ethernet driver |
| `de4x5` |  |  |
| `dmfe` | 1.36.4 | Davicom DM910X fast ethernet driver |
| `tulip` | 1.1.15 | Digital 21\*4\* Tulip ethernet driver |
| `uli526x` |  | ULi M5261/M5263 fast ethernet driver |
| `winbond-840` | 1.01-e | Winbond W89c840 Ethernet driver |
| `xircom_cb` |  | Xircom Cardbus ethernet driver |
| `dl2k` |  | D-Link DL2000-based Gigabit Ethernet Adapter |
| `sundance` |  | Sundance Alta Ethernet driver |
| `dnet` |  | Dave DNET Ethernet driver |
| `be2net` | 12.0.0.0 | Emulex OneConnect NIC Driver 12.0.0.0 |
| `ethoc` |  | OpenCores Ethernet MAC driver |
| `hinic` |  | Huawei Intelligent NIC driver |
| `e100` | 3.5.24-k2-NAPI | Intel(R) PRO/100 Network Driver |
| `e1000` | 7.3.21-k8-NAPI | Intel(R) PRO/1000 Network Driver |
| `e1000e` | 3.2.6-k | Intel(R) PRO/1000 Network Driver |
| `fm10k` | 0.26.1-k | Intel(R) Ethernet Switch Host Interface Driver |
| `i40e` | 2.8.20-k | Intel(R) Ethernet Connection XL710 Network Driver |
| `iavf` | 3.2.3-k | Intel(R) Ethernet Adaptive Virtual Function Network Driver |
| `ice` | 0.8.2-k | Intel(R) Ethernet Connection E800 Series Linux Driver |
| `igb` | 5.6.0-k | Intel(R) Gigabit Ethernet Network Driver |
| `igbvf` | 2.4.0-k | Intel(R) Gigabit Virtual Function Network Driver |
| `igc` | 0.0.1-k | Intel(R) 2.5G Ethernet Linux Driver |
| `ixgb` | 1.0.135-k2-NAPI | Intel(R) PRO/10GbE Network Driver |
| `ixgbe` | 5.1.0-k | Intel(R) 10 Gigabit PCI Express Network Driver |
| `ixgbevf` | 4.1.0-k | Intel(R) 10 Gigabit Virtual Function Network Driver |
| `jme` | 1.0.8 | JMicron JMC2x0 PCI Express Ethernet driver |
| `mvmdio` |  | Marvell MDIO interface driver |
| `skge` | 1.14 | SysKonnect Gigabit Ethernet driver |
| `sky2` | 1.30 | Marvell Yukon 2 Gigabit Ethernet driver |
| `mlx4_core` | 4.0-0 | Mellanox ConnectX HCA low-level driver |
| `mlx4_en` | 4.0-0 | Mellanox ConnectX HCA Ethernet driver |
| `mlx5_core` | 5.0-0 | Mellanox 5th generation network adapters (ConnectX series) core driver |
| `mlxfw` |  | Mellanox firmware flash lib |
| `mstflint_access` | 2.0.0 (Nov-27-2012) | MST Module |
| `myri10ge` | 1.5.3-1.534 | Myricom 10G driver (10GbE) |
| `s2io` | 2.0.26.28 |  |
| `vxge` |  | Neterion's X3100 Series 10GbE PCIe I/OVirtualized Server Adapter |
| `nfp` | 5.4.17-2102.200.13.el7uek.x86\_64 | The Netronome Flow Processor (NFP) driver. |
| `forcedeth` |  | Reverse Engineered nForce ethernet driver |
| `netxen_nic` | 4.0.82 | QLogic/NetXen (1/10) GbE Intelligent Ethernet Driver |
| `qed` | 8.37.0.20 | QLogic FastLinQ 4xxxx Core Module |
| `qede` | 8.37.0.20 | QLogic FastLinQ 4xxxx Ethernet Driver |
| `qla3xxx` | v2.03.00-k5 | QLogic ISP3XXX Network Driver v2.03.00-k5 |
| `qlcnic` | 5.3.66 | QLogic 1/10 GbE Converged/Intelligent Ethernet Driver |
| `r6040` | 0.29 04Jul2016 | RDC R6040 NAPI PCI FastEthernet driver |
| `8139cp` | 1.3 | RealTek RTL-8139C+ series 10/100 PCI Ethernet driver |
| `8139too` | 0.9.28 | RealTek RTL-8139 Fast Ethernet driver |
| `r8169` |  | RealTek RTL-8169 Gigabit Ethernet driver |
| `rocker` |  | Rocker switch device driver |
| `sfc` | 4.1 | Solarflare network driver |
| `sc92031` |  | Silan SC92031 PCI Fast Ethernet Adapter driver |
| `sis190` | 1.4 | SiS sis190/191 Gigabit Ethernet driver |
| `sis900` |  | SiS 900 PCI Fast Ethernet driver |
| `epic100` |  | SMC 83c170 EPIC series Ethernet driver |
| `smsc9420` | 1.01 |  |
| `dwmac-generic` |  | Generic dwmac driver |
| `stmmac-platform` |  | STMMAC 10/100/1000 Ethernet platform support |
| `stmmac` |  | STMMAC 10/100/1000 Ethernet device driver |
| `cassini` |  | Sun Cassini(+) ethernet driver |
| `niu` | 1.1 | NIU ethernet driver |
| `sungem` |  | Sun GEM Gbit ethernet driver |
| `sunhme` | 3.10 | Sun HappyMealEthernet(HME) 10/100baseT ethernet driver |
| `tehuti` |  | Tehuti Networks(R) Network Driver |
| `tlan` |  | Driver for TI ThunderLAN based ethernet PCI adapters |
| `fjes` | 1.2 | FUJITSU Extended Socket Network Device Driver |
| `geneve` | 0.6 | Interface driver for GENEVE encapsulated traffic |
| `hv_netvsc` |  | Microsoft Hyper-V network driver |
| `fakelb` |  |  |
| `ifb` |  |  |
| `ipvlan` |  | Driver for L3 (IPv6/IPv4) based VLANs |
| `ipvtap` |  |  |
| `macsec` |  | MACsec IEEE 802.1AE |
| `macvlan` |  | Driver for MAC address based VLANs |
| `macvtap` |  |  |
| `mdio` |  | Generic support for MDIO-compatible transceivers |
| `mii` |  | MII hardware support library |
| `net_failover` |  | Failover driver for Paravirtual drivers |
| `netconsole` |  | Console driver for network interfaces |
| `netdevsim` |  |  |
| `nlmon` |  | Netlink monitoring device |
| `ntb_netdev` | 0.7 | ntb\_netdev |
| `amd` |  | AMD PHY driver |
| `aquantia` |  | Aquantia PHY driver |
| `at803x` |  | Atheros 803x PHY driver |
| `bcm-phy-lib` |  | Broadcom PHY Library |
| `bcm7xxx` |  | Broadcom BCM7xxx internal PHY driver |
| `bcm87xx` |  |  |
| `broadcom` |  | Broadcom PHY driver |
| `cicada` |  | Cicadia PHY driver |
| `cortina` |  | Cortina EDC CDR 10G Ethernet PHY driver |
| `davicom` |  | Davicom PHY driver |
| `dp83640` |  | National Semiconductor DP83640 PHY driver |
| `dp83822` |  | Texas Instruments DP83822 PHY driver |
| `dp83848` |  | Texas Instruments DP83848 PHY driver |
| `dp83867` |  | Texas Instruments DP83867 PHY driver |
| `dp83tc811` |  | Texas Instruments DP83TC811 PHY driver |
| `et1011c` |  | LSI ET1011C PHY driver |
| `icplus` |  | ICPlus IP175C/IP101A/IP101G/IC1001 PHY drivers |
| `intel-xway` |  | Intel XWAY PHY driver |
| `lxt` |  | Intel LXT PHY driver |
| `marvell` |  | Marvell PHY driver |
| `marvell10g` |  | Marvell Alaska X 10Gigabit Ethernet PHY driver (MV88X3310) |
| `mdio-bitbang` |  |  |
| `mdio-cavium` |  | Common code for OCTEON and Thunder MDIO bus drivers |
| `mdio-mscc-miim` |  | Microsemi MIIM driver |
| `mdio-thunder` |  | Cavium ThunderX MDIO bus driver |
| `micrel` |  | Micrel PHY driver |
| `microchip` |  | Microchip LAN88XX PHY driver |
| `microchip_t1` |  | Microchip LAN87XX T1 PHY driver |
| `mscc` |  | Microsemi VSC85xx PHY driver |
| `national` |  | NatSemi PHY driver |
| `qsemi` |  | Quality Semiconductor PHY driver |
| `realtek` |  | Realtek PHY driver |
| `rockchip` |  | Rockchip Ethernet PHY driver |
| `smsc` |  | SMSC PHY driver |
| `ste10Xp` |  | STMicroelectronics STe10Xp PHY driver |
| `teranetics` |  | Teranetics PHY driver |
| `uPD60620` |  | Renesas uPD60620 PHY driver |
| `vitesse` |  | Vitesse PHY driver |
| `xilinx_gmii2rgmii` |  | Xilinx GMII2RGMII converter driver |
| `bsd_comp` |  |  |
| `ppp_async` |  |  |
| `ppp_deflate` |  |  |
| `ppp_generic` |  |  |
| `ppp_mppe` | 1.0.2 | Point-to-Point Protocol Microsoft Point-to-Point Encryption support |
| `ppp_synctty` |  |  |
| `pppoe` |  | PPP over Ethernet driver |
| `pppox` |  | PPP over Ethernet driver (generic socket layer) |
| `pptp` |  | Point-to-Point Tunneling Protocol |
| `rionet` |  | Ethernet over RapidIO |
| `slhc` |  |  |
| `slip` |  |  |
| `sungem_phy` |  |  |
| `tap` |  |  |
| `team` |  | Ethernet team device driver |
| `team_mode_activebackup` |  | Active-backup mode for team |
| `team_mode_broadcast` |  | Broadcast mode for team |
| `team_mode_loadbalance` |  | Load-balancing mode for team |
| `team_mode_random` |  | Random mode for team |
| `team_mode_roundrobin` |  | Round-robin mode for team |
| `thunderbolt-net` |  | Thunderbolt network driver |
| `tun` |  | Universal TUN/TAP device driver |
| `asix` | 22-Dec-2011 | ASIX AX8817X based USB 2.0 Ethernet Devices |
| `ax88179_178a` |  | ASIX AX88179/178A based USB 3.0/2.0 Gigabit Ethernet Devices |
| `catc` |  | CATC EL1210A NetMate USB Ethernet driver |
| `cdc-phonet` |  | USB CDC Phonet host interface |
| `cdc_eem` |  | USB CDC EEM |
| `cdc_ether` |  | USB CDC Ethernet devices |
| `cdc_mbim` |  | USB CDC MBIM host driver |
| `cdc_ncm` |  | USB CDC NCM host driver |
| `cdc_subset` |  | Simple 'CDC Subset' USB networking links |
| `ch9200` |  | QinHeng CH9200 USB Network device |
| `cx82310_eth` |  | Conexant CX82310-based ADSL router USB ethernet driver |
| `dm9601` |  | Davicom DM96xx USB 10/100 ethernet devices |
| `gl620a` |  | GL620-USB-A Host-to-Host Link cables |
| `hso` |  | USB High Speed Option driver |
| `huawei_cdc_ncm` |  | USB CDC NCM host driver with encapsulated protocol support |
| `int51x1` |  | Intellon usb powerline adapter |
| `ipheth` |  | Apple iPhone USB Ethernet driver |
| `kalmia` |  | Samsung Kalmia USB network driver |
| `kaweth` |  | KL5USB101 USB Ethernet driver |
| `lan78xx` |  | LAN78XX USB 3.0 Gigabit Ethernet Devices |
| `lg-vl600` |  | LG-VL600 modem's ethernet link |
| `mcs7830` |  | USB to network adapter MCS7830) |
| `net1080` |  | NetChip 1080 based USB Host-to-Host Links |
| `pegasus` |  | Pegasus/Pegasus II USB Ethernet driver |
| `plusb` |  | Prolific PL-2301/2302/25A1/27A1 USB Host to Host Link Driver |
| `qmi_wwan` |  | Qualcomm MSM Interface (QMI) WWAN driver |
| `r8152` | v1.10.11 | Realtek RTL8152/RTL8153 Based USB Ethernet Adapters |
| `rndis_host` |  | USB Host side RNDIS driver |
| `rtl8150` |  | rtl8150 based usb-ethernet driver |
| `sierra_net` | v.2.0 | USB-to-WWAN Driver for Sierra Wireless modems |
| `smsc75xx` |  | SMSC75XX USB 2.0 Gigabit Ethernet Devices |
| `smsc95xx` |  | SMSC95XX USB 2.0 Ethernet Devices |
| `sr9700` |  | SR9700 one chip USB 1.1 USB to Ethernet device from http://www.corechip-sz.com/ |
| `sr9800` | 11-Nov-2013 | SR9800 USB 2.0 USB2NET Dev : http://www.corechip-sz.com |
| `usbnet` |  | USB network driver framework |
| `zaurus` |  | Sharp Zaurus PDA, and compatible products |
| `veth` |  | Virtual Ethernet Tunnel |
| `virtio_net` |  | Virtio network driver |
| `vmxnet3` | 1.4.17.0-k | VMware vmxnet3 virtual NIC driver |
| `vsockmon` |  | Vsock monitoring device. Based on nlmon device. |
| `vxlan` | 0.1 | Driver for VXLAN encapsulated traffic |
| `dlci` |  | Frame Relay DLCI layer |
| `hdlc` |  | HDLC support module |
| `hdlc_cisco` |  | Cisco HDLC protocol support for generic HDLC |
| `hdlc_fr` |  | Frame-Relay protocol support for generic HDLC |
| `hdlc_ppp` |  | PPP protocol support for generic HDLC |
| `hdlc_raw` |  | Raw HDLC protocol support for generic HDLC |
| `i2400m-usb` |  | Driver for USB based Intel Wireless WiMAX Connection 2400M (5x50 & 6050) |
| `i2400m` |  | Intel 2400M WiMAX networking bus-generic driver |
| `wireguard` | 1.0.0 | WireGuard secure network tunnel |
| `adm8211` |  | Driver for IEEE 802.11b wireless cards based on ADMtek ADM8211 |
| `ath` |  | Shared library for Atheros wireless LAN cards. |
| `ath10k_core` |  | Core module for Qualcomm Atheros 802.11ac wireless LAN cards. |
| `ath9k` |  | Support for Atheros 802.11n wireless LAN cards. |
| `ath9k_common` |  | Shared library for Atheros wireless 802.11n LAN cards. |
| `ath9k_htc` |  | Atheros driver 802.11n HTC based wireless devices |
| `ath9k_hw` |  | Support for Atheros 802.11n wireless LAN cards. |
| `carl9170` |  | Atheros AR9170 802.11n USB wireless |
| `wil6210` |  | Driver for 60g WiFi WIL6210 card |
| `at76c50x-usb` |  | Atmel at76x USB Wireless LAN Driver |
| `atmel` |  | Support for Atmel at76c50x 802.11 wireless ethernet cards. |
| `atmel_pci` |  | Support for Atmel at76c50x 802.11 wireless ethernet cards. |
| `b43` |  | Broadcom B43 wireless driver |
| `b43legacy` |  | Broadcom B43legacy wireless driver |
| `brcmfmac` |  | Broadcom 802.11 wireless LAN fullmac driver. |
| `brcmsmac` |  | Broadcom 802.11n wireless LAN driver. |
| `brcmutil` |  | Broadcom 802.11n wireless LAN driver utilities. |
| `airo` |  | Support for Cisco/Aironet 802.11 wireless ethernet cards. Direct support for ISA/PCI/MPI cards and support for PCMCIA when used with airo\_cs. |
| `ipw2100` | git-1.2.2 | Intel(R) PRO/Wireless 2100 Network Driver |
| `ipw2200` | 1.2.2kdmprq | Intel(R) PRO/Wireless 2200/2915 Network Driver |
| `libipw` | git-1.1.13 | 802.11 data/management/control stack |
| `iwl3945` | in-tree:ds | Intel(R) PRO/Wireless 3945ABG/BG Network Connection driver for Linux |
| `iwl4965` | in-tree:d | Intel(R) Wireless WiFi 4965 driver for Linux |
| `iwlegacy` | in-tree: | iwl-legacy: common functions for 3945 and 4965 |
| `iwldvm` |  | Intel(R) Wireless WiFi Link AGN driver for Linux |
| `iwlwifi` |  | Intel(R) Wireless WiFi driver for Linux |
| `iwlmvm` |  | The new Intel(R) wireless AGN driver for Linux |
| `hostap` |  | Host AP common routines |
| `hostap_pci` |  | Support for Intersil Prism2.5-based 802.11 wireless LAN PCI cards. |
| `hostap_plx` |  | Support for Intersil Prism2-based 802.11 wireless LAN cards (PLX). |
| `orinoco` |  | Driver for Lucent Orinoco, Prism II based and similar wireless cards |
| `orinoco_nortel` |  | Driver for wireless LAN cards using the Nortel PCI bridge |
| `orinoco_plx` |  | Driver for wireless LAN cards using the PLX9052 PCI bridge |
| `orinoco_tmd` |  | Driver for wireless LAN cards using the TMD7160 PCI bridge |
| `p54common` |  | Softmac Prism54 common code |
| `p54pci` |  | Prism54 PCI wireless driver |
| `p54usb` |  | Prism54 USB wireless driver |
| `mac80211_hwsim` |  | Software simulator of 802.11 radio(s) for mac80211 |
| `libertas` |  | Libertas WLAN Driver Library |
| `libertas_sdio` |  | Libertas SDIO WLAN Driver |
| `usb8xxx` |  | 8388 USB WLAN Driver |
| `libertas_tf` |  | Libertas WLAN Thinfirm Driver Library |
| `libertas_tf_usb` |  | 8388 USB WLAN Thinfirm Driver |
| `mwifiex` | 1.0 | Marvell WiFi-Ex Driver version 1.0 |
| `mwifiex_pcie` | 1.0 | Marvell WiFi-Ex PCI-Express Driver version 1.0 |
| `mwifiex_sdio` | 1.0 | Marvell WiFi-Ex SDIO Driver version 1.0 |
| `mwifiex_usb` | 1.0 | Marvell WiFi-Ex USB Driver version1.0 |
| `mwl8k` | 0.13 | Marvell TOPDOG(R) 802.11 Wireless Network Driver |
| `mt76-usb` |  |  |
| `mt76` |  |  |
| `mt76x0-common` |  |  |
| `mt76x0u` |  |  |
| `mt76x02-lib` |  |  |
| `mt76x02-usb` |  |  |
| `mt76x2-common` |  |  |
| `mt76x2u` |  |  |
| `mt7601u` |  |  |
| `rt2400pci` | 2.3.0 | Ralink RT2400 PCI & PCMCIA Wireless LAN driver. |
| `rt2500pci` | 2.3.0 | Ralink RT2500 PCI & PCMCIA Wireless LAN driver. |
| `rt2500usb` | 2.3.0 | Ralink RT2500 USB Wireless LAN driver. |
| `rt2800lib` | 2.3.0 | Ralink RT2800 library |
| `rt2800mmio` | 2.3.0 | rt2800 MMIO library |
| `rt2800pci` | 2.3.0 | Ralink RT2800 PCI & PCMCIA Wireless LAN driver. |
| `rt2800usb` | 2.3.0 | Ralink RT2800 USB Wireless LAN driver. |
| `rt2x00lib` | 2.3.0 | rt2x00 library |
| `rt2x00mmio` | 2.3.0 | rt2x00 mmio library |
| `rt2x00pci` | 2.3.0 | rt2x00 pci library |
| `rt2x00usb` | 2.3.0 | rt2x00 usb library |
| `rt61pci` | 2.3.0 | Ralink RT61 PCI & PCMCIA Wireless LAN driver. |
| `rt73usb` | 2.3.0 | Ralink RT73 USB Wireless LAN driver. |
| `rtl818x_pci` |  | RTL8180 / RTL8185 / RTL8187SE PCI wireless driver |
| `rtl8187` |  | RTL8187/RTL8187B USB wireless driver |
| `rtl8xxxu` |  | RTL8XXXu USB mac80211 Wireless LAN Driver |
| `btcoexist` |  | Realtek 802.11n PCI wireless core |
| `rtl8188ee` |  | Realtek 8188E 802.11n PCI wireless |
| `rtl8192c-common` |  | Realtek 8192C/8188C 802.11n PCI wireless |
| `rtl8192ce` |  | Realtek 8192C/8188C 802.11n PCI wireless |
| `rtl8192cu` |  | Realtek 8192C/8188C 802.11n USB wireless |
| `rtl8192de` |  | Realtek 8192DE 802.11n Dual Mac PCI wireless |
| `rtl8192ee` |  | Realtek 8192EE 802.11n PCI wireless |
| `rtl8192se` |  | Realtek 8192S/8191S 802.11n PCI wireless |
| `rtl8723ae` |  | Realtek 8723E 802.11n PCI wireless |
| `rtl8723be` |  | Realtek 8723BE 802.11n PCI wireless |
| `rtl8723-common` |  | Realtek RTL8723AE/RTL8723BE 802.11n PCI wireless common routines |
| `rtl8821ae` |  | Realtek 8821ae 802.11ac PCI wireless |
| `rtl_pci` |  | PCI basic driver for rtlwifi |
| `rtl_usb` |  | USB basic driver for rtlwifi |
| `rtlwifi` |  | Realtek 802.11n PCI wireless core |
| `rtw88` |  | Realtek 802.11ac wireless core module |
| `rtwpci` |  | Realtek 802.11ac wireless PCI driver |
| `rndis_wlan` |  | Driver for RNDIS based USB Wireless adapters |
| `wl1251` |  | TI wl1251 Wireless LAN Driver Core |
| `wl1251_sdio` |  |  |
| `zd1201` | 0.15 | Driver for ZyDAS ZD1201 based USB Wireless adapters |
| `zd1211rw` | 1.0 | USB driver for devices with the ZD1211 chip. |
| `xen-netback` |  |  |
| `xen-netfront` |  | Xen virtual network device frontend |

### `ntb` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `ntb` | 1.0 | PCIe NTB Driver Framework |
| `ntb_transport` | 4 | Software Queue-Pair Transport over NTB |

### `nvdimm` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `libnvdimm` |  |  |
| `nd_blk` |  |  |
| `nd_btt` |  |  |
| `nd_e820` |  |  |
| `nd_pmem` |  |  |
| `nd_virtio` |  |  |
| `virtio_pmem` |  | Virtio pmem driver |

### `nvme` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `nvme-core` | 1.0 |  |
| `nvme-fabrics` |  |  |
| `nvme-fc` |  |  |
| `nvme-rdma` |  |  |
| `nvme-tcp` |  |  |
| `nvme` | 1.0 |  |
| `nvme-fcloop` |  |  |
| `nvme-loop` |  |  |
| `nvmet-fc` |  |  |
| `nvmet-rdma` |  |  |
| `nvmet-tcp` |  |  |
| `nvmet` |  |  |

### `parport` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `parport` |  |  |
| `parport_pc` |  | PC-style parallel port driver |
| `parport_serial` |  | Driver for common parallel+serial multi-I/O PCI cards |

### `pci` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `pci-hyperv-intf` |  | Hyper-V PCI Interface |
| `pci-hyperv` |  | Hyper-V PCI |
| `vmd` | 0.6 |  |
| `acpiphp_ibm` | 1.0.1 | ACPI Hot Plug PCI Controller Driver IBM extension |
| `pci-pf-stub` |  |  |
| `aer_inject` |  | PCIe AER software error injector |

### `pcmcia` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `yenta_socket` |  |  |

### `pinctrl` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `pinctrl-broxton` |  | Intel Broxton SoC pinctrl/GPIO driver |
| `pinctrl-cannonlake` |  | Intel Cannon Lake PCH pinctrl/GPIO driver |
| `pinctrl-cedarfork` |  | Intel Cedar Fork PCH pinctrl/GPIO driver |
| `pinctrl-denverton` |  | Intel Denverton SoC pinctrl/GPIO driver |
| `pinctrl-geminilake` |  | Intel Gemini Lake SoC pinctrl/GPIO driver |
| `pinctrl-icelake` |  | Intel Ice Lake PCH pinctrl/GPIO driver |
| `pinctrl-intel` |  | Intel pinctrl/GPIO core driver |
| `pinctrl-lewisburg` |  | Intel Lewisburg pinctrl/GPIO driver |
| `pinctrl-sunrisepoint` |  | Intel Sunrisepoint PCH pinctrl/GPIO driver |
| `pinctrl-amd` |  | AMD GPIO pinctrl driver |

### `platform` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `chromeos_laptop` |  | Chrome OS Laptop driver |
| `chromeos_pstore` |  | ChromeOS pstore module |
| `acer-wmi` |  | Acer Laptop WMI Extras Driver |
| `acerhdf` |  | Aspire One temperature and fan driver |
| `amilo-rfkill` |  |  |
| `apple-gmux` |  | Apple Gmux Driver |
| `asus-laptop` |  | Asus Laptop Support |
| `asus-nb-wmi` |  | Asus Notebooks WMI Hotkey Driver |
| `asus-wmi` |  | Asus Generic WMI Driver |
| `classmate-laptop` |  |  |
| `compal-laptop` | 0.2.7 | Compal Laptop Support |
| `dcdbas` | 5.6.0-3.3 | Dell Systems Management Base Driver (version 5.6.0-3.3) |
| `dell-laptop` |  | Dell laptop driver |
| `dell-rbtn` |  | Dell Airplane Mode Switch driver |
| `dell-smbios` |  | Common functions for kernel modules using Dell SMBIOS |
| `dell-smo8800` |  | Dell Latitude freefall driver (ACPI SMO88XX) |
| `dell-wmi-aio` |  | WMI hotkeys driver for Dell All-In-One series |
| `dell-wmi-descriptor` |  | Dell WMI descriptor driver |
| `dell-wmi-led` |  | Dell LED Control Driver |
| `dell-wmi` |  | Dell laptop WMI hotkeys driver |
| `dell_rbu` | 3.2 | Driver for updating BIOS image on DELL systems |
| `eeepc-laptop` |  | Eee PC Hotkey Driver |
| `eeepc-wmi` |  | Eee PC WMI Hotkey Driver |
| `fujitsu-laptop` | 0.6.0 | Fujitsu laptop extras support |
| `fujitsu-tablet` | 2.5 | Fujitsu tablet pc extras driver |
| `hdaps` |  | IBM Hard Drive Active Protection System (HDAPS) driver |
| `hp-wireless` |  |  |
| `hp-wmi` |  | HP laptop WMI hotkeys driver |
| `hp_accel` |  | Glue between LIS3LV02Dx and HP ACPI BIOS and support for disk protection LED. |
| `ibm_rtl` |  |  |
| `ideapad-laptop` |  | IdeaPad ACPI Extras |
| `intel-hid` |  |  |
| `intel-rst` |  |  |
| `intel-smartconnect` |  |  |
| `intel-vbtn` |  |  |
| `intel-wmi-thunderbolt` |  | Intel WMI Thunderbolt force power driver |
| `intel_ips` |  | Intelligent Power Sharing Driver |
| `intel_oaktrail` | 0.4ac1 | Intel Oaktrail Platform ACPI Extras |
| `isst_if_common` |  |  |
| `isst_if_mbox_msr` |  | Intel speed select interface mailbox driver |
| `isst_if_mbox_pci` |  | Intel speed select interface pci mailbox driver |
| `isst_if_mmio` |  | Intel speed select interface mmio driver |
| `mlx-platform` |  | Mellanox platform driver |
| `msi-laptop` | 0.5 | MSI Laptop Support |
| `msi-wmi` |  | MSI laptop WMI hotkeys driver |
| `mxm-wmi` |  | MXM WMI Driver |
| `panasonic-laptop` |  | ACPI HotKey driver for Panasonic Let's Note laptops |
| `samsung-laptop` |  | Samsung Backlight driver |
| `samsung-q10` |  | Samsung Q10 Driver |
| `sony-laptop` |  | Sony laptop extras driver (SPIC and SNC ACPI device) |
| `thinkpad_acpi` | 0.26 | ThinkPad ACPI Extras |
| `topstar-laptop` |  | Topstar Laptop ACPI Extras driver |
| `toshiba_acpi` |  | Toshiba Laptop ACPI Extras Driver |
| `toshiba_bluetooth` |  | Toshiba Laptop ACPI Bluetooth Enable Driver |
| `wmi-bmof` |  | WMI embedded Binary MOF driver |
| `wmi` |  | ACPI-WMI Mapping Driver |

### `power` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `bq2415x_charger` |  | bq2415x charger driver |
| `bq24190_charger` |  | TI BQ24190 Charger Driver |
| `bq24735-charger` |  | bq24735 battery charging driver |
| `ds2780_battery` |  | Maxim/Dallas DS2780 Stand-Alone Fuel Gauge IC driver |
| `ds2781_battery` |  | Maxim/Dallas DS2781 Stand-Alone Fuel Gauge IC driver |
| `ds2782_battery` |  | Maxim/Dallas DS2782 Stand-Alone Fuel Gauge IC driver |
| `gpio-charger` |  | Driver for chargers which report their online status through a GPIO |
| `isp1704_charger` |  | ISP170x USB Charger driver |
| `lp8727_charger` |  | TI/National Semiconductor LP8727 charger driver |
| `max17040_battery` |  | MAX17040 Fuel Gauge |
| `max17042_battery` |  | MAX17042 Fuel Gauge |
| `max8903_charger` |  | MAX8903 Charger Driver |
| `sbs-battery` |  | SBS battery monitor driver |
| `smb347-charger` |  | SMB347 battery charger driver |

### `powercap` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `intel_rapl_common` |  | Intel Runtime Average Power Limit (RAPL) common code |
| `intel_rapl_msr` |  | Driver for Intel RAPL (Running Average Power Limit) control via MSR interface |

### `pps` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `pps-gpio` | 1.2.0 | Use GPIO pin as PPS source |
| `pps-ldisc` |  | PPS TTY device driver |
| `pps_parport` |  | parallel port PPS client |

### `ptp` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `ptp_kvm` |  | PTP clock using KVMCLOCK |

### `regulator` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `fixed` |  | Fixed voltage regulator |
| `lp3971` |  | LP3971 PMIC driver |
| `max1586` |  | MAXIM 1586 voltage regulator driver |
| `tps65023-regulator` |  | TPS65023 voltage regulator driver |
| `tps6507x-regulator` |  | TPS6507x voltage regulator driver |
| `userspace-consumer` |  | Userspace consumer for voltage and current regulators |

### `rtc` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `rtc-bq32k` |  | TI BQ32000 I2C RTC driver |
| `rtc-bq4802` |  | TI BQ4802 RTC driver |
| `rtc-ds1286` |  | DS1286 RTC driver |
| `rtc-ds1307` |  | RTC driver for DS1307 and similar chips |
| `rtc-ds1374` |  | Maxim/Dallas DS1374 RTC Driver |
| `rtc-ds1511` |  | Dallas DS1511 RTC driver |
| `rtc-ds1553` |  | Dallas DS1553 RTC driver |
| `rtc-ds1672` |  | Dallas/Maxim DS1672 timekeeper driver |
| `rtc-ds1742` |  | Dallas DS1742 RTC driver |
| `rtc-ds2404` |  | DS2404 RTC |
| `rtc-ds3232` |  | Maxim/Dallas DS3232/DS3234 RTC Driver |
| `rtc-em3027` |  | EM Microelectronic EM3027 RTC driver |
| `rtc-fm3130` |  | RTC driver for FM3130 |
| `rtc-isl12022` |  | ISL 12022 RTC driver |
| `rtc-isl1208` |  | Intersil ISL1208 RTC driver |
| `rtc-m41t80` |  | ST Microelectronics M41T80 series RTC I2C Client Driver |
| `rtc-m48t35` |  | M48T35 RTC driver |
| `rtc-m48t59` |  | M48T59/M48T02/M48T08 RTC driver |
| `rtc-m48t86` |  | M48T86 RTC driver |
| `rtc-max6900` |  | Maxim MAX6900 RTC driver |
| `rtc-msm6242` |  | Oki MSM6242 RTC driver |
| `rtc-pcf2127` |  | NXP PCF2127/29 RTC driver |
| `rtc-pcf50633` |  | PCF50633 RTC driver |
| `rtc-pcf85063` |  | PCF85063 RTC driver |
| `rtc-pcf8523` |  | NXP PCF8523 RTC driver |
| `rtc-pcf8563` |  | Philips PCF8563/Epson RTC8564 RTC driver |
| `rtc-pcf8583` |  | PCF8583 I2C RTC driver |
| `rtc-rp5c01` |  | Ricoh RP5C01 RTC driver |
| `rtc-rs5c372` |  | Ricoh RS5C372 RTC driver |
| `rtc-rv3029c2` |  | Micro Crystal RV3029/RV3049 RTC driver |
| `rtc-rx8025` |  | RX-8025 SA/NB RTC driver |
| `rtc-rx8581` |  | Epson RX-8571/RX-8581 RTC driver |
| `rtc-s35390a` |  | S35390A RTC driver |
| `rtc-stk17ta8` |  | Simtek STK17TA8 RTC driver |
| `rtc-v3020` |  | V3020 RTC |
| `rtc-x1205` |  | Xicor/Intersil X1205 RTC driver |

### `scsi` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `3w-9xxx` | 2.26.02.014 | 3ware 9000 Storage Controller Linux Driver |
| `3w-sas` | 3.26.02.000 | LSI 3ware SAS/SATA-RAID Linux Driver |
| `aacraid` | 1.2.1[50877]-custom | Dell PERC2, 2/Si, 3/Si, 3/Di, Adaptec Advanced Raid Products, HP NetRAID-4M, IBM ServeRAID & ICP SCSI driver |
| `aic79xx` | 3.0 | Adaptec AIC790X U320 SCSI Host Bus Adapter driver |
| `aic7xxx` | 7.0 | Adaptec AIC77XX/78XX SCSI Host Bus Adapter driver |
| `aic94xx` | 1.0.3 | Adaptec aic94xx SAS/SATA driver |
| `arcmsr` | v1.40.00.10-20190116 | Areca ARC11xx/12xx/16xx/188x SAS/SATA RAID Controller Driver |
| `be2iscsi` | 11.4.0.1 | Emulex OneConnectOpen-iSCSI Driver version11.4.0.1 Driver 11.4.0.1 |
| `bfa` | 3.2.25.1 | QLogic BR-series Fibre Channel HBA Driver fcpim |
| `bnx2fc` | 2.12.10 | QLogic FCoE Driver |
| `bnx2i` | 2.7.10.1 | QLogic NetXtreme II BCM5706/5708/5709/57710/57711/57712/57800/57810/57840 iSCSI Driver |
| `ch` |  | device driver for scsi media changer devices |
| `csiostor` | 1.0.0-ko | Chelsio FCoE driver |
| `cxgb3i` | 2.0.1-ko | Chelsio T3 iSCSI Driver |
| `cxgb4i` | 0.9.5-ko | Chelsio T4-T6 iSCSI Driver |
| `libcxgbi` | 0.9.1-ko | Chelsio iSCSI driver library |
| `fcoe` |  | FCoE |
| `libfcoe` |  | FIP discovery protocol and FCoE transport for FCoE HBAs |
| `fnic` | 1.6.0.47 | Cisco FCoE HBA Driver |
| `hpsa` | 3.4.20-170 | Driver for HP Smart Array Controller version 3.4.20-170 |
| `hptiop` |  | HighPoint RocketRAID 3xxx/4xxx Controller Driver |
| `hv_storvsc` |  | Microsoft Hyper-V virtual storage driver |
| `imm` |  |  |
| `initio` |  | Initio INI-9X00U/UW SCSI device driver |
| `ips` | 7.12.05 | IBM ServeRAID Adapter Driver 7.12.05 |
| `isci` | 1.2.0 |  |
| `iscsi_boot_sysfs` |  | sysfs interface and helpers to export iSCSI boot information |
| `iscsi_tcp` |  | iSCSI/TCP data-path |
| `libfc` |  | libfc |
| `libiscsi` |  | iSCSI library functions |
| `libiscsi_tcp` |  | iSCSI/TCP data-path |
| `libsas` |  | SAS Transport Layer |
| `lpfc` | 0:12.8.0.5 | Emulex LightPulse Fibre Channel SCSI driver 12.8.0.5 |
| `megaraid_mbox` | 2.20.5.1 | LSI Logic MegaRAID Mailbox Driver |
| `megaraid_mm` | 2.20.2.7 | LSI Logic Management Module |
| `megaraid_sas` | 07.714.04.00-rc1 | Broadcom MegaRAID SAS Driver |
| `mpt3sas` | 36.100.00.00 | LSI MPT Fusion SAS 3.0 Device Driver |
| `mvsas` | 0.8.16 | Marvell 88SE6440 SAS/SATA controller driver |
| `mvumi` |  | Marvell UMI Driver |
| `pm80xx` | 0.1.39 | PMC-Sierra PM8001/8006/8081/8088/8089/8074/8076/8077/8070/8072 SAS/SATA controller driver |
| `pmcraid` | 1.0.3 | PMC Sierra MaxRAID Controller Driver |
| `ppa` |  |  |
| `qedf` | 8.42.3.0 | QLogic FastLinQ 4xxxx FCoE Module |
| `qedi` | 8.37.0.20 | QLogic FastLinQ 4xxxx iSCSI Module |
| `qla2xxx` |  | QLogic Fibre Channel HBA Driver |
| `tcm_qla2xxx` |  | TCM QLA24XX+ series NPIV enabled fabric driver |
| `qla4xxx` | 5.04.00-k6 | QLogic iSCSI HBA Driver |
| `raid_class` |  | RAID device class |
| `scsi_debug` | 0188 | SCSI debug adapter driver |
| `scsi_transport_fc` |  | FC Transport Attributes |
| `scsi_transport_iscsi` | 2.0-870 | iSCSI Transport Interface |
| `scsi_transport_sas` |  | SAS Transport Attributes |
| `scsi_transport_spi` |  | SPI Transport Attributes |
| `scsi_transport_srp` |  | SRP Transport Attributes |
| `sd_mod` |  | SCSI disk (sd) driver |
| `ses` |  | SCSI Enclosure Services (ses) driver |
| `sg` | 3.5.36 | SCSI generic (sg) driver |
| `smartpqi` | 1.2.10-025 | Driver for Microsemi Smart Family Controller version 1.2.10-025 |
| `snic` | 0.0.1.18 | Cisco SCSI NIC Driver |
| `sr_mod` |  | SCSI cdrom (sr) driver |
| `st` |  | SCSI tape (st) driver |
| `stex` | 6.02.0000.01 | Promise Technology SuperTrak EX Controllers |
| `sym53c8xx` | 2.2.3 | NCR, Symbios and LSI 8xx and 1010 PCI SCSI adapters |
| `ufshcd-core` | 0.2 | Generic UFS host controller driver Core |
| `ufshcd-pci` | 0.2 | UFS host controller PCI glue driver |
| `virtio_scsi` |  | Virtio SCSI HBA driver |
| `vmw_pvscsi` | 1.0.7.0-k | VMware PVSCSI driver |
| `xen-scsifront` |  | Xen SCSI frontend driver |

### `ssb` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `ssb` |  | Sonics Silicon Backplane driver |

### `staging` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `exfat` |  | exFAT Filesystem Driver |
| `firewire-serial` |  | FireWire Serial TTY Driver |
| `b1` |  | CAPI4Linux: Common support for active AVM cards |
| `b1dma` |  | CAPI4Linux: DMA support for active AVM cards |
| `b1pci` |  | CAPI4Linux: Driver for AVM B1 PCI card |
| `c4` |  | CAPI4Linux: Driver for AVM C2/C4 cards |
| `t1pci` |  | CAPI4Linux: Driver for AVM T1 PCI card |
| `bas_gigaset` |  | USB Driver for Gigaset 307x |
| `gigaset` |  | Driver for Gigaset 307x |
| `ser_gigaset` |  | Serial Driver for Gigaset 307x using Siemens M101 |
| `usb_gigaset` |  | USB Driver for Gigaset 307x using M105 |
| `hysdn` |  | ISDN4Linux: Driver for HYSDN cards |
| `qlge` | 1.00.00.35 | QLogic 10 Gigabit PCI-E Ethernet Driver |
| `r8192e_pci` | 0014.0401.2010 | Linux driver for Realtek RTL819x WiFi cards |
| `rtllib` |  |  |
| `rtllib_crypt_ccmp` |  |  |
| `rtllib_crypt_tkip` |  |  |
| `rtllib_crypt_wep` |  |  |
| `r8712u` |  | rtl871x wireless lan driver |
| `hwa-rc` |  | Host Wireless Adapter Radio Control Driver |
| `i1480-dfu-usb` |  | Intel Wireless UWB Link 1480 firmware uploader for USB |
| `i1480-est` |  | i1480's Vendor Specific Event Size Tables |
| `umc` |  | UWB Multi-interface Controller capability bus |
| `uwb` |  | Ultra Wide Band core |
| `whc-rc` |  | Wireless Host Controller Radio Control Driver |
| `whci` |  | WHCI UWB Multi-interface Controller enumerator |
| `hwa-hc` |  | Host Wired Adapter USB Host Control Driver |
| `whci-hcd` |  | WHCI Wireless USB host controller driver |
| `wusb-cbaf` |  | Wireless USB Cable Based Association |
| `wusb-wa` |  | Wireless USB Wire Adapter core |
| `wusbcore` |  | Wireless USB core |

### `target` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `cxgbit` | 1.0.0-ko | Chelsio iSCSI target offload driver |
| `iscsi_target_mod` | 4.1.x | iSCSI-Target Driver for mainline target infrastructure |
| `tcm_loop` |  | TCM loopback virtual Linux/SCSI fabric module |
| `target_core_file` |  | TCM FILEIO subsystem plugin |
| `target_core_iblock` |  | TCM IBLOCK subsystem plugin |
| `target_core_mod` |  | Target\_Core\_Mod/ConfigFS |
| `target_core_pscsi` |  | TCM PSCSI subsystem plugin |
| `target_core_user` |  | TCM USER subsystem plugin |
| `tcm_fc` |  | FC TCM fabric driver 0.4 |

### `tee` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `amdtee` | 1.0 | AMD-TEE driver |
| `tee` | 1.0 | TEE Driver |

### `thermal` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `acpi_thermal_rel` |  | Intel acpi thermal rel misc dev driver |
| `int3400_thermal` |  | INT3400 Thermal driver |
| `int3402_thermal` |  | INT3402 Thermal driver |
| `int3403_thermal` |  | ACPI INT3403 thermal driver |
| `int340x_thermal_zone` |  | Intel INT340x common thermal zone handler |
| `processor_thermal_device` |  | Processor Thermal Reporting Device Driver |
| `intel_pch_thermal` |  | Intel PCH Thermal driver |
| `intel_powerclamp` |  | Package Level C-state Idle Injection for Intel CPUs |
| `intel_soc_dts_iosf` |  |  |
| `x86_pkg_temp_thermal` |  | X86 PKG TEMP Thermal Driver |

### `tty` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `cyclades` | 2.6 |  |
| `n_gsm` |  |  |
| `n_hdlc` |  |  |
| `nozomi` |  | Nozomi driver |
| `altera_jtaguart` |  | Altera JTAG UART driver |
| `altera_uart` |  | Altera UART driver |
| `arc_uart` |  | ARC(Synopsys) On-Chip(fpga) serial driver |
| `jsm` |  | Driver for the Digi International Neo and Classic PCI based product line |
| `synclink` |  |  |
| `synclink_gt` |  |  |
| `synclinkmp` |  |  |

### `uio` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `uio` |  |  |
| `uio_aec` |  |  |
| `uio_cif` |  |  |
| `uio_hv_generic` | 0.02.1 | Generic UIO driver for VMBus devices |
| `uio_pci_generic` | 0.01.0 | Generic UIO driver for PCI 2.3 devices |
| `uio_pdrv_genirq` |  | Userspace I/O platform driver with generic IRQ handling |
| `uio_sercos3` |  | UIO driver for the Automata Sercos III PCI card |

### `usb` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `cxacru` |  | Conexant AccessRunner ADSL USB modem driver |
| `speedtch` |  | Alcatel SpeedTouch USB driver |
| `ueagle-atm` |  | ADI 930/Eagle USB ADSL Modem driver |
| `usbatm` |  | Generic USB ATM/DSL I/O |
| `xusbatm` |  | Driver for USB ADSL modems initialized in userspace |
| `cdc-acm` |  | USB Abstract Control Model driver for USB modems and ISDN adapters |
| `cdc-wdm` |  | USB Abstract Control Model driver for USB WCM Device Management |
| `usblp` |  | USB Printer Device Class driver |
| `usbtmc` |  |  |
| `ledtrig-usbport` |  | USB port trigger |
| `sl811-hcd` |  | SL811HS USB Host Controller Driver |
| `u132-hcd` |  | U132 USB Host Controller Driver |
| `mdc800` |  | USB Driver for Mustek MDC800 Digital Camera |
| `microtek` |  | Microtek Scanmaker X6 USB scanner driver |
| `adutux` |  | adutux (see www.ontrak.net) |
| `appledisplay` |  | Apple Cinema Display driver |
| `emi26` |  | Emagic EMI 2|6 firmware loader. |
| `emi62` |  | Emagic EMI 6|2m firmware loader. |
| `ezusb` |  |  |
| `ftdi-elan` |  | FTDI ELAN driver |
| `idmouse` |  | Siemens ID Mouse FingerTIP Sensor Driver |
| `iowarrior` |  | USB IO-Warrior driver |
| `isight_firmware` |  |  |
| `ldusb` |  | LD USB Driver |
| `legousbtower` |  | LEGO USB Tower Driver |
| `sisusbvga` |  | sisusbvga - Driver for Net2280/SiS315-based USB2VGA dongles |
| `usb3503` |  | USB3503 USB HUB driver |
| `usblcd` |  | USBLCD Driver Version 1.05 |
| `usbsevseg` |  | USB 7 Segment Driver |
| `uss720` |  | USB Parport Cable driver for Cables using the Lucent Technologies USS720 Chip |
| `phy-generic` |  | NOP USB Transceiver driver |
| `aircable` |  | AIRcable USB Driver |
| `ark3116` |  | USB ARK3116 serial/IrDA driver |
| `belkin_sa` |  | USB Belkin Serial converter driver |
| `ch341` |  |  |
| `cp210x` |  | Silicon Labs CP210x RS232 serial adaptor driver |
| `cyberjack` |  | REINER SCT cyberJack pinpad/e-com USB Chipcard Reader Driver |
| `cypress_m8` |  | Cypress USB to Serial Driver |
| `digi_acceleport` |  | Digi AccelePort USB-2/USB-4 Serial Converter driver |
| `empeg` |  | USB Empeg Mark I/II Driver |
| `f81232` |  | Fintek F81232 USB to serial adaptor driver |
| `f81534` |  | Fintek F81532/F81534 |
| `ftdi_sio` |  | USB FTDI Serial Converters Driver |
| `garmin_gps` |  | garmin gps driver |
| `io_edgeport` |  | Edgeport USB Serial Driver |
| `io_ti` |  | Edgeport USB Serial Driver |
| `ipaq` |  | USB PocketPC PDA driver |
| `ipw` |  | IPWireless tty driver |
| `ir-usb` |  | USB IR Dongle driver |
| `iuu_phoenix` |  | Infinity USB Unlimited Phoenix driver |
| `keyspan` |  | Keyspan USB to Serial Converter Driver |
| `keyspan_pda` |  | USB Keyspan PDA Converter driver |
| `kl5kusb105` |  | KLSI KL5KUSB105 chipset USB->Serial Converter driver |
| `kobil_sct` |  | KOBIL USB Smart Card Terminal Driver (experimental) |
| `mct_u232` |  | Magic Control Technology USB-RS232 converter driver |
| `metro-usb` |  | Metrologic Instruments Inc. - USB-POS driver |
| `mos7720` |  | Moschip USB Serial Driver |
| `mos7840` |  | Moschip 7840/7820 USB Serial Driver |
| `mxuport` |  |  |
| `navman` |  |  |
| `omninet` |  | USB ZyXEL omni.net LCD PLUS Driver |
| `opticon` |  | Opticon USB barcode to serial driver (1D) |
| `option` |  | USB Driver for GSM modems |
| `oti6858` |  | Ours Technology Inc. OTi-6858 USB to serial adapter driver |
| `pl2303` |  | Prolific PL2303 USB to serial adaptor driver |
| `qcaux` |  |  |
| `qcserial` |  | Qualcomm USB Serial driver |
| `quatech2` |  | Quatech 2nd gen USB to Serial Driver |
| `safe_serial` |  | USB Safe Encapsulated Serial |
| `sierra` |  | USB Driver for Sierra Wireless USB modems |
| `spcp8x5` |  | SPCP8x5 USB to serial adaptor driver |
| `ssu100` |  | Quatech SSU-100 USB to Serial Driver |
| `symbolserial` |  |  |
| `ti_usb_3410_5052` |  | TI USB 3410/5052 Serial Driver |
| `upd78f0730` |  | Renesas uPD78F0730 USB to serial converter driver |
| `usb-serial-simple` |  |  |
| `usb_debug` |  |  |
| `usb_wwan` |  | USB Driver for GSM modems |
| `visor` |  | USB HandSpring Visor / Palm OS driver |
| `whiteheat` |  | USB ConnectTech WhiteHEAT driver |
| `wishbone-serial` |  | USB Wishbone-Serial adapter |
| `xsens_mt` |  | USB-serial driver for Xsens motion trackers |
| `uas` |  |  |
| `ums-alauda` |  | Driver for Alauda-based card readers |
| `ums-cypress` |  | SAT support for Cypress USB/ATA bridges with ATACB |
| `ums-datafab` |  | Driver for Datafab USB Compact Flash reader |
| `ums-eneub6250` |  | Driver for ENE UB6250 reader |
| `ums-freecom` |  | Driver for Freecom USB/IDE adaptor |
| `ums-isd200` |  | Driver for In-System Design, Inc. ISD200 ASIC |
| `ums-jumpshot` |  | Driver for Lexar "Jumpshot" Compact Flash reader |
| `ums-karma` |  | Driver for Rio Karma |
| `ums-onetouch` |  | Maxtor USB OneTouch hard drive button driver |
| `ums-realtek` |  | Driver for Realtek USB Card Reader |
| `ums-sddr09` |  | Driver for SanDisk SDDR-09 SmartMedia reader |
| `ums-sddr55` |  | Driver for SanDisk SDDR-55 SmartMedia reader |
| `ums-usbat` |  | Driver for SCM Microsystems (a.k.a. Shuttle) USB-ATAPI cable |
| `usb-storage` |  | USB Mass Storage driver for Linux |
| `typec_displayport` |  | DisplayPort Alternate Mode |
| `pi3usb30532` |  | Pericom PI3USB30532 Type-C mux driver |
| `tcpm` |  | USB Type-C Port Manager |
| `tps6598x` |  | TI TPS6598x USB Power Delivery Controller Driver |
| `typec` |  | USB Type-C Connector Class |
| `typec_ucsi` |  | USB Type-C Connector System Software Interface driver |
| `ucsi_acpi` |  | UCSI ACPI driver |
| `usbip-core` |  | USB/IP Core |

### `vdpa` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `mlx5_vdpa` |  | Mellanox VDPA driver |
| `vdpa` |  |  |
| `vdpa_sim` | 0.1 | vDPA Device Simulator |

### `vfio` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `mdev` | 0.1 | Mediated device Core Driver |
| `vfio_mdev` | 0.1 | VFIO based driver for Mediated device |
| `vfio-pci` | 0.2 | VFIO PCI - User Level meta-driver |
| `vfio_virqfd` | 0.1 | IRQFD support for VFIO bus drivers |

### `vhost` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `vhost` | 0.0.1 | Host kernel accelerator for virtio |
| `vhost_iotlb` | 0.1 | VHOST IOTLB |
| `vhost_net` | 0.0.1 | Host kernel accelerator for virtio net |
| `vhost_scsi` |  | VHOST\_SCSI series fabric driver |
| `vhost_vdpa` | 0.0.1 | vDPA-based vhost backend for virtio |
| `vhost_vsock` |  | vhost transport for vsock |
| `vringh` |  |  |

### `video` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `apple_bl` |  | Apple Backlight Driver |
| `lcd` |  | LCD Lowlevel Control Abstraction |
| `platform_lcd` |  |  |
| `aty128fb` |  | FBDev driver for ATI Rage128 / Pro cards |
| `atyfb` |  | FBDev driver for ATI Mach64 cards |
| `radeonfb` |  | framebuffer driver for ATI Radeon chipset |
| `cirrusfb` |  | Accelerated FBDev driver for Cirrus Logic chips |
| `fb_ddc` |  | DDC/EDID reading support |
| `fb_sys_fops` |  | Generic file read (fb in system RAM) |
| `syscopyarea` |  | Generic copyarea (sys-to-sys) |
| `sysfillrect` |  | Generic fill rectangle (sys-to-sys) |
| `sysimgblt` |  | 1-bit/8-bit to 1-32 bit color expansion (sys-to-sys) |
| `hyperv_fb` |  | Microsoft Hyper-V Synthetic Video Frame Buffer Driver |
| `macmodes` |  |  |
| `nvidiafb` |  | Framebuffer driver for nVidia graphics chipset |
| `rivafb` |  | Framebuffer driver for nVidia Riva 128, TNT, TNT2, and the GeForce series |
| `savagefb` |  | FBDev driver for S3 Savage PCI/AGP Chips |
| `sm501fb` |  | SM501 Framebuffer driver |
| `vfb` |  |  |
| `vga16fb` |  | Legacy VGA framebuffer device driver |
| `viafb` |  |  |
| `xen-fbfront` |  | Xen virtual framebuffer device frontend |
| `vgastate` |  | VGA State Save/Restore |

### `virtio` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `virtio_balloon` |  | Virtio balloon driver |
| `virtio_input` |  | Virtio input device driver |
| `virtio_pci` | 1 | virtio-pci |
| `virtio_vdpa` | 0.1 | vDPA bus driver for virtio devices |

### `w1` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `w1_ds2780` |  | 1-wire Driver for Maxim/Dallas DS2780 Stand-Alone Fuel Gauge IC |
| `w1_ds2781` |  | 1-wire Driver for Maxim/Dallas DS2781 Stand-Alone Fuel Gauge IC |
| `wire` |  | Driver for 1-wire Dallas network protocol. |

### `watchdog` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `acquirewdt` |  | Acquire Inc. Single Board Computer Watchdog Timer driver |
| `advantechwdt` |  | Advantech Single Board Computer WDT driver |
| `alim1535_wdt` |  | ALi M1535 PMU Watchdog Timer driver |
| `alim7101_wdt` |  | ALi M7101 PMU Computer Watchdog Timer driver |
| `cpu5wdt` |  | sma cpu5 watchdog driver |
| `eurotechwdt` |  | Driver for Eurotech CPU-1220/1410 on board watchdog |
| `f71808e_wdt` |  | F71808E Watchdog Driver |
| `hpwdt` | 2.0.3 | hpe watchdog driver |
| `i6300esb` |  | Watchdog driver for Intel 6300ESB chipsets |
| `iTCO_vendor_support` | 1.04 | Intel TCO Vendor Specific WatchDog Timer Driver Support |
| `iTCO_wdt` | 1.11 | Intel TCO WatchDog Timer Driver |
| `ib700wdt` |  | IB700 SBC watchdog driver |
| `ibmasr` |  | IBM Automatic Server Restart driver |
| `ie6xx_wdt` |  | Intel Atom E6xx Watchdog Device Driver |
| `it8712f_wdt` |  | IT8712F Watchdog Driver |
| `it87_wdt` |  | Hardware Watchdog Device Driver for IT87xx EC-LPC I/O |
| `machzwd` |  | MachZ ZF-Logic Watchdog driver |
| `mei_wdt` |  | Device driver for Intel MEI iAMT watchdog |
| `mena21_wdt` |  | MEN A21 Watchdog |
| `nv_tco` |  | TCO timer driver for NV chipsets |
| `of_xilinx_wdt` |  | Xilinx Watchdog driver |
| `pc87413_wdt` |  | PC87413 WDT driver |
| `pcwd_pci` |  | Berkshire PCI-PC Watchdog driver |
| `pcwd_usb` |  | Berkshire USB-PC Watchdog driver |
| `sbc60xxwdt` |  | 60xx Single Board Computer Watchdog Timer driver |
| `sbc_epx_c3` |  | Hardware Watchdog Device for Winsystems EPX-C3 SBC. Note that there is no way to probe for this device -- so only use it if you are \*sure\* you are running on this specific SBC system from Winsystems! It writes to IO ports 0x1ee and 0x1ef! |
| `sbc_fitpc2_wdt` |  | SBC-FITPC2 Watchdog |
| `sc1200wdt` |  | Driver for National Semiconductor PC87307/PC97307 watchdog component |
| `sch311x_wdt` |  | SMSC SCH311x WatchDog Timer Driver |
| `smsc37b787_wdt` |  | Driver for SMsC 37B787 watchdog component (Version 1.1) |
| `softdog` |  | Software Watchdog Device Driver |
| `sp5100_tco` |  | TCO timer driver for SP5100/SB800 chipset |
| `via_wdt` |  | Driver for watchdog timer on VIA chipset |
| `w83627hf_wdt` |  | w83627hf/thf WDT driver |
| `w83877f_wdt` |  | Driver for watchdog timer in w83877f chip |
| `w83977f_wdt` |  | Driver for watchdog timer in W83977F I/O chip |
| `wafer5823wdt` |  | ICP Wafer 5823 Single Board Computer WDT driver |
| `wdat_wdt` |  | ACPI Hardware Watchdog (WDAT) driver |
| `wdt_pci` |  | Driver for the ICS PCI-WDT500/501 watchdog cards |
| `xen_wdt` |  | Xen WatchDog Timer Driver |

### `xen` Drivers in UEK R6 (x86\_64)

| Driver | Version | Description |
| --- | --- | --- |
| `ovmapi` |  |  |
| `xen-acpi-processor` |  | Xen ACPI Processor P-states (and Cx) driver which uploads PM data to Xen hypervisor |
| `xen-evtchn` |  |  |
| `xen-front-pgdir-shbuf` |  | Xen frontend/backend page directory based shared buffer handling |
| `xen-gntalloc` |  | User-space grant reference allocator driver |
| `xen-gntdev` |  | User-space granted page access driver |
| `xen-privcmd` |  |  |
| `xen-scsiback` |  | Xen SCSI backend driver |
| `xenfs` |  | Xen filesystem |