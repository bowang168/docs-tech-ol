---
title: "Release Notes for Oracle Linux 9.2"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.2"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol9"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux 9

Release Notes for Oracle Linux 9.2

F78223-10

January 2026

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 9 Release Notes for Oracle Linux 9.2

F78223-10

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2023, 2026, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.2/ol9.2-Preface.html -->

## Preface

[Oracle Linux 9: Release Notes for Oracle Linux 9.2](https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.2/) provides information about the new features and known issues in the Oracle
Linux 9.2 release. The information applies to both x86\_64 and 64-bit Arm (aarch64)
architectures. This document might be updated after first publication.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.2/ol9-AboutOracleLinux9.html -->

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

- `kernel-5.14.0-284.11.1`(Red Hat Compatible Kernel (RHCK))
- `kernel-uek-5.15.0-101.103.2` (Unbreakable Enterprise Kernel
  Release 7 Update 1 (UEK R7u1))

  For new installations, the UEK kernel is automatically enabled and installed. It also
  becomes the default kernel on first boot.

For the aarch64 platform, Oracle Linux ships with the UEK kernel only.

The Oracle Linux release is tested as a bundle, as shipped on the installation media image.
When installed from the installation media image, the kernel's version included in the image
is the minimum version that's supported. Downgrading kernel packages isn't supported, unless
recommended by Oracle Support.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.2/ol9-NewFeaturesandChanges.html -->

## 2 New Features and Changes

Unless indicated otherwise, the following new features, major enhancements, bug fixes, and
other changes that are introduced in this release of Oracle Linux 9 apply to both the x86\_64
and 64-bit Arm (aarch64) platforms.

### Operating System and Software Management

The following features, enhancements, and changes related to the OS and software management
are introduced in this Oracle Linux 9 release.

#### DNF Includes an offline-upgrade Command

Oracle Linux now includes the `dnf offline-upgrade` command from the DNF
`system-upgrade` plugin. Offline upgrades can help protect a system during
upgrades by performing package installations after a reboot and before libraries that might
be affected by package updates have loaded.

This feature includes the option to apply security advisory filters such as
`--advisory`, `--security`, and `--bugfix` to
limit the download of packages and their dependencies to a specified advisory.

#### DNF API Includes an unload\_plugins Function

The `unload_plugins` function is added to the DNF API so that you can unload
plugins by using the API. To use this feature, first run the `init_plugins`
function, and then run the `unload_plugins` function.

#### rpm2archive Includes a --nocompression Option

The `rpm2archive` command includes a `--nocompression`
option that can prevent compression when unpacking an RPM package.

### Infrastructure Services

The following features, enhancements, and changes related to infrastructure services are
introduced in this Oracle Linux 9 release.

#### chrony Updated to Version 4.3

The `chrony` package is updated to version 4.3. Notable features and changes
include:

- Long-term quantile-based filtering of Network Time Protocol (NTP) measurements, which
  can be enabled by adding the `maxdelayquant` option to the
  `pool`, `server`, or `peer`
  directives.
- Selection log provides more information about `chronyd` selection of
  sources and can be enabled by adding the `selection` option to the
  `log` directive.
- Improved synchronization stability when using the hardware timestamping and
  Pulse-Per-Second Hardware Clock (PHC) reference clocks.
- System clock stabilization by using a free-running stable clock, such as a Temperature
  Compensated Crystal Oscillator (TCXO), Oven-Controlled Crystal Oscillator (OCXO), or an
  atomic clock.
- Maximum polling rate increased to 128 messages per second.

#### FRRouting Updated to Version 8.3.1

The `frr` package is updated to version 8.3.1. Notable features and changes
include:

- New command for managing FRR daemons: `show thread timers` displays FRR's
  timer data.
- New Border Gateway Protocol (BGP) related commands:

  - `set as-path replace`: replaces the Autonomous System (AS) path
    attribute of a BGP route with a new value.
  - `match peer`: matches a specific BGP peer or group when configuring a
    BGP route map.
  - `ead-es-frag evi-limit`: sets a limit on the number of Ethernet A-D
    per EVI fragments that can be sent in a specified period in EVPN.
  - `match evpn route-type`: used to specify actions for certain types of
    EVPN routes, such as route-target, route-distinguisher, or MAC/IP routes.
- New commands for the Protocol Independent Multicast (PIM) daemon:

  - `debug igmp trace detail`: enables debugging for Internet Group
    Management Protocol (IGMP) messages with detailed tracing.
  - `ip pim passive`: sets the interface as passive and disables the
    sending PIM messages.
- New command for Open Shortest Path First (OSPF) protocol: `show ip ospf
  reachable-routers` displays a list of routers that are reachable at the time the
  command is run.
- New outputs for the `show zebra` command, including statuses for ECMP,
  EVPN, and MPLS.

See <https://github.com/FRRouting/frr/releases?q=8.3.1&expanded=true> for more information.

SELinux rules for FRR are included in the `frr` package to improve
integration with SELinux as new features and changes are released.

#### Very Secure FTP Daemon Updated to Version 3.0.5

The Very Secure FTP Daemon (`vsftpd`) is updated to version 3.0.5. Notable
features and changes include:

- Default requirement to use TLS version 1.2 or later for secure connections.
- Compatibility updates for use with the latest FileZilla client.

#### powertop Updated to Version 2.15

The `powertop` package is updated to version 2.15. Notable features and
changes include:

- General fixes and stability improvements.
- Improved compatibility with Ryzen processors and Kaby Lake platforms.
- Enabled Lake Field, Alder Lake N, and Raptor Lake platform functionality.
- Enabled Ice Lake NNPI and Meteor Lake mobile and desktop functionality.

