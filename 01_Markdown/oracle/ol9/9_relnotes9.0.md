---
title: "Release Notes for Oracle Linux 9"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.0"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol9"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux 9

Release Notes for Oracle Linux 9

F51009-15

January 2026

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 9 Release Notes for Oracle Linux 9

F51009-15

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2022, 2026, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.0/ol9.0-Preface.html -->

## Preface

[Oracle Linux 9: Release Notes for Oracle Linux
9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.0/) provides information about the new features
and known issues in the Oracle Linux 9 release. The information applies to both x86\_64 and
64-bit Arm (aarch64) architectures. This document might be updated after it is released.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.0/ol9-AboutOracleLinux9.html -->

## 1 About Oracle Linux 9

The current Oracle Linux 9 release contains
new features and enhancements that improve performance in different areas including automation
and management, security and compliance, container management, and developer tools. These
enhancements are especially designed to make the OS adaptable to different types of deployment
such as on-premises installations, hybrid deployments that combine on-premises and cloud
installations, and full cloud deployment.

Important:

Upgrading from an Oracle Linux Developer Preview release to its later official version is
not supported. If you're running the Developer Preview version, you must reinstall the
official Oracle Linux release upon its general availability.

### System Requirements and Limitations

To check whether a specific hardware is supported on the current Oracle Linux 9 release, see
the Hardware Certification List at <https://linux.oracle.com/hardware-certifications>. Note that as hardware becomes
available and validated, the hardware is added to the list.

