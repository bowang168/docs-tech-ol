---
title: "Release Notes for Oracle Linux 9.6"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol9"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux 9

Release Notes for Oracle Linux 9.6

G27748-05

January 2026

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 9 Release Notes for Oracle Linux 9.6

G27748-05

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2025, 2026, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9.6-Preface.html -->

## Preface

[Oracle Linux 9: Release Notes for Oracle Linux 9.6](https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/) provides information about the new features and known issues in the Oracle
Linux 9.6 release. The information applies to both x86\_64 and 64-bit Arm (aarch64)
architectures. This document might be updated after first publication.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-AboutOracleLinux9.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9.0-SystemRequirementsandLimitations.html -->

## System Requirements and Limitations

To check whether a specific hardware is supported on the current Oracle Linux 9 release, see
the Hardware Certification List at <https://linux.oracle.com/hardware-certifications>. Note that as hardware becomes
available and validated, the hardware is added to the list.

CPU, memory, disk and file system limits for all Oracle Linux releases are described in
[Oracle Linux: Limits](https://docs.oracle.com/en/operating-systems/oracle-linux/limits/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-AvailableArchitectures.html -->

## Available Architectures

The release is available for installation on the following
platforms:

- Intel® 64-bit (x86\_64) (x86-64-v2)
- AMD 64-bit (x86\_64) (x86-64-v2)
- 64-bit Arm (aarch64) (Arm v8.0-A)

  The Arm platform runs only with Unbreakable Enterprise Kernel Release (UEK).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9.6-ShippedKernels.html -->

## Shipped Kernels

For the x86\_64 platform, the current Oracle Linux 9 release ships with the following kernel
packages:

- `6.12.0-1.23.3.2` (Unbreakable Enterprise Kernel Release 8 (UEK
  R8)) (Default)
- `5.14.0-570.12.1.0.1` (Red Hat Compatible Kernel (RHCK))

For new installations, UEK R8 is automatically enabled and installed. It also becomes the
default kernel on first boot.

If you're upgrading from a previous Oracle Linux 9 update release, the kernel isn't
automatically upgraded to UEK R8. See [Installation and Boot](ol9-features-Installation.html#ol9-features-Installation) for more information.

For the aarch64 platform, Oracle Linux ships with the UEK kernel only.

The Oracle Linux release is tested as a bundle, as shipped on the installation media image.
When installed from the installation media image, the kernel's version included in the image
is the minimum version that's supported. Downgrading kernel packages isn't supported, unless
recommended by Oracle Support.

For more information about kernel availability on Oracle Linux 9 releases, see <https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/oracle_linux9_kernel_version_matrix.html>


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol-AbouttheUnbreakableEnterpriseKernel.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol-Compatibility.html -->

## User Space Compatibility

Oracle Linux maintains user space compatibility with Red Hat Enterprise Linux (RHEL) that's
independent of the kernel version that underlies the OS. Existing applications in user space
continue to run unmodified on UEK with no required recertifications for Oracle Linux certified
applications.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-ObtainingInstallationImages.html -->

## Obtaining Installation Images

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-UpgradingFromPreviousOracleLinuxReleases.html -->

## Upgrading From Previous Oracle Linux Releases

You can upgrade an Oracle Linux 8 system to the Oracle Linux 9 release by using
the `leapp` utility.

For step-by-step instructions and information about any known issues that might arise when
upgrading the system, see [Oracle Linux 9: Upgrading Systems With Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/9/leapp/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-UpgradingFromOracleLinuxUpdateReleases.html -->

## Upgrading From Previous Oracle Linux Update Releases

You can upgrade an Oracle Linux 9 system from a previous update level to the current update level by
running the `sudo dnf update` command.

After performing a system update where many packages are updated, we recommend that you
reboot the system. System functionality might become unstable if core packages are
updated and the system isn't restarted to load the most recent updates. You can check
whether a system requires a restart by running:

```
dnf needs-restarting -r
```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-NewFeaturesandChanges.html -->

## 2 New Features and Changes

Unless indicated otherwise, the following new features, major enhancements, bug fixes, and
other changes that are introduced in this release of Oracle Linux 9 apply to both the x86\_64
and 64-bit Arm (aarch64) platforms.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-Installation.html -->

## Installation and Boot

The following features, enhancements, and changes related to installation and boot are
introduced in this release of Oracle Linux 9.

### UEK R8 Default Kernel Handling

If you're performing a fresh Oracle Linux 9.6 installation from an ISO image, then after
the installation completes, the UEK R8 kernel is automatically enabled.

UEK R8 includes many new features including security and performance enhancements. For
more details, see [Unbreakable Enterprise Kernel 8: Release
Notes (6.12.0-0.20.20)](https://docs.oracle.com/en/operating-systems/uek/8/relnotes8.0/).

If you select RHCK as the default kernel instead of UEK, ensure that you disable UEK yum
repositories or ULN channels. For more information about switching to RHCK, see [Oracle Linux 9: Managing Kernels and System
Boot](https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/).

In the case of updates, switching to UEK R8 isn't automatic. If you're upgrading from a
prior update release of Oracle Linux 9, the system continues to run with the kernel
that's already installed.

If the system is using UEK R7, you can upgrade to UEK R8 by using the following
instructions:

- Updating by using yum

  When you update to Oracle Linux 9.6, the previous kernel is preserved. At the
  same time, the UEK R8 yum repository is also added to the system yum
  configuration. To move to the latest kernel, run the following commands,
  depending on the system platform:

  - On x86\_64 systems:

    ```
    sudo dnf config-manager --disable ol9_UEKR7
    sudo dnf config-manager --enable ol9_UEKR8
    sudo dnf install -y kernel-uek
    sudo dnf update
    ```
  - On aarch64 systems:

    ```
    sudo dnf config-manager -enable ol9_UEKR8
    sudo dnf install -y kernel-uek
    sudo dnf update
    ```
- Updating by using ULN

  Similar to the previous scenario, the previous kernel is preserved. However,
  system subscriptions might change as a result. Sign in to [https://linux.oracle.com](https://linux.oracle.com/), and update the system channel
  subscriptions to enable the `ol9_x86_64_UEKR8` or
  `ol9_aarch64_UEKR8`, as required. After you have updated the
  system channel subscriptions, run:

  ```
  sudo dnf install -y kernel-uek
  sudo dnf update
  ```

After setting the default kernel, you can further configure kernel boot parameters so
that these parameters are applied at every system boot. For instructions, see [Oracle Linux 9: Managing Kernels and System
Boot](https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/).

### Enhanced Security for GRUB Bootloader

The GRUB bootloader is updated for security enhancements in Oracle Linux 9.6.

Several CVEs are resolved, including issues such as:

- Heap out-of-bounds (OOB) writes during JPEG parsing
- Missing checks for failed allocations
- Integer overflows resulting in heap-based OOB writes and reads
- Use-after-free errors due to hooks not being removed on module unload
- OOB writes in configuration file parsing

### Advanced Partitioning with Oracle Linux Image Builder

Oracle Linux image builder has been updated to support creating disk images with custom
partitioning layouts. This includes the ability to create custom mountpoints, LVM-based
partitions, and LVM-based SWAP configurations using a blueprint file.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-OSandSoftwareMgmt.html -->

## Operating System and Software Management

The following features, enhancements, and changes related to the OS and software management
are introduced in this Oracle Linux 9 release.

### DNF Automatic Notifications for Failed Updates

DNF Automatic can now be configured to notify users about failed updates. A new
`send_error_messages` Boolean option has been added to the
`[emitters]` section of the `/etc/dnf/automatic.conf`
configuration file. When set to `yes`, DNF Automatic notifies users about
failed automatic updates using the configured emitter.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-InfrastructureServices.html -->

## Infrastructure Services

The following features, enhancements, and changes related to infrastructure services are
introduced in this Oracle Linux 9 release.

### `chrony` Updated to Version 4.6.1

The `chrony` package is
updated to version 4.6.1.

### `linuxptp` Updated to Version 4.4

`linuxptp` is an implementation of the Precision Time Protocol (PTP). The
`linuxptp` package is updated to version 4.4.

### FRRouting Updated to Version 8.5.3

The `frr` package is updated to version 8.5.3.

### TuneD Updated to Version 2.25.0

The `tuned` package is updated to version 2.25.0.

### samba Updated to Version 4.21.3

The `samba` packages are upgraded to upstream version 4.21.3.

### CUPS Configuration Now Disables Weak Ciphers by Default

CUPS now honors system-wide crypto policies by default, disabling weak ciphers. To follow system crypto policy, remove the `SSLOptions NoSystem` directive from the `/etc/cups/cupsd.conf` and `/etc/cups/client.conf` files.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-Security.html -->

## Security

The following features, enhancements, and changes related to security are introduced in this
Oracle Linux 9 release.

### Enhanced pcscd Configuration with --disable-polkit

The `pcscd` service now includes the `--disable-polkit` option,
enabling users to disable the PolicyKit authorization framework. With this enhancement you can
accessing PKCS #11 devices in limited environments, such as the initial RAM disk, and you can
automate the unlocking of LUKS-encrypted volumes at boot time using a PKCS #11 device.

### Enhanced `pkcs11-tool` Output

The `pkcs11-tool -L` and `pkcs11-tool -O` commands now include the `uri:` field in their output, providing URI information that can be used when configuring the `pkcs11` Clevis pin for automated unlocking of LUKS-encrypted drives with PKCS #11 devices.

### CBC Ciphers in `crypto-policies`

The `crypto-policies` now uses the `openssl -CBC
CipherString` directive, disabling CBC cipher suites in OpenSSL if none are
enabled in `crypto-policies`.

### `nettle` Library Updated to Version 3.10.1

The `nettle` library package has been updated to version 3.10.1.

This update includes several key enhancements and changes:

- Performance improvements for certain cryptographic operations.
- The addition of DRBG-CTR-AES256, a new deterministic random-bit generator.
- The introduction of RSA-OAEP, an RSA encryption/decryption method that uses a new
  OAEP padding scheme.
- The inclusion of SHAKE-128, an arbitrary-length hash function from the SHA-3 family.
- A streaming API for SHAKE-128 and SHAKE-256.
- The removal of the MD5 assembly, which might result in a slight performance
  impact.

For more information, see the upstream information on <https://git.lysator.liu.se/nettle/nettle/-/blob/master/NEWS?ref_type=heads>.

### Rsyslog Updated to Version 8.2412.0

The `rsyslog` packages have been updated to version 8.2412.0.

This update provides various fixes and enhancements, such as the ability to bind a
ruleset to the `imjournal` module, which reduces the load on the main
message queue and minimizes resource usage.

### OpenSCAP Updated to Version 1.3.11

`OpenSCAP` has been updated to version 1.3.11.

This updates includes a new script, `oscap-im`, used in Containerfiles to
build hardened bootable container images to run as Image Mode OS.

The update includes several maintenance and bug fixes, including:

- Fixing Python 3.13 compatibility
- Fixing RPM database path in RPM probes
- Ensuring xlink namespace exists, enabling OpenSCAP scans with DISA content using tailoring
  files
- Stopping the printing of useless component reference information in "oscap info"

For more information, see the upstream release notes on <https://github.com/OpenSCAP/openscap/releases/tag/1.3.11>.

### Clevis Updated to Version 21

The `clevis` packages have been updated to version 21.

This update adds support for PKCS #11 devices and providing various enhancements and bug
fixes, including the `clevis-pin-pkcs11` subpackage for unlocking
LUKS-encrypted volumes using PKCS #11 devices, two checks to the
`clevis-udisks2` subpackage, and a fix that prevents the "Address in
use" errors.

### New Keylime Policy Management Tool

The new `keylime-policy` tool integrates all management tasks of Keylime runtime policies and measured boot policies, improving the performance of generating policies.

### SELinux Type Assignment for `/dev/hfi1_0`

SELinux now assigns the `hfi1_device_t` type to the `/dev/hfi1_0` device, enabling proper access control.

### Enhanced SELinux Confinement for System Services

The SELinux policy has been strengthened with the addition of new rules that restrict the following `systemd` services:

- `iio-sensor-proxy`
- `power-profiles-daemon`
- `switcheroo-control`
- `samba-bgqd`

These services now operate under a confined SELinux context, rather than being labeled as
`unconfined_service_t`, which was non-compliant with the CIS Server
Level 2 benchmark rule "Ensure No Daemons are Unconfined by SELinux." By running in
SELinux enforcing mode, these services contribute to a more secure and compliant
system.

### SCAP Security Guide Updated to 0.1.76

The SCAP Security Guide has been updated to version 0.1.76.

Notable changes include:

- The Oracle Linux 9 STIG profile has been synchronized with the official DISA Oracle
  Linux 9 STIG, version 1, release 1.
- The `require_singleuser_auth` rule now uses the systemd override
  mechanism for enhanced functionality.
- The check for approved SSH ciphers has been updated to align with the latest STIG policy
  guidelines.

### Keylime HTTPS Revocation Notifications

Keylime components have enhanced their revocation notification webhooks to use a more secure
configuration for HTTPS connections. Before, the revocation notifier used only the
system-installed CA certificates. Now, you can configure the CA certificate used for HTTPS
connections by adding it to the `trusted_server_ca` configuration option or to
the system trust store.

### logrotate ignoreduplicates Option

The `ignoreduplicates` option is now available in the
`logrotate` package. This option ignores any duplicate file paths in
the `logrotate` configuration and is disabled by default.

### New SSSD `exop_force` Option

With the `exop_force` option, you can force a password change in the
following scenarios:

- When no grace logins remain on the LDAP server.
- The SSSD service attempts to change the password even if the LDAP server indicates
  that no remaining grace logins.

To use this feature, configure the following setting in the `sssd.conf` file:

- Set `ldap_pwmodify_mode = exop_force` in the `[domain/â¦â]` section.

### Group Merging Added in `authselect`

To use the `authselect` utility for group merging, enable it in the
`authselect` profiles. You no longer need to manually edit the
`nssswitch.conf` file to enable group merging.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-Networking.html -->

## Networking

The following features, enhancements, and changes related to networking are introduced in
this Oracle Linux 9 release.

### `iproute` Packages Updated to Version 6.11.0

The `iproute` packages are updated to version 6.11.0.

Notable changes include improvements to Multiple Spanning Tree (MST) states and Berkeley
Packet Filter (BPF) socket-local storage.

### NetworkManager Forward Error Correction

NetworkManager now allows users to configure forward error correction (FEC) encoding on
network interface controllers (NICs), reducing network overhead and latency. By configuring
FEC encoding, users can reduce the overhead of redundant data transmission and lower network
latency, resulting in improved network performance and reliability.

### NetworkManager Can Automatically Add Routes to DNS Servers

The `ipv4.routed-dns` parameter in NetworkManager allows users to configure the system to automatically add routes to DNS servers through the correct network interface. This feature ensures that DNS queries are resolved correctly, even in complex network configurations.

### NetworkManager Can Set `ipv4.dhcp-send-hostname` to Default To `false`

NetworkManager now allows users to set the `ipv4.dhcp-send-hostname`
option to `false` for all IPv4 connections. This feature provides more
control over DHCP client behavior, enabling users to customize their network
configurations according to their needs. The option is also available on IPv6
connections.

### NetworkManager Includes `ip-ping-addresses` And `ip-ping-timeout` Properties

NetworkManager is enhanced to include the `ip-ping-addresses` and
`ip-ping-timeout` properties for connection settings. These
properties enable users to configure NetworkManager to wait for a specific IP address to
become reachable before activating a network connection, ensuring that dependent
services are started only when the network is ready.

### NetworkManager DHCP Client IPv6-only Preferred Option for DHCPv4

The IPv6-only preferred option for DHCPv4 is now available for NetworkManager clients.
This feature allows users to prioritize IPv6 addresses over IPv4 addresses in dual-stack
networks, or to use IPv4 addresses assigned manually while still preferring IPv6. The
option can be disabled locally by setting the `ipv6.method disabled`
option.

### `nmstate` Includes the `require-id-on-certificate` Setting for Libreswan Configuration

The `nmstate` API now includes the
`require-id-on-certificate` setting for Libreswan VPN configurations.
This feature enables users to configure Subject Alternative Name (SAN) validation for
IPsec connections, enhancing the security of VPN connections.

### `xdp-tools` Updated to Version 1.5.1

The `xdp-tools` package is updated to version 1.5.1, which includes various
enhancements and bug fixes.

Notable changes include the addition of the `xdp-forward` utility for
XDP-accelerated packet forwarding and improved support for User Datagram Protocol (UDP) packet
sizes.

### IPsec HW Offload With ESN Available on Bonding Devices

Bonding devices can be configured with IPsec Hardware (HW) offload with Extended Sequence
Numbers (ESN). This feature enables users to configure IPsec connections with improved
security and performance on bonding devices.

### `nmstate` Can Configure IPvLANs

The `nmstate` API can configure an IPvLAN, a virtual network interface
that enhances network management and container networking. IPvLAN provides a flexible
and efficient way to manage network interfaces, making it easier to deploy and manage
complex network configurations.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-Kernel.html -->

## Kernel and System Libraries

The following notable features, enhancements, and changes apply to the Red Hat Compatible
Kernel (RHCK) that's shipped with the current Oracle Linux 9 version.

### eBPF Facility Updated

The eBPF facility has been updated to Linux kernel version 6.12.

### View cgroup Instances

With the introduction of `cgroup v2`, the traditional method of viewing
cgroup instances using the `/proc/cgroups` file is no longer applicable.
The `/proc/cgroups` file, designed for `cgroup v1`, is
deprecated for `cgroup v2` as it doesn't provide the correct
information.

To accurately find the number of cgroup subsystems with `cgroup v2`, you
can now use the `cgroup.stat` file in the root cgroup. This file serves
as the replacement for `/proc/cgroups` in `cgroup v2`,
providing the correct count of cgroup subsystems.

### `kdump` Updated to Version 6.10

`kdump` is updated to 6.10.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-FileSystemsandStorage.html -->

## File Systems and Storage

The following features, enhancements, and changes related to file systems and storage are
introduced in this Oracle Linux 9 release.

### NVME Over Fibre Channel Discovery and Connect

Using the `nvme-cli` utility, you can discover and connect to NVMe over Fibre
Channel (NVMe/FC) enabled host bus adapters (HBAs). For more information about this feature,
see [Oracle Linux 9: Managing Storage Devices](https://docs.oracle.com/en/operating-systems/oracle-linux/9/stordev/). For more information about compatible HBA
devices, see <https://linux.oracle.com/Component_Compatibility_Guide.pdf>.

### NVMe Over Fibre Channel Installation

When you install Oracle Linux installation, you can now select NVMe over Fibre Channel
(NVMe/FC) devices under the NVMe Fabrics Devices section while adding disks in the
Installation Destination window. For more information about compatible HBA devices, see <https://linux.oracle.com/Component_Compatibility_Guide.pdf>.

### NVMe Over Fiber Channel SAN Boot

You can now boot NVMe over Fibre Channel (NVMe/FC) on NVMe/FC host bus adapters that support
NVMe/FC boot capability. For more information about enabling NVMe/FC boot capability, see the
NVMe-FC host bus adapter (HBA) manufacturer documentation. For more information about
compatible HBA devices, see <https://linux.oracle.com/Component_Compatibility_Guide.pdf>.

### NFS Includes TLS

Network File System (NFS) with Transport Layer Security (TLS), introduced in Oracle Linux
9.4 as a Technology Preview, is now fully supported. This feature enhances NFS security
by enabling TLS for Remote Procedure Call (RPC) traffic, ensuring encrypted
communication between clients and servers.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-HighAvailabilityandClusters.html -->

## High Availability and Clusters

The following features, enhancements, and changes related to high availability are introduced
in this Oracle Linux 9 release.

### Deleting Several Resources With a Single `pcs` Command

You can now specify several resources at the same time when using the `pcs resource
delete`, `pcs resource remove`, `pcs stonith
delete`, and `pcs stonith remove` commands, so that you don't have
to run the command repeatedly for each resource that you want to remove.

For example, you can run:

```
pcs resource delete service2 service3
```

### `--output-format` Option Available for `pcs` Commands

The `--output-format` option is added to various pcs commands, to display
output in different formats. The option accepts the following values:

- `text`: displays output in plain text,
- `cmd`: displays output as `pcs` commands to re-create the
  configuration,
- `json`: displays output in JSON format for machine parsing.

The `--output-format` option can be used with the `pcs stonith
config` and `pcs stonith level config` commands to display fencing
level configuration.

The `--output-format` option can be used with the `pcs tag`
command to display configured tags. For example:

```
pcs tag --output-format cmd
```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-DynamicProgramming.html -->

## Dynamic Programming Languages, Web and Database Servers

The following features, enhancements, and changes related to programming languages, web
servers, and database servers are introduced in this Oracle Linux 9 release.

### PHP Updated to Version 8.3

PHP 8.3 is now in the new `php:8.3` module stream.

To install the `php:8.3` module stream, use the following command:

```
sudo dnf module install php:8.3
```

To upgrade from another stream within Oracle Linux, see [Oracle Linux: Managing Software on Oracle
Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).

For information about the length of support for the `php` module streams, see
the [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/)

### NGINX Updated to Version 1.26

NGINX 1.26 web and proxy server is included in the new `nginx:1.26` module
stream.

To install the `nginx:1.26` stream, use:

```
sudo dnf module install nginx:1.26
```

To upgrade from another stream within Oracle Linux, see [Oracle Linux: Managing Software on Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).

For information about the length of support for the `nginx` module streams,
see the [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/)

### MySQL Module Stream Updated to 8.4

MySQL 8.4 is included in the `mysql:8.4` module stream.

To install the `mysql:8.4` module stream, use the following command:

```
sudo dnf module install mysql:8.4
```

To upgrade from another stream within Oracle Linux, see [Oracle Linux: Managing Software on Oracle
Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).

For information about the length of support for the `mysql` module
streams, see the [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-CompilersandDevTools.html -->

## Compilers and Development Tools

The following features, enhancements, and changes related to compilers and development tools
are introduced in this Oracle Linux 9 release.

### `maven` Module Stream Updated to 3.9

A new update to the `maven 3.9` package is now available. Maven 3.9 is not
compatible with Maven 2.

The notable enhancements include:

- The `maven-openjdk21` package is now available, enabling seamless execution of Maven with OpenJDK 21.
- The `OpenJDK 21` package provides an expanded set of supported Java runtimes for Maven workflows, improving flexibility for development and build environments.

To install, type:

```
sudo dnf module install maven:3.9
```

### Maven OpenJDK Updated to Version 21

Maven OpenJDK is now updated to version 21.

Oracle Linux now includes running Maven with more than one Java version. The
`maven-openjdk21` package lets you seamless run Maven with OpenJDK 21. The
notable changes include:

- Expanded set of Java runtimes for Maven workflows.
- Improved flexibility for development and build environments.

### Rust Toolset Updated to Version 1.84

The Rust Toolset is now at version 1.84.

See <https://blog.rust-lang.org/2025/01/30/Rust-1.84.1/> for more information.

### libva Updated to Version 2.22.0

The `libva` package is updated to 2.22.0.

Notable enhancements include:

- Added VVC decode LibVA interface
- Works with `linux-dmabuf`

### LLVM Toolset Updated to Version 19.1.7

The LLVM Toolset is updated to version 19.1.7.

See <https://discourse.llvm.org/t/llvm-19-1-7-released/84062> for more information.

LLVM Toolset is a rolling Application Stream and only the latest version is
supported.

### `llvm-doc` Package Update

The `llvm-doc` package now contains a reference to the upstream
documentation.

### zstd Compression for Clang and LLVM

`zstd` is available for Clang and LLVM debug section compression.

### PCP Updated to Version 6.3.2

PCP is updated to version 6.3.2.

See <https://github.com/performancecopilot/pcp/blob/main/CHANGELOG> for more
information.

### `valgrind` Updated to Version 3.24.0

`valgrind` has been updated to version 3.24.0.

See <https://valgrind.org/docs/manual/dist.news.html> for more
information.

### `libabigail` Updated to Version 2.6

The `libabigail` package is updated to version 2.6.

### `elfutils` Updated to Version 0.192

The `elfutils` package is updated to version 0.192.

### Gnu `ld` Linker Update

The `ld` linker is updated with the following notable changes:

- The linker detects applications using read, write, and execute permissions in a memory region, to
  help prevent buffer overflow vulnerabilities.
- The linker detects applications using an executable stack and returns errors when
  this occurs to help prevent buffer overflow vulnerabilities.

### Boost C++ Libraries Updated to Version 1.75.0.

Boost is updated to version 1.75.0.

The `boost-devel` package is updated to provide
`BoostConfig.cmake` and other CMake scripts.

### Go Toolset Updated to Version1.23

The Go Toolset is updated to version 1.23.

See <https://tip.golang.org/doc/go1.23> for
more information.

The Go Toolset is a rolling Application Stream and only the latest version is
supported.

### `glibc` Updated to Version GB18030-2022

`glibc` is updated to replace the GB18030-2005 encoding standard with
GB18030-2022, to include new transcoding relationships and characters.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-Containers.html -->

## Containers

The following features, enhancements, and changes related to containers are introduced in
this Oracle Linux 9 release.

### Podman Updated to Version 5.4

Podman is updated to version 5.4. The components for Podman are in the
`container-tools` package.

The Container Tools RPM meta-package, features updates to Podman, Buildah, Skopeo,
`crun`, and `runc` tools. Updating the package pulls in the
latest versions of these subcomponents, including:

- podman-5.4
- buildah-1.39
- crun-1.21
- runc-1.2.4
- skopeo-1.18

Notably, Podman v5.4 includes various bug fixes and enhancements over the previous version.
See <https://github.com/containers/podman/releases> for more information.

### `zstd:chunked` Image Compression in Podman

Podman can use images compressed with the `zstd:chunked` format to reduce
image sizes and partial pulls, and improve efficiency in container image management. Note that
this feature is only tested for x86\_64 platforms.

### Customizable Healthcheck Output in Podman

You can now customize the storage of healthcheck output for individual containers in Podman, enabling more detailed debugging information to be retained as needed, and controlling healthcheck output storage for specific containers to address concerns around data sensitivity and storage optimization. This enhancement is useful for troubleshooting sporadic healthcheck failures without impacting the live service. This is a significant improvement over the previous limitations, where healthcheck output was restricted to the five most recent runs, with a character limit of 500 per run, and could only be accessed through the `podman inspect` command.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-Cockpit.html -->

## Cockpit Web Console

The following features, enhancements, and changes related to the Cockpit web console are
introduced in this Oracle Linux 9 release.

### Cockpit Web Console Updated to Version 334

The Cockpit web console is updated to version 334.

Notable updates include:

- The storage view is updated so that you can list and manage Btrfs subvolumes and
  snapshots. This functionality requires UEK and you must have the
  `udisks2-btrfs` package installed.
- Metrics prefer Valkey over Redis.
- The login page now prevents more than one login in a single browser session.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-features-Support.html -->

## Support

The following features, enhancements, and changes related to support are introduced in this
Oracle Linux 9 release.

### Use of Hyphens in Plugin Option Names

The `sos` utility has adopted a standardized naming convention for plugin options, replacing underscores with hyphens. This change enhances consistency with global options.

### New --api-url Option

Specify a custom API URL using the new `--api-url` option and interact with various APIs as needed. This enhancement provides flexibility when working with different API endpoints.

### New --skip-cleaning-files Option

Control which files are preserved during the `sos report` command execution with the new `--skip-cleaning-files` option. This option is useful when you need to retain specific files for further analysis or debugging purposes. You can specify globs or wildcards to be excluded from the cleaning process


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-TechnologyPreview.html -->

## 3 Technology Preview

The following items are available as technical previews in this release of Oracle Linux. Note
that some items listed apply to Red Hat Compatible Kernel (RHCK) and might already be
available in UEK.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-techprev-Security.html -->

## Security

The following features for security are available as technology preview.

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

### QUIC Protocol in OpenSSL

OpenSSL clients can use the QUIC transport layer network protocol as a technical
preview.

### `io_uring` Asynchronous I/O Interface

Although available, the `io_uring` asynchronous I/O interface is disabled in RHCK
by default. To enable the feature, set the `kernel.io_uring_disabled`
variable to any one of the following values when running the `sysctl`
command:

- `0`: All processes can create `io_uring` instances
  as usual.
- `1`: Creating `io_uring` is disabled for unprivileged
  processes. With this setting, the `io_uring_setup` fails with the
  `-EPERM` error. It only successfully completes if the calling
  process is privileged by the `CAP_SYS_ADMIN` capability. However,
  existing `io_uring` instances can still be used.
- `2` (default): Creating `io_uring` creation is
  disabled for all processes. With this setting, the
  `io_uring_setup` always fails with `-EPERM`.
  However, existing `io_uring` instances can still be used.

To use this feature, an updated version of the SELinux policy to enable the
`mmap` system call on anonymous inodes is also required.

Note that `io_uring` support has been available in UEK from UEK R6U3.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-techprev-InfrastructureServices.html -->

## Infrastructure Services

The following features for infrastructure services are available as technology previews.

### Socket API for TuneD

The socket API for TuneD maps one-to-one with the D-Bus API and provides an alternative
communication method for cases where D-Bus isn't available. With the socket API, you can
control the TuneD daemon to optimize the performance, and change the values of various tuning
parameters. The socket API is disabled by default. You can enable it in the
`tuned-main.conf` file.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-techprev-Networking.html -->

## Networking

The following networking features are available as technology previews.

### `gpsd-minimal`

The `gpsd-minimal` package is available as a technical preview.
`gpsd` is a service daemon that mediates access to a GPS sensor
connected to the host computer by serial or USB interface, making its data on the
location, course, and velocity of the sensor available to be queried on TCP port
2947 of the host computer.

### WireGuard

WireGuard is a VPN solution that has improved security features and is easily
configurable.

Note that WireGuard is fully supported in UEK. See [Oracle Linux: Configuring Virtual Private Networks](https://docs.oracle.com/en/operating-systems/oracle-linux/vpn/)
for more information on using WireGuard on Oracle Linux.

### `systemd-resolved` Service

The `systemd-resolved` service provides name resolution to local applications.
Its components include a caching and validating DNS stub resolver, a Link-Local Multicast Name
Resolution (LLMNR), and Multicast DNS resolver and responder.

### PRP and HSR

The `hsr` kernel module is included with RHCK to provide the following
protocols as a technology preview:

- Parallel Redundancy Protocol (PRP)
- High-availability Seamless Redundancy (HSR)

### IPsec Packet Offloading

In RHCK, complete IPsec encapsulation can be offloaded to a Network Interface Controller
(NIC) to reduce workload. This functionality is offered as a technology preview.

### Various Modem Network Drivers

Oracle Linux provides modem drivers in RHCK with limited functionality as a technology
preview:

- Qualcomm MHI WWAM MBIM - Telit FN990Axx
- Intel IPC over Shared Memory (IOSM) - Intel XMM 7360 LTE Advanced
- Mediatek t7xx (WWAN) - Fibocom FM350GL
- Intel IPC over Shared Memory (IOSM) - Fibocom L860GL modem

### Segment Routing Over IPv6

Segment Routing over IPv6 (SRv6) is available as a technology preview in RHCK. SRv6 can
improve traffic flows in edge computing and provides a mechanism to program network
slicing and resource reservation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-techprev-Kernel.html -->

## Kernel

The following kernel features are available as technology previews for RHCK.

### Soft iWarp

Soft-iWARP (`siw`) is an Internet Wide-area RDMA Protocol (iWARP) software
kernel driver. The driver implements the iWARP protocol suite over the TCP/IP network
stack. The suite is implemented in software. Therefore, it doesn't require an RDMA
hardware. The protocol suite enables a system with a standard Ethernet adapter to
connect to an iWARP adapter or to another system that already has `siw`
installed.

Note that from Oracle Linux 9.5, this driver is deprecated.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-techprev-FileSysandStorage.html -->

## File Systems and Storage

The following features that are related to file systems and storage are available as
technology preview.

### `nvme-stas` Package

The `nvme-stas` package, which is a Central Discovery Controller (CDC)
client for Linux, handles the following functionalities:

- Asynchronous Event Notifications (AEN)
- Automated NVMe subsystem connection controls
- Error handling and reporting
- Automatic (`zeroconf`) and Manual configuration.

This package consists of two daemons, Storage Appliance Finder (`stafd`)
and Storage Appliance Connector (`stacd`).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-techprev-CompilersandDevTools.html -->

## Compilers and Development Tools

The following features for compilers and development tools are available as technology
previews.

### `jmc-core` and `owasp-java-encoder`

`jmc-core` is a library that provides core APIs for Java Development Kit (JDK)
Mission Control, including APIs for:

- Parsing and writing Java Flight Recording files
- Discovering Java Virtual Machines (JVMs) through the Java Discovery Protocol (JDP)

The `owasp-java-encoder` package provides a collection of
high-performance low-overhead contextual encoders for Java.

The packages are available in the Oracle Linux 9 CodeReady Builder repository, which is
unsupported, and which you must explicitly enable.

### Flexible Array Conversion Warning-Suppression in `libabigail` Available As a Technology Preview

When comparing binaries, you can suppress warnings related to fake flexible arrays that were
converted to true flexible arrays by using the following suppression specification:

- - - - type\_kind = struct has\_size\_change = true
- - - -has\_strict\_flexible\_array\_data\_member\_conversion = true

This features is available as a technology preview.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-techprev-Virtualization.html -->

## Virtualization

The following virtualization features are available as technology previews.

### Nested VMs

Nested KVM virtualization is provided as a technology preview for KVM virtual machines
(VMs) running on Oracle Linux 9.

### SEV and SEV-ES

The Secure Encrypted Virtualization (SEV) feature is provided for AMD EPYC host machines that
use the KVM hypervisor. It encrypts a virtual machine's memory and protects the VM from access
by the host.

SEV's enhanced Encrypted State version (SEV-ES) encrypts all CPU register contents when a VM
stops running, thus preventing the host from modifying the VM's CPU registers or reading any
information from them.

Note that SEV is supported in UEK.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-DeprecatedFeatures.html -->

## 4 Deprecated Features

This chapter lists features and functionalities that are deprecated in Oracle Linux 9. While
these features might be included and operative in the release, support isn't guaranteed in
future major releases. Thus, these features must not be used in new Oracle Linux 9
deployments.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-Installation.html -->

## Installation

The following installation related features and functionalities are deprecated in Oracle
Linux 9.

### Kickstart Commands

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

### `initial-setup` Package

Instead of using this package, use the `gnome-initial-setup` package as a
replacement.

### `inst.geoloc` Boot Option Values `provider_hostip` And `provider_fedora_geoip`

The `provider_hostip` and `provider_fedora_geoip` values for
the `inst.geoloc=` boot option are deprecated. You can use the
`geolocation_provider=URL` option to set the required geolocation in the
installation program configuration file, if required. Use the `inst.geoloc=0`
option to disable the geolocation.

### Anaconda Screenshots

Capturing screenshots of the Anaconda GUI by using a global hotkey is deprecated.

### Anaconda Help

The built-in documentation from spokes and hubs of all Anaconda user interfaces that was
available during Anaconda installation is deprecated. The interface is self-documented
and the [Oracle Linux 9: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/9/install/) can be used for further
assistance.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-SoftwareManagement.html -->

## Software Management

The following software management related features and functionalities are deprecated in Oracle
Linux 9.

### DNF `debug` plugin

The DNF `debug` plugin, which includes the `dnf debug-dump`
and `dnf debug-restore` commands, is deprecated.

### DNF `libreport`

The DNF `libreport` library is deprecated.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-ShellandCommandLine.html -->

## Shell and Command Line

The following shell and command line related features and functionalities are deprecated in Oracle Linux 9.

### `dump` Utility

The `dump` utility that's included in the `dump` package
is deprecated.

You can alternatively use the `tar` or `dd` to achieve similar
functionality.

Note that the `restore` utility, originally included in the
`dump` package, remains available in Oracle Linux 9 and can be installed by
using the `restore` package.

### Bacula Sqlite Backend Database

The use of a SQLite backend database for the Bacula backup utility is deprecated. Bacula can
use a MySQL backend database and you can migrate existing deployments to MySQL. Avoid using
SQLite for new deployments of the Bacula backup utility.

### TMPDIR Variable in the ReaR Configuration File

Exporting using the `TMPDIR` environment variable in the
`/etc/rear/local.conf` or `/etc/rear/site.conf` ReaR
configuration files, is deprecated.

Instead, you can specify a custom directory for ReaR temporary files by exporting the
variable in the shell environment before executing ReaR. For example, run the
`export TMPDIR=â¦â` statement and then run the `rear`
command in the same shell session or script.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-Security.html -->

## Security

The following security related features and functionalities are deprecated in Oracle Linux
9.

### Unprivileged Access to `dmesg` Output

Unprivileged access to `dmesg` output is deprecated and will be removed in
a future release of UEK 8 and might be removed in a future release of Oracle Linux. Use the `sudo` command to escalate to
administrator privileges when running the `dmesg` command. See [Oracle Linux 9: Enhancing System Security](https://docs.oracle.com/en/operating-systems/oracle-linux/9/security/) for more information on how to restrict access to
kernel ring buffer messages as good security practice.

### OVAL Data Format

The Open Vulnerability Assessment Language (OVAL) data format used by the OpenSCAP suite
is deprecated. Declarative security data is now provided in the Common Security Advisory
Framework (CSAF) format, which is the successor of OVAL.

### Using `update-ca-trust` Without Arguments

Using the `update-ca-trust` command without arguments to update the CA trust
store is deprecated. Use the `update-ca-trust extract` command to update the CA
trust store.

### Configuring STunnel Clients to Use the Trusted Root CA Files

The option to configure STunnel Clients `CAFiles` directive to point to a file
that contains trusted root certificates in the BEGIN TRUSTED CERTIFICATE format. If you use
`CAfile = /etc/pki/tls/certs/ca-bundle.trust.crt`, change the location to
`CAfile = /etc/pki/tls/certs/ca-bundle.crt`.

### NSS Deprecated Algorithms

The following algorithms are deprecated in the Network Security Services (NSS) cryptographic library.

- Digital Signature Algorithm (DSA)
- SEED

Use RSA, ECDSA, SHB-DSA, ML-DSA, or FN-DSA instead.

### `pam_ssh_agent_auth`

`pam_ssh_agent_auth` is deprecated.

### `scap-workbench`

`scap-workbench` is deprecated.

### `oscap-anaconda-addon`

`oscap-anaconda-addon` is deprecated.

### `/etc/system-fips`

The `/etc/system-fips` file, that was used to indicate FIPS mode is
removed. To install Oracle Linux in FIPS mode, add the `fips=1` parameter
to the kernel command line during the system installation. You can check whether Oracle
Linux operates in FIPS mode by using the `fips-mode-setup --check`
command.

### `libcrypt.so.1`

The `libcrypt.so.1` library is deprecated.

### SHA-1 Algorithm

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

### SCP Protocol

In the `scp` utility, secure copy protocol (SCP) is replaced by the SSH
File Transfer Protocol (SFTP) by default. Likewise, SCP is deprecated in the
`libssh` library.

Oracle Linux 9 doesn't use SCP in the OpenSSH suite.

### OpenSSL Cryptographic Algorithms

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

### Digest-MD5

The Digest-MD5 authentication mechanism in the Simple Authentication Security Layer (SASL)
framework is deprecated.

### `/etc/system-fips` File

The `/etc/system-fips` file was used to indicate the FIPS mode in the
system. This file is removed in Oracle Linux 9.

To install Oracle Linux 9 in FIPS mode, add the `fips=1` parameter to the
kernel command line during the system installation. To check whether Oracle Linux 9 is
operating in FIPS mode, use the `fips-mode-setup --check` command.

### `libcrypt.so.1`

The `libcrypt.so.1` cryptogarhic library is deprecated.

### `fapolicyd.rules` File

The `/etc/fapolicyd/fapolicyd.rules` file is deprecated. You can store policy
rules for `fapolicyd` in the `/etc/fapolicyd/rules.d/`
directory. The `fagenrules` script merges all component rule files in
this directory to the `/etc/fapolicyd/compiled.rules` file.

Rules in `/etc/fapolicyd/fapolicyd.trust` continue to be processed by
`fapolicyd` for backward compatibility.

### OpenSSL RSA Encryption Without Padding

RSA encryption without padding for OpenSSL in FIPS mode is no longer accepted. However, key
encapsulation with RSA (RSASVE) which doesn't use padding continues to be supported for
OpenSSL.

### OpenSSL Engines API

The Engines API is deprecated in the OpenSSL 3.0 TLS toolkit. Use the
`pkcs11-provider` Providers API instead. Equally use of the OpenSSL
Engines API in Stunnel is deprecated.

### `openssl-pkcs11`

The `openssl-pkcs11` (`engine_pkcs11`) package, which
relates to the deprecated OpenSSL Engins API, is now deprecated. Use the
`pkcs11-provider` package instead.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-Networking.html -->

## Networking

The following network related features and functionalities are deprecated in Oracle Linux
9.

### Soft-iWarp

Soft-iWarp, which was available as a technology preview in previous releases of Oracle Linux 9, is deprecated.

### Network Teams

The `teamd` service, and the `libteam` library, and support
for configuring network teams are deprecated in favor of network bonds. You should use
network bonds instead, which have similar functions as teams, and which would receive
enhancements and updates.

### `dhcp-client` Package

The `dhcp-client` package and the `dhclient` tool that it
contained are deprecated in favor of the internal DHCP client library built into
NetworkManager.

### `firewalld` Lockdown

The lockdown feature in `firewalld` is deprecated because it can't prevent
processes that are running as `root` from adding themselves to the allow
list.

### `/etc/sysconfig/network-scripts` File

Network configurations profiles used to be in `ifcfg` format and stored in the
`/etc/sysconfig/network-scripts` directory. This format is deprecated. In
Oracle Linux 9, new network configurations are stored in
`/etc/NetworkManager/system-connections` in keyfile format. This format works
with all the connection settings provided by NetworkManager.

However, information in the `/etc/sysconfig/network-scripts` remain
operative, and modifications to existing profiles continue to update the older
files.

### `iptables` Framework

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

### PF\_KEYv2 Kernel API

The `PF_KEYv2` API is used to configure kernel IPsec implementation. However, this API isn't maintained upstream. Therefore, this API is deprecated. Instead, use the `netlink` API as a replacement.

### Network Manager `nmcli` Language Changes

Because Oracle is fully committed to diversity and inclusion, the Network Manager
`connection.master`, `connection.slave-type`, and
`connection.autoconnect-slaves` connection property names are
deprecated. They are retained for backward compatibility. However, consider using the
following replacement terms instead:

- Instead of `connection.master`, use
  `connection.controller`
- Instead of `connection.slave-type`, use
  `connection.port-type`
- Instead of `connection.autoconnect-slaves` use
  `connection.autoconnect-ports`

### TigerVNC

The TigerVNC remote desktop solution is deprecated.

The following packages are deprecated:

- `tigervnc`
- `tigervnc-icons`
- `tigervnc-license`
- `tigervnc-selinux`
- `tigervnc-server`
- `tigervnc-server-minimal`
- `tigervnc-server-module`

The `gnome-connections` application can be used as an alternative VNC
client, but it doesn't provide a VNC server.

Future remote desktop solutions are likely to use Remote Desktop Protocol (RDP).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-Kernel.html -->

## Kernel

The following kernel related features and functionalities are deprecated in Oracle Linux
9.

### `crashkernel=auto` Option

The `crashkernel=auto` option is deprecated and no longer supported on Oracle Linux 9 and is also unsupported for UEK R7 and later. Some platforms, such as the Raspberry Pi have maximum limits for `crashkernel` memory reservation and these must be specified explicitly. This option will be removed in a future UEK release.

### Asynchronous Transfer Mode

Asynchronous Transfer Mode (ATM) encapsulation enables Layer-2 (Point-to-Point Protocol,
Ethernet) or Layer-3 (IP) connectivity for the ATM Adaptation Layer 5 (AAL-5). Currently,
these protocols are used only in chipsets that use ADSL technology, which are being phased
out.

### `kexec_load` in `kexec_tools`

The `kexec_load` system call for `kexec-tools` is
deprecated.

The `kexec_file_load` system call replaces `kexec_load` and
is the default system call.

### `cgroupsv1`

`cgroupsv1` is deprecated in Oracle Linux 9 in favor of
`cgroupsv2`. See [Oracle Linux 9: Managing the System With
systemd](https://docs.oracle.com/en/operating-systems/oracle-linux/9/systemd/) and
[Oracle Linux 9: Managing Kernels and System
Boot](https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/) for more information on using cgroups.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-FileSystemsandStorage.html -->

## File Systems and Storage

The following features and functionalities related to file systems and storage are deprecated
in Oracle Linux 9.

### `lsscsi` NVMe

Using `lsscsi` to list information about Non-Volatile Memory Express
(NVMe) devices is deprecated. Use `nvme-cli`, `lsblk`,
and `blkid` instead.

### sg3\_utils NVMe

Using any of the tools in the `sg3_utils` package to work with
Non-Volatile Memory Express (NVMe) devices is deprecated. Use
`nvme-cli` instead.

### `lvm2-activation-generator`

The `lvm2-activation-generator` program is deprecated, together with its
generated services as follows:

- `lvm2-activation`
- `lvm2-activation-early`
- `lvm2-activation-net`

The `lvm.conf event_activation` that used to activate these services no
longer works. The only method that is used for automatic activation of volume groups is
event based activation.

### PMDK Library

The Persistent Memory Development Kit (`pmdk`) is a collection of
libraries and tools for simplifying the management and access of persistent memory
devices. This set of libraries are deprecated, including the `-debuginfo`
packages.

The following list of `pmdk`-related binary packages, including the
`nvml` source package, have been deprecated:

- `libpmem`
- `libpmem-devel`
- `libpmem-debug`
- `libpmem2`
- `libpmem2-devel`
- `libpmem2-debug`
- `libpmemblk`
- `libpmemblk-devel`
- `libpmemblk-debug`
- `libpmemlog`
- `libpmemlog-devel`
- `libpmemlog-debug`
- `libpmemobj`
- `libpmemobj-devel`
- `libpmemobj-debug`
- `libpmempool`
- `libpmempool-devel`
- `libpmempool-debug`
- `pmempool`
- `daxio`
- `pmreorder`
- `pmdk-convert`
- `libpmemobj++`
- `libpmemobj++-devel`
- `libpmemobj++-doc`

### `md-linear` and `md-faulty` MD RAID Kernel Modules

The following MD RAID kernel modules have been deprecated:

- `CONFIG_MD_LINEAR` or `md-linear`: Concatenates
  multiple drives so that when a single member disk becomes full, data is written
  to the next disk until all disks are full.
- `CONFIG_MD_FAULTY` or `md-faulty`: Tests a block
  device that occasionally returns read or write errors for testing purposes.

### Virtual Data Optimizer Parameters in `sysfs`

Virtual Data Optimizer (VDO) parameters that appears in `sysfs` have been
deprecated except for the `log_level` parameter. These include the
following:

- All `kvdo` module-level `sysfs` parameters
- All individual `dm-vdo`
  `sysfs` parameters targets specific to VDO

Parameters that are common to all DM targets don't change. Configuration values for
`dm-vdo` targets, which are set by updating the removed module-level
parameters, can no longer be changed.

You can no longer access statistics and configuration values for `dm-vdo`
targets using `sysfs`. However, these values are accessible using
`dmsetup message stats`, `dmsetup status`, and
`dmsetup table` dmsetup commands.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-HA.html -->

## High Availability

The following high availability related features and functionalities are deprecated in Oracle
Linux 9.

### Several Pacemaker Configuration Options

Several Pacemaker configuration options are deprecated.

- Configuring a `score` parameter in order constraints
- Use of the `rkt` container engine in bundles
- Use of `upstart` and `nagios` resources
- The `monthdays`, `weekdays`,
  `weekyears`, `yearsdays` and `moon`
  date specification options when configuring Pacemaker rules
- The `yearsdays` and `moon` duration options for
  configuring Pacemaker rules

The `pcs` command emits a warning when a system is configured to use any
of the deprecated features or options.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-DynamicProgramming.html -->

## Dynamic Programming Languages, Web and Database Servers

The following features and functionalities that are related to dynamic programming, web, and
database servers are deprecated in Oracle Linux 9.

### Berkeley DB (`libdb`)

Deprecation of the Berkely DB (`libdb`) package includes the removal of
cryptographic algorithms and dependencies. Users of `libdb` should
migrate to a different key-value database.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-CompilersandDev.html -->

## Compilers and Development

The following compiler and development related features and functionalities are
deprecated in Oracle Linux 9.

### Redis in Grafana, PCP, and `grafana-pcp`

Use of Redis in Grafana, PCP, and `grafana-pcp` is deprecated and will be
replaced with Valkey.

### `llvm-doc` HTML Content

The HTML content in the `llvm-doc` package is deprecated. See the content
at <https://llvm.org/>.

### Keys Smaller Than 2048-bits in OpenSSL

OpenSSL 3.0 has deprecated keys smaller than 2048 bits. Keys smaller than 2048 bits might
not work in FIPS mode.

### Some PKCS1 v1.5 modes

Some`PKCS1` v1.5 modes aren't approved in FIPS-140-3 for encryption and
are disabled.

### 32-bit `multilib` Linking

Linking against 32-bit `multilib` packages (\*.i686 packages ) are
deprecated.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-IdentityManagementandAuthentication.html -->

## Identity Management and Authentication

The following identity management and authentication features and functionalities are
deprecated in Oracle Linux 9.

### PAM Console

`pam_console` module is deprecated. It grants file permissions and
authentication to users logged in at the physical console or terminals, and adjusts
these privileges based on console login status and user presence.

### BDB backend (in 389-ds-base)

Berkeley Database (BDB) backend is deprecated in `389-ds-base` package,
the 389 Directory Server. As a replacement, Directory Server can now create instances
with Lightning Memory-Mapped Database (LMDB) available as a Technology Preview.

### sss\_ssh\_knownhostsproxy

`sss_ssh_knownhostsproxy`, a utility in the System Security Services
Daemon (SSSD) package, is deprecated.

### libsss\_simpleifp

`libsss_simpleifp` that provides the `libsss_simpleifp.so`
library is deprecated.

### SSSD Files Provider

The SSSD `files` provider, which retrieves user information from local
files such as `/etc/shadow` and group information from
`/etc/groups`, is deprecated and disabled by default in Oracle Linux
9.

To retrieve user and group information from local files with SSSD:

1. Configure SSSD. Choose one of the following options:

   1. Explicitly configure a local domain with the `id_provider=files`
      option in the `sssd.conf` configuration file.

      ```
      [domain/local]
      id_provider=files
      ...
      ```
   2. Enable the `files` provider by setting
      `enable_files_domain=true` in the `sssd.conf`
      configuration file.

      ```
      [sssd]
      enable_files_domain = true
      ```
2. Configure the name services switch.

   ```
   sudo authselect enable-feature with-files-provider
   ```

### OpenLDAP Utility Options

The OpenLDAP project has deprecated the `-h` and `-p` options
in its utilities, and recommends using the `-H` option instead to specify the
LDAP URI.

### `nsslapd-idlistscanlimit` Parameter and Default Value

Because of optimizations to filter reordering, the
`nsslapd-idlistscanlimit` parameter results in having a negative
impact on search performance and is therefore deprecated. Further, the parameter's
default value is changed to `2147483646`

### SMB1 Protocol

Beginning with Samba 4.11, the Server Message Block version 1 (SMB1) protocol is
deprecated because of its insecure features. By default, this protocol is disabled in
both Samba server and client utilities.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-Virtualization.html -->

## Virtualization

The following virtualization related features and functionalities are deprecated in Oracle
Linux 9.

### Signatures Using SHA-1

The use of SHA1-based signatures to perform SecureBoot image verification on UEFI
(PE/COFF) executables is deprecated. Instead, use signatures that are based on SHA-2 or
later.

### Virtual Machine Manager

In place of the deprecated Virtual Machine Manager (`virt-manager`), use
the web console, otherwise known as Cockpit.

### Virtual Machine Snapshots

Support for creating snapshots of VMs is limited only to those that do not use UEFI
firmware. However, the operation might cause the QEMU monitor to become blocked and
affects hypervisor operations.

As an alternative, use external snapshots.

### `libvirtd` Daemon

As a replacement of the deprecated `libvirtd` daemon, use the modular daemons
in the `libvirt` library. For example, the `virtqemud` handles
QEMU drivers.

### Virtual Floppy Driver

The `isa-fdc` driver controls virtual floppy disk devices. To ensure
compatibility with migrated virtual machines (VMs), you should not use floppy disk
devices in virtual machines that you subsequently host on Oracle Linux 9.

### `qcow2-v2` Format

For virtual disk images, use the `qcow2-v3` format instead.

### Legacy CPU Models

The following legacy CPU models are deprecated for use in VMs:

- For Intel® : models prior to Intel® Xeon 55xx and 75xx Processor families (also known
  as Nehalem)
- For AMD: models prior to AMD Opteron G4

To check whether a VM is using a deprecated CPU model, use the `virsh
dominfo` command, and look for a line similar to the following in the
`Messages` section:

```
tainted: use of deprecated configuration settings
deprecated configuration: CPU model 'i486'
```

### RDMA-based Live Migration

In this release, RDMA-based live migration of virtual machines is deprecated.

### Windows 8 and Windows Server 2012 Guest Operating System

The following Windows versions are deprecated as a guest operating system:

- Windows 8
- Windows 8.1
- Windows Server 2012
- Windows Server 2012 R2

These are deprecated because they are no longer supported by Microsoft.

### NIC Device Drivers for iPXE

The following device drivers are deprecated:

- All device drivers in the `ipxe-roms` subpackage
- The following binary files from `ipxe-bootimgs-x86:`
  - /usr/share/ipxe/ipxe-i386.efi
  - /usr/share/ipxe/ipxe-x86\_64.efi
  - /usr/share/ipxe/ipxe.dsk
  - /usr/share/ipxe/ipxe.iso
  - /usr/share/ipxe/ipxe.lkrn
  - /usr/share/ipxe/ipxe.usb

Use the following binary files from the `ipxe-bootimgs` package to provide NIC device drivers for iPXE network boot:

- /usr/share/ipxe/ipxe-snponly-x86\_64.efi
- /usr/share/ipxe/undionly.kpxe

### Intel vGPU

Dividing select Intel vGPUs into multiple virtual GPUs and assigning them to VMs is no longer supported.

### pmem Device Passthrough

The non-volatile memory library (`nvml`) packages are deprecated. When they are removed in a future release, you will be unable to pass persistent memory (`pmem`) devices to VMs. You also will be unable to configure emulated NVDIMM devices backed by volatile memory or files as persistent, but the devices will remain available.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-deprecated-Containers.html -->

## Containers

The following features and functionalities that are related to containers are deprecated in
Oracle Linux 9.

### `containers.conf` for System Connections

The `containers.conf` file is read-only for Podman commands. The
system connections and farm information must be stored in the
`podman.connections.json` file, managed only by Podman.

Podman continues to support the old configuration options such as
`[engine.service_destinations]` and the `[farms]`
section. You can still add connections or farms manually if needed, however, it's not
possible to delete a connection from the `containers.conf` file with the
`podman system connection rm` command.

### `slirp4net`

The `slirp4netns` network mode is deprecated. The `pasta`
network mode is the default network mode for rootless containers.

### `cgroupsv1` in Rootless Containers

Using `cgroupsv1` for rootless containers is deprecated.

Note that `cgroupsv1` is deprecated on Oracle Linux 9. See [cgroupsv1](ol9-deprecated-Kernel.html#ol9.5-deprecated-cgroupsv1).

### `runc` Container Runtime

The `runc` container runtime is deprecated. The default container runtime
is `crun`.

### `pasta` as a Network Name

Using `pasta` as a network name value is deprecated.

### BoltDB Database Backend

The BoltDB database backend is deprecated in favor of the SQLite database backend.

### Oracle Linux 9 Containers on Oracle Linux 7 Hosts

Creating Oracle Linux 9 containers on an Oracle Linux 7 host is unsupported. Attempts to deploy this configuration might succeed, but isn't guaranteed.

### SHA-1 Algorithm Within Podman

Support for using the SHA-11 algorithm to generate the filename of the rootless network
namespace is removed in Podman. You should restart rootless containers that were
configured by using Podman earlier than version 4.1.1. Restarting these containers
rather than just using `slirp4netns` ensures that these containers and
join the network and connect with containers that were created with upgraded Podman
versions.

### CNI Network Stack

The Container Network Interface (CNI) network stack is deprecated. You can use the
Netavark network stack with Podman and other Open Container Initiative (OCI) container
management applications. The Netavark network stack for Podman is also compatible with
advanced Docker functionalities.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9.5-deprecated-packages.html -->

## Deprecated Packages

The support status of deprecated packages remains unchanged within Oracle Linux 9. For more
information about the length of support, see [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

The following packages are deprecated in Oracle Linux 9:

- `aacraid`
- `aajohan-comfortaa-fonts`
- `adwaita-gtk2-theme`
- `adwaita-gtk2-theme`
- `adwaita-qt5`
- `af_key`
- `anaconda-user-help`
- `anaconda-user-help`
- `ant-javamail`
- `apr-util-bdb`
- `aspnetcore-runtime-7.0`
- `aspnetcore-targeting-pack-6.0`
- `aspnetcore-targeting-pack-7.0`
- `atkmm`
- `atlas`
- `atlas-devel`
- `atlas-z14`
- `atlas-z15`
- `authselect-compat`
- `autoconf271`
- `autoconf-latest`
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
- `babl`
- `bind9.18-libs`
- `bitmap-fangsongti-fonts`
- `bnx2`
- `bnx2fc`
- `bnx2i`
- `bogofilter`
- `Box2D`
- `brasero-nautilus`
- `cairomm`
- `cheese`
- `cheese-libs`
- `clucene-contribs-lib`
- `clucene-core`
- `clutter`
- `clutter-gst3`
- `clutter-gtk`
- `cnic`
- `cogl`
- `compat-hesiod`
- `compat-locales-sap`
- `compat-locales-sap-common`
- `compat-openssl11`
- `compat-paratype-pt-sans-fonts-f33-f34`
- `compat-sap-c++-12`
- `compat-sap-c++-13`
- `containernetworking-plugins`
- `containers-common-extra`
- `culmus-aharoni-clm-fonts`
- `culmus-caladings-clm-fonts`
- `culmus-david-clm-fonts`
- `culmus-drugulin-clm-fonts`
- `culmus-ellinia-clm-fonts`
- `culmus-fonts-common`
- `culmus-frank-ruehl-clm-fonts`
- `culmus-hadasim-clm-fonts`
- `culmus-miriam-clm-fonts`
- `culmus-miriam-mono-clm-fonts`
- `culmus-nachlieli-clm-fonts`
- `culmus-simple-clm-fonts`
- `culmus-stamashkenaz-clm-fonts`
- `culmus-stamsefarad-clm-fonts`
- `culmus-yehuda-clm-fonts`
- `curl-minimal`
- `daxio`
- `dbus-glib`
- `dbus-glib-devel`
- `devhelp`
- `devhelp-libs`
- `dhcp-client`
- `dhcp-common`
- `dhcp-relay`
- `dhcp-server`
- `dotnet-apphost-pack-6.0`
- `dotnet-apphost-pack-7.0`
- `dotnet-hostfxr-6.0`
- `dotnet-hostfxr-7.0`
- `dotnet-runtime-6.0`
- `dotnet-runtime-7.0`
- `dotnet-sdk-6.0`
- `dotnet-sdk-7.0`
- `dotnet-targeting-pack-6.0`
- `dotnet-targeting-pack-7.0`
- `dotnet-templates-6.0`
- `dotnet-templates-7.0`
- `double-conversion`
- `efs-utils`
- `enchant`
- `enchant-devel`
- `eog`
- `evince`
- `evince-libs`
- `evince-nautilus`
- `evince-previewer`
- `evince-thumbnailer`
- `evolution`
- `evolution-bogofilter`
- `evolution-data-server-ui`
- `evolution-data-server-ui-devel`
- `evolution-devel`
- `evolution-ews`
- `evolution-ews-langpacks`
- `evolution-help`
- `evolution-langpacks`
- `evolution-mapi`
- `evolution-mapi-langpacks`
- `evolution-pst`
- `evolution-spamassassin`
- `festival`
- `festival-data`
- `festvox-slt-arctic-hts`
- `firefox`
- `firefox`
- `firefox-x11`
- `firewire-core`
- `flite`
- `flite-devel`
- `fltk`
- `flute`
- `fontawesome-fonts`
- `gc`
- `gcr-base`
- `gedit`
- `gedit-plugin-bookmarks`
- `gedit-plugin-bracketcompletion`
- `gedit-plugin-codecomment`
- `gedit-plugin-colorpicker`
- `gedit-plugin-colorschemer`
- `gedit-plugin-commander`
- `gedit-plugin-drawspaces`
- `gedit-plugin-findinfiles`
- `gedit-plugin-joinlines`
- `gedit-plugin-multiedit`
- `gedit-plugins`
- `gedit-plugins-data`
- `gedit-plugin-sessionsaver`
- `gedit-plugin-smartspaces`
- `gedit-plugin-synctex`
- `gedit-plugin-terminal`
- `gedit-plugin-textsize`
- `gedit-plugin-translate`
- `gedit-plugin-wordcompletion`
- `ghc-srpm-macros`
- `ghostscript-x11`
- `git-p4`
- `glade`
- `glade-libs`
- `glibmm24`
- `gl-manpages`
- `gnome-backgrounds`
- `gnome-backgrounds-extras`
- `gnome-common`
- `gnome-logs`
- `gnome-photos`
- `gnome-photos-tests`
- `gnome-screenshot`
- `gnome-session-xsession`
- `gnome-shell-extension-panel-favorites`
- `gnome-shell-extension-updates-dialog`
- `gnome-terminal`
- `gnome-terminal-nautilus`
- `gnome-themes-extra`
- `gnome-tweaks`
- `gnome-video-effects`
- `google-noto-cjk-fonts-common`
- `google-noto-sans-cjk-ttc-fonts`
- `google-noto-sans-khmer-ui-fonts`
- `google-noto-sans-lao-ui-fonts`
- `google-noto-sans-thai-ui-fonts`
- `gspell`
- `gtk2`
- `gtk2-devel`
- `gtk2-devel-docs`
- `gtk2-immodules`
- `gtk2-immodule-xim`
- `gtkmm30`
- `gtksourceview4`
- `gtksourceview4`
- `gubbi-fonts`
- `gvfs-devel`
- `ha-openstack-support`
- `hesiod`
- `hexchat`
- `highcontrast-icon-theme`
- `http-parser`
- `ibus-gtk2`
- `initial-setup`
- `initial-setup-gui`
- `inkscape`
- `inkscape-docs`
- `inkscape-view`
- `iptables-devel`
- `iptables-libs`
- `iptables-nft`
- `iptables-nft-services`
- `iptables-utils`
- `iputils-ninfod`
- `ipxe-roms`
- `jakarta-activation2`
- `jboss-jaxrs-2.0-api`
- `jboss-logging`
- `jboss-logging-tools`
- `jdeparser`
- `julietaula-montserrat-fonts`
- `kacst-art-fonts`
- `kacst-book-fonts`
- `kacst-decorative-fonts`
- `kacst-digital-fonts`
- `kacst-farsi-fonts`
- `kacst-fonts-common`
- `kacst-letter-fonts`
- `kacst-naskh-fonts`
- `kacst-office-fonts`
- `kacst-one-fonts`
- `kacst-pen-fonts`
- `kacst-poster-fonts`
- `kacst-qurn-fonts`
- `kacst-screen-fonts`
- `kacst-title-fonts`
- `kacst-titlel-fonts`
- `khmer-os-battambang-fonts`
- `khmer-os-bokor-fonts`
- `khmer-os-content-fonts`
- `khmer-os-fasthand-fonts`
- `khmer-os-freehand-fonts`
- `khmer-os-handwritten-fonts`
- `khmer-os-metal-chrieng-fonts`
- `khmer-os-muol-fonts`
- `khmer-os-muol-fonts-all`
- `khmer-os-muol-pali-fonts`
- `khmer-os-siemreap-fonts`
- `kmod-kvdo`
- `lasso`
- `libabw`
- `libadwaita-qt5`
- `libbase`
- `libblockdev-kbd`
- `libcanberra-gtk2`
- `libcdr`
- `libcmis`
- `libdazzle`
- `libdb`
- `libdb-devel`
- `libdb-utils`
- `libdmx`
- `libepubgen`
- `libetonyek`
- `libexttextcat`
- `libfonts`
- `libformula`
- `libfreehand`
- `libgdata`
- `libgdata-devel`
- `libgnomekbd`
- `libiscsi`
- `libiscsi-utils`
- `liblangtag`
- `liblangtag-data`
- `liblayout`
- `libloader`
- `libmatchbox`
- `libmspub`
- `libmwaw`
- `libnsl2`
- `libnumbertext`
- `libodfgen`
- `liborcus`
- `libotr`
- `libpagemaker`
- `libpmem`
- `libpmem2`
- `libpmem2-debug`
- `libpmem2-devel`
- `libpmemblk`
- `libpmemblk-debug`
- `libpmemblk-devel`
- `libpmem-debug`
- `libpmem-devel`
- `libpmemlog`
- `libpmemlog-debug`
- `libpmemlog-devel`
- `libpmemobj`
- `libpmemobj-debug`
- `libpmemobj++-devel`
- `libpmemobj-devel`
- `libpmemobj++-doc`
- `libpmempool`
- `libpmempool-debug`
- `libpmempool-devel`
- `libpng15`
- `libpst-libs`
- `libqxp`
- `LibRaw`
- `libreoffice`
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
- `libreoffice-sdk`
- `libreoffice-sdk-doc`
- `libreoffice-ure`
- `libreoffice-ure-common`
- `libreoffice-voikko`
- `libreoffice-wiki-publisher`
- `libreoffice-writer`
- `libreoffice-x11`
- `libreoffice-xsltfilter`
- `librepository`
- `librevenge`
- `librevenge-gdb`
- `libserializer`
- `libsigc++20`
- `libsigsegv`
- `libsmbios`
- `libsoup`
- `libsoup-devel`
- `libstaroffice`
- `libstemmer`
- `libstoragemgmt-smis-plugin`
- `libteam`
- `libuser`
- `libuser-devel`
- `libvisio`
- `libvisual`
- `libwpd`
- `libwpe`
- `libwpe-devel`
- `libwpg`
- `libwps`
- `libxcrypt-compat`
- `libxklavier`
- `libXp`
- `libXp-devel`
- `libXScrnSaver`
- `libXScrnSaver-devel`
- `libXxf86dga`
- `libXxf86dga-devel`
- `libzmf`
- `lklug-fonts`
- `lohit-gurmukhi-fonts`
- `lpsolve`
- `man-pages-overrides`
- `mcpp`
- `memkind`
- `mesa-libGLw`
- `mesa-libGLw-devel`
- `mlocate`
- `mod_auth_mellon`
- `mod_jk`
- `mod_security`
- `mod_security_crs`
- `mod_security-mlogc`
- `motif`
- `motif-devel`
- `mythes`
- `mythes-bg`
- `mythes-ca`
- `mythes-cs`
- `mythes-da`
- `mythes-de`
- `mythes-el`
- `mythes-en`
- `mythes-eo`
- `mythes-es`
- `mythes-fr`
- `mythes-ga`
- `mythes-hu`
- `mythes-it`
- `mythes-lv`
- `mythes-nb`
- `mythes-nl`
- `mythes-nn`
- `mythes-pl`
- `mythes-pt`
- `mythes-ro`
- `mythes-ru`
- `mythes-sk`
- `mythes-sl`
- `mythes-sv`
- `mythes-uk`
- `navilu-fonts`
- `nbdkit-gzip-filter`
- `neon`
- `NetworkManager-initscripts-updown`
- `nginx`
- `nginx-all-modules`
- `nginx-core`
- `nginx-filesystem`
- `nginx-mod-devel`
- `nginx-mod-http-image-filter`
- `nginx-mod-http-perl`
- `nginx-mod-http-xslt-filter`
- `nginx-mod-mail`
- `nginx-mod-stream`
- `nispor`
- `nscd`
- `nvme-stas`
- `opal-firmware`
- `opal-prd`
- `opal-utils`
- `openal-soft`
- `openchange`
- `openscap-devel`
- `openscap-python3`
- `openslp-server`
- `overpass-fonts`
- `paktype-naqsh-fonts`
- `paktype-tehreer-fonts`
- `pam_ssh_agent_auth`
- `pangomm`
- `pentaho-libxml`
- `pentaho-reporting-flow-engine`
- `perl-AnyEvent`
- `perl-B-Hooks-EndOfScope`
- `perl-Class-Accessor`
- `perl-Class-Data-Inheritable`
- `perl-Class-Singleton`
- `perl-Class-Tiny`
- `perl-Crypt-OpenSSL-Bignum`
- `perl-Crypt-OpenSSL-Random`
- `perl-Crypt-OpenSSL-RSA`
- `perl-Date-ISO8601`
- `perl-DateTime`
- `perl-DateTime-Format-Builder`
- `perl-DateTime-Format-ISO8601`
- `perl-DateTime-Format-Strptime`
- `perl-DateTime-Locale`
- `perl-DateTime-TimeZone`
- `perl-DateTime-TimeZone-SystemV`
- `perl-DateTime-TimeZone-Tzfile`
- `perl-DB_File`
- `perl-Devel-CallChecker`
- `perl-Devel-Caller`
- `perl-Devel-LexAlias`
- `perl-Digest-SHA1`
- `perl-Dist-CheckConflicts`
- `perl-DynaLoader-Functions`
- `perl-Encode-Detect`
- `perl-Eval-Closure`
- `perl-Exception-Class`
- `perl-File-chdir`
- `perl-File-Copy-Recursive`
- `perl-File-Find-Object`
- `perl-File-Find-Rule`
- `perl-HTML-Tree`
- `perl-Importer`
- `perl-Mail-AuthenticationResults`
- `perl-Mail-DKIM`
- `perl-Mail-Sender`
- `perl-Mail-SPF`
- `perl-MIME-Types`
- `perl-Module-Implementation`
- `perl-Module-Pluggable`
- `perl-namespace-autoclean`
- `perl-namespace-clean`
- `perl-NetAddr-IP`
- `perl-Net-CIDR-Lite`
- `perl-Net-DNS`
- `perl-Number-Compare`
- `perl-Package-Stash`
- `perl-Package-Stash-XS`
- `perl-PadWalker`
- `perl-Params-Classify`
- `perl-Params-Validate`
- `perl-Params-ValidationCompiler`
- `perl-Perl-Destruct-Level`
- `perl-Ref-Util`
- `perl-Ref-Util-XS`
- `perl-Scope-Guard`
- `perl-Specio`
- `perl-Sub-Identify`
- `perl-Sub-Info`
- `perl-Sub-Name`
- `perl-Switch`
- `perl-Sys-CPU`
- `perl-Sys-MemInfo`
- `perl-Test-LongString`
- `perl-Test-Taint`
- `perl-Variable-Magic`
- `perl-XML-DOM`
- `perl-XML-RegExp`
- `perl-XML-Twig`
- `pinfo`
- `pki-jackson-annotations`
- `pki-jackson-core`
- `pki-jackson-databind`
- `pki-jackson-jaxrs-json-provider`
- `pki-jackson-jaxrs-providers`
- `pki-jackson-module-jaxb-annotations`
- `pki-resteasy-client`
- `pki-resteasy-core`
- `pki-resteasy-jackson2-provider`
- `pki-resteasy-servlet-initializer`
- `plymouth-theme-charge`
- `pmdk-convert`
- `pmempool`
- `podman-plugins`
- `poppler-qt5`
- `postgresql-test-rpm-macros`
- `power-profiles-daemon`
- `pulseaudio-module-x11`
- `python3.11`
- `python3.11-cffi`
- `python3.11-charset-normalizer`
- `python3.11-cryptography`
- `python3.11-devel`
- `python3.11-idna`
- `python3.11-libs`
- `python3.11-lxml`
- `python3.11-mod_wsgi`
- `python3.11-numpy`
- `python3.11-numpy-f2py`
- `python3.11-pip`
- `python3.11-pip-wheel`
- `python3.11-ply`
- `python3.11-psycopg2`
- `python3.11-pycparser`
- `python3.11-PyMySQL`
- `python3.11-PyMySQL+rsa`
- `python3.11-pysocks`
- `python3.11-pyyaml`
- `python3.11-requests`
- `python3.11-requests+security`
- `python3.11-requests+socks`
- `python3.11-scipy`
- `python3.11-setuptools`
- `python3.11-setuptools-wheel`
- `python3.11-six`
- `python3.11-tkinter`
- `python3.11-urllib3`
- `python3.11-wheel`
- `python3.12-PyMySQL+rsa`
- `python3-bind`
- `python3-chardet`
- `python3-lasso`
- `python3-libproxy`
- `python3-netifaces`
- `python3-nispor`
- `python3-py`
- `python3-pycdlib`
- `python3-pycurl`
- `python3-pyqt5-sip`
- `python3-pyrsistent`
- `python3-pysocks`
- `python3-pytz`
- `python3-pywbem`
- `python3-qt5`
- `python3-qt5-base`
- `python3-requests+security`
- `python3-requests+socks`
- `python3-scour`
- `python3-toml`
- `python3-tomli`
- `python3-tracer`
- `python3-wx-siplib`
- `python-botocore`
- `python-gflags`
- `python-netifaces`
- `python-pyroute2`
- `python-qt5-rpm-macros`
- `qgnomeplatform`
- `qla4xxx`
- `qt5`
- `qt5-assistant`
- `qt5-designer`
- `qt5-devel`
- `qt5-doctools`
- `qt5-linguist`
- `qt5-qdbusviewer`
- `qt5-qt3d`
- `qt5-qt3d-devel`
- `qt5-qt3d-doc`
- `qt5-qt3d-examples`
- `qt5-qtbase`
- `qt5-qtbase-common`
- `qt5-qtbase-devel`
- `qt5-qtbase-doc`
- `qt5-qtbase-examples`
- `qt5-qtbase-gui`
- `qt5-qtbase-mysql`
- `qt5-qtbase-odbc`
- `qt5-qtbase-postgresql`
- `qt5-qtbase-private-devel`
- `qt5-qtbase-static`
- `qt5-qtconnectivity`
- `qt5-qtconnectivity-devel`
- `qt5-qtconnectivity-doc`
- `qt5-qtconnectivity-examples`
- `qt5-qtdeclarative`
- `qt5-qtdeclarative-devel`
- `qt5-qtdeclarative-doc`
- `qt5-qtdeclarative-examples`
- `qt5-qtdeclarative-static`
- `qt5-qtdoc`
- `qt5-qtgraphicaleffects`
- `qt5-qtgraphicaleffects-doc`
- `qt5-qtimageformats`
- `qt5-qtimageformats-doc`
- `qt5-qtlocation`
- `qt5-qtlocation-devel`
- `qt5-qtlocation-doc`
- `qt5-qtlocation-examples`
- `qt5-qtmultimedia`
- `qt5-qtmultimedia-devel`
- `qt5-qtmultimedia-doc`
- `qt5-qtmultimedia-examples`
- `qt5-qtquickcontrols`
- `qt5-qtquickcontrols2`
- `qt5-qtquickcontrols2-devel`
- `qt5-qtquickcontrols2-doc`
- `qt5-qtquickcontrols2-examples`
- `qt5-qtquickcontrols-doc`
- `qt5-qtquickcontrols-examples`
- `qt5-qtscript`
- `qt5-qtscript-devel`
- `qt5-qtscript-doc`
- `qt5-qtscript-examples`
- `qt5-qtsensors`
- `qt5-qtsensors-devel`
- `qt5-qtsensors-doc`
- `qt5-qtsensors-examples`
- `qt5-qtserialbus`
- `qt5-qtserialbus-devel`
- `qt5-qtserialbus-doc`
- `qt5-qtserialbus-examples`
- `qt5-qtserialport`
- `qt5-qtserialport-devel`
- `qt5-qtserialport-doc`
- `qt5-qtserialport-examples`
- `qt5-qtsvg`
- `qt5-qtsvg-devel`
- `qt5-qtsvg-doc`
- `qt5-qtsvg-examples`
- `qt5-qttools`
- `qt5-qttools-common`
- `qt5-qttools-devel`
- `qt5-qttools-doc`
- `qt5-qttools-examples`
- `qt5-qttools-libs-designer`
- `qt5-qttools-libs-designercomponents`
- `qt5-qttools-libs-help`
- `qt5-qttools-static`
- `qt5-qttranslations`
- `qt5-qtwayland`
- `qt5-qtwayland-devel`
- `qt5-qtwayland-doc`
- `qt5-qtwayland-examples`
- `qt5-qtwebchannel`
- `qt5-qtwebchannel-devel`
- `qt5-qtwebchannel-doc`
- `qt5-qtwebchannel-examples`
- `qt5-qtwebsockets`
- `qt5-qtwebsockets-devel`
- `qt5-qtwebsockets-doc`
- `qt5-qtwebsockets-examples`
- `qt5-qtx11extras`
- `qt5-qtx11extras-devel`
- `qt5-qtx11extras-doc`
- `qt5-qtxmlpatterns`
- `qt5-qtxmlpatterns-devel`
- `qt5-qtxmlpatterns-doc`
- `qt5-qtxmlpatterns-examples`
- `qt5-rpm-macros`
- `qt5-srpm-macros`
- `raptor2`
- `rasqal`
- `redis`
- `redis-devel`
- `redis-doc`
- `redland`
- `rpmlint`
- `runc`
- `saab-fonts`
- `sac`
- `scap-workbench`
- `sendmail`
- `sendmail-cf`
- `sendmail-doc`
- `setxkbmap`
- `sgabios`
- `sgabios-bin`
- `sil-scheherazade-fonts`
- `spamassassin`
- `speech-tools-libs`
- `suitesparse`
- `sushi`
- `team`
- `teamd`
- `thai-scalable-fonts-common`
- `thai-scalable-garuda-fonts`
- `thai-scalable-kinnari-fonts`
- `thai-scalable-loma-fonts`
- `thai-scalable-norasi-fonts`
- `thai-scalable-purisa-fonts`
- `thai-scalable-sawasdee-fonts`
- `thai-scalable-tlwgmono-fonts`
- `thai-scalable-tlwgtypewriter-fonts`
- `thai-scalable-tlwgtypist-fonts`
- `thai-scalable-tlwgtypo-fonts`
- `thai-scalable-umpush-fonts`
- `thunderbird`
- `tigervnc`
- `tigervnc-icons`
- `tigervnc-license`
- `tigervnc-selinux`
- `tigervnc-server`
- `tigervnc-server-minimal`
- `tigervnc-server-module`
- `tracer-common`
- `ucs-miscfixed-fonts`
- `usb_modeswitch`
- `usb_modeswitch-data`
- `usbredir-server`
- `webkit2gtk3`
- `webkit2gtk3-devel`
- `webkit2gtk3-jsc`
- `webkit2gtk3-jsc-devel`
- `wpebackend-fdo`
- `wpebackend-fdo-devel`
- `xmlsec1-gcrypt`
- `xmlsec1-gcrypt-devel`
- `xmlsec1-gnutls`
- `xmlsec1-gnutls-devel`
- `xorg-x11-drivers`
- `xorg-x11-drv-dummy`
- `xorg-x11-drv-evdev`
- `xorg-x11-drv-fbdev`
- `xorg-x11-drv-libinput`
- `xorg-x11-drv-v4l`
- `xorg-x11-drv-vmware`
- `xorg-x11-drv-wacom`
- `xorg-x11-drv-wacom-serial-support`
- `xorg-x11-server-common`
- `xorg-x11-server-utils`
- `xorg-x11-server-Xdmx`
- `xorg-x11-server-Xephyr`
- `xorg-x11-server-Xnest`
- `xorg-x11-server-Xorg`
- `xorg-x11-server-Xvfb`
- `xorg-x11-utils`
- `xorg-x11-xbitmaps`
- `xorg-x11-xinit`
- `xorg-x11-xinit-session`
- `xsane`
- `xsane-common`
- `xxhash`
- `xxhash-libs`
- `yelp`
- `yelp-libs`
- `ypbind`
- `ypserv`
- `yp-tools`
- `zhongyi-song-fonts`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-KnownIssues.html -->

## 5 Known Issues

This
chapter describes known issues that you may encounter when installing and using the Oracle
Linux 9 software. Unless indicated otherwise, the issues apply to both x86\_64 and aarch64
systems. Information that pertains only to a specific platform is also noted accordingly.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-InstallationIssues.html -->

## Installation Issues

The following are known installation issues for Oracle Linux 9.

### Error Messages Displayed While Removing RHCK

When you issue the command `sudo dnf remove
kernel-core-version` to remove the Red Hat Compatible Kernel
(RHCK) from the system, error messages similar to the following example might be
generated:

```
...
Erasing   : kernel-core-version              4/4
warning: file /lib/modules/version/modules.builtin.modinfo:
 No such file or directory
...
```

You can ignore the messages. At the end of the operation, all RHCK related files are removed
successfully.

Bug ID 35964185

### (aarch64) Minimum XFS File System Size During Install Is 300 MB

The more recent version of the `xfsprogs` package that's included on the Oracle Linux 9.7 ISO for Arm platforms sets a minimum XFS file system size of 300 MB. This limit isn't applied when installing on x86\_64 platforms.

Because the x86\_64 ISO includes RHCK, an earlier version of `xfsprogs` is
available to maintain compatibility. On aarch64, only UEK is available and a newer
version of `xfsprogs` is included. The 300 MB limit is set by the newer
version of `xfsprogs` included with UEK 8.

(Bug 37832961)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-VirtualizationIssues.html -->

## Virtualization Issues

The following are known virtualization issues for Oracle Linux 9

### KVM Virtual Machines Panic When Started on Oracle Linux 9 Hosts

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

### Virtual Machines Fail to Start at Boot Because the `virbr0` Interface Isn't Available

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol9-KernelIssues.html -->

## Kernel Issues

The following are known kernel issues in Oracle Linux 9.

### Kdump Might Fail on Some AMD Hardware

Kdump might fail on some AMD hardware that's running the current Oracle Linux
release. Impacted hardware includes the AMD EPYC CPU servers.

To work around this issue, modify the `/etc/sysconfig/kdump` configuration
file and remove the `iommu=off` command line option from the
`KDUMP_COMMANDLINE_APPEND` variable. Restart the `kdump`
service for the changes to take effect.

This issue appears to affect systems running RHCK.

(Bug ID 31274238, 34211826, 34312626)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/issue-35270637_35034465.html -->

## (aarch64) Some GUI Elements Aren't Displayed During Installation and Boot Using VGA Output

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/issue-34050377.html -->

## Certain SEV Guest Configurations Might Cause Hypervisor CPU Soft-Lockup Warnings

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/issue-36028061.html -->

## Systems With Btrfs Fail to Boot in FIPS Mode

When booted in FIPS mode, a system using Btrfs fails with the following message:

```
FATAL: FIPS integrity test failed
Refusing to continue
```

(Bug ID 36028061)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/issue-36512929.html -->

## Leapp Upgrade Messages About Unmounted `/proc` File System

Warning messages are displayed in the package installation logs during Leapp preupgrade and
Leapp
upgrade:

```
/proc/ is not mounted. This is not a supported mode of operation. Please fix
your invocation environment to mount /proc/ and /sys/ properly. Proceeding anyway.
Your mileage may vary.
```

During upgrade `/proc` is mounted in a temporary chroot as part of the
preparation for the upgrade rootfs. This process is normal and the warning messages aren't
indicative of any real problem. You can ignore warning messages about the
`/proc` file system.

(Bug ID 36512929)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/issue-37290712.html -->

## Openssl Tool Returns Unable to Print EC Key in FIPS Mode

When FIPS mode is enabled on a system, the openssl tool is unable to print
an Elliptic Curve (EC) key, when using the following command:

```
openssl ec -in ecp256.pem -noout -text
```

The command fails with the message:

```
unable to print EC key
```

Explicitly loading the `fips` provider when running the command works around
this issue, for example:

```
openssl ec -provider=fips -in ecp256.pem  -noout -text
```

(Bug ID 37290712)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol-PackageChangesfromtheUpstreamRelease.html -->

## 6 Package Changes From the Upstream Release

The following sections list the changes to binary and source
packages from the upstream release.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol-ChangestoBinaryPackages.html -->

## Changes to Binary Packages

This section contains information about the removed, modified, and new binary packages in this release. For information about the source package changes, see [Changes to Source Packages](ol-ChangestoSourcePackages.html#ol9-packages-source).

### Added Binary Packages for BaseOS by Oracle

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
- `kernel-uek-debug-modules-core`
- `kernel-uek-debug-modules-desktop`
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

### Added Binary Packages for AppStream by Oracle

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

### Added Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages have been added to CodeReady Linux Builder by Oracle:

- `oraclelinux-sb-certs`
- `xapian-core`

### Modified BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been modified:

- `alternatives`
- `audispd-plugins`
- `audispd-plugins-zos`
- `audit`
- `audit-libs`
- `autofs`
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
- `initscripts`
- `initscripts-rename-device`
- `initscripts-service`
- `iputils`
- `irqbalance`
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
- `kernel`
- `kernel-abi-stablelists`
- `kernel-core`
- `kernel-debug`
- `kernel-debug-core`
- `kernel-debug-modules`
- `kernel-debug-modules-core`
- `kernel-debug-modules-extra`
- `kernel-debug-uki-virt`
- `kernel-modules`
- `kernel-modules-core`
- `kernel-modules-extra`
- `kernel-tools`
- `kernel-tools-libs`
- `kernel-uki-virt`
- `kernel-uki-virt-addons`
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
- `libblkid`
- `libdb`
- `libdnf`
- `libertas-sd8686-firmware`
- `libertas-sd8787-firmware`
- `libertas-usb8388-firmware`
- `libertas-usb8388-olpc-firmware`
- `libfdisk`
- `libgcc`
- `libgfortran`
- `libgomp`
- `libipa_hbac`
- `libkadm5`
- `libkcapi`
- `libkcapi-hmaccalc`
- `libmount`
- `libnfsidmap`
- `libnsl`
- `libquadmath`
- `libreport-filesystem`
- `libsmartcols`
- `libsss_autofs`
- `libsss_certmap`
- `libsss_idmap`
- `libsss_nss_idmap`
- `libsss_simpleifp`
- `libsss_sudo`
- `libstdc++`
- `libtracecmd`
- `libuuid`
- `linux-firmware`
- `linux-firmware-core`
- `linux-firmware-whence`
- `liquidio-firmware`
- `mcelog`
- `mdadm`
- `microcode_ctl`
- `netconsole-service`
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
- `nfs-utils`
- `nscd`
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
- `pam`
- `pcre2`
- `pcre2-syntax`
- `polkit`
- `polkit-libs`
- `procps-ng`
- `procps-ng-i18n`
- `python3-cffi`
- `python3-chardet`
- `python3-configshell`
- `python3-cryptography`
- `python3-dmidecode`
- `python3-dnf`
- `python3-dnf-plugin-post-transaction-actions`
- `python3-dnf-plugins-core`
- `python3-dnf-plugin-versionlock`
- `python3-firewall`
- `python3-hawkey`
- `python3-idna`
- `python3-libdnf`
- `python3-libipa_hbac`
- `python3-libsss_nss_idmap`
- `python3-ply`
- `python3-pycparser`
- `python3-pysocks`
- `python3-pyyaml`
- `python3-six`
- `python3-sss`
- `python3-sssdconfig`
- `python3-sss-murmur`
- `readonly-root`
- `redhat-release`
- `rhel-net-naming-sysattrs`
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
- `sssd-passkey`
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
- `trace-cmd`
- `tuned`
- `tuned-profiles-cpu-partitioning`
- `unzip`
- `util-linux`
- `util-linux-core`
- `util-linux-user`
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
- `cups-filters-devel`
- `dotnet-sdk-6.0-source-built-artifacts`
- `dotnet-sdk-7.0-source-built-artifacts`
- `dotnet-sdk-8.0-source-built-artifacts`
- `dotnet-sdk-9.0-source-built-artifacts`
- `edk2-aarch64`
- `edk2-tools`
- `edk2-tools-doc`
- `expect-devel`
- `fwupd-devel`
- `gcc-plugin-devel`
- `gdm-devel`
- `gdm-pam-extensions-devel`
- `glibc-benchtests`
- `glibc-nss-devel`
- `glibc-static`
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
- `java-17-openjdk-demo-slowdebug`
- `java-17-openjdk-devel-fastdebug`
- `java-17-openjdk-devel-slowdebug`
- `java-17-openjdk-fastdebug`
- `java-17-openjdk-headless-fastdebug`
- `java-17-openjdk-headless-slowdebug`
- `java-17-openjdk-jmods-fastdebug`
- `java-17-openjdk-jmods-slowdebug`
- `java-17-openjdk-slowdebug`
- `java-17-openjdk-src-fastdebug`
- `java-17-openjdk-src-slowdebug`
- `java-17-openjdk-static-libs-fastdebug`
- `java-17-openjdk-static-libs-slowdebug`
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
- `kernel-cross-headers`
- `kernel-tools-libs-devel`
- `kmod-devel`
- `libdb-cxx`
- `libdb-cxx-devel`
- `libdb-devel-doc`
- `libdb-sql`
- `libdb-sql-devel`
- `libdnf-devel`
- `libfdisk-devel`
- `libguestfs-devel`
- `libguestfs-gobject`
- `libguestfs-gobject-devel`
- `libguestfs-man-pages-ja`
- `libguestfs-man-pages-uk`
- `libnfsidmap-devel`
- `libperf`
- `librados-devel`
- `libradospp-devel`
- `librbd-devel`
- `libreoffice-sdk`
- `libreoffice-sdk-doc`
- `libsmartcols-devel`
- `libsss_nss_idmap-devel`
- `libstdc++-static`
- `libtracecmd-devel`
- `libudisks2-devel`
- `libvirt-daemon-plugin-sanlock`
- `libvirt-devel`
- `libvirt-docs`
- `lua-guestfs`
- `munge-devel`
- `NetworkManager-libnm-devel`
- `nss_db`
- `nss_hesiod`
- `ocaml-libguestfs`
- `ocaml-libguestfs-devel`
- `OpenIPMI-devel`
- `openscap-engine-sce-devel`
- `PackageKit-glib-devel`
- `pcre2-tools`
- `php-libguestfs`
- `procps-ng-devel`
- `python3-ipatests`
- `python3-mpich`
- `python3-psutil-tests`
- `python-packaging-doc`
- `ruby-libguestfs`
- `sanlock-devel`
- `sendmail-milter`
- `sendmail-milter-devel`
- `tog-pegasus-devel`
- `virt-v2v-man-pages-ja`
- `virt-v2v-man-pages-uk`
- `WALinuxAgent-cvm`

### Modified AppStream Binary Packages

The following binary packages from the AppStream upstream release have been modified:

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
- `aspnetcore-runtime-7.0`
- `aspnetcore-runtime-8.0`
- `aspnetcore-runtime-9.0`
- `aspnetcore-runtime-dbg-8.0`
- `aspnetcore-runtime-dbg-9.0`
- `aspnetcore-targeting-pack-6.0`
- `aspnetcore-targeting-pack-7.0`
- `aspnetcore-targeting-pack-8.0`
- `aspnetcore-targeting-pack-9.0`
- `audit-libs-devel`
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
- `bind`
- `bind9.18-dyndb-ldap`
- `bind-chroot`
- `bind-dnssec-doc`
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
- `clang-resource-filesystem`
- `cloud-init`
- `cockpit-composer`
- `cockpit-machines`
- `cockpit-packagekit`
- `cockpit-session-recording`
- `cockpit-storaged`
- `compat-libgfortran-48`
- `compat-openssl11`
- `containers-common`
- `containers-common-extra`
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
- `dnf-bootc`
- `dotnet-apphost-pack-6.0`
- `dotnet-apphost-pack-7.0`
- `dotnet-apphost-pack-8.0`
- `dotnet-apphost-pack-9.0`
- `dotnet-host`
- `dotnet-hostfxr-6.0`
- `dotnet-hostfxr-7.0`
- `dotnet-hostfxr-8.0`
- `dotnet-hostfxr-9.0`
- `dotnet-runtime-6.0`
- `dotnet-runtime-7.0`
- `dotnet-runtime-8.0`
- `dotnet-runtime-9.0`
- `dotnet-runtime-dbg-8.0`
- `dotnet-runtime-dbg-9.0`
- `dotnet-sdk-6.0`
- `dotnet-sdk-7.0`
- `dotnet-sdk-8.0`
- `dotnet-sdk-9.0`
- `dotnet-sdk-aot-9.0`
- `dotnet-sdk-dbg-8.0`
- `dotnet-sdk-dbg-9.0`
- `dotnet-targeting-pack-6.0`
- `dotnet-targeting-pack-7.0`
- `dotnet-targeting-pack-8.0`
- `dotnet-targeting-pack-9.0`
- `dotnet-templates-6.0`
- `dotnet-templates-7.0`
- `dotnet-templates-8.0`
- `dotnet-templates-9.0`
- `dracut-caps`
- `dracut-live`
- `edk2-ovmf`
- `efi-srpm-macros`
- `expect`
- `fapolicyd`
- `fapolicyd-selinux`
- `firefox`
- `firefox-x11`
- `firewall-applet`
- `firewall-config`
- `fwupd-plugin-flashrom`
- `galera`
- `gcc`
- `gcc-c++`
- `gcc-gfortran`
- `gcc-offload-nvptx`
- `gcc-plugin-annobin`
- `gcc-toolset-12-gcc`
- `gcc-toolset-12-gcc-c++`
- `gcc-toolset-12-gcc-gfortran`
- `gcc-toolset-12-gcc-plugin-annobin`
- `gcc-toolset-12-gcc-plugin-devel`
- `gcc-toolset-12-libasan-devel`
- `gcc-toolset-12-libatomic-devel`
- `gcc-toolset-12-libgccjit`
- `gcc-toolset-12-libgccjit-devel`
- `gcc-toolset-12-libgccjit-docs`
- `gcc-toolset-12-libitm-devel`
- `gcc-toolset-12-liblsan-devel`
- `gcc-toolset-12-libquadmath-devel`
- `gcc-toolset-12-libstdc++-devel`
- `gcc-toolset-12-libstdc++-docs`
- `gcc-toolset-12-libtsan-devel`
- `gcc-toolset-12-libubsan-devel`
- `gcc-toolset-12-offload-nvptx`
- `gcc-toolset-13-binutils`
- `gcc-toolset-13-binutils-devel`
- `gcc-toolset-13-binutils-gold`
- `gdb`
- `gdb-doc`
- `gdb-gdbserver`
- `gdb-headless`
- `gdb-minimal`
- `gdm`
- `glibc-devel`
- `glibc-doc`
- `glibc-headers`
- `glibc-locale-source`
- `glibc-utils`
- `gnome-session`
- `gnome-session-wayland-session`
- `gnome-session-xsession`
- `gnome-shell-extension-background-logo`
- `golang`
- `golang-bin`
- `golang-docs`
- `golang-misc`
- `golang-race`
- `golang-src`
- `golang-tests`
- `go-toolset`
- `gpsd-minimal`
- `gpsd-minimal-clients`
- `httpd`
- `httpd-core`
- `httpd-devel`
- `httpd-filesystem`
- `httpd-manual`
- `httpd-tools`
- `idm-pki-acme`
- `idm-pki-base`
- `idm-pki-ca`
- `idm-pki-java`
- `idm-pki-kra`
- `idm-pki-server`
- `idm-pki-tools`
- `initial-setup`
- `initial-setup-gui`
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
- `iputils-ninfod`
- `java-11-openjdk`
- `java-11-openjdk-demo`
- `java-11-openjdk-devel`
- `java-11-openjdk-headless`
- `java-11-openjdk-javadoc`
- `java-11-openjdk-javadoc-zip`
- `java-11-openjdk-jmods`
- `java-11-openjdk-src`
- `java-11-openjdk-static-libs`
- `java-17-openjdk`
- `java-17-openjdk-demo`
- `java-17-openjdk-devel`
- `java-17-openjdk-headless`
- `java-17-openjdk-javadoc`
- `java-17-openjdk-javadoc-zip`
- `java-17-openjdk-jmods`
- `java-17-openjdk-src`
- `java-17-openjdk-static-libs`
- `java-1.8.0-openjdk`
- `java-1.8.0-openjdk-demo`
- `java-1.8.0-openjdk-devel`
- `java-1.8.0-openjdk-headless`
- `java-1.8.0-openjdk-javadoc`
- `java-1.8.0-openjdk-javadoc-zip`
- `java-1.8.0-openjdk-src`
- `java-21-openjdk`
- `java-21-openjdk-demo`
- `java-21-openjdk-devel`
- `java-21-openjdk-headless`
- `java-21-openjdk-javadoc`
- `java-21-openjdk-javadoc-zip`
- `java-21-openjdk-jmods`
- `java-21-openjdk-src`
- `java-21-openjdk-static-libs`
- `kernel-debug-devel`
- `kernel-debug-devel-matched`
- `kernel-devel`
- `kernel-devel-matched`
- `kernel-doc`
- `kernel-headers`
- `kernel-rpm-macros`
- `kernel-srpm-macros`
- `krb5-devel`
- `ksh`
- `libasan`
- `libblkid-devel`
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
- `libblockdev-nvme`
- `libblockdev-part`
- `libblockdev-plugins-all`
- `libblockdev-swap`
- `libblockdev-tools`
- `libblockdev-utils`
- `libdb-devel`
- `libdb-utils`
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
- `libmount-devel`
- `libquadmath-devel`
- `librados2`
- `librbd1`
- `libreoffice`
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
- `libudisks2`
- `libuuid-devel`
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
- `net-snmp`
- `net-snmp-agent-libs`
- `net-snmp-devel`
- `net-snmp-libs`
- `net-snmp-perl`
- `net-snmp-utils`
- `netstandard-targeting-pack-2.1`
- `NetworkManager-cloud-setup`
- `NetworkManager-dispatcher-routing-rules`
- `NetworkManager-ovs`
- `NetworkManager-ppp`
- `nfs-utils-coreos`
- `nfsv4-client-utils`
- `nginx`
- `nginx-all-modules`
- `nginx-core`
- `nginx-filesystem`
- `nginx-mod-devel`
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
- `openssh-askpass`
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
- `pam-devel`
- `pam-docs`
- `pam_ssh_agent_auth`
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
- `pcp-pmda-resctrl`
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
- `pcp-testsuite`
- `pcp-zeroconf`
- `pcre2-devel`
- `pcre2-utf16`
- `pcre2-utf32`
- `perf`
- `perl-PCP-LogImport`
- `perl-PCP-LogSummary`
- `perl-PCP-MMV`
- `perl-PCP-PMDA`
- `perl-Sys-Guestfs`
- `perl-XML-Parser`
- `pesign`
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
- `podman-docker`
- `podman-plugins`
- `podman-remote`
- `podman-tests`
- `polkit-devel`
- `polkit-docs`
- `pykickstart`
- `python3-attrs`
- `python3-audit`
- `python3-bind`
- `python3-blivet`
- `python3-blockdev`
- `python3-boom`
- `python3-dnf-plugin-leaves`
- `python3-dnf-plugin-modulesync`
- `python3-dnf-plugin-show-leaves`
- `python3-idm-pki`
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-iscsi-initiator-utils`
- `python3-kickstart`
- `python3-libguestfs`
- `python3-libmount`
- `python3-libreport`
- `python3-net-snmp`
- `python3-osbuild`
- `python3-packaging`
- `python3-pcp`
- `python3-perf`
- `python3-psutil`
- `python3-psycopg2`
- `python3-PyMySQL`
- `python3-rtslib`
- `python3-sanlock`
- `python3-toml`
- `python3-virt-firmware`
- `rasdaemon`
- `rear`
- `redhat-rpm-config`
- `rhel-system-roles`
- `rpmdevtools`
- `rtla`
- `rv`
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
- `sssd-idp`
- `sysstat`
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
- `uuidd`
- `vim-common`
- `vim-enhanced`
- `vim-X11`
- `virt-p2v`
- `virt-top`
- `virt-v2v`
- `virt-v2v-bash-completion`
- `WALinuxAgent`
- `WALinuxAgent-udev`
- `xsane`
- `xsane-common`

### Removed BaseOS Binary Packages

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

### Removed AppStream Binary Packages

The following binary packages from the AppStream upstream release have been removed:

- `ansible-collection-microsoft-sql`
- `ansible-collection-redhat-rhel_mgmt`
- `cockpit-leapp`
- `command-line-assistant`
- `command-line-assistant-selinux`
- `fence-agents-aliyun`
- `fence-agents-azure-arm`
- `fence-agents-gce`
- `fence-agents-openstack`
- `insights-client`
- `insights-client-ros`
- `leapp`
- `leapp-deps`
- `leapp-upgrade-el9toel10`
- `leapp-upgrade-el9toel10-deps`
- `libreport-rhel-anaconda-bugzilla`
- `NetworkManager-config-connectivity-redhat`
- `opentelemetry-collector`
- `python3-leapp`
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
- `s390utils`
- `s390utils-se-data`
- `toolbox`
- `toolbox-tests`
- `virtio-win`
- `virt-who`

### Removed CodeReady Linux Builder Binary Packages

The following binary packages from the CodeReady Linux Builder upstream release have been removed:

- `redhat-sb-certs`
- `rhc-devel`
- `snactor`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.6/ol-ChangestoSourcePackages.html -->

## Changes to Source Packages

This section contains information about the removed, modified, and new source packages in this release. For information about the binary package changes, see [Changes to Binary Packages](ol-ChangestoBinaryPackages.html#ol9-packages-binary).

### Added Source Packages for BaseOS by Oracle

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

### Added Source Packages for AppStream by Oracle

The following source packages have been added to AppStream by Oracle:

- `dnf-plugin-spacewalk`
- `dtrace`
- `pyOpenSSL`
- `python3-dnf-plugin-ulninfo`
- `python-hwdata`
- `rhn-client-tools`
- `rhnlib`
- `rhnsd`

### Modified BaseOS Source Packages

The following source packages from the BaseOS upstream release have been modified:

- `audit`
- `autofs`
- `binutils`
- `biosdevname`
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
- `initscripts`
- `iputils`
- `irqbalance`
- `iscsi-initiator-utils`
- `kernel`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `krb5`
- `libdb`
- `libdnf`
- `libkcapi`
- `libreport`
- `linux-firmware`
- `mcelog`
- `mdadm`
- `microcode_ctl`
- `NetworkManager`
- `nfs-utils`
- `nvmetcli`
- `openssh`
- `openssl`
- `openssl-fips-provider`
- `os-prober`
- `pam`
- `pcre2`
- `polkit`
- `procps-ng`
- `python-cffi`
- `python-chardet`
- `python-configshell`
- `python-cryptography`
- `python-dmidecode`
- `python-idna`
- `python-ply`
- `python-pycparser`
- `python-pysocks`
- `python-six`
- `PyYAML`
- `redhat-release`
- `selinux-policy`
- `shim`
- `sos`
- `sssd`
- `systemd`
- `trace-cmd`
- `tuned`
- `unzip`
- `util-linux`
- `vim`

### Modified AppStream Source Packages

The following source packages from the AppStream upstream release have been modified:

- `anaconda`
- `anaconda-user-help`
- `audit`
- `bind`
- `bind9.18-dyndb-ldap`
- `binutils`
- `boom-boot`
- `buildah`
- `ceph`
- `chkconfig`
- `clang`
- `cloud-init`
- `cockpit`
- `cockpit-composer`
- `cockpit-machines`
- `cockpit-session-recording`
- `compat-libgfortran-48`
- `compat-openssl11`
- `containers-common`
- `container-tools`
- `crash`
- `cups-filters`
- `dbus`
- `ddiskit`
- `delve`
- `dnf`
- `dnf-plugins-core`
- `dotnet6.0`
- `dotnet7.0`
- `dotnet8.0`
- `dotnet9.0`
- `dracut`
- `edk2`
- `efi-rpm-macros`
- `expect`
- `fapolicyd`
- `firefox`
- `firewalld`
- `fwupd`
- `galera`
- `gcc`
- `gcc-toolset-12-gcc`
- `gcc-toolset-13-binutils`
- `gdb`
- `gdm`
- `glibc`
- `gnome-session`
- `gnome-shell-extension-background-logo`
- `golang`
- `gpsd-minimal`
- `httpd`
- `initial-setup`
- `ipa`
- `iputils`
- `iscsi-initiator-utils`
- `java-11-openjdk`
- `java-17-openjdk`
- `java-1.8.0-openjdk`
- `java-21-openjdk`
- `kernel`
- `kernel-srpm-macros`
- `krb5`
- `ksh`
- `libblockdev`
- `libdb`
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
- `net-snmp`
- `NetworkManager`
- `nfs-utils`
- `nginx`
- `opa-ff`
- `opa-fm`
- `OpenIPMI`
- `openscap`
- `openssh`
- `openssl`
- `open-vm-tools`
- `osbuild`
- `osbuild-composer`
- `osinfo-db`
- `pacemaker`
- `PackageKit`
- `pam`
- `pcp`
- `pcre2`
- `perl-XML-Parser`
- `pesign`
- `pki-core`
- `plymouth`
- `podman`
- `polkit`
- `pykickstart`
- `python-attrs`
- `python-blivet`
- `python-packaging`
- `python-psutil`
- `python-psycopg2`
- `python-PyMySQL`
- `python-rtslib`
- `python-toml`
- `python-virt-firmware`
- `rasdaemon`
- `rear`
- `redhat-rpm-config`
- `rhel-system-roles`
- `rpmdevtools`
- `sanlock`
- `scap-security-guide`
- `selinux-policy`
- `sendmail`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `sssd`
- `sysstat`
- `systemd`
- `systemtap`
- `thunderbird`
- `tog-pegasus`
- `tuned`
- `udisks2`
- `util-linux`
- `vim`
- `virt-p2v`
- `virt-top`
- `virt-v2v`
- `WALinuxAgent`
- `xsane`

### Modified Source Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `anaconda`
- `bind`
- `ceph`
- `crash`
- `cups-filters`
- `dotnet6.0`
- `dotnet7.0`
- `dotnet8.0`
- `dotnet9.0`
- `edk2`
- `expect`
- `fwupd`
- `gcc`
- `gdm`
- `glibc`
- `ipa`
- `java-11-openjdk`
- `java-17-openjdk`
- `java-1.8.0-openjdk`
- `java-21-openjdk`
- `kernel`
- `kmod`
- `libdb`
- `libdnf`
- `libguestfs`
- `libreoffice`
- `libvirt`
- `mpich`
- `munge`
- `NetworkManager`
- `nfs-utils`
- `OpenIPMI`
- `openscap`
- `PackageKit`
- `pcre2`
- `procps-ng`
- `python-packaging`
- `python-psutil`
- `sanlock`
- `sendmail`
- `sssd`
- `tog-pegasus`
- `trace-cmd`
- `udisks2`
- `util-linux`
- `virt-v2v`
- `WALinuxAgent`

### Removed BaseOS Source Packages

The following source packages from the BaseOS upstream release have been removed:

- `kpatch`
- `subscription-manager`
- `subscription-manager-cockpit`
- `subscription-manager-rhsm-certificates`

### Removed AppStream Source Packages

The following source packages from the AppStream upstream release have been removed:

- `ansible-collection-microsoft-sql`
- `ansible-collection-redhat-rhel_mgmt`
- `cockpit-leapp`
- `command-line-assistant`
- `insights-client`
- `leapp`
- `opentelemetry-collector`
- `realtime-tests`
- `redhat-cloud-client-configuration`
- `redhat-indexhtml`
- `redhat-logos`
- `rhc`
- `rhc-worker-playbook`
- `s390utils`
- `toolbox`
- `virtio-win`
- `virt-who`