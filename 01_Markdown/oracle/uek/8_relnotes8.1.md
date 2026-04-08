---
title: "Unbreakable Enterprise Kernel 8 Update 1: Release Notes (6.12.0-100)"
source_url: "https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "uek"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

## Unbreakable Enterprise Kernel

Unbreakable Enterprise Kernel 8 Update 1 - Release Notes (Version 6.12.0-100)

G34758-03

January 2026

---

[Title and Copyright Information](#copyright-information)

Unbreakable Enterprise Kernel Unbreakable Enterprise Kernel 8 Update 1 - Release Notes (Version 6.12.0-100)

G34758-03

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2025, 2026, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.1-Preface.html -->

## Preface

[Unbreakable Enterprise Kernel 8 Update 1: Release
Notes (6.12.0-100)](https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/) provides a summary of the new features,
significant changes, and any known issues in Unbreakable Enterprise Kernel 8 Update 1 (UEK 8U1).


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8-AboutUEK8.html -->

## 1 About Unbreakable Enterprise Kernel 8 Update 1

This chapter provides an overview of Unbreakable Enterprise Kernel 8 Update 1 (UEK 8U1) and contains important information about this major
release.

Note:

Upgrading from an Unbreakable Enterprise Kernel Developer Preview release to its later
official version isn't supported. If you're running the Developer Preview version, you must
reinstall the official UEK release upon its general availability.

UEK 8U1 is initially released with the 6.12.0-100.28.2 version of the kernel. The kernel's source code is
available through a public git source code repository at <https://github.com/oracle/linux-uek>.

The following is a general description of the scope of support for UEK 8U1:

- The kernel is developed, built, and tested on the 64-bit Arm (aarch64), Intel® 64-bit
  x86\_64, and AMD 64-bit x86\_64 architectures and is based on the mainline Linux kernel
  version 6.12 (LTS).
- UEK 8U1 is made available for installation on the latest
  Oracle Linux 9 update releases and for Oracle Linux 10.
- In UEK 8U1, more features are enabled to provide support
  for key functional requirements and patches are applied to improve performance and
  optimize the kernel for use on Oracle operating environments. Note that Oracle actively
  monitors upstream check-ins and applies critical bug and security fixes to UEK 8U1.
- Although UEK 8U1 uses the same versioning model as the
  mainline Linux kernel version, it's possible that some applications might not understand
  the 6.12.0 versioning scheme. Note, however, that regular Linux applications are usually
  neither aware of nor affected by Linux kernel version numbers.
- A version of UEK 8U1 that enables 64k pages is available
  for 64-bit Arm (aarch64) platforms for Oracle Linux 9 and later. The
  `kernel-uek64k` package is available on Oracle Cloud Infrastructure Arm
  compute shapes only. Use of this kernel outside of Oracle Cloud Infrastructure is only
  available as a technical preview.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8-CertificationofUEK8forOracleProducts.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8-Compatibility.html -->

## Compatibility

Oracle Linux maintains full user space compatibility with Red Hat Enterprise Linux (RHEL),
which is independent of the kernel version that's running underneath the OS. Note that
existing applications in user space continue to run unmodified with UEK 8U1; no
recertifications are required for RHEL certified applications.

To minimize any impact on interoperability during releases, the Oracle Linux team works with
third-party vendors that have hardware and software with dependencies on kernel modules. The
kernel ABI for UEK 8U1 remains unchanged in all subsequent updates to the initial release.
Customers migrating from UEK R7 must be aware that kernel ABIs have changed in UEK 8U1. If an
application is using kernel modules, users must verify the support status with the application
vendor.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.1-NewFeaturesandChanges.html -->

## 2 New Features and Changes

The following new features, enhancements, and notable changes are
introduced in UEK 8U1.

For other features introduced in UEK 8, see [Unbreakable Enterprise Kernel 8: Release
Notes (6.12.0-0.20.20)](https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.1-dmesg_hardening.html -->

## `dmesg` Hardening for Administrator Privileges

UEK 8U1 is built with the SECURITY\_DMESG\_RESTRICT flag enabled. Administrator privileges
are now required to run the `dmesg` command when a system is running
UEK 8U1.

This update hardens the system against unrestricted access to sensitive information
about the system. Use the `sudo` command to gain administrator
privileges when running `dmesg`.

If you urgently need to disable this restriction, you can run `sudo sysctl
kernel.dmesg_restrict=0` to temporarily disable the restriction. Or you can
add the configuration entry in a system configuration file in the
`/etc/sysctl.d/` directory:

```
echo "kernel.dmesg_restrict = 0" | sudo tee /etc/sysctl.d/dmesg-restrict
sudo sysctl --system
```

Consider the security risk of disabling this restriction before doing so, and evaluate
whether it might be better to resolve this requirement in another way.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek_8_1_features_driver_updates.html -->

## Updated Drivers

Device drivers included in UEK 8U1 are aligned with
the drivers in the upstream mainline Linux 6.12 kernel. A few notable updates are
included where drivers include functionality or fixes available in later upstream kernel
versions.

Many driver modules no longer track version information. Oracle works with vendors to
align device drivers included in UEK 8U1 with the code
available in upstream kernel versions.

Notable driver updates are presented in the following table:

Table 2-1 Driver Alignment

| Driver Module | Driver Description | Aligned Kernel Version | Notable Updates |
| --- | --- | --- | --- |
| `megaraid_sas` | Broadcom MegaRAID SAS Driver | 6.15 | Several fixes and improvements from 6.15 were backported in this release. Note that this driver includes a version string: 07.734.00.00-rc1 |
| `mgag200` | HPE MGA G200 SE Driver | 6.12 | Partner provided update for new iLO7 devices on HPE Gen12 servers. |
| `mpi3mr` | Broadcom MPI3 Storage Controller Device Driver | 6.15 | Several fixes and improvements from 6.15 were backported in this release. Note that this driver includes a version string: 8.13.0.5.50 |
| `mpt3sas` | Broadcom LSI MPT Fusion SAS 3.0 Device Driver | 6.15 | Several fixes and improvements from 6.15 were backported in this release. Note that this driver includes a version string: 52.100.00.00 |


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.1-DeprecatedandRemovedFeatures.html -->

## Deprecated and Removed Features

The following features are deprecated, removed, or no longer supported in UEK 8U1:

Deprecated Features

- SHA-1 Algorithm

  The SHA-1 algorithm is deprecated in UEK 8U1 while in
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

  `cgroupsv1` is deprecated in Oracle Linux 9 and is removed in a Oracle
  Linux 10.
- `XFS_SUPPORT_V4` is deprecated

  The V4 file system format contains known weaknesses in the on-disk format. Therefore,
  the option is deprecated in UEK 8U1 and will be removed
  in a future UEK release.

  You can check whether the file system is formatted to use V4, by running the
  `xfs_db -r -c version`
  <device> command.

  If the feature is enabled, you must backup data, reformat the device, and restore
  data.
- `XFS_SUPPORT_ASCII_CI` is deprecated

  The XFS ASCII case-insensitive name feature is deprecated in UEK 8U1 and will be removed in a future UEK release. The
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

- Unrestricted access to the kernel ring buffer is removed.

  Unprivileged access to the kernel ring buffer through the `dmesg`
  command output is removed in this release. Use the `sudo` command to
  escalate to administrator privileges when running the `dmesg` command.
  See [dmesg Hardening for Administrator Privileges](uek8.1-dmesg_hardening.html#uek8_0_dmesg_hardening).
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

  The `CONFIG_STAGING` kernel configuration option is disabled in UEK 8U1. The kernel option made available drivers that
  don't necessarily meet the highest kernel quality level and which were available for
  test use. The option was deprecated in UEK R7 and is removed in UEK 8U1.
- `CONFIG_IXGB` option is disabled

  The `CONFIG_IXGB` for Intel PRO/10GbE hardware is removed in this UEK
  release.
- crashkernel=auto removed

  The `crashkernel=auto` option was deprecated in UEK R7 and unsupported
  for Oracle Linux 9. The kernel option is removed in UEK 8U1. For more information about configuring the `crashkernel` setting on
  Oracle Linux 9, see [Oracle Linux 9: Managing Kernels and System Boot](https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/), and on Oracle Linux 10,
  see [Oracle Linux 10: Managing Kernels and System
  Boot](https://docs.oracle.com/en/operating-systems/oracle-linux/10/boot/).
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
  in UEK 8U1:

  - `cls_tcindex`
  - `cls_rsvp`
  - `sch_dsmark`
  - `sch_atm`
  - `sch_cbq`
- `resilient_rdmaip` Module Removed

  The `resilient_rdmaip` module was deprecated in UEK R7 and is now
  removed.
- `oracleasm` Kernel Module Removed

  The `oracleasm` kernel module is removed in UEK 8U1. Note that this module continues to be supported in
  the UEK R5 and UEK R6 releases.

  Oracle ASMLib continues to be supported using `io_uring` interfaces.
  See [Oracle Linux: Installing and Configuring Oracle ASMLIB
  v3](https://docs.oracle.com/en/operating-systems/oracle-linux/asmlib/) for more information.
- `sundance` Kernel Module Removed

  The DLink Sundance (ST201), `sundance`, driver is removed in UEK 8U1. The module was removed in the upstream kernel
  because it was unmaintained.
- `cpu5_wdt` Kernel Module Removed

  The `cpu5_wdt` watchdog driver is removed in UEK 8U1. The module was removed in the upstream kernel
  because it had several issues that were unresolved and lacked maintenance.
- `i2c-amd756-s4882` and `i2c-nforce2-s4985` Kernel
  Modules Removed

  The `i2c-amd756-s4882` and `i2c-nforce2-s4985` legacy
  muxing drivers are removed in UEK 8U1. The module was
  removed in the upstream kernel because they're old and contain technically inaccurate
  code.
- `CONFIG_CRYPTO_OFB` and `CONFIG_CRYPTO_CFB`
  cryptographic modes

  The CFB (Cipher Feedback) mode (NIST SP800-38A) used for TPM2 cryptography and the OFB
  (Output Feedback) mode (NIST SP800-38A) used to turn a block cipher into a synchronous
  stream cipher are removed in UEK 8U1, to align with
  upstream changes.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.0-KnownIssues.html -->

## 3 Known Issues

This chapter describes any known issues for Unbreakable Enterprise Kernel 8 Update 1.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.0-UnusableorUnavailableFeaturesfortheArmPlatform.html -->

## Unusable or Unavailable Features for Arm Platforms

The following features are known to not work, remain untested, or have issues that render
the feature unusable. The following features aren't supported on Arm platforms:

- InfiniBand
- FibreChannel
- RDMA


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/38006792.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.0-UpgradingOracleSupportedRDMAPackagesonOracleLinux.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.0-InstallationandAvailability.html -->

## 4 Installation and Availability

This chapter provides information about the availability of
UEK 8U1 on Oracle Linux and includes installation and instructions on
upgrading from a previous UEK release to UEK 8U1.

UEK 8U1 is supported on the Intel® 64-bit x86\_64, AMD 64-bit
x86\_64 and 64-bit Arm (aarch64) platforms.


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.0-AboutUpgradingFromaPreviousOracleLinuxorUEKReleasetoUEK8.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.0-ObtainingPackagesforInstallation.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/uek8.0-UpgradingaSystemtoUEK8.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/u1-cve-fixes.html -->

## 5 List of CVEs fixed in this release

The following list describes the CVEs that are fixed in UEK R8U1 (6.12.0-100.28.2) as
compared to initial release of UEK R8 (6.12.0-0.20.20). The content provided here is
automatically generated and includes the CVE identifier and a summary of the issue.

Note that CVEs are
continually handled in patch updates that are made available as
errata builds for the current release. For this reason, it's
critical that keep systems updated with the latest package updates
for this kernel release. Many of the issues listed here might have
already been resolved in prior errata builds for the previous update
level.

You can keep current with the latest CVE information at
<https://linux.oracle.com/cve>.

- [CVE-2024-28956](https://linux.oracle.com/cve/CVE-2024-28956.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/module_deprecations_x86_64.html -->

## A Module Deprecations (x86\_64)

The following modules are deprecated in this release of UEK 8U1.
While these modules are available and operative in this release, they are planned for removal
and support isn't guaranteed in future UEK releases. Thus, these modules should not be used in
new UEK 8U1 deployments to avoid problems upgrading in the future.

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
<!-- page: https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.1/module_deprecations_aarch64.html -->

## B Module Deprecations (aarch64)

The following modules are deprecated in this release of UEK 8U1.
While these modules are available and operative in this release, they are planned for removal
and support isn't guaranteed in future UEK releases. Thus, these modules should not be used in
new UEK 8U1 deployments to avoid problems upgrading in the future.

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