CPU, memory, disk and file system limits for all Oracle Linux releases are described in
[Oracle Linux: Limits](https://docs.oracle.com/en/operating-systems/oracle-linux/limits/).

### Available Architectures

The release is available for installation on the following
platforms:

- Intel® 64-bit (x86\_64) (x86-64-v2)
- AMD 64-bit (x86\_64) (x86-64-v2)
- 64-bit Arm (aarch64) (Arm v8.0-A)

  The Arm platform runs only with Unbreakable Enterprise Kernel Release (UEK).

### Shipped Kernels

For the x86\_64 platform, Oracle Linux 9 ships with the following default kernel packages:

- `kernel-5.14.0-70.13.1.el9_0`
  (Red Hat Compatible Kernel (RHCK))
- `kernel-uek-5.15.0-0.30.19.el9uek`
  (Unbreakable Enterprise Kernel Release 7 (UEK R7))

  For new installations, the UEK kernel is automatically
  enabled and installed. It also becomes the default kernel on
  first boot.

For the aarch64 platform, Oracle Linux ships with the UEK kernel only.

The Oracle Linux release is tested as a bundle, as shipped on the
installation media image. When installed from the installation
media image, the kernel's version included in the image is the
minimum version that is supported. Downgrading kernel packages
is not supported, unless recommended by Oracle Support.

For more information about kernel availability on Oracle Linux 9 releases, see <https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/oracle_linux9_kernel_version_matrix.html>.

### About the Unbreakable Enterprise Kernel

The Unbreakable Enterprise Kernel (UEK) is a Linux kernel built by Oracle and supported
through Oracle Linux support. UEK is tested on Arm (aarch64), Intel® x86, and AMD x86 (x86\_64)
platforms. Each release contains added features, bug fixes, and updated drivers to provide
support for key functional requirements, improve performance, and optimize the kernel for use
on Oracle products such as Oracle's Engineered Systems, Oracle Cloud Infrastructure, and large enterprise deployments for Oracle customers.

Typically, a UEK release contains changes to the kernel ABI relative to a previous UEK
release. These changes require recompilation of third-party kernel modules on the system. To
minimize impact on interoperability during releases, the Oracle Linux team works with
third-party vendors regarding hardware and software that have dependencies on kernel modules.
Thus, before installing the latest UEK release, verify its support status with the application
vendor.

The kernel ABI for a UEK release remains unchanged in all later updates to the initial
release.

The kernel source code for UEK is available after the initial release through a public git
source code repository at <https://github.com/oracle/linux-uek>.

For more information about UEK such as tutorials, notices, and
release notes of different UEK versions, go to
[Unbreakable Enterprise Kernel documentation](https://docs.oracle.com/en/operating-systems/uek/).

### User Space Compatibility

Oracle Linux maintains user space compatibility with Red Hat Enterprise Linux (RHEL) that's
independent of the kernel version that underlies the OS. Existing applications in user space
continue to run unmodified on UEK with no required recertifications for Oracle Linux certified
applications.

### Obtaining Installation Images

The following installation images for the current Oracle Linux 9 release are available:

- Full ISO of Oracle Linux for typical on-premises installations
- Boot ISO of Oracle Linux for network installations
- Boot ISO of the official UEK release for installing on hardware which is supported only
  on UEK
- Source DVDs

You can download these images from the following locations. Note
that the images in these locations are for both the x86\_64 and
aarch64 platforms, unless indicated otherwise:

- Oracle Linux yum server at <https://yum.oracle.com/oracle-linux-downloads.html>

  For more information managing and updating software on Oracle Linux systems, see [Oracle Linux: Managing Software on Oracle
  Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).
- Oracle Software Delivery Cloud at <https://edelivery.oracle.com>

To prepare a downloaded image for installing Oracle Linux, see [Oracle Linux 9: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/9/install/).

Note:

Aside from installation ISO images, you can also use Oracle Linux images to create compute
instances on Oracle Cloud Infrastructure. For information about these images, see
the release notes for the specific image that you're using on the [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/images/) page.

To use Oracle Linux on Oracle Cloud Infrastructure, see <https://docs.oracle.com/iaas/oracle-linux/home.htm>.

For information about the available ISO images for the three most recent updates to the Oracle
Linux releases, see <https://yum.oracle.com/oracle-linux-isos.html>.

### Upgrading From Previous Oracle Linux Releases

You can upgrade an Oracle Linux 8 system to the Oracle Linux 9 release by using
the `leapp` utility.

For step-by-step instructions and information about any known issues that might arise when
upgrading the system, see [Oracle Linux 9: Upgrading Systems With Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/9/leapp/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.0/ol9-NewFeaturesandChanges.html -->

## 2 New Features and Changes

Unless indicated otherwise, the following new features, major enhancements, bug fixes, and
other changes that are introduced in this release of Oracle Linux 9 apply to both the x86\_64
and 64-bit Arm (aarch64) platforms.

### Installation and Boot

The following features, enhancements, and changes related to installation and boot are
introduced in this release of Oracle Linux 9.

#### Graphical Installation Program Activates the Network Automatically During Interactive Installations

In the interactive installation mode that uses the graphical user interface, the network
is automatically enabled. Manually activating the network is no longer required.

Note that this change does not impact the kickstart installations and installations that
use the `ip=` boot option.

#### Licensing and User Setting Configuration Screens No Longer Part of Post Installation

Initial setup screens for licensing and for configuring users that previously appeared as
post installation steps are now disabled. To restore these screens, run the following
commands which install and enable the relevant packages, and then reboot the system. The
initial setup screens appear when the boot up system is completed.

```
sudo dnf install initial-setup initial-setup-gui -y
systemctl enable initial setup
reboot
```

For kickstart installations, add and enable these packages as follows:

```
firstboot --enable
%packages
@^graphical-server-environment
initial-setup-gui
%end
```

#### Root Account Is Locked by Default

As an added security feature, the root account in an Oracle Linux 9 installation is locked
by default. However, the installation program provides options for you to enable SSH root
logins with appropriately set passwords during the installation. For instructions, see [Oracle Linux 9: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/9/install/).

#### Kickstart Changes Have Been Implemented

The following changes in Oracle Linux 9 affect how you configure automatic installations
that use kickstart:

- All boot options must use the `inst` prefix; otherwise, those options
  are ignored. Add the prefix to previously configured standalone options to maintain
  their functionality.
- The new `timesource` command replaces the previous
  `timezone --ntpservers` command, which has been deprecated.
- The following kickstart commands and options are removed and generate errors if used:

  - `device`
  - `deviceprobe`
  - `dmraid`
  - `install`

    Instead, use the subcommands or methods directly as commands.
  - `multipath`
  - `bootloader --upgrade`
  - `ignoredisk --interactive`
  - `partition --active`
  - `harddrive --biospart`
  - `autostep`

#### Changes to Boot Options Implemented

The following changes were applied to some boot options:

- `inst.zram` and `inst.singlelang` options are not
  supported in Oracle Linux 9.
- `inst.loglevel` is always set to debug. Other log levels in previous
  Oracle Linux releases have been removed.

### Kernel and System Libraries

The following notable features, enhancements, and changes apply to the Red Hat Compatible
Kernel (RHCK) that's shipped with the current Oracle Linux 9 version.

#### RHCK Kernel Signed With Trusted Secure Boot Certificates

This feature eliminates the need to enroll a separate public key to use the kernel
versions on systems that have UEFI Secure Boot enabled. Previous releases required you to
enroll a separate public key by using the Machine Owner Key (MOK) facility.

#### Control Group Version 2 Enabled by Default

Version 2 of the control groups (`cgroup-v2`) is enabled together with
version 1 (`cgroup-v1`).

`cgroup-v2` implements a single hierarchy model to simplify the management
of control groups. The model ensures that a process can only be a member of a single control
group at a time. The feature is integrated with `systemd` and improves
resource control configuration on an Oracle Linux system.

Note that feature incompatibilities exist between `cgroup-v2` and
`cgroup-v1`. Moreover, control interfaces are different between the two
versions. Consequently, third-party software that has a direct dependency on
`cgroup-v1` might not run properly in the `cgroup-v2`
environment.

While both versions are enabled in the kernel, no default control group version is set in
the kernel. Instead, the version that mounts at startup is determined by
`systemd`.

To use `cgroup-v1`, add the following parameters to the kernel command
line:

```
systemd.unified_cgroup_hierarchy=0
systemd.legacy_systemd_cgroup_controller
```

#### Kernel Changes Might Affect Third-Party Kernel Modules

Linux distributions with a kernel version prior to 5.9 included support for exporting GPL
functions as non-GPL functions. This support enabled users to link proprietary functions to
GPL kernel functions by using the `shim` mechanism. In this release,
upstream changes have been incorporated into the kernel that enable Oracle Linux to enforce
GPL more strictly. Accordingly, `shim` is now rebuffed.

Important:

Partners and independent software vendors (ISVs) should test their kernel modules with
an early version of Oracle Linux 9 to ensure compliance with GPL.

#### Fixes to `strace` Utility

In this release, the `strace` utility correctly displays SELinux context
mismatches through the extension of the utilities `--secontext` option. This
extension is the `mismatch` parameter. See the following example:

```
[...]
$ strace --secontext=full,mismatch -e statx stat /home/user/file
statx(AT_FDCWD, "/home/user/file" [system_u:object_r:user_home_t:s0!!unconfined_u:object_r:user_home_t:s0], ...

$ strace --secontext=mismatch -e statx stat /home/user/file
statx(AT_FDCWD, "/home/user/file" [user_home_t:s0], ...
```

#### `perf-top` Capable of Sorting by a Specific Column

The `perf-top` system profiling tool can sort samples by an arbitrary
event column instead of just the first column when multiple events in the group are sampled.
Samples are sorted through the `--group-sort-idx` option, where you press a
number key to sort the table by the data column that corresponds to that key. Column
numbering starts from `0`.

#### New Jigawatts Package Added

The new `jigawatts` package includes a Java library that works to improve
the functionality of the Checkpoint/Restore in Userspace (CRIU) utility specifically on Java
applications.

#### `trace-cmd reset` Behavior Change

Instead of disabling, `trace-cmd reset` now resets settings of the
`ftrace` framework to their default values. This behavior specifically
affects `tracing_on`, `trace_clock`,
`set_event_pid`, and `tracing_max_latency`.

#### Support for Extended Berkeley Packet Filter

The Extended Berkeley Packet Filter (eBPF) is an in-kernel virtual machine that enables
code execution in the kernel space in a restricted sandbox environment with access to a
limited set of functions. The virtual machine executes a special assembly-like code.

#### Crash Utility 8.0.0

This version of the utility has a new `offset` parameter in the
`add-symbol-file` command that helps to set the
`kaslr-offset` to `gdb`. The parameter also upgrades
`gdb-7.6` to `gdb-10.2`.

#### Changes Implemented on `makedumpfile` Utility

The following enhancements and improvements are in the utility:

- Support for the Zstandard compression capability

  The utility is thus able to take advantage of `zstd`'s high compression
  ratios which improve compression efficiency especially in large memory systems. The
  improved compression mechanism creates a smaller `vmcore` file within a
  reasonable compression time.
- New options improve ways to obtain an estimate of the vmcore size

  The following options can be used with the `makedump` command:

  - `--dry-run` performs all operations specified by the command without
    writing the output file.
  - `--show-stats` prints the report messages. This option is an
    alternative to enabling bit 4 that is provided to the
    `--message-level` option.

    The following shows an example in the use of these options:

    ```
    sudo makedumpfile --dry-run --show-stats -l --message-level 7 -d 31 /proc/kcore dump.dummy
    ```

#### Support for `numatop` Utility for Intel Xeon Scalable Processors

`numatop` monitors and analyzes threads and processes running on Numa
systems. It uses Intel performance counter sampling technologies and associates the
performance data with Linux system `runtime` information for better analysis
of Numa systems deployed in production.

#### New `crashkernel.default` File for `kdump` Memory Allocation

In the `kexec-tools` package, the new `crashkernel.default`
file for `kdump` contains a default crash kernel value for the corresponding
kernel build. `kdump` uses the value to control the default crash kernel
memory value of each kernel.

`crashkernel.default` serves as a good reference for `kdump`
memory reservation. By basing on this value, you can configure the desired setting for
`crashkernel=`. Consequently, memory allocation for `kdump`
is improved for systems that have less than 4 GB of available memory.

To query the default crashkernel value, type:

```
sudo kdumpctl get-default-crashkernel
```

For more details, refer to the
`/usr/share/doc/kexec-tools/crashkernel-howto.txt` file.

#### Core Scheduling Functionality Added

The core scheduling functionality enables you to define groups of tasks that can share a
CPU core, and thereby exclude tasks that should not trust each other from sharing the same
resource. This feature enhances security by mitigating some cross-Symmetric Multithreading
(SMT) attacks. It also isolates tasks that need a whole core, such as those that are
performed in real-time environments or those that rely on specific processor features, such
as Single Instruction, Multiple Data (SIMD) processing.

#### CPU Hot-Plug in `hv_24x7` and `hv_gpci` PMUs

PMU counters can correctly react to the hot plugging of a CPU, such that if an
`hv_gpci` event counter is running on a CPU that becomes disabled, the
counting redirects to another CPU.

#### IRDMA Driver Added

The IRDMA driver enables RDMA functionality on the following RDMA-capable Intel network
devices:

- Ethernet Network Adapter X722: an Internet Wide-area RDMA Protocol (iWARP) device.

  This device supports only iWARP and a more limited set of configuration parameters.
- Ethernet Controller E810: a device that supports iWARP and RDMA over Converged
  Ethernet (RoCEv2)

  This device iWARP and RoCEv2 RDMA transports, Priority Flow Control (PFC), and
  Explicit Congestion Notification (ECN).

The IRDMA module replaces as well as extends the Application Binary Interface (ABI)
defined for the legacy i40iw module for X722. The change is backward compatible with legacy
X722 RDMA-Core provider (`libi40iw`).

#### `aarch64`: Default Page Size on Arm Platform Changed to 4 KB

Based on UEK R7 implementation, the default page size on the 64-bit Arm platform has
changed from 64 KB to 4 KB. This new size pairs well with the workloads and memory amounts
that exist on the majority of Arm-based systems. To use large page sizes efficiently, ensure
that you specify the huge pages option, which addresses a greater amount of memory for
workloads with large data sets.

#### `aarch64`: `kexec_file_load` Enabled by Default

For systems using the 64-bit Arm architecture, the added `kexec_file_load`
system call provides an in-kernel `kexec` loader for `kdump`
which enables an unsigned kernel to work correctly. Prior to this update, an unsigned kernel
failed to load with secure boot enabled and `kexec_file_load()` specified.

#### `aarch64`: Armv8-R Architecture Supported

The architecture is supported through the `-march=armv8-r` option of the
improved GCC 11.2.1.

### Operating System and Software Management

The following features, enhancements, and changes related to the OS and software management
are introduced in this Oracle Linux 9 release.

#### RPM Updated to Version 4.16

The updated version includes notable changes such as the following:

- Support for new SPEC features such as caret version operator,
  `%autopatch` for specifying patch ranges, meta or unordered
  dependencies, generation of dynamic build dependencies through the
  `%generate_buildrequires` section, and so on.
- RPM is fully based on the sqlite library. For Berkeley DB databases, Read-only support
  is provided.
- `rpm-audit-plugin` is a new plugin for recording audit log events on
  transactions.
- Validation of UTF-8 headers is performed at build time.
- Increased parallelism is applied in package builds.

#### New RPM Plugin Notifies `fapolicyd` About Changes During RPM Transactions

Updated `rpm` packages include a new RPM plugin that integrates the
`fapolicyd` framework with the RPM database. By informing
`fapolicyd` about any installed and changed files during an RPM
transaction, the plugin enables `fapolicyd` to support integrity checking.
The plugin's functionality extends its coverage beyond just Yum transactions to changes made
by RPM as a whole. Thus, the plugin is effectively a replacement to the Yum plugin.

#### Support for Signing Keys Using EdDSA Public Key Algorithm

This added support to the `rpm` command enables you to use
EdDSA-generated keys for signing and verifying packages. However, RSA continues to be the
default public key algorithm in GnuPG.

#### RPM Supports ZSTD Algorithm

RPM supports the Zstandard (`zstd`) compression algorithm, which makes
package installations faster, especially in large transactions. Oracle Linux 9 uses
Zstandard as the default compression algorithm.

#### New Options Available for DNF

The following are new DNF options:

- `exclude_from_weak_autodetect` automatically detects unwanted weak
  dependencies of packages being installed. Thus, providers of the weak dependencies are
  not installed as weak dependencies. However, if pulled in, these weak dependencies are
  installed as regular dependencies. The option is enabled by default.
- `exclude_from_weak` prevents the installation of packages as weak
  dependencies.

#### `libmodulemd` Packages Updated to Version 2.13.0

This version of `libmodulemd` packages includes the following features and
changes:

- Support for delisting demodularized packages from a module.
- Support for validating `modulemd-packager-v3` documents by using
  `modulemd-validator --type`, where `--type` is a new
  option.
- Fortified parsing integers.

### Shells and Command Line Tools

The following features, enhancements, and changes related to shells and command line tools
are introduced in this Oracle Linux 9 release.

#### `bash` Library Version 8.1

In this library, bracketed paste mode is enabled by default. This mode causes text that
you paste on your terminal to be highlighted and requires you to press Enter to execute the
command in the text. This feature prevents you from executing malicious commands.

To disable the feature, add the following line to either `$HOME/.inputrc` or
`/etc/inputrc`:

```
set enable-bracketed-paste off
```

- If added to `$HOME/.inputrc`, the feature is disabled for a specific user.
- If added to `/etc/inputrc`, the feature is disabled for all users.

Disabling the feature causes pasted commands on the terminal to be immediately executed.

#### Additional Shell Related Packages Available With Updated Versions

- `opal-prd 6.7.1`
- `lvspd 1.7.12`
- `Fetchmail 6.4.24`
- `Eigen 3.4`

#### New `cdrskin` Package Introduced

The package replaces the `cdrecord` executable. However, the
`cdrskin` package includes the `cdrecord` command as a
symbolic link to the `cdrskin` binary so that existing user scripts need not
be revised.

#### `util-linux-core` Added as a Package

The `util-linux-core` is added as a subpackage to the
`util-linux` package to manage scenarios where the size of installed
package is a critical issue, such as in buildroots, some containers, and boot images.

However, for standard installations, install the `util-linux` package,
which automatically includes the `util-linux-core` package.

### Compilers and Development Tools

The following features, enhancements, and changes related to compilers and development tools
are introduced in this Oracle Linux 9 release.

#### Summary List of Tools and Compilers and Their Latest Versions

- System toolchain components

  - GCC 11.2.1
  - glibc 2.34
  - binutils 2.35.2
- Performance tools and debuggers

  - GDB 10.2
  - Valgrind 3.18.1
  - SystemTap 4.6
  - Dyninst 11.0.0
  - elfutils 0.186
- Performance monitoring tools

  - PCP 5.3.5
  - Grafana 7.5.11
- Compiler toolsets

  - LLVM Toolset 13.0.1
  - Rust Toolset 1.58.1
  - Go Toolset 1.17.7
- `python-jsonpointer` is rebased to
  version 2.0
- `grafana-pcp` is rebased to 3.2.0

#### GCC Updated to Version 11.2

This version includes notable changes such as the following:

- DWARF Version 5 is used as the default debugging format.
- Diagnostics column numbers represent real column numbers by default and recognizes
  multicolumn numbers.
- The straight-line code vectorizer considers the whole function when vectorizing.
- A series of conditional expressions that compare the same variable can be transformed
  into a switch statement if each of them contains a comparison expression.
- Procedural optimizations have been implemented through a new IPS-modref pass which
  tracks side effects of function calls and improves the precision of points-to analysis,
  and the identical code folding pass, which is improved to increase the number of unified
  functions and reduce compile-time memory use.
- Memory allocation during linking is improved to reduce peak memory use.
- Through the new `GCC_EXTRA_DIAGNOSTIC_OUTPUT` environment variable in
  IDEs, you can request machine-readable "fix-it-hints" without adjusting build flags.

#### Go Toolset Updated to Version 1.17.7

This version includes notable changes such as the following:

- The `GO111MODULE` environment variable is set to `on` by
  default. To revert this setting, set the variable to `auto`.
- The Go linker uses less resources and improves code robustness and maintainability in
  all supported CPU architectures and operating systems.
- The new `embed` package enables you to access embedded files while
  compiling.
- All functions of the `io/ioutil` package have been moved to the
  `io` and `os` packages, both of which provide better
  definitions.
- The Delve debugger 1.6.0 supports Go Toolset 1.16.6.

#### Go FIPS Mode Supported With OpenSSL 3

With this support, you can use the OpenSSL library while on Go FIPS mode.

#### Rust Toolset Updated to Version 1.54.0

This version includes notable changes such as the following:

- The Rust standard library is available for the `wasm32-unknown-unknown`
  target and enables you to generate WebAssembly binaries, including newly stabilized
  intrinsics.
- You can use constant-value parameters to define generics. This change enables you to
  write functions completely generic over the values of any integer, boolean, or character
  type, and arrays generic over their element type as well as their length. Additionally,
  you can also iterate items from an array by value by using the new standard libraryâs
  array type API `std::array::IntoIter`.
- Rust includes the `IntoIterator` implementation for arrays. Use the
  `IntoIterator` trait to iterate over arrays by value and pass arrays to
  methods. However, `array.into_iter()` still iterates values by reference
  until the 2021 edition of Rust.
- The syntax for `or` patterns allows nesting anywhere in the pattern,
  for example: `Pattern(1|2)` instead of
  `Pattern(1)|Pattern(2)`.
- Unicode identifiers can contain all valid identifier characters as defined in the
  Unicode Standard Annex #31.
- Methods and trait implementations have been stabilized.

#### LLVM Toolset Updated to Version 12.0.1

This version includes notable changes such as the following:

- New compiler flag `-march=x86-64-v[234]` introduced.
- Compiler flag `-fasynchronous-unwind-tables` of the
  `clang` compiler is the default on Oracle Linux aarch64 systems in this
  release.
- The `clang` compiler supports the C++20 `[[likely]]` and
  `[[unlikely]]` attributes.
- With the newly added function attribute `tune-cpu`, microarchitectural
  optimizations can be applied independently from the `target-cpu`
  attribute or TargetMachine CPU.
- The `-fsanitize=unsigned-shift-base` sanitizer is added to the integer
  sanitizer `-fsanitizer=integer` to improve security.
- The WebAssembly backend is now enabled in LLVM. when enables you to generate
  WebAssembly binaries with LLVM and Clang.

#### CMake Updated to Version 3.20.2

This version includes notable changes such as the following:

- C++ compiler modes can be specified through the target properties
  `CXX_STANDARD`, `CUDA_STANDARD`, and
  `OBJCXX_STANDARD` or, alternatively, the `cxx_std_23`
  metafeature of the compile features section.
- The NVIDIA CUDA compiler as a symbolic link is supported.
- The Intel oneAPI NextGen LLVM compilers are supported with the
  `IntelLLVM` compiler ID.
- CMake now facilitates cross compiling for Android by merging with the Android NDKâs
  toolchain file.
- When generating a project build system, the `cmake` command
  rejects unknown arguments that start with a hyphen.

To use CMake on projects that require this or an earlier version, use the command
`cmake_minimum_required (version 3.20.2)`.

#### Java in Oracle Linux 9

In this release, Java includes the following packages:

- `java-17-openjdk`
- `java-11-openjdk`
- `java-1.8.0-openjdk`

#### Java Tools Implementation

In this release, Java tools include the following:

- `Maven 6.3.6`
- `Ant 1.10.9`

You can install these tools as non modular RPM packages from AppStream.

#### SWIG 4.0 Available in CodeReady Builder Repository

Version 4.0 of Simplified Wrapper and Interface Generator (SWIG), which includes support
for PHP 8, can be installed as an RPM package from the CRB repository.

#### `pcp` Updated to Version 5.3.5

The Performance Co-Pilot (PCP) package (`pcp`) includes bug fixes,
enhancements, and new features, including the following:

- Large number of hosts can have performance metrics centrally logged
  (`pmlogger` farms) and automatically monitored with performance rules
  (`pmie` farms).
- New `pcp-ss` tool for historical socket statistics is supported.
- `php-htop` tool is improved.
- Extensions have been added to the over-the-wire PCP protocol, which support higher
  resolution timestamps.

### Desktop

The following desktop features are included with Oracle Linux 9:

#### GNOME Desktop Environment Updated to Version 40

This version includes numerous new and improved features, including a redesigned
Activities Overview that provides for better navigation of the system and the launching of
applications. Note that workspaces are now arranged horizontally and the window overview, as
well as the application grid, are accessed vertically.

#### Pipewire as Default Audio Service

Pipewire replaces both the PulseAudio and Jack audio services that was used in previous
releases. All audio applications that use these earlier services are redirected to Pipewire.
Jack applications work well with default Oracle Linux configurations and therefore do not
require additional configurations.

#### Power Profiles in GNOME

Power profiles enable you to optimize power usage of your system. The selected profile
persists across system reboots. You can select from the following:

- `Performance` sets the system for peak performance but reduces battery
  life. The profile is not available in all system configurations.
- `Balanced` is the default profile which provides standard performance
  and power consumption.
- `Power Saver` prioritizes battery life and can impact system
  performance. The system switches to this profile automatically if low battery level is
  detected.

#### Boot Loader Changes

Configuration files are unified across CPU architectures. These files are stored in
`/boot/grub2`, regardless of the platform. The
`grub.cfg` file that GRUB previously used on UEFI systems is now a symbolic
link to `/boot/grub2/grub.cfg`. This change provides benefits, such as
improved user experience, simplified GRUB layout configuration, the ability to boot the same
installation with either EFI or legacy BIOS, and so on.

#### Langpacks Replaces `comps` Language Groups

Previously, language support was provided by `comps` language groups, which
required you to install the corresponding `code-support`
package. In this release, you would install the `langpacks-code` package instead.

#### Single Application GNOME Sessions Supported

This support enables users to use a lightweight UI for single applications. Also described
as the kiosk mode of a GNOME session, this feature displays a full-screen window only of the
application that you have configured. In this mode, use of resources is less intensive than
in a standard GNOME session.

### Dynamic Programming Languages, Web and Database Servers

The following features, enhancements, and changes related to programming languages, web
servers, and database servers are introduced in this Oracle Linux 9 release.

#### Python 3.9

Python 3.9 is the default version in Oracle Linux 9, and is also installed by default.
Python 3.9 will be supported for the entire Oracle Linux 9 life cycle. However, additional
versions of Python 3 are also distributed as RPM packages with a shorter life cycle through
the AppStream repository. These versions can be installed in parallel.

The `/usr/bin/python` command and other Python-related commands, such
as `pip`, are made available in an unversioned form and point to the
default Python 3.9 version.

Note:

Python 2 is excluded in Oracle Linux 9.

#### Node.js 16

The following are notable changes:

- The `V8` engine is updated to version 9.2.
- The `npm` package manager is updated to version 7.20.3.
- A new `Timers Promises` API that provides an alternative set of timer
  functions that return `Promise` objects is included.
- A new experimental `Web Streams` API is included.
- Node.js is compatible with OpenSSL version 3.0.

Node.js 16 is the initial version of this Application Stream. However, additional Node.js
versions will be provided as modules with a shorter life cycle in future minor releases of
Oracle Linux 9.

#### Ruby 3.0.3

The following are notable changes:

- Concurrency and parallelism features, such as Ractor and Fiber Scheduler.
- Static analysis features, such as the RBS language and the
  `Typeprof` utility,
- Pattern matching with the `case/in` expression is no longer
  experimental.
- The experimental one-line pattern matching feature is redesigned.
- The Find pattern is added as an experimental feature.

Ruby 3.0 is the initial version of this Application Stream. Additional versions of Ruby
will be provided as modules with a shorter life cycle in future minor releases of Oracle
Linux 9.

#### Perl 5.32

This version includes numerous enhancements and bug fixes, some of which are the
following:

- Support for Unicode 13.0
- Enhanced `qr` quote-like operator
- Alpha assertions and script runs no longer experimental
- Faster feature checks
- Ability to dump compiled patterns prior to optimization

Perl 5.32 is the initial version of this Application Stream. Additional versions of Perl
will be provided as modules with a shorter life cycle in future minor releases of Oracle
Linux 9.

#### PHP 8.0

This version includes numerous enhancements and bug fixes, some of which are the
following:

- New self-documented and order-independent named arguments so you can specify only
  required parameters
- New attributes for using structured metadata with PHP's native syntax
- New union types for using native union types in place of PHPDoc annotations for a
  combination of types. These types are validated at runtime.
- Error exception is consistently generated when parameter validation fails.
- Improved `Just-In-Time` compilation performance

PHP 8.0 is the initial version of this Application Stream. Additional versions of PHP will
be provided as modules with a shorter life cycle in future minor releases of Oracle Linux 9.

#### Git 2.31 and Git LFS 2.13

Git 2.31 includes numerous enhancements, some of which are the following:

- Status of sparse checkout is included in the output of `git
  status`.
- `git archive --add-file` includes untracked files in a snapshot
  from a tree-like identifier.
- `clone.remotedefaultname` enables you to customize nickname for a source
  remote repository.
- Maximum length of output file names is now configurable beyond the previous 64 byte
  limit.
- PCRE1 library no longer supported.

In addition, the Git Large File Storage (LFS) extension 2.13 includes numerous
enhancements, some of which are the following:

- SHA-256 repositories, as well as the `socks5h` protocol, are supported.
- The `git lfs install|uninstall` commands include a new
  `--worktree` option.
- The `git lfs migrate import` command includes a new
  `--above` option.

#### Subversion 1.14

Subversion 1.14 is the initial version of this Application Stream. Additional versions of
Subversion will be provided as modules with a shorter life cycle in future minor releases of
Oracle Linux 9.

#### Apache HTTP Server 2.4.51

The following are notable changes:

- Changes to the Apache HTTP Server Control Interface (`apachectl`)
  - In the `apachectl status` output,
    `systemctl` pager is disabled.
  - Instead of the previous behavior of issuing warnings, the
    `apachectl` fails if you include additional arguments to
    the command.
  - The `graceful-stop` subcommand returns immediately.
  - The `configtest` subcommand runs `httpd
    -t` without changing the SELinux context.
- The Apache eXtenSion tool (`apxs`) does not use or expose compiler
  optimization flags in the process of building the `httpd` package.
- The `mod_lua` Apache module is provided in a separate package.
- In the `mod_access_compat` module's deprecated `Allow`
  directive, the use of the comment character (`#`) generates a syntax
  error.
- Kernel thread IDs are directly used in error log messages for accuracy and
  conciseness.

Apache HTTP Server 2.4 is the initial version of this Application Stream, which you can
install easily as an RPM package.

#### `nginx` 1.20

The following are notable changes:

- Support for client SSL certificate validation using the Online Certificate Status
  Protocol (OCSP).
- Through the `min_free` parameter of the
  `proxy_cache_path` directive, the driver now supports cache clearing.
- A new `ngx_stream_set_module` module is introduced.
- New directives as well as directive variables are supported.
- Support for HTTP/2 is improved.

#### Varnish Cache 6.6

Varnish Cache 6.5, which is a high-performance HTTP reverse proxy, provides a number of
enhancements and bug fixes version 6.0 available.

Varnish Cache 6 is the initial version of this Application Stream.

#### Squid 5.2

Squid 5.2 is a high-performance proxy caching server for web clients. Squid 5.2 includes
support for FTP, Gopher, and HTTP data objects as well as the following additional features:

- Uses a received IP address immediately when request forwarding requires it.
- New directive have been introduced.
- `dns_v4_first` directive no longer included in this version.
- Uses the `CDN-Loop` header for loop detection in Content Delivery
  Networks (CDN).
- Internet Content Adaptation Protocol (ICAP) trailers introduced as a new feature to
  enable ICAP agents to reliably send message metadata after the message body.
- New configuration options are introduced to replace existing ones, such as
  `mark_client_packet` for `clientside_mark` and
  `shared_transient_entries_limit` for
  `collapsed_forwarding_shared_entries_limit`.

Squid 5.2 is the initial version of this Application Stream.

#### MySQL 8.0

Oracle Linux 9 includes MySQL version 8.0. MySQL 8.0 is the initial version of this
Application Stream.

For this software's documentation, see <https://dev.mysql.com/doc/relnotes/mysql/8.0/en/>

#### Redis 6.2

Among enhancements and fixes in this version, the most notable is that the paths of Redis
server configuration files are dedicated directories  `/etc/redis/redis.conf`
and `/etc/redis/sentinel.conf`. In Oracle Linux 8, these files were located
in `/etc/redis.conf` and `/etc/redis-sentinel.conf`.

Redis 6 is the initial version of this Application Stream. In future minor releases of
Oracle Linux 9, additional Redis versions will be provided as modules with a shorter life
cycle.

#### MariaDB

MariaDB is updated to version 10.5

#### PostgreSQL

PostgreSQL is updated to version 13.

### File Systems and Storage

The following features, enhancements, and changes related to file systems and storage are
introduced in this Oracle Linux 9 release.

#### XFS File System Includes New Features

The XFS file system supports two new options for the `mkfs.xfs` command:
`bigtime` that supports timestamps beyond the year 2038 and
`inobtcount` that reduces mount time on large file systems.

Caution:

These options are enabled by default. Consequently, in Oracle Linux 9, the
`mkfs.xfs` command creates an XFS file system that is unmountable
by previous kernels where these options are not supported. To disable these options, type
the `mkfs.xfs` command as follows:

```
mkfs.xfs -m bigtime=0,inobtcount=0
```

For more information about file systems in Oracle Linux, see [Oracle Linux 9: Performing File System
Administration](https://docs.oracle.com/en/operating-systems/oracle-linux/9/fsadmin/).

#### `ext4` File Systems Support Year 2038 or Later Timestamps

The ext4 file system supports timestamps beyond the year 2038. This feature is enabled
automatically and requires only that the file system size is not lower than the default 128
bytes size.

#### `exFAT` Support

The newly supported Extensible File Allocation Table (exFAT) file system enables you to
use this file system, which is typically used by default on flash memory.

### High Availability and Clusters

The following features, enhancements, and changes related to high availability are introduced
in this Oracle Linux 9 release.

#### Changed Default Setting of `resource-stickiness meta-attribute`

The change is in response to user preference that resources are not automatically moved in
the process of a cluster balancing operation. Only newly-created clusters are affected by
this change. The behavior does not change for existing clusters.

This new default value of `1` keeps the resources in place during
balancing. However, a possible consequence might be that newly added nodes become
resourceless and would require the administrator to manually intervene to allot resources to
the nodes. Both resource stickiness (`1`) and non-stickiness
(`0`) can produce unexpected behavior. However, user preference is to
implement stickiness for resources.

If you prefer the old behavior for your cluster, delete the
`resource-stickiness` entry from resource defaults.

#### New LVM Volume Group Flag for Controlling Autoactivation

The `setautoactivation` flag controls whether logical volumes that are
created from a volume group are automatically activated upon startup. When creating a volume
group to be managed by Pacemaker in a cluster, you can set this flag to `n`
by using the `vgcreate --setautoactivation n` command for the volume
group. Running this command prevents possible data corruption. If you have an existing
volume group that is used in a Pacemaker cluster, set the flag by using the
`vgchange --setautoactivation n` command.

#### New Options for `pcs resource status` and `pcs stonith status` Commands

The `pcs resource status` and the `pcs stonith
status` commands include support for the following new options:

- The `pcs resource status node=`
  node\_id and `pcs stonith status node=`
  node\_id options display the status of resources that are configured
  on a specific node.
- The `pcs resource status`
  resource\_id and `pcs stonith status`
  resource\_id  options display the status of a single resource.
- The `pcs resource status`
  tag\_id and `pcs stonith status`
  tag\_id  options display the status of all of the resources with a
  specified tag.

#### Reduced Output Display Option for `pcs resource safe-disable` Command

To print errors only in a report instead of including lengthy simulation results, you can
use the `--brief` option in some `pcs resource`
subcommands as follows:

- `pcs resource safe-disable --brief`
- `pcs resource disable --safe --brief`

The error report now always contains resource IDs of affected resources.

#### New `pcs` Command for Updating SCSI Fencing Device

The new `pcs stonith update-scsi-devices` command enables you to
update SCSI devices without causing a restart of other cluster resources. The `pcs
stonith update` command causes a restart of all of the resources that are
running on the same node that the stonith resource was running.

#### `fence_watchdog` Agent for Configuring Watchdog-Only SBD Setup

Use the new `fence_watchdog` agent to configure a watchdog-only SBD
setup. This setup enables cluster configurations where only some nodes use watchdog-only SBD
for fencing, while other nodes use other fencing types. Note that a cluster may only have a
single such device, and it must be named `watchdog`. Previous watchdog-only
SBD configurations had no such flexibility and required that all of the nodes in the cluster
use SBD.

#### Local Mode Version of `pcs` Cluster Setup Command Supported

The `--corosync-conf` option switches the pcs cluster setup command to
local mode. In this mode, the `pcs` command creates a
`corosync.conf` file and saves on the local node only without communicating
with any other node. You can thus create a `corosync.conf` file in a script
and handle that file by using a script.

#### Location Constraint Removed Following Resource Move

The `pcs resource move` command adds a constraint to the resource to
prevent it from running on its original node. By default, the location constraint is
automatically removed when the resource has been moved. The removal does not necessarily
move the resource back to the original node. Where resources can run at that point depends
on how your resources are initially configured. To move a resource and leave the resulting
constraint in place, use the `pcs resource move-with-constraint`
command.

#### `pcs` Command Accepts Promoted and Unpromoted Roles

The `pcs` command accepts the `Promoted` and
`Unpromoted` anywhere roles that are specified in Pacemaker configuration.
Note that these role names are the functional equivalent of the `Master` and
`Slave` Pacemaker roles that was used in previous releases. Also, these
role names are visible in configuration displays and help pages.

### Infrastructure Services

The following features, enhancements, and changes related to infrastructure services are
introduced in this Oracle Linux 9 release.

#### `chrony` Updated to Version 4.1

- This updated `chrony` package includes notable changes including the
  following:

  - Additional support for Network Time Security (NTS) authentication.
  - In Oracle Linux 9, Authenticated Network Time Protocol (NTP) sources are trusted
    over non-authenticated NTP sources. To restore the previous behavior, add the
    `autoselectmode ignore` argument to the
    `chrony.conf` file.
  - Removal of support for authentication with the following RIPEMD keys:
    `RMD128`, `RMD160`, `RMD256`,
    `RMD320`.
  - Removal of support for long non-standard MACs in NTPv4 packets. If you are using
    `chrony 2.x`
    `non-MD5/SHA1` keys, you will need to configure
    `chrony` by using the `version 3` option.

  The following differences exist between this release's version of
  `chrony` from the version in Oracle Linux 8:

  - The `seccomp` filter is enabled by default.

    The `-F Z` option is set in
    `/etc/sysconfig/chronyd`.
  - The `seccomp` filter conflicts with the
    `mailonchange` directive. If you set this directive in
    `/etc/chrony.conf`, then disable the filter by removing the
    `-F Z` setting.

### Networking

The following features, enhancements, and changes related to networking are introduced in
this Oracle Linux 9 release.

#### WireGuard Available in UEK

WireGuard is a Virtual Private Network (VPN) implementation with advanced security
features, but is also designed to be simple to use and can be a replacement for earlier
tunneling protocols. WireGuard has been in production support in the UEK release since UEK
R6U3 and continues to be a supported feature in Oracle Linux 9, with UEK R7. For more
details, see [Unbreakable Enterprise Kernel Release 7: Release
Notes (5.15.0-0.30)](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/) . To configure WireGuard, see
[Oracle Linux: Configuring Virtual Private Networks](https://docs.oracle.com/en/operating-systems/oracle-linux/vpn/).

Note, however, that in RHCK, WireGuard is available only as a Technology Preview. See
[Technology Preview](ol9-TechnologyPreview.html#ol9-features-techprev).

#### `diag` Modules Available With Kernel Image

The kernel image includes the following `diag` modules:

```
CONFIG_INET_DIAG
CONFIG_INET_RAW_DIAG
CONFIG_INET_TCP_DIAG
CONFIG_INET_UDP_DIAG
CONFIG_NETLINK_DIAG
CONFIG_PACKET_DIAG
CONFIG_UNIX_DIAG
```

Being part of the kernel, these modules no longer need to be dynamically loaded with the
`ss` command. The change facilitates debugging of networking issues
regardless of customer policy in the kernel modules.

#### Core and IPv4-related Networking Kernel Parameters Added To `sysctl`

For a list of these parameters and their descriptions, install the
`kernel-doc` package and refer to the following files:

- `/usr/share/doc/kernel-doc-version/Documentation/admin-guide/sysctl/net.rst`
- `/usr/share/doc/kernel-doc-version/Documentation/networking/ip-sysctl.rst`

#### `nmstate` API Uses More Inclusive Terminology

As part of an ongoing effort to make terms more inclusive, the term `slave`
term has been replaced with the term `port` in the `nmstate`
API.

#### NetworkManager Support for `queue_id` in a Bond Port

`NetworkManager` ports that are in a bond include support for the setting
the `queue_id` parameter.

For example, if `eth1` is a port of a bond interface, you can enable the
`queue_id` parameter for that bond port by using the following command:

```
sudo nmcli connection modify eth1 bond-port.queue-id 1
sudo nmcli connection up eth1
```

Note:

A
network interface that needs to use this option should configure it with multiple calls
until the appropriate priorities are set for all interfaces. For more information, see the
`/usr/share/docs/kernel-doc-_version/Documentation/networking/bonding.rst`
file, which is provided in the `kernel-docs` package.

#### RDMA Packages From Oracle

Oracle provides Remote Direct Memory Access (RDMA) packages for use with UEK R7 to enable
direct memory access between two systems that are connected by a network. For more details,
see [Unbreakable Enterprise Kernel Release 7: Release
Notes (5.15.0-0.30)](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/).

### Security

The following features, enhancements, and changes related to security are introduced in this
Oracle Linux 9 release.

#### System-Wide `crypto-policies` More Secure

System wide cryptographic policies are more secure through the disabling of older
cryptographic algorithms and increased minimum RSA key size. Using SHA-1 is restricted in
the `DEFAULT` crypto policy. With the exception of HMAC and DNSSec usage,
SHA-1 is not allowed in TLS, DTLS, SSH, IKEv2 and Kerberos protocols. As part of this
change, some algorithms have been disabled.

If you require that some of the disabled algorithms and ciphers be enabled, use policy
modifiers or customize the policy.

#### OpenSSL Version 3.0.1 Supported

This version contains enhancements and fixes such as new versioning schemes, support for
new algorithms, new HTTP(S) client that supports GET and POST, and many others. The
following are features related to OpenSSL:

- OpenSSL supports new concept of providers

  The OpenSSL 3.0.1 toolkit introduces the concept of providers, which are
  collections of algorithms from which you can choose for different applications. The
  following providers are provided: `base`, `default`,
  `FIPS`, `legacy`, and `null`.

  By default, OpenSSL loads and activates the default provider, which is comprised of
  commonly used algorithms such as RSA, DSA, DH, CAMELLIA, SHA-1, and SHA-2. If the FIPS
  flag is set in the kernel, the FIPS provider is automatically loaded, and no manual
  switching to FIPS mode is required. To change the provider on the system level, edit the
  `openssl.cnf` configuration file.

  Caution:

  Explicitly activating a provider overrides the default provider selection, which
  might make the system remotely inaccessible.
- OpenSSL random bit generator includes CPACF support

  The `openssl` packages provide support for the CP Assist for
  Cryptographic Functions (CPACF) in the OpenSSL NIST SP800-90A-compliant AES-based
  deterministic random bit generator (DRBG).
- `openssl-spkac` can create SPKAC files signed with SHA-1 and
  SHA-256

  You can use the `openssl-spkac` utility to create Netscape signed
  public key and challenge (SPKAC) files that are signed with hashes different from MD5.
  Likewise, you can also create and verify SPKAC files that are signed with SHA-1 and
  SHA-256 hashes.

  To use FIPS-approved only algorithms, you need only to set the FIPS flag in the
  kernel. OpenSSL then opens the FIPS provider that contains the approved algorithms.
  Thus, you no longer need to switch OpenSSL to FIPS mode.

#### `openCryptoki` 3.17.0 Supported

Some differences exist between this version and what is provided upstream. Although
`opencryptoki` supports the old data format that uses non-FIPs approved
algorithms, the FIPS provider no longer allows those algorithms. Thus, you must migrate your
existing tokens to the new format before enabling FIPS mode on your system. To migrate
tokens using the old data format, use the `pkcstok_migrate` utility. See
<https://www.ibm.com/docs/en/linux-on-systems?topic=tools-pkcstok-migrate>.

#### GnuTLS Version 3.7.3 Provided

`gnutls` 3.7.3 packages include numerous improvements and bug fixes over
previous versions, including the following: Fixed timing of the early date (zero round trip
data, 0-RTT) exchange; the `cerutil` tool no longer inherits the CRL
(Certificate Revocation List) distribution point from the certificate authority (CA) when
signing a certificate signing request (CSR).

#### Network Security Service 3.71

The Network Security Services (NSS) libraries 3.71 support only the SQLite format. Support
for legacy DBM format has been removed.

#### System Roles Support VPN Management

With the availability of VPN support, the Oracle Linux System Role can be used to more
easily create VPN tunnels for host-to-host and mesh connections that involve large numbers
of hosts. Consequently, you obtain a VPN configuration interface as well as tunneling
configuration s that are more stable and constant within the System Roles project.

#### OpenSSH Updated to Version 8.7p1

OpenSSH 8.7p1 includes notable features and enhancements such as
`LogVerbose` configuration, client address-based rate-limiting through new
directives, support for Universal 2nd Factor (U2F) hardware authenticators specified by the
FIDO Alliance, and others. This version also includes the following fixes:

- A bug fix to address an exploitable integer overflow issue in the private key parsing
  code for the XMSS key type. This key type is still experimental and support for it is
  not compiled by default. No user-facing `autoconf` option exists in
  portable OpenSSH to enable it.
- A bug fix to clarify the semantics of the `ClientAliveCountMax=0`
  keyword has been implemented in Oracle Linux 9. Instead of the previous behavior of
  instantly killing the connection after the first liveness test, regardless of its
  success, the mechanism entirely disables connection killing.
- Added protection is provided for private keys at rest in RAM against speculation and
  memory side-channel attacks like Spectre, Meltdown, and Rambleed. Oracle Linux 9
  encrypts private keys when not in use with a symmetric key that is derived from a
  relatively large âprekeyâ that consists of random data (currently 16 KB).

#### Libreswan 4.6 Supported

This version of Libreswan contains enhancements and fixes. Notably, because IKEv2 is now
generally deployed, IKEv1 packets are no longer supported by default. If your setup requires
the use of IKEv1 packets, you can enable support for these packets by adding the
`ikev1-policy=accept` line to the `/etc/ipsec.conf` file.

#### `stunnel` 5.62 Supported

This package version includes bug fixes and enhancements such as enabling or disabling the
resumption of a session through the `sessionResume` option and the
availability of a Bash-completion script.

#### Nettle Updated to Version 3.7.3

This new version contains the following enhancements:

- New algorithms and modes are supported, such as `Ed448`,
  `SHAKE256`, `AES-XTS`, and `SIV-CMAC`.
- Support is provided for architecture-specific optimizations for existing algorithms.

#### `pk11-kit` Updated to Version 0.24

In this package version, the subdirectory for the location of distrusted Certificate
Authorities is renamed `blocklist` for easier identification.

#### `cyrus-sasl` Uses GDBM Instead of Berkeley DB

The `cyrus-sasl` package no longer has the `libdb`
dependency. Further, the `sasldb` plugin uses the GDBM (GNU
`dbm`) database format instead of Berkeley DB.

To migrate existing SASL databases that are stored in the old Berkeley DB format, use the
following command:

```
cyrusbdb2current sasldb-path new-path
```

#### Updated SELinux Policy With the Current Kernel

Performance of SELinux has improved through faster loading of SELinux policy to the
kernel, reduction of memory overhead, and efficient disk space use. Additionally, the
SELinux policy integrates well with the current kernel and can use the current's
permissions, classes, and capabilities. which improves security. Better granularity in
defining permissions enables systems to run with the MLS SELinuxpolicy, which can prevent
systems with permissions undefined in the policy from starting.

Additionally, you can only disable SELinux by using the `selinux=0`
parameter in the kernel command line. Using the older method of disabling SELinux in the
`/etc/selinux/config` does not disable SELinux; but rather, SELinux
stays enabled, but no policy is loaded.

By default, SELinux policy prohibits commands with text relocation libraries. SELinux can
enter commands that use libraries requiring text relocation provided that the library files
have the `textrel_shlib_t` label.

#### `scap-security-guide` 0.1.60 Changes

In this version, rules for hardening PAM stack use `authselect` as the
configuration tool.

#### `fapolicyd` Supports Version 1.1

The following are notable features in this version:

- `/etc/fapolicyd/rules.d/` replaces
  `/etc/fapolicyd/fapolicyd.rules` to store files that allow or deny
  execution rules.
- The new `/etc/fapolicyd/trust.d` directory supports separating a
  list of trusted files into more files. You can also add an entry for a file by using the
  `fapolicyd-cli -f` command syntax enables you to add an entry for a
  file with the `--trust-file` directive to these files.
- White spaces in file names are supported through the `fapolicyd` trust
  database.
- `fapolicyd` stores the correct path to an executable file when it adds
  the file to the trust database.

#### Rsyslog Package Includes `rsyslog-mmfields` Subpackage

The subpackage provides the `mmfields` module as an alternative to the
property replacer field extraction. The module extracts all the fields at once and stores
them inside the structured data part. Thus, `mmfields` enables you to process
field based log formats such as the Common Event Format (CEF). You can also use the module
in cases where you need a large number of fields, or reuse specific fields.

#### `logrotate` Provided in a Separate `rsyslog-logrotate` Package

In this release, the `logrotate` configuration has been removed from the
main `rsyslog` package and is included in a new
`rsyslog-logrotate` package. This change is useful in certain minimal
environments for preventing the installation of unnecessary dependencies, for example, where
log rotation is not required.

#### `sudo` Program Includes Python Plugins

The `sudo 1.9` program provides capability for writing
`sudo` plugins in Python. This capability makes it easier to enhance the
`sudo` program to more precisely suit specific scenarios.

#### `libseccomp` 2.5.2 Supported

This version contains bug fixes and enhancements such as an updated syscall table for
Linux v5.14-rc7, consolidated multiplexed syscall handling for all architectures into a
single location, clarification of the maintainers' GPG keys, and so on.

#### Clevis Supports SHA-256

The Clevis framework is in compliance with the recommendations of `RFC
7638` and supports the `SHA-256` algorithm as the default hash for
JSON Web Key (JWK) thumbprints. The older thumbprints (`SHA-1`) continue to
be supported so you can still decrypt previously encrypted data.

### Virtualization

The following features, enhancements, and changes related to virtualization are introduced in
this Oracle Linux 9 release.

#### QEMU Uses Clang

In Oracle Linux 9, the QEMU emulator is built by using the Clang compiler. This
improvement enables the KVM hypervisor to use several advanced security and debugging
features, which provides better opportunities for future feature development.

#### Support for SafeStack on VMs

As of Oracle Linux 9, the QEMU machine emulator on x86\_64 and AMD64 hardware can use the
SafeStack feature. SafeStack is a enhanced compiler-based stack protection feature that
reduces the ability of an attacker to exploit a stack- based buffer overflow to change
return pointers in the stack and create Return-Oriented Programming (ROP) attacks. This
change makes virtual machines (VMs) that are hosted on Oracle Linux 9 significantly more
secure against ROP-based vulnerabilities.

### Containers

The following features, enhancements, and changes related to containers are introduced in
this Oracle Linux 9 release.

#### Podman Supports Short Names

The `registries.conf` file now accepts configuration of short-name aliases
for images in the `[aliases]` table. The short-names modes are:

- Enforcing: If no matching alias is found during the image pull, Podman prompts
  the user to choose one of the unqualified-search registries. If the selected image is
  pulled successfully, Podman automatically records a new short-name alias in the
  `$HOME/.cache/containers/short-name-aliases.conf` file (rootless user)
  and in the `/var/cache/containers/short-name-aliases.conf` (root user).
  If the user cannot be prompted (for example, `stdin` or
  `stdout` are not a TTY), Podman fails. Note that the
  `short-name-aliases.conf` file has precedence over
  `registries.conf` file if both specify the same alias.
- Permissive: Similar to enforcing mode, but Podman does not fail if the user
  cannot be prompted. Instead, Podman searches in all unqualified-search registries in the
  given order. Note that no alias is recorded.

#### Changes in `container-tools` Module

The `container-tools` module contains the Podman, Buildah, Skopeo, and
`runc` tools. The rolling stream, represented by the
`container-tools:ol8` stream in Oracle Linux 8, is named
`container-tools:latest` in Oracle Linux 9. Similarly to Oracle Linux 8,
stable versions of container tools are going to be available in numbered streams (for
example, 3.0).

#### `containers-common` Package Available In `containers-tools:latest` Module

The `containers-common` package has been added to the
`container-tools:latest` module. The `containers-common`
package contains common configuration files and documentation for the container tools'
ecosystem, such as Podman, Buildah, and Skopeo.

#### `podman-py` Package Available

The `podman-py` package has been added to the
`container-tools:3.0` stable module stream and the
`container-tools:latest` module. The `podman-py` package is
a library of bindings to use the RESTful API of Podman.

#### Improvements From Control Groups Version 2

With the availability of `cgroupv2`, system administrators can limit
resources for any application without causing performance problems that were encountered in
the previous version.

For additional information about notable changes in `cgroupv2`, see <unresolvable-reference.html#ol9-features-kernel>.

#### `container-tools meta-package` Available

This RPM meta-package includes Podman, Buildah, Skopeo, CRIU, Udica, and all required
libraries, and are in Oracle Linux 9. To install the container-tools meta-package, run the
following command:

```
sudo dnf install container-tools
```

#### Podman Builds and Runs Pods Using YAML Files

The `podman play kube` command automatically builds and runs multiple
pods with multiple containers in the pods using a YAML file.

#### Oracle Linux 9 Containers on Oracle Linux 7 Host Unsupported

Running Oracle Linux 9 containers on an Oracle Linux 7 host is not supported. Such a setup
might work, but cannot be guaranteed.

### Cloud Environment

The following changes and features apply to Oracle Linux used in cloud environments.

#### WALinuxAgent Updated to Version 2.3.0.2

The Windows Azure Linux Agent (WALinuxAgent) has been upgraded to upstream version
2.3.0.2, which introduces a number of bug fixes and enhancement, most notably the following:

- Support has been added for RequiredFeatures and GoalStateAggregateStatus APIs.
- Fallback locations for extension manifests have been added.
- Missing calls to `str.format()` have been added when creating
  exceptions.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.0/ol9-TechnologyPreview.html -->

## 3 Technology Preview

The following items are available as technical previews in this release of Oracle Linux. Note
that some items listed apply to Red Hat Compatible Kernel (RHCK) and might already be
available in UEK.

### KTLS

Oracle Linux 9 provides kernel Transport Layer Security (KTLS) as a technology preview.

The Linux Kernel TLS (KTLS) handles TLS records for the AES-GCM cipher. KTLS also provides
the interface for offloading TLS record encryption to NICs that support this functionality.

OpenSSL 3.0 is able to use KTLS if the `enable-ktls` configuration option is
used during compiling.

The updated `gnutls` packages can use KTLS for accelerating data transfer on
encrypted channels. To enable KTLS, add the `tls.ko` kernel module using the
`modprobe` command, and create a new configuration file
`/etc/crypto-policies/local.d/gnutls-ktls.txt` for the system-wide
cryptographic policies with the following content:

```
[global]
ktls = true
```

Note that `gnutls` doesn't permit you to update traffic keys through TLS
`KeyUpdate` messages, which impacts the security of AES-GCM ciphersuites.

### SGX Available

Software Guard Extensions (SGX) from Intel® protects software code and data from disclosure
and modification. The Linux kernel partially supports SGX v1 and SGX v1.5. Version 1 enables
platforms by using the Flexible Launch Control mechanism to use the SGX technology.

Note that SGX is supported in UEK.

### DAX File System Available

In this release,
the DAX file system is available as a Technology Preview for the ext4 and XFS file systems.
DAX enables an application to directly map persistent memory into its address space. The
system must have some form of persistent memory available to use DAX. Persistent memory can be
in the form of one or more Non-Volatile Dual In-line Memory Modules (NVDIMMs). In addition, a
file system that supports DAX must be created on the NVDIMMs; the file system must be mounted
with the `dax` mount option. Then, an `mmap` of a file on the
DAX mounted file system results in a direct mapping of storage into the application's address
space.

### SEV and SEV-ES

The Secure Encrypted Virtualization (SEV) feature is provided for AMD EPYC host machines that
use the KVM hypervisor. It encrypts a virtual machine's memory and protects the VM from access
by the host.

SEV's enhanced Encrypted State version (SEV-ES) encrypts all CPU register contents when a VM
stops running, thus preventing the host from modifying the VM's CPU registers or reading any
information from them.

Note that SEV is supported in UEK.

### WireGuard

WireGuard is a VPN solution that has improved security features and is easily
configurable.

Note that WireGuard is fully supported in UEK. See [Oracle Linux: Configuring Virtual Private Networks](https://docs.oracle.com/en/operating-systems/oracle-linux/vpn/)
for more information on using WireGuard on Oracle Linux.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.0/ol9-DeprecatedFeatures.html -->

## 4 Deprecated Features

This chapter lists features and functionalities that are deprecated in Oracle Linux 9. While
these features might be included and operative in the release, support isn't guaranteed in
future major releases. Thus, these features must not be used in new Oracle Linux 9
deployments.

### Installation

The following installation related features and functionalities are deprecated in Oracle
Linux 9.

#### Kickstart Commands

- `timezone --ntpservers`
- `timezone --nontp`
- `logging --level`
- `%packages --excludeWeakdeps`
- `%packages --instLangs`
- `%anaconda`
- `pwpolicy`
- `nvdimm`

Even though specific options are listed as deprecated, the base command and the other
options remain available and operative. If you use a deprecated command in kickstart
files, warnings are generated in the logs. To change deprecated command warnings to
errors, set the `inst.ksstrict` boot option.

### Dynamic Programming Languages, Web and Database Servers

The following features and functionalities that are related to dynamic programming, web, and
database servers are deprecated in Oracle Linux 9.

#### Berkeley DB (`libdb`)

Deprecation of the Berkely DB (`libdb`) package includes the removal of
cryptographic algorithms and dependencies. Users of `libdb` should
migrate to a different key-value database.

#### Python Packages

`python3-pytz` and `mcpp` packages are removed from Oracle
Linux 9.

### Networking

The following network related features and functionalities are deprecated in Oracle Linux
9.

#### Network Teams

The `teamd` service, and the `libteam` library, and support
for configuring network teams are deprecated in favor of network bonds. You should use
network bonds instead, which have similar functions as teams, and which would receive
enhancements and updates.

#### `/etc/sysconfig/network-scripts` File

Network configurations profiles used to be in `ifcfg` format and stored in the
`/etc/sysconfig/network-scripts` directory. This format is deprecated. In
Oracle Linux 9, new network configurations are stored in
`/etc/NetworkManager/system-connections` in keyfile format. This format works
with all the connection settings provided by NetworkManager.

However, information in the `/etc/sysconfig/network-scripts` remain
operative, and modifications to existing profiles continue to update the older
files.

#### `iptables` Framework

With the deprecation of the `iptables` framework, the
`iptables` backend and the `direct interface` are also
deprecated.

Therefore, the following packages are also deprecated:

- `iptables-devel`
- `iptables-libs`
- `iptables-nft`
- `iptables-nft-services`
- `iptables-utils`

As an alternative to using `direct interface`, use the native features in
`firewalld` to configure the required rules.

### Security

The following security related features and functionalities are deprecated in Oracle Linux
9.

#### SHA-1 Algorithm

The SHA1 algorithm is deprecated in Oracle Linux 9. Digital signatures using SHA-1 hash
algorithm are no longer considered secure and therefore not allowed on Oracle Linux 9
systems by default. Oracle Linux 9 has been updated to avoid using SHA-1 in
security-related use cases.

However, the HMAC-SHA1 message authentication code and the Universal Unique Identifier
(UUID) values can still be created by using SHA-1.

In cases where you need SHA-1 to verify existing or third party cryptographic
signatures, you can enable SHA-1 as follows:

```
sudo update-crypto-policies --set DEFAULT:SHA1
```

As an alternative, you can switch the systemwide crypto policies to the
`LEGACY` policy. However, this policy also enables other algorithms
that are not secure, and therefore risks making the system vulnerable.

Furthermore, use of the SHA-1 algorithm at `SECLEVEL=2` is
deprecated in OpenSSL.

#### SCP Protocol

In the `scp` utility, secure copy protocol (SCP) is replaced by the SSH
File Transfer Protocol (SFTP) by default. Likewise, SCP is deprecated in the
`libssh` library.

Oracle Linux 9 doesn't use SCP in the OpenSSH suite.

#### OpenSSL Cryptographic Algorithms

- MD2
- MD4
- MDC2
- Whirlpool
- RIPEMD160
- Blowfish
- CAST
- DES
- IDEA
- RC2
- RC4
- RC5
- SEED
- PBKDF1

The implementations of these algorithms have been moved to the legacy provider in
OpenSSL

For instructions on how to load the legacy provider and enable support for the deprecated
algorithms, see the `/etc/pki/tls/openssl.cnf` configuration file.

#### `libcrypt.so.1`

The `libcrypt.so.1` cryptogarhic library is deprecated.

#### `/etc/system-fips` File

The `/etc/system-fips` file was used to indicate the FIPS mode in the
system. This file is removed in Oracle Linux 9.

To install Oracle Linux 9 in FIPS mode, add the `fips=1` parameter to the
kernel command line during the system installation. To check whether Oracle Linux 9 is
operating in FIPS mode, use the `fips-mode-setup --check` command.

#### `fapolicyd.rules` File

The `/etc/fapolicyd/fapolicyd.rules` file is deprecated. You can store policy
rules for `fapolicyd` in the `/etc/fapolicyd/rules.d/`
directory. The `fagenrules` script merges all component rule files in
this directory to the `/etc/fapolicyd/compiled.rules` file.

Rules in `/etc/fapolicyd/fapolicyd.trust` continue to be processed by
`fapolicyd` for backward compatibility.

### Kernel

The following kernel related features and functionalities are deprecated in Oracle Linux
9.

#### Asynchronous Transfer Mode

Asynchronous Transfer Mode (ATM) encapsulation enables Layer-2 (Point-to-Point Protocol,
Ethernet) or Layer-3 (IP) connectivity for the ATM Adaptation Layer 5 (AAL-5). Currently,
these protocols are used only in chipsets that use ADSL technology, which are being phased
out.

#### `crashkernel=auto` Option

The `crashkernel=auto` option is deprecated and no longer supported on Oracle Linux 9 and is also unsupported for UEK R7 and later. Some platforms, such as the Raspberry Pi have maximum limits for `crashkernel` memory reservation and these must be specified explicitly. This option will be removed in a future UEK release.

### File Systems and Storage

The following features and functionalities related to file systems and storage are deprecated
in Oracle Linux 9.

#### `lvm2-activation-generator`

The `lvm2-activation-generator` program is deprecated, together with its
generated services as follows:

- `lvm2-activation`
- `lvm2-activation-early`
- `lvm2-activation-net`

The `lvm.conf event_activation` that used to activate these services no
longer works. The only method that is used for automatic activation of volume groups is
event based activation.

### Desktop

The following desktop related features and functionalities are deprecated in Oracle Linux
9.

#### X.org Server

In Oracle Linux 9, the `X.org` display server is deprecated, and
consequently, the `xorg-x11-server-Xorg` package.

The default desktop session is the Wayland session. However, the X11 protocol continues
to be supported by using the `XWayland` backend. Therefore, applications
that require X11 can run in Wayland sessions.

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
Linux 9.

#### Signatures Using SHA-1

The use of SHA1-based signatures to perform SecureBoot image verification on UEFI
(PE/COFF) executables is deprecated. Instead, use signatures that are based on SHA-2 or
later.

#### Virtual Machine Snapshots

Support for creating snapshots of VMs is limited only to those that do not use UEFI
firmware. However, the operation might cause the QEMU monitor to become blocked and
affects hypervisor operations.

As an alternative, use external snapshots.

#### Virtual Machine Snapshots

Support for creating snapshots of VMs is limited only to those that do not use UEFI
firmware. However, the operation might cause the QEMU monitor to become blocked and
affects hypervisor operations.

As an alternative, use external snapshots.

#### `libvirtd` Daemon

As a replacement of the deprecated `libvirtd` daemon, use the modular daemons
in the `libvirt` library. For example, the `virtqemud` handles
QEMU drivers.

#### Virtual Floppy Driver

The `isa-fdc` driver controls virtual floppy disk devices. To ensure
compatibility with migrated virtual machines (VMs), you should not use floppy disk
devices in virtual machines that you subsequently host on Oracle Linux 9.

#### `qcow2-v2` Format

For virtual disk images, use the `qcow2-v3` format instead.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.0/ol9-KnownIssues.html -->

## 5 Known Issues

This
chapter describes known issues that you may encounter when installing and using the Oracle
Linux 9 software. Unless indicated otherwise, the issues apply to both x86\_64 and aarch64
systems. Information that pertains only to a specific platform is also noted accordingly.

### Installation Issues

The following are known installation issues for Oracle Linux 9.

#### iscsi-init service falls into a failed state by default

At the initial boot after installation, the
`iscsi-init.service` service enters a failed
state on a system where the operating system is installed to
local disk. The failure is caused by the service attempting to
write to a configuration file early in the boot process before
the root file system becomes writable. Running the
`systemctl is-system-running` command
generates a report that indicates that the system is degraded.
However, if a system is configured with a valid
`InitiatorName` value in the
`/etc/iscsi/initiatorname.iscsi` file, this
issue is not encountered. In this case, the service runs
normally.

To workaround this issue, wait until the system is fully
booted. Then, run the following command:

```
sudo systemctl restart iscsi-init
```

The `iscsi-init.service` is a one-time
service in the installation process and therefore, the issue
is no longer encountered in subsequent reboots.

(Bug ID 33930979)

#### Network Installation With PXE Boot Server Fails

While using a PXE boot server to perform a network installation on a UEFI client where
Secure Boot is enabled, the installation might fail because the `grubx64.efi`
file can't load the `grub` configuration file. The `grub`
bootloader switches to the command line mode and the installation process stops at the
`grub` prompt.

To work around this issue, configure the
`tftpd` service to run with the `-r
blksize` option enabled.

If you are using `dnsmasq` for TFTP services,
uncomment the `tftp-no-blocksize` line in the
`/etc/dnsmasq.conf` file. Then restart the
`dnsmasq` service.

(Bug ID 34233443)

### Virtualization Issues

The following are known virtualization issues for Oracle Linux 9

#### KVM Virtual Machines Panic When Started on Oracle Linux 9 Hosts

The `glibc` version that's included with Oracle Linux 9 checks for
compatibility between a system's CPU and new architectures that are supported. A system might
pass the compatibility check. However, the CPU flags that are set on the system after passing
the check might be unknown to the KVM virtual machines that are hosted on that system.
Consequently, the VMs panic when they're booted.

To work around this issue, run the following command:

```
virsh edit vm-name
```

Then, add the following declaration in the virtual machine's
XML file:

```
<cpu mode='host-model' check='partial'/>
```

The `check` parameter's `partial` setting sets
`libvirt` to check the VM's CPU specification before starting a domain.
However, the rest of the checking remains on the hypervisor, which can still provide a
different virtual CPU.

(Bug ID 34224821)

#### Virtual Machines Fail to Start at Boot Because the `virbr0` Interface Isn't Available

After reboot, the `virbr0` network interface might be missing, which can
prevent virtual machines from automatically starting up after boot.

The libvirt daemons on Oracle Linux 9 are modular to handle atomic features within the
virtualization environment and are started and run as required, and stopped after two minutes
of inactivity. The daemon responsible for setting up the networking interfaces for libvirt is
`virtnetworkd`. This service isn't automatically started when a virtual
machine is started.

To work around this issue, enable the `virtnetworkd` service so that the
service starts at boot:

```
sudo systemctl enable --now virtnetworkd
```

(Bug ID 34237540)

### Kernel Issues

The following are known kernel issues in Oracle Linux 9.

#### Kdump Might Fail on Some AMD Hardware

Kdump might fail on some AMD hardware that's running the current Oracle Linux
release. Impacted hardware includes the AMD EPYC CPU servers.

To work around this issue, modify the `/etc/sysconfig/kdump` configuration
file and remove the `iommu=off` command line option from the
`KDUMP_COMMANDLINE_APPEND` variable. Restart the `kdump`
service for the changes to take effect.

This issue appears to affect systems running RHCK.

(Bug ID 31274238, 34211826, 34312626)

#### Sub-optimal Kdump settings on some platforms

The `crashkernel` memory reservations for
certain platforms might not be optimal in all circumstances.

To check if Kdump settings are optimal, ensure the Kdump
kernel is loaded:

```
sudo kdumpctl status
kdump: Kdump is operational
```

If `kdumpctl` reports otherwise, change the
`crashkernel` settings to a higher value for
your memory requirements:

1. Run `cat /proc/cmdline` to see the
   current kernel command line options.
2. Use the `grubby` command to remove the
   current `crashkernel` settings for all
   kernels, for example:

   ```
   sudo grubby --update-kernel=ALL --remove-args="crashkernel=2G-8G:256M,8G-:896M
   ```
3. Use the `grubby` command to add a new
   `crashkernel` setting for all kernels,
   for example:

   ```
   sudo grubby --update-kernel=ALL --args="crashkernel=2G-:448M"
   ```
4. Reboot the system for the changes to take effect. Confirm
   that the new changes have enabled the Kdump kernel to load
   correctly.

The `crashkernel=auto` option is no longer
supported on Oracle Linux 9. Some platforms, such as the
Raspberry Pi have maximum limits for crashkernel memory
reservation.

(Bug ID 34240246)

### `flatpak-system-helper` File Access Triggers SELinux Policy Violations

Booting Oracle Linux 9 with a GUI desktop environment that has
SELinux enabled can produce SELinux security messages similar to
the following:

```
SELinux is preventing /usr/libexec/flatpak-system-helper from read access on the file passwd.
SELinux is preventing /usr/libexec/flatpak-system-helper from write access on the directory flatpak.
SELinux is preventing /usr/libexec/flatpak-system-helper from watch access on the directory /usr/libexec.
```

A popup message notifying you of a violation might appear
immediately after the installation if the `Server with
GUI` or `Workstation with GUI`
installation profiles are selected and SELinux is enabled and
Flatpak installed.

You can continue to use Flatpak with SELinux; however, continued
use can result in large numbers of messages to the logs.

To work around this issue, create an SELinux policy module for
the `flatpak-system-helper` service:

```
ausearch -c 'flatpak-system-' --raw |audit2allow -M my-flatpaksystem
semodule -i my-flatpaksystem.pp
```

(Bug ID 34321783)

### (aarch64) Some GUI Elements Aren't Displayed During Installation and Boot Using VGA Output

During installations on the Arm platform, the Oracle Linux installer doesn't display some
GUI elements, such as the progress update screen, on VGA output. Output is displayed on the
serial console, instead.

Additionally, if you install Oracle Linux with GUI on an encrypted disk, for example, by choosing Server with GUI during the installation stage, and VGA is enabled, the password prompt doesn't appear on the VGA output at system boot, and consequently, the boot process can't be completed. The prompt appears only on a serial console, and therefore, you would need to switch to a serial console to provide the password there.

This issue is specific to systems on the Arm platform only and occurs regardless of whether
you are using secure boot or non secure boot. Further, the issue applies to Oracle Linux 8 or
Oracle Linux 9 systems that use UEKR6 and UEKR7. The issue occurs wherever Plymouth graphical
elements are loaded in the GUI.

To resolve these GUI issues and to cause these elements to display on VGA output without
using a serial console, add `plymouth.ignore-serial-consoles`
to the kernel command line in the GRUB configuration. For instructions, see
[Oracle Linux 9: Managing Kernels and System
Boot](https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/).

(Bug ID 35034465 and 35270637)

### Certain SEV Guest Configurations Might Cause Hypervisor CPU Soft-Lockup Warnings

On older generation AMD systems that are based on the AMD Rome processors, such as E2 and E3
systems, a guest with more than 350GB memory that's configured to use Secure
Encrypted Virtualization (SEV) memory encryption can trigger a CPU
soft-lockup warning on the hypervisor host during guest boot or shutdown
operations.

The time that's needed to flush the pinned memory that's being encrypted is proportional to
the amount of guest memory. However, with larger amounts of memory in excess
of 350GB, the time on the CPU to flush the memory becomes excessive, which
consequently triggers a warning. After the memory is flushed, the hypervisor
resumes normal operations.

Newer systems that are based on the AMD Milan processor, such as E4 systems, have hardware
support that can minimize the time required for flushing the memory.
Therefore, the CPU soft-hang issue isn't encountered.

As a workaround, if a SEV enabled guest with more then 350GB of memory is required, create
the guest on a system that's based on the AMD Milan processor. If you are
using systems with the AMD Rome processor, limit the guest memory to less
than 350GB if the guest is configured with SEV memory encryption.

(Bug ID 34050377)

### Tuned Profile Packages for Oracle Cloud Infrastructure Are Moved

Packages intended for use only on Oracle Cloud Infrastructure instances, such
as the `tuned-profile-oci-*` packages, are available in the
`ol9_appstream` repository. Some of these packages were previously
available in the dedicated `ol9_oci_included` repository but have been
moved to avoid cross-channel dependencies.

The `tuned-profile` packages include profiles intended to run in specific
corresponding environments and must be intentionally installed for the correct
environment.

Sources for all profiles are included in the tuned source RPM package that is available
in the `ol9_baseos` repository.

(Bug 34867566)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.0/ol-PackageChangesfromtheUpstreamRelease.html -->

## 6 Package Changes From the Upstream Release

The following sections list the changes to binary and source
packages from the upstream release.

### Changes to Binary Packages

This section contains information about the removed, modified, and new binary packages in this release. For information about the source package changes, see [Changes to Source Packages](ol-PackageChangesfromtheUpstreamRelease.html#ol9-packages-source).

#### Added Binary Packages for BaseOS by Oracle

The following binary packages have been added to BaseOS by Oracle:

- `bcache-tools`
- `btrfs-progs`
- `dtrace`
- `iwl3945-firmware`
- `iwl4965-firmware`
- `iwl6000-firmware`
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
- `libertas-sd8686-firmware`
- `libertas-usb8388-firmware`
- `libertas-usb8388-olpc-firmware`
- `linux-firmware-core`
- `liquidio-firmware`
- `NetworkManager-config-connectivity-oracle`
- `ocfs2-tools`
- `oracle-backgrounds`
- `oracle-indexhtml`
- `oraclelinux-release`
- `oraclelinux-release-el9`
- `oracle-logos`
- `oracle-logos-httpd`
- `oracle-logos-ipa`

#### Added Binary Packages for AppStream by Oracle:

The following binary packages have been added to AppStream by Oracle:

- `dnf-plugin-spacewalk`
- `dtrace-devel`
- `dtrace-testsuite`
- `libblockdev-btrfs`
- `python3-dnf-plugin-spacewalk`
- `python3-dnf-plugin-ulninfo`
- `python3-hwdata`
- `python3-pyOpenSSL`
- `python3-rhn-check`
- `python3-rhn-client-tools`
- `python3-rhnlib`
- `python3-rhn-setup`
- `python3-rhn-setup-gnome`
- `rhn-check`
- `rhn-client-tools`
- `rhnlib`
- `rhnsd`
- `rhn-setup`
- `rhn-setup-gnome`

#### Added Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages have been added to CodeReady Linux Builder by Oracle:

- `oraclelinux-sb-certs`

#### Modified BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been modified:

- `alternatives`
- `autofs`
- `binutils`
- `binutils-gold`
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
- `dbus-libs`
- `dbus-tools`
- `dnf`
- `dnf-automatic`
- `dnf-data`
- `dnf-plugins-core`
- `dracut`
- `dracut-config-generic`
- `dracut-config-rescue`
- `dracut-network`
- `dracut-squash`
- `dracut-tools`
- `efibootmgr`
- `efi-filesystem`
- `firewalld`
- `firewalld-filesystem`
- `fwupd`
- `glibc`
- `glibc-all-langpacks`
- `glibc-common`
- `glibc-gconv-extra`
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
- `glibc-langpack-ckb`
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
- `glibc-langpack-mnw`
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
- `glibc-minimal-langpack`
- `grub2-common`
- `grub2-efi-aa64-modules`
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
- `ima-evm-utils`
- `iproute`
- `iproute-tc`
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
- `krb5-libs`
- `krb5-pkinit`
- `krb5-server`
- `krb5-server-ldap`
- `krb5-workstation`
- `libatomic`
- `libdnf`
- `libertas-sd8686-firmware`
- `libertas-sd8787-firmware`
- `libertas-usb8388-firmware`
- `libertas-usb8388-olpc-firmware`
- `libgcc`
- `libgfortran`
- `libgomp`
- `libipa_hbac`
- `libkadm5`
- `libkcapi`
- `libkcapi-hmaccalc`
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
- `linux-firmware`
- `linux-firmware-core`
- `linux-firmware-whence`
- `liquidio-firmware`
- `mcelog`
- `microcode_ctl`
- `netronome-firmware`
- `NetworkManager`
- `NetworkManager-adsl`
- `NetworkManager-bluetooth`
- `NetworkManager-config-connectivity-oracle`
- `NetworkManager-config-server`
- `NetworkManager-initscripts-updown`
- `NetworkManager-libnm`
- `NetworkManager-team`
- `NetworkManager-tui`
- `NetworkManager-wifi`
- `NetworkManager-wwan`
- `nscd`
- `nvmetcli`
- `os-prober`
- `polkit`
- `polkit-libs`
- `python3-configshell`
- `python3-dnf`
- `python3-dnf-plugin-post-transaction-actions`
- `python3-dnf-plugins-core`
- `python3-dnf-plugin-versionlock`
- `python3-firewall`
- `python3-hawkey`
- `python3-libdnf`
- `python3-libipa_hbac`
- `python3-libsss_nss_idmap`
- `python3-rpm`
- `python3-sss`
- `python3-sssdconfig`
- `python3-sss-murmur`
- `redhat-release`
- `rpm`
- `rpm-build-libs`
- `rpm-libs`
- `rpm-plugin-audit`
- `rpm-plugin-selinux`
- `rpm-sign`
- `rpm-sign-libs`
- `selinux-policy`
- `selinux-policy-doc`
- `selinux-policy-mls`
- `selinux-policy-sandbox`
- `selinux-policy-targeted`
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
- `systemd-libs`
- `systemd-oomd`
- `systemd-pam`
- `systemd-resolved`
- `systemd-rpm-macros`
- `systemd-udev`
- `tuned`
- `tuned-profiles-cpu-partitioning`
- `vim-filesystem`
- `vim-minimal`
- `yum`
- `yum-utils`

#### Modified Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `crash-devel`
- `cups-filters-devel`
- `dotnet-sdk-6.0-source-built-artifacts`
- `fwupd-devel`
- `gcc-plugin-devel`
- `glibc-benchtests`
- `glibc-nss-devel`
- `glibc-static`
- `ima-evm-utils-devel`
- `iproute-devel`
- `kmod-devel`
- `libdnf-devel`
- `libguestfs-devel`
- `libguestfs-gobject`
- `libguestfs-gobject-devel`
- `libguestfs-man-pages-ja`
- `libguestfs-man-pages-uk`
- `librados-devel`
- `libradospp-devel`
- `librbd-devel`
- `libreoffice-sdk`
- `libreoffice-sdk-doc`
- `libsss_nss_idmap-devel`
- `libstdc++-static`
- `libtirpc-devel`
- `libvirt-devel`
- `libvirt-docs`
- `libvirt-lock-sanlock`
- `lua-guestfs`
- `mpich`
- `munge-devel`
- `NetworkManager-libnm-devel`
- `nginx-mod-devel`
- `nss_db`
- `nss_hesiod`
- `ocaml-libguestfs`
- `ocaml-libguestfs-devel`
- `OpenIPMI-devel`
- `openscap-engine-sce-devel`
- `PackageKit-glib-devel`
- `python3-ipatests`
- `python3-mpich`
- `ruby-libguestfs`
- `sanlock-devel`
- `sendmail-milter`
- `sendmail-milter-devel`
- `tog-pegasus-devel`
- `virt-v2v-man-pages-ja`
- `virt-v2v-man-pages-uk`

#### Modified AppStream Binary Packages

The following binary packages from the AppStream upstream release have been modified:

- `aardvark-dns`
- `anaconda`
- `anaconda-core`
- `anaconda-dracut`
- `anaconda-gui`
- `anaconda-install-env-deps`
- `anaconda-install-img-deps`
- `anaconda-tui`
- `anaconda-user-help`
- `anaconda-widgets`
- `aspnetcore-runtime-6.0`
- `aspnetcore-targeting-pack-6.0`
- `autocorr-af`
- `autocorr-bg`
- `autocorr-ca`
- `autocorr-cs`
- `autocorr-da`
- `autocorr-de`
- `autocorr-dsb`
- `autocorr-el`
- `autocorr-en`
- `autocorr-es`
- `autocorr-fa`
- `autocorr-fi`
- `autocorr-fr`
- `autocorr-ga`
- `autocorr-hr`
- `autocorr-hsb`
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
- `autocorr-vro`
- `autocorr-zh`
- `binutils-devel`
- `blivet-data`
- `boom-boot`
- `boom-boot-conf`
- `boom-boot-grub2`
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
- `cockpit-packagekit`
- `cockpit-pcp`
- `cockpit-session-recording`
- `cockpit-storaged`
- `compat-libgfortran-48`
- `containers-common`
- `container-tools`
- `cpp`
- `crash`
- `cups-filters`
- `cups-filters-libs`
- `dbus-daemon`
- `dbus-devel`
- `dbus-x11`
- `ddiskit`
- `delve`
- `dotnet-apphost-pack-6.0`
- `dotnet-host`
- `dotnet-hostfxr-6.0`
- `dotnet-runtime-6.0`
- `dotnet-sdk-6.0`
- `dotnet-targeting-pack-6.0`
- `dotnet-templates-6.0`
- `dracut-caps`
- `dracut-live`
- `efi-srpm-macros`
- `eth-tools-basic`
- `eth-tools-fastfabric`
- `fapolicyd`
- `fapolicyd-dnf-plugin`
- `fapolicyd-selinux`
- `firefox`
- `firewall-applet`
- `firewall-config`
- `fwupd-plugin-flashrom`
- `galera`
- `gcc`
- `gcc-c++`
- `gcc-gfortran`
- `gcc-offload-nvptx`
- `gcc-plugin-annobin`
- `gdb`
- `gdb-doc`
- `gdb-gdbserver`
- `gdb-headless`
- `gdb-minimal`
- `git-clang-format`
- `glibc-devel`
- `glibc-doc`
- `glibc-headers`
- `glibc-locale-source`
- `glibc-utils`
- `gnome-shell-extension-background-logo`
- `httpd`
- `httpd-devel`
- `httpd-filesystem`
- `httpd-manual`
- `httpd-tools`
- `initial-setup`
- `initial-setup-gui`
- `ipa-client`
- `ipa-client-common`
- `ipa-client-epn`
- `ipa-client-samba`
- `ipa-common`
- `ipa-selinux`
- `ipa-server`
- `ipa-server-common`
- `ipa-server-dns`
- `ipa-server-trust-ad`
- `krb5-devel`
- `ksh`
- `libasan`
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
- `libblockdev-tools`
- `libblockdev-utils`
- `libgccjit`
- `libgccjit-devel`
- `libgomp-offload-nvptx`
- `libguestfs`
- `libguestfs-appliance`
- `libguestfs-bash-completion`
- `libguestfs-inspect-icons`
- `libguestfs-rescue`
- `libguestfs-rsync`
- `libguestfs-xfs`
- `libitm`
- `libitm-devel`
- `liblsan`
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
- `libreoffice-help-eo`
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
- `libreoffice-langpack-eo`
- `libreoffice-langpack-es`
- `libreoffice-langpack-et`
- `libreoffice-langpack-eu`
- `libreoffice-langpack-fa`
- `libreoffice-langpack-fi`
- `libreoffice-langpack-fr`
- `libreoffice-langpack-fy`
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
- `libreport-plugin-bugzilla`
- `libreport-plugin-reportuploader`
- `libreport-web`
- `libreswan`
- `libstdc++-devel`
- `libstdc++-docs`
- `libtsan`
- `libubsan`
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
- `libvirt-daemon-driver-storage-iscsi`
- `libvirt-daemon-driver-storage-logical`
- `libvirt-daemon-driver-storage-mpath`
- `libvirt-daemon-driver-storage-rbd`
- `libvirt-daemon-driver-storage-scsi`
- `libvirt-daemon-kvm`
- `libvirt-libs`
- `libvirt-nss`
- `libxslt`
- `libxslt-devel`
- `lorax`
- `lorax-docs`
- `lorax-lmc-novirt`
- `lorax-lmc-virt`
- `lorax-templates-generic`
- `lorax-templates-rhel`
- `mecab-ipadic`
- `mecab-ipadic-EUCJP`
- `mod_ldap`
- `mod_lua`
- `mod_proxy_html`
- `mod_session`
- `mod_ssl`
- `mpich`
- `mpich-autoload`
- `mpich-devel`
- `mpich-doc`
- `munge`
- `munge-libs`
- `netavark`
- `netstandard-targeting-pack-2.1`
- `NetworkManager-cloud-setup`
- `NetworkManager-dispatcher-routing-rules`
- `NetworkManager-ovs`
- `NetworkManager-ppp`
- `nginx`
- `nginx-all-modules`
- `nginx-filesystem`
- `nginx-mod-http-image-filter`
- `nginx-mod-http-perl`
- `nginx-mod-http-xslt-filter`
- `nginx-mod-mail`
- `nginx-mod-stream`
- `ntsysv`
- `opa-address-resolution`
- `opa-basic-tools`
- `opa-fastfabric`
- `opa-fm`
- `opa-libopamgt`
- `OpenIPMI`
- `OpenIPMI-lanserv`
- `OpenIPMI-libs`
- `openscap`
- `openscap-devel`
- `openscap-engine-sce`
- `openscap-python3`
- `openscap-scanner`
- `openscap-utils`
- `open-vm-tools`
- `open-vm-tools-desktop`
- `open-vm-tools-sdmp`
- `open-vm-tools-test`
- `osbuild-composer`
- `osbuild-composer-core`
- `osbuild-composer-dnf-json`
- `osbuild-composer-worker`
- `oscap-anaconda-addon`
- `osinfo-db`
- `PackageKit`
- `PackageKit-command-not-found`
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
- `plymouth`
- `plymouth-core-libs`
- `plymouth-graphics-libs`
- `plymouth-plugin-fade-throbber`
- `plymouth-plugin-label`
- `plymouth-plugin-script`
- `plymouth-plugin-space-flares`
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
- `polkit-devel`
- `polkit-docs`
- `pykickstart`
- `python3-blivet`
- `python3-blockdev`
- `python3-boom`
- `python3-clang`
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-iscsi-initiator-utils`
- `python3-kickstart`
- `python3-libguestfs`
- `python3-libreport`
- `python3-pki`
- `python3-rtslib`
- `python3-sanlock`
- `rear`
- `rhel-system-roles`
- `rpm-apidocs`
- `rpm-build`
- `rpm-cron`
- `rpm-devel`
- `rpmdevtools`
- `rpm-plugin-fapolicyd`
- `rpm-plugin-ima`
- `rpm-plugin-syslog`
- `rpm-plugin-systemd-inhibit`
- `sanlock`
- `sanlock-lib`
- `scap-security-guide`
- `scap-security-guide-doc`
- `selinux-policy-devel`
- `sendmail`
- `sendmail-cf`
- `sendmail-doc`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `setroubleshoot-server`
- `systemd-devel`
- `systemd-journal-remote`
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
- `target-restore`
- `thunderbird`
- `tog-pegasus`
- `tog-pegasus-libs`
- `tuned-gtk`
- `tuned-profiles-atomic`
- `tuned-profiles-mssql`
- `tuned-profiles-oracle`
- `tuned-profiles-spectrumscale`
- `tuned-utils`
- `vim-common`
- `vim-enhanced`
- `vim-X11`
- `virt-install`
- `virt-manager`
- `virt-manager-common`
- `virt-p2v`
- `virt-v2v`
- `virt-v2v-bash-completion`
- `WALinuxAgent`
- `WALinuxAgent-udev`
- `xsane`
- `xsane-common`

#### Removed BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been removed:

- `kpatch`
- `kpatch-dnf`
- `libdnf-plugin-subscription-manager`
- `python3-cloud-what`
- `python3-subscription-manager-rhsm`
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
- `insights-client`
- `libreport-rhel-anaconda-bugzilla`
- `NetworkManager-config-connectivity-redhat`
- `nmap`
- `nmap-ncat`
- `realtime-tests`
- `redhat-backgrounds`
- `redhat-indexhtml`
- `redhat-logos`
- `redhat-logos-httpd`
- `redhat-logos-ipa`
- `rhc`
- `rhc-worker-playbook`
- `toolbox`
- `toolbox-tests`
- `virtio-win`
- `virt-who`

#### Removed CodeReady Linux Builder Binary Packages

The following binary packages from the CodeReady Linux Builder upstream release have been removed:

- `redhat-sb-certs`

### Changes to Source Packages

This section contains information about the removed, modified, and new source packages in this release. For information about the binary package changes, see [Changes to Binary Packages](ol-PackageChangesfromtheUpstreamRelease.html#ol9-packages-binary).

#### Added Source Packages for BaseOS by Oracle

The following source packages have been added to the BaseOS by Oracle:

- `bcache-tools`
- `btrfs-progs`
- `dtrace`
- `kernel-uek`
- `ocfs2-tools`
- `oracle-indexhtml`
- `oraclelinux-release`
- `oraclelinux-release-el9`
- `oracle-logos`

#### Added Source Packages for AppStream by Oracle

The following source packages have been added to AppStream by Oracle:

- `dnf-plugin-spacewalk`
- `dtrace`
- `pyOpenSSL`
- `python3-dnf-plugin-ulninfo`
- `python-hwdata`
- `rhn-client-tools`
- `rhnlib`
- `rhnsd`

#### Modified BaseOS Source Packages

The following source packages from the BaseOS upstream release have been modified:

- `autofs`
- `binutils`
- `chkconfig`
- `chrony`
- `cockpit`
- `coreutils`
- `dbus`
- `dnf`
- `dnf-plugins-core`
- `dracut`
- `efibootmgr`
- `efi-rpm-macros`
- `firewalld`
- `fwupd`
- `gcc`
- `glibc`
- `grub2`
- `grubby`
- `ima-evm-utils`
- `iproute`
- `iscsi-initiator-utils`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `krb5`
- `libdnf`
- `libkcapi`
- `libreport`
- `libtirpc`
- `linux-firmware`
- `mcelog`
- `microcode_ctl`
- `NetworkManager`
- `nvmetcli`
- `os-prober`
- `polkit`
- `python-configshell`
- `redhat-release`
- `rpm`
- `selinux-policy`
- `shim`
- `sos`
- `sssd`
- `systemd`
- `tuned`
- `vim`

#### Modified AppStream Source Packages

The following source packages from the AppStream upstream release have been modified:

- `anaconda`
- `anaconda-user-help`
- `binutils`
- `boom-boot`
- `buildah`
- `ceph`
- `chkconfig`
- `clang`
- `cloud-init`
- `cockpit`
- `cockpit-composer`
- `cockpit-session-recording`
- `compat-libgfortran-48`
- `containers-common`
- `container-tools`
- `crash`
- `cups-filters`
- `dbus`
- `ddiskit`
- `delve`
- `dotnet6.0`
- `dracut`
- `efi-rpm-macros`
- `eth-tools`
- `fapolicyd`
- `firefox`
- `firewalld`
- `fwupd`
- `galera`
- `gcc`
- `gdb`
- `glibc`
- `gnome-shell-extension-background-logo`
- `httpd`
- `initial-setup`
- `ipa`
- `iscsi-initiator-utils`
- `krb5`
- `ksh`
- `libblockdev`
- `libguestfs`
- `libreoffice`
- `libreport`
- `libreswan`
- `libvirt`
- `libxslt`
- `lorax`
- `lorax-templates-rhel`
- `mecab-ipadic`
- `mpich`
- `munge`
- `NetworkManager`
- `nginx`
- `opa-ff`
- `opa-fm`
- `OpenIPMI`
- `openscap`
- `open-vm-tools`
- `osbuild-composer`
- `oscap-anaconda-addon`
- `osinfo-db`
- `PackageKit`
- `perl-XML-Parser`
- `pesign`
- `pki-core`
- `plymouth`
- `podman`
- `polkit`
- `pykickstart`
- `python-blivet`
- `python-rtslib`
- `rear`
- `rhel-system-roles`
- `rpm`
- `rpmdevtools`
- `sanlock`
- `scap-security-guide`
- `selinux-policy`
- `sendmail`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `systemd`
- `systemtap`
- `thunderbird`
- `tog-pegasus`
- `tuned`
- `vim`
- `virt-manager`
- `virt-p2v`
- `virt-v2v`
- `WALinuxAgent`
- `xsane`

#### Modified Source Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `anaconda`
- `ceph`
- `crash`
- `cups-filters`
- `dotnet6.0`
- `dovecot`
- `fwupd`
- `gcc`
- `glibc`
- `ipa`
- `java-11-openjdk`
- `java-1.8.0-openjdk`
- `kmod`
- `libbpf`
- `libdnf`
- `libguestfs`
- `libreoffice`
- `libvirt`
- `mpich`
- `munge`
- `NetworkManager`
- `nginx`
- `ocaml`
- `OpenIPMI`
- `openscap`
- `PackageKit`
- `python-packaging`
- `python-psutil`
- `sanlock`
- `sendmail`
- `sssd`
- `tog-pegasus`
- `virt-v2v`

#### Removed BaseOS Source Packages

The following source packages from the BaseOS upstream release have been removed:

- `kpatch`
- `subscription-manager`

#### Removed AppStream Source Packages

The following source packages from the AppStream upstream release have been removed:

- `ansible-collection-microsoft-sql`
- `ansible-collection-redhat-rhel_mgmt`
- `insights-client`
- `libica`
- `nmap`
- `realtime-tests`
- `redhat-indexhtml`
- `redhat-logos`
- `rhc`
- `rhc-worker-playbook`
- `toolbox`
- `virtio-win`
- `virt-who`