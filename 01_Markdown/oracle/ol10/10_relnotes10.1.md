---
title: "Release Notes for Oracle Linux 10.1"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol10"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux 10

Release Notes for Oracle Linux 10.1

G44070-04

January 2026

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 10 Release Notes for Oracle Linux 10.1

G44070-04

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2025, 2026, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10.1-Preface.html -->

## Preface

[Oracle Linux 10: Release Notes for Oracle Linux
10.1](https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/) provides information about the new features
and known issues in the Oracle Linux 10.1 release. The
information applies to both x86\_64 and 64-bit Arm (aarch64) architectures. This document might
be updated after it's released.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-AboutOracleLinux10.html -->

## 1 About Oracle Linux 10

The current Oracle Linux 10 release contains
new features and enhancements that improve performance in different areas including automation
and management, security and compliance, container management, and developer tools. These
enhancements are especially designed to make the OS adaptable to different types of deployment
such as on-premises installations, hybrid deployments that combine on-premises and cloud
installations, and full cloud deployment.

Important:

Upgrading from an Oracle Linux Developer Preview release to its later official version is
not supported. If you're running the Developer Preview version, you must reinstall the
official Oracle Linux release upon its general availability.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10.0-SystemRequirementsandLimitations.html -->

## System Requirements and Limitations

To check whether a specific hardware is supported on the current Oracle Linux 10 release,
see the Hardware Certification List at <https://linux.oracle.com/hardware-certifications>. Note that as hardware becomes
available and validated, the hardware is added to the list.

