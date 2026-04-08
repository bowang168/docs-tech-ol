---
title: "Release Notes for Oracle Linux 9.3"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.3"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol9"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux 9

Release Notes for Oracle Linux 9.3

F87400-05

January 2026

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 9 Release Notes for Oracle Linux 9.3

F87400-05

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2023, 2026, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.3/ol9.3-Preface.html -->

## Preface

[Oracle Linux 9: Release Notes for Oracle Linux 9.3](https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.3/) provides information about the new features and known issues in the Oracle
Linux 9.3 release. The information applies to both x86\_64 and 64-bit Arm (aarch64)
architectures. This document might be updated after first publication.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.3/ol9-AboutOracleLinux9.html -->

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

For the x86\_64 platform, the current Oracle Linux 9 release ships with the following default
kernel packages:

- `5.14.0-362.8.1` (Red Hat Compatible Kernel (RHCK))
- `5.15.0-200.131.27` (Unbreakable Enterprise Kernel Release 7 Update
  2 (UEK R7U2))

  For new installations, the UEK kernel is automatically enabled and installed. It also
  becomes the default kernel on first boot.

For the aarch64 platform, Oracle Linux ships with the UEK kernel only.

The Oracle Linux release is tested as a bundle, as shipped on the installation media image.
When installed from the installation media image, the kernel's version included in the image
is the minimum version that's supported. Downgrading kernel packages isn't supported, unless
recommended by Oracle Support.

For more information about kernel availability on Oracle Linux 9 releases, see <https://docs.oracle.com/en/operating-systems/oracle-linux/9/boot/oracle_linux9_kernel_version_matrix.html>

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.3/ol9-NewFeaturesandChanges.html -->

## 2 New Features and Changes

Unless indicated otherwise, the following new features, major enhancements, bug fixes, and
other changes that are introduced in this release of Oracle Linux 9 apply to both the x86\_64
and 64-bit Arm (aarch64) platforms.

### Installation and Boot

The following features, enhancements, and changes related to installation and boot are
introduced in this release of Oracle Linux 9.

#### New Kickstart Options for DNS

Kickstart includes new options for the `network` command to set DNS
configuration information for a device. The following new options are available:

- `--ipv4-dns-search` and `--ipv6-dns-search`:
  can be used to configure DNS search domains as a comma-separated list.

- `--ipv4-ignore-auto-dns` and
  `--ipv6-ignore-auto-dns`: can be used to disable
  automatic DNS configuration by DHCP.

### Operating System and Software Management

The following features, enhancements, and changes related to the OS and software management
are introduced in this Oracle Linux 9 release.

#### DNF-automatic `reboot` Option

Use DNF-automatic `reboot` option after performing an upgrade to
automatically reboot the system and apply changes.

To set the required DNF-automatic reboot behavior, edit the `[commands]`
section of `/etc/dnf/automatic.conf` to include a
`reboot` entry, for example:

```
reboot = [never , when-changed, when-needed]
```

where:

- never (default behavior) – The system is not rebooted
  following an upgrade.
- when-changed –The system is automatically rebooted following any
  upgrade changes.
- when-needed – The system is only automatically rebooted following
  upgrade changes to `systemd` or the `kernel`.

You can also include a `reboot_command` entry to customize the reboot
behavior. For example, to skip the 5 minute delay following an upgrade, you can specify the
`shutdown - r`

```
reboot_command = shutdown -r
```

#### DNF System-Upgrade Plugin `reboot --poweroff` Flag

Use the DNF system-upgrade plugin `reboot --poweroff` flag to shutdown the
system after installing updates, instead of rebooting.

CLI syntax usage:

```
dnf system-upgrade reboot --poweroff
```

#### DNF Plugins: `leaves` and `show-leaves`

The new DNF `leaves` and `show-leaves` plugins help you
identify packages installed on the system that aren't dependencies of other packages. For
example, use:

- `dnf leaves` – To list the installed packages that aren't required by
  any other installed packages.
- `dnf show-leaves` – To list newly installed leaf packages and packages
  that have become leaves after a transaction.

### Infrastructure Services

The following features, enhancements, and changes related to infrastructure services are
introduced in this Oracle Linux 9 release.

#### Postfix Can Handle SRV Lookups

DNS service records resolution (SRV) entries can be used by Postfix to automatically
configure mail clients and balance server load. Furthermore, Postfix can handle temporary
DNS issues and provides configurable options for fault-resilience in case of SRV record
failures. You can configure SRV handling for Postfix by setting the following options in the
Postfix server configuration:

- `use_srv_lookup=smtp`

  Enables discovery of the specified service
  by using DNS SRV records.
- `allow_srv_lookup_fallback= yes`

  Configures the service for SRV
  lookup fallback, so that Postfix falls back to using MX and IP address records in the
  case where an SRV entry lookup fails either because of misconfiguration or a missing
  entry, but continues to use SRV for the service.
- `ignore_srv_lookup_error=yes`

  Configures the service to stop
  using SRV when a lookup fails, and to switch to using MX or IP address records instead.

#### CUPS: Generic LF-to-CRLF Print Driver

A Generic LF-to-CRLF, `lftocrlf`, print driver is available for configuration
when using the Common UNIX Printing System (CUPS). This driver enables you to convert a line
ending with a Line Feed (LF) control character to a Carriage Return Line Feed (CRLF) control
character.

The `lftocrlf` print driver is a renamed version of the
`text-only` driver available in Oracle Linux 7, so that the name describes
its actual functionality.

### Security

The following features, enhancements, and changes related to security are introduced in this
Oracle Linux 9 release.

#### Keylime Updated to Version 7.3.0

Aside from security fixes, this updated version of Keylime includes the
`convert_runtime_policy.py` script that lets you combine
`allow` and `exclude` lists into the runtime policy.

#### Keylime SELinux Policy Improvements

The Keylime SELinux policy labels ports used by Keylime with the label
`keylime_port_t` and allows TCP connections for ports with the label set.
By labeling ports for Keylime the SELinux policy is more specific and port security can be
more targeted.

#### `crypto-policies` Includes the `NO-ENFORCE-EMS` Subpolicy for TLS 1.2 Connections in FIPS Mode

The `NO-ENFORCE-EMS` subpolicy is included in the system-wide cryptographic
policies. When this subpolicy is enforced, the system no longer requires the Extended Master
Secret (EMS) extension (RFC 7627) for all TLS 1.2 connections negotiated in FIPS mode. The
system can therefore connect with legacy systems that don't work with EMS or TLS 1.3. Note,
however, that applying the subpolicy would result in noncompliance with the requirements of
the FIPS-140-3 standard.

To apply the subpolicy, use the following command:

```
sudo update-crypto-policies --set FIPS:NO-ENFORCE-EMS
```

#### GnuTLS Requires EMS With TLS 1.2 in FIPS Mode

The FIPS-140-3 standard requires the Extended Master Secret (EMS) extension in GnuTLS
servers and clients for all TLS 1.2 connections in FIPS mode.

If you need to preserve compatibility with older servers and clients that don't work with
EMS on TLS 1.2 and, at the same time, you can't use TLS 1.3, apply the
`NO-ENFORCE-EMS` subpolicy instead. Enter the following command:

```
sudo update-crypto-policies --set FIPS:NO-ENFORCE-EMS
```

WARNING:

Setting the subpolicy to accept TLS 1.2 connections without EMS renders the system
incompliant with FIPS-140-3 requirements.

#### NSS Enforce EMS in FIPS Mode

The Network Security Services (NSS) libraries contain the `TLS-REQUIRE-EMS`
policy. This policy enforces the use of the Extended Master Secret (EMS) extension for all
TLS 1.2 connections as required by the FIPS 140-3 standard. NSS enforces the
`TLS-REQUIRE-EMS` policy when system-wide cryptographic policies are set to
`FIPS`.

If you need to work with older servers and clients that don't enforce EMS and, at
the same time, you can't use TLS 1.3, apply the `NO-ENFORCE-EMS` subpolicy
instead. Enter the following command:

```
sudo update-crypto-policies --set FIPS:NO-ENFORCE-EMS
```

However, applying the subpolicy would violate the requirements of the FIPS-140-3
standard.

#### EMS in FIPS Mode Can Be Disabled in OpenSSL

You can configure the OpenSSL cryptographic libraries so you can use TLS 1.2 connections
without the Extended Master Secret (EMS) extension in FIPS mode. Do the following:

1. Edit the `/etc/pki/tls/fips_local.cnf` file by adding the following
   section:

   ```
   [fips_sect]
   tls1-prf-ems-check = 0
   activate = 1
   ```
2. Open the `/etc/pki/tls/openssl.cnf` and navigate to the SSL
   configuration section whose section heading is `[crypto_policy]`.

   At the end of the section, add the following line:

   ```
   Options=RHNoEnforceEMSinFIPS
   ```

You can also stop enforcing EMS for TLS 1.2 in FIPS mode with the following command:

```
sudo update-crypto-policies --set FIPS:NO-ENFORCE-EMS
```

However, whether you use the previous steps or the single command, disabling EMS for TLS
1.2 in FIPS mode would violate the requirements of the FIPS-140-3 standard.

#### OpenSSH Enforces SHA-2

To discourage the use of the less secure SHA-1 algorithm, OpenSSH applies the following
changes:

- Checks `sshd` startup whether SHA-1 is configured. If it's unavailable,
  OpenSSH doesn't use SHA-1 for operations. Thus, DSS keys, if present, aren't loaded.
  Further, the advertising of `rsa-sha2` combinations, when available, is
  enforced.
