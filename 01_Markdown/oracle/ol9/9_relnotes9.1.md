---
title: "Release Notes for Oracle Linux 9.1"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.1"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol9"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux 9

Release Notes for Oracle Linux 9.1

F70545-08

January 2026

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 9 Release Notes for Oracle Linux 9.1

F70545-08

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2022, 2026, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.1/ol9.1-Preface.html -->

## Preface

[Oracle Linux 9: Release Notes for Oracle Linux 9.1](https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.1/) provides information about the new features
and known issues in the Oracle Linux 9.1 release. The information applies to both x86\_64 and
64-bit Arm (aarch64) architectures. This document might be updated after it is released.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.1/ol9-AboutOracleLinux9.html -->

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

- `kernel-5.14.0-162.6.1.el9_1` (Red Hat Compatible Kernel (RHCK))
- `kernel-uek-5.15.0-3.60.5.1.el9uek` (Unbreakable Enterprise Kernel
  Release 7 (UEK R7))

  For new installations, the UEK kernel is automatically enabled and installed. It also
  becomes the default kernel on first boot.

For the aarch64 platform, Oracle Linux ships with the UEK kernel only.

The Oracle Linux release is tested as a bundle, as shipped on the installation media
image. When installed from the installation media image, the kernel's version included
in the image is the minimum version that is supported. Downgrading kernel packages is
not supported, unless recommended by Oracle Support.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.1/ol9-NewFeaturesandChanges.html -->

## 2 New Features and Changes

Unless indicated otherwise, the following new features, major enhancements, bug fixes, and
other changes that are introduced in this release of Oracle Linux 9 apply to both the x86\_64
and 64-bit Arm (aarch64) platforms.

### Installation and Boot

The following features, enhancements, and changes related to installation and boot are
introduced in this release of Oracle Linux 9.

#### `--allow-ssh` Kickstart Option Enables Password-based SSH Root Logins

The `--allow-ssh` option is used with the `rootpw` command.
With this option, the same functionality in graphical installations that enables root users
to login by using SSH with a password is now available in kickstart installations.

### Operating System and Software Management

The following features, enhancements, and changes related to the OS and software management
are introduced in this Oracle Linux 9 release.

#### `modulesync` Command Replaces Certain Workflows

This enhancement facilitates the installation of modular packages by ensuring the presence
of modular metadata. Previously, the metadata is not included in the installation.
Consequently, you would use the `dnf` command first to download the packages,
and then the `createrepo_c` command to redistribute those packages.

The `modulesync` command streamlines the process by downloading the modular
packages and at the same time creating a repository with modular metadata in a working
directory.

#### Boot Loader Menu Hidden by Default

The GRUB boot loader does not display the boot menu by default.

However, if a previous system boot fails, then the GRUB boot loader displays the boot menu
at the next system boot.

To access the boot menu manually, do one of the following steps while the system is
booting:

- Press Esc repeatedly.
- Press F8 repeatedly.
- Hold Shift.

To disable the default setting, use the following command:

```
sudo grub2-editenv - unset menu_auto_hide
```

### Shells and Command Line Tools

The following features, enhancements, and changes related to shells and command line tools
are introduced in this Oracle Linux 9 release.

#### `xmlstarlet` Package is Available in a Recognized Repository

The `xmlstarlet` package was previously available in the
`ol9_developer_EPEL` repository, but is now available in the supported
`ol9_appstream` repository. This package contains utilities that are
frequently used on the command line to perform common operations on XML files that other
command line tools are unable to do easily by taking advantage of XPath syntax to properly
locate, add, or modify information within the file.

#### Updated Packages

- `libvpd` Is Update to Version 2.2.9

  This version has the fix for database locking and an updated `libtool`
  utility version information.
- `lsvpd` is Updated to Version 1.7.14

  In this updated version, the `lsvpd` utility prevents corruption of the
  database file when you run the `vpdupdate` command.

#### `sysctl` Introduces Same Syntax as `systemd-sysctl` for Handling Arguments

The `sysctl` utility can parse hyphens (`-`) or globs
(`*`) that are in configuration lines. For more information about the
`systemd-sysctl` syntax, see the `sysctl.d(5)` manual page.

### Infrastructure Services

The following features, enhancements, and changes related to infrastructure services are
introduced in this Oracle Linux 9 release.

#### `chrony` Uses DHCPv6 NTP Servers

You can use specify DHCP options to indicate how the NetworkManager dispatcher script for
`chrony` updates the Network time protocol (NTP) sources. The DHCP option
56 indicates that DHCPv6 is used while the DHCP option 42 specifies that DHCPv4 is used.
With these options, the dispatcher script can be configured to use NTP servers that are
provided by both DHCPv6 and DHCPv4.

#### `chrony` Updated to Version 4.2

The updated version includes the following changes and enhancements:

- The server interleaved mode is updated to be more reliable and to support multiple
  clients behind a single address translator that uses Network Address Translation
  (NAT).
- The Network Time Protocol Version 4 (NTPv4) extension field is available to improve
  time synchronization stability and precision of estimated errors. This field extends the
  capabilities of the NTPv4 protocol. You can enable the field by using the `extfield
  F323` option. This option is experimental.
