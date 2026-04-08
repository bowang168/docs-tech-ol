---
title: "Unbreakable Enterprise Kernel 8: Release Notes (6.12.0-0.20)"
source_url: "https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "uek"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

## Unbreakable Enterprise Kernel

Unbreakable Enterprise Kernel 8 - Release Notes (6.12.0-0.20.20)

F91418-07

June 2025

---

[Title and Copyright Information](#copyright-information)

Unbreakable Enterprise Kernel Unbreakable Enterprise Kernel 8 - Release Notes (6.12.0-0.20.20)

F91418-07

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2025, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-Preface.html -->

## Preface

[Unbreakable Enterprise Kernel 8: Release
Notes (6.12.0-0.20.20)](https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/) provides a summary of the new features,
significant changes, and any known issues in Unbreakable Enterprise Kernel 8 (UEK 8).


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/ref-conventions.html -->

## Conventions

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| boldface | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| italic | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/ref-doc-accessibility.html -->

## Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility
Program website at <https://www.oracle.com/corporate/accessibility/>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/ref-accessibility.html -->

## Access to Oracle Support for Accessibility

Oracle customers that have purchased support have access to electronic support through My
Oracle Support. For information, visit <https://www.oracle.com/corporate/accessibility/learning-support.html#support-tab>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/ref-diversity.html -->

## Diversity and Inclusion

Oracle is fully committed to diversity and inclusion. Oracle respects and values having a
diverse workforce that increases thought leadership and innovation. As part of our
initiative to build a more inclusive culture that positively impacts our employees,
customers, and partners, we are working to remove insensitive terms from our products and
documentation. We are also mindful of the necessity to maintain compatibility with our
customers' existing technologies and the need to ensure continuity of service as Oracle's
offerings and industry standards evolve. Because of these technical constraints, our effort
to remove insensitive terms is ongoing and will take time and external cooperation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8-AboutUEK8.html -->

## 1 About Unbreakable Enterprise Kernel 8

This chapter provides an overview of Unbreakable Enterprise Kernel 8 (UEK 8) and contains important information about this major
release.

Note:

Upgrading from an Unbreakable Enterprise Kernel Developer Preview release to its later
official version isn't supported. If you're running the Developer Preview version, you must
reinstall the official UEK release upon its general availability.

UEK 8 is initially released with the 6.12.0-0.20.20 version of the kernel. The kernel's source code is
available through a public git source code repository at <https://github.com/oracle/linux-uek>.

The following is a general description of the scope of support for UEK 8:

- The kernel is developed, built, and tested on the 64-bit Arm (aarch64), Intel® 64-bit
  x86\_64, and AMD 64-bit x86\_64 architectures and is based on the mainline Linux kernel
  version 6.12 (LTS).
- UEK 8 is made available for installation on the latest
  Oracle Linux 9 update releases and for Oracle Linux 10.
- In UEK 8, more features are enabled to provide support
  for key functional requirements and patches are applied to improve performance and
  optimize the kernel for use on Oracle operating environments. Note that Oracle actively
  monitors upstream check-ins and applies critical bug and security fixes to UEK 8.
- Although UEK 8 uses the same versioning model as the
  mainline Linux kernel version, it's possible that some applications might not understand
  the 6.12.0 versioning scheme. Note, however, that regular Linux applications are usually
  neither aware of nor affected by Linux kernel version numbers.
- A version of UEK 8 that enables 64k pages is available
  for 64-bit Arm (aarch64) platforms for Oracle Linux 9 and later. The
  `kernel-uek64k` package is available on Oracle Cloud Infrastructure Arm
  compute shapes only. Use of this kernel outside of Oracle Cloud Infrastructure is only
  available as a technical preview.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8-CertificationofUEK8forOracleProducts.html -->

## Certification of UEK 8 for Oracle Products

The following important information applies to the certification of Oracle products with UEK
8.

Note that certification of different Oracle products with UEK 8 might not be immediately
available at the time of the UEK 8 release. Ensure that the product you're using is certified
for use with UEK 8 before upgrading or installing the kernel. You can check for certification
information at <https://support.oracle.com/epmos/faces/CertifyHome>.

Oracle Automatic Storage Management Cluster File System (Oracle
ACFS) certification for different kernel versions is described in
Document ID 1369107.1, which is available at
<https://support.oracle.com/epmos/faces/DocumentDisplay?id=1369107.1>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8-Compatibility.html -->

## Compatibility

Oracle Linux maintains full user space compatibility with Red Hat Enterprise Linux (RHEL),
which is independent of the kernel version that's running underneath the OS. Note that
existing applications in user space continue to run unmodified with UEK 8; no
recertifications are required for RHEL certified applications.

To minimize any impact on interoperability during releases, the Oracle Linux team works with
third-party vendors that have hardware and software with dependencies on kernel modules. The
kernel ABI for UEK 8 remains unchanged in all subsequent updates to the initial release.
Customers migrating from UEK R7 must be aware that kernel ABIs have changed in UEK 8. If an
application is using kernel modules, users must verify the support status with the application
vendor.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8-NewFeaturesandChanges.html -->

## 2 New Features and Changes

This chapter describes new features, enhancements, and other notable changes that are
introduced in UEK 8.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-SummaryofNotableChangesinUEK8.html -->

## Summary of Notable Changes in UEK 8

The following is a summary of the features, changes, and improvements that are introduced in
UEK 8, relative to UEK R7:

- Linux 6.12 stable kernel base

  The 6.12 mainline kernel release that's used as the base kernel for UEK 8 includes many
  upstream kernel features and improvements over previous UEK releases and over RHCK on
  Oracle Linux 9.
- Kernel module packaging is updated

  Kernel modules are distributed in more atomic packages to reduce the attack surface on
  the kernel, to improve kernel module maintenance, and to also improve visibility of module
  deprecation. See [Changes to UEK Content Distribution and Packaging](uek8.0-ChangestoUEKContentDistributionandPackaging.html#uek8-features-content) for a complete view of kernel packaging in UEK 8.
- 64k Base Page Size on Arm

  In this release, a version of the kernel with a 64k base page size is available for
  Ampere Arm-based Compute shapes in Oracle Cloud Infrastructure only. The 64k base page
  size improves how Arm platforms process workloads with large, contiguous memory datasets.
  See [(aarch64) 64k Base Page Size on Arm](uek8.0-DefaultPageSizeonArmPlatform.html#feature-ol9-64k-page)
  for more information.
- Other platform updates

  Several generic platform updates are included. See [Generic Platform Updates](uek8.0-GenericPlatformUpdates.html#generic-platform). Some other
  Intel-specific platform updates are available, including security features such as Intel
  Software Guard Extensions and new hardware support for Intel Quick Assist Technology
  (QAT). See [Intel Platform Updates](uek8.0-IntelPlatformUpdates.html#topic_cvc_52l_b2c).
- Completely Fair Scheduler (CFS) replaced by Earliest Eligible Virtual Deadline First
  (EEVDF)

  CFS is replaced by the EEVDF scheduler to improve scheduling behavior and to reduce
  configuration complexity. See [EEVDF Scheduler Replaces CFS](uek8.0-core-feature-eevdf_scheduler_replaces_cfs.html#concept_jkb_fgt_21c).
- Improved Memory Management

  Many memory management improvements appear in UEK 8, including several memory mapping
  optimizations, improvements to performance through the introductions of folio structures,
  and some enhancements to Huge Page handling. See [Memory Management](uek8.0-MM.html#uek8.0-MM).
- File systems updates

  Support for the Btrfs and OCFS2 file systems is enabled in UEK 8. Significant
  enhancements are available for the Btrfs, XFS, and NFS file systems in this release. For
  more information about new file systems features that are introduced in UEK 8, see [File Systems](uek8-FileSystems.html#uek8-features-fs)
- ASMLib v3 and io\_uring

  Several io\_uring enhancements are included in this release of UEK, which also supports
  ASMLib v3. ASMLib v3 uses io\_uring for the Automatic Storage Management feature of the
  Oracle Database. See [io\_uring Enhancements](uek8.0-core-feature-io_uring_enhancements.html#io_uring_enhancements) and [ASMLib v3](uek8.0-ASMLib.html#uek8-asmlib).
- Networking updates

  Several general networking enhancements are included in UEK 8. See [General Networking Enhancements](uek8.0-Networking.html#general-networking).
- Security related updates

  Some other security related updates are included in this release of UEK, including some
  updates to the Random Number Generator help improve performance and security. See [Random Number Generator Enhancements](uek8.0-RNG.html#rng-enhancements). The kernel TLS offload facility is
  enabled in UEK 8. See [KTLS](uek8.0-KTLS.html#uek8.0-KTLS).
- Berkeley Packet Filter

  Several enhancements are available in the Berkeley Packet Filter (BPF) used for tracing,
  including a dedicated memory allocator, a new user ring buffer, and the use of resilient
  BPF Type Format (BTF) modules to use BTF for out-of-tree modules. See [Berkeley Packet Filter (BPF) Enhancements](uek8.0-BPF.html#uek8.0-BPF).
- DTrace v2.0

  Dtrace v2.0 continues to be available in UEK 8 and leverages kernel tracing facilities
  such as eBPF. Detailed information about DTrace releases and other notable changes are
  available at [Oracle Linux: DTrace Release Notes](https://docs.oracle.com/en/operating-systems/oracle-linux/dtrace-relnotes/).

  .


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-ChangestoUEKContentDistributionandPackaging.html -->

## Changes to UEK Content Distribution and Packaging

The following table provides details about how UEK 8 content is distributed and packaged and
includes information about package dependencies, and any other notable requirements.

Note:

Kernel packaging is updated in UEK 8 and differs from previous UEK releases. Most notably,
kernel modules are now shipped in a collection of separate packages. Separating modules out
of the core kernel packages helps to reduce overhead, provides a mechanism to minimize
attack surface, and improves kernel module maintenance.

Configuration files to identify modules that are denied from loading are renamed from
'blacklist' files to 'denylist' as part of Oracle's initiative to use more inclusive
language in its products.

Also, some kernel utility tools that were bundled in the `kernel-uek-core`
package in previous releases are moved into a separate package,
`kernel-uek-tools`.

You can list the modules available in each package by running:

```
rpm -q -l kernel-uek-modules-<ext>
```

To find which package a module that's available on the system belongs to, you can run:

```
rpm -q -f /lib/modules/$(uname -r)/<path to module>
```

If you run the modprobe command for a module and the package that the module belongs to
isn't installed, the output notifies you and provides the package name that you must
install. Note that you might need to update the `kmod` package to the latest
version for this functionality to work.

```
sudo modprobe wl1251_sdio
```

```
modprobe: FATAL: Module wl1251_sdio not found in directory /lib/modules/6.12.0-0.20.20.el9uek.x86_64, 
ensure the following package is installed: kernel-uek-modules-wireless-6.12.0-0.20.20.el9uek.x86_64
```

A package mapping file is included at `/lib/modules/$(uname
-r)/modules.packages` and is shipped in the `kernel-uek-core`
package for UEK 8 and later. You can also use this file to identify the module package that
contains a particular driver.

| Package | Description |
| --- | --- |
| `kernel-uek` | This is a meta package that doesn't contain any files.  In Oracle Linux 9, the package has the following dependencies:   - `kernel-uek-core` - `kernel-uek-modules-core` - `kernel-uek-modules` - `kernel-uek-modules-desktop` - `kernel-uek-modules-extra-netfilter` - `kernel-uek-modules-usb` - `kernel-uek-modules-wireless`   Installing this package is equal to installing the full UEK kernel. Installing this package maintains compatibility with previous releases. |
| `kernel-uek-core` | This package contains the UEK kernel binary and supporting files, which are copied to `/boot`. The package is installed along with the `kernel-uek-modules-core` package and the `kernel-uek-modules` package. Note that this package requires that the `linux-firmware-core` package also be installed. |
| `kernel-uek-modules-core` | This package contains a minimal number of core kernel modules and supporting files used for Oracle engineered systems. The package is a dependency of the `kernel-uek-core` and is installed by default. |
| `kernel-uek-modules` | This package contains various modules that are commonly used in most server configurations. Note that this package requires that the `linux-firmware` package also be installed. |
| `kernel-uek-modules-desktop` | This package contains modules for desktop-type hardware.  This package can be removed to harden the system on many server platforms if none of the modules are used. |
| `kernel-uek-modules-usb` | This package contains USB drivers.  This package can be removed to harden the system on many server platforms if none of the modules are used. |
| `kernel-uek-modules-wireless` | This package contains wireless drivers.  This package is can be removed to harden the system on many server platforms if none of the modules are used. |
| `kernel-uek-modules-extra-netfilter` | This package contains uncommon netfilter modules.  This package can be removed to harden the system on many server platforms if none of the modules are used. |
| `kernel-uek-modules-deprecated` | This package contains modules that we plan to remove in future releases.  This package is optional and you can install the package manually from the yum repository or ULN channel.  Modules included in this package are deprecated and might be removed in a future release. |
| `kernel-uek-modules-extra` | This package contains extra modules for server configurations, but which aren't commonly used.  This package is optional and you can install the package manually from the yum repository or ULN channel. |
| `kernel-uek-tools` | This package contains tools that are required to satisfy other build and runtime dependencies in the `tools/perf` code base, and which can be used after boot to interact with the kernel. For example, the `perf` tool used for system performance analysis is included in this package. |
| `linux-firmware-core` | This package contains core firmware components and is a dependency for the `kernel-uek-core` package. |
| `linux-firmware` | This package contains firmware components that aren't provided in the `linux-firmware-core` package and is a dependency for the `kernel-uek-modules` package.  Note that this package requires that the `linux-firmware-core` package also be installed. |

For security hardening, we recommend that you remove any of the
`kernel-uek-modules-*` packages that aren't required by the system. To
remove packages:

1. Mark the core modules packages that you require on the system to prevent them from
   being removed. For example:

   ```
   sudo dnf mark install kernel-uek-core kernel-uek-modules
   ```
2. Remove the unused modules packages and the `kernel-uek` metapackage from
   the system:

   ```
   sudo dnf erase kernel-uek-modules-desktop kernel-uek
   ```


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-DefaultPageSizeonArmPlatform.html -->

## (aarch64) 64k Base Page Size on Arm

In addition to the standard build of UEK for Arm (aarch64), which sets a base 4k page size, a
`kernel-uek64k` package that sets a 64k base page size is available for
Ampere Arm-based Compute shapes in Oracle Cloud Infrastructure only. For use cases other than
OCI, the `kernel-uek64` package is available only as a technical preview. The
`kernel-uek64k` package is available for Oracle Linux 9 and later.

The 64k page size kernel is a useful option for Ampere (Arm-based) platforms that process
workloads with large, contiguous memory datasets, and can achieve better performance for some
types of memory and CPU intensive operations.

The 4k page size kernel is useful for smaller environments, where minimizing physical system
memory usage is a priority.

Note that the 4k page size kernel and 64k page size kernel don't differ in user
experience as the user space is the same.

After a system is installed with `kernel-uek64k` switching to a 4k kernel page
size is unsupported.

### Installing `kernel-uek64k`

Note:

Installation of `kernel-uek64k` on systems outside
of Oracle Cloud Infrastructure (OCI) is only available as a technical preview. Don't install
this kernel on production systems outside of OCI.

To install the `kernel-uek64k` on a system installed with the standard 4k
page size `kernel-uek`:

1. Install the `kernel-uek64k`
   package.

   ```
   sudo dnf install -y kernel-uek64k
   ```
2. Set the 64k page size kernel as the default
   kernel.

   ```
   sudo grubby --set-default=$(echo /boot/vmlinuz*64k)
   ```

   Note
   that if you have more than one 64k page kernel installed, you must explicitly declare
   the kernel that you intend to be the default. For
   example:

   ```
   sudo grubby --set-default=/boot/vmlinuz-6.12.0-0.20.20.el9uek.aarch64.64k
   ```
3. Reboot the
   system.

   ```
   sudo reboot
   ```
4. After the system is rebooted, verify that the page size is
   64k.

   ```
   getconf PAGESIZE
   ```

   If the
   PAGESIZE returns 65536, the 64k kernel is loaded. If the PAGESIZE returns 4096, the 4k
   kernel is loaded and you must check that the default kernel is set correctly.

   You
   can also check that the running kernel contains the 64k string, for
   example:

   ```
   uname -a|grep 64k
   ```
5. If the system is running the 64k kernel, proceed to remove the 4k page size kernel
   packages to avoid future
   conflicts.

   ```
   sudo dnf erase kernel-uek-core
   ```


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-GenericPlatformUpdates.html -->

## Generic Platform Updates

Some generic platform updates are available in UEK 8. Updates include:

- Split-lock detection for operations on memory that spans two cache lines, such as
  misaligned memory access. See also <https://docs.kernel.org/arch/x86/buslock.html>
- Call depth tracking is implemented to improve performance in the Retbleed security
  vulnerability mitigation code.
- x86 CPU bringup is updated so that secondary CPU cores are booted in parallel to
  improve kernel boot times on high core count systems.
- 32-bit emulation on x86\_64 kernels with the `ia32_emulation`
  command-line parameter. When set to true, you can load 32-bit programs and run
  32-bit system calls.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-IntelPlatformUpdates.html -->

## Intel Platform Updates

Some upstream Intel platform updates are included in UEK 8. Notable items include:

- Intel Software Guard Extensions (SGX2), a hardware-based implementation of Enclave Dynamic
  Memory Management (EDMM), is an enhanced version of a security technology that can protect
  sensitive data and code by isolating them in private memory regions called enclaves. SGX2
  introduces new features such as dynamic memory management, so that enclaves can resize and
  manage their memory during runtime. This update is important for applications with dynamic
  workloads or larger memory requirements, that require a more scalable architecture. SGX2
  provides robust confidentiality and integrity for sensitive workloads in both on-premises
  and cloud environments. See <https://www.intel.com/content/www/us/en/support/articles/000058764/software/intel-security-products.html>.
- Quick Assist Technology (QAT) functionality is updated to support 4th Gen Intel Xeon processors.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-core-feature-eevdf_scheduler_replaces_cfs.html -->

## EEVDF Scheduler Replaces CFS

Earliest Eligible Virtual Deadline First (EEVDF) is a new kernel scheduler that replaces the
Completely Fair Scheduler (CFS). EEVDF provides a better scheduling policy for the kernel and
reduces configuration complexity and improves scheduling behavior.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-MM.html -->

## Memory Management

Several important memory management updates are available in UEK 8 with upstream changes that
are included from v5.15 to v6.12.

- The folios data structure replaces struct page to provide better abstraction for the
  management of pages. Folios is a new data structure that represents one or more pages of
  memory. The new structure reduces type confusion and memory overhead.
- Huge Pages are improved with several useful updates, including:
  - Update to handle hugeTLB faults when using per-VMA locking. Memory management operations like
    page faults and memory mapping can be handled in a more fine-grained and efficient
    manner reducing contention and improving concurrency.
  - Split underused THPs, and improve THP=always policy. These changes improve
    overprovisioning of THPs in sparsely accessed memory areas.
- Continued improvements to memory control groups code, memcg, to decouple v1 fields
  in the code from the v2 code base.
- Memory Mapping optimizations:

  - Maple Tree replaced Red-Black Trees (RB Trees) for managing virtual memory areas
    (VMAs) for better performance with faster lookups, inserts, and deletes.
  - Per-VMA mmap locking to improve concurrency and reduce contention in
    multithreaded applications with many VMAs.
  - Introduction of the `ptdesc` data structure to optimize
    management of page tables by decoupling page metadata from the
    `page` data structure.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8-FileSystems.html -->

## File Systems

The following file systems features and enhancements are introduced in UEK 8:

### Btrfs

The following notable Btrfs file system changes are introduced in UEK 8:

- Compressed data can be sent or received without transformation, and data chunks larger than 64K
  are now handled for writes.
- Quota accounting is simplified. Simple quotas can be used instead of quota groups for
  straightforward tracking of space usage by linking extents to their subvolumes. This
  approach can improve performance, but simple quotas are unable to track shared data, so
  are best suited to environments where extents are immutable and persist longer than any
  copies.
- The introduction of a temporary FSID makes it possible to mount cloned devices. The file system
  gets a randomly generated UUID on mount.
- Improved NOCOW write checks improve throughput by 9%.
- A new mount option `discard=async` is enabled by default for devices that support
  trim/discard, applying asynchronous discard for the whole file system.
- The mount option `ignoremetacsums` ignores invalid metadata checksums, and the
  `ignoresuperflags` mount option can be set to ignore superblock flags
  tracking conversion progress.
- Send and relocation tasks, such as balance, device removal, shrink, and block group reclaim, run
  in parallel.
- Devices can be added during a paused balance.

### XFS

The following notable XFS file system changes are introduced
in UEK 8:

- You can now mount a file system with the blocksize larger than the pagesize.
- Large extent counts are available for big virtual disk images.
- Atomic file content commits are now available.
- Fully autonomous online fsck and repair are available as a technical preview.
- An update to the `mkfs.xfs` command sets a minimum XFS file system size
  to 300 MB to prevent the creation of small file systems that caused performance and
  redundancy problems. This change differs from the command included in the earlier
  `xfsprogs` package available in the `ol9_baseos_latest`
  repository on Oracle Linux 9 systems.

### NFS

The following notable NFS file system changes are introduced in UEK 8:

- NFSv4.2 READ\_PLUS feature is enabled by default within the kernel to improve handling of
  sparse files by including a description of holes, or data blocks that are
  uninitialized.
- Various older protocol features for NFS are removed in UEK 8. See [Deprecated and Removed Features](uek8.0-DeprecatedandRemovedFeatures.html#uek8-features-removed).


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-BPF.html -->

## Berkeley Packet Filter (BPF) Enhancements

Several important updates are available in UEK 8 for the Berkeley Packet Filter (BPF),
including:

- Introduction of a dedicated BPF memory allocator is added to improve the
  reliability of allocations made within BPF programs, which can run in a wide
  variety of contexts.
- Addition of a new user ring buffer BPF map type for asynchronous message passing
  and faster data transfer between a BPF program and user space.
- BPF programs can now call kernel functions from a loadable module, can access and
  store task\_struct objects, and can use absolute time values.
- Friendlier helper functions, such as `bpf_trace_vprintk`, and also
  destructive helpers such as `crash_kexec`, are included.
- BPF programs can attach filter functions to kfuncs. The filter can limit the
  contexts from which the kfunc can be invoked.
- Resilient BPF Type Format (BTF) information for modules is included so that out-of-tree
  modules can define BTF that works for the lifetime of a UEK release.
- BPF trampoline is now available for aarch64 platforms to provide faster BPF tracing
  program execution using Fentry and Fexit programs.
- BPF hooks:

  - To see and filter complete packets.
  - To change the requested protocol for a new socket, primarily to
    transparently cause programs requesting TCP connections to use multipath
    TCP instead.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-core-feature-io_uring_enhancements.html -->

## `io_uring` Enhancements

`io_uring` is a system call interface to manage storage device
asynchronous I/O operations. Several features and improvements are provided in the
implementation that's available in UEK 8 and some of these might have been backported
to previous UEK releases. Updates include many optimizations for security and
performance. Significant new features and changes include:

- `io_uring` now supports sending and receiving T10 Protection Information
  along with the data buffer.
- Operations for `getsockopt()`, `setsockopt()`,
  `bind()`, `listen()` and `waitid()`.
- Mechanism to omit system calls with IORING\_SETUP\_SQPOLL at setup time. A call to
  `io_uring_enter()` starts a kernel thread that occasionally polls the
  submission queue and automatically submits any requests found there.
- Batch request for `recv()` calls and for `reads()`.
- IORING\_OP\_SENDZC to perform Zero-copy writes.
- Several Ring code optimizations:

  - Rings and submission queue can be in user space memory, such as huge pages.
  - One ring is now able to signal another to speed up message requests.
  - Ring related work can be deferred until an application asks for it.
- `io_uring` improvements in buffered writes, in XFS.
- `io_uring` optimization in XFS and Ext4 can handle multiple direct-I/O
  writes to a file in parallel.
- Absolute timeouts, along with the relative timeouts that were already available, are now
  possible.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-ASMLib.html -->

## ASMLib v3

ASMLib is a library for the Automatic Storage Management feature of the Oracle Database.
ASMLib v3 takes advantage of the `io_uring` features included in the
kernel to deliver high performance. UEK 8 is tested and fully supported with Oracle
ASMLib v3.

Note that with this update, the `oracleasm` kernel module is no longer
included, as Oracle ASMLib v3 no longer requires this module to work.

ASMLIB release 3.1 leverages the protection information passthrough enhancements added to
`io_uring` in UEK 8. Through this interface CRC checksums can be attached to
each I/O, providing an additional layer of protection against data corruption.

To use this feature, ASM disks must be provisioned on storage hardware which implements T10
Protection Information (SCSI controller with DIX support or NVMe).

See [Oracle Linux: Installing and Configuring Oracle ASMLIB
v3](https://docs.oracle.com/en/operating-systems/oracle-linux/asmlib/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-RDMA.html -->

## RDMA

UEK 8 includes Remote Direct Memory Access (RDMA) features that are provided in the upstream
kernel, with the addition of Ksplice and DTrace functionality. RDMA enables direct memory
access between two systems that are connected by an InfiniBand or RoCE network. RDMA
facilitates high-throughput and low-latency networking in clusters.

Oracle RDMA packages are available in the following ULN channels and yum repositories:

- Oracle Linux 10

  - ULN channel: `ol10_x86_64_RDMA`
  - Oracle Linux yum server repository: `ol10_RDMA`
- Oracle Linux 9

  - ULN channel: `ol9_x86_64_RDMA`
  - Oracle Linux yum server repository: `ol9_RDMA`

See [Upgrading Oracle RDMA Packages on Oracle Linux](uek8.0-UpgradingOracleSupportedRDMAPackagesonOracleLinux.html#uek8_upgrade_rdma) if you're upgrading a system that has the
`oracle-rdma-release` or `oracle-rdma-release-guest` package
installed.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-Networking.html -->

## General Networking Enhancements

Some general networking enhancements are available in UEK 8 with upstream changes that
are included from v5.15 to v6.12.

- BIG TCP, which uses bigger TSO/GRO packet sizes for IPv6 traffic, is included to
  improve the performance when sending large IPv6 TCP packets on data-center
  networks. Note that this feature isn't enabled by default because it can affect
  eBPF programs that might assume the TCP header immediately follows the IPv6
  header. BIG TCP is enabled by setting the `gro_ipv6_max_size` and
  `gso_ipv6_max_size` on a link device.
- A new socket option SO\_RESERVE\_MEM is available to provide a mechanism for users
  to reserve a certain amount of memory for the socket. With this socket option
  set, the networking stack spends less cycles doing forward alloc and reclaim,
  which can lead to better system performance, with the cost of an amount of
  preallocated and irreclaimable memory, even under memory pressure.
- The fair queuing packet scheduler has gained several performance improvements,
  including a 5% throughput increase in intensive TCP Request/Response (TCP\_RR)
  workload, and 13% increase for UDP packets without a pacing rate set on the
  socket.
- Several core networking data structures are reorganized for better cache
  efficiency that can result in TCP performance improvement in where the are many
  concurrent connections.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-KTLS.html -->

## KTLS

KTLS handles TLS records using the symmetric encryption or decryption algorithms in the
kernel for the AES-GCM cipher. KTLS was enabled in UEK R7U3 for TLS encrypted
connections for NFS. KTLS continues to be available in UEK 8.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/8.0-feature-nfs-rpc-tls.html -->

## TLS Encrypted Connections for NFS

RPC-With-TLS is enabled in the Linux NFS server and client. This update provides a
standards-based peer authentication mechanism over an encrypted connection using TLS. The TLS
Record protocol is handled entirely by kTLS.

Note that both the server and client systems must run UEK R7U3 or later, or must be running a
kernel and user space client that supports RFC 9289, to use this functionality. The user space
package, `ktls-utils`, is also required and must be installed on both the
client and server systems. Also ensure that you have installed the most recent version of the
`nfs-utils` package or that you have done a full system update.

RPC-With-TLS is contributed upstream by Oracle and is described in [RFC 9289](https://datatracker.ietf.org/doc/rfc9289/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-RNG.html -->

## Random Number Generator Enhancements

Some enhancements to the Random Number Generator (RNG) are available in UEK 8 with
upstream changes that are included from v5.15 to v6.12. Most notably, RNG has switched
from the SHA1 hash algorithm to the faster and more secure BLAKE2s algorithm.

Also, the `getrandom()` system call is now implemented in the kernel's
virtual dynamic shared object (vDSO) area. This implementation improves performance when
obtaining random number data by removing the need to switch from a user space context
into the kernel context.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-kvm-virtualization.html -->

## KVM and Virtualization

The following KVM and virtualization changes are included in this release of UEK 8:

- Two-Dimensional Paging (TDP) MMU support is added to significantly improve page fault performance on many-VCPU VMs. This functionality is enabled by default.
- The UEK 8 kernel configuration for VCPUs is increased to a
  theoretical limit of 4096. Note that the actual VCPU limit is use case specific
  and dependent on many factors including system and QEMU configuration.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek_8_0_features_driver_updates.html -->

## Updated Drivers

Device drivers included in UEK 8 are aligned with
the drivers in the upstream mainline Linux 6.12 kernel. A few notable updates are
included where drivers include functionality or fixes available in later upstream kernel
versions.

Many driver modules no longer track version information. Oracle works with vendors to
align device drivers included in UEK 8 with the code
available in upstream kernel versions.

Notable driver updates are presented in the following table:

Table 2-1 Driver Alignment

| Driver Module | Driver Description | Aligned Kernel Version | Notable Updates |
| --- | --- | --- | --- |
| `fnic` | Cisco FCoE HBA Driver | 6.14 | Updates from 6.14 were backported to this release. Note that this driver includes a version string: 1.8.0.0. |
| `lpfc` | Broadcom Emulex Fibre Channel HBA Driver | 6.14 | Updates from 6.14 were backported to this release. Note that this driver includes a version string: 0:14.4.0.8. |
| `mlx5` | NVIDIA 5th Generation Network Adapters (NVIDIA ConnectX series) Core Driver | 6.12 | Several fixes and improvements from 6.14 were backported in this release. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-DeprecatedandRemovedFeatures.html -->

## Deprecated and Removed Features

The following features are deprecated, removed, or no longer supported in UEK 8:

Deprecated Features

- SHA-1 Algorithm

  The SHA-1 algorithm is deprecated in UEK 8 while in
  FIPS mode and will be removed in a future UEK release. The SHA-1 algorithm has been
  retired by National Institute of Standard and Technology (NIST) because the SHA-1 hash
  algorithm is no longer considered secure. See Oracle Linux release notes for more
  details on SHA-1 usage and deprecation.
- Kernel modules moved to the `kernel-uek-modules-deprecated` package
  are now deprecated.

  These modules might be removed in a future release of UEK.

  See [Module Deprecations (x86\_64)](module_deprecations_x86_64.html) and
  [Module Deprecations (aarch64)](module_deprecations_aarch64.html) for a
  detailed listing.
- `cgroupsv1` is deprecated

  `cgroupsv1` is deprecated in Oracle Linux 9 and will be removed in a
  future Oracle Linux release.
- `XFS_SUPPORT_V4` is deprecated

  The V4 file system format contains known weaknesses in the on-disk format. Therefore,
  the option is deprecated in UEK 8 and will be removed
  in a future UEK release.

  You can check whether the file system is formatted to use V4, by running the
  `xfs_db -r -c version`
  <device> command.

  If the feature is enabled, you must backup data, reformat the device, and restore
  data.
- `XFS_SUPPORT_ASCII_CI` is deprecated

  The XFS ASCII case-insensitive name feature is deprecated in UEK 8 and will be removed in a future UEK release. The
  feature provided an option to format an XFS file system with the
  `ascii-ci` option enabled to disable case-sensitivity.

  You can check whether the feature is enabled by using the `xfs_info`
  command.

  If the feature is enabled, you must backup data, reformat the device with the option
  disabled, and restore data.
- `CONFIG_SECURITY_SELINUX_DISABLE` and
  `CONFIG_SECURITY_WRITABLE_HOOKS` options are disabled

  The option to disable SELinux at runtime by using the sysfs interface is removed in
  this UEK release.

  The preferred method of disabling SELinux is by using the `selinux=0`
  boot parameter

Removed Features

- `CONFIG_RPCSEC_GSS_KRB5_ENCTYPES_DES` option for 3DES/DES3 RPCSEC GSS
  encryption types is disabled

  The RPCSEC GSS encryption types DES and Triple-DES (3DES/DES3) is removed in this UEK
  release.

  These encryption types were deprecated by RFCs 6649 and 8429 because they're known to
  be insecure.
- `CONFIG_NFS_V2` and `CONFIG_NFSD_V2` options for NFSv2
  client and server are disabled

  Support for NFSv2 clients and NFSv2 servers is removed in this UEK release.

  NFSv2
  has long been replaced by NFSv3 and NFSv4, which offer improved functionality,
  performance, and security.
- `CONFIG_NFS_DISABLE_UDP_SUPPORT` option for NFSv3 over UDP is
  enabled

  Support for NFS version 3 over the UDP network protocol is removed in this UEK
  release.

  Modern NFS/RPC over TCP and RDMA implementations provide better
  performance than UDP, and provide reliable ordered delivery of data combined with
  congestion control.

  Note that NFSv4 is already not supported over UDP, for the same
  reasons.
- `CONFIG_STAGING` option is disabled

  The `CONFIG_STAGING` kernel configuration option is disabled in UEK 8. The kernel option made available drivers that
  don't necessarily meet the highest kernel quality level and which were available for
  test use. The option was deprecated in UEK R7 and is removed in UEK 8.
- `CONFIG_IXGB` option is disabled

  The `CONFIG_IXGB` for Intel PRO/10GbE hardware is removed in this UEK
  release.
- crashkernel=auto removed

  The `crashkernel=auto` option was deprecated in UEK R7 and unsupported
  for Oracle Linux 9. The kernel option is removed in UEK 8. For more information about configuring the `crashkernel` setting on
  Oracle Linux 9, see [Oracle Linux 9: Managing Kernels and System Boot](https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/).
- `CONFIG_IP_NF_TARGET_CLUSTERIP` option is disabled

  The `CONFIG_IP_NF_TARGET_CLUSTERIP` option that allowed you to build
  load-balancing clusters of network servers without a dedicated load-balancing router or
  switch is removed in favor of functionality already in Netfilter cluster match.
- `CONFIG_EFI_VARS` option disabled

  The `CONFIG_EFI_VARS` option that provided the `efivars`
  sysfs interface to configure UEFI variables is removed from this release of UEK.
  Replacement functionality has been present in the kernel since 2012. For more
  information, see <https://www.kernel.org/doc/html/latest/filesystems/efivarfs.html>.
- Firewire driver removed

  The `CONFIG_FIREWIRE` option is disabled in this UEK release.
- Several Network Scheduler Modules Removed

  The following network scheduler modules were deprecated in UEK R7 and are now removed
  in UEK 8:

  - `cls_tcindex`
  - `cls_rsvp`
  - `sch_dsmark`
  - `sch_atm`
  - `sch_cbq`
- `resilient_rdmaip` Module Removed

  The `resilient_rdmaip` module was deprecated in UEK R7 and is now
  removed.
- `oracleasm` Kernel Module Removed

  The `oracleasm` kernel module is removed in UEK 8. Note that this module continues to be supported in
  the UEK R5 and UEK R6 releases.

  Oracle ASMLib continues to be supported using `io_uring` interfaces.
  See [ASMLib v3](uek8.0-ASMLib.html#uek8-asmlib) for more information.
- `sundance` Kernel Module Removed

  The DLink Sundance (ST201), `sundance`, driver is removed in UEK 8. The module was removed in the upstream kernel
  because it was unmaintained.
- `cpu5_wdt` Kernel Module Removed

  The `cpu5_wdt` watchdog driver is removed in UEK 8. The module was removed in the upstream kernel
  because it had several issues that were unresolved and lacked maintenance.
- `i2c-amd756-s4882` and `i2c-nforce2-s4985` Kernel
  Modules Removed

  The `i2c-amd756-s4882` and `i2c-nforce2-s4985` legacy
  muxing drivers are removed in UEK 8. The module was
  removed in the upstream kernel because they're old and contain technically inaccurate
  code.
- `CONFIG_CRYPTO_OFB` and `CONFIG_CRYPTO_CFB`
  cryptographic modes

  The CFB (Cipher Feedback) mode (NIST SP800-38A) used for TPM2 cryptography and the OFB
  (Output Feedback) mode (NIST SP800-38A) used to turn a block cipher into a synchronous
  stream cipher are removed in UEK 8, to align with
  upstream changes.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-RelatedUserSpacePackages.html -->

## 3 Related User Space Packages

To expose newly added functionality that's included in UEK 8, several user space binary
packages are required. Some of these packages are separate from the packages that are included
in the base distribution.

For more information about the ULN channels and Oracle Linux yum server
repositories in which these packages are available, see
[Installation and Availability](uek8.0-InstallationandAvailability.html#ol_instav).

The packages listed in the following table are specific to user space functionality. The
versions listed are tested to take advantage of the features that are available in UEK 8. If
you use any of the packages that are listed with UEK 8, update the package to the latest
version for full compatibility with all the features that are included in this release. Note
that `btrfs-progs`, `ocfs2-tools` and the user space packages
released in the UEK 8 repository are only supported with UEK 8 and should not be installed on
systems using RHCK.

Table 3-1 User Space Packages for UEK 8

| Package Name | Oracle Linux 9 Version |
| --- | --- |
| `adaptivemm` | 2.1.0-2 |
| `bcache-tools` | 1.0.8-3.101.0.1 |
| `bpftool` | 7.4.0-503.23.2 |
| `btrfs-progs` | 6.12.0-0 |
| `btrfs-progs-devel` | 6.12.0-0 |
| `crash` | 8.0.6-1.0.1 |
| `cxl-cli` | 78-2 |
| `cxl-devel` | 78-2 |
| `cxl-libs` | 78-2 |
| `daxctl` | 78-2 |
| `daxctl` | 78-2 |
| `dmidecode` | 3.6-1 |
| `dnf-plugins-extras` | 4.0.15-3.0.1 |
| `dtrace` | 2.0.2-5 |
| `dtrace-devel` | 2.0.2-5 |
| `dtrace-testsuite` | 2.0.2-5 |
| `dwarves` | 1.28-1 |
| `e2fsprogs` | 1.46.5-5 |
| `ipmctl` | 03.00.00.0485-1.0.1 |
| `iproute` | 6.8.0-2 |
| `kexec-tools` | 2.0.29-5.0.2 |
| `libbpf` | 1.5.0-2.0.1 |
| `libbpf-devel` | 1.5.0-2.0.1 |
| `libdnf` | 0.69.0-12.0.1 |
| `libdwarves1` | 1.28-1 |
| `libipmctl5` | 03.00.00.0485-1.0.1 |
| `libipmctl5-devel` | 03.00.00.0485-1.0.1 |
| `libnvme` | 1.9-3 |
| `linux-firmware` | 20250319-999.39.git430633ec |
| `mcelog` | 204-1.0.1 |
| `microcode_ctl` | 20240910-1.0.2 |
| `ndctl` | 78-2 |
| `nvme-cli` | 2.9.1-6 |
| `ocfs2-tools` | 1.8.6-17 |
| `pciutils` | 3.7.0-5 |
| `pciutils-libs` | 3.7.0-5 |
| `snapper` | 0.8.7-4 |
| `wireguard-tools` | 1.0.20210914-3 |
| `xfsprogs` | 6.12.0-1.0.1 |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-KnownIssues.html -->

## 4 Known Issues

This chapter describes any known issues for Unbreakable Enterprise Kernel 8.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-UnusableorUnavailableFeaturesfortheArmPlatform.html -->

## Unusable or Unavailable Features for Arm Platforms

The following features are known to not work, remain untested, or have issues that render
the feature unusable. The following features aren't supported on Arm platforms:

- InfiniBand
- FibreChannel
- RDMA


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/38006792.html -->

## Xen Hypervisor VM CPU Initialization Failure

On some Xen-based virtualization platforms, such as Oracle VM 3.4, only the first CPU is
initialized when the guest VM is started. VM boot is slow, the remaining configured CPUs
fail to report an `alive` state, and the following errors might appear in
the VM `dmesg` output:

```
...
[   10.190039] CPU1 failed to report alive state
[   20.192038] CPU2 failed to report alive state
...
```

The issue is related to a problem in the Xen hypervisor's `x2apic`
emulation. The incorrect APIC ID is returned.

To work around the issue, add the `nox2apic` parameter to the kernel command line and reboot.

1. In the VM, edit `/etc/default/grub` to add the
   `nox2apic` parameter to the GRUB\_CMDLINE\_LINUX entry:

   ```
   GRUB_CMDLINE_LINUX="...... nox2apic"
   ```
2. Regenerate the `/boot/grub2/grub.cfg` file:

   ```
   sudo grub2-mkconfig -o /boot/grub2/grub.cfg --update-bls-cmdline
   ```
3. Reboot the virtual machine

(Bug 38006792)


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-UpgradingOracleSupportedRDMAPackagesonOracleLinux.html -->

## Upgrading Oracle RDMA Packages on Oracle Linux

You can upgrade the Oracle RDMA packages on Oracle Linux by using the `dnf
update` command.

If you're upgrading a system that has the `oracle-rdma-release` or
`oracle-rdma-release-guest` package installed, if the package version is
lower than version 0.18.1-1 and you intend to upgrade to version 0.18.1-1, or later, you must
first manually remove the `rdma-core-devel` package. Remove this package by
using the `rpm -e --nodeps` command, which removes the package outside of
the standard yum or DNF package manager control and leaves any dependencies intact, for
example:

```
sudo /bin/rpm -e --nodeps rdma-core-devel
sudo dnf update
```

If the system you have upgraded has the `oracle-rdma-release` or
`oracle-rdma-release-guest` package installed and if the package version is
version 0.31.0-1, then you can remove it because that package no longer serves any purpose:

```
sudo dnf remove oracle-rdma-release*
```


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-InstallationandAvailability.html -->

## 5 Installation and Availability

This chapter provides information about the availability of
UEK 8 on Oracle Linux and includes installation and instructions on
upgrading from a previous UEK release to UEK 8.

UEK 8 is supported on the Intel® 64-bit x86\_64, AMD 64-bit
x86\_64 and 64-bit Arm (aarch64) platforms.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-AboutUpgradingFromaPreviousOracleLinuxorUEKReleasetoUEK8.html -->

## About Upgrading From a Previous Oracle Linux or UEK Release to UEK 8

UEK 8 is the default kernel on Oracle Linux 10.

UEK 8 is made available for installation on Oracle Linux 9, starting with the Oracle Linux
9.5 release, and is the default kernel on Oracle Linux 9.6.

The suggested migration path for upgrading the system from an earlier UEK release to UEK 8
is as follows:

- If you're running an Oracle Linux 8 release you must upgrade to Oracle Linux 9 to
  install UEK 8. For instructions on upgrading an Oracle Linux 8 system to Oracle Linux 9,
  see [Oracle Linux 9: Upgrading Systems With
  Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/9/leapp/).
- If you're running an Oracle Linux 9 release, you must ensure that the system is updated
  to the latest update level before installing UEK 8.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-ObtainingPackagesforInstallation.html -->

## Obtaining Packages for Installation

If you have a subscription to Oracle Unbreakable Linux support, you can obtain the packages
for UEK 8 by registering the system with the Unbreakable Linux Network (ULN) and then
subscribing it to other channels. See [Subscribing to ULN Channels](uek8.0-ObtainingPackagesforInstallation.html#ol_sub_uln).

If the system isn't registered with ULN, you can obtain most of the required packages from
the Oracle Linux yum server. See [Enabling Access to Oracle Linux Yum Server Repositories](uek8.0-ObtainingPackagesforInstallation.html#ol_sub_pubyum).

When you have subscribed the system to the appropriate ULN channels or to the Oracle Linux
yum server, you can proceed to upgrade the system to UEK 8. See [Upgrading a System to UEK 8](uek8.0-UpgradingaSystemtoUEK8.html#ol_upgradea_sys).

### Enabling Access to Oracle Linux Yum Server Repositories

Packages for UEK 8 and any
associated user space applications are available on the Oracle Linux yum server at <https://yum.oracle.com/>
in yum repositories that are available for each supported Oracle Linux release.

- Oracle Linux 9: `ol9_UEKR8`
- Oracle Linux 10: `ol10_UEKR8`

#### Oracle Linux 10

To enable access to the UEK 8 repository on the Oracle Linux yum server, use the
`dnf config-manager` command.

Note:

64-bit Arm (aarch64) platforms that have Oracle Linux 10 installed use UEK 8 by default and
RHCK isn't available on these platforms, therefore no installation steps are required.

1. Ensure that you have the latest `oraclelinux-release-el10` package
   installed and updated.

   ```
   sudo dnf install -y oraclelinux-release-el10
   ```

   The package contains the yum repository definition for the `ol10_UEKR8`
   repository.
2. Enable the `ol10_UEKR8` repository.

   ```
   sudo dnf config-manager --set-enabled ol10_UEKR8
   ```
3. Install the UEK 8 packages, for example:

   ```
   sudo dnf install -y kernel-uek kernel-uek-devel
   ```

   Installing the `kernel-uek-devel` package also installs the
   `gcc-toolset-14` packages.
4. Verify the UEK 8 kernel packages are installed, for example:

   ```
   dnf list --installed kernel-uek*-6.12.0-*
   ```

#### Oracle Linux 9

To enable access to the UEK 8 repository on the Oracle Linux yum server, use the
`dnf config-manager` command.

1. Ensure that you have the latest `oraclelinux-release-el9` package
   installed and updated.

   ```
   sudo dnf install -y oraclelinux-release-el9
   ```

   The package contains the yum repository definition for the `ol9_UEKR8`
   repository.
2. Enable the `ol9_UEKR8` repository.

   ```
   sudo dnf config-manager --set-enabled ol9_UEKR8
   ```
3. Install the UEK 8 packages, for example:

   ```
   sudo dnf install -y kernel-uek kernel-uek-devel
   ```

   Installing the `kernel-uek-devel` package also installs the
   `gcc-toolset-14` packages.
4. Verify the UEK 8 kernel packages are installed, for example:

   ```
   dnf list --installed kernel-uek*-6.12.0-*
   ```

### Subscribing to ULN Channels

UEK 8 kernel image and user space
packages are made available for the each supported Oracle Linux release and platform
architecture in the following ULN channels:

- Oracle Linux 10 (x86\_64): `ol10_x86_64_UEKR8`
- Oracle Linux 10 (aarch64): `ol10_aarch64_UEKR8`
- Oracle Linux 9 (x86\_64): `ol9_x86_64_UEKR8`
- Oracle Linux 9 (aarch64): `ol9_aarch64_UEKR8`

The following instructions assume that you have already registered the system with ULN.

To subscribe a system to a ULN channel:

1. Sign in to <https://linux.oracle.com> with a ULN username and password.
2. On the Systems tab, in the list of registered machines, select the link that corresponds
   to the name of the system.
3. On the System Details page, select Manage Subscriptions.
4. On the System Summary page, from the list of available channels, select each of the
   required channels, then select the right arrow to move the selected channel to the list of
   subscribed channels.
5. Select Save Subscriptions.

For more information about using ULN, see [Oracle Linux: Managing Software on Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/uek8.0-UpgradingaSystemtoUEK8.html -->

## Upgrading a System to UEK 8

The following instructions describe how to upgrade a system to UEK 8. For more details about
the suggested migration paths for upgrading to UEK 8, see [About Upgrading From a Previous Oracle Linux or UEK Release to UEK 8](uek8.0-AboutUpgradingFromaPreviousOracleLinuxorUEKReleasetoUEK8.html#uek8-upgrade-paths).

1. Enable access to the appropriate ULN channels or yum
   repositories, as described in [Subscribing to ULN Channels](uek8.0-ObtainingPackagesforInstallation.html#ol_sub_uln)
   and [Enabling Access to Oracle Linux Yum Server Repositories](uek8.0-ObtainingPackagesforInstallation.html#ol_sub_pubyum).

   Tip:

   Disable any other UEK channels or repositories that you might have previously
   configured as good practice.
2. After enabling access to the appropriate channels or repositories, upgrade the system to
   UEK 8 by running the following commands:

   ```
   sudo dnf install -y kernel-uek
   sudo dnf update -y
   ```
3. After the upgrade has completed, reboot the system.

   Ensure to select the UEK 8 kernel (version 6.12.0) if it's not the default boot kernel.
   For more information about setting the default boot kernel, see [Oracle Linux 9: Managing Kernels and System Boot](https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/) or [Oracle Linux 10: Managing Kernels and System
   Boot](https://docs.oracle.com/en/operating-systems/oracle-linux/10/boot/).

For questions regarding installing software or updating a
system, see [Oracle Linux: Managing Software on Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/module_deprecations_x86_64.html -->

## A Module Deprecations (x86\_64)

The following modules are deprecated in this release of UEK 8.
While these modules are available and operative in this release, they are planned for removal
and support isn't guaranteed in future UEK releases. Thus, these modules should not be used in
new UEK 8 deployments to avoid problems upgrading in the future.

Table A-1 Module Deprecations (x86\_64)

| Module Name | Description |
| --- | --- |
| `a8293` | Allegro A8293 |
| `adm8211` | ADMtek ADM8211 support |
| `af9013` | Afatech AF9013 demodulator |
| `af9033` | Afatech AF9033 DVB-T demodulator |
| `atbm8830` | AltoBeam ATBM8830/8831 DMB-TH demodulator |
| `atmtcp` | ATM over TCP |
| `au8522_common` |  |
| `au8522_decoder` | Auvitek AU8522 based ATV demod |
| `au8522_dig` | Auvitek AU8522 based DTV demod |
| `b2c2-flexcop` |  |
| `b2c2-flexcop-pci` | Technisat/B2C2 Air/Sky/Cable2PC PCI |
| `b2c2-flexcop-usb` | Technisat/B2C2 Air/Sky/Cable2PC USB |
| `b43legacy` | Broadcom 43xx-legacy wireless support (mac80211 stack) |
| `bcm3510` | Broadcom BCM3510 |
| `cpu5wdt` | SMA CPU5 Watchdog |
| `cx22700` | Conexant CX22700 based |
| `cx22702` | Conexant cx22702 demodulator (OFDM) |
| `cx23885` | Conexant cx23885 (2388x successor) support |
| `cx24110` | Conexant CX24110 based |
| `cx24113` | Conexant CX24113/CX24128 tuner for DVB-S/DSS |
| `cx24116` | Conexant CX24116 based |
| `cx24117` | Conexant CX24117 based |
| `cx24120` | Conexant CX24120 based |
| `cx24123` | Conexant CX24123 based |
| `cxd2099` | Sony CXD2099AR Common Interface driver |
| `cxd2820r` | Sony CXD2820R |
| `cxd2841er` | Sony CXD2841ER |
| `dib0070` | DiBcom DiB0070 silicon base-band tuner |
| `dib0090` | DiBcom DiB0090 silicon base-band tuner |
| `dib3000mb` | DiBcom 3000M-B |
| `dib3000mc` | DiBcom 3000P/M-C |
| `dib7000m` | DiBcom 7000MA/MB/PA/PB/MC |
| `dib7000p` | DiBcom 7000PC |
| `dib8000` | DiBcom 8000MB/MC |
| `dibx000_common` | DiBcom 9000 |
| `drx39xyj` | Micronas DRX-J demodulator |
| `drxd` | Micronas DRXD driver |
| `drxk` | Micronas DRXK based |
| `ds3000` | Montage Tehnology DS3000 based |
| `dvb-pll` | Generic I2C PLL based tuners |
| `dvb-usb` | Support for various USB DVB devices |
| `dvb-usb-a800` | AVerMedia AverTV DVB-T USB 2.0 (A800) |
| `dvb-usb-af9005` | Afatech AF9005 DVB-T USB1.1 support |
| `dvb-usb-af9005-remote` | Afatech AF9005 default remote control support |
| `dvb-usb-af9015` | Afatech AF9015 DVB-T USB2.0 support |
| `dvb-usb-af9035` | Afatech AF9035 DVB-T USB2.0 support |
| `dvb-usb-anysee` | Anysee DVB-T/C USB2.0 support |
| `dvb-usb-au6610` | Alcor Micro AU6610 USB2.0 support |
| `dvb-usb-az6007` | AzureWave 6007 and clones DVB-T/C USB2.0 support |
| `dvb-usb-az6027` | Azurewave DVB-S/S2 USB2.0 AZ6027 support |
| `dvb-usb-ce6230` | Intel CE6230 DVB-T USB2.0 support |
| `dvb-usb-cinergyT2` | Terratec CinergyT2/qanu USB 2.0 DVB-T receiver |
| `dvb-usb-cxusb` | Conexant USB2.0 hybrid reference design support |
| `dvb-usb-dib0700` | DiBcom DiB0700 USB DVB devices (see help for supported devices) |
| `dvb-usb-dibusb-common` | DiBcom USB DVB-T devices (based on the DiB3000M-B) (see help for device list) |
| `dvb-usb-dibusb-mb` | DiBcom USB DVB-T devices (based on the DiB3000M-B) (see help for device list) |
| `dvb-usb-dibusb-mc` | DiBcom USB DVB-T devices (based on the DiB3000M-C/P) (see help for device list) |
| `dvb-usb-dibusb-mc-common` |  |
| `dvb-usb-digitv` | Nebula Electronics uDigiTV DVB-T USB2.0 support |
| `dvb-usb-dtt200u` | WideView WT-200U and WT-220U (pen) DVB-T USB2.0 support (Yakumo/Hama/Typhoon/Yuan) |
| `dvb-usb-dtv5100` | AME DTV-5100 USB2.0 DVB-T support |
| `dvb-usb-dvbsky` | DVBSky USB support |
| `dvb-usb-dw2102` | DvbWorld & TeVii DVB-S/S2 USB2.0 support |
| `dvb-usb-ec168` | E3C EC168 DVB-T USB2.0 support |
| `dvb-usb-gl861` | Genesys Logic GL861 USB2.0 support |
| `dvb-usb-gp8psk` | GENPIX 8PSK->USB module support |
| `dvb-usb-lmedm04` | LME DM04/QQBOX DVB-S USB2.0 support |
| `dvb-usb-m920x` | Uli m920x DVB-T USB2.0 support |
| `dvb-usb-mxl111sf` |  |
| `dvb-usb-nova-t-usb2` | Hauppauge WinTV-NOVA-T usb2 DVB-T USB2.0 support |
| `dvb-usb-opera` | Opera1 DVB-S USB2.0 receiver |
| `dvb-usb-pctv452e` | Pinnacle PCTV HDTV Pro USB device/TT Connect S2-3600 |
| `dvb-usb-rtl28xxu` | Realtek RTL28xxU DVB USB support |
| `dvb-usb-technisat-usb2` | Technisat DVB-S/S2 USB2.0 support |
| `dvb-usb-ttusb2` | Pinnacle 400e DVB-S USB2.0 support |
| `dvb-usb-umt-010` | HanfTek UMT-010 DVB-T USB2.0 support |
| `dvb-usb-vp702x` | TwinhanDTV StarBox and clones DVB-S USB2.0 support |
| `dvb-usb-vp7045` | TwinhanDTV Alpha/MagicBoxII, DNTV tinyUSB2, Beetle USB2.0 support |
| `dvb_dummy_fe` | Dummy frontend driver |
| `dvb_usb_v2` | Support for various USB DVB devices v2 |
| `e4000` | Elonics E4000 silicon tuner |
| `ec100` | E3C EC100 |
| `fc0011` | Fitipower FC0011 silicon tuner |
| `fc0012` | Fitipower FC0012 silicon tuner |
| `fc0013` | Fitipower FC0013 silicon tuner |
| `fc2580` | FCI FC2580 silicon tuner |
| `gp8psk-fe` |  |
| `isl6405` | ISL6405 SEC controller |
| `isl6421` | ISL6421 SEC controller |
| `isl6423` | ISL6423 SEC controller |
| `it913x` | ITE Tech IT913x silicon tuner |
| `itd1000` | Integrant ITD1000 Zero IF tuner for DVB-S/DSS |
| `ix2505v` | Sharp IX2505V silicon tuner |
| `l64781` | LSI L64781 |
| `lg2160` | LG Electronics LG216x based |
| `lgdt3305` | LG Electronics LGDT3304 and LGDT3305 based |
| `lgdt3306a` | LG Electronics LGDT3306A based |
| `lgdt330x` | LG Electronics LGDT3302/LGDT3303 based |
| `lgs8gxx` | Legend Silicon LGS8913/LGS8GL5/LGS8GXX DMB-TH demodulator |
| `libertas_sdio` | Marvell Libertas 8385/8686/8688 SDIO 802.11b/g cards |
| `lnbh25` | LNBH25 SEC controller |
| `lnbp21` | LNBP21/LNBH24 SEC controllers |
| `lnbp22` | LNBP22 SEC controllers |
| `m88ds3103` | Montage Technology M88DS3103 |
| `m88rs2000` | M88RS2000 DVB-S demodulator and tuner |
| `m88rs6000t` | Montage M88RS6000 internal tuner |
| `max2165` | Maxim MAX2165 silicon tuner |
| `mb86a16` | Fujitsu MB86A16 based |
| `mb86a20s` | Fujitsu mb86a20s |
| `mc44s803` | Freescale MC44S803 Low Power CMOS Broadband tuners |
| `mn88472` | Panasonic MN88472 |
| `mn88473` | Panasonic MN88473 |
| `mt2060` | Microtune MT2060 silicon IF tuner |
| `mt2063` | Microtune MT2063 silicon IF tuner |
| `mt20xx` | Microtune 2032 / 2050 tuners |
| `mt2131` | Microtune MT2131 silicon tuner |
| `mt2266` | Microtune MT2266 silicon tuner |
| `mt312` | Zarlink VP310/MT312/ZL10313 based |
| `mt352` | Zarlink MT352 based |
| `mxl111sf-tuner` | MxL111SF DTV USB2.0 support |
| `mxl5005s` | MaxLinear MSL5005S silicon tuner |
| `mxl5007t` | MaxLinear MxL5007T silicon tuner |
| `mxl5xx` | MaxLinear MxL5xx based tuner-demodulators |
| `mxl692` | MaxLinear MXL692 based |
| `nxt200x` | NxtWave Communications NXT2002/NXT2004 based |
| `nxt6000` | NxtWave Communications NXT6000 based |
| `or51132` | Oren OR51132 based |
| `or51211` | Oren OR51211 based |
| `parport_pc` | PC-style hardware |
| `parport_serial` | Multi-IO cards (parallel and serial) |
| `pluto2` | Pluto2 cards |
| `qm1d1b0004` | Sharp QM1D1B0004 tuner |
| `qm1d1c0042` | Sharp QM1D1C0042 tuner |
| `qt1010` | Quantek QT1010 silicon tuner |
| `r820t` | Rafael Micro R820T silicon tuner |
| `rt2400pci` | Ralink rt2400 (PCI/PCMCIA) support |
| `rt2500pci` | Ralink rt2500 (PCI/PCMCIA) support |
| `rt61pci` | Ralink rt2501/rt61 (PCI/PCMCIA) support |
| `rtl2830` | Realtek RTL2830 DVB-T |
| `rtl2832` | Realtek RTL2832 DVB-T |
| `rtl2832_sdr` | Realtek RTL2832 SDR |
| `rtl818x_pci` | Realtek 8180/8185/8187SE PCI support |
| `s5h1409` | Samsung S5H1409 based |
| `s5h1411` | Samsung S5H1411 based |
| `s5h1420` | Samsung S5H1420 based |
| `s921` | Sharp S921 frontend |
| `si2157` | Silicon Labs Si2157 silicon tuner |
| `si2165` | Silicon Labs si2165 based |
| `si2168` | Silicon Labs Si2168 |
| `si21xx` | Silicon Labs SI21XX based |
| `sp2` | CIMaX SP2 |
| `sp887x` | Spase sp887x based |
| `stb0899` | STB0899 based |
| `stb6000` | ST STB6000 silicon tuner |
| `stb6100` | STB6100 based tuners |
| `stv0288` | ST STV0288 based |
| `stv0297` | ST STV0297 based |
| `stv0299` | ST STV0299 based |
| `stv0367` | ST STV0367 based |
| `stv0900` | ST STV0900 based |
| `stv090x` | STV0900/STV0903(A/B) based |
| `stv0910` | STV0910 based |
| `stv6110` | ST STV6110 silicon tuner |
| `stv6110x` | STV6110/(A) based tuners |
| `stv6111` | STV6111 based tuners |
| `sundance` | Sundance Alta support |
| `tc90522` | Toshiba TC90522 |
| `tda10021` | Philips TDA10021 based |
| `tda10023` | Philips TDA10023 based |
| `tda10048` | Philips TDA10048HN based |
| `tda1004x` | Philips TDA10045H/TDA10046H based |
| `tda10071` | NXP TDA10071 |
| `tda10086` | Philips TDA10086 based |
| `tda18212` | NXP TDA18212 silicon tuner |
| `tda18218` | NXP TDA18218 silicon tuner |
| `tda18250` | NXP TDA18250 silicon tuner |
| `tda18271` | NXP TDA18271 silicon tuner |
| `tda18271c2dd` | NXP TDA18271C2 silicon tuner |
| `tda665x` | TDA665x tuner |
| `tda8083` | Philips TDA8083 based |
| `tda8261` | Philips TDA8261 based |
| `tda826x` | Philips TDA826X silicon tuner |
| `tda827x` | Philips TDA827X silicon tuner |
| `tda8290` | TDA 8290/8295 + 8275(a)/18271 tuner combo |
| `tda9887` | TDA 9885/6/7 analog IF demodulator |
| `tea5761` | TEA 5761 radio tuner |
| `tea5767` | TEA 5767 radio tuner |
| `ts2020` | Montage Tehnology TS2020 based tuners |
| `tua6100` | Infineon TUA6100 PLL |
| `tua9001` | Infineon TUA9001 silicon tuner |
| `tuner-simple` |  |
| `tuner-types` | Simple tuner support |
| `ves1820` | VLSI VES1820 based |
| `ves1x93` | VLSI VES1893 or VES1993 based |
| `wl1251` | TI wl1251 driver support |
| `wl1251_sdio` | TI wl1251 SDIO support |
| `xc4000` | Xceive XC4000 silicon tuner |
| `xc5000` | Xceive XC5000 silicon tuner |
| `zl10036` | Zarlink ZL10036 silicon tuner |
| `zl10039` | Zarlink ZL10039 silicon tuner |
| `zl10353` | Zarlink ZL10353 based |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/module_deprecations_aarch64.html -->

## B Module Deprecations (aarch64)

The following modules are deprecated in this release of UEK 8.
While these modules are available and operative in this release, they are planned for removal
and support isn't guaranteed in future UEK releases. Thus, these modules should not be used in
new UEK 8 deployments to avoid problems upgrading in the future.

Table B-1 Module Deprecations (aarch64)

| Module Name | Description |
| --- | --- |
| `a8293` | Allegro A8293 |
| `af9013` | Afatech AF9013 demodulator |
| `af9033` | Afatech AF9033 DVB-T demodulator |
| `as102_fe` |  |
| `ascot2e` | Sony Ascot2E tuner |
| `atbm8830` | AltoBeam ATBM8830/8831 DMB-TH demodulator |
| `ath10k_sdio` | Atheros ath10k SDIO support |
| `ath6kl_sdio` | Atheros ath6kl SDIO support |
| `au8522_common` |  |
| `au8522_decoder` | Auvitek AU8522 based ATV demod |
| `au8522_dig` | Auvitek AU8522 based DTV demod |
| `b2c2-flexcop` |  |
| `b2c2-flexcop-pci` | Technisat/B2C2 Air/Sky/Cable2PC PCI |
| `b43legacy` | Broadcom 43xx-legacy wireless support (mac80211 stack) |
| `bcm3510` | Broadcom BCM3510 |
| `cw1200_wlan_sdio` | Support SDIO platforms |
| `cw1200_wlan_spi` | Support SPI platforms |
| `cx22700` | Conexant CX22700 based |
| `cx22702` | Conexant cx22702 demodulator (OFDM) |
| `cx23885` | Conexant cx23885 (2388x successor) support |
| `cx24110` | Conexant CX24110 based |
| `cx24113` | Conexant CX24113/CX24128 tuner for DVB-S/DSS |
| `cx24116` | Conexant CX24116 based |
| `cx24117` | Conexant CX24117 based |
| `cx24120` | Conexant CX24120 based |
| `cx24123` | Conexant CX24123 based |
| `cxd2099` | Sony CXD2099AR Common Interface driver |
| `cxd2820r` | Sony CXD2820R |
| `cxd2841er` | Sony CXD2841ER |
| `dib0070` | DiBcom DiB0070 silicon base-band tuner |
| `dib0090` | DiBcom DiB0090 silicon base-band tuner |
| `dib3000mb` | DiBcom 3000M-B |
| `dib3000mc` | DiBcom 3000P/M-C |
| `dib7000m` | DiBcom 7000MA/MB/PA/PB/MC |
| `dib7000p` | DiBcom 7000PC |
| `dib8000` | DiBcom 8000MB/MC |
| `dibx000_common` | DiBcom 9000 |
| `drx39xyj` | Micronas DRX-J demodulator |
| `drxd` | Micronas DRXD driver |
| `drxk` | Micronas DRXK based |
| `ds3000` | Montage Tehnology DS3000 based |
| `dvb-pll` | Generic I2C PLL based tuners |
| `dvb-usb` | Support for various USB DVB devices |
| `dvb-usb-a800` | AVerMedia AverTV DVB-T USB 2.0 (A800) |
| `dvb-usb-af9005` | Afatech AF9005 DVB-T USB1.1 support |
| `dvb-usb-af9005-remote` | Afatech AF9005 default remote control support |
| `dvb-usb-af9015` | Afatech AF9015 DVB-T USB2.0 support |
| `dvb-usb-af9035` | Afatech AF9035 DVB-T USB2.0 support |
| `dvb-usb-anysee` | Anysee DVB-T/C USB2.0 support |
| `dvb-usb-au6610` | Alcor Micro AU6610 USB2.0 support |
| `dvb-usb-az6007` | AzureWave 6007 and clones DVB-T/C USB2.0 support |
| `dvb-usb-az6027` | Azurewave DVB-S/S2 USB2.0 AZ6027 support |
| `dvb-usb-ce6230` | Intel CE6230 DVB-T USB2.0 support |
| `dvb-usb-cinergyT2` | Terratec CinergyT2/qanu USB 2.0 DVB-T receiver |
| `dvb-usb-cxusb` | Conexant USB2.0 hybrid reference design support |
| `dvb-usb-dib0700` | DiBcom DiB0700 USB DVB devices (see help for supported devices) |
| `dvb-usb-dibusb-common` | DiBcom USB DVB-T devices (based on the DiB3000M-B) (see help for device list) |
| `dvb-usb-dibusb-mb` | DiBcom USB DVB-T devices (based on the DiB3000M-B) (see help for device list) |
| `dvb-usb-dibusb-mc` | DiBcom USB DVB-T devices (based on the DiB3000M-C/P) (see help for device list) |
| `dvb-usb-dibusb-mc-common` |  |
| `dvb-usb-digitv` | Nebula Electronics uDigiTV DVB-T USB2.0 support |
| `dvb-usb-dtt200u` | WideView WT-200U and WT-220U (pen) DVB-T USB2.0 support (Yakumo/Hama/Typhoon/Yuan) |
| `dvb-usb-dtv5100` | AME DTV-5100 USB2.0 DVB-T support |
| `dvb-usb-dvbsky` | DVBSky USB support |
| `dvb-usb-dw2102` | DvbWorld & TeVii DVB-S/S2 USB2.0 support |
| `dvb-usb-ec168` | E3C EC168 DVB-T USB2.0 support |
| `dvb-usb-gl861` | Genesys Logic GL861 USB2.0 support |
| `dvb-usb-gp8psk` | GENPIX 8PSK->USB module support |
| `dvb-usb-lmedm04` | LME DM04/QQBOX DVB-S USB2.0 support |
| `dvb-usb-m920x` | Uli m920x DVB-T USB2.0 support |
| `dvb-usb-mxl111sf` |  |
| `dvb-usb-nova-t-usb2` | Hauppauge WinTV-NOVA-T usb2 DVB-T USB2.0 support |
| `dvb-usb-opera` | Opera1 DVB-S USB2.0 receiver |
| `dvb-usb-pctv452e` | Pinnacle PCTV HDTV Pro USB device/TT Connect S2-3600 |
| `dvb-usb-rtl28xxu` | Realtek RTL28xxU DVB USB support |
| `dvb-usb-technisat-usb2` | Technisat DVB-S/S2 USB2.0 support |
| `dvb-usb-ttusb2` | Pinnacle 400e DVB-S USB2.0 support |
| `dvb-usb-umt-010` | HanfTek UMT-010 DVB-T USB2.0 support |
| `dvb-usb-vp702x` | TwinhanDTV StarBox and clones DVB-S USB2.0 support |
| `dvb-usb-vp7045` | TwinhanDTV Alpha/MagicBoxII, DNTV tinyUSB2, Beetle USB2.0 support |
| `dvb_dummy_fe` | Dummy frontend driver |
| `dvb_usb_v2` | Support for various USB DVB devices v2 |
| `e4000` | Elonics E4000 silicon tuner |
| `ec100` | E3C EC100 |
| `fc0011` | Fitipower FC0011 silicon tuner |
| `fc0012` | Fitipower FC0012 silicon tuner |
| `fc0013` | Fitipower FC0013 silicon tuner |
| `fc2580` | FCI FC2580 silicon tuner |
| `gp8psk-fe` |  |
| `helene` | Sony HELENE Sat/Ter tuner (CXD2858ER) |
| `horus3a` | Sony Horus3A tuner |
| `isl6405` | ISL6405 SEC controller |
| `isl6421` | ISL6421 SEC controller |
| `isl6423` | ISL6423 SEC controller |
| `it913x` | ITE Tech IT913x silicon tuner |
| `itd1000` | Integrant ITD1000 Zero IF tuner for DVB-S/DSS |
| `ix2505v` | Sharp IX2505V silicon tuner |
| `l64781` | LSI L64781 |
| `lg2160` | LG Electronics LG216x based |
| `lgdt3305` | LG Electronics LGDT3304 and LGDT3305 based |
| `lgdt3306a` | LG Electronics LGDT3306A based |
| `lgdt330x` | LG Electronics LGDT3302/LGDT3303 based |
| `lgs8gxx` | Legend Silicon LGS8913/LGS8GL5/LGS8GXX DMB-TH demodulator |
| `libertas_sdio` | Marvell Libertas 8385/8686/8688 SDIO 802.11b/g cards |
| `lnbh25` | LNBH25 SEC controller |
| `lnbp21` | LNBP21/LNBH24 SEC controllers |
| `lnbp22` | LNBP22 SEC controllers |
| `m88ds3103` | Montage Technology M88DS3103 |
| `m88rs2000` | M88RS2000 DVB-S demodulator and tuner |
| `m88rs6000t` | Montage M88RS6000 internal tuner |
| `max2165` | Maxim MAX2165 silicon tuner |
| `mb86a16` | Fujitsu MB86A16 based |
| `mb86a20s` | Fujitsu mb86a20s |
| `mc44s803` | Freescale MC44S803 Low Power CMOS Broadband tuners |
| `mn88472` | Panasonic MN88472 |
| `mn88473` | Panasonic MN88473 |
| `mt2060` | Microtune MT2060 silicon IF tuner |
| `mt2063` | Microtune MT2063 silicon IF tuner |
| `mt20xx` | Microtune 2032 / 2050 tuners |
| `mt2131` | Microtune MT2131 silicon tuner |
| `mt2266` | Microtune MT2266 silicon tuner |
| `mt312` | Zarlink VP310/MT312/ZL10313 based |
| `mt352` | Zarlink MT352 based |
| `mxl111sf-tuner` | MxL111SF DTV USB2.0 support |
| `mxl5005s` | MaxLinear MSL5005S silicon tuner |
| `mxl5007t` | MaxLinear MxL5007T silicon tuner |
| `mxl5xx` | MaxLinear MxL5xx based tuner-demodulators |
| `mxl692` | MaxLinear MXL692 based |
| `nxt200x` | NxtWave Communications NXT2002/NXT2004 based |
| `nxt6000` | NxtWave Communications NXT6000 based |
| `or51132` | Oren OR51132 based |
| `or51211` | Oren OR51211 based |
| `pluto2` | Pluto2 cards |
| `qm1d1b0004` | Sharp QM1D1B0004 tuner |
| `qm1d1c0042` | Sharp QM1D1C0042 tuner |
| `qt1010` | Quantek QT1010 silicon tuner |
| `r820t` | Rafael Micro R820T silicon tuner |
| `rsi_sdio` | Redpine Signals SDIO bus support |
| `rt2400pci` | Ralink rt2400 (PCI/PCMCIA) support |
| `rt2500pci` | Ralink rt2500 (PCI/PCMCIA) support |
| `rt61pci` | Ralink rt2501/rt61 (PCI/PCMCIA) support |
| `rtl2830` | Realtek RTL2830 DVB-T |
| `rtl2832` | Realtek RTL2832 DVB-T |
| `rtl2832_sdr` | Realtek RTL2832 SDR |
| `rtl818x_pci` | Realtek 8180/8185/8187SE PCI support |
| `s5h1409` | Samsung S5H1409 based |
| `s5h1411` | Samsung S5H1411 based |
| `s5h1420` | Samsung S5H1420 based |
| `s921` | Sharp S921 frontend |
| `si2157` | Silicon Labs Si2157 silicon tuner |
| `si2165` | Silicon Labs si2165 based |
| `si2168` | Silicon Labs Si2168 |
| `si21xx` | Silicon Labs SI21XX based |
| `sp2` | CIMaX SP2 |
| `sp887x` | Spase sp887x based |
| `stb0899` | STB0899 based |
| `stb6000` | ST STB6000 silicon tuner |
| `stb6100` | STB6100 based tuners |
| `stv0288` | ST STV0288 based |
| `stv0297` | ST STV0297 based |
| `stv0299` | ST STV0299 based |
| `stv0367` | ST STV0367 based |
| `stv0900` | ST STV0900 based |
| `stv090x` | STV0900/STV0903(A/B) based |
| `stv0910` | STV0910 based |
| `stv6110` | ST STV6110 silicon tuner |
| `stv6110x` | STV6110/(A) based tuners |
| `stv6111` | STV6111 based tuners |
| `sundance` | Sundance Alta support |
| `tc90522` | Toshiba TC90522 |
| `tda10021` | Philips TDA10021 based |
| `tda10023` | Philips TDA10023 based |
| `tda10048` | Philips TDA10048HN based |
| `tda1004x` | Philips TDA10045H/TDA10046H based |
| `tda10071` | NXP TDA10071 |
| `tda10086` | Philips TDA10086 based |
| `tda18212` | NXP TDA18212 silicon tuner |
| `tda18218` | NXP TDA18218 silicon tuner |
| `tda18250` | NXP TDA18250 silicon tuner |
| `tda18271` | NXP TDA18271 silicon tuner |
| `tda18271c2dd` | NXP TDA18271C2 silicon tuner |
| `tda665x` | TDA665x tuner |
| `tda8083` | Philips TDA8083 based |
| `tda8261` | Philips TDA8261 based |
| `tda826x` | Philips TDA826X silicon tuner |
| `tda827x` | Philips TDA827X silicon tuner |
| `tda8290` | TDA 8290/8295 + 8275(a)/18271 tuner combo |
| `tda9887` | TDA 9885/6/7 analog IF demodulator |
| `tea5761` | TEA 5761 radio tuner |
| `tea5767` | TEA 5767 radio tuner |
| `ts2020` | Montage Tehnology TS2020 based tuners |
| `tua6100` | Infineon TUA6100 PLL |
| `tua9001` | Infineon TUA9001 silicon tuner |
| `tuner-simple` |  |
| `tuner-types` | Simple tuner support |
| `ves1820` | VLSI VES1820 based |
| `ves1x93` | VLSI VES1893 or VES1993 based |
| `wl1251` | TI wl1251 driver support |
| `wl1251_sdio` | TI wl1251 SDIO support |
| `wl1251_spi` | TI wl1251 SPI support |
| `wl12xx` | TI wl12xx support |
| `wl18xx` | TI wl18xx support |
| `wlcore` | TI wlcore support |
| `wlcore_sdio` | TI wlcore SDIO support |
| `wlcore_spi` | TI wlcore SPI support |
| `xc4000` | Xceive XC4000 silicon tuner |
| `xc5000` | Xceive XC5000 silicon tuner |
| `zd1301` | ZyDAS ZD1301 |
| `zd1301_demod` | ZyDAS ZD1301 |
| `zl10036` | Zarlink ZL10036 silicon tuner |
| `zl10039` | Zarlink ZL10039 silicon tuner |
| `zl10353` | Zarlink ZL10353 based |