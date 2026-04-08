---
title: "Release Notes for Oracle Linux 9.4"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol9"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux 9

Release Notes for Oracle Linux 9.4

F95366-06

January 2026

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 9 Release Notes for Oracle Linux 9.4

F95366-06

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2024, 2026, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9.4-Preface.html -->

## Preface

[Oracle Linux 9: Release Notes for Oracle Linux 9.4](https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/) provides information about the new features and known issues in the Oracle
Linux 9.4 release. The information applies to both x86\_64 and 64-bit Arm (aarch64)
architectures. This document might be updated after first publication.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-AboutOracleLinux9.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9.0-SystemRequirementsandLimitations.html -->

## System Requirements and Limitations

To check whether a specific hardware is supported on the current Oracle Linux 9 release, see
the Hardware Certification List at <https://linux.oracle.com/hardware-certifications>. Note that as hardware becomes
available and validated, the hardware is added to the list.

CPU, memory, disk and file system limits for all Oracle Linux releases are described in
[Oracle Linux: Limits](https://docs.oracle.com/en/operating-systems/oracle-linux/limits/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-AvailableArchitectures.html -->

## Available Architectures

The release is available for installation on the following
platforms:

- Intel® 64-bit (x86\_64) (x86-64-v2)
- AMD 64-bit (x86\_64) (x86-64-v2)
- 64-bit Arm (aarch64) (Arm v8.0-A)

  The Arm platform runs only with Unbreakable Enterprise Kernel Release (UEK).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9.4-ShippedKernels.html -->

## Shipped Kernels

For the x86\_64 platform, the current Oracle Linux 9 release ships with the following default
kernel packages:

- `5.14.0-427.13.1` (Red Hat Compatible Kernel (RHCK))
- `5.15.0-205.149.5.1` (Unbreakable Enterprise Kernel Release 7 Update
  2 (UEK R7U2))

  For new installations, the UEK kernel is automatically enabled and installed. It also
  becomes the default kernel on first boot.

For the aarch64 platform, Oracle Linux ships with the UEK kernel only.

The Oracle Linux release is tested as a bundle, as shipped on the installation media image.
When installed from the installation media image, the kernel's version included in the image
is the minimum version that's supported. Downgrading kernel packages isn't supported, unless
recommended by Oracle Support.

For more information about kernel availability on Oracle Linux 9 releases, see <https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/oracle_linux9_kernel_version_matrix.html>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol-AbouttheUnbreakableEnterpriseKernel.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol-Compatibility.html -->

## User Space Compatibility

Oracle Linux maintains user space compatibility with Red Hat Enterprise Linux (RHEL) that's
independent of the kernel version that underlies the OS. Existing applications in user space
continue to run unmodified on UEK with no required recertifications for Oracle Linux certified
applications.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-ObtainingInstallationImages.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-UpgradingFromPreviousOracleLinuxReleases.html -->

## Upgrading From Previous Oracle Linux Releases

You can upgrade an Oracle Linux 8 system to the Oracle Linux 9 release by using
the `leapp` utility.

For step-by-step instructions and information about any known issues that might arise when
upgrading the system, see [Oracle Linux 9: Upgrading Systems With Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/9/leapp/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-UpgradingFromOracleLinuxUpdateReleases.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-NewFeaturesandChanges.html -->

## 2 New Features and Changes

Unless indicated otherwise, the following new features, major enhancements, bug fixes, and
other changes that are introduced in this release of Oracle Linux 9 apply to both the x86\_64
and 64-bit Arm (aarch64) platforms.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-Installation.html -->

## Installation and Boot

The following features, enhancements, and changes related to installation and boot are
introduced in this release of Oracle Linux 9.

### Tailoring Options for the SCAP Security Profile to a Blueprint Customization

You can add tailoring options for a profile to the `/b` blueprint
customizations by using the following options:

- `selected` for the list of rules that you want to add
- `unselected` for the list of rules that you want to
  remove

With the default `org.ssgproject.content` rule namespace, you can omit
the prefix for rules under this namespace. For example: the
`org.ssgproject.content_grub2_password` and
`grub2_password` are functionally equivalent.

When you build an image from that blueprint, it creates a tailoring file with a new
tailoring profile ID and saves it to the image as
`/usr/share/xml/osbuild-oscap-tailoring/tailoring.xml`. The new
profile ID will have `_osbuild_tailoring` appended as a suffix to the
base profile. For example, if you use the `cis` base profile,
`xccdf_org.ssgproject.content_profile_cis_osbuild_tailoring`.

### `boom` Updated to 1.6.0

The `boom` package has been updated to 1.6.0. Notable changes include:

- `boom` can use the `systemd` multi-volume snapshot boot
  syntax.
- New `--mount` and `--no-fstab` options for additional
  volumes to mount at the boot entry.

### DEP and NX Options During Pre-Boot

The Data Execution Prevention (DEP), No Execute (NX), or Execute Disable (XD) memory
protection features are now included in the GRUB and `shim` boot loaders to
help prevent some vulnerabilities during the preboot stage, such as a malicious EFI drivers.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-InfrastructureServices.html -->

## Infrastructure Services

The following features, enhancements, and changes related to infrastructure services are
introduced in this Oracle Linux 9 release.

### `chrony` Updated to Version 4.5

The `chrony` packages are updated to version 4.5. Notable changes
include:

- Added the AES-GCM-SIV cipher to shorten Network Time Security (NTS) cookies to
  avoid some length-specific blocking of Network Time Protocol (NTP).
- Improved automatic NTP source replacement for unreachable NTP sources.
- Logging of important changes made by command requests using the
  `chronyc` command.
- Periodic refreshes of NTP sources. The default refresh period is two weeks. You
  can disable refreshes by adding the `refresh 0` configuration
  entry in the `chrony.conf` file.
- Improved logging of source selection failures and falsetickers.
- Added the `hwtstimeout` directive to configure timeout for late
  hardware transmit timestamps.
- Added the `chronyd-restricted` service as an optional service for
  minimal client-only configurations so that the `chronyd` service
  can be started without `root` privileges.
- Fixed the `presend` option in `interleaved`
  mode.
- Fixed reloading of modified sources from the `sourcedir`
  directories.

### `linuxptp` Updated to Version 4.2

`linuxptp` is an implementation of the Precision Time Protocol (PTP). The
`linuxptp` package is updated to version 4.2 to include the following
notable changes:

- Multiple domain capability in the `phc2sys` tool.
- Clock update and change notifications in the Precision Time Protocol (PTP) parent
  dataset.
- Addition of the PTP Power Profile (IEEE C37.238-2011 and IEEE C37.238-2017).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-Security.html -->

## Security

The following features, enhancements, and changes related to security are introduced in this
Oracle Linux 9 release.

### `libkcapi` Can Target File Names in Hash-Sum Calculations

The `libkcapi` packages includes a new `-T` option that
specifies target file names in hash-sum calculations. This option must be used with the
`-c` option that specifies the HMAC files and overrides the target file names
specified in the HMAC file. For example:

```
$ sha256hmac -c <hmac_file> -T <target_file>
```

### Crypto-Policies Updated to Enable Message Authentication Codes in SSH

The system-wide cryptographic policies (`crypto-policies`) can be configured
with options that control handling of message authentication codes (MACs) for the SSH
protocol. The `crypto-policies` option `ssh_etm` is now a
tri-state `etm@SSH` option. The previous `ssh_etm` option has
been deprecated.

You can set `ssh_etm` to one of the following values:

- `ANY`: to allow both `encrypt-then-mac` and
  `encrypt-and-mac` MACs.
- `DISABLE_ETM`: to prevent `encrypt-then-mac` MACs.
- `DISABLE_NON_ETM`: to prevent MACs that don't use
  `encrypt-then-mac`.

Ciphers that use implicit MACs are always allowed because they use authenticated
encryption.

### `semanage fcontext` Orders Local File Context Modifications Correctly

The `semanage fcontext -l -C` command is updated to display rules in the
`file_contexts.local` file in the correct order, from oldest to newest, to
improve SELinux rule management when using the `restorecon` command, which
processes entries by age.

### SELinux Policy Updated for Services

Several new rules are added to the SELinux policy that confine the following
`systemd` services:

- `nvme-stas`
- `realmd`

Services that are affected by this update no longer run with the
`unconfined_service_t` SELinux label, and can run successfully in SELinux
enforcing mode.

### SELinux Policy Updated for `chronyd-restricted` Service

The SELinux policy includes rules to confine the `chronyd-restricted`
service. The service runs successfully in SELinux enforcing mode.

### SELinux User Space Update to Version 3.6

The SELinux user-space component packages are updated to version 3.6. The following
component packages are updated:

- `libsepol`
- `libselinux`
- `libsemanage`
- `policycoreutils`
- `checkpolicy`
- `mcstrans`

Notable changes include:

- Addition of `deny` rules in SELinux Common Intermediate Language
  (CIL)
- Addition of `notself` and `other` keywords in CIL.
- New `getpolicyload` utility that prints the number of policy reloads.

### GnuTLS Updated to Version 3.8.3

The `gnutls` package is updated to version 3.8.3. Notable changes
include:

- The `gnutls_hkdf_expand` function only accepts arguments with lengths less
  than or equal to 255 times hash digest size, to comply with RFC 5869 2.3.
- Length limit for `TLS PSK` usernames has been increased to 65535
  characters.
- The `gnutls_session_channel_binding` API function performs further checks
  when `GNUTLS_CB_TLS_EXPORTER` is requested according to RFC9622 4.2.
- The `GNUTLS_NO_STATUS_REQUEST` flag and the
  `%NO_STATUS_REQUEST` priority modifier are added so that the
  `status_request` TLS extension can be disabled on the client side.
- GnuTLS ensures that the contents of the Change Cipher Spec message is equal to 1 when the
  TLS version is older than 1.3.
- TLS extensions in ClientHello messages are shuffled to harden fingerprinting.
- GnuTLS can perform EdDSA key generation on PKCS #11 tokens.

### `nettle` Updated to Version 3.9.1

The `nettle` package is updated to version 3.9.1. Notable changes
include:

- Includes Balloon password hashing.
- Includes SM4 block cipher.
- Includes SIV-GCM authenticated encryption mode.
- Includes OCB authenticated encryption mode.
- New exported functions `md5_compress`, `sha1_compress`,
  `sha256_compress`, `sha512_compress`.
- Improved performance of the SHA-256 hash function for x86\_64 platforms.
- Improved performance of the Poly1305 hash function for x86\_64 platforms.

### Oracle Linux 9 OpenSSL FIPS Provider Available

OpenSSL uses the `fips.so` shared library as a FIPS provider. With this
update, the latest version of `fips.so` submitted to the National Institute of
Standards and Technology (NIST) for certification is shipped in a separate
`openssl-fips-provider` package. This package ensures that future versions
of OpenSSL use certified code or code undergoing certification.

### OpenSSL Drop-In Directory for Provider Configuration

The OpenSSL TLS toolkit provides more atomic integration with provider APIs for
installation and configuration of modules that provide cryptographic algorithms.
Provider-specific configuration can be defined in separate `.conf` files
in the `/etc/pki/tls/openssl.d` directory.

### `p11-kit` Updated to Version 0.25.3

The `p11-kit` package is updated to version 0.25.3 and includes the
`p11-kit` tool for managing PKCS#11 modules, the
`trust` tool for operating on the trust policy store, and the
`p11-kit` library. Notable changes include:

- Added integration with PKCS#11 version 3.0
- The `pkcs11.h` header file:

  - Added ChaCha20/Salsa20, and Poly1305 mechanisms and attributes
  - Added AES-GCM mechanism parameters for message-based encryption
- The `p11-kit` tool:

  - Added commands to list and manage objects of a token
    (`list-tokens`, `list-mechanisms`,
    `list-objects`, `import-object`,
    `export-object`, `delete-object`, and
    `generate-keypair`)
  - Added commands to manage PKCS#11 profiles of a token
    (`list-profiles`, `add-profile`, and
    `delete-profile`)
  - Added the `print-config` command for printing merged
    configuration
- The `trust` tool:

  - Added the `check-format` command to check the format of
    `.p11-kit` files

### `libkcapi` Updated to Version 1.4.0

The `libkcapi` library is updated to version 1.4.0. Notable changes
include:

- Added the `sm3sum` and `sm3hmac` tools.
- Added the `kcapi_md_sm3` and `kcapi_md_hmac_sm3`
  APIs.
- Added SM4 convenience functions.
- Added link-time optimization (LTO ) and LTO regression testing
- Fixed support for AEAD encryption of an arbitrary size with
  `kcapi-enc`.

### OpenSSH Uses the sysusers.d Format for Creating Users and Groups

OpenSSH now uses the `sysusers.d` format to declare system users.
Previously, static `useradd` scripts were used for this purpose.

### OpenSSH Adds Authentication Delay Limits

OpenSSH artificially delays responses after login failure to prevent user enumeration
attacks. An upper limit on artificial delays is applied when remote authentication takes
too long, for example in privilege access management (PAM) processing.

### `stunnel` Updated to Version 5.71

The `stunnel` TLS/SSL tunneling service is updated to version 5.71.

Notable changes include:

- Integration with latest PostgreSQL clients.
- New `protocolHeader` service-level option to insert custom
  `connect` protocol negotiation headers for software
  impersonation.
- New `protocolHost` option to control the client SMTP protocol
  negotiation HELO/EHLO value.
- New client-side `protocol = ldap` availability.
- New `sessionResume` service-level option to control whether a
  session can be resumed.
- Extended option to request client certificates in server mode with
  `CApath` or `CAfile`.
- Improved file reading and logging performance.
- Added a configurable delay for the `retry` option.
- OCSP stapling is requested and verified when `verifyChain` is set
  in client mode.
- OCSP stapling is always available in server mode.
- Inconclusive OCSP verification breaks TLS negotiation. You can disable this by
  setting `OCSPrequire = no`.

### `audit` Updated to Version 3.1.2

The `audit` package is updated to version 3.1.2. Notable changes include:

- The `auparse` library now interprets unnamed and anonymous
  sockets.
- Added keyword, `this-hour`, to the `ausearch` and
  `aureport` command `start` and
  `end` options.
- Added user friendly keywords for signals to the `auditctl`
  command.
- The `auparse` command is hardened to better handle corrupt
  logs.
- The `ProtectControlGroups` option is disabled by default in the
  `auditd` service.
- Rule checking for the exclude filter is fixed.
- `OPENAT2` field interpretation is improved.
- The `audispd af_unix` plugin is moved to a standalone program.
- The Python binding is updated to disable setting Audit rules from the Python API
  to resolve an issue in the Simplified Wrapper and Interface Generator
  (SWIG).
- Added `io_uring` asynchronous I/O API capability.

### `rsyslog` Updated to Version 8.2310

Rsyslog is updated to version 8.2310. Notable changes include:

- Customizable TLS/SSL encryption settings

  Rsyslog includes features to configure unique TLS/SSL settings for each
  connection, including specifying different CA certificates, private keys, public
  keys, and CRL files for enhanced security and flexibility. For more information
  and usage, see documentation provided in the `rsyslog-doc`
  package.
- Improved capability dropping

  Rsyslog includes new global options to define
  behavior when dropping capabilities:
  - `libcapng.default`: Defines how Rsyslog behaves when
    errors are returned while dropping capabilities. The default value is
    `on`, which causes Rsyslog to exit if an error
    related to `libcapng` occurs.
  - `libcapng.enable` Controls whether Rsyslog drops
    capabilities during startup. If this option is disabled,
    `libcapng.default` has no impact and capability
    dropping is disabled.

### `opencryptoki` Updated to Version 3.22.0

The `opencryptoki` package is updated to version 3.22.0. Notable changes
include:

- The `AES-XTS` key type can be used with the `CPACF`
  protected keys.
- Certificate object management.
- A `no-login` option to create public sessions.
- Authentication as the Security Officer (SO).
- Capability to import and export the `Edwards` and
  `Montgomery` keys.
- Capability to import `RSA-PSS` keys and certificates.
- Validation that the keys AES-XTS are different when they're created or
  imported.

### SCAP Security Guide Updated to Version 0.1.72

Updates to the SCAP Security Guide include the following notable changes:

- Bash remediations are fixed to handle ISO9660 partitions in the fstab.
- The PCI DSS profile is aligned with the PCI DSS policy version 4.0.
- STIG profiles are aligned with the latest DISA STIG policies.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-Networking.html -->

## Networking

The following features, enhancements, and changes related to networking are introduced in
this Oracle Linux 9 release.

### `nmstate` Includes a `priority` Bond Property

You can set priority of bond ports through the `priority` property in the
`ports-config` section of an `nmstate` framework configuration
file. Example YAML file content might look as follows:

```
---
interfaces:
- name: bond99
  type: bond
  state: up
  link-aggregation:
    mode: active-backup
    ports-config:
    - name: eth2
      priority: 15
```

When an active port within the bonded interface is down, the Oracle Linux kernel re-elects
the next active port with the highest numerical value in the `priority`
property, from the pool of all backup ports.

The `priority` property is relevant for the following modes of the bond
interface:

- `active-backup`
- `balance-tlb`
- `balance-alb`

### `nmstate` Attributes Available for VLAN Interfaces

The `nmstate` framework is updated to introduce new VLAN configuration
attributes:

- `registration-protocol`: VLAN Registration Protocol. Values can be set
  to:
  - `gvrp` (GARP VLAN Registration Protocol)
  - `mvrp` (Multiple VLAN Registration Protocol)
  - `none`

  `reorder-headers`: a Boolean attribute to control whether output packet
  headers are reordered.
- `loose-binding`: a Boolean attribute to control loose binding of the
  interface to the operating state of its primary device.

A configuration entry might look similar to the following:

```
---
interfaces:
  - name: eth1.101
    type: vlan
    state: up
    vlan:
      base-iface: eth1
      id: 101
      registration-protocol: mvrp
      loose-binding: true
      reorder-headers: true
```

### `nmstate` Can Configure MACsec Interfaces

The `nmstate` framework is updated so that you can configure MACsec interfaces
to protect their communication on Layer 2 of the Open Systems Interconnection (OSI) model,
removing any requirement to encrypt individual services later on Layer 7.

### `nmstate` Can Configure IPSec Interfaces

The `nmstate` framework is updated so that you can configure IPSec VPN
interfaces by using the underlying Libreswan utility. You can configure a selection of
Libreswan VPN network layouts, and authentication types with either tunnel (default) or
transport configuration modes. See <https://nmstate.io/features/ipsec.html> for more information.

### `nmstate` YAML file to Revert Network Changes

To change the network configuration, you can create a YAML network configuration file
with new network configuration settings. Before you apply this configuration file, you
can use Use `Nmstate` to create a reversion file that identifies the
differences between the new configuration and the current configuration. You can apply
this reversion file in case the new configuration file causes any problems.

To revert the settings to the previous settings, do the following:

1. Create a YAML file with the new network configuration. For example,
   `new_network_config.yml`.
2. Create a revert configuration file that contains the differences between
   intended settings in `new_network_config.yml` and the current
   state. For example, run the following command:

   ```
   nmstatectl gr new_network_config.yml revert.yml
   ```
3. Apply the configuration from `new_network_config.yml`.
4. If you want now to switch back to the previous state, apply the
   `revert.yml` file.

If you use the Nmstate API to create a revert configuration, you can also use the
`NetworkState::generate_revert(current)` call to perform the
reversion.

### `netfilter` Update

With the update to
RHCK to version 5.14.0-405 in Oracle Linux 9, several updates to the
`netfilter` component of the Oracle Linux kernel are now available. This
update enables the `nftables` subsystem to match various inner header fields of
tunnel packets for more granular and effective control over network traffic.

### `firewalld` Updated Handling of `iptables` Configuration

The
`firewalld` service is updated so that it doesn't remove all existing rules
from the `iptables` configuration if both following conditions are met:

- `firewalld` is using the `nftables` back end.
- No firewall rules were created with the `--direct` option.

Unnecessary operations, such as firewall rule flushes, are avoided to improve performance.
Integration with other software that might use `iptables` configuration is also
improved.

### `nft` Resets `nftables` rule-contained states

`nft reset` resets `nftables` rule-contained states. For
example, you can reset counter and quota statement values.

### NetworkManager Includes an Option To Disable Sending a `client-identifier`

You can now set `ipv4.dhcp-client-id` connection property to
`none` to disable sending the client identifier for DHCP server
configurations that might require that a client doesn't sent a client identifier. Note
that setting this option is normally not recommended. When this option isn't configured,
a globally configured default from NetworkManager.conf is used. If no configuration for
the `client-identifier` is found in NetworkManager.conf, the client
identifier value depends on the DHCP client in use.

### `ss` utility Improved Visibility of TCP Bound-Inactive Sockets

The socket services `ss` utility now supports kernel dumps of TCP
bound-inactive sockets. TCP bound-inactive sockets are attached to an IP address and a
port number but neither connected nor listening on TCP ports.

To dump all sockets including TCP bound-inactive use the following command:

```
ss --all
```

To dump only bound-inactive sockets use the following command:

```
ss --bound-inactive
```

### `iptables` Updated to Version 1.8.10

`iptables` is
updated to version 1.8.10, with several upstream bug fixes and enhancements.

### `nftables` Updated to Version 1.0.9

`nftables` is updated to version 1.0.9, with several upstream bug fixes and enhancements.

### `firewalld` Updated to Version 1.3

The `firewalld` package is updated to version 1.3, with several upstream bug fixes and enhancements.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-Kernel.html -->

## Kernel and System Libraries

The following notable features, enhancements, and changes apply to the Red Hat Compatible
Kernel (RHCK) that's shipped with the current Oracle Linux 9 version.

### Intel® SGX Available in RHCK

Intel® Software Guard Extensions (Intel® SGX) is an Intel® technology for protecting selected
code and data from disclosure or modification.

Intel® SGX versions 1 and 2 are now available for use in Oracle Linux. Version 1 provides the
Flexible Launch Control mechanism that enables SGX technology on platforms. Version 2 provides
the Enclave Dynamic Memory Management (EDMM) functionality.

Notable functionality includes:

- Update of EPCM permissions on regular enclave pages that belong to an initialized
  enclave.
- Dynamically add regular enclave pages to an initialized enclave.
- Expand an initialized enclave to accommodate more threads.
- Remove regular pages and TCS pages from an initialized enclave.

### IDXD Available in RHCK

The Intel® Data Streaming Accelerator Driver (IDXD) is an Intel® CPU integrated
accelerator that shares a work queue with process address space ID
(`pasid`) submission and shared virtual memory (SVM). From this
release, IDXD is a supported feature in RHCK.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-FileSystemsandStorage.html -->

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

### Samba Updated to Version 4.19.4

The `samba` packages are updated to 4.19.4. Notable changes include:

- The `smbget` utility is updated to use a common command line parser to
  handle command line options and provides better authentication handling. This change is
  significant and can break scripts that depend on `smbget` because the
  options interface has changed. Also, you can no longer use the `smbgetrc`
  configuration file. For more information about changes to `smbget`, run
  `smbget --help` or see the `smbget(1)` manual page.
- An update to the handling of `winbind` tracing, so that if `winbind
  debug traceid` is enabled in the `smb.conf` file, the
  `winbind` service logs the following fields:

  - `traceid`: shows records belonging to the same request.
  - `depth`: shows the request nesting level.
- Samba uses the GnuTLS cryptographic library functionality, to replace its own
  cryptography implementation.
- The `directory name cache size` option is removed.

Before updating Samba and before you start the service, ensure that you back up the database
files because downgrading databases isn't supported. When the `smbd`,
`nmbd`, or `winbind` services start, Samba automatically
updates its `tdb` database files.

Use the `testparm` utility to verify the `/etc/samba/smb.conf`
file after updating Samba.

### `multipath.conf` Includes New `max_retries` Option

The multipath.conf configuration file for the multipathd daemon now includes the
`max_retries` option in the `defaults` section . By
default this option is disabled which sets the SCSI layerâs default value of 5 retries.
Valid values are from 0 to 5. When this option is set, it overrides the default value of
the `max_retries`
`sysfs` attribute for SCSI devices. This attribute controls the number of
times the SCSI layer retries I/O commands before returning failure when it encounters
certain error types.

If users encounter an issue where multipathâs path checkers return success but I/O to a
device is hanging, they can set this option to decrease the time before the I/O will be
retried down another path.

### `multipath.conf` Includes New `auto_resize` Option

You use the new `auto_resize` option in the `defaults`
section of the `multipath.conf` file to controls when the
`multipathd` command automatically resizes a multipath device. The
following are the different values for `auto_resize`:

- By default, `auto_resize` is set to `never`. In
  this case, `multipathd` works without any change.
- If `auto_resize` is set to `grow_only`,
  `multipathd` automatically resizes the multipath device when
  the deviceâs paths have grown in size.
- If `auto_resize` is set to `grow_shrink`,
  `multipathd` automatically shrinks the multipath device when
  the deviceâs paths are decreased in size.

As a result, when this option is enabled, you no longer need to manually resize your
multipath devices.

### `lvconvert` now Converts Standard to Thin Logical Volumes

You can use the `lvconvert` command to convert a standard LV to a thin LV.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-HighAvailabilityandClusters.html -->

## High Availability and Clusters

The following features, enhancements, and changes related to high availability are introduced
in this Oracle Linux 9 release.

### `pcs` Adds Time Properties Related to the ISO 8601 Duration Specification

The `pcs` Corosync and Pacemaker configuration tool now includes values
for Pacemaker time properties related to the ISO 8601 duration specification
standard.

### `pscd` Adds Web UI Features

`pscd` is a pcs daemon that operates as a remote server for
`pcs`. `pscd`'s Web UI now includes:

- Moving a cluster resource off the node on which it is currently running
- Banning a resource from running on a node
- Displaying cluster status that shows the age of the cluster status and when the
  cluster state is being reloaded
- Requesting a reload of the cluster status display

### `pcsd` TLS Cipher List Defaults to System-Wide Crypto Policy

Previously, the `pcsd` TLS cipher list was set to
`DEFAULT:!RC4:!3DES:@STRENGTH` by default. With this update, the
cipher list is defined by the system-wide crypto policy by default. The TLS ciphers
accepted by the `pcsd` daemon might change with this upgrade, depending
on the currently set crypto policy. For more information about the crypto policies
framework, see the `crypto-policies`(7) man page.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-DynamicProgramming.html -->

## Dynamic Programming Languages, Web and Database Servers

The following features, enhancements, and changes related to programming languages, web
servers, and database servers are introduced in this Oracle Linux 9 release.

### Python Version 3.12 Availability

The newest release of Python 3.12 is available for use. Notable enhancements in Python 3.12
(compared to the 3.11) include:

- Syntax feature updates include a `type` statement and a type parameter
  syntax for generic classes and functions.
- Grammar feature updates include syntactic formalization of f-strings which can be
  integrated into the parser directly.
- The use of a unique per-interpreter Global Interpreter Lock (GIL). This feature enables
  Python programs to take full advantage of multiple CPU cores. Note that in this release
  this feature is only available through the C-API.
- Python data model updates include a way to the use a buffer protocol from Python code.
  Classes that implement the [`__buffer__()`](https://docs.python.org/3.12/reference/datamodel.html#object.__buffer__) method are now
  usable as buffer types.
- Security improvements include the replacement of the built-in [`hashlib`](https://docs.python.org/3.12/library/hashlib.html#module-hashlib) implementations of SHA1, SHA3,
  SHA2-384, SHA2-512, and MD5 with formally verified code from the [HACL\*](https://github.com/hacl-star/hacl-star/) project. These built-in implementations remain as fallbacks that are only
  used when OpenSSL does not provide them.
- Dictionary, list, and set comprehensions in `CPython` are now inlined.
  This enhancement increases the speed of a comprehension execution.
- `CPython` is available for use with the Linux `perf`
  profiler.
- Stack protection is provided by `CPython` on supported platforms.

Note that the Python 3.12 series packages can be installed in parallel with Python 3.9 and
Python 3.11 on the same system.

For example:

- To install packages from the `python3.12` stack, type:

  ```
  # dnf install python3.12
  # dnf install python3.12-pip
  ```
- To run the interpreter, type:

  ```
  $ python3.12
  $ python3.12 -m pip --help
  ```

For more information, see [Oracle Linux 9: Installing and Managing Python](https://docs.oracle.com/en/operating-systems/oracle-linux/9/python/).

Note:

The Python 3.12 series documentation is available in the
`python3.12-docs` package.

For information about product support for Python language versions, see [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

### Python Improvements for Controlling Email Addresses Parsing

A fix relating to [CVE-2023-27043](https://linux.oracle.com/cve/CVE-2023-27043), introduced the ability to
enable stricter parsing of email addresses in Python 3 in the
`getaddresses` and `parseaddr` functions from the
`email.utils` module. However, this fix is not compatible with the
old parsing behavior and so this improvement includes two methods to disable the new
behavior in favor of the old behavior without having to implement the new code changes
in existing code.

The first methods is a new `PYTHON_EMAIL_DISABLE_STRICT_ADDR_PARSING`
environment variable that when set to `true`, enables the older parsing
behavior as the default. For example:

```
export PYTHON_EMAIL_DISABLE_STRICT_ADDR_PARSING=true
```

You can do the same by creating the `/etc/python/email.cfg` configuration
file with the following section:

```
[email_addr_parsing]
PYTHON_EMAIL_DISABLE_STRICT_ADDR_PARSING = true
```

Note:

If the new functions are implemented in the code, the functions
can still enable the stricter behavior despite these settings.

### Ruby Version 3.3 Availablility

Ruby 3.3.0 is included in a new `ruby:3.3` module stream with the following
notable enhancements:

- New `Prism` parser. Prism is a portable, error tolerant, and maintainable
  recursive descent parser for the Ruby language. `Prism` is an alternative
  parser to the `Ripper` script parser.
- Major new performance improvements are available for Ruby just-in-time YJIT compiler.
- The `Regexp` matching algorithm was updated to reduce the impact of
  potential Regular Expression Denial of Service (ReDoS) vulnerabilities.
- The new pure-Ruby JIT compiler (RJIT) is available for use on x86-64 architecture Unix
  platforms. The RJIT compiler replaces MJIT compiler.
- The new M:N thread scheduler is available for use.

Other notable changes:

- Use the `Lrama` LALR parser generator instead of
  `Bison`.
- Several deprecated methods and constants have been removed.
- The `Racc` gem has been promoted from a default gem to a bundled gem.

To enable and install the `ruby:3.3` module stream, type:

```
sudo dnf module enable ruby:3.3
```

```
sudo dnf module install ruby:3.3
```

If you want to upgrade from an earlier `ruby` module stream, see [Oracle Linux: Managing Software on Oracle
Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).

For information about product support for Ruby modules, see [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

### PHP Version 8.2 Availability

PHP 8.2 is included in the new `php:8.2` module stream with the following
notable changes:

- Ability to mark a class with a readonly modifier.
- Ability to use null, false, and true as stand alone types.
- A new `Random` extension named `random`. This extension
  helps to organizes and integrate existing PHP functionality related to random number
  generation.
- Ability to define constants in traits.

To install the `php:8.2` module stream, use the following command:

```
sudo dnf module install php:8.2
```

If you want to upgrade from the `php:8.1` stream within Oracle Linux, see
[Oracle Linux: Managing Software on Oracle
Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).

For information about the length of support for the `php` module streams, see
the [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/)

### NGINX Version 1.24 Availability

NGINX 1.24 web and proxy server is included in the new `nginx:1.24` module
stream with the following notable changes:

New features and changes related to Transport Layer Security (TLS):

- Encryption keys are automatically rotated for TLS session tickets when using shared
  memory in the `ssl_session_cache` directive.
- Memory usage optimization improvements in configurations with Secure Sockets Layer (SSL)
  proxy.
- You can now use `ipv4=off` parameter to disable look up of IPv4 addresses
  while resolving IP addresses.
- New `$proxy_protocol_tlv_*` variables are available for use. You can use
  these variables to store the values ââof the Type-Length-Value (TLV) fields that appear in
  the PROXY v2 TLV protocol.
- New `byte range` functionality added to the
  `ngx_http_gzip_static_module`.

Other changes:

- Header lines now appear as linked lists in the internal API.
- NGINX can now combine arbitrary header lines with identical named header strings as they
  get passed to the FastCGI, SCGI, and uwsgi back ends in the
  `$r->header_in()` method of the `ngx_http_perl_module`,
  and during lookups of the `$http_...`, `$sent_http_...`,
  `$sent_trailer_...`, `$upstream_http_...`, and
  `$upstream_trailer_...` variables.
- A warning message appears if protocol parameters of a listening socket are redefined.
- NGINX closes connections with lingering if pipeline request was used by the client.
- The logging level for various SSL errors has been lowered from `Critical`
  to `Informational`.

To install the `nginx:1.24` stream, use:

```
sudo dnf module install nginx:1.24
```

To upgrade from the `nginx 1.22` stream within Oracle Linux, see [Oracle Linux: Managing Software on Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).

For information about the length of support for the `php` module streams, see
the [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/)

### PostgreSQL Version 16 Availability

PostgreSQL 16 is available for use as a `postgresql:16` module stream.
PostgreSQL 16 contains many new features and enhancements over version 15.

Notable enhancements include:

- Improved performance for bulk-loading database operations.
- The `libpq` library handles connection-level load balancing. A new
  `load_balance_hosts = disable |
  random` option is available for use to control the order in
  which the client tries to connect to the available hosts and addresses.
- Ability to create custom configuration files and include them in the
  `pg_hba.conf` and `pg_ident.conf` files.
- Enhanced regular expression matching of user and database names in
  `pg_hba.conf`, and usernames in `pg_ident.conf` files.

Other changes include:

- PostgreSQL is no longer distributed with the `postmaster` binary. Users
  who start the `postgresql` server by using the provided
  `systemd` unit file (the `systemctl start postgres`
  command) are not affected by this change. If you start the `postgresql`
  server directly through the `postmaster` binary, you must use the
  `postgres` binary instead.
- PostgreSQL no longer provides documentation in PDF format within the package. Use the
  PostgreSQL online documentation instead. See <https://www.postgresql.org/files/documentation/pdf/16/postgresql-16-US.pdf>

To install the `postgresql:16` stream, use the following command:

```
sudo dnf module install postgresql:16
```

To upgrade from an earlier `postgresql` stream within Oracle Linux, follow the
procedure described in [Oracle Linux: Managing Software on Oracle
Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).

For information about the length of support for the `postgresql` module
streams, see the [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

### Git Updated to Version 2.43.0

Git version 2.43 is included in this release with the following notable enhancements.

- The `git check-attr` command has a new `--source`
  option you can use to read the `.gitattributes` file from the
  provided tree object instead of the current working directory.
- When Git receives an HTTP response that includes one or more
  `WWW-Authenticate` headers, the values for each
  `WW-Authenticate` header are then passed by Git to credential
  helpers.
- In the case of an empty commit, you can use the `git format-patch`
  command to write an output file containing a header of the commit instead of
  creating an empty file.
- You can use `git blame --contents=*<file>* *<revision>* --
  *<path>*` command to examine the origins of lines starting at
  `*<file>*` through the history that leads to
  `*<revision>*`.
- The `git log --format` command was updated to accept the
  `%(decorate)` placeholder for further customization and to
  extend the capabilities provided by the `--decorate` option.

### Git LFS Updated to Version 3.4.1

The Git Large File Storage (LFS) version 3.4.1 is included with the following notable
changes:

- The `git lfs push` command now reads references and object IDs
  from standard input.
- Git LFS now handles alternative remotes without relying on Git.
- Git LFS now handles the `WWW-Authenticate` response-type header as
  a credential helper.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-CompilersandDevTools.html -->

## Compilers and Development Tools

The following features, enhancements, and changes related to compilers and development tools
are introduced in this Oracle Linux 9 release.

### Clang Resource Directory Moved

The Clang resource directory, where Clang stores its internal headers and libraries, has
been moved from `/usr/lib64/clang/17` to
`/usr/lib/clang/17`.

### `elfutils` Updated to Version 0.190

The `elfutils` 0.190 update introduces the following changes:

- `libelf`: This library now includes relative relocation (RELR).
- `libdw`: This library now functions with the
  `.debug_[ct]u_index` sections.
- `-Ds`, `--use-dynamic --symbol`: You can use these options
  with the `eu-readelf` tool to show symbols through the dynamic segment
  without using ELF sections.
- `eu-readelf`: This tool now shows `.gdb_index` version
  9.
- `eu-scrlines`: This new tool generates a list of source files associated
  with a specified DWARF or ELF file.
- `debuginfod`: This server schema now compresses file name representations.
  You must reindex before you can use this feature.

### `systemtap` Updated to Version 5.0

The `systemtap` 5.0 update introduces the following changes:

- Improved kernel-user transport.
- Extended DWARF5 debuginfo format handling.

### `grafana-selinux` Package Added

A `grafana-selinux` package, which contains an SELinux policy for
`grafana-server`, and which is installed by default with
`grafana-server` is added to the release. This update ensures that the
`grafana-server` runs as `grafana_t` SELinux type, rather than
as an `unconfined_service_t` SELinux type.

### `maven-openjdk21` Package Added

The `maven:3.8` module stream now includes the
`maven-openjdk21` subpackage, which provides the Maven JDK binding
for OpenJDK 21 and configures Maven to use the system OpenJDK 21.

### `libzip-tools` Package Added

A `libzip-tools` package, which provides tools such as
`zipcmp`, `zipmerge`, and `ziptool` is
included in the update release.

### `cmake` Updated to Version 3.26

The `cmake` package is updated to version 3.26. Notable changes include:

- Addition of the C17 and C18 language standards.
- `cmake` can query the `/etc/os-release` file to identify
  the OS.
- `cmake` can use CUDA 20 and `nvtx3` libraries.
- `cmake` can use the Python stable application binary interface.
- Perl 5 can be used in the Simplified Wrapper and Interface Generator (SWIG) tool.

### LLVM Toolset Updated to Version 17.0.6

The LLVM Toolset package is updated to version 17.0.6. Notable changes include:

- opaque pointers migration: completed
- legacy pass manager in middle-end optimization deprecated.

Notable Clang changes include:

- C++20 coroutines now fully supported.
- Improved code generation for the std::move function and also in unoptimized
  builds.

See the [LLVM](https://discourse.llvm.org/t/llvm-17-0-6-released/75281) and [Clang](https://releases.llvm.org/17.0.1/tools/clang/docs/ReleaseNotes.html) upstream release notes for more
information.

### Rust Toolset Updated to Version 1.75.0

Rust Toolset is now at version 1.75.0. Notable changes include:

- Unlimited Constant evaluation time
- Panic messages are now printed on their own lines without surrounding quotes,
  making them easier to read.
- Cargo registry authentication is enhanced so that authenticated registries
  require a credential provider.
- Improved expressiveness of the Rust language and trait system by stabilizing the
  `async fn` and
  `return_position_impl_trait_in_trait`

### Go Toolset Updated to Version 1.21.0

GoToolset is now at version 1.21.0. Notable changes include:

- Added min, max, and clear built-ins.
- Added official support for profile guided optimization.
- Precisely defined package initialization order.
- Improved type inferencing.
- Improved backwards compatibility.

See the [Go](https://tip.golang.org/doc/go1.21) upstream release notes for more information.

### GCC Toolset 13 is Updated

GCC Toolset 13 is a compiler toolset that provides recent versions of development tools.
The toolset is available as an Application Stream in the form of a Software Collection in
the `AppStream` repository.

The following tools and versions are available in the GCC Toolset 13:

- GCC 13.2.1
- GDB 12.1
- binutils 2.40
- dwz 0.14
- annobin 12.32

To install the toolset, type:

```
sudo dnf install gcc-toolset-13
```

To run a tool from GCC Toolset 13, type:

```
$ scl enable gcc-toolset-13 tool
```

To run a shell session where tool versions from GCC Toolset 13 override system versions of
these tools, type:

```
scl enable gcc-toolset-13 bash
```

### `pcp` Updated to Version 6.2.0

The `pcp` package is updated to version 6.2.0. Notable changes
include:

- `pcp-htop` provides dynamic screens to include user-configurable
  tabs.
- `pcp-atop` provides a new bar graph visualization mode.
- `pmdaopenmetrics` is updated to reduce transient instance logs and
  improve labeling.
- New tools are included:

  - `pmlogredact`: new command for archive anonymization.
  - `pcp-buddyinfo`: reports Linux buddyinfo statistics.
  - `pcp-meminfo`: reports Linux kernel memory statistics.
  - `pcp-netstat`: reports networking statistics.
  - `pcp-slabinfo`: reports Linux slabinfo kernel
    statistics.
  - `pcp-zoneinfo`: reports Linux zoneinfo kernel
    statistics.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-Containers.html -->

## Containers

The following features, enhancements, and changes related to containers are introduced in
this Oracle Linux 9 release.

### Podman `containers.conf` Modules

Podman can run with `containers.conf` modules files to
load a predetermined set of configurations on-demand. When you specify a module file, you
override the system and user configuration files.

You can created these files in the following directories:

- For rootless users, put the configuration file in the home directory of the user. For
  example,

  ```
  $HOME/.config/containers/containers.conf.modules
  ```
- For root users, put the configuration file in one of the following directories:

  ```
  /etc/containers/containers.conf.modules
              /usr/share/containers/containers.conf.modules
  ```

To load the modules on-demand, use the followign
command:

```
podman --module <your_module_name>
```

In the previous command,

- `--module` specifies a module. You can use this option multiple times if
  required.
- `<your_module_name>` Is path to the module and the module name which
  is the name of the configuration file. The path can be an absolute path or a relative
  path. If the module path is absolute, then the module is loaded directly. If the module
  path is relative, then it resolves to the rootless or root user module directories
  mentioned previously.
- Modules contained in the `$HOME` directory override those in the
  `/etc/` and `/usr/share/` directories.

For more information, see man page for `containers.conf`.

### Container Tools Packages Are Updated

The updated Container Tools RPM meta-package, which contain the Podman, Buildah, Skopeo,
crun, and runc tools, are now available. Notable bug fixes and enhancements over the
previous version include:

Notable changes in Podman v4.9:

- You can now use Podman to load the modules on-demand by using the `podman --module
  <your_module_name>` command and to override the system and user
  configuration files. For more information, see [Podman containers.conf Modules](ol9-features-Containers.html#topic_w1w_2pk_y1c).
- A new `podman farm` command with a set of the
  `create`, `set`, `remove`, and
  `update` subcommands has been added. With these commands, you
  can farm out builds to machines running podman for different architectures.
- A new `podman-compose` command has been added, which runs Compose
  workloads by using an external compose provider such as Docker compose.
- The `podman build` command now supports the
  `--layer-label` and `--cw` options.
- The `podman generate systemd` command is deprecated. Use Quadlet
  to run containers and pods under `systemd`.
- The `podman build` command now supports `Containerfiles`
  with the HereDoc syntax. For more information ,see [Containerfile Multi-Line Instructions](ol9-features-Containers.html#topic_lxb_lsk_y1c).
- The `podman kube play` command now supports a new
  `--publish-all` option. Use this option to expose all
  containerPorts on the host.

For more information about notable changes, see <https://github.com/containers/podman/blob/main/RELEASE_NOTES.md#470%22>.

### SQLite Now Default Podman Database

The SQLite database backend for Podman, which provides better stability, performance, and
consistency when working with container metadata, is now fully supported.

You can explicitly specify the database backend in the `containers.conf` file
by using the `database_backend` option. Available values are:

- "" If an empty value is specified, the default value is `sqlite`. If you
  upgrade from a previous Oracle Linux version, and the empty value is specified, the
  default value is `boltdb` if BoltDB was already on the previous version of
  the system. This enables backward compatibility. If BoltDB was not already on the previous
  version of Oracle Linux, then `sqlite` is used.
- "sqlite" The database backend for Podman uses SQLite.
- "boltdb" The database backend for Podman uses BoltDB

Run the `podman system reset` command before switching to the SQLite database
backend.

### `Containerfile` Multi-Line Instructions

You can use the multi-line HereDoc instructions (Here Document notation) in the
`Containerfile` file to simplify this file and reduce the number of
image layers caused by performing multiple `RUN` directives.

For example, the original `Containerfile` can contain the following
`RUN` directives:

```
RUN dnf update
RUN dnf -y install golang
RUN dnf -y install java
```

Instead of multiple RUN directives, you can use the HereDoc notation:

```
RUN <<EOF
dnf update
dnf -y install golang
dnf -y install java
EOF
```

### `pasta` Networking Mode Is Available

The `pasta` network mode, available beginning with Podman 4.4.1, is a
high-performance replacement of the default network mode `slirp4netns` and can
handle IPv6 forwarding.

To use this network mode when the `podman run` command is used, install
the `passt` package as follows:

```
sudo dnf install passt --network=pasta
```

To set a rootless network mode as default, edit the
`/etc/containers/containers.conf` file with the following entry:

```
[network]
default_rootless_network_cmd
```

### Podman Works With Images Compressed With `zstd`

In Podman, you can pull and push images compressed with the `zstd` format.
`zstd` compression is more efficient and faster than `gzip`.
Therefore, the amount of network traffic and storage for these operations is reduced.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-Cockpit.html -->

## Cockpit Web Console

The following features, enhancements, and changes related to the Cockpit web console are
introduced in this Oracle Linux 9 release.

### Cockpit Storage Section Improvements

The storage section in the Cockpit web console is redesigned to improve visibility across all
host views and to simplify various storage management tasks. The Overview page, for
example, displays all storage objects in a comprehensive table. By using this table, you can
directly perform various storage operations on selected storage entries. For example, you can
view details about a storage object or perform a supplementary storage action.

### Cockpit kdump Script Generation

The Kernel Dump page in the Cockpit web console includes an option to access and copy
Ansible and shell scripts. You can use these generated scripts to apply a
specific Kdump configuration across one or more hosts.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-features-CloudEnvironments.html -->

## Cloud Environment

The following changes and features apply to Oracle Linux used in cloud environments.

### Cloud Init Includes a Clean Configurations Command

The `clean --configs` subcommand and option are added to
`cloud-init` utility to cleanup unnecessary configuration files that
are generated by `cloud-init`. For example, to delete
`cloud-init` network configuration files, run:

```
cloud-init clean --configs network
```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-TechnologyPreview.html -->

## 3 Technology Preview

The following items are available as technical previews in this release of Oracle Linux. Note
that some items listed apply to Red Hat Compatible Kernel (RHCK) and might already be
available in UEK.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-techprev-Security.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-techprev-InfrastructureServices.html -->

## Infrastructure Services

The following features for infrastructure services are available as technology previews.

### Socket API for TuneD

The socket API for TuneD maps one-to-one with the D-Bus API and provides an alternative
communication method for cases where D-Bus isn't available. With the socket API, you can
control the TuneD daemon to optimize the performance, and change the values of various tuning
parameters. The socket API is disabled by default. You can enable it in the
`tuned-main.conf` file.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-techprev-Networking.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-techprev-Kernel.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-techprev-FileSysandStorage.html -->

## File Systems and Storage

The following features that are related to file systems and storage are available as
technology preview.

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

### NVMe-oF Discovery Service

The NVMe-oF Discovery Service features are defined in the NVMexpress.org Technical Proposals
(TP) 8013 and 8014. To preview these features, install the `nvme-cli 2.0`
package and attach the host to an NVMe-oF target device that implements TP-8013 or TP-8014.
For more information about TP-8013 and TP-8014, see the NVM Express 2.0 Ratified TPs from the
[https://nvmexpress.org/developers/nvme-specification/](https://nvmexpress.org/specifications/) website.

Note that NVMe-oF is supported in UEK.

### `nvme-stas` Package

The `nvme-stas` package, which is a Central Discovery Controller (CDC)
client for Linux, handles the following functionalities:

- Asynchronous Event Notifications (AEN)
- Automated NVMe subsystem connection controls
- Error handling and reporting
- Automatic (`zeroconf`) and Manual configuration.

This package consists of two daemons, Storage Appliance Finder (`stafd`)
and Storage Appliance Connector (`stacd`).

### NVMe 8006 in-Band Authentication

Non-Volatile Memory Express (NVMe) TP 8006, which is an in-band authentication for NVMe
over Fabrics (NVMe-oF), is available as for technology preview. The NVMe Technical
Proposal 8006 defines the `DH-HMAC-CHAP` in-band authentication protocol
for NVMe-oF. For more information, see the `dhchap-secret` and
`dhchap-ctrl-secret` option descriptions in the
`nvme-connect(1)` manual page.

in-Band Authentication is fully available in UEK R7U2.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-techprev-CompilersandDevTools.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-techprev-Virtualization.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-techprev-Cloud.html -->

## Cloud Environment

The following features for the cloud environment are available as technology preview.

### VM Deployment in Azure

With the updated RHCK, Oracle Linux confidential virtual machines (VMs) can be deployed on
Microsoft Azure. Through the availability of Unified Kernel Images (UKIs), you can boot
encrypted confidential VM images on that cloud environment. The UKI is available as a
`kernel-uki-virt` package in Oracle Linux 9 repositories.

Note that the Oracle Linux UKI can only be used in a UEFI boot configuration.

This functionality isn't yet available for UEK.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-DeprecatedFeatures.html -->

## 4 Deprecated Features

This chapter lists features and functionalities that are deprecated in Oracle Linux 9. While
these features might be included and operative in the release, support isn't guaranteed in
future major releases. Thus, these features must not be used in new Oracle Linux 9
deployments.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-Installation.html -->

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

### TMPDIR Variable in the ReaR Configuration File

Exporting using the `TMPDIR` environment variable in the
`/etc/rear/local.conf` or `/etc/rear/site.conf` ReaR
configuration files, is deprecated.

Instead, you can specify a custom directory for ReaR temporary files by exporting the
variable in the shell environment before executing ReaR. For example, run the
`export TMPDIR=â¦â` statement and then run the `rear`
command in the same shell session or script.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-ShellandCommandLine.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-Security.html -->

## Security

The following security related features and functionalities are deprecated in Oracle Linux
9.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-Networking.html -->

## Networking

The following network related features and functionalities are deprecated in Oracle Linux
9.

### Network Teams

The `teamd` service, and the `libteam` library, and support
for configuring network teams are deprecated in favor of network bonds. You should use
network bonds instead, which have similar functions as teams, and which would receive
enhancements and updates.

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-Kernel.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-FileSystemsandStorage.html -->

## File Systems and Storage

The following features and functionalities related to file systems and storage are deprecated
in Oracle Linux 9.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-DynamicProgramming.html -->

## Dynamic Programming Languages, Web and Database Servers

The following features and functionalities that are related to dynamic programming, web, and
database servers are deprecated in Oracle Linux 9.

### Berkeley DB (`libdb`)

Deprecation of the Berkely DB (`libdb`) package includes the removal of
cryptographic algorithms and dependencies. Users of `libdb` should
migrate to a different key-value database.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-CompilersandDev.html -->

## Compilers and Development

The following compiler and development related features and functionalities are
deprecated in Oracle Linux 9.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-IdentityManagementandAuthentication.html -->

## Identity Management and Authentication

The following identity management and authentication features and functionalities are
deprecated in Oracle Linux 9.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-Desktop.html -->

## Desktop

The following desktop related features and functionalities are deprecated in Oracle Linux
9.

### X.org Server

In Oracle Linux 9, the `X.org` display server is deprecated, and
consequently, the `xorg-x11-server-Xorg` package.

The default desktop session is the Wayland session. However, the X11 protocol continues
to be supported by using the `XWayland` backend. Therefore, applications
that require X11 can run in Wayland sessions.

### GTK 2

The legacy GTK 2 toolkit and the following, related packages are deprecated:

- `adwaita-gtk2-theme`
- `gnome-common`
- `gtk2`
- `gtk2-immodules`
- `hexchat`

If you maintain an application that uses GTK 2, port the application to GTK 4 as soon as
possible.

### Motif Toolkit

The Motif widget tool is deprecated, including the following packages:

- `motif`
- `openmotif`
- `openmotif21`
- `openmotif22`

Likewise, the `motif-static` package has been removed. In place of Motif,
use the GTK toolkit.

### LibreOffice and Inkscape

The LibreOffice RPM packages are now deprecated. However, LibreOffice itself continues to
be supported.

As a replacement for the RPM packages, you can use the following sources to install
LibreOffice:

- Official Flatpak package in the Flathub repository: <https://flathub.org/apps/org.libreoffice.LibreOffice>.
- Official RPM packages: <https://www.libreoffice.org/download/download-libreoffice/>.

Likewise, the Inkscape Flatpak image (`inkscape-flatpak`) is also deprecated.
As a replacement, use the `inkscape` RPM package from <https://inkscape.org/>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-Virtualization.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-deprecated-Containers.html -->

## Containers

The following features and functionalities that are related to containers are deprecated in
Oracle Linux 9.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9.3-deprecated-packages.html -->

## Deprecated Packages

The support status of deprecated packages remains unchanged within Oracle Linux 9. For more
information about the length of support, see [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

The following packages are deprecated in Oracle Linux 9:

- daxio
- aacraid
- adwaita-gtk2-theme
- af\_key
- anaconda-user-help
- autocorr-af
- autocorr-bg
- autocorr-ca
- autocorr-cs
- autocorr-da
- autocorr-de
- autocorr-dsb
- autocorr-el
- autocorr-en
- autocorr-es
- autocorr-fa
- autocorr-fi
- autocorr-fr
- autocorr-ga
- autocorr-hr
- autocorr-hsb
- autocorr-hu
- autocorr-is
- autocorr-it
- autocorr-ja
- autocorr-ko
- autocorr-lb
- autocorr-lt
- autocorr-mn
- autocorr-nl
- autocorr-pl
- autocorr-pt
- autocorr-ro
- autocorr-ru
- autocorr-sk
- autocorr-sl
- autocorr-sr
- autocorr-sv
- autocorr-tr
- autocorr-vi
- autocorr-vro
- autocorr-zh
- cheese
- cheese-libs
- clutter
- clutter-gst3
- clutter-gtk
- cogl
- daxio
- dbus-glib
- dbus-glib-devel
- dhcp
- dhcp-client
- dhcp-common
- dhcp-relay
- dhcp-server
- enchant
- enchant-devel
- eog
- evolution
- evolution-bogofilter
- evolution-devel
- evolution-help
- evolution-langpacks
- evolution-mapi
- evolution-mapi-langpacks
- evolution-pst
- evolution-spamassassin
- festival
- festival-data
- festvox-slt-arctic-hts
- flite
- flite-devel
- firewire-core
- gedit
- gedit-plugin-bookmarks
- gedit-plugin-bracketcompletion
- gedit-plugin-codecomment
- gedit-plugin-colorpicker
- gedit-plugin-colorschemer
- gedit-plugin-commander
- gedit-plugin-drawspaces
- gedit-plugin-findinfiles
- gedit-plugin-joinlines
- gedit-plugin-multiedit
- gedit-plugin-sessionsaver
- gedit-plugin-smartspaces
- gedit-plugin-synctex
- gedit-plugin-terminal
- gedit-plugin-textsize
- gedit-plugin-translate
- gedit-plugin-wordcompletion
- gedit-plugins
- gedit-plugins-data
- ghostscript-x11
- gnome-common
- gnome-photos
- gnome-photos-tests
- gnome-screenshot
- gnome-themes-extra
- gtk2 gtk2-devel
- gtk2-devel-docs
- gtk2-immodule-xim
- gtk2-immodules
- highcontrast-icon-theme
- inkscape
- inkscape-docs
- inkscape-view
- iptables-devel
- iptables-libs
- iptables-nft
- iptables-nft-services
- iptables-utils
- libdb
- libgdata
- libgdata-devel
- libotr
- libpmem
- libpmem-debug
- libpmem-devel
- libpmem2
- libpmem2-debug
- libpmem2-devel
- libpmemblk
- libpmemblk-debug
- libpmemblk-devel
- libpmemlog
- libpmemlog-debug
- libpmemlog-devel
- libpmemobj
- libpmemobj-debug
- libpmemobj-devel
- libpmempool
- libpmempool-debug
- libpmempool-devel
- libreoffice
- libreoffice-base
- libreoffice-calc
- libreoffice-core
- libreoffice-data
- libreoffice-draw
- libreoffice-emailmerge
- libreoffice-filters
- libreoffice-gdb-debug-support
- libreoffice-graphicfilter
- libreoffice-gtk3
- libreoffice-help-ar
- libreoffice-help-bg
- libreoffice-help-bn
- libreoffice-help-ca
- libreoffice-help-cs
- libreoffice-help-da
- libreoffice-help-de
- libreoffice-help-dz
- libreoffice-help-el
- libreoffice-help-en
- libreoffice-help-eo
- libreoffice-help-es
- libreoffice-help-et
- libreoffice-help-eu
- libreoffice-help-fi
- libreoffice-help-fr
- libreoffice-help-gl
- libreoffice-help-gu
- libreoffice-help-he
- libreoffice-help-hi
- libreoffice-help-hr
- libreoffice-help-hu
- libreoffice-help-id
- libreoffice-help-it
- libreoffice-help-ja
- libreoffice-help-ko
- libreoffice-help-lt
- libreoffice-help-lv
- libreoffice-help-nb
- libreoffice-help-nl
- libreoffice-help-nn
- libreoffice-help-pl
- libreoffice-help-pt-BR
- libreoffice-help-pt-PT
- libreoffice-help-ro
- libreoffice-help-ru
- libreoffice-help-si
- libreoffice-help-sk
- libreoffice-help-sl
- libreoffice-help-sv
- libreoffice-help-ta
- libreoffice-help-tr
- libreoffice-help-uk
- libreoffice-help-zh-Hans
- libreoffice-help-zh-Hant
- libreoffice-impress
- libreoffice-langpack-af
- libreoffice-langpack-ar
- libreoffice-langpack-as
- libreoffice-langpack-bg
- libreoffice-langpack-bn
- libreoffice-langpack-br
- libreoffice-langpack-ca
- libreoffice-langpack-cs
- libreoffice-langpack-cy
- libreoffice-langpack-da
- libreoffice-langpack-de
- libreoffice-langpack-dz
- libreoffice-langpack-el
- libreoffice-langpack-en
- libreoffice-langpack-eo
- libreoffice-langpack-es
- libreoffice-langpack-et
- libreoffice-langpack-eu
- libreoffice-langpack-fa
- libreoffice-langpack-fi
- libreoffice-langpack-fr
- libreoffice-langpack-fy
- libreoffice-langpack-ga
- libreoffice-langpack-gl
- libreoffice-langpack-gu
- libreoffice-langpack-he
- libreoffice-langpack-hi
- libreoffice-langpack-hr
- libreoffice-langpack-hu
- libreoffice-langpack-id
- libreoffice-langpack-it
- libreoffice-langpack-ja
- libreoffice-langpack-kk
- libreoffice-langpack-kn
- libreoffice-langpack-ko
- libreoffice-langpack-lt
- libreoffice-langpack-lv
- libreoffice-langpack-mai
- libreoffice-langpack-ml
- libreoffice-langpack-mr
- libreoffice-langpack-nb
- libreoffice-langpack-nl
- libreoffice-langpack-nn
- libreoffice-langpack-nr
- libreoffice-langpack-nso
- libreoffice-langpack-or
- libreoffice-langpack-pa
- libreoffice-langpack-pl
- libreoffice-langpack-pt-BR
- libreoffice-langpack-pt-PT
- libreoffice-langpack-ro
- libreoffice-langpack-ru
- libreoffice-langpack-si
- libreoffice-langpack-sk
- libreoffice-langpack-sl
- libreoffice-langpack-sr
- libreoffice-langpack-ss
- libreoffice-langpack-st
- libreoffice-langpack-sv
- libreoffice-langpack-ta
- libreoffice-langpack-te
- libreoffice-langpack-th
- libreoffice-langpack-tn
- libreoffice-langpack-tr
- libreoffice-langpack-ts
- libreoffice-langpack-uk
- libreoffice-langpack-ve
- libreoffice-langpack-xh
- libreoffice-langpack-zh-Hans
- libreoffice-langpack-zh-Hant
- libreoffice-langpack-zu
- libreoffice-math
- libreoffice-ogltrans
- libreoffice-opensymbol-fonts
- libreoffice-pdfimport
- libreoffice-pyuno
- libreoffice-sdk
- libreoffice-sdk-doc
- libreoffice-ure
- libreoffice-ure-common
- libreoffice-wiki-publisher
- libreoffice-writer
- libreoffice-x11
- libreoffice-xsltfilter
- libreofficekit
- libsoup
- libsoup-devel
- libuser
- libuser-devel
- libwpe
- libwpe-devel
- mcpp
- mod\_auth\_mellon
- mod\_security
- motif
- motif-devel
- pmdk-convert
- pmempool
- python3-pytz
- qla4xxx
- qt5
- qt5-assistant
- qt5-designer
- qt5-devel
- qt5-doctools
- qt5-linguist
- qt5-qdbusviewer
- qt5-qt3d
- qt5-qt3d-devel
- qt5-qt3d-doc
- qt5-qt3d-examples
- qt5-qtbase
- qt5-qtbase-common
- qt5-qtbase-devel
- qt5-qtbase-doc
- qt5-qtbase-examples
- qt5-qtbase-gui
- qt5-qtbase-mysql
- qt5-qtbase-odbc
- qt5-qtbase-postgresql
- qt5-qtbase-private-devel
- qt5-qtbase-static
- qt5-qtconnectivity
- qt5-qtconnectivity-devel
- qt5-qtconnectivity-doc
- qt5-qtconnectivity-examples
- qt5-qtdeclarative
- qt5-qtdeclarative-devel
- qt5-qtdeclarative-doc
- qt5-qtdeclarative-examples
- qt5-qtdeclarative-static
- qt5-qtdoc
- qt5-qtgraphicaleffects
- qt5-qtgraphicaleffects-doc
- qt5-qtimageformats
- qt5-qtimageformats-doc
- qt5-qtlocation
- qt5-qtlocation-devel
- qt5-qtlocation-doc
- qt5-qtlocation-examples
- qt5-qtmultimedia
- qt5-qtmultimedia-devel
- qt5-qtmultimedia-doc
- qt5-qtmultimedia-examples
- qt5-qtquickcontrols
- qt5-qtquickcontrols-doc
- qt5-qtquickcontrols-examples
- qt5-qtquickcontrols2
- qt5-qtquickcontrols2-devel
- qt5-qtquickcontrols2-doc
- qt5-qtquickcontrols2-examples
- qt5-qtscript
- qt5-qtscript-devel
- qt5-qtscript-doc
- qt5-qtscript-examples
- qt5-qtsensors
- qt5-qtsensors-devel
- qt5-qtsensors-doc
- qt5-qtsensors-examples
- qt5-qtserialbus
- qt5-qtserialbus-devel
- qt5-qtserialbus-doc
- qt5-qtserialbus-examples
- qt5-qtserialport
- qt5-qtserialport-devel
- qt5-qtserialport-doc
- qt5-qtserialport-examples
- qt5-qtsvg
- qt5-qtsvg-devel
- qt5-qtsvg-doc
- qt5-qtsvg-examples
- qt5-qttools
- qt5-qttools-common
- qt5-qttools-devel
- qt5-qttools-doc
- qt5-qttools-examples
- qt5-qttools-libs-designer
- qt5-qttools-libs-designercomponents
- qt5-qttools-libs-help
- qt5-qttools-static
- qt5-qttranslations
- qt5-qtwayland
- qt5-qtwayland-devel
- qt5-qtwayland-doc
- qt5-qtwayland-examples
- qt5-qtwebchannel
- qt5-qtwebchannel-devel
- qt5-qtwebchannel-doc
- qt5-qtwebchannel-examples
- qt5-qtwebsockets
- qt5-qtwebsockets-devel
- qt5-qtwebsockets-doc
- qt5-qtwebsockets-examples
- qt5-qtx11extras
- qt5-qtx11extras-devel
- qt5-qtx11extras-doc
- qt5-qtxmlpatterns
- qt5-qtxmlpatterns-devel
- qt5-qtxmlpatterns-doc
- qt5-qtxmlpatterns-examples
- qt5-rpm-macros
- qt5-srpm-macros
- redis
- sendmail
- spamassassin
- team
- tigervnc
- tigervnc-icons
- tigervnc-license
- tigervnc-selinux
- tigervnc-server
- tigervnc-server-minimal
- tigervnc-server-module
- webkit2gtk3
- webkit2gtk3-devel
- webkit2gtk3-jsc
- webkit2gtk3-jsc-devel
- wpebackend-fdo
- wpebackend-fdo-devel
- xorg-x11-server-Xorg
- xsane
- yp-tools
- ypbind
- ypserv


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-KnownIssues.html -->

## 5 Known Issues

This
chapter describes known issues that you may encounter when installing and using the Oracle
Linux 9 software. Unless indicated otherwise, the issues apply to both x86\_64 and aarch64
systems. Information that pertains only to a specific platform is also noted accordingly.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-InstallationIssues.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-VirtualizationIssues.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol9-KernelIssues.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/issue-35270637_35034465.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/issue-34050377.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/issue-34867566.html -->

## Tuned Profile Packages for Oracle Cloud Infrastructure Are Moved

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/issue-36028061.html -->

## Systems With Btrfs Fail to Boot in FIPS Mode

When booted in FIPS mode, a system using Btrfs fails with the following message:

```
FATAL: FIPS integrity test failed
Refusing to continue
```

(Bug ID 36028061)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/issue-36512929.html -->

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/issue-36563373.html -->

## Kdump Service Disabled After Upgrade

Kdump configuration might be disabled after updating
NetworkManager. This is because of a version update of NetworkManager that changes the default
options during nmcli run time for enabling kdump. Kdump is enabled again after the next
reboot.

(Bug ID 36563373)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol-PackageChangesfromtheUpstreamRelease.html -->

## 6 Package Changes From the Upstream Release

The following sections list the changes to binary and source
packages from the upstream release.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol-ChangestoBinaryPackages.html -->

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
- `kernel-uek-debug-modules-extra`
- `kernel-uek-devel`
- `kernel-uek-doc`
- `kernel-uek-modules`
- `kernel-uek-modules-extra`
- `libertas-sd8686-firmware`
- `libertas-usb8388-firmware`
- `libertas-usb8388-olpc-firmware`
- `linux-firmware-core`
- `NetworkManager-config-connectivity-oracle`
- `ocfs2-tools`
- `oracle-backgrounds`
- `oracle-indexhtml`
- `oraclelinux-release`
- `oraclelinux-release-el9`
- `oracle-logos`
- `oracle-logos-httpd`
- `oracle-logos-ipa`
- `rhnsd`

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
- `rhn-setup`
- `rhn-setup-gnome`

### Added Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages have been added to CodeReady Linux Builder by Oracle:

- `oraclelinux-sb-certs`

### Modified BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been modified:

- `alternatives`
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
- `libblkid`
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
- `libnetapi`
- `libnfsidmap`
- `libnsl`
- `libquadmath`
- `libreport-filesystem`
- `libsmartcols`
- `libsmbclient`
- `libsss_autofs`
- `libsss_certmap`
- `libsss_idmap`
- `libsss_nss_idmap`
- `libsss_simpleifp`
- `libsss_sudo`
- `libstdc++`
- `libuuid`
- `libwbclient`
- `linux-firmware`
- `linux-firmware-core`
- `linux-firmware-whence`
- `liquidio-firmware`
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
- `nfs-utils`
- `nscd`
- `nvmetcli`
- `openssh`
- `openssh-clients`
- `openssh-keycat`
- `openssh-server`
- `openssl`
- `openssl-fips-provider`
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
- `python3-rpm`
- `python3-samba`
- `python3-samba-dc`
- `python3-six`
- `python3-sss`
- `python3-sssdconfig`
- `python3-sss-murmur`
- `redhat-release`
- `rhel-net-naming-sysattrs`
- `rpm`
- `rpm-build-libs`
- `rpm-libs`
- `rpm-plugin-audit`
- `rpm-plugin-selinux`
- `rpm-sign`
- `rpm-sign-libs`
- `samba`
- `samba-client-libs`
- `samba-common`
- `samba-common-libs`
- `samba-common-tools`
- `samba-dcerpc`
- `samba-dc-libs`
- `samba-ldb-ldap-modules`
- `samba-libs`
- `samba-tools`
- `samba-usershares`
- `samba-winbind`
- `samba-winbind-modules`
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
- `bind-libs`
- `crash-devel`
- `cups-filters-devel`
- `dotnet-sdk-6.0-source-built-artifacts`
- `dotnet-sdk-7.0-source-built-artifacts`
- `edk2-aarch64`
- `edk2-tools`
- `edk2-tools-doc`
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
- `kmod-devel`
- `libdnf-devel`
- `libfdisk-devel`
- `libguestfs-devel`
- `libguestfs-gobject`
- `libguestfs-gobject-devel`
- `libguestfs-man-pages-ja`
- `libguestfs-man-pages-uk`
- `libnetapi-devel`
- `libnfsidmap-devel`
- `librados-devel`
- `libradospp-devel`
- `librbd-devel`
- `libreoffice-sdk`
- `libreoffice-sdk-doc`
- `libsmartcols-devel`
- `libsmbclient-devel`
- `libsss_nss_idmap-devel`
- `libstdc++-static`
- `libvirt-client-qemu`
- `libvirt-daemon-plugin-sanlock`
- `libvirt-devel`
- `libvirt-docs`
- `libvirt-lock-sanlock`
- `libwbclient-devel`
- `libwebp-tools`
- `lua-guestfs`
- `mpich`
- `munge-devel`
- `NetworkManager-libnm-devel`
- `nss_db`
- `nss_hesiod`
- `ocaml-libguestfs`
- `ocaml-libguestfs-devel`
- `OpenIPMI-devel`
- `openscap-engine-sce-devel`
- `PackageKit-glib-devel`
- `php-libguestfs`
- `postgresql-docs`
- `postgresql-private-devel`
- `postgresql-server-devel`
- `postgresql-static`
- `postgresql-test`
- `postgresql-upgrade-devel`
- `procps-ng-devel`
- `python3-ipatests`
- `python3-mpich`
- `python3-psutil-tests`
- `python3-samba-devel`
- `python3-samba-test`
- `python-packaging-doc`
- `ruby-libguestfs`
- `samba-devel`
- `samba-pidl`
- `samba-test`
- `samba-test-libs`
- `sanlock-devel`
- `sendmail-milter`
- `sendmail-milter-devel`
- `systemd-boot-unsigned`
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
- `aspnetcore-targeting-pack-6.0`
- `aspnetcore-targeting-pack-7.0`
- `aspnetcore-targeting-pack-8.0`
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
- `clang`
- `clang-analyzer`
- `clang-devel`
- `clang-libs`
- `clang-resource-filesystem`
- `clang-tools-extra`
- `cloud-init`
- `cockpit-composer`
- `cockpit-machines`
- `cockpit-packagekit`
- `cockpit-pcp`
- `cockpit-session-recording`
- `cockpit-storaged`
- `compat-libgfortran-48`
- `compat-openssl11`
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
- `dotnet-apphost-pack-7.0`
- `dotnet-apphost-pack-8.0`
- `dotnet-host`
- `dotnet-hostfxr-6.0`
- `dotnet-hostfxr-7.0`
- `dotnet-hostfxr-8.0`
- `dotnet-runtime-6.0`
- `dotnet-runtime-7.0`
- `dotnet-runtime-8.0`
- `dotnet-sdk-6.0`
- `dotnet-sdk-7.0`
- `dotnet-sdk-8.0`
- `dotnet-sdk-8.0-source-built-artifacts`
- `dotnet-targeting-pack-6.0`
- `dotnet-targeting-pack-7.0`
- `dotnet-targeting-pack-8.0`
- `dotnet-templates-6.0`
- `dotnet-templates-7.0`
- `dotnet-templates-8.0`
- `dracut-caps`
- `dracut-live`
- `edk2-ovmf`
- `efi-srpm-macros`
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
- `gdb`
- `gdb-doc`
- `gdb-gdbserver`
- `gdb-headless`
- `gdb-minimal`
- `gdm`
- `git-clang-format`
- `glibc-devel`
- `glibc-doc`
- `glibc-headers`
- `glibc-locale-source`
- `glibc-utils`
- `gnome-session`
- `gnome-session-wayland-session`
- `gnome-session-xsession`
- `gnome-shell-extension-background-logo`
- `gstreamer1-rtsp-server`
- `httpd`
- `httpd-core`
- `httpd-devel`
- `httpd-filesystem`
- `httpd-manual`
- `httpd-tools`
- `idm-pki-acme`
- `idm-pki-base`
- `idm-pki-ca`
- `idm-pki-est`
- `idm-pki-java`
- `idm-pki-kra`
- `idm-pki-server`
- `idm-pki-tools`
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
- `libwebp`
- `libwebp-devel`
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
- `PackageKit`
- `PackageKit-command-not-found`
- `PackageKit-glib`
- `PackageKit-gstreamer-plugin`
- `PackageKit-gtk3-module`
- `pam-devel`
- `pam-docs`
- `pam_ssh_agent_auth`
- `pcre2-devel`
- `pcre2-utf16`
- `pcre2-utf32`
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
- `podman-gvproxy`
- `podman-plugins`
- `podman-remote`
- `podman-tests`
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
- `postgresql-test-rpm-macros`
- `postgresql-upgrade`
- `postgresql-upgrade-devel`
- `pykickstart`
- `python3-attrs`
- `python3-bind`
- `python3-blivet`
- `python3-blockdev`
- `python3-boom`
- `python3-clang`
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
- `python3-libnmstate`
- `python3-libreport`
- `python3-net-snmp`
- `python3-numpy`
- `python3-numpy-f2py`
- `python3-packaging`
- `python3-pcp`
- `python3-psutil`
- `python3-psycopg2`
- `python3-PyMySQL`
- `python3-rtslib`
- `python3-sanlock`
- `python3-scipy`
- `python3-toml`
- `qemu-guest-agent`
- `qemu-img`
- `qemu-kvm`
- `qemu-kvm-audio-pa`
- `qemu-kvm-block-blkio`
- `qemu-kvm-block-curl`
- `qemu-kvm-block-rbd`
- `qemu-kvm-common`
- `qemu-kvm-core`
- `qemu-kvm-device-display-virtio-gpu`
- `qemu-kvm-device-display-virtio-gpu-pci`
- `qemu-kvm-device-display-virtio-vga`
- `qemu-kvm-device-usb-host`
- `qemu-kvm-device-usb-redirect`
- `qemu-kvm-docs`
- `qemu-kvm-tools`
- `qemu-kvm-ui-egl-headless`
- `qemu-kvm-ui-opengl`
- `qemu-pr-helper`
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
- `samba-client`
- `samba-krb5-printing`
- `samba-vfs-iouring`
- `samba-winbind-clients`
- `samba-winbind-krb5-locator`
- `samba-winexe`
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
- `tuned-profiles-postgresql`
- `tuned-profiles-spectrumscale`
- `tuned-utils`
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
- `insights-client`
- `libreport-rhel-anaconda-bugzilla`
- `NetworkManager-config-connectivity-redhat`
- `realtime-tests`
- `redhat-backgrounds`
- `redhat-cloud-client-configuration`
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

### Removed CodeReady Linux Builder Binary Packages

The following binary packages from the CodeReady Linux Builder upstream release have been removed:

- `redhat-sb-certs`
- `rhc-devel`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.4/ol-ChangestoSourcePackages.html -->

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
- `rhnsd`

### Added Source Packages for AppStream by Oracle

The following source packages have been added to AppStream by Oracle:

- `dnf-plugin-spacewalk`
- `dtrace`
- `pyOpenSSL`
- `python3-dnf-plugin-ulninfo`
- `python-hwdata`
- `rhn-client-tools`
- `rhnlib`

### Modified BaseOS Source Packages

The following source packages from the BaseOS upstream release have been modified:

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
- `iscsi-initiator-utils`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `krb5`
- `libdnf`
- `libkcapi`
- `libreport`
- `linux-firmware`
- `microcode_ctl`
- `NetworkManager`
- `nvmetcli`
- `openssh`
- `openssl`
- `os-prober`
- `pcre2`
- `polkit`
- `python-cffi`
- `python-chardet`
- `python-configshell`
- `python-idna`
- `python-ply`
- `python-pycparser`
- `python-pysocks`
- `python-six`
- `PyYAML`
- `redhat-release`
- `rpm`
- `samba`
- `selinux-policy`
- `shim`
- `sos`
- `sssd`
- `systemd`
- `tuned`
- `unzip`
- `util-linux`
- `vim`

### Modified AppStream Source Packages

The following source packages from the AppStream upstream release have been modified:

- `anaconda`
- `anaconda-user-help`
- `bind`
- `bind-dyndb-ldap`
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
- `dnf-plugins-core`
- `dotnet6.0`
- `dotnet7.0`
- `dracut`
- `edk2`
- `efi-rpm-macros`
- `fapolicyd`
- `firefox`
- `firewalld`
- `fwupd`
- `galera`
- `gcc`
- `gdb`
- `gdm`
- `glibc`
- `gnome-shell-extension-background-logo`
- `httpd`
- `initial-setup`
- `ipa`
- `iscsi-initiator-utils`
- `jackson-databind`
- `java-11-openjdk`
- `java-17-openjdk`
- `java-1.8.0-openjdk`
- `kernel-srpm-macros`
- `keybinder3`
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
- `net-snmp`
- `NetworkManager`
- `numpy`
- `opa-ff`
- `opa-fm`
- `OpenIPMI`
- `openscap`
- `openssh`
- `openssl`
- `open-vm-tools`
- `PackageKit`
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
- `python-PyMySQL`
- `python-rtslib`
- `python-toml`
- `rear`
- `rhel-system-roles`
- `rpm`
- `rpmdevtools`
- `samba`
- `sanlock`
- `scap-security-guide`
- `scipy`
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
- `edk2`
- `fwupd`
- `gcc`
- `gdm`
- `glibc`
- `ipa`
- `java-11-openjdk`
- `java-1.8.0-openjdk`
- `kmod`
- `libdnf`
- `libguestfs`
- `libreoffice`
- `libvirt`
- `mpich`
- `munge`
- `NetworkManager`
- `ocaml`
- `OpenIPMI`
- `openscap`
- `PackageKit`
- `python-packaging`
- `python-psutil`
- `samba`
- `sanlock`
- `sendmail`
- `sssd`
- `tog-pegasus`
- `util-linux`
- `virt-v2v`

### Removed BaseOS Source Packages

The following source packages from the BaseOS upstream release have been removed:

- `kpatch`
- `openssl-fips-provider`
- `subscription-manager`
- `subscription-manager-cockpit`
- `subscription-manager-rhsm-certificates`

### Removed AppStream Source Packages

The following source packages from the AppStream upstream release have been removed:

- `ansible-collection-microsoft-sql`
- `ansible-collection-redhat-rhel_mgmt`
- `insights-client`
- `libica`
- `realtime-tests`
- `redhat-cloud-client-configuration`
- `redhat-indexhtml`
- `redhat-logos`
- `rhc`
- `rhc-worker-playbook`
- `toolbox`
- `virtio-win`
- `virt-who`