CPU, memory, disk, and file system limits for all Oracle Linux releases are described in
[Oracle Linux: Limits](https://docs.oracle.com/en/operating-systems/oracle-linux/limits/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-AvailableArchitectures.html -->

## Available Architectures

The release is available for installation on the following
platforms:

- Intel® 64-bit (x86\_64) (x86-64-v3)
- AMD 64-bit (x86\_64) (x86-64-v3)
- 64-bit Arm (aarch64) (Arm v8.0-A)

  The Arm platform runs only with Unbreakable Enterprise Kernel Release (UEK).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10.1-ShippedKernels.html -->

## Shipped Kernels

For the x86\_64 platform, Oracle Linux 10 ships with the following default kernel packages:

- `kernel-uek-6.12.0-105.51.5` (Unbreakable
  Enterprise Kernel 8 Update 1 (UEK 8U1))

  For new installations, the UEK kernel is automatically
  enabled and installed. It also becomes the default kernel on
  first boot.
- `kernel-6.12.0-124.8.1` (Red Hat
  Compatible Kernel (RHCK))

For the aarch64 platform, Oracle Linux ships with the UEK kernel only.

The Oracle Linux release is tested as a bundle, as shipped on the installation media image.
When installed from the installation media image, the kernel's version included in the image
is the minimum version that's supported. Downgrading kernel packages isn't supported, unless
recommended by Oracle Support.

For more information about kernel availability on Oracle Linux 10 releases, see <https://docs.oracle.com/en/operating-systems/oracle-linux/10/boot/oracle_linux10_kernel_version_matrix.html>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol-AbouttheUnbreakableEnterpriseKernel.html -->

## About the Unbreakable Enterprise Kernel

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol-Compatibility.html -->

## User Space Compatibility

Oracle Linux maintains user space compatibility with Red Hat Enterprise Linux (RHEL) that's
independent of the kernel version that underlies the OS. Existing applications in user space
continue to run unmodified on UEK R8 with no required recertifications for Oracle Linux
certified applications.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-ObtainingInstallationImages.html -->

## Obtaining Installation Images

The following installation images for the current Oracle Linux 10 release are available:

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

To prepare a downloaded image for installing Oracle Linux, see [Oracle Linux 10: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/10/install/).

Note:

Aside from installation ISO images, you can also use Oracle Linux images to create compute
instances on Oracle Cloud Infrastructure. For information about these images, see
the release notes for the specific image that you're using on the [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/images/) page.

To use Oracle Linux on Oracle Cloud Infrastructure, see <https://docs.oracle.com/iaas/oracle-linux/home.htm>.

For information about the available ISO images for the three most recent updates to the Oracle
Linux releases, see <https://yum.oracle.com/oracle-linux-isos.html>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-PreparingInstallationMedia.html -->

## Preparing Installation Media

Before you can use an ISO image to install Oracle Linux, you must first store it on bootable
installation media, such as the following:

- [USB Flash Drive](ol10-PreparingInstallationMedia.html#flash-drives)
- [DVD or CD](ol10-PreparingInstallationMedia.html#dvd-cd "Because of storage limits, optical media such as CDs or DVDs might not have capacity to accommodate most installation ISO images. However they can be used to store the boot ISO image.")

### USB Flash Drive

You can install Oracle Linux by using a boot image on portable devices such as a USB flash
drive or an SD card, if the system's firmware can boot from those devices.

To create a bootable drive, use the `dd` or
`xorriso-dd-target` command. Or, use a separate third-party utility to
write the ISO image to a drive. See, for example, [Create USB Installation Media for Oracle
Linux with Fedora Media Writer](https://docs.oracle.com/en/learn/usb-media/).

Caution:

This procedure destroys any existing data on the drive. Ensure that you specify the
correct device name for the USB drive on the system.

1. Insert a USB flash drive into an Oracle Linux system.
2. Use the `xorriso-dd-target` command to list available block devices
   and to identify likely candidate devices for use.

   ```
   xorriso-dd-target -with_sudo -list_all
   ```

   The command presents a password prompt as it uses sudo to access all devices on the
   system. Output similar to the following is displayed:

   ```
   sda : YES : usb+ has_vfat+ : SanDisk Cruzer Switch 
   nvme0n1 : NO  : not_usb- has_vfat+ has_xfs- has_crypto_LUKS- has_swap- :  PM9A1 NVMe Samsung 512GB
   ```

   The command identifies removable block devices with disposable content. In the example
   output, the command identified a USB device at `/dev/sda`, that could
   be used to write an ISO image.
3. Ensure that any file systems on the device are unmounted.

   For example, to unmount the first partition on `/dev/sda`:

   ```
   sudo umount /dev/sda1
   ```
4. Write the contents of the ISO image file to the USB device.

   Do one of the following to write the ISO image file to the USB device:

   - Use the `dd` command
     directly:

     ```
     sudo dd if=./full_image.iso of=/dev/sda bs=512k
     ```
   - Use the `xorriso-dd-target` command to guide you through this
     process:

     ```
     xorriso-dd-target -with_sudo -plug_test -DO_WRITE -image_file ./full_image.iso
     ```

     The command guides you through testing for appropriate devices and finally prompts
     you to select and approve writing to the device. Example output
     follows:

     ```
     sudo /bin/lsblk seems ok.

     Caused by option -plug_test: Attempt to find the desired device
     by watching it appear after being plugged in.

     Step 1:
     Please make sure that the desired target device is plugged _out_ now.
     If it is currently plugged in, make sure to unmount all its fileystems
     and then unplug it.
     Press the Enter key when ready.

     Found and noted as _not_ desired:  nvme0n1  

     Step 2:
     Please plug in the desired target device and then press the Enter key.

     Waiting up to 10 seconds for a new device to be listed .... found: sda
     Now waiting 5 seconds to let it settle .........
     Found and noted as desired device:  sda

     sda : YES : usb+ has_vfat+ : SanDisk Cruzer Switch 

     Step 3:
     Last chance to abort. Enter the word 'yes' to start REAL WRITING.
     yes
     Looking for mount points of sda:
     Performing:
       sudo /bin/dd if=/dev/zero of=/dev/'sda' bs=512 seek='30595071' count=1 status=none
       sudo /bin/dd if='OracleLinux.iso' of=/dev/'sda' bs=1M status=progress oflag=dsync ; sync
     ```

The USB flash drive is now ready to be used to boot a system and start the installation.

### DVD or CD

Because of storage limits, optical media such as CDs or DVDs might not have capacity
to accommodate most installation ISO images. However they can be used to store the boot ISO
image.

1. Insert an empty recordable CD or DVD into the CD or DVD writer device.
2. Open a terminal and use `cdrecord` to write the ISO file to
   the device.

   To write the downloaded ISO image file to a CD or DVD, use a command such as
   `cdrecord`, for example:

   ```
   sudo cdrecord -v -eject speed=16 dev=/dev/sr0 file_name.iso
   ```

   To display the device that corresponds to the CD or DVD writer, use the
   `cdrecord --devices` command.

The CD or DVD is now ready to be used to boot a system and start the installation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-UpgradingFromPreviousOracleLinuxReleases.html -->

## Upgrading From Previous Oracle Linux Releases

You can upgrade an Oracle Linux 9 system to the Oracle Linux 10 release by using
the `leapp` utility.

For step-by-step instructions and information about any known issues that might arise when
upgrading the system, see [Oracle Linux 10: Upgrading Systems With Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/10/leapp/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-UpgradingFromOracleLinuxUpdateReleases.html -->

## Upgrading From Previous Oracle Linux Update Releases

You can upgrade an Oracle Linux 10 system from a previous update level to the current update level by
running the `sudo dnf update` command.

After performing a system update where many packages are updated, we recommend that you
reboot the system. System functionality might become unstable if core packages are
updated and the system isn't restarted to load the most recent updates. You can check
whether a system requires a restart by running:

```
dnf needs-restarting -r
```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-NewFeaturesandChanges.html -->

## 2 New Features and Changes

Unless indicated otherwise, the following new features, major enhancements, bug fixes, and
other changes that are introduced in Oracle Linux 10.1 apply to both the x86\_64
and 64-bit Arm (aarch64) platforms.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-features-Installation.html -->

## Installation and Boot

The following features, enhancements, and changes related to installation and boot are
introduced in Oracle Linux 10.1 release.

### New Boot Menu Entry for `fips=1` Added to ISO Installations

A new boot menu entry enables the `fips=1` kernel option for ISO installations
to simplify FIPS compliance.

The DVD and Boot ISO image installations provide a new boot menu entry for setting the
`fips=1` kernel boot option. Enabling FIPS mode during the Oracle Linux
installation ensures that the system generates all keys with FIPS-approved algorithms and
continuous monitoring tests in place. By using this boot option, you start the installation
with the `fips=1` kernel parameter to target the system's compliance with
Federal Information Processing Standards (FIPS) 140 requirements.

### Logical Volumes in `/etc/fstab` Use UUID

After installation with Oracle Linux 10.1, logical volume (LV) devices are written in
`/etc/fstab` using their UUIDs in the `fs_spec`
field. This change makes configurations more consistent and reliable, especially during
renaming, re-encryption, or reprovisioning of storage devices.

- Supports LV or group renaming without manual `/etc/fstab` edits.
- Keeps mount configuration portable across diverse environments.
- Preserves correctness after LUKS re-encryption or device-mapper path changes.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-features-Kernel.html -->

## Kernel and System Libraries

The following notable features, enhancements, and changes apply to the Red Hat Compatible
Kernel (RHCK) that's shipped with Oracle Linux 10.1.

### Perf Tool Updated to Version 6.15

The `perf` tool and kernel backend are updated to version 6.15 with additional enhancements and support for new hardware, extended python-perf features, and improved reporting.

See <https://lore.kernel.org/lkml/20250328063228.3824573-1-namhyung@kernel.org/> for more information.

### eBPF Subsystem Updated to Version 6.14

The eBPF subsystem in RHCK is updated to version 6.14, introducing various upstream enhancements from the Linux kernel v6.14.

### Crash Utility Updated to Version 9.0.0

The `crash` package, which provides a kernel analysis utility for live systems
and various types of dump files, is updated to upstream version 9.0.0. This version provides
several fixes and enhancements, including:

- The internal gdb database is updated to version 16.2.
- The crash utility now supports cross-compilations.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-features-CompilersandDevTools.html -->

## Compilers and Development Tools

The following features, enhancements, and changes related to compilers and development tools
are introduced in Oracle Linux 10.1.

### `dyninst` Framework Updated to 13.0.0

`dyninst` 13.0.0 improves AMD GPU binary support and x86 instruction/C++ DWARF
parsing for better runtime instrumentation.

### SystemTap Updated to Version 5.3

SystemTap 5.3 features multithreaded parsing for faster initialization.

See <https://sourceware.org/systemtap/wiki/SystemTapReleases> for more information.

### `elfutils` Updated to Version 0.193

`elfutils` is updated to version 0.193.

### `valgrind` Upgraded to Version 3.25.1

`valgrind` is upgraded to 3.25.1.

See <https://valgrind.org/docs/manual/dist.news.html> for more information.

Oracle Linux 10.1 splits `valgrind` into subpackages for core, scripts, GDB
integration, and documentation, providing selective installation of required components.

This modular approach reduces footprint and improves management for users focusing on
specific `valgrind` features in Oracle Linux development workflows.

### `llvm-toolset` Updated to LLVM 20

The `llvm-toolset` is upgraded to LLVM 20.

See <https://releases.llvm.org/20.1.0/docs/ReleaseNotes.html>.

### GCC Toolset 15 is now Available

Oracle Linux 10.1 provides `gcc-toolset-15`, which includes current GCC and related utilities so you can build, test, and deploy applications using the latest compiler technology.

### `gdb` Updated to Version 16.3

Oracle Linux 10.1 updates `gdb` to version 16.3.

See <https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;a=blob_plain;f=gdb/NEWS;hb=gdb-16.3-release> for more information.

### Rust Toolset Updated to Version 1.88.0

Oracle Linux 10.1 includes Rust Toolset version 1.88.0, which brings Rust 2024 Edition, let chains, intrinsics in safe Rust, async closures, trait upcasting, and Cargo cache cleaning.

See <https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/> for more information.

Rust Toolset is a rolling Application Stream. Oracle only supports the latest version. For
more details, see [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

### OpenJDK 25 Is Available

Oracle Linux 10.1 now provides OpenJDK 25, delivering the latest long-term support Java platform enhancements and new features.

See <https://openjdk.org/projects/jdk/25/> for
more information.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-features-FileSystemsandStorage.html -->

## File Systems and Storage

The following features, enhancements, and changes related to file systems and storage are
introduced in Oracle Linux 10.1.

### Multipathd Supports File-Based Sockets for Container Communication

Multipathd can use file-based sockets for communication from containers to the host daemon.
The `multipathd` daemon listens on a socket file at
`/run/multipathd.socket` and also the abstract namespace socket. You can
bind-mount the socket into a container, letting it interact with the host's
`multipathd` daemon more easily.

This feature improves container integration for storage management, so you can monitor and configure multipath devices from inside containers without extra networking. Device paths stay consistent across container boundaries.

Mount `/run/multipathd.socket` in the container and use standard multipath
tools, such as `multipath -ll`, to query or manage devices from within the
container.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-features-HighAvailabilityandClusters.html -->

## High Availability and Clusters

The following features, enhancements, and changes related to high availability are introduced
in Oracle Linux 10.1.

### `IPaddr2` Resource Agent Detects Interface Link Failures

The `IPaddr2` resource agent checks the link state of network interfaces and
correctly handles failover if a network interface is down, improving cluster reliability. This
feature is enabled by default.

Administrators can disable link monitoring and automatic failover by setting
`check_link_status=false` in the resource configuration.

### `fence_sbd` Agent Automatically Detects SBD Devices

The `fence_sbd` agent can automatically retrieve the SBD device configuration
if you don't explicitly specify the SBD device path when using the devices parameter. If you
omit the parameter, the agent gets the configuration from the `SBD_DEVICE`
variable in `/etc/sysconfig/sbd`.

This enhancement simplifies fencing setup in Pacemaker clusters that use SBD, reduces
configuration errors, and streamlines deployment for standard setups.

### `pcs` Warns Users Before Removing the Last Fencing Device

`pcs` prevents accidental removal of the last cluster fencing mechanism,
displaying an error message to avoid leaving the cluster in an unsupported state. For
example:

```
Error: Requested action lefts the cluster with no enabled means to fence nodes, 
resulting in the cluster not being able to recover from certain failure conditions, 
use --force to override
```

If you use the `--force` option, you can override the block on this action,
but a warning message is displayed:

```
Warning: Requested action lefts the cluster with no enabled means to fence nodes, 
resulting in the cluster not being able to recover from certain failure conditions
Warning: Resources are not going to be stopped before deletion, this may result in 
orphaned resources being present in the cluster
```

### `pcs alert config` Provides Multiple Output Formats

The `pcs alert config` subcommand provides `text`,
`json`, and `cmd` output formats, which can be controlled by
using the `--output-format` option. JSON and command output make alert
configuration easier to automate and replicate.

### `pcs cluster rename` Command Available for Renaming Clusters

Clusters can be renamed with the `pcs cluster rename <new-name>`
command, reducing the need for manual steps. The command updates all relevant cluster
properties so the cluster continues working seamlessly after the rename.

### `pcs node attribute` and `pcs node utilization` Commands Include Multiple Output Formats

Node attribute and utilization reporting in `pcs` now include
`text`, `json`, and `cmd` output formats for
easier scripting and automation. Use the `--output-format` option with
`pcs node` commands to set the output that you need.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-features-Networking.html -->

## Networking

The following features, enhancements, and changes related to networking are introduced in
Oracle Linux 10.1.

### `iproute2` Updated to Version 6.14

The iproute package in Oracle Linux 10.1 is updated to version 6.14.0.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-features-Security.html -->

## Security

The following features, enhancements, and changes related to security are introduced in
Oracle Linux 10.1.

### Post-Quantum Cryptography Enabled by Default in System-Wide Crypto Policies

Oracle Linux 10.1 system-wide cryptographic policies now enable post-quantum (PQ)
cryptography algorithms by default in all predefined policy sets.

Notable changes include:

- Hybrid Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) and pure
  Module-Lattice-Based Digital Signature Standard (ML-DSA) PQ cryptographic algorithms are
  enabled in LEGACY, DEFAULT, and FUTURE policies with the highest priorities.
- You can use the NO-PQ subpolicy to disable the PQC algorithms.
- The TEST-PQ subpolicy can be used to enable pure ML-KEM in OpenSSL.
- The FIPS cryptographic policy enables hybrid ML-KEM and pure ML-DSA PQ cryptographic
  algorithms.
- OpenSSL group selection give PQ groups higher priority than classical ones. Disable all PQ
  groups to revert to previous behavior.
- The PQC algorithms are enabled for the Sequoia PGP tool in all policies.
- ML-DSA algorithms are enabled for GnuTLS TLS connections by default, and you can control
  them through the `MLDSA44`, `MLDSA65`, and
  `MLDSA87` values.
- The ML-DSA-44, ML-DSA-65, and ML-DSA-87 PQC algorithms are enabled for NSS TLS connections
  in all cryptographic policies.
- The `mlkem768x25519`, `secp256r1mlkem768`, and
  `secp384r1mlkem1024` hybrid ML-KEM groups are enabled for NSS TLS
  negotiations.

### AD-SUPPORT-LEGACY Cryptography Subpolicy Re-Added

The `AD-SUPPORT-LEGACY` cryptographic subpolicy is restored in Oracle Linux 10.1 for compatibility with legacy Active Directory environments that require RC4 encryption.

### `openssl` Updated to Version 3.5

With Oracle Linux 10.1, OpenSSL is updated to version 3.5 and includes ML-KEM, ML-DSA,
SLH-DSA, QUIC transport, and additional post-quantum and modern cryptography features.

You can now improve security for TLS connections and cryptographic operations in Oracle Linux
environments, preparing systems for a quantum-safe future.

See <https://github.com/openssl/openssl/blob/openssl-3.5/CHANGES.md#openssl-35> for more information.

### OpenSSL SSLKEYLOGFILE Environment Variable For Debugging

With Oracle Linux 10.1, use the SSLKEYLOGFILE environment variable to instruct OpenSSL to log
TLS connection secrets to a file.

Caution:

Only enable this feature in test or debug environments. Logging key material can
introduce security risks.

### OpenSSL 3.5 Uses Standard Private Key Format for ML-KEM and ML-DSA

Oracle Linux 10.1 requires ML-KEM and ML-DSA private keys to use the standard format in OpenSSL 3.5. Convert old keys using `openssl pkcs8`.

For example, use the following command to convert an ML-KEM key.

```
openssl pkcs8 -in mlkem.key -nocrypt -topk8 -out mlkem.new.key
```

Verify that the newly generated key is valid and contains the same content as the original key:

```
diff <(openssl pkey -in mlkem.new.key -text -noout) <(openssl pkey -in mlkem.key -text -noout)
```

The same approach applies to converting and verifying an ML-DSA key.

### NSS Updated to 3.112

With Oracle Linux 10.1, the NSS cryptographic toolkit packages are updated to upstream version 3.112 with many improvements and fixes.

See <https://firefox-source-docs.mozilla.org/security/nss/releases/index.html> for more information.

Notable changes include:

- This update adds support for the Module-Lattice-Based Digital Signature Algorithm
  (ML-DSA), a post-quantum cryptography (PQC) standard.
- You can take advantage of hybrid SSL support with the MLKEM1024 key encapsulation
  mechanism.

### `libreswan` Updated to Version 5.3

The `libreswan` IPsec implementation is updated to version 5.3, delivering bug fixes and feature improvements.

See <https://download.libreswan.org/CHANGES> for
more information.

### `gnutls` Updated to Version 3.8.10

The `gnutls` package is updated to version 3.8.10, adding certificate compression, expanded ML-DSA algorithm support, and support for PKCS#11 module overrides.

See <https://lists.gnupg.org/pipermail/gnutls-help/2025-July/004883.html> for more information.

- Certificate compression options and algorithms can now be set with
  `cert-compression-alg` configuration option in the gnutls priority
  file.
- TLS X.509 certificates with ML-DSA keys for TLS 1.3. ML-DSA signature algorithms,
  ML-DSA-44, ML-DSA-65, and ML-DSA-87, can digitally sign TLS handshake messages.
- PKCS#11 provider override as tech preview. Use the `[provider]` section
  in the system-wide config to specify the path and pin for the module.

### Sequoia Updated With OpenPGP V6 Support

The Sequoia tools in Oracle Linux 10.1, `sequioa-sq` and
`sequioa-sqv`, handle post-quantum cryptography keys, enabling
quantum-resistant digital signatures. Also, the `rpm-sequoia` package can
verify RPM packages with post-quantum cryptographic algorithms and can now verify verification
of OpenPGP v6 signatures when running the `rpm -Kv` command.

For example, you can generate an ML-DSA key using Sequoia as follows:

```
sq key generate --name "Test key" --own-key --cipher-suite mldsa65 --profile rfc9580
sq key list
 - A3C077C3A6A6067E7B457DDCF7E80097AC929B341C8499841A3ACFB4342A81FF
   - user ID: Test key (authenticated)
[...]
```

To sign an RPM using Sequoia keys, first update the /etc/rpm/macros with the Sequoia RPM
signing macro.

```
sudo cp /usr/share/doc/rpm/macros.rpmsign-sequoia /etc/rpm
cat /etc/rpm/macros
%_gpg_name A3C077C3A6A6067E7B457DDCF7E80097AC929B341C8499841A3ACFB4342A81FF

rpmsign --rpmv6 --resign wget-1.24.5-5.el10.x86_64.rpm
wget-1.24.5-5.el10.x86_64.rpm:
```

To verify an RPM package and view the OpenPGP V6 signature:

```
rpm -Kv wget-1.24.5-5.el10.x86_64.rpm
wget-1.24.5-5.el10.x86_64.rpm:
    Header V6 ML-DSA-65+Ed25519/SHA512 Signature, key ID 250ac5d3: OK
    Header SHA256 digest: OK
    Header SHA1 digest: OK
    Payload SHA256 digest: OK
    MD5 digest: OK
```

### SELinux Policy Updated to Version 42.1

SELinux policy packages are updated to version 42.1, delivering multiple improvements and fixes, including added types for `systemd` generators.

### SELinux `-extra` Policy Modules for EPEL Moved to CRB Repository

Policy modules only used for EPEL packages have been moved from `selinux-policy` to `selinux-policy-targeted-extra` and `selinux-policy-mls-extra` in the CodeReady Linux Builder repository, improving policy management and automatic EPEL enablement.

### SELinux Permissive Mode Removed Services

SELinux types for `gnome_remote_desktop_t`, `pcmsensor_t`, and
`samba_bgqd_t` are now enabled in enforcing mode, improving security for
these services. Previously, these services were configured to run in permissive mode.

### SELinux Policy Updated for `qgs` Daemon

The SELinux policy adds a new `qgs_t type` and access rules for the
`qgs` daemon, which lets the daemon operate securely in
TDX confidential VM environments.

With these rules, SELinux can control access for `qgs` in Oracle Linux,
strengthening security for confidential computing deployments.

### SELinux Policy Confines Additional Services

SELinux policy now confines `switcheroo-control` and `tuned-ppd` services, removing their `unconfined_service_t` label and improving system security.

### `setroubleshoot-server` No Longer Requires Initscripts

The `setroubleshoot-server` SELinux diagnostic tool no longer uses `/sbin/service` in its scriptlets and instead interacts directly with `auditctl`, simplifying dependencies.

### SCAP Security Guide Updated to Version 0.1.78

The SCAP Security Guide (SSG) packages are updated to the upstream version 0.1.78 and provide
enhancements and bug fixes such as the following:

- Oracle Linux 9 `stig` and `stig_gui` profiles are aligned
  with DISA STIG for Oracle Linux 9 V1R2.

- The `auditd_freq` rule correctly honors the XCCDF variable.
- Added support for drop-in files to systemd coredump rules.
- Rules allow white spaces around the equal sign in systemd configuration.
- Improved detection of the retry option in password complexity.

### OpenSSH Ignores Invalid RSA Hostkeys in `known_hosts`

OpenSSH is updated to ignore RSA bad hostkeys in `known_hosts` that are
invalid because of an unsupported length. Instead of failing, the SSH connection proceeds and
uses valid keys instead.

### `fips-provider-next` Package Added

The `fips-provider-next` package introduces the next version of the FIPS
provider for OpenSSL. This package might be submitted to the National Institute of Standards
and Technology (NIST) for future validation. The `openssl-fips-provider`
remains the validated FIPS provider.

To switch to the `fips-provider-next`, run the following command:

```
sudo dnf swap openssl-fips-provider fips-provider-next
```

The `fips-provider-next` package is available as a technical preview.

### `auditd` Includes Cron-Based Log Rotation Example

Oracle Linux 10.1 includes `auditd.cron` to help set up time-based `auditd` log rotation. This provides administrators with a clear, documented example configuration for rotating audit logs by schedule.

### `openCryptoki` Updated to Version 3.25.0

Version 3.25.0 of the `openCryptoki` packages is now available.

See <https://github.com/opencryptoki/opencryptoki/releases/tag/v3.25.0> for more information.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-features-Cockpit.html -->

## Cockpit Web Console

The following features, enhancements, and changes related to the Cockpit web console are introduced in Oracle Linux 10.1.

### `cockpit` Updated to Version 344

The `cockpit` web console
is updated to version 344, notable enhancements include:

- New PatternFly 6-based UI and style.
- Improved graphical VNC/serial consoles.
- IPv6 WireGuard VPN support in Networking.
- Branding support using branding.css.

### Separate `cockpit-ws-selinux` Subpackage for Cockpit SELinux Policy

The SELinux policy for `cockpit_ws` processes is now provided in the dedicated
`cockpit-ws-selinux` package, avoiding unnecessary
`selinux_policy` dependencies and ensuring Cockpit works properly on systems
with or without SELinux.

For more information, see the `cockpit_ws_selinux(8)` man page.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-features-Containers.html -->

## Containers

The following features, enhancements, and changes related to containers are introduced in
Oracle Linux 10.1.

### Container Tools Packages Updated

The Container Tools RPM meta-package is now updated and includes Podman v5.6, Buildah
v1.41.0, and Skopeo 1.20.0. The package installs `crun` instead of
`runc`.

We recommend doing a full `dnf update` before installing or updating the
container tools packages, because some SELinux policy updates and related dependencies are
required.

See <https://github.com/containers/podman/releases>, <https://github.com/containers/buildah/releases>, and <https://github.com/containers/skopeo/releases> for more information.

### The ADD and COPY Instructions Can Use the `--link` Option

Buildah and Podman can use the `--link` option for ADD and COPY instructions
in Containerfiles, which causes the new content to be added as its own layer in the built
image.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-DeprecatedFeatures.html -->

## 3 Deprecated Features

This chapter lists features and functionalities that are deprecated in Oracle Linux 10. While
these features might be included and operative in the release, support isn't guaranteed in
future major releases. Thus, these features must not be used in new Oracle Linux 10
deployments.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-deprecated-Installation.html -->

## Installation

The following installation related features and functionalities are deprecated in Oracle
Linux 10.

### Cockpit Composer

The `cockpit-composer` package is deprecated and will be removed in future
major Oracle Linux releases. Use `cockpit-image-builder` instead.

### SquashFS

The `squashfs` package is deprecated and will be removed in a future major
Oracle Linux release. Consider using EROFS as an alternative solution.

### Gdisk

`gdisk` is deprecated from the `boot.iso` image type. Other
tools, such as `parted`, are available for handling GPT disks.

### Module Kickstart Command

The module kickstart command is deprecated due to Anaconda's deprecated support for DNF
modularity.

### Inst.gpt Boot Option

The `inst.gpt` boot option is deprecated and will be removed in future
releases. Use the `inst.disklabel` boot option instead.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-deprecated-Compilers.html -->

## Compilers and Development Tools

### Utmp and Utmpx Interfaces

The `utmp` and `utmpx` interfaces provided by the
`glibc` library are deprecated and will be removed in Oracle Linux 11.

### Nodejs 18 Deprecation

The `nodejs-18` and `nodejs-18-minimal` container images are
deprecated and will no longer receive feature updates. Use `nodejs-22` and
`nodejs-22-minimal` instead.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-deprecated-Networking.html -->

## Networking

The following network related features and functionalities are deprecated in Oracle Linux
10.

### Ipset

Ipset is unmaintained and planned to be removed in a future major release. Use nftables sets
functionality as an alternative.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-deprecated-Security.html -->

## Security

The following security related features and functionalities are deprecated in Oracle Linux
10.

### ENGINE API in OpenSSL

The Engine API in OpenSSL is deprecated and will be removed in a future major release. No new
applications should be built using the Engine API.

### Crypto Policies

The `allow-rsa-pkcs1-encrypt` option is set to false for GnuTLS in all
system-wide cryptographic policies (DEFAULT, FUTURE, and FIPS).

### HMAC-SHA-1 in FIPS Mode

The HMAC-SHA-1 cryptographic algorithm is deprecated in FIPS mode and may be removed in a
future release.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-deprecated-FileSystemsandStorage.html -->

## File Systems and Storage

The following features and functionalities related to file systems and storage are deprecated
in Oracle Linux 10.

### SquashFS

The `squashfs` package is deprecated and will be removed in a future major
Oracle Linux release. Consider using EROFS as an alternative solution.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-deprecated-HighAvailability.html -->

## High Availability and Clusters

The following features and functionalities related to high availability and clusters are deprecated
in Oracle Linux 10.

### Deprecated High Availability Add-On Features

The following features have been deprecated in Oracle Linux 10 and will be removed in the next
major release.

- Specifying rules as multiple arguments. Use a single string argument instead.
- Specifying score as a standalone value in `pcs constraint location add`
  and `pcs constraint colocation add`. Use `score=value` instead.

Other deprecations:

- The `--group`, `--after`, and
  `--before` options used with the `pcs resource
  create` command are deprecated in favor of `group`,
  `after`, and `before`. To start using the
  replacement flags, you can run the `pcs resource create` command
  with the `--future` option.

  See the `pcs(8)` manual page for more information.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-deprecated-Containers.html -->

## Containers

The following features and functionalities related to container technologies are deprecated
in Oracle Linux 10.

### Runc Container Runtime

The `runc` container runtime is removed. The default container runtime is
`crun`.

### Tzdata Package

The `tzdata` package is no longer installed by default in the minimal container
images.

### Podman v5.0 Deprecations

The following features are deprecated in Podman v5.0:

- The system connections and farm information stored in the
  `containers.conf` file.
- The `slirp4netns` network mode.
- The `containernetworking-plugins` package.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-deprecated-Virtualization.html -->

## Virtualization

The following virtualization related features and functionalities are deprecated in Oracle
Linux 10.

### Virt Manager

The Virtual Machine Manager application (`virt-manager`) is deprecated. The
Cockpit web console is intended to become its replacement in a subsequent release.

### Libvirtd

The monolithic `libvirt` daemon (`libvirtd`) is deprecated and
will be removed in a future major release. Use the newly introduced modular `libvirt`
daemons instead.

### SecureBoot Image Verification

Performing SecureBoot image verification using SHA1-based signatures on UEFI (PE/COFF)
executables is deprecated. Use signatures based on the SHA-2 algorithm or later instead.

### Virtual Floppy Driver

The `isa-fdc` driver, which controls virtual floppy disk devices, is deprecated
and will become unsupported in a future release.

### Qcow2-v2 Image Format

The qcow2-v2 format for virtual disk images is deprecated and will become unsupported in a
future major release. Use qcow2-v3 instead.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-deprecated-Packages.html -->

## Deprecated Packages

The following packages are deprecated in Oracle Linux 10:

- `daxio`
- `gvvisor-tap-vsock-gvforwarder`
- `libpmem`
- `libpmem2`
- `libpmemblk`
- `libpmemlog`
- `libpmemobj`
- `libpmemobj-cpp`
- `libpmempool`
- `libslirp`
- `nvml`
- `pmempool`
- `pmreorder`
- `sdl2-compat`
- `wget`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-RemovedFeatures.html -->

## 4 Removed Features

This chapter lists features and functionalities that are removed in Oracle Linux 10 and which might have been available in previous Oracle Linux releases.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-removed-installer-and-image-creation.html -->

## Installer and Image Creation

The following installation related features and functionalities are removed in Oracle
Linux 10.

### Authconfig Commands

The `auth` and `authconfig` Kickstart commands are removed. Use
the `authselect` kickstart command instead.

### Inst.xdriver and Inst.usefbx Options

The `inst.xdriver` and `inst.usefbx` boot options are
removed.

### Capturing Screenshots from the Anaconda GUI

Capturing screenshots from the Anaconda GUI with a global hot key is removed.

### Removed Boot Options

The following boot options are removed: `inst.nompath`,
`dmraid`, and `nodmraid`.

### Automatic Bug Reporting System

The automatic bug reporting system from Anaconda is removed.

### Timezone Kickstart Command Options

The following options of the `timezone` Kickstart command are removed:
`--isUtc`, `--ntpservers`, and `--nontp`.

### Logging Kickstart Command Parameter

The `--level` parameter of the logging kickstart command is removed.

### Support for %anaconda Kickstart Command

The support for the `%anaconda` Kickstart command is removed.

### Pwpolicy Kickstart Command

The `pwpolicy` Kickstart command is removed.

### Support for Adding Additional Repositories from GUI

Support for adding additional repositories from the GUI is removed.

### Support for LUKS Version Selection from Anaconda

Support for selecting the LUKS version from the Manual Installation screen is removed.

### Initial-Setup Package

The `initial-setup` package is removed. Use
`gnome-initial-setup` instead.

### Anaconda Built-in Help

The built-in documentation from all Anaconda user interfaces is
removed.

### Teaming Options from the Network Kickstart Command

The `--teamslaves` and `--teamconfig` options used for
configuring team devices in the `network` kickstart command are removed.

### NVDIMM Reconfiguration Support during the Installation Process

Support for reconfiguring NVDIMM devices during the Kickstart and GUI installation is
removed.

### Options from %packages

The `--excludeWeakdeps` and `--instLangs` options used in the
`%packages` section are removed.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-removed-security.html -->

## Security

The following security related features and functionalities are deprecated in Oracle
Linux 10.

### Scap-Workbench

The `scap-workbench` package is removed.

### Oscap-Anaconda-Addon

The `oscap-anaconda-addon` is removed.

### DSA and SEED Algorithms

The DSA and SEED algorithms are removed from the Network Security Services (NSS) cryptographic
library.

### Fips-Mode-Setup

The `fips-mode-setup` command is removed.

### /etc/system-fips

Support for indicating FIPS mode through the `/etc/system-fips` file is
removed.

### TLS HeartBeat

Support for the HeartBeat extension in TLS is removed.

### SRP Authentication

Authentication that uses Secure Remote Password protocol (SRP) in TLS is removed.

### Keylime HTTP

The Keylime components no longer support the HTTP protocol for revocation notification
webhooks.

### DEFAULT Cryptographic Policy

TLS ciphers that use the RSA key exchange are no longer accepted in the
`DEFAULT` system-wide cryptographic policy.

### Ca-Certificates Trust Store

The `/etc/pki/tls/certs` trust store is converted to a different
format.

### LEGACY Cryptographic Policy

The `LEGACY` system-wide cryptographic policy no longer allows creating or
verifying signatures that use SHA-1 in TLS contexts.

### Pam\_Ssh\_Agent\_Auth

The `pam_ssh_agent_auth` package is removed.

### OpenSSL SHA-1 in TLS

OpenSSL does not accept the SHA-1 algorithm at `SECLEVEL=2` in TLS.

### Stunnel OpenSSL ENGINE API

The `stunnel` TLS offloading and load-balancing proxy no longer supports the
previously deprecated OpenSSL ENGINE API.

### OpenSSL Engines

OpenSSL Engines are removed from upstream.

### Libsss\_Simpleifp Subpackage

The `libsss_simpleifp` subpackage is removed.

### SSSD Files Provider

The SSSD files provider is removed.

### Ad-Allow-Remote-Domain-Local-Groups Option

The `ad_allow_remote_domain_local_groups` option is removed from SSSD.

### Reconnection\_Retries Option

The `reconnection_retries` option is removed from the
`sssd.conf` file in SSSD.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-removed-software-management.html -->

## Software Management

The following software management related features and functionalities are deprecated in Oracle
Linux 10.

### Libreport Library

Support for the `libreport` library is removed from DNF.

### Dnf Debug Plug-in

The DNF `debug` plug-in is removed from the `dnf-plugins-core`
package.

### Numberless %patch Syntax

Using the `%patch` directive without a number specified as a shorthand for
`%patch 0` is removed.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-removed-infrastructure-services.html -->

## Infrastructure Services

The following infrastructure related features and functionalities are removed in Oracle
Linux 10.

### Removed Packages

The following packages are removed:

- `sendmail`
- `redis`
- `dhcp`
- `mod_security`
- `spamassassin`
- `xsane`

### Rename of Gpsd

The `gpsd-minimal` package is renamed to `gpsd`.

### ISC Kea DHCP Server Solution

The ISC Kea DHCP server solution is now available, replacing `ISC DHCP`.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-removed-networking.html -->

## Networking

The following networking related features and functionalities are removed in Oracle Linux
10.

### ATM Encapsulation

Asynchronous Transfer Mode (ATM) encapsulation is removed.

### Dhcp-Client Package

The `dhcp-client` package is removed.

### Mlx4 Driver

The `mlx4` driver for the Mellanox ConnectX-3 network interface
controller (NIC) is removed from RHCK.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-removed-kernel.html -->

## Kernel

The following kernel related features and functionalities are removed in Oracle Linux
10.

### Kexec\_Load System Call

The `kexec_load` system call is removed.

### Crash --log Dumpfile Option

The `crash --log dumpfile` option is deprecated.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-removed-file-systems-and-storage.html -->

## File Systems and Storage

The following file systems and storage related features and functionalities are removed
in Oracle Linux 10.

### Support for NVMe Devices in lsscsi and sg3\_utils

Support for Non-volatile Memory Express (NVMe) devices is removed from the
`lsscsi` and `sg3_utils` packages.

### VDO Sysfs Parameters

The Virtual Data Optimizer (VDO) `sysfs` parameters are removed.

### Support for GFS2 File Systems

Support for GFS2 file systems is removed.

### Support for Block Translation Table Driver

Support for the block translation table driver is removed.

### Nvme\_Core.Multipath Parameter

The `nvme_core.multipath` parameter is removed.

### Md-Faulty and Md-Multipath Modules

The `md-faulty` and `md-multipath` MD RAID kernel modules are
removed.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-removed-high-availability-and-clusters.html -->

## High Availability and Clusters

The following high availability and cluster related features and functionalities are
removed in Oracle Linux 10.

### pcsd Web UI

The `pcsd` Web UI is no longer available as a standalone user interface. Use the Cockpit web console instead.

### Removed and Updated Pacemaker CIB Elements

The following configuration components of the Pacemaker CIB are removed or
changed:

- The `validate-with` attribute of the `cib` element is set
  to `pacemaker-4.0`.
- The `stonith-action` cluster property is set to `off` if
  it was previously set to `poweroff`.
- Legacy promotable clone (master) resources are changed to standard promotable clones by
  changing the `master` xml element to the `clone` xml element and by
  setting the `promotable` meta attribute.
- Location constraints with more than one top-level rule are converted to separate
  location constraints for each top-level rule.

The following components are renamed:

- The `crmd-finalization-timeout` cluster property is renamed to
  `join-finalization-timeout`.
- The `crmd-integration-timeout` cluster property is renamed to
  `join-integration-timeout`.
- The `crmd-transition-delay` cluster property is renamed to
  `transition-delay`.

The following components are removed from the CIB:

- `nagios-class` and `upstart-class` resources.
- `bundle` resources based on an `rkt` container.
- The `restart-type` resource meta-attribute.
- The `can_fail` operation meta-attribute.
- The `role_after_failure` operation meta-attribute.
- `moon` attributes in `date_spec` elements of
  rules.
- The `remove-after-stop` cluster property.
- Ping nodes, which are changed to cluster member nodes with all resources banned and
  probes disabled.
- NVpairs without a value attribute.
- Duplicate NVpairs with a specific name within an NVset, for which only the first NVpair is
  kept.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-removed-compilers-and-development-tools.html -->

## Compilers and Development Tools

### Linking against 32-bit Packages

Linking against 32-bit multilib packages is removed.

### Perl(Mail::Sender) Module

The `perl(Mail::Sender)` module is removed.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-removed-containers.html -->

## Containers

The following container technology related features and functionalities are removed in
Oracle Linux 10.

### Runc Container Runtime

The `runc` container runtime is removed. The default container runtime is `crun`.

### Cgroupv1

The `cgroupv1` control group mechanism is removed, use `cgroupv2` instead.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-KnownIssues.html -->

## 5 Known Issues

This chapter describes known issues that you may encounter when installing and using the Oracle
Linux 10 software. Unless indicated otherwise, the issues apply to both x86\_64 and aarch64
systems. Information that pertains only to a specific platform is also noted accordingly.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-InstallationIssues.html -->

## Installation Issues

The following are known installation issues for Oracle Linux 10.

### RDP Install Error

When using RDP during an installation of Oracle Linux 10, the
following error message might appear on the console or in the install logs:

```
*** BUG *** In pixman_region32_init_rect: Invalid rectangle passed 
Set a breakpoint on '_pixman_log_error' to debug
```

The installation proceeds normally, and this error can be ignored.

(Bug 37644579)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol10-KernelIssues.html -->

## Kernel Issues

The following kernel issues apply in Oracle Linux 10.

### Console Font Loading Failure Messages During `systemd-vconsole-setup` With UEK 8

During system boot, when booting into UEK 8, the system might emit error messages while
starting the `systemd-vconsole-setup` service:

```
systemd-vconsole-setup[1463]: setfont: ERROR kdfontop.c:183 put_font_kdfontop: Unable to load such font with such kernel version
systemd-vconsole-setup[1453]: /usr/bin/setfont failed with a "system error" (EX_OSERR), ignoring.
systemd-vconsole-setup[1453]: Setting source virtual console failed, ignoring remaining ones.
```

The issue results because the framebuffer console driver, `fbcon`, is set to use deferred takeover,
which causes it to wait until a message is sent to the default
boot console. The deferred takeover causes the `systemd-vconsole-setup`
service to try to set the font on the default boot console which doesn't support this
operation.

You can work around the issue by setting the `fbcon=nodefer` kernel
command line option. For example, if UEK 8 is the default kernel, run:

```
sudo grubby --update-kernel=DEFAULT --args="fbcon=nodefer"
```

(Bug 37920190)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol-PackageChangesfromtheUpstreamRelease.html -->

## 6 Package Changes From the Upstream Release

The following sections list the changes to binary and source
packages from the upstream release.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol-ChangestoBinaryPackages.html -->

## Changes to Binary Packages

This section contains information about the removed, modified, and new binary packages in this release. For information about the source package changes, see [Changes to Source Packages](ol-ChangestoSourcePackages.html#ol10-packages-source).

### Added Binary Packages for BaseOS by Oracle

The following binary packages have been added to BaseOS by Oracle:

- `btrfs-progs`
- `dtrace`
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
- `kernel-uek`
- `kernel-uek-core`
- `kernel-uek-debug`
- `kernel-uek-debug-core`
- `kernel-uek-debug-devel`
- `kernel-uek-debug-modules`
- `kernel-uek-debug-modules-core`
- `kernel-uek-debug-modules-extra`
- `kernel-uek-debug-modules-extra-netfilter`
- `kernel-uek-debug-modules-usb`
- `kernel-uek-debug-modules-wireless`
- `kernel-uek-devel`
- `kernel-uek-doc`
- `kernel-uek-modules`
- `kernel-uek-modules-core`
- `kernel-uek-modules-desktop`
- `kernel-uek-modules-extra`
- `kernel-uek-modules-extra-netfilter`
- `kernel-uek-modules-usb`
- `kernel-uek-modules-wireless`
- `libertas-sd8686-firmware`
- `libertas-sd8787-firmware`
- `libertas-usb8388-firmware`
- `libertas-usb8388-olpc-firmware`
- `linux-firmware-core`
- `liquidio-firmware`
- `ocfs2-tools`
- `oracle-backgrounds`
- `oracle-indexhtml`
- `oraclelinux-release`
- `oraclelinux-release-el10`
- `oracle-logos`
- `oracle-logos-httpd`
- `oracle-logos-ipa`
- `python3-dmidecode`

### Added Binary Packages for AppStream by Oracle

The following binary packages have been added to AppStream by Oracle:

- `dnf-plugin-spacewalk`
- `dtrace-devel`
- `dtrace-testsuite`
- `libblockdev-btrfs`
- `NetworkManager-config-connectivity-oracle`
- `pcp-pmda-rocestat`
- `python3-dnf-plugin-spacewalk`
- `python3-dnf-plugin-ulninfo`
- `python3-hwdata`
- `python3-netifaces`
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

### Added Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages have been added to CodeReady Linux Builder by Oracle:

- `oraclelinux-sb-certs`

### Modified BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been modified:

- `alternatives`
- `audispd-plugins`
- `audispd-plugins-zos`
- `audit`
- `audit-libs`
- `audit-rules`
- `autofs`
- `basesystem`
- `binutils`
- `binutils-gold`
- `biosdevname`
- `chkconfig`
- `chrony`
- `cockpit`
- `cockpit-bridge`
- `cockpit-doc`
- `cockpit-system`
- `cockpit-ws`
- `cockpit-ws-selinux`
- `coreutils`
- `coreutils-common`
- `coreutils-single`
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
- `glibc-langpack-gbm`
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
- `glibc-langpack-kv`
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
- `glibc-langpack-rif`
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
- `glibc-langpack-ssy`
- `glibc-langpack-st`
- `glibc-langpack-su`
- `glibc-langpack-sv`
- `glibc-langpack-sw`
- `glibc-langpack-syr`
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
- `glibc-langpack-tok`
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
- `glibc-langpack-zgh`
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
- `initscripts`
- `initscripts-rename-device`
- `initscripts-service`
- `ipset`
- `ipset-libs`
- `iptables-libs`
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
- `kdump-utils`
- `kexec-tools`
- `kmod`
- `kmod-libs`
- `krb5-libs`
- `krb5-pkinit`
- `krb5-server`
- `krb5-server-ldap`
- `krb5-workstation`
- `libdnf`
- `libertas-sd8686-firmware`
- `libertas-sd8787-firmware`
- `libertas-usb8388-firmware`
- `libertas-usb8388-olpc-firmware`
- `libipa_hbac`
- `libkadm5`
- `libkcapi`
- `libkcapi-hasher`
- `libkcapi-hmaccalc`
- `libnfsidmap`
- `libnsl`
- `libsss_autofs`
- `libsss_certmap`
- `libsss_idmap`
- `libsss_nss_idmap`
- `libsss_sudo`
- `linux-firmware`
- `linux-firmware-core`
- `linux-firmware-whence`
- `liquidio-firmware`
- `makedumpfile`
- `mcelog`
- `mdadm`
- `microcode_ctl`
- `netconsole-service`
- `netronome-firmware`
- `NetworkManager`
- `NetworkManager-adsl`
- `NetworkManager-bluetooth`
- `NetworkManager-config-server`
- `NetworkManager-libnm`
- `NetworkManager-tui`
- `NetworkManager-wifi`
- `NetworkManager-wwan`
- `nfs-utils`
- `nvme-cli`
- `nvmetcli`
- `openssh`
- `openssh-clients`
- `openssh-keycat`
- `openssh-server`
- `openssl`
- `openssl-fips-provider`
- `openssl-fips-provider-so`
- `openssl-libs`
- `os-prober`
- `parted`
- `pcre2`
- `pcre2-syntax`
- `polkit`
- `polkit-libs`
- `python3`
- `python3-configshell`
- `python3-dnf`
- `python3-dnf-plugin-post-transaction-actions`
- `python3-dnf-plugin-pre-transaction-actions`
- `python3-dnf-plugins-core`
- `python3-dnf-plugin-versionlock`
- `python3-firewall`
- `python3-hawkey`
- `python3-libdnf`
- `python3-libipa_hbac`
- `python3-libs`
- `python3-libsss_nss_idmap`
- `python3-sss`
- `python3-sssdconfig`
- `python3-sss-murmur`
- `readonly-root`
- `redhat-release`
- `selinux-policy`
- `selinux-policy-doc`
- `selinux-policy-mls`
- `selinux-policy-sandbox`
- `selinux-policy-targeted`
- `shim-x64`
- `sos`
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
- `sssd-passkey`
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
- `vim-data`
- `vim-filesystem`
- `vim-minimal`
- `yum`
- `yum-utils`

### Modified Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `anaconda-widgets-devel`
- `bind-devel`
- `bind-doc`
- `crash-devel`
- `dotnet-sdk-10.0-source-built-artifacts`
- `dotnet-sdk-8.0-source-built-artifacts`
- `dotnet-sdk-9.0-source-built-artifacts`
- `edk2-aarch64`
- `edk2-tools`
- `edk2-tools-doc`
- `glibc-benchtests`
- `glibc-nss-devel`
- `glibc-static`
- `hivex-devel`
- `ipset-devel`
- `java-21-openjdk-demo-fastdebug`
- `java-21-openjdk-demo-slowdebug`
- `java-21-openjdk-devel-fastdebug`
- `java-21-openjdk-devel-slowdebug`
- `java-21-openjdk-fastdebug`
- `java-21-openjdk-headless-fastdebug`
- `java-21-openjdk-headless-slowdebug`
- `java-21-openjdk-jmods-fastdebug`
- `java-21-openjdk-jmods-slowdebug`
- `java-21-openjdk-slowdebug`
- `java-21-openjdk-src-fastdebug`
- `java-21-openjdk-src-slowdebug`
- `java-21-openjdk-static-libs-fastdebug`
- `java-21-openjdk-static-libs-slowdebug`
- `java-25-openjdk-demo-fastdebug`
- `java-25-openjdk-demo-slowdebug`
- `java-25-openjdk-devel-fastdebug`
- `java-25-openjdk-devel-slowdebug`
- `java-25-openjdk-fastdebug`
- `java-25-openjdk-headless-fastdebug`
- `java-25-openjdk-headless-slowdebug`
- `java-25-openjdk-jmods-fastdebug`
- `java-25-openjdk-jmods-slowdebug`
- `java-25-openjdk-slowdebug`
- `java-25-openjdk-src-fastdebug`
- `java-25-openjdk-src-slowdebug`
- `java-25-openjdk-static-libs-fastdebug`
- `java-25-openjdk-static-libs-slowdebug`
- `kmod-devel`
- `libdnf-devel`
- `libguestfs-devel`
- `libguestfs-man-pages-ja`
- `libguestfs-man-pages-uk`
- `libnfsidmap-devel`
- `librados-devel`
- `libradospp-devel`
- `librbd-devel`
- `libsss_nss_idmap-devel`
- `libudisks2-devel`
- `libvirt-daemon-plugin-sanlock`
- `libvirt-devel`
- `libvirt-docs`
- `NetworkManager-libnm-devel`
- `nginx-mod-devel`
- `nss_db`
- `nss_hesiod`
- `ocaml-hivex`
- `ocaml-hivex-devel`
- `ocaml-libguestfs`
- `ocaml-libguestfs-devel`
- `OpenIPMI-devel`
- `PackageKit-glib-devel`
- `parted-devel`
- `pcp-testsuite`
- `pcre2-static`
- `pcre2-tools`
- `podman-tests`
- `postgresql-test-rpm-macros`
- `python3-debug`
- `python3-hivex`
- `python3-idle`
- `python3-ipatests`
- `python3-mpich`
- `python3-test`
- `ruby-hivex`
- `sanlock-devel`
- `selinux-policy-extra`
- `selinux-policy-mls-extra`
- `selinux-policy-targeted-extra`
- `tog-pegasus-devel`
- `virt-v2v-man-pages-ja`
- `virt-v2v-man-pages-uk`
- `wireshark-devel`

### Modified AppStream Binary Packages

The following binary packages from the AppStream upstream release have been modified:

- `anaconda`
- `anaconda-core`
- `anaconda-dracut`
- `anaconda-gui`
- `anaconda-install-env-deps`
- `anaconda-install-img-deps`
- `anaconda-tui`
- `anaconda-widgets`
- `aspnetcore-runtime-10.0`
- `aspnetcore-runtime-8.0`
- `aspnetcore-runtime-9.0`
- `aspnetcore-runtime-dbg-10.0`
- `aspnetcore-runtime-dbg-8.0`
- `aspnetcore-runtime-dbg-9.0`
- `aspnetcore-targeting-pack-10.0`
- `aspnetcore-targeting-pack-8.0`
- `aspnetcore-targeting-pack-9.0`
- `audit-libs-devel`
- `bind`
- `bind-chroot`
- `bind-dnssec-utils`
- `bind-libs`
- `bind-license`
- `bind-utils`
- `binutils-devel`
- `blivet-data`
- `boom-boot`
- `boom-boot-conf`
- `buildah`
- `buildah-tests`
- `cloud-init`
- `cockpit-image-builder`
- `cockpit-machines`
- `cockpit-packagekit`
- `cockpit-session-recording`
- `cockpit-storaged`
- `containers-common`
- `containers-common-extra`
- `container-tools`
- `coreos-installer`
- `coreos-installer-bootinfra`
- `coreos-installer-dracut`
- `crash`
- `ddiskit`
- `delve`
- `dnf-bootc`
- `dotnet-apphost-pack-10.0`
- `dotnet-apphost-pack-8.0`
- `dotnet-apphost-pack-9.0`
- `dotnet-host`
- `dotnet-hostfxr-10.0`
- `dotnet-hostfxr-8.0`
- `dotnet-hostfxr-9.0`
- `dotnet-runtime-10.0`
- `dotnet-runtime-8.0`
- `dotnet-runtime-9.0`
- `dotnet-runtime-dbg-10.0`
- `dotnet-runtime-dbg-8.0`
- `dotnet-runtime-dbg-9.0`
- `dotnet-sdk-10.0`
- `dotnet-sdk-8.0`
- `dotnet-sdk-9.0`
- `dotnet-sdk-aot-10.0`
- `dotnet-sdk-aot-9.0`
- `dotnet-sdk-dbg-10.0`
- `dotnet-sdk-dbg-8.0`
- `dotnet-sdk-dbg-9.0`
- `dotnet-targeting-pack-10.0`
- `dotnet-targeting-pack-8.0`
- `dotnet-targeting-pack-9.0`
- `dotnet-templates-10.0`
- `dotnet-templates-8.0`
- `dotnet-templates-9.0`
- `dracut-caps`
- `dracut-live`
- `edk2-ovmf`
- `efi-srpm-macros`
- `fapolicyd`
- `fapolicyd-selinux`
- `fdo-admin-cli`
- `fdo-client`
- `fdo-init`
- `fdo-manufacturing-server`
- `fdo-owner-cli`
- `fdo-owner-onboarding-server`
- `fdo-rendezvous-server`
- `fips-provider-next`
- `firefox`
- `firewall-applet`
- `firewall-config`
- `gdb`
- `gdb-doc`
- `gdb-gdbserver`
- `gdb-headless`
- `gdb-minimal`
- `glibc-devel`
- `glibc-doc`
- `glibc-locale-source`
- `glibc-utils`
- `gnome-shell-extension-background-logo`
- `gnome-tour`
- `gnome-user-docs`
- `gpsd`
- `gpsd-clients`
- `hivex`
- `hivex-libs`
- `httpd`
- `httpd-core`
- `httpd-devel`
- `httpd-filesystem`
- `httpd-manual`
- `httpd-tools`
- `ignition`
- `ignition-edge`
- `ignition-grub`
- `ignition-validate`
- `image-builder`
- `ipa-client`
- `ipa-client-common`
- `ipa-client-encrypted-dns`
- `ipa-client-epn`
- `ipa-client-samba`
- `ipa-common`
- `ipa-selinux`
- `ipa-selinux-luna`
- `ipa-selinux-nfast`
- `ipa-server`
- `ipa-server-common`
- `ipa-server-dns`
- `ipa-server-encrypted-dns`
- `ipa-server-trust-ad`
- `ipset-service`
- `iptables-devel`
- `iptables-nft`
- `iptables-nft-services`
- `iptables-utils`
- `java-21-openjdk`
- `java-21-openjdk-demo`
- `java-21-openjdk-devel`
- `java-21-openjdk-headless`
- `java-21-openjdk-javadoc`
- `java-21-openjdk-javadoc-zip`
- `java-21-openjdk-jmods`
- `java-21-openjdk-src`
- `java-21-openjdk-static-libs`
- `java-25-openjdk`
- `java-25-openjdk-demo`
- `java-25-openjdk-devel`
- `java-25-openjdk-headless`
- `java-25-openjdk-javadoc`
- `java-25-openjdk-javadoc-zip`
- `java-25-openjdk-jmods`
- `java-25-openjdk-src`
- `java-25-openjdk-static-libs`
- `kernel-rpm-macros`
- `kernel-srpm-macros`
- `krb5-devel`
- `ksh`
- `libblockdev`
- `libblockdev-btrfs`
- `libblockdev-crypto`
- `libblockdev-dm`
- `libblockdev-fs`
- `libblockdev-loop`
- `libblockdev-lvm`
- `libblockdev-lvm-dbus`
- `libblockdev-mdraid`
- `libblockdev-mpath`
- `libblockdev-nvdimm`
- `libblockdev-nvme`
- `libblockdev-part`
- `libblockdev-plugins-all`
- `libblockdev-smart`
- `libblockdev-smartmontools`
- `libblockdev-swap`
- `libblockdev-tools`
- `libblockdev-utils`
- `libguestfs`
- `libguestfs-appliance`
- `libguestfs-bash-completion`
- `libguestfs-inspect-icons`
- `libguestfs-rescue`
- `libguestfs-rsync`
- `libguestfs-xfs`
- `librados2`
- `librbd1`
- `libreswan`
- `libudisks2`
- `libvirt`
- `libvirt-client`
- `libvirt-client-qemu`
- `libvirt-daemon`
- `libvirt-daemon-common`
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
- `libvirt-daemon-lock`
- `libvirt-daemon-log`
- `libvirt-daemon-plugin-lockd`
- `libvirt-daemon-proxy`
- `libvirt-libs`
- `libvirt-nss`
- `libvirt-ssh-proxy`
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
- `mptcpd`
- `net-snmp`
- `net-snmp-agent-libs`
- `net-snmp-devel`
- `net-snmp-libs`
- `net-snmp-perl`
- `net-snmp-perl-module`
- `net-snmp-utils`
- `netstandard-targeting-pack-2.1`
- `NetworkManager-cloud-setup`
- `NetworkManager-config-connectivity-oracle`
- `NetworkManager-ovs`
- `NetworkManager-ppp`
- `nfs-utils-coreos`
- `nfsv4-client-utils`
- `nginx`
- `nginx-all-modules`
- `nginx-core`
- `nginx-filesystem`
- `nginx-mod-http-image-filter`
- `nginx-mod-http-perl`
- `nginx-mod-http-xslt-filter`
- `nginx-mod-mail`
- `nginx-mod-stream`
- `ntsysv`
- `OpenIPMI`
- `OpenIPMI-lanserv`
- `OpenIPMI-libs`
- `openssh-askpass`
- `openssh-keysign`
- `openssl-devel`
- `openssl-perl`
- `open-vm-tools`
- `open-vm-tools-desktop`
- `open-vm-tools-salt-minion`
- `open-vm-tools-sdmp`
- `open-vm-tools-test`
- `osbuild`
- `osbuild-composer`
- `osbuild-composer-core`
- `osbuild-composer-worker`
- `osbuild-depsolve-dnf`
- `osbuild-luks2`
- `osbuild-lvm2`
- `osbuild-ostree`
- `osbuild-selinux`
- `osinfo-db`
- `pacemaker-cluster-libs`
- `pacemaker-libs`
- `pacemaker-schemas`
- `PackageKit`
- `PackageKit-command-not-found`
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
- `pcp-export-pcp2openmetrics`
- `pcp-export-pcp2spark`
- `pcp-export-pcp2xml`
- `pcp-export-pcp2zabbix`
- `pcp-export-zabbix-agent`
- `pcp-geolocate`
- `pcp-gui`
- `pcp-import-collectl2pcp`
- `pcp-import-ganglia2pcp`
- `pcp-import-iostat2pcp`
- `pcp-import-mrtg2pcp`
- `pcp-import-sar2pcp`
- `pcp-libs`
- `pcp-libs-devel`
- `pcp-pmda-activemq`
- `pcp-pmda-amdgpu`
- `pcp-pmda-apache`
- `pcp-pmda-bash`
- `pcp-pmda-bcc`
- `pcp-pmda-bind2`
- `pcp-pmda-bonding`
- `pcp-pmda-bpf`
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
- `pcp-pmda-farm`
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
- `pcp-pmda-resctrl`
- `pcp-pmda-rocestat`
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
- `pcp-pmda-uwsgi`
- `pcp-pmda-weblog`
- `pcp-pmda-zimbra`
- `pcp-pmda-zswap`
- `pcp-selinux`
- `pcp-system-tools`
- `pcp-zeroconf`
- `pcre2-devel`
- `pcre2-utf16`
- `pcre2-utf32`
- `perl-hivex`
- `perl-PCP-LogImport`
- `perl-PCP-LogSummary`
- `perl-PCP-MMV`
- `perl-PCP-PMDA`
- `perl-Sys-Guestfs`
- `perl-XML-Parser`
- `pesign`
- `plymouth`
- `plymouth-core-libs`
- `plymouth-devel`
- `plymouth-graphics-libs`
- `plymouth-plugin-fade-throbber`
- `plymouth-plugin-label`
- `plymouth-plugin-script`
- `plymouth-plugin-space-flares`
- `plymouth-plugin-two-step`
- `plymouth-scripts`
- `plymouth-system-theme`
- `plymouth-theme-fade-in`
- `plymouth-theme-script`
- `plymouth-theme-solar`
- `plymouth-theme-spinfinity`
- `plymouth-theme-spinner`
- `podman`
- `podman-docker`
- `podman-remote`
- `polkit-devel`
- `polkit-docs`
- `postgresql`
- `postgresql-contrib`
- `postgresql-docs`
- `postgresql-plperl`
- `postgresql-plpython3`
- `postgresql-pltcl`
- `postgresql-private-devel`
- `postgresql-private-libs`
- `postgresql-server`
- `postgresql-server-devel`
- `postgresql-static`
- `postgresql-test`
- `postgresql-upgrade`
- `postgresql-upgrade-devel`
- `pykickstart`
- `python3-audit`
- `python3-blivet`
- `python3-blockdev`
- `python3-boom`
- `python3-devel`
- `python3-dnf-plugin-leaves`
- `python3-dnf-plugin-modulesync`
- `python3-dnf-plugin-show-leaves`
- `python3-gpsd`
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-iscsi-initiator-utils`
- `python3-kickstart`
- `python3-libguestfs`
- `python3-net-snmp`
- `python3-osbuild`
- `python3-pcp`
- `python3-rtslib`
- `python3-tkinter`
- `python3-virt-firmware`
- `python-unversioned-command`
- `rear`
- `redhat-rpm-config`
- `rhel-system-roles`
- `rpmdevtools`
- `sanlock`
- `sanlock-lib`
- `scap-security-guide`
- `scap-security-guide-doc`
- `selinux-policy-devel`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `setroubleshoot-server`
- `slapi-nis`
- `sssd-idp`
- `system-config-printer-libs`
- `system-config-printer-udev`
- `systemd-boot-unsigned`
- `systemd-devel`
- `systemd-journal-remote`
- `systemd-ukify`
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
- `systemtap-sdt-dtrace`
- `systemtap-server`
- `target-restore`
- `thunderbird`
- `tog-pegasus`
- `tog-pegasus-libs`
- `tuned-gtk`
- `tuned-ppd`
- `tuned-profiles-atomic`
- `tuned-profiles-mssql`
- `tuned-profiles-oracle`
- `tuned-profiles-postgresql`
- `tuned-profiles-spectrumscale`
- `tuned-utils`
- `udisks2`
- `udisks2-iscsi`
- `udisks2-lsm`
- `udisks2-lvm2`
- `uki-direct`
- `vim-common`
- `vim-enhanced`
- `vim-X11`
- `virt-p2v`
- `virt-sb-certs`
- `virt-top`
- `virt-v2v`
- `virt-v2v-bash-completion`
- `WALinuxAgent`
- `WALinuxAgent-udev`
- `wireshark`
- `wireshark-cli`
- `xxd`

### Removed BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been removed:

- `amd-ucode-firmware`
- `atheros-firmware`
- `brcmfmac-firmware`
- `cirrus-audio-firmware`
- `dvb-firmware`
- `intel-audio-firmware`
- `intel-vsc-firmware`
- `iwlegacy-firmware`
- `iwlwifi-dvm-firmware`
- `iwlwifi-mvm-firmware`
- `kpatch`
- `kpatch-dnf`
- `libdnf-plugin-subscription-manager`
- `libertas-firmware`
- `mlxsw_spectrum-firmware`
- `mrvlprestera-firmware`
- `mt7xxx-firmware`
- `nxpwireless-firmware`
- `python3-cloud-what`
- `python3-subscription-manager-rhsm`
- `qcom-firmware`
- `realtek-firmware`
- `redhat-release-eula`
- `rhsm-icons`
- `subscription-manager`
- `subscription-manager-cockpit`
- `subscription-manager-plugin-ostree`
- `subscription-manager-rhsm-certificates`
- `tiwilink-firmware`

### Removed AppStream Binary Packages

The following binary packages from the AppStream upstream release have been removed:

- `amd-gpu-firmware`
- `ansible-collection-microsoft-sql`
- `command-line-assistant`
- `command-line-assistant-selinux`
- `insights-client`
- `insights-client-ros`
- `intel-gpu-firmware`
- `NetworkManager-config-connectivity-redhat`
- `nvidia-gpu-firmware`
- `opentelemetry-collector`
- `realtime-tests`
- `redhat-backgrounds`
- `redhat-cloud-client-configuration`
- `redhat-cloud-client-configuration-cdn`
- `redhat-indexhtml`
- `redhat-logos`
- `redhat-logos-httpd`
- `redhat-logos-ipa`
- `rhc`
- `rhc-worker-playbook`
- `rhel-drivers`
- `s390utils`
- `s390utils-se-data`
- `toolbox`
- `virtio-win`
- `virt-who`

### Removed CodeReady Linux Builder Binary Packages

The following binary packages from the CodeReady Linux Builder upstream release have been removed:

- `dyninst-testsuite`
- `redhat-sb-certs`
- `SDL2-static`
- `toolbox-tests`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/relnotes10.1/ol-ChangestoSourcePackages.html -->

## Changes to Source Packages

This section contains information about the removed, modified, and new source packages in this release. For information about the binary package changes, see [Changes to Binary Packages](ol-ChangestoBinaryPackages.html#ol10-packages-binary).

### Added Source Packages for BaseOS by Oracle

The following source packages have been added to the BaseOS by Oracle:

- `btrfs-progs`
- `dtrace`
- `kernel-uek`
- `ocfs2-tools`
- `oracle-indexhtml`
- `oraclelinux-release`
- `oraclelinux-release-el10`
- `oracle-logos`
- `python-dmidecode`

### Added Source Packages for AppStream by Oracle

The following source packages have been added to AppStream by Oracle:

- `dnf-plugin-spacewalk`
- `dtrace`
- `pyOpenSSL`
- `python3-dnf-plugin-ulninfo`
- `python-hwdata`
- `python-netifaces`
- `rhn-client-tools`
- `rhnlib`
- `rhnsd`

### Modified BaseOS Source Packages

The following source packages from the BaseOS upstream release have been modified:

- `audit`
- `autofs`
- `basesystem`
- `binutils`
- `biosdevname`
- `chkconfig`
- `chrony`
- `cockpit`
- `coreutils`
- `dnf`
- `dnf-plugins-core`
- `dracut`
- `efibootmgr`
- `efi-rpm-macros`
- `firewalld`
- `glibc`
- `grub2`
- `grubby`
- `initscripts`
- `ipset`
- `iptables`
- `iscsi-initiator-utils`
- `kdump-utils`
- `kexec-tools`
- `kmod`
- `krb5`
- `libdnf`
- `libkcapi`
- `linux-firmware`
- `makedumpfile`
- `mcelog`
- `mdadm`
- `microcode_ctl`
- `NetworkManager`
- `nfs-utils`
- `nvme-cli`
- `nvmetcli`
- `openssh`
- `openssl`
- `openssl-fips-provider`
- `os-prober`
- `parted`
- `pcre2`
- `polkit`
- `python3.12`
- `python-configshell`
- `redhat-release`
- `selinux-policy`
- `shim`
- `sos`
- `sssd`
- `systemd`
- `tuned`
- `vim`

### Modified AppStream Source Packages

The following source packages from the AppStream upstream release have been modified:

- `anaconda`
- `audit`
- `bind`
- `binutils`
- `boom-boot`
- `buildah`
- `ceph`
- `chkconfig`
- `cloud-init`
- `cockpit`
- `cockpit-image-builder`
- `cockpit-machines`
- `cockpit-session-recording`
- `containers-common`
- `container-tools`
- `crash`
- `ddiskit`
- `delve`
- `dnf`
- `dnf-plugins-core`
- `dotnet10.0`
- `dotnet8.0`
- `dotnet9.0`
- `dracut`
- `edk2`
- `efi-rpm-macros`
- `fapolicyd`
- `fido-device-onboard`
- `fips-provider-next`
- `firefox`
- `firewalld`
- `gdb`
- `glibc`
- `gnome-shell-extension-background-logo`
- `gnome-tour`
- `gnome-user-docs`
- `gpsd`
- `hivex`
- `httpd`
- `ignition`
- `image-builder`
- `ipa`
- `ipset`
- `iptables`
- `iscsi-initiator-utils`
- `java-21-openjdk`
- `java-25-openjdk`
- `kernel-srpm-macros`
- `krb5`
- `ksh`
- `libblockdev`
- `libguestfs`
- `libreswan`
- `libvirt`
- `lorax`
- `lorax-templates-rhel`
- `mecab-ipadic`
- `mpich`
- `mptcpd`
- `net-snmp`
- `NetworkManager`
- `nfs-utils`
- `nginx`
- `OpenIPMI`
- `openssh`
- `openssl`
- `open-vm-tools`
- `osbuild`
- `osbuild-composer`
- `osinfo-db`
- `pacemaker`
- `PackageKit`
- `pcp`
- `pcre2`
- `perl-XML-Parser`
- `pesign`
- `plymouth`
- `podman`
- `polkit`
- `postgresql16`
- `pykickstart`
- `python3.12`
- `python-blivet`
- `python-rtslib`
- `python-virt-firmware`
- `rear`
- `redhat-rpm-config`
- `rhel-system-roles`
- `rpmdevtools`
- `rust-coreos-installer`
- `sanlock`
- `scap-security-guide`
- `selinux-policy`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `slapi-nis`
- `sssd`
- `system-config-printer`
- `systemd`
- `systemtap`
- `thunderbird`
- `tog-pegasus`
- `tuned`
- `udisks2`
- `vim`
- `virt-p2v`
- `virt-top`
- `virt-v2v`
- `WALinuxAgent`
- `wireshark`

### Removed BaseOS Source Packages

The following source packages from the BaseOS upstream release have been removed:

- `kpatch`
- `subscription-manager`
- `subscription-manager-cockpit`
- `subscription-manager-rhsm-certificates`

### Removed AppStream Source Packages

The following source packages from the AppStream upstream release have been removed:

- `ansible-collection-microsoft-sql`
- `command-line-assistant`
- `insights-client`
- `opentelemetry-collector`
- `realtime-tests`
- `redhat-cloud-client-configuration`
- `redhat-indexhtml`
- `redhat-logos`
- `rhc`
- `rhc-worker-playbook`
- `rhel-drivers`
- `s390utils`
- `toolbox`
- `virtio-win`
- `virt-who`