#### Package Updates for systemd-sysusers Integration

The `systemd-sysusers` utility creates system users and groups during
package installation and removes them during a removal of the package. Several packages are
updated to integrate with the `systemd-sysusers` utility. The packages that
are updated include:

- `chrony`
- `dhcp`
- `radvd`
- `squid`

#### synce4l Package for Frequency Synchronization Added

The `synce4l` package manages devices that include the SyncE (Synchronous
Ethernet), a hardware feature that helps PTP clocks to achieve precise synchronization of
frequency at the physical layer. SyncE is available in certain network interface cards
(NICs) and network switches and helps Telco Radio Access Network (RAN) applications to
achieve accurate time synchronization that results in better communication efficiency. See
<https://github.com/intel/synce4l> for more
information.

#### TuneD Updated to Version 2.20.0

The `tuned` package is updated to version 2.20.0. Notable features and
changes include:

- API update to facilitate moving devices between plugin instances at runtime.
- Update to the `plugin_cpu` module:

  - The `pm_qos_resume_latency_us` feature limits the maximum time
    permitted for each CPU to transition from an idle state to an active state.
  - The `Intel® _pstate` scaling driver provides scaling algorithms to tune
    power management for a system based on usage scenarios.

#### samba Updated to Version 4.17.5

The `samba` packages are upgraded to upstream version 4.17.5. Notable
features and changes include:

- Improvements in performance around security for the Server Message Block (SMB) server
  when working with high metadata workloads.
- Addition of a `--json` option to the `smbstatus`
  command to display status information in JSON format.
- Addition of `samba.smb.conf` and `samba.samba3.smb.conf`
  modules to the `smbconf` Python API to facilitate reading and writing the
  Samba configuration directly from Python programs.

Server Message Block version 1 (SMB1) protocol is deprecated in Samba 4.11 and later. SMB1
will be removed in a future release. Back up the database files before starting Samba. When
the `smbd`, `nmbd`, or `winbind` services
start, Samba automatically updates its `tdb` database files. Downgrading
`tdb` database files isn't supported. After updating Samba, use the
`testparm` utility to verify the `/etc/samba/smb.conf`
file.

### Security

The following features, enhancements, and changes related to security are introduced in this
Oracle Linux 9 release.

#### Libreswan Updated to Version 4.9

The following features were added:

- `{left,right}pubkey=` to `addconn` and
  `whack`
- KDF self-tests to Crypto
- Updated syscall allow-list in `seccomp`
- Support of show host's authentication key (`showhostkey`) for ECDSA
  pubkeys and for printing PEM encoded public key through the `--pem`
  option
- New functionalities for the Internet Key Exchange Protocol Version 2 (IKEv2) and the
  `pluto` IKE daemon

#### OpenSSL Updated to Version 3.0.7

The OpenSSL packages are updated to version 3.0.7. Notable features and changes
include:

- Various bug fixes and improvements
- The default provider includes the `RIPEMD160` hash function.

#### SELinux User-Space Packages Updated to Version 3.5

SELinux user-space packages are updated to version 3.5. Packages affected include:
`libselinux`, `libsepol`, `libsemanage`,
`checkpolicy`, `mcstrans`, and
`policycoreutils`. Notable features and changes include:

- The `sepolicy` utility includes several Python and GTK updates. The
  manual pages are also updated to cover several missing descriptions.
- `libselinux` is improved to reduce heap memory usage by the
  `PCRE2` library.
- The `libsepol` package is updated for stricter policy validation and to
  reject attributes in Access Vector (AV) rules for kernel policies.
- The `fixfiles` script unmounts temporary bind mounts on the
  `SIGINT` signal
- The `semodule`
  `--refresh` option replaces `--rebuild-if-modules-changed`.
- Bug fixes and improvements to errors and descriptions, including translation fixes.

#### OpenSCAP Updated to Version 1.3.7

The OpenSCAP packages are updated to version 1.3.7. Notable features and changes include:

- Fixed error when processing OVAL filters.
- OpenSCAP no longer emits invalid empty `xmlfilecontent` items if an XPath
  doesn't match.
- Removed `Failed to check available memory` errors.

#### SCAP Security Guide Updated to Version 0.1.66

The SCAP Security Guide (SSG) packages are updated to version 0.1.66. Notable features and
changes include:

- Deprecation of rule `account_passwords_pam_faillock_audit` in favor of
  `accounts_passwords_pam_faillock_audit`
- Updated Oracle Linux 9 `stig` and `stig_gui` draft
  profiles to obtain more secure configuration.

#### Rsyslog Updated

RSyslog is updated for several changes. Notable features and changes include:

- A new `NetstreamDriverCaExtraFiles` directive that can be used to specify
  a list of additional certificate authority (CA) certificates for TLS encrypted remote
  logging. The new directive is available only for the `ossl` (OpenSSL)
  Rsyslog network stream driver.
- Improved privileges to the Rsyslog log processing system to limit privileges to those
  required by Rsyslog. This update tightens security for Rsyslog but doesn't affect existing
  functionality.

#### SELinux Policy Supports Rsyslog to Drop Privileges at Start

As a consequence of the privilege limitations of the Rsyslog log processing system, which
is described in the previous item, the SELinux policy has been updated so that the
`rsyslog` service can drop privileges at start.

#### SELinux Confines udftools

With updated `selinux-policy` packages, SELinux confines
`udftools` services.

#### Clevis Can Use External Tokens for Configuration

Clevis includes a new `-e` option that can be used to specify an external
token ID to avoid entering a password during `cryptsetup`. Use of external
token IDs can be used to automate configuration.

#### Tang Now Uses systemd-sysusers