- On SSH private key conversion, OpenSSH explicitly uses SHA-2 for testing RSA keys.
- The `sshd` daemon uses SHA-2 to confirm host key proof if SHA-1
  signatures are unavailable on the server side. However, this configuration might be
  incompatible with clients that use Oracle Linux 8 and earlier versions.
- The `sshd` daemon also uses SHA-2 if SHA-1 signatures are unavailable on
  the client side.
- On the client side, OpenSSH accepts SHA-2-based key proofs from the server if SHA-1 is
  used in the key proof request or when the hash algorithm isn't specified and the default
  configuration is used. This behavior is aligned with the already present exception for
  RSA certificates, and lets connections be established by using modern algorithms.

#### OpenSSL Elliptic Curve Cryptography Works With Brainpool Curves

The following brainpool curves are enabled in OpenSSL Elliptic Curve Cryptography:

- `brainpoolP256r1`
- `brainpoolP256t1`
- `brainpoolP320r1`
- `brainpoolP320t1`
- `brainpoolP384r1`
- `brainpoolP384t1`
- `brainpoolP512r1`
- `brainpoolP512t1`

#### `pcsc-lite-ccid` Updated to 1.5.2

The updated `pcsc-lite-ccid` package provides various bug fixes and
enhancements such as the ability to work with new readers and a fix for Alcor Micro AU9560
card reader.

#### `opensc` Package Updated to 0.23

The updated `opensc` package provides various bug fixes and enhancements
such as the following:

- Works with encryption and decryption using symmetric keys
- Can be used to sign data with a length of more than 512 bytes
- Automatically disables old card driver functionality
- Removes functionality for the MioCOS and JCOP drivers

#### New SELinux Systemd Service Rules

New rules are added to the SELinux policy that confine the following
`systemd` services:

- `qat`
- `systemd-pstore`
- `boothd`
- `fdo-manufacturing-server`
- `fdo-rendezvous-server`
- `fdo-client-linuxapp`
- `fdo-owner-onboarding-server`

The listed services no longer run with the `unconfined_service_t` SELinux
label, and run in SELinux enforcing mode.

#### OpenSCAP Updated to 1.3.8

The OpenSCAP packages are updated to version 1.3.8. Notable changes include:

- Fixes to `systemd` probes to not ignore some `systemd`
  units.
- Addition of offline capabilities to the `shadow` OVAL probe.
- Addition of offline capabilities to the `sysctl` OVAL probe.
- Addition of `auristorfs` to the list of network file systems.
- Improved handling of tailoring files generated by `autotailor`.

#### SCAP Security Guide Updated to Version 0.1.69

Updates to the SCAP Security Guide include the following notable changes:

- Password aging rules no longer ignore empty string as passwords.
- The remote OVAL content URL is updated to be more specific to Oracle Linux 9 to improve
  memory usage when scanning with `--fetch-remote-resources`.
- Rules related to `/var/log` and `/var/log/audit` are now
  only applicable if those partitions exist.
- Bash remediations are fixed to handle ISO9660 partitions in the fstab.

#### SCAP Security Guide Updated ANSSI-BP-028 Security Profiles to Version 2.0

The Agence Nationale de la SÃ©curitÃ© des SystÃ¨mes d'Information (ANSSI) BP-028 profiles in
the SCAP security guide were updated to align with the version 2.0 guidelines described at
<https://cyber.gouv.fr/publications/recommandations-de-securite-relatives-un-systeme-gnulinux>.

#### Expanded `fanotify` Information in Audit Logs

The Audit service includes information about `fanotify` events in
appropriate audit record fields, as follows:

- `fan_type`: Specifies the type of `fanotify` event.
- `fan_info`: Specifies added context information.
- `sub_trust` and `obj_trust`: Specify trust levels for a
  subject and an object in an event.

The `fanotify` information can clarify causes of access denials in certain
cases, and thereby helps with creating policies for tools such as the
`fapolicyd` framework.

Note:

This feature is available only in the RHCK kernel, not in the UEK7 kernel.

#### `fapolicyd` Includes Rule Numbers in Audit Output

Fapolicyd is updated along with kernel and Auditd components to include the rule number
when outputting to the audit log so that it's easier to troubleshoot policy related
issues.

Note:

This feature is available only in the RHCK kernel, not in the UEK7 kernel.

#### `setools` Updated to 4.4.3

The updated `setools` packages include the following features:

- Fixed compilation with Cython 3.0.0
- Improved manual pages
- Removed unused options in `sediff`, `sesearch`, and
  `apol`
- Added the `-r` option to `seinfoflow` command to
  get flows analysis into the source type
- Automatically rejects as an invalid policy rules that have no permissions set

#### `python3-greenlet-devel` Package Available

The `python3-greenlet-devel` package, used for developing coroutines for
in-process concurrent programming, is now available in the unsupported CodeReady Linux
Builder repository. Previous versions of this package were available in the EPEL
repository.

### Networking

The following features, enhancements, and changes related to networking are introduced in
this Oracle Linux 9 release.

#### `iproute` Packages Updated to Version 6.2.0

The `iproute` packages have been updated to version
6.2.0. This update provides various enhancements and bug fixes over the previous version.
The most notable changes include:

- New `ip stats` command to view and manage interface statistics. See the
  `ip-stats(8)` manual page for more information.
- New `--threads` option used by the `ss` command to
  display thread information. See the `ss(8)` manual page for more
  information.
- New `bridge fdb flush` command to flush forwarding database entries. See
  the `bridge(8)` manual page for more information.

#### NetworkManager Updated With Latest Upstream Version

The `NetworkManager` packages have been upgraded to
upstream version 1.44.0. This update provides various enhancements and bug fixes over the
previous version.

Notable changes include:

- New configurable link properties in `NetworkManager`. For more details,
  see [Network Manager Connection Profiles Include Configurable Link Properties](ol9-NewFeaturesandChanges.html#ol9.3-features-Networking_network_manager_connection_profiles_include_configurable_link_properties)
- New configurable properties for ARP monitoring, LACP active ports, and IPv6 bonding
  targets. For more information see:

  - [Network Manager Includes New arp\_missed\_max Property for Reporting Port as Down](ol9-NewFeaturesandChanges.html#ol9.3-features-Networking_network_manager_includes_new_arp_missed_max_property_for_reporting_port_as_down)
  - [Network Manager Includes New Active Bonding Mode for Sending LACPDU Frames](ol9-NewFeaturesandChanges.html#ol9.3-features-Networking_network_manager_includes_new_active_bonding_mode_for_sending_lacpdu_frames)
  - [Network Manager Includes New ns\_ip6\_target Bonding Option Available](ol9-NewFeaturesandChanges.html#ol9.3-features-Networking_network_manager_includes_new_ns_ip6_target_bonding_option_available)
- IPv6 Access Services: DHCPv6 Prefix Delegation. Ability to set a DHCPv6 prefix
  delegation hint in the `ipv6.dhcp-pd-hint` connection property.
- New `rename` property available to rename a connection profile.
  `NetworkManager` offers a new `rename` property in the
  `keyfile` section of the `/etc/NetworkM
  anager/NetworkManager.conf` file that enables you to change the connection
  profile name. When the `rename` property is enabled,
  `NetworkManager` renames the connection profile and saves it in the
  `/etc/NetworkManager/system-connections/` directory.

  Note:

  Note that if external applications or scripts rely on the file
  names, don't enable the `rename` property in [keyfile] section.
- `NetworkManager` can use TLD as the DNS search domain instead of the full
  hostname when `hostname` is set to a nonpublic Top-Level Domain (TLD)
- `NetworkManager` applies DNS options from the
  `[global-dns]` section in the
  `/etc/NetworkManager/NetworkManager.conf` file.
- To prevent race conditions from occurring with other depending services,
  `NetworkManager` retrieves the D-Bus name only after populating the
  D-Bus tree. Note that with this new D-Bus processing behavior a delay could occur when
  starting `NetworkManager`.
- `NetworkManager` includes a `version-id` argument to
  `Update2()` D-Bus calls to prevent concurrent profile
  modifications.
- `NetworkManager` no longer uses tentative IPv6 addresses to resolve the
  system hostname from DNS.
- To prevent unexpected connection issues with multiconnect profiles,
  `NetworkManager` tracks the remaining number of autoconnect retries for
  each device and connection, instead of tracking the retries only for a connection.
- `NetworkManager` sets VLAN filtering options by using the kernelâs
  `netlink` interface instead of the `sysfs` file
  system.
- A new option is available to `enable` or `disable` wifi
  and Wireless Wide Area Networks (WWANs) using the user interface tool,
  `nmtui`.
- A new property is available (`ignore-carrier=no`) for bond, bridge, and
  team configurations in the `[main]` section of the
  `/etc/NetworkManager/NetworkManager.conf` file.
- The issue that prevented `NetworkManager` from starting after restarting
  the `dbus` service is fixed. In this update,
  `NetworkManager` automatically starts upon a restart the
  `dbus` service.

#### SCTP Updated With Latest Kernel Version of Networking Tree

Notable changes in the Stream Control Transmission Protocol (SCTP) networking subsystem include:

- Virtual routing and forwarding (VRF) enables you to segment and isolate SCTP traffic
  within complex network environments.
- New stream schedulers (`fair capacity`, and `weighted fair
  queueing`) to ensure that efficient and equal resource allocation within the
  network.

#### Network Manager Includes an Option to Suppress AAAA Queries

The `no-aaaa` option can be used to configure DNS settings to suppress AAAA
queries. By using this option, IPv6 DNS resolution can be disabled by using the
`nmcli` utility. After the `NetworkManager` service is
restarted, the `no-aaaa` setting is added to the
`/etc/resolv.conf` file.

#### Network Manager Notifies of Deprecated `ifcfg` Profile Formats

The storage connection profile format `ifcfg` is deprecated in
`NetworkManager`. As of this update, `NetworkManager` warns
users of using the deprecated `ifcfg` profile format in following manner:

- Warning log entry is added to `systemd` journal. For
  example:

  ```
  Warning: the ifcfg-rh plugin is deprecated, migrate connections to the keyfile format using "nmcli connection migrate"
  ```
- Error message is generated in `nmcli` utility reports. For
  example:

  ```
  Error: Failed to update connection '<name>': The ifcfg-rh plugin doesn't support setting '<property>'. If you're updating an existing connection profile saved in ifcfg-rh format, migrate the connection to keyfile using 'nmcli connection migrate <connection_uuid>' or the Update2() D-Bus API and try again.
  ```

#### Network Manager Includes New Active Bonding Mode for Sending LACPDU Frames

A new bonding mode `lacp_active` is available for configuration. The option
provide fine-grained control over Link Aggregation Control Protocol Data Units (LACPDU)
frames in bonding setups. When the LACP is operating in active mode on either end of a link,
both ports can send PDUs. By default, the `lacp_active` option is set
`ON`. To disable the LACP active mode, set the `lacp_active`
option to `OFF`.

#### Network Manager Includes New `ns_ip6_target` Bonding Option Available

A new bonding option `ns_ip6_target` is available for configuration with the
`ns_i6_target` option. With this update, you can set IPv6 targets and send
IPv6 NS requests to monitor the health of the link to the targets. The IPv6 NS monitoring
takes affect when at least one IPv6 address is specified and `arp_interval`
option is set to > 0. The maximum number of configurable `ns_ip_targets`
is 16. The default is 0. Multiple targets must be separated by a comma.

You can use the `NetworkManager`
`nmcli` utility to configure the bonding option parameters for
`arp_interval`, `ns_i6_target`, and
`ns_ip6_target`.

#### Network Manager Can Handle Static and DHCP IP on Same Network Interface

You can use the `nmstate` utility to configure a static IP address by using
the `dhcp: true` or `autoconf: true` properties on a DHCP or
an Ad-Hoc Network Autoconfiguration (autoconf) enabled interface.

With this enhancement, `nmstate` provides the following IP properties for
configuration:

- `valid_lft`= valid lifetime in seconds of the IP address.
- `preferred_lft`= preferred lifetime in seconds of the IP address.

By default, `valid_lft` and `preferred_lft` have a
`forever` value .

When configured, `nmstate` can ignore the DHCP/autoconf based IP addresses
to avoid converting dynamic IP addresses to static IP after applying the queried state back.
Note that in cases where a network environment requires disabling DHCP/autoconf settings or
dynamic IP addresses, `nmstate` converts those dynamic IP addresses to static
IP addresses.

#### Network Manager Connection Profiles Include Configurable Link Properties

The following connection profile link properties in `NetworkManager` are
available for configuration.

Important:

The new link-related properties in
`NetworkManager` are only configurable in connection profiles using the
`keyfile` format and not the deprecated `ifcfg` format.

- `link.tx-queue-length`

  Sets the number of packets allowed per the kernel transit queue of the network device.
- `link.gro-max-size`

  Sets the maximum size in bytes of a Generic Receive Offload (GRO) packet the device can
  accept.
- `link.gso-max-segments`

  Sets maximum number of segments of a Generic Segmentation Offload (GSO) packet the
  device can accept.
- `link.gso-max-size`

  The maximum size in bytes of a GSO packet.

#### Network Manager Includes New `arp_missed_max` Property for Reporting Port as Down

A new `arp_missed_max` property is available to bond connection profiles in
`NetworkManager`. When using the Address Resolution Protocol (ARP) monitor
to check if ports of a bond are up, you can set the `arp_missed_max` option
to define after how many failed checks the bonding driver marks the port as down.

#### Network Manager Includes New `bond-port.prio` Property to Activate Bond Ports in a Specific Order

The kernelâs netlink interface enables you to set priority values on ports for the
following bonding configuration modes: `active-backup`,
`balance-tlb`, or `balance-alb`. The new priority property
(`bond-port.prio`) accepts 32-bit integer values. Increasing the value
increases the priority order for activating the ports.

The `bond-port.prio` property is available for configuration
in`NetworkManager` port connection profile.

#### `nmstate` Can Directly Configure a MAC Address Identified Network Interface

You can use the `nmstate` utility to directly configure network interfaces
identified by a Media Access Control (MAC) address instead of a user identified interface
name.

With this update, the following properties are configurable for a base interface:

- `identifier` = identifies `name` or
  `mac-address` on a network. The default value is
  `name`.
- `profile-name` = string

Usage Notes:

- `nmstate` uses the `identifier` property to identify a
  network interface to a specific network state. For example, if the value for
  `identifier` is set to `mac-address`,
  `nmstate` uses the `interface.mac-address` over the
  `interface.name` to identify the interface.
- `nmstate` stores the network configuration based on the value of the
  `interface.profile-name`. If the `profile-name` isn't
  set, `nmstate` uses the `interface.profile-name` over the
  `interface.name`. When checking the network state, the
  `interface.profile-name` appears hidden if its value is equal to the
  `interface.name.`

#### `nmstate` API Includes `dhcp-send-hostname` And `dhcp-custom-hostname`

`nmstate` includes the following two new configurable DHCP properties:

- `dhcp-send-hostname` = true |
  false (default = true)

  When a DHCP client sends a DHCP request with its `hostname`, the DHCP
  server adds the domain name specified to create an FQDN for the client.
- `dhcp-custom-hostname` = hostname | Fully
  Qualified Domain Name (FQDN)

Usage Notes for DHCPv4:

- If the `hostname` is set to FQDN, see the Fully Qualified Domain Name
  (FQDN), option (81) in RFC 4702.
- If the `hostname` isn't set to FQDN, see the Host Name, option (12) in
  RFC 2132.

#### `nmstate` Includes Option to Filter Untagged Traffic on Bridge VLAN Interfaces

Within the `nmstate` framework, as Oracle Linux 9.3, you can configure
`NetworkManager` to use the `bridge.vlan-default-pvid`
option to filter untagged traffic on bridge VLAN interfaces.

Syntax Usage:

```
bridge.vlan-default-pvid: [n]
```

Assigns default Port VLAN ID (`pvid)` to incoming untagged frames.

where:

- n =1

  Default value
- n = 0

  Untagged traffic is dropped when VLAN filtering is enabled
  (`bridge.vlan-filtering: yes`)

Example: Bridge VLAN Default PVID Assignment - Using YAML

```
interfaces:
  - name: linux-br0
    type: linux-bridge
    state: up
    bridge:
      options:
        vlan-default-pvid: [0-4094]
      port:
        - name: eth1
          stp-hairpin-mode: false
          stp-path-cost: 100
          stp-priority: 32
          vlan:
            mode: access
            tag: 100
```

#### `nmstate` Can Handle Static DNS Search With Dynamic DNS Name Server

`nmstate` can handle static DNS search domains to coexist with dynamic DNS
nameservers. This enhancement offers greater flexibility in network set up and DNS
management.

As of this update, `nmstate` finds a network interface and stores its DNS
configuration per the following order:

1. The preferred interface, which has a valid DNS configuration.
2. An automatic interface.
3. An IP enabled interface.

Note:

`NetworkManager` doesn't remove any DNS
nameservers that might be provided by DHCP.

The following interface configuration example depicts the use of this new
functionality:

```
dns-resolver:
  config:
    search:
      - example.com
      - example.org
interfaces:
  - name: eth1
    type: ethernet
    state: up
    ipv4:
      enabled: true
      dhcp: true
    ipv6:
      enabled: true
      dhcp: true
      autoconf: true
```

### Kernel and System Libraries

The following notable features, enhancements, and changes apply to the Red Hat Compatible
Kernel (RHCK) that's shipped with the current Oracle Linux 9 version.

#### Updated Crash Utility

Version 8.0.3 of the Crash utility addresses both bug fixes and enhancements. Crash is an
interactive utility used to analyze the Linux system state while it's running, or after a
kernel failure and the creation of a core `kdump` file. The most notable
enhancement is the added IPv6 functionality. For example:

- The Crash utility prints IPv6 addresses with the `net` or `net
  -s` command. `net` displays the list of network devices, names,
  and the IP address. `net -s` command displays the following information:
  - Open network socket and sock addresses
  - Sockets types and addresses
  - Source and destination addresses, and ports for `INET` and
    `INET6` families

#### Updated Intel® QAT Kernel Driver

The Intel® Quick Assist Technology (QAT), as of version 6.2, includes both bug fixes and
enhancements. The most notable enhancement includes added functionality for the following
QAT GEN4 hardware accelerator devices:

- Intel Quick Assist Technology 401xx devices
- Intel Quick Assist Technology 402xx devices

The updated driver is only available in RHCK.

#### `perf` Package Updated to Version 6.2

The `perf` performance analysis tool is updated to version 6.2 to include
minor bug fixes and updates. As of this update, the `perf list` command
displays human-friendly names and descriptions for Performance Monitor Unit (PMU) events.

#### RHCK Can Handle AutoIBRS Configurations on AMD Processors

RHCK can handle Automatic Indirect Branch Restricted
Speculation (AutoIBRS) configurations on AMD processors. AutoIBRS is a feature provided by
the AMD EPYC 9004 Genoa family of processors and later CPU versions. AutoIBRS is the
default mitigation used for the Spectre v2 CPU to reduce vulnerabilities, boost performance,
and improve scalability.

#### Kdump Utility Can Handle LVM Thin Provisioned Logical Volumes as Targets

The `kdump` utility includes added functionality for configuring thin
provisioned logical volumes as the `vmcore` target. The configuration of LVM
thin provisioning includes these steps:

1. Create a LVM volume group.

   ```
   vgcreate vg00 /dev/sdb
   ```
2. Create a LVM thin pool of 10 MB available space.

   ```
   lvcreate -L 10M -T vg00/thinpool
   ```
3. Create a LVM thin volume with 300 MB of the file system space.

   ```
   lvcreate -V 300M -T vg00/thinpool -n thinvol
   mkfs.ext4 /dev/vg00/thinvol
   ```
4. Configure the LVM thin pool threshold to automatically extend the space.

   ```
   cat /etc/lvm/lvm.conf
   activation {
   	thin_pool_autoextend_threshold = 70
   	thin_pool_autoextend_percent = 20
   	monitoring = 1
   }
   ```
5. Enable the LVM thin pool monitoring service for the first kernel.

   ```
   systemctl enable lvm2-monitor.service
   systemctl start lvm2-monitor.service
   ```
6. Append the following lines to the `kdump.conf` file to set the LVM thin
   volume as the `kdump` target.

   ```
   ext4 /dev/vg00/thinvol
   path /
   ```
7. Start the `kdump` service.

   ```
   kdumpctl restart
   ```
8. Verify the configuration by triggering a kernel panic and check if the
   `vmcore` is saved to `/dev/vg00/thinvol`.

With this enhancement, the `kdump` utility can save the
`vmcore` dump files on thin provisioned storage volumes.

#### `makedumpfile` Updated to Version 1.7.3

The `makedumpfile` utility is updated to version 1.7.3. This tool is used to
reduce the size of dump files by compression and by excluding pages.

Notable changes include the addition of a 5-level paging mode for standalone dump on x86\_64
architectures, to extend processor linear address width to give applications access to more
memory.

### File Systems and Storage

The following features, enhancements, and changes related to file systems and storage are
introduced in this Oracle Linux 9 release.

#### `nvme-cli` Updated to Version 2.4

The `nvme-cli` package as of version 2.4 provides bug fixes and
enhancements. Notable changes include:

- Functionality for TLS over TCP configurations.
- Functionality for `nvme effects-log` command for fabrics
  controllers.
- Fixes for the incorrect ordering of `systemd` for auto-connect services
  when mounting file systems using the `/etc/fstab` configuration file.:
- Fixes for printing issues seen with `u32` values.
- Fixes for incorrect validation storage tag size.

#### New NFSv4 Courteous Server Functionality

New functionality is added for NSFv4 Courteous Server in RHCK. The NFSv4 Courteous Server
enables clients to continue operation even after experiencing a transient network outage by
enabling clientsâ uncontested locks to remain valid on the server when network outage lasts
longer than the NFSv4 lease period. NSFv4 Courteous Server functionality was developed by
Oracle for upstream Linux (v5.19) and is available in UEK7 Update 1 as part of our ongoing
effort to improve NFS for Linux users. For more information see <https://blogs.oracle.com/linux/post/nfsv4-courteous-server>.

#### DAX Mount Compatible With Reflink-Enabled XFS

The DAX file system mount option `-o dax=always` is compatible with
reflink-enabled XFS file systems. This compatible option is useful for users configuring
persistent memory direct access targets. Note that this feature is available on RHCK but is
under development in UEK.

#### New Per-Device Counter for SCSI Devices

A new SCSI device counter (`iotmo_cnt`) is available for I/O timeouts seen.
For example:

```
/sys/devices/pci0000:16/0000:16:02.0/0000:17:00.0/host2/target2:2:0/2:2:0:0/iorequest_cnt
/sys/devices/pci0000:16/0000:16:02.0/0000:17:00.0/host2/target2:2:0/2:2:0:0/iodone_cnt
/sys/devices/pci0000:16/0000:16:02.0/0000:17:00.0/host2/target2:2:0/2:2:0:0/iotmo_cnt
/sys/devices/pci0000:16/0000:16:02.0/0000:17:00.0/host2/target2:2:0/2:2:0:0/ioerr_cnt
```

where:

- `iorequest_cnt` = count of I/O requests
- `iodone_cnt` = I/O completions
- `ioerr_cnt` = I/O errors

#### New `mpathcleanup` Tool to Manage Device Cleanup

A new `mpathcleanup` tool is available for use to help manage multipath
device cleanup. This tool works on SCSI-based multipath devices and removes the multipath
device along with the SCSI path devices. This enhancement is helpful for users that often
need to remove multipath devices and their underlying storage path devices.

#### Updated `dmpd` Package

The `dmpd` package, as of version 1.0.2, includes the following
changes:

- Memory safety and performance improvements for Rust language tool
- Updates for `thin_check` and `cache_check` tools to
  save execution time for LVM pool activiation and system start up.
- Updates for `thin_dump` and `thin_restore` tools to
  handle metadata `btrees` sharing for snapshots.
- Updates for `thin_metadata_pack` and
  `thin_metadata_unpack` tools to compress thin metadata
  (typically to a tenth of the size). These tools typically make it easier to
  submit damaged metadata for inspection.

### High Availability and Clusters

The following features, enhancements, and changes related to high availability are introduced
in this Oracle Linux 9 release.

#### Pacemaker Packages Updated

The Pacemaker packages as of version 2.1.6 include the following enhancements and bug
fixes:

- Pacemaker remote nodes updated to preserve transient node attributes after a brief,
  recoverable connection outage.
- Sample alert agent (`alert_snmp.sh.sample`) updated to include SNMPv3
  configurations. With this update, you can copy the Pacemaker
  `alert_snmp.sh.sample` agent without making modifications for SNMPv3 .
- New `enabled` meta option configuration that enables you to temporarily
  disable an Pacemaker alert for any reason, such as planned maintenance

  Setting this option to `false` for an alert disables the alert. Setting
  this option to `true` for an alert and `false` for a
  particular recipient disables the alert for that recipient. The default value for this
  option is `true`.
- Pacemaker centralizes cluster decision-making for electing a Designated Controller (DC)
  is no longer complete until all pending actions and results are processed
- Pacemaker fencing agent (`fence_scsi`) enables you to automatically
  detect shared `lvmlockd` devices for when the `devices`
  parameter is undefined.
- Resource stickiness updated to make comparisons against colocation constraint
  scores.
- Updated `crm_resource` command that enables banning clones or moving
  bundle resources with a single active replica.
- An unpromoted clone instance no longer gets moved when a cloned resource starts on a
  node with a higher promotable score. With this fix, no unnecessary restarts occur
  because roles are considered part of the process when assigning node instance
  numbers.

#### New Options for LVM Volume Group Failover

The `LVM-activate` resource agent includes the following configuration
options for enabling a volume group failover when the volume group is missing physical
volumes:

- The `majoritypvs` option enables you to change the volume group system
  ID when the volume group is missing physical volumes.
- The `degraded_activation` option enables RAID logical volumes in a
  volume group to be activated with missing legs.

#### New Policy-Based Routing Functionality for `IPaddr2` And `IPsrcaddr` Resources

As Oracle Linux 9.3, the `IPaddr2` and `IPsrcaddr` cluster
resource agents can handle policy-based routing. Policy-based routing enables you to
configure complex routing scenarios. To use policy-based routing, you need to configure the
resource agentâs `table` parameter.

#### Updated `pcs` Parsing Requires Meta Keyword for Clone Meta Attributes

The `pcs` command format for `pcs resource clone`,
`pcs resource promotable`, and `pcs resource create`
commands must specify a `meta` keyword when configuring clone meta
attributes. For example, the following syntax creates a Pacemaker resource (`pcs
resource create`) by using the meta attribute `mv=v1` and a clone
meta attribute `mv=v2`:

`pcs resource create dummy1 ocf:pacemaker:Dummy meta m1=v1 clone meta m2=v2
--future`

To maintain compatibility with existing scripts which rely on an older command format, you
must specify the `--future` command option to enable the new argument
processing when creating a cloned resource with the `pcs resource create`
command.

#### New Command to Display `pcs` Resource Constraints

You can use the `pcs constraint` command to that can be used to re-create
configured resource constraints on a different system by using the `pcs
constraint` command with the new `--output-format=cmd` option. The
default output format is plain text, as in previous releases, which you can specify with the
`--output-format=text` option. The plain text format has been changed
slightly to make it consistent with the output format of other `pcs`
commands.

#### `pcs property` Command Enhancements

The `pcs property` command includes the following updates:

- The `pcs property config --output-format=` option

  - `--output-format=cmd`

    Use to display the `pcs property set` command created from the
    current cluster properties configuration. You can use this command to re-create
    configured cluster properties on a different system.
  - `--output-format=json`

    Use to display the configured cluster properties in JSON format
  - `output-format=text`

    Use to display the configured cluster properties in plain text format, which is the
    default value for this option.
- The `pcs property defaults` command replaces the deprecated `pcs
  property --defaults` command option
- The `pcs property describe` command identifies the meaning of cluster
  properties.

### Dynamic Programming Languages, Web and Database Servers

The following features, enhancements, and changes related to programming languages, web
servers, and database servers are introduced in this Oracle Linux 9 release.

#### `HTTP::Tiny` Perl Module Updated to Perform TLS Verification By Default

The `HTTP::Tiny` Perl module is updated to perform TLS certificate
verification by default when using HTTPS. The update adds the following dependencies to the
`perl-HTTP-Tiny` package:

- `perl-IO-Socket-SSL`
- `perl-Mozilla-CA`
- `perl-Net-SSLeay`

The `verify_SSL` option is changed from `0` to
`1` when the package is installed.

#### `httpd` Updated to Version 2.4.57

This updated version of thee Apache HTTP Server contains bug fixes, enhancements, and
security fixes, such as the following:

- The HTTP daemon's `rotatelogs` utility has a `-T` option
  which truncates rotated logfiles except the initial logfile.
- In `httpd` configuration dumping operations, the
  `mod_ssl` module no longer tests existence of certificate and key
  files.
- In the `mod_ldap` module, the `LDAPConnectionPoolTTL`
  directive accepts negative values. This feature enables reuse of connections of any
  age.
- Workers from the `mod_proxy_hcheck` module work correctly based on
  worker timeout settings.
- The `mod_proxy_hcheck` module's `hcmethod` parameter
  includes these new methods for HTTP/1.1 requests:

  - `GET11`
  - `HEAD11`
  - `OPTIONS11`

#### New Module in Apache HTTP Server

The `httpd` daemon includes the `mod_authnz_fcgi` module,
enabling FastCGI authorizer applications to authenticate users and authorize access to
resources.

The module must be manually configured to load, as follows:

1. Create a configuration file in the `/etc/httpd/conf.mudles.d`
   directory.
2. Add the following line to the file:

   ```
   LoadModule authnz_fcgi_module modules/mod_authnz_fcgi.so
   ```

#### `nginx:1.22` Updated With New Directive

The `nginx:1.22` module stream includes the new
`ssl_pass_phrase_dialog` directive. Use the directive to configure an
external program that's called when `nginx` is start for each encrypted
private key.

To use the new directive, add one of the following lines to the
`/etc/nginx/nginx.conf` file:

- `ssl_pass_phrase_dialog exec:<path_to_program>;`

  Add this line if you're using an external program. This program is called for each
  encrypted private key file with two arguments:

  - Server name
  - One of the following algorithms: `RSA`, `DSA`,
    `EC`, `DH`, or `UNK` if a
    cryptographic algorithm can't be recognized.
- `ssl_pass_phrase_dialog builtin;`

  Add this line to manually enter a passphrase for each encrypted private key file.
  Entering a passphrase is the default behavior when
  `ssl_pass_phrase_dialog` isn't configured.
- `ssl_pass_phrase_dialog exec:/usr/libexec/nginx-ssl-pass-dialog;`

  Add this line to use this helper script so you can enter a passphrase for each
  encrypted private key at the `nginx` service start when you use the
  `systemctl` command.

Note:

The `ssl_pass_phrase_dialog` directive in `nginx` is
similar to the `SSLPassPhraseDialog` directive in the Apache HTTP
Server.

#### Redis 7 Module Stream Introduced

`Redis 7` is now available as a new module stream called
`redis:7`. Changes from `Redis 6` include the following:

- Server-side scripting in the Redis Functions API
- Fine-grained access control lists (ACLs)
- Shared publish/subscribe (`pub/sub`) functionality for clusters
- New commands and command arguments

Some `Redis 7` features are incompatible with earlier versions, such as the
following:

- `Redis 7` now stores append-only files (AOF) as several files in a
  folder.
- `Redis 7` uses a new version format for Redis Database (RDB) files.

For a complete list of features and incompatible changes, see the [upstream release notes](https://github.com/redis/redis/blob/7.0/00-RELEASENOTES#L688).

To install the `redis:7` module stream, issue the following command:

```
sudo dnf module install redis:7
```

For information about the length of support for the `redis` Application
Streams, see [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

### Compilers and Development Tools

The following features, enhancements, and changes related to compilers and development tools
are introduced in this Oracle Linux 9 release.

#### `glibc` Performance Enhancement for Intel Xeon V5 Hardware

The default amount of cache used by `glibc` for string and memory routines
is tuned to improve performance on Intel Xeon v5 hardware.

#### System GCC Compiler Updated to Version 11.4.1

The GNU Compiler Collection (GCC) provides tools for developing applications with the C,
C++, and Fortran programming languages. Its system GCC compiler is now updated to version
11.4.1.

#### GCC Preserves Register Arguments

GCC is updated to preserve register argument content and generate proper Call Frame
Information (CFI) to make it easier for the unwinder to find this information without
negatively impacting performance.

#### GCC Toolset 13

GCC Toolset 13 is a compiler toolset that provides recent versions of development tools.
The toolset is available as an Application Stream in the form of a Software Collection in
the `AppStream` repository.

The following tools and versions are available in the GCC Toolset 13:

- GCC 13.1.1
- GDB 12.1
- binutils 2.40
- dwz 0.14
- annobin 12.20

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

#### `bintuils` Updated to Version 2.40 in GCC Toolset 13

The GCC Toolset 13 includes version 2.40 of `binutils` which includes the
following notable changes:

- Added a `-w` (`--no-warnings`) option for the linker to
  disable warning messages.
- Improved warning messages in the ELF linker for notifications around permissions
  changes.
- Added a `--private` option in the `objdump` tool that
  shows the fields in the file header and section headers for Portable Executable (PE)
  format files.
- Added a `--show-all-symbols` option for the `objdump` tool
  to show all symbols matching an address when disassembling.
- Added a `--strip-section-headers` option for the `objcopy`
  and `strip` tools to remove the ELF section header from ELF files.
- Added a `-W` (`--no-weak`) option to the
  `nm` tool to set it to ignore weak symbols.
- Added syntax highlighting for disassembler output in the `objdump`
  tool.

#### `libabigail` Updated to Version 2.3

`libabigail` version 2.3 includes the following features:

- Works with the BTF debuginfo format.
- Improvements to Ada range types.
- Availability of new `[allow_type]` directive in suppression
  specifications.
- Addition of new properties for the `[supress_type]` suppression
  specification.
- Update of the ABIXML to version 2.2.
- Change of the SONAME of the library to reflect its own ABI change.

#### New Flag Available in `debugedit` Utility

In the `debugedit` utility, the `find-debuginfo` script can
be configured with the `-q` (`--quiet`) flag to silence non
error output from the script.

#### `systemtap` Updated to Version 4.9

This updated version include the following changes:

- A new Language-Server-Protocol (LSP) backend for easier interactive drafting of
  `systemtap` scripts on LSP-capable editors.
- Access to a Python/Jupyter interactive notebook frontend.
- Improved handling of DWARF 5 bitfields.

#### `elfutils` Updated to Version 0.189

Notable features include the following:

- In `libelf`, the `elf_compress` tool accepts the
  `ELFCOMPRESS_ZSTD` ELF compression type.
- In `libdwfl`, the `dwfl_module_return_value_location`
  function returns 0 (no return type) for DWARF Information Entries (DIEs) that point to a
  `DW_TAG_unspecified_type` type tag.
- In `eu-elfcompress`, the `-t` and
  `--type=` options can handle the Zstandard (`zstd`)
  compression format through the `zstd` argument.

#### `libpfm` Updated to Version 4.13

This version provides access to performance monitoring hardware native events for a wider
range of processor microarchitectures, including ARM Neoverse, AMD Zen 4, and 4th Generation
Intel Xeon processors.

#### LLVM Toolset Updated to Version 16.0.6

In this version, some enhancements include the following:

- Improved optimization
- Addition of new CPU extensions
- Improvements for new C++ versions.

This version also includes changes that are incompatible with earlier versions, such as the
following:

- Clangâs default C++ standard is `gnu++17` instead of
  `gnu++14`.
- The following options default to error for the C code and might affect the behavior of
  configure scripts:

  - `-Wimplicit-function-declaration`
  - `-Wimplicit-int`
  - `-Wincompatible-function-pointer-types`

By default, Clang 16 uses the `libstdc++` library version 13 and
`binutils 2.40` provided by GCC Toolset 13.

#### Rust Toolset Updated to Version 1.71.1

The updated version includes the following features:

- A new implementation of multiple producer, single consumer (`mpsc`)
  channels to improve performance
- A new Cargo `sparse` index protocol for more efficient use of the
  `crates.io` registry
- New `OnceCell` and `OnceLock` types for one-time value
  initialization
- A new `C-unwind` ABI string to enable usage of forced unwinding across
  Foreign Function Interface (FFI) boundaries

Further, the following compiler options for Rust `profiler_builtins` runtime
component are available:

- `-C instrument-coverage` for coverage profiling
- `-C profile-generate` for profile-guided optimization

#### `pcp` Updated to Version 6.0.5

The Performance Co-Pilot, `pcp`, package is updated to version 6.0.5 and
includes many new collector and monitoring tool features.

The updated version has the following collector tool features:

- `pmdaproc`:

  - Per-cgroup IRQ PSI metrics in recent kernels
  - New `proc.smaps.pss_dirty` metric
- `pmdasmart`: More NVME disk information and power state metrics
- `pmdalinux`:

  - System wide IRQ PSI metrics in recent kernels
  - More NUMA external memory fragmentation metric
  - New networking (TCP, ICMP) metrics
- `pmdaoverhead`: New PMDA to measure overhead for groups of processes
- `pmdahacluster`: Updated to handle Pacemaker 2.1.5
  `crm_mon` output changes

The updated version has the following monitoring tool features:

- `pmieconf`:

  - Added webhook actions (Event Driven Ansible)
  - Added a new `pmie` rule that checks file descriptor limits
- `pcp2json`: Extended `pcp2json` with an option to send
  HTTP POSTs
- `pcp-atop`: Added `cgroup`, NUMA memory, and NUMA CPU
- `pcp-htop`: Added a new open file descriptors Meter
- `pcp-ps`: Added capability to show multiple archive samples

#### `pmie` Utility Generates Webhook Events

The Performance Metrics Inference Engine (`pmie`) utility from Performance
Co-Pilot (PCP) is updated to generate webhook events. Configured `pmie` rules
generate events in a format which Event-Driven Ansible (EDA) reads so that EDA can respond
to the rules.

To enable this feature, configure all local `pmie` rules to send to a
webhook at a specific endpoint or URL, for example:

```
sudo pmieconf modify global webhook_endpoint https://localhost:443/endpoint
sudo pmieconf modify global webhook_action yes
```

#### Availability of .NET 8.0

In this release, .NET is updated to version 8.0 which provides support for C#12 and F#8
programming languages and for building container images by directly using the .NET Software
Development Kit. This version also includes performance improvements in the garbage
collector (GC), Just-In-Time (JIT) compiler, and the base libraries.

### Virtualization

The following features, enhancements, and changes related to virtualization are introduced in
this Oracle Linux 9 release.

#### `sevctl` Works With AMD EPYC Rome and Milan

The `sevctl` tool recognizes the latest AMD EPYC cores, including the AMD
EPYC Rome and AMD EPYC Milan series so that you can configure AMD Secure Encrypted
Virtualization (SEV) features for these CPU models.

### Containers

The following features, enhancements, and changes related to containers are introduced in
this Oracle Linux 9 release.

#### Container Tools Packages Are Updated

The Podman, Buildah, Skopeo, crun, and runc packages in the
`container-tools` module are updated for version 4.6.

Notable changes in Podman v4.6 include:

- Updates to the `podman kube play` command, including:
  - a `--configmap=<path>` option to provide one or more Kubernetes
    YAML files with environment variables to be used within the containers of the
    pod;
  - the ability to use `containerPort` names and port numbers in liveness
    probes;
  - automatic addition of `ctrName` as an alias to the pod network
  - handling of SELinux filetype labels and ulimit annotations.
- The `podman secret exists` command is added to verifiy whether a secret
  with the specified name exists.
- The `--shm-size-systemd` option is available in the `podman
  create`, `podman run`, `podman pod create`, and
  `podman pod clone` commands to limit the size of tmpfs for systemd
  mounts.
- The `--security-opt label=nested` option can be specified to use SELinux
  labeling within a confined container when using the `podman create`
  command.
- Podman can automatically update containers running inside a pod.
- You can configure Podman to use a SQLite database as a backend database. The default
  database type is the BoltDB database. You can change the database type by setting the
  `database_backend` field in the `containers.conf` file.
  Changing the backend database requires that you reset Podman back to its initial state
  first. All existing containers and pods are lost and must be re-created after the backend
  database is changed. This feature is available as a technology preview.
- Quadlets can be used to automatically generate a `systemd` service file
  from the container description. See [Quadlet in Podman Available](ol9-NewFeaturesandChanges.html#ol8.9-featuresContainers_quadlet_in_podman_available).

#### Quadlet in Podman Available

Quadlet is available in Podman 4.6. Quadlets can be used to automatically generate a
`systemd` service file from the container description. The container
description is in the `systemd` unit file format and simplifies the technical
complexity of running containers under `systemd`. Quadlet formatted
descriptions might be easier to write and maintain than `systemd` unit
files.

Note that you can't run quadlets in rootless mode, unless you enable `cgroups
v2` by setting the `systemd.unified_cgroup_hierarchy=1` option as a
kernel command line argument at boot time. For example, run any of the following commands,
before rebooting the system:

```
sudo grubby --update-kernel=/boot/vmlinuz-$(uname -r) --args="systemd.unified_cgroup_hierarchy=1"
sudo grubby --update-kernel=DEFAULT --args="systemd.unified_cgroup_hierarchy=1"
sudo grubby --update-kernel=ALL --args="systemd.unified_cgroup_hierarchy=1"
```

For more details, see the [Quadlet upstream documentation](https://github.com/containers/quadlet).

#### Podman Includes `podmansh` Login Shell

The `Podman` login shell is available beginning with Podman v4.6. Configure
the user settings to use `/usr/bin/podmansh` as the login shell. The
command then runs the user's session into a Podman container named
`podmansh`.

Quadlet files define which containers users can log into. The quadlets are typically stored
as configuration files in
`/etc/containers/systemd/users/<uid>/podmansh.container`,
where <uid> is the user ID for each user. In these files, the
`ContainerName` field in the `[Container]` section is set to
`podmansh`. If a proxy is used, the proxy details can also be added into the
`[Service]` section as follows:

```
[Service]
Environment="http_proxy=http://proxy.example.com:80"
Environment="https_proxy=http://proxy.example.com:80"
```

Systemd automatically starts the Podman shell when the user session starts and continues
running until all user sessions exit.

Note that podmansh user session is connected through SSH. Sometimes you might need to try to
connect again if the previous connection fails.

For more information, see <https://blog.podman.io/2023/08/podman-v4-6-introduces-podmansh-a-revolutionary-login-shell/>.

### Support

The following features, enhancements, and changes related to support are introduced in this
Oracle Linux 9 release.

#### `sos` Utility Updated to Version 4.6

The Supportability and Serviceability (`sos`) utility for collecting
configuration, diagnostic, and troubleshooting data is updated to Version 4.6 with
enhancements such as the following:

- Improvements to the reporting and logging methods that aid in troubleshooting.
- Fixes in gathering of `cgroup` data and other information for generation
  of reports.
- Fixes that improve security in the manner that usernames, passwords, and other sensitive
  data are handled when data is collected for reports.

For details on each release of `sos`, see [upstream
release notes](https://github.com/sosreport/sos/releases).

### Cloud Environment

The following changes and features apply to Oracle Linux used in cloud environments.

#### `cloud-init` Utility Works With `NetworkManager` Keyfiles

The `cloud-init` utility can work with `NetworkManager`
keyfiles to configure the network of the created cloud instance.

Note:

By default, the `cloud-init` uses the `sysconfig`
method to configure the network. To set `cloud-init` to use a NM
keyfile instead, edit the `/etc/cloud/cloud.cfg`. On the
`network` line, set `network-manager` as the
primary network renderer, as shown:

```
network:
      renderers: ['network-manager', 'eni', 'netplan', 'sysconfig', 'networkd']
```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.3/ol9-TechnologyPreview.html -->

## 3 Technology Preview

The following items are available as technical previews in this release of Oracle Linux. Note
that some items listed apply to Red Hat Compatible Kernel (RHCK) and might already be
available in UEK.

### Security

The following features for security are available as technology preview.

#### KTLS

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

### Infrastructure Services

The following features for infrastructure services are available as technology previews.

#### Socket API for TuneD

The socket API for TuneD maps one-to-one with the D-Bus API and provides an alternative
communication method for cases where D-Bus isn't available. With the socket API, you can
control the TuneD daemon to optimize the performance, and change the values of various tuning
parameters. The socket API is disabled by default. You can enable it in the
`tuned-main.conf` file.

### Networking

The following networking features are available as technology previews.

#### `gpsd-minimal`

The `gpsd-minimal` package is available as a technical preview.
`gpsd` is a service daemon that mediates access to a GPS sensor
connected to the host computer by serial or USB interface, making its data on the
location, course, and velocity of the sensor available to be queried on TCP port
2947 of the host computer.

#### WireGuard

WireGuard is a VPN solution that has improved security features and is easily
configurable.

Note that WireGuard is fully supported in UEK. See [Oracle Linux: Configuring Virtual Private Networks](https://docs.oracle.com/en/operating-systems/oracle-linux/vpn/)
for more information on using WireGuard on Oracle Linux.

#### `systemd-resolved` Service

The `systemd-resolved` service provides name resolution to local applications.
Its components include a caching and validating DNS stub resolver, a Link-Local Multicast Name
Resolution (LLMNR), and Multicast DNS resolver and responder.

#### PRP and HSR

The `hsr` kernel module is included with RHCK to provide the following
protocols as a technology preview:

- Parallel Redundancy Protocol (PRP)
- High-availability Seamless Redundancy (HSR)

#### IPsec Packet Offloading

In RHCK, complete IPsec encapsulation can be offloaded to a Network Interface Controller
(NIC) to reduce workload. This functionality is offered as a technology preview.

#### Various Modem Network Drivers

Oracle Linux provides modem drivers in RHCK with limited functionality as a technology
preview:

- Qualcomm MHI WWAM MBIM - Telit FN990Axx
- Intel IPC over Shared Memory (IOSM) - Intel XMM 7360 LTE Advanced
- Mediatek t7xx (WWAN) - Fibocom FM350GL
- Intel IPC over Shared Memory (IOSM) - Fibocom L860GL modem

#### Segment Routing Over IPv6

Segment Routing over IPv6 (SRv6) is available as a technology preview in RHCK. SRv6 can
improve traffic flows in edge computing and provides a mechanism to program network
slicing and resource reservation.

### Kernel

The following kernel features are available as technology previews for RHCK.

#### SGX Available

Software Guard Extensions (SGX) from Intel® protects software code and data from disclosure
and modification. The Linux kernel partially supports SGX v1 and SGX v1.5. Version 1 enables
platforms by using the Flexible Launch Control mechanism to use the SGX technology.

Note that SGX is supported in UEK.

#### Intel® Data Streaming Accelerator Driver

The driver is an Intel® CPU integrated accelerator and shares a work queue with process
address space ID (`pasid`) submission and shared virtual memory (SVM).

#### Soft iWarp

Soft-iWARP (`siw`) is an Internet Wide-area RDMA Protocol (iWARP) software
kernel driver. The driver implements the iWARP protocol suite over the TCP/IP network
stack. The suite is implemented in software. Therefore, it doesn't require an RDMA
hardware. The protocol suite enables a system with a standard Ethernet adapter to
connect to an iWARP adapter or to another system that already has `siw`
installed.

Note that from Oracle Linux 9.5, this driver is deprecated.

### File Systems and Storage

The following features that are related to file systems and storage are available as
technology preview.

#### DAX File System Available

In this release,
the DAX file system is available as a Technology Preview for the ext4 and XFS file systems.
DAX enables an application to directly map persistent memory into its address space. The
system must have some form of persistent memory available to use DAX. Persistent memory can be
in the form of one or more Non-Volatile Dual In-line Memory Modules (NVDIMMs). In addition, a
file system that supports DAX must be created on the NVDIMMs; the file system must be mounted
with the `dax` mount option. Then, an `mmap` of a file on the
DAX mounted file system results in a direct mapping of storage into the application's address
space.

#### NVMe-oF Discovery Service

The NVMe-oF Discovery Service features are defined in the NVMexpress.org Technical Proposals
(TP) 8013 and 8014. To preview these features, install the `nvme-cli 2.0`
package and attach the host to an NVMe-oF target device that implements TP-8013 or TP-8014.
For more information about TP-8013 and TP-8014, see the NVM Express 2.0 Ratified TPs from the
[https://nvmexpress.org/developers/nvme-specification/](https://nvmexpress.org/specifications/) website.

Note that NVMe-oF is supported in UEK.

#### `nvme-stas` Package

The `nvme-stas` package, which is a Central Discovery Controller (CDC)
client for Linux, handles the following functionalities:

- Asynchronous Event Notifications (AEN)
- Automated NVMe subsystem connection controls
- Error handling and reporting
- Automatic (`zeroconf`) and Manual configuration.

This package consists of two daemons, Storage Appliance Finder (`stafd`)
and Storage Appliance Connector (`stacd`).

#### NVMe 8006 in-Band Authentication

Non-Volatile Memory Express (NVMe) TP 8006, which is an in-band authentication for NVMe
over Fabrics (NVMe-oF), is available as for technology preview. The NVMe Technical
Proposal 8006 defines the `DH-HMAC-CHAP` in-band authentication protocol
for NVMe-oF. For more information, see the `dhchap-secret` and
`dhchap-ctrl-secret` option descriptions in the
`nvme-connect(1)` manual page.

in-Band Authentication is fully available in UEK R7U2.

#### `io_uring` Asynchronous I/O Interface

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

### Compilers and Development Tools

The following features for compilers and development tools are available as technology
previews.

#### `jmc-core` and `owasp-java-encoder`

`jmc-core` is a library that provides core APIs for Java Development Kit (JDK)
Mission Control, including APIs for:

- Parsing and writing Java Flight Recording files
- Discovering Java Virtual Machines (JVMs) through the Java Discovery Protocol (JDP)

The `owasp-java-encoder` package provides a collection of
high-performance low-overhead contextual encoders for Java.

The packages are available in the Oracle Linux 9 CodeReady Builder repository, which is
unsupported, and which you must explicitly enable.

### Virtualization

The following virtualization features are available as technology previews.

#### Nested VMs

Nested KVM virtualization is provided as a technology preview for KVM virtual machines
(VMs) running on Oracle Linux 9.

#### SEV and SEV-ES

The Secure Encrypted Virtualization (SEV) feature is provided for AMD EPYC host machines that
use the KVM hypervisor. It encrypts a virtual machine's memory and protects the VM from access
by the host.

SEV's enhanced Encrypted State version (SEV-ES) encrypts all CPU register contents when a VM
stops running, thus preventing the host from modifying the VM's CPU registers or reading any
information from them.

Note that SEV is supported in UEK.

#### Virtualization for Arm Platforms

You can create KVM virtual machines on systems running on
the Arm (aarch64) platforms using RHCK as a technical preview.

KVM is supported on aarch64 in UEK.

### Cloud Environment

The following features for the cloud environment are available as technology preview.

#### VM Deployment in Azure

With the updated RHCK, Oracle Linux confidential virtual machines (VMs) can be deployed on
Microsoft Azure. Through the availability of Unified Kernel Images (UKIs), you can boot
encrypted confidential VM images on that cloud environment. The UKI is available as a
`kernel-uki-virt` package in Oracle Linux 9 repositories.

Note that the Oracle Linux UKI can only be used in a UEFI boot configuration.

This functionality isn't yet available for UEK.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.3/ol9-DeprecatedFeatures.html -->

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

#### `initial-setup` Package

Instead of using this package, use the `gnome-initial-setup` package as a
replacement.

### Shell and Command Line

The following shell and command line related features and functionalities are deprecated in Oracle Linux 9.

#### `dump` Utility

The `dump` utility that's included in the `dump` package
is deprecated.

You can alternatively use the `tar` or `dd` to achieve similar
functionality.

Note that the `restore` utility, originally included in the
`dump` package, remains available in Oracle Linux 9 and can be installed by
using the `restore` package.

#### Bacula Sqlite Backend Database

The use of a SQLite backend database for the Bacula backup utility is deprecated. Bacula can
use a MySQL backend database and you can migrate existing deployments to MySQL. Avoid using
SQLite for new deployments of the Bacula backup utility.

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

#### Digest-MD5

The Digest-MD5 authentication mechanism in the Simple Authentication Security Layer (SASL)
framework is deprecated.

#### `/etc/system-fips` File

The `/etc/system-fips` file was used to indicate the FIPS mode in the
system. This file is removed in Oracle Linux 9.

To install Oracle Linux 9 in FIPS mode, add the `fips=1` parameter to the
kernel command line during the system installation. To check whether Oracle Linux 9 is
operating in FIPS mode, use the `fips-mode-setup --check` command.

#### `libcrypt.so.1`

The `libcrypt.so.1` cryptogarhic library is deprecated.

#### `fapolicyd.rules` File

The `/etc/fapolicyd/fapolicyd.rules` file is deprecated. You can store policy
rules for `fapolicyd` in the `/etc/fapolicyd/rules.d/`
directory. The `fagenrules` script merges all component rule files in
this directory to the `/etc/fapolicyd/compiled.rules` file.

Rules in `/etc/fapolicyd/fapolicyd.trust` continue to be processed by
`fapolicyd` for backward compatibility.

#### OpenSSL RSA Encryption Without Padding

RSA encryption without padding for OpenSSL in FIPS mode is no longer accepted. However, key
encapsulation with RSA (RSASVE) which doesn't use padding continues to be supported for
OpenSSL.

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

#### PF\_KEYv2 Kernel API

The `PF_KEYv2` API is used to configure kernel IPsec implementation. However, this API isn't maintained upstream. Therefore, this API is deprecated. Instead, use the `netlink` API as a replacement.

### Kernel

The following kernel related features and functionalities are deprecated in Oracle Linux
9.

#### `crashkernel=auto` Option

The `crashkernel=auto` option is deprecated and no longer supported on Oracle Linux 9 and is also unsupported for UEK R7 and later. Some platforms, such as the Raspberry Pi have maximum limits for `crashkernel` memory reservation and these must be specified explicitly. This option will be removed in a future UEK release.

#### Asynchronous Transfer Mode

Asynchronous Transfer Mode (ATM) encapsulation enables Layer-2 (Point-to-Point Protocol,
Ethernet) or Layer-3 (IP) connectivity for the ATM Adaptation Layer 5 (AAL-5). Currently,
these protocols are used only in chipsets that use ADSL technology, which are being phased
out.

#### `kexec_load` in `kexec_tools`

The `kexec_load` system call for `kexec-tools` is
deprecated.

The `kexec_file_load` system call replaces `kexec_load` and
is the default system call.

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

#### PMDK Library

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

### Dynamic Programming Languages, Web and Database Servers

The following features and functionalities that are related to dynamic programming, web, and
database servers are deprecated in Oracle Linux 9.

#### Berkeley DB (`libdb`)

Deprecation of the Berkely DB (`libdb`) package includes the removal of
cryptographic algorithms and dependencies. Users of `libdb` should
migrate to a different key-value database.

### Compilers and Development

The following compiler and development related features and functionalities are
deprecated in Oracle Linux 9.

#### Keys Smaller Than 2048-bits in OpenSSL

OpenSSL 3.0 has deprecated keys smaller than 2048 bits. Keys smaller than 2048 bits might
not work in FIPS mode.

#### Some PKCS1 v1.5 modes

Some`PKCS1` v1.5 modes aren't approved in FIPS-140-3 for encryption and
are disabled.

### Identity Management and Authentication

The following identity management and authentication features and functionalities are
deprecated in Oracle Linux 9.

#### SSSD Files Provider

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

#### OpenLDAP Utility Options

The OpenLDAP project has deprecated the `-h` and `-p` options
in its utilities, and recommends using the `-H` option instead to specify the
LDAP URI.

#### `nsslapd-idlistscanlimit` Parameter and Default Value

Because of optimizations to filter reordering, the
`nsslapd-idlistscanlimit` parameter results in having a negative
impact on search performance and is therefore deprecated. Further, the parameter's
default value is changed to `2147483646`

#### SMB1 Protocol

Beginning with Samba 4.11, the Server Message Block version 1 (SMB1) protocol is
deprecated because of its insecure features. By default, this protocol is disabled in
both Samba server and client utilities.

### Desktop

The following desktop related features and functionalities are deprecated in Oracle Linux
9.

#### X.org Server

In Oracle Linux 9, the `X.org` display server is deprecated, and
consequently, the `xorg-x11-server-Xorg` package.

The default desktop session is the Wayland session. However, the X11 protocol continues
to be supported by using the `XWayland` backend. Therefore, applications
that require X11 can run in Wayland sessions.

#### GTK 2

The legacy GTK 2 toolkit and the following, related packages are deprecated:

- `adwaita-gtk2-theme`
- `gnome-common`
- `gtk2`
- `gtk2-immodules`
- `hexchat`

If you maintain an application that uses GTK 2, port the application to GTK 4 as soon as
possible.

#### Motif Toolkit

The Motif widget tool is deprecated, including the following packages:

- `motif`
- `openmotif`
- `openmotif21`
- `openmotif22`

Likewise, the `motif-static` package has been removed. In place of Motif,
use the GTK toolkit.

#### LibreOffice and Inkscape

The LibreOffice RPM packages are now deprecated. However, LibreOffice itself continues to
be supported.

As a replacement for the RPM packages, you can use the following sources to install
LibreOffice:

- Official Flatpak package in the Flathub repository: <https://flathub.org/apps/org.libreoffice.LibreOffice>.
- Official RPM packages: <https://www.libreoffice.org/download/download-libreoffice/>.

Likewise, the Inkscape Flatpak image (`inkscape-flatpak`) is also deprecated.
As a replacement, use the `inkscape` RPM package from <https://inkscape.org/>.

### Virtualization

The following virtualization related features and functionalities are deprecated in Oracle
Linux 9.

#### Signatures Using SHA-1

The use of SHA1-based signatures to perform SecureBoot image verification on UEFI
(PE/COFF) executables is deprecated. Instead, use signatures that are based on SHA-2 or
later.

#### Virtual Machine Manager

In place of the deprecated Virtual Machine Manager (`virt-manager`), use
the web console, otherwise known as Cockpit.

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

#### Legacy CPU Models

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

#### RDMA-based Live Migration

In this release, RDMA-based live migration of virtual machines is deprecated.

### Containers

The following features and functionalities that are related to containers are deprecated in
Oracle Linux 9.

#### Oracle Linux 9 Containers on Oracle Linux 7 Hosts

Creating Oracle Linux 9 containers on an Oracle Linux 7 host is unsupported. Attempts to deploy this configuration might succeed, but isn't guaranteed.

#### SHA-1 Algorithm Within Podman

Support for using the SHA-11 algorithm to generate the filename of the rootless network
namespace is removed in Podman. You should restart rootless containers that were
configured by using Podman earlier than version 4.1.1. Restarting these containers
rather than just using `slirp4netns` ensures that these containers and
join the network and connect with containers that were created with upgraded Podman
versions.

#### CNI Network Stack

The Container Network Interface (CNI) network stack is deprecated. You can use the
Netavark network stack with Podman and other Open Container Initiative (OCI) container
management applications. The Netavark network stack for Podman is also compatible with
advanced Docker functionalities.

### Deprecated Packages

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.3/ol9-KnownIssues.html -->

## 5 Known Issues

This
chapter describes known issues that you may encounter when installing and using the Oracle
Linux 9 software. Unless indicated otherwise, the issues apply to both x86\_64 and aarch64
systems. Information that pertains only to a specific platform is also noted accordingly.

### Installation Issues

The following are known installation issues for Oracle Linux 9.

#### Error Messages Displayed While Removing RHCK

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

### Cockpit Podman Interface Might Require Additional Proxy Configuration

If you use the Cockpit web console and the system that you are managing accesses the
Internet by using a proxy server, you might need to perform additional configuration
steps on the host where Podman is running. Cockpit web console uses the Podman API
Service, a systemd service that enables applications to interact with standard Podman
commands. To configure the Podman API Service so that it uses a proxy server to access
the Internet when pulling images, you must perform the following steps:

1. Create the `/etc/systemd/system/podman.service.d` directory, if it
   doesn't already exist, to host Systemd service drop-in configuration specific to the
   Podman API
   service.

   ```
   sudo mkdir -p /etc/systemd/system/podman.service.d
   ```
2. Create or modify
   `/etc/systemd/system/podman.service.d/http-proxy.conf` to contain
   contents similar to:

   ```
   [Service]
   Environment="HTTP_PROXY=proxy_URL:port"
   Environment="HTTPS_PROXY=proxy_URL:port"
   ```

   Replace
   proxy\_URL:port with the URL and port number for the proxy
   server that you need to use.
3. Reload the Systemd configuration changes and restart the Podman API
   service:

   ```
   sudo systemctl daemon-reload
   sudo systemctl restart podman
   ```

(Bug ID 35155346)

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

### Systems With Btrfs Fail to Boot in FIPS Mode

When booted in FIPS mode, a system using Btrfs fails with the following message:

```
FATAL: FIPS integrity test failed
Refusing to continue
```

(Bug ID 36028061)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.3/ol-PackageChangesfromtheUpstreamRelease.html -->

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

#### Added Binary Packages for AppStream by Oracle

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

#### Added Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages have been added to CodeReady Linux Builder by Oracle:

- `oraclelinux-sb-certs`

#### Modified BaseOS Binary Packages

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
- `linux-firmware`
- `linux-firmware-core`
- `linux-firmware-whence`
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
- `openssl`
- `openssl-libs`
- `os-prober`
- `pcre2`
- `pcre2-syntax`
- `polkit`
- `polkit-libs`
- `procps-ng`
- `procps-ng-i18n`
- `python3-cffi`
- `python3-chardet`
- `python3-configshell`
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
- `python3-six`
- `python3-sss`
- `python3-sssdconfig`
- `python3-sss-murmur`
- `python3-urllib3`
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
- `unzip`
- `vim-filesystem`
- `vim-minimal`
- `yum`
- `yum-utils`

#### Modified Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `anaconda-widgets-devel`
- `crash-devel`
- `cups-filters-devel`
- `dotnet-sdk-6.0-source-built-artifacts`
- `dotnet-sdk-7.0-source-built-artifacts`
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
- `libvirt-devel`
- `libvirt-docs`
- `libvirt-lock-sanlock`
- `libwebp-tools`
- `lua-guestfs`
- `mpich`
- `munge-devel`
- `NetworkManager-libnm-devel`
- `nmstate-devel`
- `nmstate-static`
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
- `python-packaging-doc`
- `qatzip-devel`
- `ruby-libguestfs`
- `sanlock-devel`
- `sendmail-milter`
- `sendmail-milter-devel`
- `tog-pegasus-devel`
- `virt-v2v-man-pages-ja`
- `virt-v2v-man-pages-uk`

#### Modified AppStream Binary Packages

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
- `aspnetcore-targeting-pack-6.0`
- `aspnetcore-targeting-pack-7.0`
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
- `dotnet-host`
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
- `dracut-caps`
- `dracut-live`
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
- `nginx`
- `nginx-all-modules`
- `nginx-core`
- `nginx-filesystem`
- `nginx-mod-http-image-filter`
- `nginx-mod-http-perl`
- `nginx-mod-http-xslt-filter`
- `nginx-mod-mail`
- `nginx-mod-stream`
- `nmstate`
- `nmstate-libs`
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
- `openssl-devel`
- `openssl-perl`
- `open-vm-tools`
- `open-vm-tools-desktop`
- `open-vm-tools-salt-minion`
- `open-vm-tools-sdmp`
- `open-vm-tools-test`
- `osinfo-db`
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
- `pcp-export-pcp2spark`
- `pcp-export-pcp2xml`
- `pcp-export-pcp2zabbix`
- `pcp-export-zabbix-agent`
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
- `python3-blivet`
- `python3-blockdev`
- `python3-boom`
- `python3-clang`
- `python3-dnf-plugin-modulesync`
- `python3-idm-pki`
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-iscsi-initiator-utils`
- `python3-kickstart`
- `python3-libguestfs`
- `python3-libnmstate`
- `python3-libreport`
- `python3-net-snmp`
- `python3-numpy`
- `python3-numpy-f2py`
- `python3-packaging`
- `python3-pcp`
- `python3-psutil`
- `python3-PyMySQL`
- `python3-rtslib`
- `python3-sanlock`
- `python3-scipy`
- `python3-toml`
- `qatengine`
- `qatzip`
- `qatzip-libs`
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

#### Removed CodeReady Linux Builder Binary Packages

The following binary packages from the CodeReady Linux Builder upstream release have been removed:

- `redhat-sb-certs`
- `rhc-devel`
- `swig-debuginfo`
- `swig-debugsource`

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
- `rhnsd`

#### Added Source Packages for AppStream by Oracle

The following source packages have been added to AppStream by Oracle:

- `dnf-plugin-spacewalk`
- `dtrace`
- `pyOpenSSL`
- `python3-dnf-plugin-ulninfo`
- `python-hwdata`
- `rhn-client-tools`
- `rhnlib`

#### Modified BaseOS Source Packages

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
- `mcelog`
- `microcode_ctl`
- `NetworkManager`
- `nvmetcli`
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
- `python-urllib3`
- `PyYAML`
- `redhat-release`
- `rpm`
- `selinux-policy`
- `shim`
- `sos`
- `sssd`
- `systemd`
- `tuned`
- `unzip`
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
- `java-11-openjdk`
- `java-17-openjdk`
- `java-1.8.0-openjdk`
- `kernel-srpm-macros`
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
- `vim`
- `virt-p2v`
- `virt-top`
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
- `dotnet7.0`
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
- `sanlock`
- `sendmail`
- `sssd`
- `tog-pegasus`
- `virt-v2v`

#### Removed BaseOS Source Packages

The following source packages from the BaseOS upstream release have been removed:

- `kpatch`
- `subscription-manager`
- `subscription-manager-cockpit`
- `subscription-manager-rhsm-certificates`

#### Removed AppStream Source Packages

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