- NTP forwarding over the Precision Time Protocol (PTP) is available to enable full
  hardware timestamping on network interface cards (NICs) that have timestamping limited to
  PTP packets. You can enable NTP over PTP by using the `ptpport 319` option.
  This option is experimental.

#### `unbound` Updated to Version 1.16.2

The updated versions includes bug fixes and the following enhancements:

- Recipients can verify the zone contents for data integrity and origin authenticity by
  using ZONEMD Zone Verification to ensure compliance with RFC 8976.
- `unbound` enables you to configure persistent TCP connections.
- The SVCB and HTTPS types and handling according to the Service binding and parameter
  specification through the DNS `draft-ietf-dnsop-svcb-https` document were
  added.
- The default TLS ciphers from system cryptographic policies are used by
  `unbound` components.
- The Special-Use Domain `home.arpa.` defined in RFC 8375 is available for
  non-unique use in residential home networks.
- Selective enabling of `tcp-upstream` queries for stub or forward zones
  is supported.
- The `aggressive-nsec` option is enabled by default.
- Logic for the `ratelimit` function is updated and introduces
  `ratelimit-backoff` and `ip-ratelimit-backoff` for an
  optional more aggressive countermeasure when the limit is reached.
- The new `rpz-signal-nxdomain-ra` option can be used to unset the
  `RA` flag when a query is blocked by an Unbound response policy zone
  (RPZ) nxdomain reply.
- Additional error information is provided through Extended DNS Errors (EDE) in
  accordance with RFC 8914.

#### Password Encryption Function Available in `whois`

The `whois` package supports the `/usr/bin/mkpasswd` binary,
which enables you to encrypt a password with the `crypt` C library interface.

#### `frr` Updated to Version 8.2.2

The updated `frr` package includes the following changes and
enhancements:

- Support for Ethernet VPN (EVPN) route type-5 gateway IP Overlay Index.
- Support for Autonomous system border router (ASBR) summarization in the
  Open-shortest-path-first (OSPFv3) protocol.
- Usage of stub and not-so-stubby-areas (NSSA) in OSPFv3 is enhanced.
- Support for graceful restart capability in OSPFv2 and OSPFv3.
- The link bandwidth in the border gateway protocol (BGP) is compliant with the IEEE 754
  standard. To use the previous encoding method, run the `neighbor PEER
  disable-link-bw-encoding-ieee` command in the existing configuration.
- Support for the long-lived graceful restart capability in BGP.
- Implementation of RFC 9003 on extended administrative shutdown communication as well
  as extended optional parameters length in BGP, based on RFC 9072.

### Security

The following features, enhancements, and changes related to security are introduced in this
Oracle Linux 9 release.

#### OpenSSH Supports Setting the Minimum RSA Key Length

Using short RSA keys makes the system more vulnerable to attacks. This update enables you
to set minimum RSA key lengths for OpenSSH servers and clients through the
`RequiredRSASize` option in the `/etc/ssh/sshd_config` file
for OpenSSH servers or in the `/etc/ssh/ssh_config` file for OpenSSH clients.

#### `crypto-policies` Enforces OpenSSH 2048-bit RSA Key Length Minimum by Default

Consequent to the support for setting minimum RSA key length in OpenSSH, the system-wide
cryptographic policies enforce the 2048-bit minimum key length for RSA by default.

OpenSSH failing connections with an `Invalid key length` error message
indicates that you need to use longer RSA keys.

You can relax the default key length policy restriction, but at the expense of security.
Ensure that you know the risks before performing any of the following methods:

- Define a custom subpolicy by inserting the `min_rsa_size@openssh = 1024`
  parameter into the
  `/etc/crypto-policies/policies/modules/RSA-OPENSSH-1024.pmod` file.
- Apply the custom subpolicy using the `update-crypto-policies --set
  DEFAULT:RSA-OPENSSH-1024` command.

#### OpenSSL Option Supports SHA-1 for Signatures

By default, OpenSSL 3.0.0 does not support SHA-1 for signature creation and verification.
SHA-1 key derivation functions (KDF) and hash-based message authentication codes (HMAC) are
still supported. However, backwards compatibility with Oracle Linux 8 systems that still use
SHA-1 for signatures can be achieved through the `rh-allow-sha1-signatures`
configuration option. If enabled in the `alg_section` of
`openssl.cnf`, this option enables the creation and verification of SHA-1
signatures.

This option is automatically enabled if the LEGACY system-wide cryptographic policy is
set, which might be needed if RPM packages with SHA-1 signatures are installed.

#### `crypto-policies` Supports `sntrup761x25519-sha512@openssh.com` Key Exchange (KEX) Method

The post-quantum `sntrup761` algorithm is already available in the OpenSSH
suite. This method provides better security against attacks from quantum computers. To
enable this key exxchange method, create and apply a subpolicy, for example:

```
sudo echo 'key_exchange = +SNTRUP' > /etc/crypto-policies/policies/modules/SNTRUP.pmod
sudo update-crypto-policies --set DEFAULT:SNTRUP
```

#### Support RSA Keys Shorter Than 1023 Bits Removed in NSS

Updates of Network Security Services (NSS) libraries have dropped support of RSA keys of
128 bits in favor of 1023 bits. With this change, NSS no longer performs the following
functions:

- Generate RSA keys shorter than 1023 bits.
- Sign or verify RSA signatures with RSA keys shorter than 1023 bits.
- Encrypt or decrypt values with RSA key shorter than 1023 bits.

#### SCAP Security Guide Updated to 0.1.63

The SCAP Security Guide (SSG) provides new compliance rules for `sysctl`,
`grub2`, `pam_pwquality`, and build time kernel
configuration. New profiles that are specific for Oracle Linux 9 include the following:

- ANSSI-BP-028 (enhanced, high, intermediary, and minimal)
- CUI
- E8
- HIPAA
- OSPP
- PCI-DSS
- Standard
- STIG
- STIG\_GUI

#### `keylime` Package Available

Keylime is a tool for attestation of remote systems by using trusted platform module (TPM)
technology. Keylime enables you to verify and continuously monitor the integrity of remote
systems. Further, the tool enables you to specify encrypted payloads that Keylime delivers
to the monitored machines. You can also use the tool to define automated actions that
trigger whenever a system fails the integrity test.

#### Rsyslog Error Files Can Be Set With Maximum Size Option

The `action.errorfile.maxsize` option enables you to specify a maximum
number of bytes of the error file for the Rsyslog log processing system. Beyond the maximum
setting, Rsyslog cannot write any additional errors or other data in it. The option prevents
oversized error files from rendering the host system unusable.

#### `opencryptoki` Updated to Version 3.18.0

This version includes the following improvements:

- Default to Federal Information Processing Standards (FIPS) compliant token data format
  (tokversion = 3.12).
- Enabled restricting usage of mechanisms and keys using a global policy.
- Enabled statistics counting of mechanism usage.
- The `ICA/EP11` tokens can use `libica` library version 4.
- The `p11sak` tool allows setting different attributes for public and
  private keys.
- The `C_GetMechanismList` does not return
  `CKR_BUFFER_TOO_SMALL` in the EP11 token.

In this version, data formats that use algorithms that are not approved by FIPS no longer
work. Therefore, to use `openCryptoki` on Oracle Linux 9, you must migrate
tokens that used the earlier token data format to use the new data format before enabling
FIPS on the system. To migrate, use the `pkcstok_migrate` utility, which is
provided with `openCryptoki`.

Note:

The `pkcstok_migrate` utility uses non-FIPS-approved algorithms during
the migration. You must use this tool before enabling FIPS mode on the system. For
additional information, see [Migrating to FIPS compliance - pkcstok\_migrate
utility](https://www.ibm.com/docs/en/linux-on-systems?topic=tools-pkcstok-migrate).

#### `fapolicyd` Updated to 1.1.3

The updated `fapolicyd` software framework includes several enhancements
including a change to use the OpenSSL library as the cryptographic engine for hash
computation and a facility to allow rules to match the parent process ID (PPID) of a
subject. A fix to the `fagenrules --load` command is also included.

#### SELinux Policy Confines Additional Services

With updated `selinux-policy` packages, SELinux confines the following
services:

- `ksm`
- `nm-priv-helper`
- `rhcd`
- `stalld`
- `systemd-network-generator`
- `targetclid`
- `wg-quick`

#### SELinux Supports the `self` Keyword in Type Transitions

SELinux tooling supports type transition rules with the `self` keyword in
the policy sources, which enables the SELinux policy for labeling of anonymous inodes.

#### SELinux User-space Packages Updated

User-space packages `libsepol`, `libselinux`,
`libsemanage`, `policycoreutils`,
`checkpolicy`, and `mcstrans` include the following
changes;

- The `-T` option in the `setfiles`,
  `restorecon`, and `fixfiles` tools supports and enables
  parallel relabeling.

  With this option, you can specify the number of process threads. Or, you can use
  `-T 0` for setting the maximum of available processor cores.
- The new `--checksum` option prints SHA-256 hashes of modules.
- New policy utilities are added to the `libsepol-utils` package.

#### SELinux Automatic Relabeling Now Parallel by Default

The `-T 0` option setting is included in the automatic relabeling script
that is run by the `fixfiles` command line. The `-T 0` option
ensures that the `setfiles` program uses the maximum of available processor
cores for relabeling by default.

To override this default setting, choose one of the following commands:

- ```
  fixfiles -T 1 onboot
  ```
- ```
  echo "-T 1" > /.autorelabel
  ```

### Networking

The following features, enhancements, and changes related to networking are introduced in
this Oracle Linux 9 release.

#### `firewalld` Updated to version 1.1.1

This version provides multiple bug fixes and enhancements including the following:

- Rich rules support NetFilter-log (NFLOG) target for user-space logging. No
  NFLOG-capable logging daemon exists in Oracle Linux. To collect the logs that you need,
  use the `tcpdump -i nflog` command.
- `ingress-zones=HOST` and `egress-zones={ANY, source based
  zone}` settings enable support for port forwarding in firewall policies.
- Support is added for the `afp`, `http3`,
  `jellyfin`, `netbios-ns`, `ws-discovery`,
  and `ws-discovery-client` services
- Tab-completion and sub-options in Z Shell for the `policy` option is
  supported.

#### NetworkManager Displays Warnings About Unavailability of WEP Support

The Wired Equivalent Privacy (WEP) security algorithm has been removed from
`wpa_supplicant` packages. This enhancement updates NetworkManager to
reflect these changes. Appropriate mechanisms are in place to indicate the absence of
support for WEP, and attempts to connect to WEP protected network generates an error
message.

For secure encryption, use only wifi networks with Wi-Fi Protected Access 2 (WPA2) and
WPA3 authentication.

### Kernel and System Libraries

The following notable features, enhancements, and changes apply to the Red Hat Compatible
Kernel (RHCK) that's shipped with the current Oracle Linux 9 version.

#### BPF Updated to the Linux Kernel Version 5.16

This updated version of the Berkeley Packet Filter (BPF) facility multiple bug fixes and
enhancements such as the following:

- Streamlined internal BPF program sections handling and
  `bpf_program__set_attach_target()` API function in the
  `libbpf` userspace library. The function sets the BPF based attach
  targets for BPF based programs.
- Support for the following parameters and funtionalities:

  - `BTF_KIND_TAG` kind, which allows you to tag declarations, as well
    as the `BTF_KIND_DECL_TAG` kind.
  - `bpf_get_branch_snapshot()` helper which enables the tracing program
    to capture the last branch records (LBR) from the hardware.
  - Legacy `kprobe` in the `libbpf` userspace library
    that enables `kprobe` trace events creation through the legacy
    interface.
  - Capability through the `__sk_buff` helper function to access
    hardware timestamps through BPF specific structures with the .
  - Batched interface for RX buffer allocation in `AF_XDP` buffer pool,
    with driver support for `i40e` and `ice`.
  - Legacy `uprobe` support in `libbpf` userspace library
    to complement recently merged legacy `kprobe`.
  - `bpf_trace_vprintk()` as a variadic `printk` helper.
  - `libbpf` opt-in that enforces stricter BPF program section name
    handling as part of `libbpf` 1.0 effort.
  - `libbpf` for locating specialized maps, such as `perf
    RB` and internally delete BTF type identifiers while creating them.
  - `bloomfilter` BPF map type to test if an element exists in a set.
  - Kernel module function calls from BPF.
  - Typeless and weak `ksym` in light skeleton.

For a full list and descriptions of BPF features in the running kernel, use the
`bpftool feature` command.

#### `tpm2-tools` Package Updated to 5.2.1

This version provides additional support for the following features and tools:

- Public-key output when a primary object is created by using the
  `tpm2_createprimary` and `tpm2_create` tools.
- The `tpm2_print` tool for printing public-key output formats. The tool
  decodes a Trusted Platform Module (TPM) data structure and prints enclosed elements.
- The `tpm2_eventlog` tool for reading logs larger than 64 KB.
- The `tpm2_sessionconfig` tool to support displaying and configuring
  session attributes.

For more information, see the `/usr/share/doc/tpm2-tools/Changelog.md`
file.

### High Availability and Clusters

The following features, enhancements, and changes related to high availability are introduced
in this Oracle Linux 9 release.

#### `pcs stonith update-scsi-devices` Accepts Updates to Multipath SCSI Devices Without Restarting the Cluster

The `pcs stonith update-scsi-devices` command can be used to update fencing
on a cluster by using multipath devices without requiring a restart of other cluster
resources running on the same node. For example:

```
sudo pcs stonith update-scsi-devices <mpath-fence-dev> set <device-path>
sudo pcs stonith update-scsi-devices <mpath-fence-dev> add <device-path>
sudo pcs stonith update-scsi-devices <mpath-fence-dev> remove <device-path>...
```

#### Pacemaker Clusters Have UUIDs

The `pcs` command generates a UUID that you can use to uniquely identify
the cluster when it is created. The UUID is displayed when you run the `pcs cluster
config [show]` command. You can add a UUID to an existing cluster or regenerate a
UUID if one already exists by running `pcs cluster config uuid generate`.

#### Pacemaker Updated to Version 2.1.4

The updated version contains the following changes:

- New value `stop_unexpected` can be assigned to the
  `multiple-active` resource parameter

  The `multiple-active` resource parameter determines recovery behavior
  when additional instances unexpectedly become active on a resource. By default, the
  parameter is set to execute a full restart of the resource, even if the resource is
  operating normally for the other originally configured instances.

  `stop_unexpected` enables you to specify that only unexpected instances
  of a multiple active resource are stopped. However, you must verify that the service and
  its resource agent continue to function with these extra active instances without
  requiring to restart the resource.
- Pacemaker `allow-unhealthy-node` resource meta-attribute added

  The `allow-unhealthy-node` resource meta-attribute can be set to
  `true` to ensure that the resource is not forced off a node due to
  degraded node health. This feature allows the health agent to continue to run on an
  unhealthy node so that the cluster is able to automatically detect when the node becomes
  healthy again, before moving resources back to the node.
- Pacemaker includes Access Control Lists (ACLs) for system groups

  In addition to the ACLs that were previously allows for individual users, Pacemaker
  includes ACLs for system groups to facilitate role-based access controls. The
  `pcs acl group` command can now be used to apply ACLs to system groups.
  For example, to create a read-only ACL for the pcs\_ro\_group system
  group:

  ```
  sudo pcs acl group create pcs_ro_group readonly
  ```

#### Samba Not Installed With Cluster Packages

Samba packages are separated from packages for the Oracle Linux High Availability Add-on
and are therefore not automatically installed. If you require these packages, you need to
perform a manual installation.

### Dynamic Programming Languages, Web and Database Servers

The following features, enhancements, and changes related to programming languages, web
servers, and database servers are introduced in this Oracle Linux 9 release.

#### `nodejs:18` Module Stream

`Node.js 18` provides numerous new features together with bug and security
fixes over `Node.js 16`, including the following:

- `V8` engine is upgraded to version 10.1.
- The `npm` package manager is upgraded to version 8.15.0.
- `Node.js` provides a new experimental `fetch` API
  as well as an experimental `node:test` module that facilitates
  the creation of tests that report results in the Test Anything Protocol (TAP)
  format.

To install the `nodejs:18` module stream, type:

```
sudo dnf module install nodejs:18
```

#### `php:8.1` Module Stream Available

The new version enables you to do the following:

- Use the Enumerations (`Enums`) feature to define a custom type from a
  selection of possible values.
- Flag a property with the `readonly` modifier to lock the property from
  being modified after initialization.
- Use fibers, full-stack, interruptible functions.

#### Ruby 3.1.2 Available as a New Module Stream

Ruby 3.1.2 is available in a new `ruby:3.1` module stream. This version of
Ruby includes several enhancements and performance improvements over the
`ruby:3.0` module stream, including:

- An auto-complete feature and a documentation dialog included in the `Interactive
  Ruby` (IRB) utility.
- New `debug` and `error_highlight` gems to provide
  improved performance, more functionality and more granular control.
- Values in the hash literal data types and keyword arguments can now be omitted
- Parentheses can now be omitted in one-line pattern matching and the pin operator
  (`^`) now accepts an expression in pattern matching.
- YJIT, a new experimental in-process Just-in-Time (JIT) compiler, is now available on
  the AMD and Intel 64-bit architectures
- The Method Based Just-in-Time Compiler (MJIT) includes several performance improvements
  including an increase in the default maximum JIT cache value for large workloads like
  Rails.

#### `httpd` Updated to Version 2.4.53

Notable changes in the `mod_proxy` and `mod_proxy_connect`
modules include:

- `mod_proxy`: The length limit of the name of the controller has been
  increased
- `mod_proxy`: You can now selectively configure timeouts for backend and
  frontend
- `mod_proxy`: You can now disable TCP connections redirection by setting
  the `SetEnv proxy-nohalfclose` parameter
- `mod_proxy` and `mod_proxy_connect`: It is forbidden to
  change a status code after sending it to a client

In addition, a new `ldap` function has been added to the expression API,
which can help prevent the LDAP injection vulnerability.

#### `LimitRequestBody` Directive in `httpd` Configuration Updated With a New Default Value

The default value for the `LimitRequestBody` directive in the Apache HTTP
Server has been changed from `0` (unlimited) to 1 GiB to resolve a security
issue. Systems that are already configured to use an explicit value for the
`LimitRequestBody` directive are unaffected by this change.

On systems where the value of `LimitRequestBody` is not explicitly
specified in an `httpd` configuration file, the default value of 1 GiB is
applied when the `httpd` package is updated. If the total size of the HTTP
request body exceeds this 1 GiB default limit, the `413 Request Entity Too
Large` error code is returned. If your server needs to serve larger files you must
update your httpd configuration and set your limit in bytes.

#### `httpd-core` Package is Available

This new package now contains the `httpd` binary file with all essential
files. Thus, you can install only basic `httpd` functionality of the Apache
HTTP server as required, such as in the case of containers, without additional dependencies.

The `httpd` package includes `systemd`-related files,
including `mod_systemd`, `mod_brotli`, and documentation.

Additionally, the `httpd` Module Magic Number (MMN) value is moved from the
`httpd` package to the new `httpd-core` package. Therefore,
to obtain the `httpd-mmn` value of the installed `httpd`
binary, you would need to use the `apxs` binary in the
`httpd-devel` package as follows:

```
sudo apxs -q  HTTPD_MMN
```

```
20120211
```

#### `pcre2` Updated to Version 10.40

The `pcre2` package provides the Perl Compatible Regular Expressions
library v2.

In this version, you can no longer use the `\K` escape sequence in
lookaround assertions. Instead, you can use the
`PCRE2_EXTRA_ALLOW_LOOKAROUND_BSK` option. When this option is set,
`\K` is accepted only inside positive assertions but is ignored in negative
assertions.

### Compilers and Development Tools

The following features, enhancements, and changes related to compilers and development tools
are introduced in this Oracle Linux 9 release.

#### GCC Toolset 12 is Available

To install the toolset, type:

```
sudo dnf install gcc-toolset-12
```

To run a tool from the toolset, type:

```
scl enable gcc-toolset-12 tool
```

To run a shell session where the tool versions from GCC Toolset 12 override system versions
of these tools, type:

```
scl enable gcc-toolset-12 bash
```

The new GCC Toolset contains the following tools:

- Updated GCC compiler
- Annobin 10.79
  - Contains a new command line option for `annocheck` to avoid using
    the `debuginfod` service if no alternatives exist for finding debug
    information. The `debuginfod` service can provide more debug
    information, but can also downgrade `annocheck`'s performance if the
    `debuginfod` server is unavailable.
  - `meson` and `ninja` are alternative tools for building
    Annobin sources, if desired.
  - Annocheck supports binaries built by the Rust 1.18 compiler.

  In some circumstances, this version might cause compilation errors with messages
  similar to the
  following:

  ```
  cc1: fatal error: inaccessible plugin file
  opt/rh/gcc-toolset-12/root/usr/lib/gcc/architecture-linux-gnu/12/plugin/gcc-annobin.so
  expanded from short plugin name gcc-annobin: No such file or directory
  ```

  To
  work around this issue, create a symbolic link in the plugin directory as
  follows:

  ```
  cd /opt/rh/gcc-toolset-12/root/usr/lib/gcc/architecture-linux-gnu/12/plugin
  sudo ln -s annobin.so gcc-annobin.so
  ```

  For architecture,
  specify the architecture of the system you are using.
- `binutils` 2.38
  - All tools in this package can be set to display or warn about the presence of
    multibyte characters.
  - The `readelf` and `objdump` tools now automatically
    follow any links to separate `debuginfo` files by default. To disable
    this behavior, choose one of the following commands:.

    ```
    readelf --debug-dump=no-follow-links
    ```

    ```
    objdump --dwarf=no-follow-links
    ```
- GCC 12 supports `_FORTIFY_SOURCE` level 3

  When building applications
  with GCC 12 or later versions, you can use `-D_FORTIFY_SOURCE=3` in the
  compiler command line to improve coverage of source code fortification as well as
  security for the applications. This support is also available in all Clang with the
  `__builtin_dynamic_object_size` built in.
- GDB 11.2

  - Adds new support for Aarch64 MTE.
  - Provides the `--qualified` option for `-break-insert`
    and `-dprintf-insert` that looks for an exact match of the userâs event
    location instead of searching in all scopes.
  - Provides the `--force-condition` option where any supplied condition
    can be defined even if the condition is currently invalid.
  - Provides the `-break-condition --force` option and has analogous
    behavior as in the preceding option.
  - Provides the `-file-list-exec-source-files` option that accepts
    optional `REGEXP` to limit output.
  - The `.gdbinit` search path includes the config directory.
  - Supports `$HOME/.config/gdb/gdbearlyinit` or
    `$HOME/.gdbearlyinit`.
  - Provides the `-eix` and `-eiex` early initialization
    file options.

  In the erminal user interface (TUI), support is available for mouse actions.
  Additionally, key combinations that do not act on the focused window are now passed to
  GDB.

  This updated GDB also includes new and revised commands as well as updates to the
  Python API.

#### GDB Supports Power 10 PLT Instructions

This update enables users to step into shared library functions and inspect stack
backtraces by using GDB version 10.2-10 and later.

#### Rust Toolset Updated to Version 1.62.1

- You can now use tuple, slice, and struct patterns as the left-hand side of an
  assignment. For example, a tuple assignment can swap two variables:

  ```
  (a, b) = (b, a);
  ```

  Note that destructuring assignments with operators
  such as `+=` are not allowed.
- Inline assembly is available on x86\_64 and aarch64 using the
  `core::arch::asm!` macro.
- Enums can derive the `Default` trait with an explicitly annotated
  `#[default]` variant.
- An optimized `futex`-based implementation is used for
  `Mutex`, `CondVar`, and `RwLock`, to
  replace pthreads.
- Custom exit codes from `main`, including user-defined types that use the
  `Termination` trait, can be used.
- Cargo supports more control over dependency features. The `dep:` prefix
  can refer to an optional dependency without exposing that as a feature, and a
  `?` only enables a dependency feature if that dependency is enabled
  elsewhere, like `package-name?/feature-name`.
- A new `cargo add` subcommand for adding dependencies to
  `Cargo.toml` is available.

For more details, see consecutive upstream release announcements, including the following:

- [Rust 1.59.0](https://blog.rust-lang.org/2022/02/24/Rust-1.59.0.html)
- [Rust 1.60.0](https://blog.rust-lang.org/2022/04/07/Rust-1.60.0.html)
- [Rust 1.61.0](https://blog.rust-lang.org/2022/05/19/Rust-1.61.0.html)
- [Rust 1.62.0](https://blog.rust-lang.org/2022/06/30/Rust-1.62.0.html)
- [Rust 1.62.1](https://blog.rust-lang.org/2022/07/19/Rust-1.62.1.html)

#### LLVM Toolset Updated to Version 14.0.0

- On 64-bit x86, support for `AVX512-FP16` instructions has been added.
- Support for the Armv9-A, Armv9.1-A and Armv9.2-A architectures has been added.

This version also includes the following changes in `clang`:

- `if consteval` for `C++2b` is now implemented.
- `AVX512-FP16` instructions have been added for the x86\_64 architecture.
- The `-E -P` preprocessor output now always omits blank lines, matching
  GCC behavior. Previously, up to 8 consecutive blank lines could appear in the output.
- Support `-Wdeclaration-after-statement` with `C99` and
  later standards, and not just C89, matching GCCâs behavior. A notable use case is
  supporting style guides that forbid mixing declarations and code, but want to move to
  newer C standards.

For more information, see the [LLVM Toolset](https://releases.llvm.org/14.0.0/docs/ReleaseNotes.html) and [Clang](https://releases.llvm.org/14.0.0/tools/clang/docs/ReleaseNotes.html) upstream release notes.

#### `maven:3.8` Module Stream Updated

To install, type:

```
sudo dnf module install maven:3.8
```

### Virtualization

The following features, enhancements, and changes related to virtualization are introduced in
this Oracle Linux 9 release.

#### `open-vm-tools` Updated to 12.0.5

In this updated version of the open source implementation of VMware Tools, support has
been added for the Salt Minion tool which is managed through guest OS variables.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.1/ol9-TechnologyPreview.html -->

## 3 Technology Preview

The following items are available as technical previews in this release of Oracle Linux. Note
that some items listed apply to Red Hat Compatible Kernel (RHCK) and might already be
available in UEK.

### Networking

The following networking features are available as technology previews.

#### `systemd-resolved` Service

The `systemd-resolved` service provides name resolution to local applications.
Its components include a caching and validating DNS stub resolver, a Link-Local Multicast Name
Resolution (LLMNR), and Multicast DNS resolver and responder.

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

#### WireGuard

WireGuard is a VPN solution that has improved security features and is easily
configurable.

Note that WireGuard is fully supported in UEK. See [Oracle Linux: Configuring Virtual Private Networks](https://docs.oracle.com/en/operating-systems/oracle-linux/vpn/)
for more information on using WireGuard on Oracle Linux.

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

### File Systems and Storage

The following features that are related to file systems and storage are available as
technology preview.

#### `nvme-stas` Package

The `nvme-stas` package, which is a Central Discovery Controller (CDC)
client for Linux, handles the following functionalities:

- Asynchronous Event Notifications (AEN)
- Automated NVMe subsystem connection controls
- Error handling and reporting
- Automatic (`zeroconf`) and Manual configuration.

This package consists of two daemons, Storage Appliance Finder (`stafd`)
and Storage Appliance Connector (`stacd`).

#### Stratis

A local storage manager, Stratis manages file systems on top of pools of storage and
provides features such as the following:

- Manage snapshots and thin provisioning
- Automatically grow file system sizes as needed
- Maintain file systems

You administer Stratis storage through the `stratis` utility, which
communicates with the `stratisd` background service.

#### NVMe-oF Discovery Service

The NVMe-oF Discovery Service features are defined in the NVMexpress.org Technical Proposals
(TP) 8013 and 8014. To preview these features, install the `nvme-cli 2.0`
package and attach the host to an NVMe-oF target device that implements TP-8013 or TP-8014.
For more information about TP-8013 and TP-8014, see the NVM Express 2.0 Ratified TPs from the
[https://nvmexpress.org/developers/nvme-specification/](https://nvmexpress.org/specifications/) website.

Note that NVMe-oF is supported in UEK.

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

### Virtualization

The following virtualization features are available as technology previews.

#### `virtio-mem` for Intel® and AMD Systems

Oracle Linux 9 introduces the `virtio-mem` feature for AMD and Intel®
systems. With `virtio-mem`, you can dynamically add or remove host memory in
virtual machines (VMs).

To use `virtio-mem`, do the following:

1. Define `virtio-mem` memory devices in the XML configuration of a
   VM.
2. Use the `virsh update-memory-device` command to request memory device
   size changes while the VM is running.

To see the current memory size exposed by such memory devices to a running VM, view the
XML configuration of the VM.

#### Virtualization for Arm Platforms

You can create KVM virtual machines on systems running on
the Arm (aarch64) platforms using RHCK as a technical preview.

KVM is supported on aarch64 in UEK.

#### SEV and SEV-ES

The Secure Encrypted Virtualization (SEV) feature is provided for AMD EPYC host machines that
use the KVM hypervisor. It encrypts a virtual machine's memory and protects the VM from access
by the host.

SEV's enhanced Encrypted State version (SEV-ES) encrypts all CPU register contents when a VM
stops running, thus preventing the host from modifying the VM's CPU registers or reading any
information from them.

Note that SEV is supported in UEK.

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.1/ol9-DeprecatedFeatures.html -->

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

### Kernel

The following kernel related features and functionalities are deprecated in Oracle Linux
9.

#### Asynchronous Transfer Mode

Asynchronous Transfer Mode (ATM) encapsulation enables Layer-2 (Point-to-Point Protocol,
Ethernet) or Layer-3 (IP) connectivity for the ATM Adaptation Layer 5 (AAL-5). Currently,
these protocols are used only in chipsets that use ADSL technology, which are being phased
out.

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

### Dynamic Programming Languages, Web and Database Servers

The following features and functionalities that are related to dynamic programming, web, and
database servers are deprecated in Oracle Linux 9.

#### Berkeley DB (`libdb`)

Deprecation of the Berkely DB (`libdb`) package includes the removal of
cryptographic algorithms and dependencies. Users of `libdb` should
migrate to a different key-value database.

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.1/ol9-KnownIssues.html -->

## 5 Known Issues

This
chapter describes known issues that you may encounter when installing and using the Oracle
Linux 9 software. Unless indicated otherwise, the issues apply to both x86\_64 and aarch64
systems. Information that pertains only to a specific platform is also noted accordingly.

### Installation Issues

The following are known installation issues for Oracle Linux 9.

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

#### `fwupd` Error Reported During an Oracle Linux 9 Update

During an update from Oracle Linux 9.0 to the current Oracle Linux 9 update release, the
installer program might report failures when setting properties for the
`pesign.service`. A message similar to the following might be displayed:

```
...
Running transaction
...
Running scriptlet: fwupd-1.7.4-2.0.2.el9_0.aarch64                        
3/4
Failed to set unit properties on pesign.service: Unit pesign.service not
found.
...
```

You can ignore the message. The upgrade successfully completes in the end.

(Bug ID 34760075)

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.1/ol-PackageChangesfromtheUpstreamRelease.html -->

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
- `rhn-setup`
- `rhn-setup-gnome`

#### Added Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages have been added to CodeReady Linux Builder by Oracle:

- `oraclelinux-sb-certs`

#### Modified BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been modified:

- `alternatives`
- `autofs`
- `bcache-tools`
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
- `libbpf`
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
- `oracle-indexhtml`
- `os-prober`
- `pcre2`
- `pcre2-syntax`
- `polkit`
- `polkit-libs`
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
- `python3-pysocks`
- `python3-pyyaml`
- `python3-requests`
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
- `dovecot`
- `dovecot-devel`
- `fwupd-devel`
- `gcc-plugin-devel`
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
- `kmod-devel`
- `libbpf-devel`
- `libbpf-static`
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
- `lua-guestfs`
- `mpich`
- `munge-devel`
- `NetworkManager-libnm-devel`
- `nginx-mod-devel`
- `nss_db`
- `nss_hesiod`
- `ocaml`
- `ocaml-compiler-libs`
- `ocaml-docs`
- `ocaml-libguestfs`
- `ocaml-libguestfs-devel`
- `ocaml-ocamldoc`
- `ocaml-runtime`
- `ocaml-source`
- `OpenIPMI-devel`
- `openscap-engine-sce-devel`
- `PackageKit-glib-devel`
- `php-libguestfs`
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
- `dotnet-host`
- `dotnet-hostfxr-6.0`
- `dotnet-runtime-6.0`
- `dotnet-sdk-6.0`
- `dotnet-targeting-pack-6.0`
- `dotnet-templates-6.0`
- `dovecot`
- `dovecot-mysql`
- `dovecot-pgsql`
- `dovecot-pigeonhole`
- `dracut-caps`
- `dracut-live`
- `efi-srpm-macros`
- `eth-tools-basic`
- `eth-tools-fastfabric`
- `fapolicyd`
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
- `java-1.8.0-openjdk`
- `java-1.8.0-openjdk-demo`
- `java-1.8.0-openjdk-devel`
- `java-1.8.0-openjdk-headless`
- `java-1.8.0-openjdk-javadoc`
- `java-1.8.0-openjdk-javadoc-zip`
- `java-1.8.0-openjdk-src`
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
- `npm`
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
- `oscap-anaconda-addon`
- `osinfo-db`
- `PackageKit`
- `PackageKit-command-not-found`
- `PackageKit-glib`
- `PackageKit-gstreamer-plugin`
- `PackageKit-gtk3-module`
- `pcre2-devel`
- `pcre2-utf16`
- `pcre2-utf32`
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
- `podman-catatonit`
- `podman-docker`
- `podman-gvproxy`
- `podman-plugins`
- `podman-remote`
- `podman-tests`
- `polkit-devel`
- `polkit-docs`
- `pykickstart`
- `python3-attrs`
- `python3-blivet`
- `python3-blockdev`
- `python3-boom`
- `python3-cffi`
- `python3-clang`
- `python3-dnf-plugin-modulesync`
- `python3-idm-pki`
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-iscsi-initiator-utils`
- `python3-kickstart`
- `python3-libguestfs`
- `python3-libreport`
- `python3-numpy`
- `python3-numpy-f2py`
- `python3-packaging`
- `python3-ply`
- `python3-psutil`
- `python3-pycparser`
- `python3-PyMySQL`
- `python3-requests+security`
- `python3-requests+socks`
- `python3-rtslib`
- `python3-sanlock`
- `python3-scipy`
- `python3-toml`
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
- `netronome-firmware`
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
- `bcache-tools`
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
- `iscsi-initiator-utils`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `krb5`
- `libbpf`
- `libdnf`
- `libkcapi`
- `libreport`
- `linux-firmware`
- `mcelog`
- `microcode_ctl`
- `NetworkManager`
- `nvmetcli`
- `openssl`
- `oracle-indexhtml`
- `os-prober`
- `pcre2`
- `polkit`
- `python-chardet`
- `python-configshell`
- `python-idna`
- `python-pysocks`
- `python-requests`
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
- `dovecot`
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
- `java-11-openjdk`
- `java-1.8.0-openjdk`
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
- `numpy`
- `opa-ff`
- `opa-fm`
- `OpenIPMI`
- `openscap`
- `openssl`
- `open-vm-tools`
- `oscap-anaconda-addon`
- `osinfo-db`
- `PackageKit`
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
- `python-cffi`
- `python-packaging`
- `python-ply`
- `python-psutil`
- `python-pycparser`
- `python-PyMySQL`
- `python-requests`
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
- `realtime-tests`
- `redhat-cloud-client-configuration`
- `redhat-indexhtml`
- `redhat-logos`
- `rhc`
- `rhc-worker-playbook`
- `toolbox`
- `virtio-win`
- `virt-who`