The Tang server handles the addition of system users and groups through the
`systemd-sysusers` service to simplify user management and providing the
option to override system user creation by providing `sysuser.d` files with
higher priority.

#### Fapolicyd Now Provides Filtering of the RPM Database

The list of RPM-database files that `fapolicyd` stores in the trust
database can be customized by editing a new `/etc/fapolicyd/rpm-filter.conf`
configuration file. By using this feature, you can override by the default configuration
filter to specify which applications installed by RPM are permitted or excluded.

#### GnuTLS Handles PKCS#7 Padding During Decryption and Encryption

The `gnutls_cipher_encrypt3` and `gnutls_cipher_decrypt3`
block cipher functions in GnuTLS handle the PKCS#7padding, required by some protocols,
transparently. The functions can be used in combination with the
`GNUTLS_CIPHER_PADDING_PKCS7` flag to automatically add or remove padding
if the length of the original plaintext isn't a multiple of the block size.

#### NSS No Longer Support RSA Keys Shorter Than 1023 Bits

Network Security Services (NSS) libraries are updated to change the minimum key size for
all RSA operations from 128 to 1023 bits. The following NSS functions are no longer
available:

- Generating RSA keys shorter than 1023 bits.
- Signing or verifying RSA signatures with RSA keys shorter than 1023 bits.
- Encrypting or decrypting values with RSA key shorter than 1023 bits.

#### libssh Supports Smart Cards

Smart cards are supported through Public-Key Cryptography Standard (PKCS) #11 Uniform
Resource Identifier (URI). Therefore, you can use smart cards with the
`libssh` SSH library and with applications that use
`libssh`.

#### libssh Updated to 0.10.4

The `libssh` library is updated to version 0.10.4 and includes the
following support:

- OpenSSL 3.0
- Smart cards has been added.
- Two new configuration options `IdentityAgent` and
  `ModuliFile` have been added.

With this update, OpenSSL versions previous to 1.0.1 are no longer supported. Further,
Digital Signature Algorithm (DSA) support is disabled, and both the SCP API,
`pubkey` and `privatekey` APIs have been deprecated.

#### Compatibility Between scap-security-guide Rules and RainerScript logs

Rules in `scap-security-guide` are now compatible with the RainerScript
syntax. Therefore, `scap-security-guide` rules can check and remediate
ownership, group ownership, and permissions of Rsyslog log files in both available syntaxes.

#### Keylime Updated to 6.5.2

This version contains various enhancements and bug fixes, most notably the following:

