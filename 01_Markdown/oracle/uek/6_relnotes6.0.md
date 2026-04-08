---
title: "Unbreakable Enterprise Kernel Release 6: Release Notes (5.4.17-2011)"
source_url: "https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "uek"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

Release Notes for Unbreakable Enterprise Kernel Release 6

F23078-21

January 2025

---

[Title and Copyright Information](#copyright-information)

Unbreakable Enterprise Kernel Release Notes for Unbreakable Enterprise Kernel Release 6

F23078-21

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2020, 2025, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-Preface.html -->

[Unbreakable Enterprise Kernel Release 6: Release
Notes (5.4.17-2011)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/) provides a summary of the new features, changes, and
known issues in the Unbreakable Enterprise Kernel Release 6.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/ref-conventions.html -->

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| boldface | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| italic | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/ref-doc-accessibility.html -->

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility
Program website at <https://www.oracle.com/corporate/accessibility/>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/ref-accessibility.html -->

Oracle customers that have purchased support have access to electronic support through My
Oracle Support. For information, visit <https://www.oracle.com/corporate/accessibility/learning-support.html#support-tab>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/ref-diversity.html -->

Oracle is fully committed to diversity and inclusion. Oracle respects and values having a
diverse workforce that increases thought leadership and innovation. As part of our
initiative to build a more inclusive culture that positively impacts our employees,
customers, and partners, we are working to remove insensitive terms from our products and
documentation. We are also mindful of the necessity to maintain compatibility with our
customers' existing technologies and the need to ensure continuity of service as Oracle's
offerings and industry standards evolve. Because of these technical constraints, our effort
to remove insensitive terms is ongoing and will take time and external cooperation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-NewFeaturesandChanges.html -->

Unbreakable Enterprise Kernel Release 6 (UEK R6) is a heavily tested and optimized operating
system kernel for Oracle Linux 7.7 and later and for Oracle Linux 8.1 and later.
The kernel is developed, built, and tested on Arm (aarch64)
Intel x86 and AMD x86 (x86\_64). platforms. It is based on the
mainline Linux kernel version 5.4. This release also
updates drivers and includes bug and security fixes.

Oracle actively monitors upstream check-ins and applies critical
bug and security fixes to UEK R6.

UEK R6 is initially released with the 5.4.17-2011 version and
build of the kernel.

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-NotableFeaturesandChanges.html -->

The following sections describe the major new features of
Unbreakable Enterprise Kernel Release 6 (UEK R6), relative to UEK R5. A summary list of the
key features in this release follows:

- Linux 5.4 stable kernel base

  The 5.4 mainline kernel release used as the
  base kernel for UEK R6 includes many upstream kernel
  features and improvements over previous releases and over
  RHCK. For a listing of major features and enhancements
  that are available in this kernel, as opposed to the
  previous major release of UEK, see
  [Core Kernel Functionality](uek6.0-NotableFeaturesandChanges.html#uek6-features-core-kernel).
- Arm Support

  Many features and improvements in this release are aimed
  at improved support for the Arm (aarch64) platform.
  Notable changes include security improvements and improved
  virtualization support on Arm. See
  [Arm (aarch64) Platform](uek6.0-NotableFeaturesandChanges.html#uek6-features-arm) for details.
- Cgroup v2 enhancements

  Cgroup v2 functionality was first introduced in UEK R5 to
  enable the CPU controller functionality. UEK R6 includes
  all Cgroup v2 features, along with several enhancements
  described in [Core Kernel Functionality](uek6.0-NotableFeaturesandChanges.html#uek6-features-core-kernel).
- ktask enhancements

  ktask is a framework for parallelizing CPU-intensive work
  in the kernel. It can be used to speed up large tasks on
  systems with a lot of available CPU power, where a task is
  single-threaded in user space. ktask provides a generic
  API that can add concurrency to many different kinds of
  tasks, while reducing the complexity around the management
  of multiple threads, and is currently used during struct
  page initialization and VFIO-enabled KVM guest
  initialization to significantly reduce start-up times.

  Documentation for ktask is provided in
  `/usr/share/doc/kernel-uek-doc-5.4/core-api/ktask.html`,
  though the interface is not yet stable.
- Parallelized kswapd

  Page replacement is handled in the kernel asynchronously
  by kswapd and synchronously by direct reclaim. When free
  pages within the zone free list are low, kswapd scans
  pages to determine if there are unused pages that can be
  evicted to free up space for new page allocations. This
  optimization can improve performance by avoiding direct
  reclaims, which can be resource intensive and
  time-consuming.
- Kexec firmware signing

  The option to check and validate a kernel image signature
  is enabled in UEK R6. When `kexec` is
  used to load a kernel from within UEK R6, kernel image
  signature checking and validation can be implemented to
  ensure that a system only loads a signed and validated
  kernel image.
- Memory management improvements

  Several performance enhancements have been implemented in
  the kernel's memory management code to improve the
  efficiency around clearing pages and cache, as well as
  enhancements to fault management and reporting. See
  [Memory Management](uek6.0-NotableFeaturesandChanges.html#uek6-features-mm) for more information.
- NVDIMM updates

  NVDIMM feature updates have been implemented so that
  persistent memory can now be used as traditional RAM and
  an update that helps to standardize the zero-key erase
  functionality has also been included. See
  [Core Kernel Functionality](uek6.0-NotableFeaturesandChanges.html#uek6-features-core-kernel) for more
  information.
- DTrace v2.0

  DTrace support is enabled in UEK R6 and has been
  reimplemented to use the Berkeley Packet Filter (BPF) that
  is integrated into the Linux kernel. The current version
  is the first Dtrace release based on the new
  implementation, it does not achieve feature parity with
  DTrace on UEK R5 yet, but it will in the future. Other
  improvements have been made to simplify the set of RPMs
  that are available for DTrace as a result of improvements
  in the upstream toolchain. See
  [DTrace v2.0](uek6.0-NotableFeaturesandChanges.html#uek6-features-dtrace) for
  more information.
- OCFS2

  Support for the OCFS2 file system is enabled in UEK R6.
  See [OCFS2](uek6.0-NotableFeaturesandChanges.html#uek6-features-ocfs2)
  for more information.
- Btrfs file system support

  Support for the Btrfs file system is enabled on Oracle Linux 8
  systems if UEK R6 is installed on the system. Further
  enhancements have been made to Btrfs in this release. See
  [Btrfs](uek6.0-NotableFeaturesandChanges.html#uek6-features-btrfs) for more
  information.

### Core Kernel Functionality

Several major core kernel features have been implemented in
the upstream kernel, between the 4.14 release that was used as
the base kernel version for UEK R5, and the 5.4
kernel release that is used as the base kernel version for
UEK R6. Although some features have been back-ported into the
UEK R5 kernel in update releases, the following significant
new features are available in UEK R6:

- Lockdown mode (x86\_64 only)

  Lockdown mode is significantly improved and there are
  several implementation changes that are worth noting.
  This release distinguishes between
  integrity and
  confidentiality modes. See
  [Security](uek6.0-NotableFeaturesandChanges.html#uek6-sec) for more information on this
  feature.
- fs-verity

  fs-verity is a kernel feature that file systems can hook
  into to for integrity and authenticity protection of
  read-only files. This facility can be used to detect
  non-malicious file corruption and malicious modification
  of files that should not be changed on a system. This
  feature currently only works with ext4 and f2fs file
  systems.
- High-performance asynchronous I/O with io\_uring

  This feature provides a fast, scalable asynchronous I/O
  interface for both buffered and unbuffered I/Os. It also
  supports asynchronous polled I/O. A user-space library,
  `liburing`, provides basic
  functionality for applications with helpers to allow
  applications to easily set up an
  `io_uring` instance and submit/complete
  I/O.
- Cgroup updates

  Full Cgroup v2 functionality is included in UEK R6.
  Functionality in UEK R5 included some features, such as
  the CPU controller, which allowed CPU resources to be
  set for a particular group of tasks. UEK R6 includes
  these features, along with the following notable
  enhancements:

  - A cgroup-aware OOM killer that can be used to kill a
    cgroup as a single unit to maintain the integrity of a
    workload. This functionality can be enabled by setting
    `memory.oom.group` in the cgroup v2
    memory controller. This setting determines that the
    cgroup is an indivisible workload, and tasks, along
    with their descendents, are killed together by the OOM
    killer or not at all.
  - A freezer controller is added to cgroupsv2, providing
    the ability to stop the workload in a cgroup and
    temporarily free up some resources.
  - This release introduces blk-iocost, an I/O cost-based
    model work-conserving proportional controller. It
    currently has a simple linear cost model built-in,
    where each I/O is classified as sequential or random
    and given a base cost, accordingly. Additional
    size-proportional cost is then added on top.
- NVDIMM

  Persistent memory can now be used as traditional RAM.
  Furthermore, fixes were implemented around the
  security-related commands within libnvdimm to enable the
  use of keys where payload data was filled with zero
  values, to allow secure operations to continue to take
  place where a zero-key is in use. A common
  implementation was put in place to ensure that all
  commands use the same zero-key semantic and that secure
  erasure of data on an NVDIMM can be performed where a
  zero-key is in use. This change is important because
  some NVDIMM platforms enable security with a default
  zero-key , rather than letting the operating system
  specify the initial key, which could prevent operations
  from working where security was enabled.

### Arm (aarch64) Platform

The following notable ARM features are implemented in UEK R6:

- Security improvements

  Various enhancements have been made to improve
  mitigations against attacks including the following:
  syscall wrappers, pointer authentication, KASLR (kernel
  virtual address randomization) support, and PSTATE.SSBS
  bit support (ARM v8.5 cores).
- Memory hotplug

  Core support for hot plugging memory.
- KVM improvements

  Improvements for KVM guests on Arm (aarch64) systems
  include pointer authentication (ARM v8.3) and Scalable
  Vector Extension (SVE) support.

### Cryptography

The following notable cryptographic features are implemented
in UEK R6:

- Simplified key description management

  Keys and keyrings are more namespace-aware .
- Zstandard Compression

  Zstandard compression (zstd) is added to crypto and
  scompress. Only the default level is enabled.

### DTrace v2.0

DTrace v2.0 is a re-implementation of DTrace that makes use of
existing Linux kernel tracing facilities, like eBPF, which did
not exist when DTrace was first ported to Linux. The new
implementation removes DTrace dependencies on specialized
kernel patches.

DTrace v2.0 is available with UEK R6 only. Previous versions
of UEK continue to include the original DTrace
implementation.

DTrace V2.0 on Oracle Linux 8 has been reimplemented as a user space
application. It no longer requires the libdtrace-ctf library
to run on Oracle Linux 8. The functionality of that library is
integrated into the Oracle Linux 8 GNU toolchain. Note that
libdtrace-ctf is still required on Oracle Linux 7.

Functionality is being delivered as it becomes available,
starting with a limited set of capabilities (primarily
framework functionality that does not offer many user visible
features) but ultimately reaching, and then exceeding, earlier
support.

- Notable changes and improvements

  The following notable changes and improvements are
  included:

  - The majority of underlying core DTrace functionality
    is re-implemented (D compiler, provider API, probe
    management) in user space. Much of this functionality
    previously resided in the kernel.
  - The D compiler is now targeted to generate eBPF code,
    and the majority of the D language is already
    supported by the compiler.
  - BPF verifier reporting output is enabled. When
    compiled D scripts are loaded into the kernel as BPF
    programs, the BPF verifier performs a static code
    analysis to ensure safety of the program. When this
    analysis fails, output is generated and DTrace reports
    this output to the user.
  - Function Boundary Tracing (FBT) probes are enabled
    with functions grouped by module (regardless of
    whether the module is compiled in or loadable) if the
    kernel provides this information in
    `/proc/kallsyms` (or
    `/proc/kallmodsyms`).
  - Syscall entry and return probes (systrace provider)
    are enabled, with support for typed probe arguments.
    Currently only available in `-lv`
    output.
  - Statically Defined Tracing (SDT) probes based on Linux
    tracepoints are enabled, with support for typed probe
    arguments. Currently only available in
    `-lv` output.
- Notable limitations

  Limitations of note include:

  - The `printf()` function is not yet
    implemented; use `trace()`.
  - The `trace()` action currently works
    only on numeric values, not strings.
  - Most actions, like `exit()`, are not
    yet implemented.
  - Of the three variable scopes, `Global
    ("x")` and `thread-local
    ("self->x")` are not yet implemented
  - Many providers (like dtrace or profile) -- including
    probes like `BEGIN`,
    `END`, and
    `profile-1n` -- are not yet
    functional
  - Probe descriptions (provider:module:function:name)
    that match multiple probes through the use of
    wild-cards are not yet supported. For example,
    `write:entry` works because it
    matches `syscall:vmlinux:write:entry`
    only, but `write:*` does not because
    it matches both
    `syscall:vmlinux:write:entry` and
    `syscall:vmlinux:write:return`.

#### Example Usage

The following examples illustrate current functionality in
DTrace v2.0 on UEK R6. Examples assume that commands are
run as root and `/usr/sbin` is in the PATH.

- Show DTrace version information:

  ```
  # dtrace -V
  DTrace 2.0.0 [Pre-Release with limited functionality]
  dtrace: Oracle D 2.0
  ```
- List probes:

  ```
  # dtrace -l
  DTrace 2.0.0 [Pre-Release with limited functionality]
  ID   PROVIDER    MODULE                     FUNCTION NAME
  1     dtrace                                        BEGIN
  2     dtrace                                        END
  3     dtrace                                        ERROR
  4        fbt   vmlinux     trace_initcall_finish_cb entry
  5        fbt   vmlinux     trace_initcall_finish_cb return
  6        fbt   vmlinux         initcall_blacklisted entry
  7        fbt   vmlinux         initcall_blacklisted return
  ```

  On this particular system, there were:

  - 3 dtrace probes
  - 87890 fbt probes (based on kprobes)
  - 1262 sdt probes (based on Linux tracepoints)
  - 666 syscall probes
- Example script that uses the `-S`
  option, to output the compiled D code as an eBPF
  program, and that uses the `-e` option,
  to exit after compilation:

  ```
  # dtrace -Sen 'write:entry { trace(1) }'
  DTrace 2.0.0 [Pre-Release with limited functionality]

  Disassembly of ::write:entry
            
  DIFO 0x46af600 returns D type (integer) (size 8) [record 16 bytes]
  INS OFF  OPCODE                  INSTRUCTION
  000 000: 62 a 0 fef8 ffffffff    stw  [%fp-264], -1     ! = EPID
  001 008: 62 a 0 fefc 00000000    stw  [%fp-260], 0
  002 016: 7a a 0 ff00 00000000    stdw [%fp-256], 0
  003 024: 7a a 0 ff08 00000000    stdw [%fp-248], 0
  004 032: 7a a 0 ff10 00000000    stdw [%f
  [...]
  ```
- Example script:

  ```
  # dtrace -n '
  write:entry,
  write:return
  {
  this->x = 3;                /* clause-local variables */
  this->y = 8;
  trace(this->x * this->y);
  trace(&`max_pfn);
  }'
  ```

  In the above:

  - Probe `write()` system call entry
    and exit (multiple probes at once);
  - Probe with recording the address of a kernel
    identifier (`max_pfn`) and other
    data items;
  - Probes are named (explicitly, no wild-cards) with
    the same action.
  - Clause-local variables are used.
  - The `trace()` action is used to
    report output.

### File Systems

The following are the most notable features that have been
implemented for file systems in UEK R6:

#### Btrfs

Btrfs continues to be supported in UEK. Several improvements
and patches have been applied in this update, including
support for swap files, ZStandard compression, and various
performance improvements. Btrfs support for root file
systems is introduced in Oracle Linux 8.3.

#### ext4

64-bit timestamps have been added to the superblock fields.

#### OCFS2

OCFS2 continues to be supported in UEK. Several improvements
and patches have been applied in this update, including
support for the 'nowait' AIO feature, support on Arm
platforms, and reading of the journal superblock for online
as well as offline operations.

#### XFS

A new, online health reporting infrastructure and user space
ioctl to get metadata health status after online fsck has
been added. Also added in this release is support to
fallocate swap files and swap files on realtime devices, as
well as partial reflink support. Various performance
improvements have also been made.

#### NFS

Performance improvements and enhancements have been made to
RPC and the NFS client and server components. Significant
improvements were made for NFS with RDMA. Enhancements
include the following: multiple TCP NFSv4.1+ client
connections, per server, for improved throughput from
hardware parallelism, enhanced soft-mount behaviour, and
improved diagnostics.

### Memory Management

The following notable memory management features are
implemented in UEK R6:

- TLB Flushing

  TLB flushing code is improved to avoid unnecessary
  flushes and to reduce TLB shootdowns.
- Huge Page clearing

  Memory management is enhanced to improve throughput by
  leveraging the clearing of huge pages more optimally.
- Page cache improvements

  Page cache efficiency is improved by using the more
  efficient Xarray data type.
- Improved fragmentation avoidance

  Fragmentation avoidance algorithms are improved and
  compaction and defragmentation times are faster.
- THP fault handling improvements

  Improvements have been implemented to the handling of
  Transparent Huge Page (THP) faults and also to provide
  better reporting on THP status.

### Networking

The following notable networking features are implemented in
Unbreakable Enterprise Kernel Release 6:

- TCP Early Departure Time

  The TCP stack now uses the Early Departure Time model
  for sending packets, instead of the As Fast As Possible
  model. This improvement brings several performance
  gains, as it resolves a limitation in the original
  TCP/IP framework and introduces the scheduled release of
  packets for overcoming hardware limitations and
  bottlenecks.
- Generic Receive Offload

  GRO is enabled for the User Datagram Protocol (UDP).
- TLS Receive

  The prior UEK release enabled the kernel to send TLS
  messages. This release enables the kernel to also
  receive TLS messages. The implementation of kernel
  handling of TLS connections offers significant
  performance gains over implementations that are limited
  to user space.
- Zero-copy TCP Receive

  The prior UEK release introduced a zero-copy TCP feature
  for sending packets to the network. This release enables
  receive functionality for zero-copy TCP.
- Packet Filtering

  nftables is now the default backend for firewall rules.
  BPF-based networking filtering (bpfilter) is also added
  in this release.
- Express data path (XDP) Added

  XDP is a flexible and minimal kernel-based packet
  transport for high-speed networking.

### RDMA

Remote Direct Memory Access (RDMA) is a feature that allows
direct memory access between two systems that are connected by
a network. RDMA facilitates high-throughput and low-latency
networking in clusters.

Unbreakable Enterprise Kernel Release 6 includes RDMA features that are provided in the
upstream kernel, with the addition of Ksplice and DTrace
functionality.

UEK R6 maintains feature parity with UEK R5 and includes the
following notable upstream updates:

- Dynamic Statistics Infrastructure

  A dynamic statistics infrastructure has been implemented
  to facilitate the monitoring of various objects by
  binding them to counters that are accessible through a
  netlink interface.
- Verbs Flow Counters

  Patches have been applied to provide an API that allows
  user-space applications to monitor real-time traffic
  activity and events of the verbs objects that it
  manages.
- RDMA ioctl() improvements

  Various updates have been applied to improve RDMA
  `ioctl()`. Significantly, new headers
  are used and naming has been made more consistent. The
  `uverbs_ioctl` header has been extended
  to include the `driver_id` and compact
  representation of `uverbs_attr_spec` is
  enabled.
- RDMA Resource tracking

  A general infrastructure for RDMA resource tracking has
  been implemented. This infrastructure is used to provide
  detailed Queue Pair (QP) information, as well as global
  resource utilization information.
- CQ moderation is exposed to user space

  Patches are applied to expose Completion Queue (CQ) to
  user-space applications to control the number of CQEs
  that are required to create an event. This change gives
  more controls to user applications to improve
  performance tuning.
- Improved Namespace functionality

  Various patches have been applied to improve namespace
  functionality. A patch that allows you to safely change
  the net namespace of an RDMA device was applied to add a
  command. Device sharing in multiple net namespaces is
  disabled and running `netlink` commands
  in non init\_net net namespaces is now possible.

### Security

The following notable security features are implemented in
Unbreakable Enterprise Kernel Release 6:

- Lockdown mode for x86\_64 systems

  Lockdown mode is improved. This release distinguishes
  between the integrity and confidentiality modes. When
  Secure Boot is enabled in UEK R6, lockdown integrity
  mode is enforced by default. Confidentiality mode can be
  enabled as an option on the kernel command line or by
  using securityfs, when UEFI Secure Boot is enabled.
  Lockdown modes can also be enabled when a kernel command
  line option is used to disable Secure Boot; however, no
  lockdown enforcing is performed by default when Secure
  Boot is disabled.

  The following restrictions are applied when integrity mode
  is enabled:

  - Enforce kernel module signatures
  - Restrict read write access to
    `/dev/{mem,kmem,port}`
  - Restrict efivar\_ssdt\_load
  - Disable kexec\_load system call
  - Disable hibernation
  - Prohibit PCI BAR access from user space
  - Prohibit X86 IO port access from user space
  - Restrict MSR access
  - Limit access to ACPI custom\_method
  - Ignore acpi\_rspd kernel param
  - Disable ACPI table override
  - Prohibit PCMCIA CIS storage
  - Prohibit TIOCSSEARIAL
  - Prohibit unsafe kernel module parameters
  - Prohibit the testmmiotrace module
  - Prohibit debugs access

  The following restrictions are applied when
  confidentiality mode is enabled:

  - Prohibit tracing and perf kprobes
  - Restrict use of bpf to read kernel memory
  - Prohibit unsafe use of perf
  - Prohibit tracefs
  - Prohibit access to `/proc/kcore`

  Note that kernel keyring management has also changed for
  UEK R6, which now uses code from the mainline upstream
  kernel to implement a platform keyring. UEFI Secure Boot
  DB and Machine Owner Keys (MOKs) are now stored in the
  platform keyring and are not treated equally to the kernel
  trust keyring. Although `kexec` trusts
  keys in the platform keyring, these cannot be used to add
  a new CA into the kernel for IMA (Integrity Measurement
  Architecture) and cannot be used to verify kernel modules.
- IBRS

  Indirect Branch Restricted Speculation (IBRS) continues
  to be supported for processors affected by Spectre V2
  Speculative Execution Side Channel Vulnerability and for
  which other software or hardware techniques may not be
  sufficient or are not available.
- Improved protection in world writable directories

  This kernel release discourages spoofing attacks by
  disallowing the opening of FIFOs or regular files that
  are not owned by the user in world-writable sticky
  directories, such as `/tmp`.
- Arm KASLR

  Kernel virtual address randomization is enabled by
  default for Arm platforms.
- aarch64 Pointer authentication

  This feature adds primitives that can be used to
  mitigate certain classes of memory stack corruption
  attacks on Arm platforms.

### Storage

The following notable storage features are implemented in
Unbreakable Enterprise Kernel Release 6:

- NVMe improvements

  NVMe over Fabrics TCP host and the target drivers have
  been added. Multipath support and passthrough command
  support have been added. NVMe namespace support is
  extended to include Namespace Write Protect and
  Asynchronous Namespace Access.

### Virtualization

The following notable virtualization features are implemented
in Unbreakable Enterprise Kernel Release 6:

- VirtIO improvements

  The VirtIO PMEM feature adds a VirtIO-based asynchronous
  flush mechanism and simulates persistent memory to a
  guest, allowing it to bypass a guest page cache. A
  VirtIO-IOMMU para-virtualized driver that allows IOMMU
  requests over the VirtIO transport without emulating
  page tables is also added in this release.
- Arm platform improvements

  Guests on Arm (aarch64) platform systems include pointer
  authentication (ARM v8.3) and Scalable Vector Extension
  (SVE) support.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-DriverUpdates.html -->

The Unbreakable Enterprise Kernel Release 6 supports a large number of hardware and devices. In
close cooperation with hardware and storage vendors, Oracle has
updated several device drivers from the versions in mainline
Linux 5.4.

A complete list of the driver modules included in UEK R6 along
with version information is provided in the appendix at
[Driver Modules in Unbreakable Enterprise Kernel Release 6 (x86\_64)](uek6.0-DriverModulesinUnbreakableEnterpriseKernelRelease6x8664.html#uek-driver-versions-x86_64).

### Notable Driver Features

The following new features are noted in the drivers shipped
with UEK R6:

- Broadcom BCM573xx network driver

  The `bnxt_en` driver version was
  updated to 1.10.1, with additional patches back-ported
  from the upstream 5.5 kernel release
  and vendor contributed patches that are specific to
  expanding and updating functionality for Broadcom Thor
  Ethernet controllers.

  An upstream change to this driver that was incorporated
  into a UEK R6 errata update in kernel version
  5.4.17-2011.6.2 results in a device name change for the
  second port of Broadcom network interfaces that use this
  driver. For example, a device that was previously
  identified as `eno3d1` is now identified
  as `eno3`. This fix was applied to
  improve device naming and also to address assumptions
  about port functionality on a device, such as in
  situations where the network device may belong to
  different functions. Consequently, this change can result
  in issues with network scripts when upgrading from a
  system that uses RHCK or UEK R5 to UEK R6. You may need
  to ensure that that network scripts are renamed and
  updated accordingly if you upgrade from a previous kernel
  version to a current version of UEK R6 or later.
- Broadcom Emulex LightPulse Fibre Channel SCSI driver

  The `lpfc` driver was updated to
  12.6.0.3. This update includes a large number of vendor
  contributed patches to address changes to the driver
  since the upstream 5.4 kernel was made available
  and important bug fix for the adapter firmware .
  Changes for this driver also resulted in updates to
  other kernel dependencies, such as code for NVMe over
  Fibre Channel.
- QLogic BCM5706/5708/5709/5716 driver

  The `bnx2` driver is updated; and,
  although the version number remains at 2.2.6, the driver
  includes vendor contributed patches and firmware
  updates.
- QLogic Fibre Channel HBA driver

  The `qla2xxx` driver is updated to
  version 10.01.00.22.81.1-k. This update back-ports many
  patches that have since gone into the upstream kernel
  and includes particular vendor contributed patches to
  improve performance and provide fixes for some bugs in
  the original driver.
- Microsemi Smart Family Controller driver

  The `smartpqi` driver is updated to
  version 1.2.10-025 and includes upstream patches that
  have been applied to the driver since the 5.4 kernel
  release under vendor guidance. These updates include
  several bug fixes and performance enhancements.
- LSI MPT Fusion SAS 3.0 Device driver

  The `mpt3sas` driver is updated to
  version 33.100.00.00 and includes vendor contributed
  patches.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-NewandUpdatedPackages.html -->

To support the newly added functionality that the UEK R6
provides, several kernel and user-space binary packages have
been added or updated from the packages that are included in the
base distribution. For more information about the ULN channels
and Oracle Linux yum server repositories in which these packages are available,
see [Installation and Availability](uek6-InstallationandAvailability.html#ol_instav).

Kernel space packages that are added and updated for UEK R6 are
labeled with the prefix `kernel-uek`. The
`linux-firmware` package is also updated with
the latest available firmwares.

The packages listed here are specific to user-space
functionality and are updated to take advantage of features that
are available in UEK R6. There is no dependency on these
packages to use UEK R6. If you use any of these packages and
also use UEK R6, you should update the package to the latest
version for full compatibility with all of the features that are
available in UEK R6.

| Packages | Oracle Linux 8 version number | Oracle Linux 7 version number |
| --- | --- | --- |
| `ndctl`,`ndctl-libs`, `ndctl-devel`, `daxctl`, `daxctl-libs`, `daxctl-devel` | 67 (x86\_64) | 67 (x86\_64) |
| `ipmctl`, `ipmctl-monitor`, `libipmctl`, `libipmctl-devel` | 01.00.00.3467 (x86\_64) | 01.00.00.3467 (x86\_64) |
| `libsafec`, `libsafec-check`, `libsafec-devel` | 3.3 (x86\_64) | 3.3 (x86\_64) |
| `btrfs-progs`, `btrfs-progs-devel` | 5.4.0 (x86\_64, aarch64) | 5.4.0 (x86\_64, aarch64) |
| `xfsprogs`, `xfsprogs-devel` | 5.4.0 (x86\_64, aarch64) | 5.4.0 (x86\_64, aarch64) |
| `ocfs2-tools` | 1.8.6 (x86\_64, aarch64) | 1.8.6 (x86\_64, aarch64) |
| `e2fs-progs`, `libss`, `libss-devel`, `libcom_err`, `libcom_err-devel` | 1.45.4 (x86\_64, aarch64) | 1.45.4 (x86\_64, aarch64) |
| `dtrace`, `dtrace-devel`, `dtrace-testsuite` | 2.0.0 (x86\_64, aarch64) | 2.0.0 (x86\_64, aarch64) |
| `libdtrace-ctf`,`libdtrace-ctf-devel` | N/A | 1.1.0 (x86\_64, aarch64) |
| `bcache-tools` | 1.0.8 (x86\_64, aarch64) | 1.0.8 (x86\_64, aarch64) |
| `cloud-init` | 18.5 (x86\_64, aarch64) | 18.5 (x86\_64, aarch64) |
| `crash`, `crash-devel` | 7.2.7 (x86\_64, aarch64) | 7.2.7 (x86\_64, aarch64) |
| `iproute`, `iproute-devel`, `iproute-doc`, `iproute-tc` | 5.4.0 (x86\_64, aarch64) | 5.4.0 (x86\_64, aarch64) |
| `kexec-tools` | 2.0.19 (x86\_64, aarch64) | 2.0.15 (x86\_64, aarch64) |
| `libzstd`, `libzstd-devel` | 1.3.8 (x86\_64, aarch64) | 1.3.4 (x86\_64, aarch64) |
| `linux-firmware` | 20200124-999.4 (x86\_64, aarch64) | 20200124-999.4 (x86\_64, aarch64) |
| `nvme-cli` | 1.9 (x86\_64, aarch64) | 1.9 (x86\_64, aarch64) |
| `nvmetcli` | 0.7 (x86\_64, aarch64) | 0.7 (x86\_64, aarch64) |
| `nbd` | 3.20 (x86\_64, aarch64) | 3.20 (x86\_64, aarch64) |
| `drbd-utils` | 9.0.0 (x86\_64, aarch64) | 9.0.0 (x86\_64, aarch64) |
| `libdnf`, `python3-libdnf`, `python3-hawkey` | 0.35 (x86\_64, aarch64) | N/A |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-Compatibility.html -->

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

### Notable changes in kernel headers

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-CertificationofUEKR6forOracleproducts.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-SecurityFixesforCVEs.html -->

This chapter lists security vulnerabilities and exposures (CVEs)
that are specifically addressed in this release. Note that CVEs are
continually handled in patch updates that are made available as
errata builds for the current release. For this reason, it is
absolutely critical that you keep your system up to date with the
latest package updates for this kernel release.

You can keep up to date with the latest CVE information at
<https://linux.oracle.com/cve>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-ListofCVEsfixedinthisrelease.html -->

The following list describes the CVEs that are fixed in this
release. The content provided here is automatically generated and
includes the CVE identifier and a summary of the issue. The
associated internal Oracle bug identifiers are also included to
reference work that was carried out to address each issue.

- CVE-2012-3430

  The rds\_recvmsg function in net/rds/recv.c in the Linux
  kernel before 3.0.44 does not initialize a certain structure
  member, which allows local users to obtain potentially
  sensitive information from kernel stack memory via a (1)
  recvfrom or (2) recvmsg system call on an RDS socket. (Bug:
  27364391
  )

  See
  <https://linux.oracle.com/cve/CVE-2012-3430.html>
  for more information.
- CVE-2013-1798

  The ioapic\_read\_indirect function in virt/kvm/ioapic.c in
  the Linux kernel through 3.8.4 does not properly handle a
  certain combination of invalid IOAPIC\_REG\_SELECT and
  IOAPIC\_REG\_WINDOW operations, which allows guest OS users to
  obtain sensitive information from host OS memory or cause a
  denial of service (host OS OOPS) via a crafted application.
  (Bug: 30851972
  )

  See
  <https://linux.oracle.com/cve/CVE-2013-1798.html>
  for more information.
- CVE-2015-6937

  The \_\_rds\_conn\_create function in net/rds/connection.c in
  the Linux kernel through 4.2.3 allows local users to cause a
  denial of service (NULL pointer dereference and system
  crash) or possibly have unspecified other impact by using a
  socket that was not properly bound. (Bug: 27364391
  )

  See
  <https://linux.oracle.com/cve/CVE-2015-6937.html>
  for more information.
- CVE-2016-5244

  The rds\_inc\_info\_copy function in net/rds/recv.c in the
  Linux kernel through 4.6.3 does not initialize a certain
  structure member, which allows remote attackers to obtain
  sensitive information from kernel stack memory by reading an
  RDS message. (Bug: 30816909
  )

  See
  <https://linux.oracle.com/cve/CVE-2016-5244.html>
  for more information.
- CVE-2018-12126

  Microarchitectural Store Buffer Data Sampling (MSBDS): Store
  buffers on some microprocessors utilizing speculative
  execution may allow an authenticated user to potentially
  enable information disclosure via a side channel with local
  access. A list of impacted products can be found here:
  https://www.intel.com/content/dam/www/public/us/en/documents/corporate-information/SA00233-microcode-update-guidance\_05132019.pdf
  (Bug: 30091537
  )

  See
  <https://linux.oracle.com/cve/CVE-2018-12126.html>
  for more information.
- CVE-2018-12127

  Microarchitectural Load Port Data Sampling (MLPDS): Load
  ports on some microprocessors utilizing speculative
  execution may allow an authenticated user to potentially
  enable information disclosure via a side channel with local
  access. A list of impacted products can be found here:
  https://www.intel.com/content/dam/www/public/us/en/documents/corporate-information/SA00233-microcode-update-guidance\_05132019.pdf
  (Bug: 30091537
  )

  See
  <https://linux.oracle.com/cve/CVE-2018-12127.html>
  for more information.
- CVE-2018-12130

  Microarchitectural Fill Buffer Data Sampling (MFBDS): Fill
  buffers on some microprocessors utilizing speculative
  execution may allow an authenticated user to potentially
  enable information disclosure via a side channel with local
  access. A list of impacted products can be found here:
  https://www.intel.com/content/dam/www/public/us/en/documents/corporate-information/SA00233-microcode-update-guidance\_05132019.pdf
  (Bug: 30091537
  )

  See
  <https://linux.oracle.com/cve/CVE-2018-12130.html>
  for more information.
- CVE-2018-12928

  In the Linux kernel 4.15.0, a NULL pointer dereference was
  discovered in hfs\_ext\_read\_extent in hfs.ko. This can occur
  during a mount of a crafted hfs filesystem. (Bug: 28312743
  )
- CVE-2018-5333

  In the Linux kernel through 4.14.13, the rds\_cmsg\_atomic
  function in net/rds/rdma.c mishandles cases where page
  pinning fails or an invalid address is supplied, leading to
  an rds\_atomic\_free\_op NULL pointer dereference. (Bug:
  28020561
  )

  See
  <https://linux.oracle.com/cve/CVE-2018-5333.html>
  for more information.
- CVE-2018-7492

  A NULL pointer dereference was found in the net/rds/rdma.c
  \_\_rds\_rdma\_map() function in the Linux kernel before 4.14.7
  allowing local attackers to cause a system panic and a
  denial-of-service, related to RDS\_GET\_MR and
  RDS\_GET\_MR\_FOR\_DEST. (Bug: 28565415
  )

  See
  <https://linux.oracle.com/cve/CVE-2018-7492.html>
  for more information.
- CVE-2019-11091

  Microarchitectural Data Sampling Uncacheable Memory (MDSUM):
  Uncacheable memory on some microprocessors utilizing
  speculative execution may allow an authenticated user to
  potentially enable information disclosure via a side channel
  with local access. A list of impacted products can be found
  here:
  https://www.intel.com/content/dam/www/public/us/en/documents/corporate-information/SA00233-microcode-update-guidance\_05132019.pdf
  (Bug: 30091537
  )

  See
  <https://linux.oracle.com/cve/CVE-2019-11091.html>
  for more information.
- CVE-2019-11815

  An issue was discovered in rds\_tcp\_kill\_sock in
  net/rds/tcp.c in the Linux kernel before 5.0.8. There is a
  race condition leading to a use-after-free, related to net
  namespace cleanup. (Bug: 29760503
  )

  See
  <https://linux.oracle.com/cve/CVE-2019-11815.html>
  for more information.
- CVE-2019-14615

  Insufficient control flow in certain data structures for
  some Intel(R) Processors with Intel(R) Processor Graphics
  may allow an unauthenticated user to potentially enable
  information disclosure via local access.

  See
  <https://linux.oracle.com/cve/CVE-2019-14615.html>
  for more information.
- CVE-2019-14895

  A heap-based buffer overflow was discovered in the Linux
  kernel, all versions 3.x.x and 4.x.x before 4.18.0, in
  Marvell WiFi chip driver. The flaw could occur when the
  station attempts a connection negotiation during the
  handling of the remote devices country settings. This could
  allow the remote device to cause a denial of service (system
  crash) or possibly execute arbitrary code. (Bug: 30588647
  )

  See
  <https://linux.oracle.com/cve/CVE-2019-14895.html>
  for more information.
- CVE-2019-14896

  A heap-based buffer overflow vulnerability was found in the
  Linux kernel, version kernel-2.6.32, in Marvell WiFi chip
  driver. A remote attacker could cause a denial of service
  (system crash) or, possibly execute arbitrary code, when the
  lbs\_ibss\_join\_existing function is called after a STA
  connects to an AP.
- CVE-2019-14897

  A stack-based buffer overflow was found in the Linux kernel,
  version kernel-2.6.32, in Marvell WiFi chip driver. An
  attacker is able to cause a denial of service (system crash)
  or, possibly execute arbitrary code, when a STA works in
  IBSS mode (allows connecting stations together without the
  use of an AP) and connects to another STA.
- CVE-2019-18660

  The Linux kernel before 5.4.1 on powerpc allows Information
  Exposure because the Spectre-RSB mitigation is not in place
  for all applicable CPUs, aka CID-39e72bf96f58. This is
  related to arch/powerpc/kernel/entry\_64.S and
  arch/powerpc/kernel/security.c.
- CVE-2019-18808

  A memory leak in the ccp\_run\_sha\_cmd() function in
  drivers/crypto/ccp/ccp-ops.c in the Linux kernel through
  5.3.9 allows attackers to cause a denial of service (memory
  consumption), aka CID-128c66429247. (Bug: 30521460
  )
- CVE-2019-19037

  ext4\_empty\_dir in fs/ext4/namei.c in the Linux kernel
  through 5.3.12 allows a NULL pointer dereference because
  ext4\_read\_dirblock(inode,0,DIRENT\_HTREE) can be zero.
- CVE-2019-19332

  An out-of-bounds memory write issue was found in the Linux
  Kernel, version 3.13 through 5.4, in the way the Linux
  kernel's KVM hypervisor handled the 'KVM\_GET\_EMULATED\_CPUID'
  ioctl(2) request to get CPUID features emulated by the KVM
  hypervisor. A user or process able to access the '/dev/kvm'
  device could use this flaw to crash the system, resulting in
  a denial of service.

  See
  <https://linux.oracle.com/cve/CVE-2019-19332.html>
  for more information.
- CVE-2019-3016

  In a Linux KVM guest that has PV TLB enabled, a process in
  the guest kernel may be able to read memory locations from
  another process in the same guest. This problem is limit to
  the host running linux kernel 4.10 with a guest running
  linux kernel 4.16 or later. The problem mainly affects AMD
  processors but Intel CPUs cannot be ruled out. (Bug:
  30758026
  )

  See
  <https://linux.oracle.com/cve/CVE-2019-3016.html>
  for more information.
- CVE-2020-2732

  \*\*\* UNKNOWN \*\*\* (Bug: 30847133
  )

  See
  <https://linux.oracle.com/cve/CVE-2020-2732.html>
  for more information.
- CVE-2020-8648

  There is a use-after-free vulnerability in the Linux kernel
  through 5.5.2 in the n\_tty\_receive\_buf\_common function in
  drivers/tty/n\_tty.c. (Bug: 30863513
  )


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-KnownIssues.html -->

This chapter describes the known issues for the Unbreakable Enterprise Kernel Release 6.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-UnusableorUnavailableArmFeatures.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/30953934.html -->

On systems that use a physical serial console to monitor system
output, such as on an ILOM console interface, it is possible
that high levels of output can introduce abnormal system
behavior such as kernel deadman timer events that indicate
processes are unable to obtain CPU scheduler time. This is
typically experienced if the serial console speed is set too low
and a loglevel of 6 or higher is configured for the system. To
reduce the likelihood of this issue occurring, either reduce the
log level or configure the console for the maximum possible baud
rate, 115200.

The current console speed for a running Oracle Linux 7 or Oracle Linux 8 system
can be set for a configured serial port by running:

```
sudo stty -F /dev/ttyS0 speed 115200
```

To change the serial console speed that is used when the system boots, you must edit the
GRUB configuration. Edit `/etc/sysconfig/grub` in a text editor and append
`console=ttyS0,115200` to the line
starting with `GRUB_CMDLINE_LINUX`, for example:

```
GRUB_CMDLINE_LINUX="crashkernel=auto resume=/dev/mapper/linux1-swap rd.lvm.lv=linux1/root \
  rd.lvm.lv=linux1/swap rhgb quiet console=ttyS0,115200"
```

Note that in the above examples, the serial console is assumed
to be ttyS0, you may need to change
this if your have used an alternate serial port.

To update your grub configuration with the changes so that they
are used on the next boot if you are using legacy BIOS, run:

```
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

Alternately, if you are booting using UEFI, run:

```
sudo grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg
```

If you are using Oracle Server hardware, or a system that
provides an ILOM interface to the serial console, make sure that
you update the serial console configuration on the ILOM to match
the speed that you have set within the host operating system.
You can set the serial port on the ILOM CLI by running:

```
set /SP/serial/host pendingspeed=115200 commitpending=true
```

To check the current console port speed on the ILOM, using the
CLI, run:

```
show /SP/serial/host
```

For more information about ILOM configuration, see
<https://docs.oracle.com/cd/E19203-01/820-1188-12/core_ilom_managing.html>.

(Bug ID 30953934, 30487830, 30439170)


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/30687021.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/30797389.html -->

When SELinux is configured to use the Multilevel Security (MLS)
policy and it is in the enforcing mode, several issues can prevent
normal functioning of the operating system, including permissions
errors when attempting to mount file systems and the likelihood of
a Systemd freeze when booting the operating system.

SELinux in the enforcing mode with the MLS policy is not
supported. Note that you can continue to use SELinux in the
enforcing mode by using the targeted policy.

(Bug ID 30797389, 30609238)


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/30339848.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/30993407.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-IOMMUkerneloptionenabledbydefault.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/30512596.html -->

The PCIE hot-plug driver emits an error message when a virtual
machine running on an Arm platform is rebooted. The error emitted
is similar to the following message:

```
[    3.574244] pcieport 0000:00:02.1: pciehp: Failed to check link status
```

The issue is not replicated on bare metal systems.

(Bug ID 30512596)


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/30456791.html -->

Attempts to unload the `dsa-loop` driver with
`modprobe -r` may cause a crash on some Arm
platforms.

Do not unload the `dsa-loop` driver.

(Bug ID 30456791)


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/32834324.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/30976607.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/31021418.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/31025483.html -->

The version of Podman that is available on Oracle Linux 8 has an issue
unmounting the overlay file system for a container when
performing an `rm` operation while using the
`--uidmap` option. The issue typically
manifests with output similar to the following:

```
ERRO[0000] error unmounting
/var/lib/containers/storage/overlay/9bf314b8c2411fd7b7e2f249671bead918a7aaffec
a8299a602b525c061c1cd3/merged: invalid argument
```

The following error appears in the dmesg log:

```
[  848.192546] overlayfs: failed to verify upper
(9bf314b8c2411fd7b7e2f249671bead918a7aaffeca8299a602b525c061c1cd3/diff,
ino=101428727, err=-116)
[  848.198470] overlayfs: failed to verify index dir 'upper' xattr
[  848.200809] overlayfs: try deleting index dir or mounting with '-o
index=off' to disable inodes index.
```

The default handling for the overlay file system on UEK R6 is
to mount with the `index` option enabled. This
feature uses use the index directory to map lower inodes to
upper inodes by default, however the impact of turning it off is
negligible. If you experience this issue, it can be avoided by
loading the `overlay` module with the
`index=off` option set. For example, run:

```
sudo rmmod overlay 
sudo modprobe overlay index=off
```

To make these settings persistent, set this option in
`/etc/modprobe.d/`. For example, run the
following:

```
echo 'options overlay index=off' | sudo tee /etc/modprobe.d/overlay.conf
```

(Bug ID 31025483)


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/30979601.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/31085618.html -->

When booting an Oracle Linux 7 bare-metal system with UEK R6, the
following may be reported in the dmesg log:

```
This kernel doesn't handle early microcode load properly (it tries to load
microcode even in virtualised environment, which may lead to a panic on some
hypervisors), thus the microcode files have not been added to the initramfs
image.
```

UEK R6 does, in fact, handle late microcode loading properly. The
messages are due to a downrev `microcode-ctl`
user space package that does not recognize the UEK R6 kernel
version.

This issue is fixed in the
`microcode_ctl-2.1-61.10.0.1` package or later
versions.

(Bug ID 31085618)


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-InstallationandAvailability.html -->

You can install Unbreakable Enterprise Kernel Release 6 on Oracle Linux 7.7, or later, and on Oracle Linux 8.1, or
later, by running either the Red Hat Compatible Kernel (RHCK) or
a previous release of the Unbreakable Enterprise Kernel. If you are still running an
older version of Oracle Linux, you must first update your system to the
latest available update release.

Unbreakable Enterprise Kernel Release 6 is supported on x86-64 platforms but not on x86. The
Unbreakable Enterprise Kernel Release 6 is also supported on 64-bit Arm (aarch64) platforms.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-InstallationOverview.html -->

If you have a subscription to Oracle Unbreakable Linux support,
you can obtain the packages for Unbreakable Enterprise Kernel Release 6 by registering your
system with the Unbreakable Linux Network (ULN) and subscribing
it to additional channels. See [Subscribing to ULN Channels](uek6-SubscribingtoULNChannels.html#ol_sub_uln).

If your system is not registered with ULN, you can obtain most
of the packages from Oracle Linux yum server. See [Enabling Access to Oracle Linux Yum Server Repositories](uek6-EnablingAccesstoOracleLinuxYumServerRepositories.html#ol_sub_pubyum).

Having subscribed your system to the appropriate channels on ULN
or Oracle Linux yum server, upgrade your system. See
[Upgrading Your System](uek6-UpgradingYourSystem.html#ol_upgradea_sys).


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-SubscribingtoULNChannels.html -->

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

### Oracle Linux 7

The kernel image and user space packages are available on the
`ol7_x86_64_UEKR6` ULN channel for Oracle Linux 7 on
x86\_64 platforms. For aarch64 platforms, these packages are
available on the `ol7_aarch64_UEKR6` ULN
channel.

### Oracle Linux 8

Kernel image and user space packages are available on the
following ULN channels for Oracle Linux 8 on x86\_64 platforms:

- `ol8_x86_64_UEKR6`
- `ol8_x86_64_baseos_latest`

Oracle Linux 8 kernel image and user space packages for Oracle Linux 8 (aarch64) are made
available by default on the
`ol8_aarch64_baseos_latest` ULN channel.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-EnablingAccesstoOracleLinuxYumServerRepositories.html -->

Packages for UEK R6 and associated user space applications are
available on the Oracle Linux yum server at
<https://yum.oracle.com/>.

### Oracle Linux 7

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

### Oracle Linux 8

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-UpgradingYourSystem.html -->

To upgrade your system to Unbreakable Enterprise Kernel Release 6:

1. Enable access to the appropriate ULN channels or yum
   repositories as described in [Subscribing to ULN Channels](uek6-SubscribingtoULNChannels.html#ol_sub_uln)
   and [Enabling Access to Oracle Linux Yum Server Repositories](uek6-EnablingAccesstoOracleLinuxYumServerRepositories.html#ol_sub_pubyum). It is good practice to
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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-InstallingOracleSupportedRDMAPackagesforx8664platforms.html -->

The following procedure describes how to install the RDMA release packages. The instructions
describe how to remove previous existing `oracle-ofed-release` packages and
other previously installed RDMA packages that could cause conflicts during the installation of
the UEK R6 RDMA packages. Note that the `yum` commands used in this
procedure are interchangeable with the `dnf` command available in Oracle
Linux 8.

1. In addition to the ULN channels and yum repositories
   described in [Subscribing to ULN Channels](uek6-SubscribingtoULNChannels.html#ol_sub_uln) and
   [Enabling Access to Oracle Linux Yum Server Repositories](uek6-EnablingAccesstoOracleLinuxYumServerRepositories.html#ol_sub_pubyum), subscribe the system to the
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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6-UpgradingOracleSupportedRDMAPackagesforx8664platforms.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-DriverModulesinUnbreakableEnterpriseKernelRelease6x8664.html -->

This appendix presents all of the driver modules and their version
information as shipped in the current version of UEK R6 (x86\_64).
This appendix is generated automatically. Note that driver versions
and available drivers may change in subsequent errata releases, but
the driver versions will always be the same or later than presented
here.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-acpiDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-ataDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-atmDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `atmtcp` |  |  |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-auxdisplayDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `cfag12864b` |  | cfag12864b LCD driver |
| `cfag12864bfb` |  | cfag12864b LCD framebuffer driver |
| `ks0108` |  | ks0108 LCD Controller driver |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-bcmaDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `bcma` |  | Broadcom's specific AMBA driver |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-blockDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-bluetoothDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-cdromDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `cdrom` |  |  |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-charDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-cpufreqDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `acpi-cpufreq` |  | ACPI Processor P-States Driver |
| `amd_freq_sensitivity` |  | AMD frequency sensitivity feedback powersave bias for the ondemand governor. |
| `p4-clockmod` |  | cpufreq driver for Pentium(TM) 4/Xeon(TM) |
| `pcc-cpufreq` | 1.10.00 | Processor Clocking Control interface driver |
| `powernow-k8` |  | AMD Athlon 64 and Opteron processor frequency driver. |
| `speedstep-lib` |  | Library for Intel SpeedStep 1 or 2 cpufreq drivers. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-cryptoDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-daxDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `device_dax` |  |  |
| `kmem` |  |  |
| `dax_pmem` |  |  |
| `dax_pmem_compat` |  |  |
| `dax_pmem_core` |  |  |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-dcaDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `dca` | 1.12.1 |  |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-devfreqDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `governor_simpleondemand` |  |  |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-dmaDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `dw_dmac` |  | Synopsys DesignWare DMA Controller platform driver |
| `idma64` |  | iDMA64 core driver |
| `ioatdma` | 5.00 |  |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-edacDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `amd64_edac_mod` |  | MC support for AMD64 memory controllers - 3.5.0 |
| `e752x_edac` |  | MC support for Intel e752x/3100 memory controllers |
| `edac_mce_amd` |  | AMD MCE decoder |
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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-firewireDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `firewire-core` |  | Core IEEE1394 transaction logic |
| `firewire-net` |  | IP over IEEE1394 as per RFC 2734/3146 |
| `firewire-ohci` |  | Driver for PCI OHCI IEEE1394 controllers |
| `firewire-sbp2` |  | SCSI over IEEE1394 |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-firmwareDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `edd` | 0.16 | sysfs interface to BIOS EDD information |
| `iscsi_ibft` | 0.5.0 | sysfs interface to BIOS iBFT information |
| `qemu_fw_cfg` |  | QEMU fw\_cfg sysfs support |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-gpioDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `gpio-amdpt` |  | AMD Promontory GPIO Driver |
| `gpio-generic` |  | Driver for basic memory-mapped GPIO controllers |
| `gpio-ich` |  | GPIO interface for Intel ICH series |
| `gpio-viperboard` |  | GPIO driver for Nano River Techs Viperboard |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-gpuDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-hidDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-hvDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `hv_balloon` |  | Hyper-V Balloon |
| `hv_utils` |  | Hyper-V Utilities |
| `hv_vmbus` |  | Microsoft Hyper-V VMBus Driver |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-hwmonDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-i2cDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-iioDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `industrialio` |  | Industrial I/O core |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-infinibandDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-inputDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-isdnDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-ledsDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-mdDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-mediaDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-memstickDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `memstick` |  | Sony MemoryStick core driver |
| `mspro_block` |  | Sony MemoryStickPro block device driver |
| `jmb38x_ms` |  | JMicron jmb38x MemoryStick driver |
| `r592` |  | Ricoh R5C592 Memstick/Memstick PRO card reader driver |
| `rtsx_pci_ms` |  | Realtek PCI-E Memstick Card Host Driver |
| `rtsx_usb_ms` |  | Realtek USB Memstick Card Host Driver |
| `tifm_ms` |  | TI FlashMedia MemoryStick driver |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-messageDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `mptbase` | 3.04.20 | Fusion MPT base driver |
| `mptctl` | 3.04.20 | Fusion MPT misc device (ioctl) driver |
| `mptfc` | 3.04.20 | Fusion MPT FC Host driver |
| `mptlan` | 3.04.20 | Fusion MPT LAN driver |
| `mptsas` | 3.04.20 | Fusion MPT SAS Host driver |
| `mptscsih` | 3.04.20 | Fusion MPT SCSI Host driver |
| `mptspi` | 3.04.20 | Fusion MPT SPI Host driver |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-mfdDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-miscDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-mmcDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-mtdDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-netDriversinUEKR6x8664.html -->

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
| `atlantic` | 5.4.17-2011.0.7.el7uek.x86\_64-kern | aQuantia Corporation(R) Network Driver |
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
| `ice` | 0.8.1-k | Intel(R) Ethernet Connection E800 Series Linux Driver |
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
| `nfp` | 5.4.17-2011.0.7.el7uek.x86\_64 | The Netronome Flow Processor (NFP) driver. |
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
| `r8152` | v1.10.10 | Realtek RTL8152/RTL8153 Based USB Ethernet Adapters |
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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-ntbDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `ntb` | 1.0 | PCIe NTB Driver Framework |
| `ntb_transport` | 4 | Software Queue-Pair Transport over NTB |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-nvdimmDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `libnvdimm` |  |  |
| `nd_blk` |  |  |
| `nd_btt` |  |  |
| `nd_e820` |  |  |
| `nd_pmem` |  |  |
| `nd_virtio` |  |  |
| `virtio_pmem` |  | Virtio pmem driver |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-nvmeDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-parportDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `parport` |  |  |
| `parport_pc` |  | PC-style parallel port driver |
| `parport_serial` |  | Driver for common parallel+serial multi-I/O PCI cards |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-pciDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `pci-hyperv-intf` |  | Hyper-V PCI Interface |
| `pci-hyperv` |  | Hyper-V PCI |
| `acpiphp_ibm` | 1.0.1 | ACPI Hot Plug PCI Controller Driver IBM extension |
| `pci-pf-stub` |  |  |
| `aer_inject` |  | PCIe AER software error injector |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-pcmciaDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `yenta_socket` |  |  |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-pinctrlDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-platformDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-powerDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-powercapDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `intel_rapl_common` |  | Intel Runtime Average Power Limit (RAPL) common code |
| `intel_rapl_msr` |  | Driver for Intel RAPL (Running Average Power Limit) control via MSR interface |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-ppsDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `pps-gpio` | 1.2.0 | Use GPIO pin as PPS source |
| `pps-ldisc` |  | PPS TTY device driver |
| `pps_parport` |  | parallel port PPS client |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-ptpDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `ptp_kvm` |  | PTP clock using KVMCLOCK |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-regulatorDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `fixed` |  | Fixed voltage regulator |
| `lp3971` |  | LP3971 PMIC driver |
| `max1586` |  | MAXIM 1586 voltage regulator driver |
| `tps65023-regulator` |  | TPS65023 voltage regulator driver |
| `tps6507x-regulator` |  | TPS6507x voltage regulator driver |
| `userspace-consumer` |  | Userspace consumer for voltage and current regulators |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-rtcDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-scsiDriversinUEKR6x8664.html -->

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
| `lpfc` | 0:12.6.0.3 | Emulex LightPulse Fibre Channel SCSI driver 12.6.0.3 |
| `megaraid_mbox` | 2.20.5.1 | LSI Logic MegaRAID Mailbox Driver |
| `megaraid_mm` | 2.20.2.7 | LSI Logic Management Module |
| `megaraid_sas` | 07.710.50.00-rc1 | Broadcom MegaRAID SAS Driver |
| `mpt3sas` | 33.100.00.00 | LSI MPT Fusion SAS 3.0 Device Driver |
| `mvsas` | 0.8.16 | Marvell 88SE6440 SAS/SATA controller driver |
| `mvumi` |  | Marvell UMI Driver |
| `pm80xx` | 0.1.39 | PMC-Sierra PM8001/8006/8081/8088/8089/8074/8076/8077/8070/8072 SAS/SATA controller driver |
| `pmcraid` | 1.0.3 | PMC Sierra MaxRAID Controller Driver |
| `ppa` |  |  |
| `qedf` | 8.42.3.0 | QLogic FastLinQ 4xxxx FCoE Module |
| `qedi` | 8.37.0.20 | QLogic FastLinQ 4xxxx iSCSI Module |
| `qla2xxx` | 10.01.00.22.81.1-k | QLogic Fibre Channel HBA Driver |
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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-ssbDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `ssb` |  | Sonics Silicon Backplane driver |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-stagingDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-targetDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-thermalDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-ttyDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-uioDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `uio` |  |  |
| `uio_aec` |  |  |
| `uio_cif` |  |  |
| `uio_hv_generic` | 0.02.1 | Generic UIO driver for VMBus devices |
| `uio_pci_generic` | 0.01.0 | Generic UIO driver for PCI 2.3 devices |
| `uio_pdrv_genirq` |  | Userspace I/O platform driver with generic IRQ handling |
| `uio_sercos3` |  | UIO driver for the Automata Sercos III PCI card |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-usbDriversinUEKR6x8664.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-vfioDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `mdev` | 0.1 | Mediated device Core Driver |
| `vfio_mdev` | 0.1 | VFIO based driver for Mediated device |
| `vfio-pci` | 0.2 | VFIO PCI - User Level meta-driver |
| `vfio_virqfd` | 0.1 | IRQFD support for VFIO bus drivers |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.0/uek6.0-vhostDriversinUEKR6x8664.html -->

| Driver | Version | Description |
| --- | --- | --- |
| `vhost` | 0.0.1 | Host kernel accelerator for virtio |
| `vhost_net` | 0.0.1 | Host kernel accelerator for virtio net |
| `vhost_scsi` |  | VHOST\_SCSI series fabric driver |
| `vhost_vsock` |  | vhost transport for vsock |