- Vulnerability reported in [CVE-2022-3500](https://nvd.nist.gov/vuln/detail/CVE-2022-3500) is addressed.
- The Keylime agent no longer fails IMA attestation in cases where race conditions exist
  between running scripts.
- Segmentation fault in the `/usr/share/keylime/create_mb_refstate` script
  is fixed.
- Registrar no longer fails during EK validation when the
  `require_ek_cert` option is enabled

#### opencryptoki Updated to 3.19.0

The updated package version provides notable features such as the following:

- Dual-function cryptographic functions
- New `C_SessionCancel` function cancels active session-based operations,
  as described in the PKCS #11 Cryptographic Token Interface Base Specification v3.0

### Networking

The following features, enhancements, and changes related to networking are introduced in
this Oracle Linux 9 release.

#### NetworkManager Updated to Version 1.42.2

The `NetworkManager` packages are updated to version 1.42.2. Notable
features and changes include:

- Ethernet bonds can be configured for source load balancing.
- NetworkManager can manage connections on the `loopback` device.
- IPv4 equal-cost multipath (ECMP) route management is included.
- `802.1ad` tagging in Virtual Local Area Networks (VLANs) connections is
  now possible.
- The `nmtui` application can be used with Wi-Fi WPA-Enterprise, Ethernet
  with 802.1X authentication, and MACsec connection profiles.
- NetworkManager is updated to reject DHCPv6 leases if all addresses fail IPv6 duplicate
  address detection (DAD).

For more information, see <https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/1.42.2/NEWS>.

#### ECMP Routing in NetworkManager Can Use Weights

NetworkManager can now be configured using a `weight` property when defining
IPv4 Equal-Cost MultiPath (ECMP) routes. You can configure multipath routing to load-balance
and stabilize network traffic. The `weight` property can have a value from 1
to 256. You must define multiple next-hop routes as single-hop routes that use the
`weight` property. If no `weight` property is set on a
route, the routes aren't merged into an ECMP route.

#### The balance-slb Bonding Mode Is Available in NetworkManager

The `balance-slb` bonding mode used to configure source load balancing is
available in NetworkManager. The `balance-slb` mode divides traffic on the
source ethernet address using
`xmit_hash_policy`=`vlan+srcmac`, and NetworkManager
automatically adds necessary `nftables` rules for traffic filtering.

#### Flexible DNS Configuration Across Multiple Networks in NetworkManager

The `[global-dns]` section in the
`/etc/Networkmanager/NetworkManager.conf` file can be configured without
specifying the `nameserver` value in the
`[global-dns-domain-*]` section. By avoiding `nameserver`
configuration you are able to configure DNS in the `/etc/resolv.conf` file
while still relying on the DNS servers provided by the network connection for actual DNS
resolution. This update makes it easier to configure DNS across multiple networks.

#### VLAN Protocol Can Be Specified in NetworkManager

`vlan` interface types can be configured with a `protocol`
property in NetworkManager to specify the VLAN protocol that controls the tag identified for
encapsulation. The property can be set to either `802.1Q` (default), or
`802.1ad`.

#### VLANs Can Be Configured on Unmanaged Interfaces in NetworkManager

NetworkManager can configure an unmanaged networking interface as a base interface when
configuring VLANs. The VLAN base interface remains intact unless changed explicitly by
NetworkManager.

#### loopback Interface Connections Can Be Configured In NetworkManager

NetworkManager can configure the `loopback` interface to provide additional
IP addresses, DNS configuration, routing that isn't bound to an interface and MTU
settings.

#### nmstate API Accepts IPv6 Link-Local Addresses for DNS Server Entries

The `nmstate` API is updated to accept IPv6 link-local addresses for DNS
server entries. Use the
`<link-local_address>``%<interface>` format, for
example:

```
dns-resolver:
  config:
    server:
    - fe80::deef:1%enp1s0
```

#### nmstate API Includes Default MTU Range Properties on All Interfaces

Default properties for the `min-mtu` and `max-mtu` values are
set on all interfaces, so that if the required MTU is out of range, `nmstate`
indicates the available MTU range.

#### firewalld Updated to Version 1.2

The `firewalld` package is updated to version 1.2. Notable features and
changes include:

- New services including Kodi JSON-RPC, EventServer, netdata, and IPFS.
- A fail-safe mode can be used to ensure that the system remains protected and that
  network communication continues if the `firewalld` service encounters an
  error when it's started. If errors are encountered in the user configuration or another
  startup issue causes the `firewalld` service to fail,
  `firewalld` falls back to failsafe defaults.
- Tab-completion updated in the CLI for some `firewalld` policy
  commands.

#### conntrack-tools Updated to Version 1.4.7

The `conntrack-tools` package is updated to version 1.4.7. Notable features
and changes include:

- A new `IPS_HW_OFFLOAD` flag, which specifies offloading of a
  `conntrack` entry to the hardware.
- New `clash_resolve` and `chaintoolong` statistical
  counters.
- Filtering of events by IP address family.
- The `conntrackd.conf` file accepts 'yes' or 'no' values, as synonyms of
  'on' and 'off'.
- A user space helper can be configured to automatically load upon daemon startup. Users
  don't have to manually run the `nfct add helper` commands.
- The `-o userspace` command option is removed and user space triggered
  events are always tagged.
- External inject problems are only logged as warnings.
- The conntrack ID is ignored when looking up cache entries to replace old stale
  entries.
- Parsing of IPv6 `M-SEARCH` requests in the `ssdp cthelper`
  module is fixed.
- The `nfct` library no longer requires lazy binding.
- Protocol value parsing is improved and has better detection of invalid values.

#### xdp-tools Updated to Version 1.3.1

The `xdp-tools` packages are updated to version 1.3.1. Notable features and
changes include:

- New utility commands:

  - `xdp-bench`: XDP benchmarking on the receive side.
  - `xdp-monitor`: XDP error and statistic monitoring using kernel trace
    points.
  - `xdp-trafficgen`: Generates and sends traffic through the XDP driver
    hook.
- New features in the `libxdp` library:

  - Reference counting is improved when attaching programs to `AF_XDP`
    socket, so that applications no longer have to manually detach XDP programs when using
    sockets.
  - New functions are added to the library:

    - `xdp_program__create()` for creating `xdp_program`
      objects
    - `xdp_program__clone()` for cloning an
      `xdp_program` reference
    - `xdp_program__test_run()` for running XDP programs through the
      `BPF_PROG_TEST_RUN` kernel API
    - The `xdp_multiprog__xdp_frags_support()`,
      `xdp_program__set_xdp_frags_support()`, and
      `xdp_program__xdp_frags_support()` functions are added for
      loading programs with XDP `frags`or multibuffer XDP.
  - When the `LIBXDP_BPFFS_AUTOMOUNT` environment variable is set, the
    `libxdp` library automatically mounts a `bpffs`
    virtual file system if none is found. A subset of the library features can now also
    function when no `bpffs` is mounted.

This version also changes the version number of the XDP dispatcher program that's loaded on
the network devices. You can't use a previous and a new version of `libxdp`
and `xdp-tools` at the same time. The `libxdp` 1.3 library
displays old versions of the dispatcher, but doesn't automatically upgrade them. Programs
that are loaded with `libxdp` 1.3 don't work with programs that are loaded
with a previous version of the library.

#### iproute Updated to Version 6.1.0

The `iproute` package is updated to version 6.1.0. Notable features and
changes include:

- The `vdpa` command includes the ability to read device statistics,
  For example, you can read the `virtqueue` data structure at index 1, by
  running:

  ```
  sudo vdpa dev vstats show vdpa-a qidx 1
  ```
- Updates to the corresponding manual pages

### Kernel and System Libraries

The following notable features, enhancements, and changes apply to the Red Hat Compatible
Kernel (RHCK) that's shipped with the current Oracle Linux 9 version.

#### BPF Functionality Updated to Version Upstream Linux 6.0

The Berkeley Packet Filter (BPF) functionality in Red Hat Compatible Kernel (RHCK) is
updated to upstream Linux 6.0. All BPF features that depend on the BPF Type Format (BTF) for
kernel modules are enabled, including the usage of BPF trampolines for tracing, the
availability of the Compile Once - Run Everywhere (CO-RE) principle, and several
networking-related features. Kernel modules also contain debugging information, which means
that you no longer need to install `debuginfo` packages to inspect running
modules. For more information on the complete list of BPF features available in the running
kernel, use the `bpftool feature` command.

#### tuna Command Is Updated for Better Command Line Argument Parsing

The `tuna` command now uses `argparse` to provide
better command line argument parsing and the CLI can now display a standardized menu of
commands and options. You can now perform the following tasks:

- Change the attributes of the application and kernel threads.
- Operate on interrupt requests (IRQs) by name or number.
- Operate on tasks or threads by using the process identifier.
- Specify CPUs and sets of CPUs with the CPU or the socket number.

You can also use the `tuna -h` command to print the command line arguments
and their corresponding options.

Note that this functionality also works with UEK.

### File Systems and Storage

The following features, enhancements, and changes related to file systems and storage are
introduced in this Oracle Linux 9 release.

#### nvme-cli Updated to Version 2.2.1

The `nvme-cli` packages are updated to version 2.2.1. Notable features and
changes include:

- A new `nvme show-topology` command to display the NVMe subsystem
  topology.
- The `uint128` data fields are displayed correctly.
- The `libnvme` dependency is updated to version 1.2.
- The `libuuid` dependency is dropped.

#### libnvme Updated to Version 1.2

The `libnvme` packages are updated to version 1.2. Dependency on the
`libuuid` library is dropped.

#### Improved Functionality of the lvreduce Command

The `lvreduce` command does not reduce the size of an active logical volume
(LV) unless the `lvreduce esizefs` option is enabled. In this manner, the
risk of file system damage resulting from a reduction in the size of the LV is
prevented.

New options are available to the command for better control of the file systems while the
logical volume is beng reduced.

### High Availability and Clusters

The following features, enhancements, and changes related to high availability are introduced
in this Oracle Linux 9 release.

#### Pacemaker Can Run the validate-all Action for Resource and Stonith Agents

Use the `validate-all --agent-validation` command option when creating or
updating a resource or a STONITH device to trigger additional validation to that performed
by `pcs` based on the agent's metadata.

### Dynamic Programming Languages, Web and Database Servers

The following features, enhancements, and changes related to programming languages, web
servers, and database servers are introduced in this Oracle Linux 9 release.

#### Python 3.11 Available

Python 3.11 is available in the package `python3.11`. An additional suite of
packages compatible with Python 3.11 are also available. Notable features and changes
include:

- Improved performance.
- The new `match` keyword (similar to `switch` in other
  languages) can be used for structural pattern matching.
- Improved error messages, for example, indicating unclosed parentheses or brackets.
  Precise error locations in tracebacks pointing to the expression that caused the error.
  Exact line numbers for debugging and other use cases.
- The ability to define context managers across multiple lines by enclosing the
  definitions in parentheses.
- Various new features related to type hints and the `typing` module, such
  as the new `X | Y` type union operator, variadic generics, and the new
  `Self` type.
- A new `tomllib` standard library module which can be used to parse
  TOML.
- An ability to raise and handle multiple unrelated exceptions simultaneously using
  Exception Groups and the new `except*` syntax.

#### Git Updated to Version 2.39.1

The `git` version control system is updated to version 2.39.1. Notable
features and changes include:

- The `git log` command includes a format placeholder for the `git
  describe` output: `git log --format=%(describe)`
- The `git commit` command includes the
  `--fixup<commit>` option so that you to fix the content of the
  commit without changing the log message. With this update, you can also use:

  - The `--fixup=amend:<commit>` option to change both the message
    and the content.
  - The `--fixup=reword:<commit>` option to update only the commit
    message.
- The `git clone` command includes the `--reject-shallow`
  option to disable cloning from a shallow repository.
- The `git branch` command includes the
  `--recurse-submodules` option.
- The `git merge-tree` command can be used to:

  - Test if two branches can merge.
  - Compute a tree that would result in the merge commit if the branches were
    merged.
- T `safe.bareRepository` configuration variable can filter out bare
  repositories.

#### git-lfs Updated to Version 3.2.0

The `Git Large File Storage (LFS)` extension is updated to version 3.2.0.
Notable features and changes include:

- `Git LFS` introduces a pure SSH-based transport protocol.
- `Git LFS` provides a merge driver.
- The `git lfs fsck` command checks that pointers are canonical and that
  expected LFS files have the correct format.
- NT LAN Manager (NTLM) authentication protocol is removed. Use Kerberos or Basic
  authentication instead.

#### nginx:1.22 Available as a Module Stream

The `nginx 1.22` web and proxy server is available as the
`nginx:1.22` module stream. New features and changes include:

- OpenSSL 3.0 integration and handling of the `SSL_sendfile()` function
  when using OpenSSL 3.0.
- Integration with the PCRE2 library.
- POP3 and IMAP pipelining in the `mail` proxy module. Additionally, the
  `Auth-SSL-Protocol` and `Auth-SSL-Cipher` header lines are
  passed to the mail proxy authentication server.

- Multiple new directives are available, including `ssl_conf_command` and
  `ssl_reject_handshake`.
- Variables can be used in multiple directives, including
  `proxy_cookie_flags`, `proxy_ssl_certificate`,
  `proxy_ssl_certificate_key`, `grpc_ssl_certificate`,
  `grpc_ssl_certificate_key`, `uwsgi_ssl_certificate`, and
  `uwsgi_ssl_certificate_key`.
- The `listen` directive in the stream module now can take a new
  `fastopen` parameter to use `TCP Fast Open` mode for
  listening sockets.
- A new `max_errors` directive is added to the `mail` proxy
  module.
- `nginx` always returns an error if:

  - The `CONNECT` method is used.
  - Both `Content-Length` and `Transfer-Encoding` headers
    are specified in the request.
  - The request header name contains spaces or control characters.
  - The `Host` request header line contains spaces or control
    characters.
- `nginx` blocks all HTTP/1.0 requests that include the
  `Transfer-Encoding` header.
- `nginx` establishes HTTP/2 connections using the Application Layer
  Protocol Negotiation (ALPN) and can no longer use the Next Protocol Negotiation (NPN)
  protocol.

#### mod\_security Updated to Version 2.9.6

The `mod_security` module for the Apache HTTP Server is updated to version
2.9.6. Notable features and changes include:

- Adjusted parser activation rules in the `modsecurity.conf-recommended`
  file.
- Improvements to HTTP multipart request parsing.
- A new `MULTIPART_PART_HEADERS` collection.
- Microsecond timestamp resolution is used in the formatted log timestamp.
- Geo Countries updated for missing entries

#### postgresql:15 Module Stream Added

PostgreSQL version 15 is made available as the `postgresql:15` module
stream. PostgreSQL 15 includes several new features and enhancements over version 13. See
<https://www.postgresql.org/docs/release/15.0/> for more information.

Module stream life cycle information is available in [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

#### nodejs:18 Version 18.14 Includes npm Version 9

The updated `Node.js 18.14` includes a SemVer major upgrade of
`npm` from version 8 to version 9. In this update, support for unscoped
authentication configurations is removed to improve security. This update might require
adjustments to the current `npm` configuration.

If you use unscoped authentication tokens, generate and supply registry-scoped tokens in
the `.npmrc` file. If the `.npmrc` file contains lines that
use `_auth`, for example, `///registry.npmjs.org/:_auth`,
replace these lines with `///registry.npmjs.org:_authToken=${NPM_TOKEN}`.
Then apply the scoped token that is generated.

#### New Tomcat Package Introduced

The current Oracle Linux release includes the Apache Tomcat server version 9. Tomcat is the
servlet container that is used in the official Reference Implementation for the Java Servlet
and JavaServer Pages technologies. Tomcat is developed in an open and participatory
environment and released under the Apache Software License version 2.0.

### Compilers and Development Tools

The following features, enhancements, and changes related to compilers and development tools
are introduced in this Oracle Linux 9 release.

#### Updated Compilers and Development Tools

The following system toolchain components are updated in Oracle Linux 9.2:

- GCC 11.3.1
- glibc 2.34
- binutils 2.35.2

The following performance tools and debuggers are updated in Oracle Linux 9.2:

- GDB 10.2
- Valgrind 3.19
- SystemTap 4.8
- Dyninst 12.1.0
- elfutils 0.188

The following performance monitoring tools are updated in Oracle Linux 9.2:

- PCP 6.0.1
- Grafana 9.0.9

The following compiler toolsets are updated in Oracle Linux 9.2:

- GCC Toolset 12
- LLVM Toolset 15.0.7
- Rust Toolset 1.66.1
- Go Toolset 1.19.6

#### Updated GCC Toolset 12

GCC Toolset 12 is a compiler toolset that provides recent versions of development tools.The
toolset is available as an Application Stream in the form of a Software Collection in the
`AppStream` repository. Notable features and changes include:

- Updated the GCC compiler to version 12.2.1.
- `annobin` is updated to version 11.08.

The following tools and versions are provided by GCC Toolset 12:

| Tool | Version |
| --- | --- |
| GCC | 12.2.1 |
| GDB | 11.2 |
| binutils | 2.38 |
| dwz | 0.14 |
| annobin | 11.08 |

To install GCC Toolset 12, run the following command as root:

```
sudo dnf install gcc-toolset-12
```

To run a tool from GCC Toolset 12:

```
scl enable gcc-toolset-12 tool
```

To run a shell session where tool versions from GCC Toolset 12 override system versions of
these tools:

```
scl enable gcc-toolset-12 bash
```

#### LLVM Toolset Updated to Version 15.0.7

LLVM Toolset is updated to version 15.0.7.The update includes changes that enable the
`-Wimplicit-function-declaration` and `-Wimplicit-int`
warnings by default in C99 and later.

#### Go Toolset Updated to Version 1.19.6

Go Toolset is updated to version 1.19.6 to include several notable security and bug fixes.

#### System GCC Compiler Is Updated

The system GCC compiler, version 11.3.1, is updated to include numerous bug fixes and
enhancements available in the upstream GCC. The GNU Compiler Collection (GCC) provides tools
for developing applications with the C, C++, and Fortran programming languages.

#### Performance Co-Pilot Updated to Version 6.0

Performance Co-Pilot (`PCP`) is updated to version 6.0. Notable improvements
include:

1. Version 3 PCP archive:

   Instance domain change-deltas, Y2038-safe timestamps, nanosecond-precision timestamps,
   arbitrary timezones, and 64-bit file offsets used throughout for larger (beyond 2GB)
   individual volumes can all be used by configuring the
   `PCP_ARCHIVE_VERSION` setting in the `/etc/pcp.conf`
   file.

   Version 2 archives remain the default.
2. Only OpenSSL is used throughout PCP. Mozilla NSS/NSPR use is dropped:

   `libpcp`, `PMAPI` clients and `PMCD` use
   of encryption is impacted. These elements are now configured and used consistently with
   `pmproxy` HTTPS support and `redis-server`, which were
   both already using OpenSSL.
3. New nanosecond precision timestamp `PMAPI` calls for
   `PCP` library interfaces that use timestamps are included for optional
   use, but full backward compatibility is preserved for existing tools.
4. The following tools and services are updated:

   `pcp2elasticsearch`
   :   Authentication feature enabled.

   `pcp-dstat`
   :   Can use `top-alike` plugins.

   `pcp-htop`
   :   Updated to the latest stable upstream release.

   `pmseries`
   :   Added `sum`, `avg`, `stdev`,
       `nth_percentile`, `max_inst`,
       `max_sample`, `min_inst` and
       `min_sample` functions.

   `pmdabpf`
   :   Added CO-RE (Compile Once - Run Everywhere) modules.

   `pmdabpftrace`
   :   Moved example autostart scripts to the `/usr/share` directory.

   `pmdadenki`
   :   Multiple active batteries can be used.

   `pmdalinux`
   :   Updates for the latest `/proc/net/netstat` changes.

   `pmdaopenvswitch`
   :   Added additional interface and coverage statistics.

   `pmproxy`
   :   Request parameters can now be sent in the request body.

   `pmieconf`
   :   Added several `pmie` rules for Open vSwitch metrics.

   `pmlogger_farm`
   :   Added a default configuration file for farm loggers.

   `pmlogger_daily_report`
   :   Code changes for efficiency.

#### grafana Updated to Version 9.0.9

The `grafana` package is updated to version 9.0.9. Notable features and
changes include:

- The time series panel is now the default visualization option, replacing the graph
  panel
- New heatmap panel
- New Prometheus and Loki query builder
- Updated Grafana Alerting
- UI/UX and performance improvements
- License changed from Apache 2.0 to GNU Affero General Public License (AGPL)

The following are offered as opt-in experimental features:

- New bar chart panel
- New state timeline panel
- New status history panel
- New histogram panel

#### grafana-pcp Updated to Version 5.1.1

The `grafana-pcp` package is updated to version 5.1.1. Notable features and
changes include:

- Added buttons to disable rate conversation and time usage conversation in the query
  editor.
- Removed the deprecated `label_values(metric, label)` function for
  Redis.
- Fixed the network error for metrics with many series (requires Performance Co-Pilot
  v6+).
- Set the `pmproxy` API timeout to 1 minute.

#### tzdata Package Includes the leap-seconds.list File

The `/usr/share/zoneinfo/leap-seconds.list` file accommodates an alternate
format to the `/usr/share/zoneinfo/leapseconds` file that was previously
shipped with the `tzdata` package. Both formats are included to support
applications that choose to use either format to calculate International Atomic Time (TAI)
from Coordinated Universal Time (UTC) values that are used by almost all time services.

### Virtualization

The following features, enhancements, and changes related to virtualization are introduced in
this Oracle Linux 9 release.

#### passt Package Introduced

The package enables you to configure `passt` and `pasta`
network connections for virtual machines and containers, respectively, that are running in
the non privileged connection mode of `libvirt`
(`qemu:///session`). The two functionalities further offer the following
improvements for IPv6:

- Use of the Neighbor Discvoery Protocol (NDP) responder and for DHCPv6
- Port forwarding on TCP and UDP protocols on IPv6

This update adds the `passt` package, which makes it possible to use the
`passt` and `pasta` network connections. As a result, you
can set up `passt` and `pasta` for virtual machines and
containers, respectively, that run in the non-privileged connection mode of
`libvirt` (`qemu:///session`).

For more information on using `passt`, see the [libvirt upstream documentation](https://libvirt.org/formatdomain.html#userspace-slirp-or-passt-connection).

To use `pasta` in a podman container, use `-network pasta`
command-line option.

### Containers

The following features, enhancements, and changes related to containers are introduced in
this Oracle Linux 9 release.

#### Multiple GPG Keys for Podman Images

The `/etc/containers/policy.json` file accepts a `keyPaths`
field that contains a list of trusted GPG keys. Usage of more than one GPG key in the
container policy is a technology preview feature that permits Podman to install images
signed by any one of multiple GPG keys.

#### Updated container-tools Package and Podman

The `container-tools` package is updated for Podman v4.4. The package
contains the Podman, Buildah, Skopeo, `crun` and `runc` tools.
The updates have the following features and changes:

- Information about a container can be audited directly from a `journald`
  entry in Podman v4.4 and later. To enable Podman auditing, modify the
  `container.conf` configuration file and add the
  `events_container_create_inspect_data=true` option to the
  `[engine]` section. The audit data is in JSON format, equivalent to the
  output of the `podman container inspect` command.
- The `podman network update` command is added to update networks for
  containers and pods.
- Podman can be configured with pre-execution hooks that can be used to control container
  operations by creating plugin scripts in
  `/usr/libexec/podman/pre-exec-hooks` or
  `/etc/containers/pre-exec-hooks`. Pre-execution scripts are only run if
  a file named `/etc/containers/podman_preexec_hooks.txt` exists. If all
  plugin scripts return zero value, then the `podman` command is run,
  otherwise, the `podman` command exits with the exit code returned by the
  script that failed.
- The `podman buildx version` command is added to output the Buildah
  version.
- Container startup health checks are available, to trigger a command to check that the
  container is fully started before the regular health check is activated.
- New Docker compatibility options and aliases are included.
- Improved Kubernetes integration by consolidating `kube` commands:
  the `podman kube generate` and `podman kube
  play` replace the `podman generate kube` and `podman
  play kube` commands.
- Systemd-managed pods created by the `podman kube play` command
  now integrate with sd-notify, using the `io.containers.sdnotify`
  annotation (or `io.containers.sdnotify/$name` for specific
  containers).
- Systemd-managed pods created by `podman kube play` can be auto-updated by
  using the `io.containers.auto-update` annotation.

For further information about notable changes, see [upstream release notes](https://github.com/containers/podman/blob/main/RELEASE_NOTES.md#440).

#### Custom DNS Server Selection Is Available for Aardvark and Netavark

Custom DNS server selection for containers using the Aardvark and Netavark network stack is
available. Containers are able to use customer DNS servers instead of the default DNS
servers on the host. To enable a custom DNS server, either add the
`dns_servers` field in the `containers.conf` configuration
file or use the new `--dns` option to specify the IP address of the DNS
server when running the `podman` command. The `--dns`
option overrides any values that are set in the `container.conf` file.

#### Generate Sigstore Key Pairs With Skopeo

Skopeo can generate sigstore key pairs through the `skopeo
generate-sigstore-key` command. For more information, see
`skopeo-generate-sigstore-key` manual page.

#### Toolbox Utility Is Available

Use the `toolbox` utility to access the container command line
environment without installing additional troubleshooting tools directly on the system.
Toolbox uses Podman and other standard container technologies from the Open Container
Initiative. For more information, see [toolbx](https://containertoolbx.org/).

#### Container Images Now Have a Two-Digit Tag

In Oracle Linux 9.0 and Oracle Linux 9.1, container images had a three-digit tag. Starting
from Oracle Linux 9.2, container images have a two-digit tag.

### Support

The following features, enhancements, and changes related to support are introduced in this
Oracle Linux 9 release.

#### sos clean Command Obfuscates IPv6 Addresses

`sos clean` detects and obfuscates IPv6 addresses to ensure that
customer-sensitive data is appropriately obfuscated.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.2/ol9-TechnologyPreview.html -->

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

### Graphics

The following graphics features are available as technology previews in Oracle Linux.

#### Intel® Arc A-Series Graphics

Intel® Arc A-Series graphics, also known as Alchemist or DG2, are available as a
technology preview.

Add the following option to the kernel command line to enable hardware acceleration with
Intel® Arc A-Series graphics:

```
i915.force_probe=pci-id
```

In this option, replace `pci-id` with the PCI ID of the Intel®
GPU.

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

#### Intel® Trust Domain Extensions Available for Oracle VM Guests

Intel® Trust Domain Extension (TDX) can be used with Oracle Linux guest VMs. TDX protects
confidential guest VMs by isolating the guest register state and encrypting the guest
memory.

Note:

Using TDX can cause `kdump` to fail on the VM.

### File Systems and Storage

The following features that are related to file systems and storage are available as
technology preview.

#### Stratis

A local storage manager, Stratis manages file systems on top of pools of storage and
provides features such as the following:

- Manage snapshots and thin provisioning
- Automatically grow file system sizes as needed
- Maintain file systems

You administer Stratis storage through the `stratis` utility, which
communicates with the `stratisd` background service.

#### NVMe 8006 in-Band Authentication

Non-Volatile Memory Express (NVMe) TP 8006, which is an in-band authentication for NVMe
over Fabrics (NVMe-oF), is available as for technology preview. The NVMe Technical
Proposal 8006 defines the `DH-HMAC-CHAP` in-band authentication protocol
for NVMe-oF. For more information, see the `dhchap-secret` and
`dhchap-ctrl-secret` option descriptions in the
`nvme-connect(1)` manual page.

in-Band Authentication is fully available in UEK R7U2.

#### `nvme-stas` Package

The `nvme-stas` package, which is a Central Discovery Controller (CDC)
client for Linux, handles the following functionalities:

- Asynchronous Event Notifications (AEN)
- Automated NVMe subsystem connection controls
- Error handling and reporting
- Automatic (`zeroconf`) and Manual configuration.

This package consists of two daemons, Storage Appliance Finder (`stafd`)
and Storage Appliance Connector (`stacd`).

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

### Infrastructure Services

The following features for infrastructure services are available as technology previews.

#### Socket API for TuneD

The socket API for TuneD maps one-to-one with the D-Bus API and provides an alternative
communication method for cases where D-Bus isn't available. With the socket API, you can
control the TuneD daemon to optimize the performance, and change the values of various tuning
parameters. The socket API is disabled by default. You can enable it in the
`tuned-main.conf` file.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.2/ol9-DeprecatedFeatures.html -->

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


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.2/ol9-KnownIssues.html -->

## 5 Known Issues

This
chapter describes known issues that you may encounter when installing and using the Oracle
Linux 9 software. Unless indicated otherwise, the issues apply to both x86\_64 and aarch64
systems. Information that pertains only to a specific platform is also noted accordingly.

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

### Systems With Btrfs Fail to Boot in FIPS Mode

When booted in FIPS mode, a system using Btrfs fails with the following message:

```
FATAL: FIPS integrity test failed
Refusing to continue
```

(Bug ID 36028061)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/9/relnotes9.2/ol-PackageChangesfromtheUpstreamRelease.html -->

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
- `libnetapi`
- `libnsl`
- `libquadmath`
- `libreport-filesystem`
- `libsmbclient`
- `libsss_autofs`
- `libsss_certmap`
- `libsss_idmap`
- `libsss_nss_idmap`
- `libsss_simpleifp`
- `libsss_sudo`
- `libstdc++`
- `libwbclient`
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
- `python3-requests`
- `python3-rpm`
- `python3-samba`
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
- `samba`
- `samba-client-libs`
- `samba-common`
- `samba-common-libs`
- `samba-common-tools`
- `samba-dcerpc`
- `samba-dc-libs`
- `samba-ldb-ldap-modules`
- `samba-libs`
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
- `catatonit`
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
- `eth-tools-basic`
- `eth-tools-fastfabric`
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
- `python3-libreport`
- `python3-net-snmp`
- `python3-numpy`
- `python3-numpy-f2py`
- `python3-packaging`
- `python3-pcp`
- `python3-psutil`
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
- `vim-common`
- `vim-enhanced`
- `vim-X11`
- `virt-p2v`
- `virt-top`
- `virt-v2v`
- `virt-v2v-bash-completion`
- `WALinuxAgent`
- `WALinuxAgent-udev`
- `wireplumber`
- `wireplumber-libs`
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
- `python-requests`
- `python-six`
- `python-urllib3`
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
- `eth-tools`
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
- `osinfo-db`
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
- `python-requests`
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
- `vim`
- `virt-p2v`
- `virt-top`
- `virt-v2v`
- `WALinuxAgent`
- `wireplumber`
- `xsane`

#### Modified Source Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `anaconda`
- `catatonit`
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