---
title: "Release Notes for Oracle Linux 8.9"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.9"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol8"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

Release Notes for Oracle Linux 8.9

F87399-03

December 2023

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 8 Release Notes for Oracle Linux 8.9

F87399-03

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2023, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.9/ol8.9-Preface.html -->

[Oracle Linux 8: Release Notes for Oracle Linux
8.9](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.9/) provides information about the new features and known issues in the Oracle
Linux 8.9 release. The information applies to both x86\_64 and 64-bit Arm (aarch64)
architectures. This document might be updated after first publication.

### Documentation License

The content in this document is licensed under the [Creative Commons Attribution–Share Alike 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.

### Conventions

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| boldface | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| italic | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |

### Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility
Program website at <https://www.oracle.com/corporate/accessibility/>.

For information about the accessibility of the Oracle Help Center, see the Oracle
Accessibility Conformance Report at <https://www.oracle.com/corporate/accessibility/templates/t2-11535.html>.

### Access to Oracle Support for Accessibility

Oracle customers that have purchased support have access to electronic support through My
Oracle Support. For information, visit <https://www.oracle.com/corporate/accessibility/learning-support.html#support-tab>.

### Diversity and Inclusion

Oracle is fully committed to diversity and inclusion. Oracle respects and values having a
diverse workforce that increases thought leadership and innovation. As part of our
initiative to build a more inclusive culture that positively impacts our employees,
customers, and partners, we are working to remove insensitive terms from our products and
documentation. We are also mindful of the necessity to maintain compatibility with our
customers' existing technologies and the need to ensure continuity of service as Oracle's
offerings and industry standards evolve. Because of these technical constraints, our effort
to remove insensitive terms is ongoing and will take time and external cooperation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.9/ol8-AboutOracleLinux8.html -->

The current Oracle Linux 8 release contains
new features and enhancements that improve performance in different areas including automation
and management, security, and compliance, container management, and developer tools. These
enhancements are especially designed to make the OS adaptable to different types of deployment
such as on-premises installations, hybrid deployments that combine on-premises and cloud
installations, and full cloud deployment.

Important:

Upgrading from an Oracle Linux Developer Preview release to its later official version
isn't supported. If you're running the Developer Preview version, you must reinstall the
official Oracle Linux release upon its general availability.

### System Requirements and Limitations

To check whether a specific hardware can be used with the current Oracle Linux 8 release,
see the Hardware Certification List at <https://linux.oracle.com/hardware-certifications>. Note that as hardware becomes
available and validated, the hardware is added to the list.

Oracle Linux 8 for the aarch64 platform is primarily engineered for use with Ampereâ¢ eMAGâ¢-based EVK platform and the Marvell ThunderX2® processor.
Other hardware might be supported and added to the Hardware Certification List in the
future.

CPU, memory, disk, and file system limits for all Oracle Linux releases are described in
[Oracle Linux: Limits](https://docs.oracle.com/en/operating-systems/oracle-linux/limits/).

### Available Architectures

The release is available on the following platforms:

- Intel® 64-bit (x86\_64)
- AMD 64-bit (x86\_64)
- Arm 64-bit (aarch64)

The Arm platform runs only with Unbreakable Enterprise Kernel Release (UEK).

### Shipped Kernels

On the x86\_64 platform, the current Oracle Linux 8 release ships with the following default
kernel packages:

- `4.18.0-513.5.1` (Red Hat Compatible Kernel (RHCK))
- `5.15.0-200.131.27` (Unbreakable Enterprise Kernel Release 7 Update
  2 (UEK R7U2))

  For new installations, the UEK R7 is automatically enabled and installed. It also
  becomes the default kernel on first boot.

  On the aarch64 platform, Oracle Linux ships with the UEK kernel only.

  Important:

  If you're upgrading from a previous Oracle Linux 8 version, the kernel isn't
  automatically upgraded to UEK R7.

The Oracle Linux release is tested as a bundle, as shipped on the installation media image.
When installed from the installation media image, the kernel's version included in the image
is the minimum version that's supported. Downgrading kernel packages is unsupported, unless
recommended by Oracle Support.

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
continue to run unmodified on UEK R6 and UEK R7, with no required recertifications for RHEL
certified applications.

### Obtaining Installation Images

The following installation images for the current Oracle Linux 8 release are available:

- Full ISO of Oracle Linux for typical installations on premises.
- Boot ISO of Oracle Linux for network installations
- Boot ISO of the official UEK release for installing on hardware which is supported only
  on UEK
- Source DVDs

You can download these images from the following locations. Note
that the images in these locations are for both the x86\_64 and
aarch64 platforms, unless indicated otherwise:

- Oracle Software Delivery Cloud at <https://edelivery.oracle.com>
- Oracle Linux yum server at <https://yum.oracle.com/oracle-linux-downloads.html>

To prepare a downloaded image for installing Oracle Linux, see [Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/).

For information about the available ISO images for the three most recent updates to the Oracle
Linux releases, see <https://yum.oracle.com/oracle-linux-isos.html>.

For developers who use the Raspberry Pi hardware platform, Oracle provides an unsupported
developer release image, which includes the required firmware to boot this platform. For more
information about using the Raspberry Pi hardware platform, see [Install Oracle Linux on a Raspberry Pi](https://docs.oracle.com/en/learn/oracle-linux-install-rpi/).

Note:

Aside from installation ISO images, you can also use Oracle Linux images to create compute
instances on Oracle Cloud Infrastructure. For information about these images, see
the release notes for the specific image that you're using on the [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/images/) page.

To use Oracle Linux on Oracle Cloud Infrastructure, see <https://docs.oracle.com/iaas/oracle-linux/home.htm>.

### Upgrading From Oracle Linux 7 to Oracle Linux 8

You can upgrade an Oracle Linux 7 system to the latest Oracle Linux 8 release by using the
`leapp` utility. For step-by-step instructions and information about
any known issues that might arise when upgrading the system, see [Oracle Linux 8: Upgrading Systems With Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/8/leapp/).

### Installing Oracle-Supported RDMA Packages

Oracle Linux 8 releases earlier than Oracle Linux 8.7 ship with UEK R6 as the default
kernel.

Starting with Oracle Linux 8.5, you also have the option of installing UEK R7. From Oracle
Linux 8.7 onward, UEK R7 is the default kernel.

Oracle provides Remote Direct Memory Access (RDMA) packages for use with UEK R6 and UEK R7.
The RDMA feature provides direct memory access between two systems that are connected by a
network. RDMA improves high-throughput and low-latency networking in clusters.

To use RDMA features, you must first install the Oracle-supported RDMA packages. To do so,
ensure that the system is subscribed to the appropriate channels on ULN or that you have
enabled the appropriate repositories on the Oracle Linux yum server.

For more information about RDMA, including any known issues, see [Unbreakable Enterprise Kernel documentation](https://docs.oracle.com/en/operating-systems/uek/) for the required kernel.

RDMA With UEK R6

If you're subscribed to ULN, enable the following channels:

- `ol8_x86_64_UEKR6`
- `ol8_x86_64_baseos_latest`
- `ol8_x86_64_appstream`
- `ol8_x86_64_UEKR6_RDMA`

Note that if the system is newly registered on ULN, then the system is already subscribed
to the `ol8_x86_64_UEKR6`, `ol8_x86_64_baseos_latest`, and
`ol8_x86_64_appstream` channels by default. However, you must explicitly
subscribe to the `ol8_x86_64_UEKR6_RDMA` channel before installing RDMA
packages.

If you're using the Oracle Linux yum server, enable the following repositories:

- `ol8_UEKR6`
- `ol8_baseos_latest`
- `ol8_appstream`
- `ol8_UEKR6_RDMA`

Note that if the system already uses the Oracle Linux yum server, the
`ol8_UEKR6`, `ol8_baseos_latest`, and
`ol8_appstream` repositories are enabled by default. However, you must
explicitly enable the `ol8_UEKR6_RDMA` repository before installing RDMA
packages.

RDMA With UEK R7

If you're subscribed to ULN, enable the following channels:

- `ol8_x86_64_UEKR7`
- `ol8_x86_64_baseos_latest`
- `ol8_x86_64_appstream`
- `ol8_x86_64_UEKR7_RDMA`

Note that if the system is newly registered on ULN, then the system is already subscribed
to the `ol8_x86_64_UEKR6`, `ol8_x86_64_baseos_latest`, and
`ol8_x86_64_appstream` channels by default. Disable
`ol8_x86_64_UEKR6` and then explicitly subscribe to the
`ol8_x86_64_UEKR7_RDMA` and `ol8_x86_64_UEKR7_RDMA` channels
before installing RDMA packages.

If you're using the Oracle Linux yum server, enable the following repositories:

- `ol8_UEKR7`
- `ol8_baseos_latest`
- `ol8_appstream`
- `ol8_UEKR7_RDMA`

Note that if the system already uses the Oracle Linux yum server, the
`ol8_UEKR6`, `ol8_baseos_latest`, and
`ol8_appstream` repositories are enabled by default. Disable
`ol8_UEKR6` and then explicitly subscribe to the
`ol8_UEKR7_RDMA` and `ol8_UEKR7_RDMA` repositories before
installing RDMA packages.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.9/ol8-NewFeaturesandChanges.html -->

This chapter describes the new features, major enhancements, bug fixes, and other changes
that are included in this release of Oracle Linux 8.

### Cloud Environment

The following features, enhancements, and changes related to the cloud environment are
introduced in this Oracle Linux 8 release.

#### `cloud-init` Integration With NetworkManager

The `cloud-init` tool can use a `network-manager`
keyfile to configure the network by using NetworkManager instead of the default
`sysconfig` method for network setup.

To use NetworkManager as the primary network renderer, edit
`/etc/cloud/cloud.cfg` and set
`network-manager` as the first entry in the list:

```
network:
    renderers: ['network-manager', 'eni', 'netplan', 'sysconfig', 'networkd']
```

### Containers

The following features, enhancements, and changes related to containers are introduced in
this Oracle Linux 8 release.

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
  from the container description. See [Quadlet in Podman Available](ol8-NewFeaturesandChanges.html#ol8.9-featuresContainers_quadlet_in_podman_available).

#### Quadlet in Podman Available

Quadlet is available beginning with Podman 4.6. Quadlets can be used to automatically
generate a `systemd` service file from the container description. The
container description is in the `systemd` unit file format and simplifies
much of the technical complexity of running containers under `systemd`.
Quadlet formatted descriptions might be easier to write and maintain than
`systemd` unit files.

Note:

Quadlets don't work on Oracle Linux 8 in rootless
mode.

For more details, see the [Quadlet upstream documentation](https://github.com/containers/quadlet).

### Compilers and Development Tools

The following features, enhancements, and changes related to compilers and development tools
are introduced in this Oracle Linux 8 release.

#### Updated Compilers and Development Tools

The following performance tools and debuggers are updated:

- Valgrind 3.21.0
- SystemTap 4.9
- elfutils 0.189

The following performance monitoring tools are updated:

- libpfm 4.13

The following compiler toolsets are updated :

- GCC Toolset 13
- LLVM Toolset 16.0.6
- Rust Toolset 1.71.1

  With this update, the Rust `profile_builtins` runtime component is now
  available.
- Go Toolset 1.20.10

#### GCC Toolset 13

GCC Toolset 13 is a compiler toolset that provides recent versions of development
tools. The toolset is available as an Application Stream in the form of a Software
Collection in the `AppStream` repository.

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
scl enable gcc-toolset-13 tool
```

To run a shell session where tool versions from GCC Toolset 13 override system
versions of these tools, type:

```
scl enable gcc-toolset-13 bash
```

#### GCC Preserves Register Arguments

GCC is updated to preserve register argument content and generate proper Call Frame
Information (CFI) to make it easier for the unwinder to find this information
without negatively impacting performance.

#### `binutils` Updated to Version 2.40 in GCC Toolset 13

The GCC Toolset 13 includes version 2,40 of `binutils` which includes
the following notable changes:

- Added a `-w` (`--no-warnings`) option for the
  linker to disable warning messages.
- Improved warning messages in the ELF linker for notifications around
  permissions changes.
- Added a `--private` option in the `objdump` tool
  that shows the fields in the file header and section headers for Portable
  Executable (PE) format files.
- Added a `--show-all-symbols` option for the
  `objdump` tool to show all symbols matching an address when
  disassembling.
- Added a `--strip-section-headers` option for the
  `objcopy` and `strip` tools to remove the ELF
  section header from ELF files.
- Added a `-W` (`--no-weak`) option to the
  `nm` tool to set it to ignore weak symbols.
- Added syntax highlighting for disassembler output in the
  `objdump` tool.

#### `glibc` Performance Enhancement for Intel Xeon V5 Hardware

The default amount of cache used by `glibc` for string and memory
routines is tuned to improve performance on Intel Xeon v5 hardware.

#### Backward Incompatibility From C++ Code Changes

Changes were applied to C++ to improve startup performance of C++ programs. For example,
global iostream objects such as `std::cout`, `std::cin` are
constructed inside the standard library rather than in source files that include the
`<iostream>` header. However, the consequence is that code compiled
with the GCC 13.1 toolset would fail if the incorrect `libstdc++.so` version
is used at runtime. For more information about using the correct
`libstdc++.so` at runtime, see <https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dynamic_or_shared.html#manual.intro.using.linkage.dynamic>.

### Dynamic Programming Languages, Web and Database Servers

The following features, enhancements, and changes related to programming languages, web
servers, and database servers are introduced in this Oracle Linux 8 release.

#### `nodejs:20` Module Stream Support

The `nodejs:20` module stream is supported and includes `Node.js
20.9`, which is a Long Term Support (LTS) version. The following notable features
are included:

- The `V8` JavaScript engine is updated to version 11.3.
- The `npm` package manager is updated to version 9.8.0.
- `Node.js` includes the experimental Permission Model.
- `Node.js` includes the experimental Single Executable Application (SEA)
  feature.
- `Node.js` includes improvements to the Experimental ECMAScript modules
  (ESM) loader.
- The `node:test` module is now considered stable.

To install the `nodejs:20` module stream, run:

```
sudo dnf module install nodejs:20
```

For information about the length of support for Application Streams, see [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

#### Python `tarfile` Extraction Functions Include a `filter` Argument

Python now includes a `filter` argument to `tarfile`
extraction functions to disable some features of `tar` to enhance security.
If a filter isn't specified, the `'data'` filter, which is the safest but
most limited, is used by default.

#### `HTTP::Tiny` Perl Module Updated to Perform TLS Verification By Default

The `HTTP::Tiny` Perl module is updated to perform TLS certificate
verification by default when using HTTPS. The update adds the following dependencies to
the `perl-HTTP-Tiny` package:

- `perl-IO-Socket-SSL`
- `perl-Mozilla-CA`
- `perl-Net-SSLeay`

The `verify_SSL` option is changed from `0` to
`1` when the package is installed.

### High Availability and Clusters

The following features, enhancements, and changes related to high availability are introduced
in this Oracle Linux 8 release.

#### Improvements to Pacemaker Scheduler for Colocation Constraint Handling

The Pacemaker scheduler is updated and improved to prioritize mandatory colocation
constraints, including those between group members, over optional colocation constraints. This
change improves how the scheduler works with resources that have a heterogeneous mix of
colocation constraints. Note that this feature requires at least three nodes.

#### `alert_snmp.sh.sample` Alert Agent Works With SNMPv3

The `alert_snmp.sh.sample` alert agent now works with SNMPv2 and SNMPv3 without
any requirement to modify the agent.

#### New Meta Option to Disable Alerts

You can configure a Boolean value for the `enabled` meta option to control
whether Pacemaker generates alerts for a recipient, by setting the value to either
`true` or `false`. The default value is set to
`true`.

#### Enhancements to the `pcs property` Command

The `pcs property` command now supports the following enhancements:

- The `pcs property config --output-format=` option

  - Specify `--output-format=cmd` to display the `pcs property
    set` command created from the current cluster properties configuration. You
    can use this command to re-create configured cluster properties on a different
    system.
  - Specify `--output-format=json` to display the configured cluster
    properties in JSON format.
  - Specify `output-format=text` to display the configured cluster
    properties in plain text format, which is the default value for this option.
- The `pcs property defaults` command, which replaces the deprecated
  `pcs property --defaults` option
- The `pcs property describe` command, which describes the meaning of
  cluster properties.

### Infrastructure Services

The following features, enhancements, and changes related to infrastructure services are
introduced in this Oracle Linux 8 release.

#### Postfix Can Handle SRV Lookups

DNS service records resolution (SRV) entries can be used by Postfix to automatically
configure mail clients and balance server load. Furthermore, Postfix can handle temporary
DNS issues and provides configurable options for fault-resilience in case of SRV record
failures. You can configure SRV handling for Postfix by setting the following options in the
Postfix server configuration:

- `use_srv_lookup=smtp`

  Enables discovery of the specified
  service by using DNS SRV records.
- `allow_srv_lookup_fallback=yes`

  Configures the service for SRV
  lookup fallback, so that Postfix falls back to using MX and IP address records in the
  case where an SRV entry lookup fails either because of misconfiguration or a missing
  entry, but continues to use SRV for the service.
- `ignore_srv_lookup_error=yes`

  Configures the service to stop
  using SRV when a lookup fails, and to switch to using MX or IP address records
  instead.

#### TLS 1.3 Cipher Suites Can Be Used in `vsftpd`

The `ssl_ciphersuites` option can be used when configuring
`vsftpd` to configure the service to use different cipher suites, including
TLS 1.3 cipher suites that weren't available in the service before. Cipher suite entries are
specified on a single line separated using the colon (:) character.

### Kernel and System Libraries

The following notable features, enhancements, and changes apply to the Red Hat Compatible
Kernel (RHCK) that's shipped with the current Oracle Linux 8 version.

#### RHCK Can Handle AutoIBRS Configurations on AMD Processors

RHCK can handle Automatic Indirect Branch Restricted Speculation (AutoIBRS)
configurations on AMD processors. AutoIBRS is a feature provided by the AMD EPYC
9004 Genoa family of processors and later CPU versions. AutoIBRS is the default
mitigation used for the Spectre v2 CPU to reduce vulnerabilities, boost performance,
and improve scalability.

#### Updated Intel® QAT Kernel Driver

The Intel® Quick Assist Technology (QAT), as of version 6.2, includes both bug fixes
and enhancements. The most notable enhancement includes added functionality for the
following QAT GEN4 hardware accelerator devices:

- Intel Quick Assist Technology 401xx devices
- Intel Quick Assist Technology 402xx devices

#### `makedumpfile` Updated to Version 1.7.2

The `makedumpfile` utility is updated to version 1.7.2. This tool is
used to reduce the size of dump files by compression and by excluding pages.

### Networking

The following features, enhancements, and changes related to networking are introduced in
this Oracle Linux 8 release.

#### `nftables` Default Service Configuration Update

The default service configuration for `nftables` now includes the
`do_masquerade` chain to reduce the risk of a port shadow attack. The
update is applied to `/etc/sysconfig/nftables/nat.nft` to add a rule in
the `do_masquerade` chain that detects suitable packets and enforces source
port randomization.

#### `NetworkManager` Includes an Option to Suppress AAAA Queries

The `no-aaaa` option can be used to configure DNS settings to suppress AAAA
queries. By using this option, IPv6 DNS resolution can be disabled by using the
`nmcli` utility. After the `NetworkManager` service is
restarted, the `no-aaaa` setting is added to the
`/etc/resolv.conf` file.

#### `libnftnl` Package Version 1.2.2 Updates

The Netlink API to the in-kernel `nf_tables` subsystem
(`libnftnl`) package has been updated. Notable changes and enhancements
include:

- New features:

  - Nesting of the `udata` attribute
  - Resetting TCP options with the `exthdr` expression
  - Meta keywords: `sdif` and `sdifname`
  - Ability to handle a new attribute `NFTNL_CHAIN_FLAGS` in the
    `nftnl_chain` struct, to communicate flags between the kernel and
    user space.
  - New `nftnl_set` struct for nftables to add expressions to sets and
    set elements.
  - Comment abililty for sets, tables, objects, and chains
  - The `nftnl_table` struct includes an
    `NFTNL_TABLE_OWNER` attribute. Use this attribute to enable the
    kernel to communicate the owner to the user space.
  - Readiness for incremental updates to flowtable device
  - The `typeof` keyword related `nftnl_set udata`
    definitions
  - A `chain` ID attribute
  - Capability to remove expressions from a rule
  - Capability for a `last` expression
- Bitwise expressions enhancements:

  - New attributes: `op` and `data`
  - Left and right shifts
  - Debug output alignment of other expressions
- Socket expression enhancements:

  - New attribute: `wildcard`
  - Ability to handle cgroups v2
- Debug output enhancements:

  - `key_end` data register included in set elements
  - Removal of unused registers from `masq` and nat expressions
  - Fix applied to verdict map elements
  - Removed leftovers from dropped XML formatting
  - Payload offset of inner header

#### `iproute` Updated to Version 6.2.0

The `iproute` package is updated to version 6.2.0. Notable changes
include:

- New `ip stats` command to view and manage interface
  statistics. See the `ip-stats(8)` manual page for more
  information.
- New `--threads` option for the `ss` command
  to display thread information. See the `ss(8)` manual page for more
  information.
- New `bridge fdb flush` command to flush forwarding database
  entries. See the `bridge(8)` manual page for more information.

### Security

The following features, enhancements, and changes related to security are introduced in this
Oracle Linux 8 release.

#### FIPS-enabled In-place Upgrades of Oracle Linux 8.9 to Latest Oracle Linux 9

Beginning with Oracle Linux 8.9, you can perform in-place upgrades of FIPS-enabled Oracle
Linux 8 systems to Oracle Linux 9.2 and later. For more information, see [Oracle Linux 9: Upgrading Systems With
Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/9/leapp/).

#### SCAP Security Guide Updated ANSSI-BP-028 Security Profiles to Version 2.0

The Agence Nationale de la SÃ©curitÃ© des SystÃ¨mes d'Information (ANSSI) BP-028 profiles
in the SCAP security guide were updated to align with the version 2.0 guidelines
described at <https://cyber.gouv.fr/publications/recommandations-de-securite-relatives-un-systeme-gnulinux>.

#### SCAP Security Guide Rule Update for Consistent Interactive User Configuration

Several rules were updated in the SCAP security guide to provide more consistent
interactive user configuration. User accounts with UID greater than or equal to 1000 are
considered interactive, unless the account username is `nobody` or
`nfsnobody`, or the account login shell is set to
`/sbin/nologin`. With these updates, SCAP users are no longer
considered interactive users.

The following rules are updated for more consistent interactive user configuration :

- `accounts_umask_interactive_users`
- `accounts_user_dot_user_ownership`
- `accounts_user_dot_group_ownership`
- `accounts_user_dot_no_world_writable_programs`
- `accounts_user_interactive_home_directory_defined`
- `accounts_user_interactive_home_directory_exists`
- `accounts_users_home_files_groupownership`
- `accounts_users_home_files_ownership`
- `accounts_users_home_files_permissions`
- `file_groupownership_home_directories`
- `file_ownership_home_directories`
- `file_permissions_home_directories`
- `file_permissions_home_dirs`
- `no_forward_files`

#### OpenSCAP Updated to 1.3.8

The OpenSCAP packages are updated to version 1.3.8. Notable changes include:

- Fixes to `systemd` probes to not ignore some `systemd`
  units.
- Addition of offline capabilities to the `shadow` OVAL probe.
- Addition of offline capabilities to the `sysctl` OVAL probe.
- Addition of `auristorfs` to the list of network file systems.
- Improved handling of tailoring files generated by `autotailor`.

#### `opencryptoki` Updated to 3.21.0

The `opencryptoki` package is updated to version 3.21.0 and includes the
following notable changes:

- Concurrent hardware security module (HSM) master key updates
- Added a new `protected-key` option to transform a chosen key into a
  protected key
- Added several key types, including DH, DSA, AES-XTS, Kyber, Dilithium, and generic
  secret key types
- Added EP11 host library version 4
- `pkcsslotd` no longer runs as root
- New commands:

  - `p11sak set-key-attr`: to change key attributes
  - `p11sak copy-key`: to copy a key
  - `p11sak import-key`: to import a key
  - `p11sak export-key`: to export a key

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

This feature is available only in RHCK.

#### `fapolicyd` Includes Rule Numbers in Audit Output

Fapolicyd is updated along with kernel and Auditd components to include the rule number
when outputting to the audit log so that it's easier to troubleshoot policy related
issues.

This feature is available only in RHCK.

#### SCAP Security Guide Updated to Version 0.1.69

Updates to the SCAP Security Guide include the following notable changes:

- Password aging rules no longer ignore empty string as passwords.
- The remote OVAL content URL is updated to be more specific to Oracle Linux 8 to improve
  memory usage when scanning with `--fetch-remote-resources`.
- Rules related to `/var/log` and `/var/log/audit`
  are now only applicable if those partitions exist.
- Bash remediations are fixed to handle ISO9660 partitions in the fstab.
- The Oracle Linux 8 stig profile has been updated to comply with DISA Oracle Linux 8 STIG
  - Ver 1, Rel 8.

### Support

The following features, enhancements, and changes related to support are introduced in this
Oracle Linux 8 release.

#### `sos` Updated to Version 4.6

The `sos` utility that's used to collect configuration, diagnostic, and
troubleshooting data, is updated to version 4.6 to provide the following notable
changes:

- The contents of the `/boot/grub2/custom.cfg` and
  `/boot/grub2/user.cfg` files are included in reports to help with
  troubleshooting boot issues.
- `sos` removes the `bindpw` option when used with the
  `sudo` plugin.
- Various improvements to remove and mask username and password information for
  plugins
- `sos` completes the tailed log collection even when the size of the log
  file is exceeded and when a plugin times out
- `sos` collects the sos report from the same cluster node as where it's
  run, when running on a Pacemaker cluster node
- The `sos report --clean` command obfuscates all MAC addresses.

For details on each release of `sos`, see [upstream
release notes](https://github.com/sosreport/sos/releases).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.9/ol8-TechnologyPreview.html -->

For the Red Hat Compatible Kernel in the current Oracle Linux 8 release, the following
features are under technology preview:

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

#### Multi-Protocol Label Switching

Multi-protocol Label Switching (MPLS) is an in-kernel data-forwarding mechanism that routes
the traffic flow across enterprise networks. In an MPLS network, the router that receives
packets decides the further route of the packets, based on the labels that are attached to the
packet. With the usage of labels, the MPLS network can handle packets with particular
characteristics.

#### XDP Features

XDP programs can be loaded on architectures other than AMD and Intel® 64-bit. Note, however,
that the `libxdp` library is available only for AMD and Intel® 64-bit platforms.
Likewise, in this technology preview feature, you can offload XDP hardware.

Also, XDP includes the Address Family eXpress Data Path (`AF_XDP`) socket for
high-performance packet processing. It grants efficient redirection of programmatically
selected packets to user space applications for further processing.

#### `act_mpls` Module

The `act_mpls` module in the `kernel-modules-extra` rpm applies
Multi-Protocol Label Switching (MPLS) actions with Traffic Control (TC) filters, for example,
push and pop MPLS label stack entries with TC filters. The module also accepts the Label,
Traffic Class, Bottom of Stack, and Time to Live fields to be set independently.

#### `systemd-resolved` Service

The `systemd-resolved` service provides name resolution to local applications.
Its components include a caching and validating DNS stub resolver, a Link-Local Multicast Name
Resolution (LLMNR), and Multicast DNS resolver and responder.

#### `nispor` Package

The `nispor` package is a unified interface for Linux network state querying
all running network status. Version 1.2.10 includes the following features and changes:

- `NetstateFilter` can use the kernel filter on network routes and
  interfaces.
- SR-IOV interfaces can query SR-IOV Virtual Function (SR-IOV VF) for every (VF).
- The `lacp_active`, `missed_max`, and
  `ns_ip6_target` bonding options are available.

You can install `nispor` in one of two ways:

- As an individual package:

  ```
  sudo dnf install nispor
  ```
- As a dependency of `nmstate`:

  ```
  sudo dnf install nmstate
  ```

  `nispor` is listed as the dependency.

For more information on using `nispor`, see the
`/usr/share/doc/nispor/README.md` file.

### Kernel

The following kernel features are available as technology previews.

#### `kexec` Fast Reboot

The `kexec fast reboot` feature is available as a technology preview
feature in Oracle Linux 8. This feature significantly speeds up the boot process by enabling
the kernel to boot directly into the second kernel without first passing through the Basic
Input/Output System (BIOS). To use this feature, load the `kexec` module first,
then reboot the system.

#### SGX Available

Software Guard Extensions (SGX) from Intel® protects software code and data
from disclosure and modification. The Linux kernel partially supports SGX v1 and SGX v1.5.
Version 1 enables platofmrs by using the Flexible Launch Control mechanism to use the SGX
technology.

#### Soft-RoCE Driver

The Soft-RoCE `rdma_rxe` is the software implementation of the Remote Direct
Memory Access (RDMA) over Converged Ethernet (RoCE) network protocol for processing RDMA over
Ethernet. Soft-RoCE maintains two protocol versions, RoCE v1 and RoCE v2.

#### Extended Berkeley Packet Filter (eBPF)

`eBPF` is an in-kernel virtual machine code is processed in the kernel space,
in the restricted sandbox environment with access to a limited set of
functions.

`eBPF` has a new system call `bpf()` for creating various types
of maps and for loading programs that can be attached onto various points (sockets,
tracepoints, packet reception) to receive and process data.

An `eBPF` component is `AF_XDP`, a socket for
connecting the eXpress Data Path (XDP) path to user space for
applications that prioritize packet processing performance.

#### Intel® Data Streaming Accelerator Driver

The driver is an Intel® CPU integrated accelerator and shares a work queue with process
address space ID (`pasid`) submission and shared virtual memory (SVM).

#### `accel-config` Package

The `accel-config` package is available on Intel® `EM64T` and
`AMD64` architectures for managing data-streaming accelerator (DSA) subsystem
in the Linux kernel. Also, it configures devices through `sysfs` (pseudo file
system), saves and loads the configuration in the `json` format.

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

#### NVMe/TCP Available

NVMe over Fabrics
TCP host and the target drivers are included in RHCK as a technology preview in this
release.

Note:

Support for NVMe/TCP is already available in Unbreakable Enterprise Kernel Release
6.

### High Availability and Clusters

The following features for high availability and clusters are available as technology
previews.

#### Pacemaker Podman Bundles

Pacemaker container bundles now run on Podman, with the container bundle feature being
available as a Technology Preview.

#### Heuristics in `corosync-qdevice`

Heuristics are a set of commands that run locally on startup, cluster membership change,
successful connect to `corosync-qnetd`, and, optionally, on a periodic basis.
When all commands finish successfully, heuristics have passed; otherwise, they have failed.
The heuristics result is sent to `corosync-qnetd` where it's used in
calculations to decide which partition is quorate.

#### Fence Agent

The `fence_heuristics_ping` agent is available with Pacemaker. The agent aims
to open a class of experimental fence agents that do no actual fencing by themselves but
instead exploit the behavior of fencing levels in a new way.

Through the agent, particularly by its issuing an `off` action, Pacemaker
can be informed if fencing would succeed or not. The heuristics agent can prevent the
agent that does the actual fecing from fencing a node under certain conditions.

### Cloud Environment

The following features for the cloud environment are available as technology preview.

#### VM Deployment in Azure

With the updated Oracle Linux kernel, Oracle Linux confidential virtual machines (VMs) can be
deployed on Microsoft Azure. However, encrypting confidential VM images while booting on Azure
isn't supported.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.9/ol8-DeprecatedFeatures.html -->

This chapter lists features and functionalities that are deprecated in Oracle Linux 8. While
these features might be currently included and operative in the release, support is not
guaranteed in future major releases. Thus, they should not be used in new Oracle Linux 8
deployments.

### Installation

The following installation related features and functionalities are deprecated in Oracle
Linux 8.

#### Kickstart Commands

- `auth` or `authconfig`
- `device`
- `deviceprobe`
- `dmraid`
- `install`
- `lilo`
- `lilocheck`
- `mouse`
- `multipath`
- `bootloader --upgrade`
- `ignoredisk --interactive`

  Using the `--interactive` option causes a fatal installation error. You
  must remove this option from any kickstart files.
- `partition --active`
- `reboot --kexec`
- `autostep`

Even though specific options are listed as deprecated, the base command and the other options
remain available and operative.

### Software Management

The following features and functionalities related to software management are deprecated
in Oracle Linux 8.

#### `rpmbuild --sign`

Using `rpmbuild --sign` can cause a fatal error in the system. Use the
`rpmsign` command instead.

### Shells and Command Lines

The following shell and command line components are deprecated in Oracle Linux 8.

#### OpenEXR

As a consequence of the OpenEXR deprecation, the `EXR` image format is no
longer supported in the `imagecodex` module.

#### Dump Utility

With this removal of support for the `dump` utility, use other commands to
back up file systems, for example, `tar`, `dd`, or
`bacula`.

The `restore` component of the `dump` package remains
supported and available as a separate `restore` package.

#### `hidepid=n` Mount Option

As a `mount` option, `hidepid=n` controls
access to `/proc/[pip]`. The option is incompatible with the
`systemd` infrastructure and might cause certain `systemd`
services to generate SELinux AVC denial messages, which would inhibit completion of other
operations.

#### ABRT Tool

The Automatic Bug Reporting Tool (ABRT) is used to detect and report application crashes.
Instead of this tool, use the `systemd-coredump` tool for logging and
storing core dumps that are generated when program crash.

#### `udev` Rename Device Helper Utility

The `udev` helper utility `/usr/lib/udev/rename_device` for
renaming network interfaces is deprecated.

#### ReaR Crontab

The `/etc/cron.d/rear` crontab is deprecated in the `rear`
package. The crontab utility monitors for any changes in the disk layout and runs
`rear mkrescue` if changes are detected. If you require the
`rear` functionality, configure the ReaR utility to run
periodically.

#### SQLite in Bacula

Support is deprecated for SQLite as a database backend of the Bacula backup system. You
should migrate to one of the backends that Bacula supports, such as PostgreSQL or
MySQL.

#### `raw` Command

Use of the deprecated `/usr/bin/raw` command in future Oracle Linux releases
might generate errors.

### Security

The following security related features and functionalities are deprecated in Oracle Linux
8.

#### NSS SEED Ciphers

Support for TLS cipher suites that use a SEED cipher is deprecated in the Network
Security Services (NSS) library from Mozilla. If your setup relies on SEED ciphers, you
should enable support for other cipher suites in preparation for the complete removal of
SEED ciphers from NSS.

#### TLS 1.0 and TLS 1.1

These two protocols are disabled in the `DEFAULT` system-wide cryptographic
policy level. If you require these protocols, switch the policy to the `LEGACY`
level as follows:

```
sudo update-crypto-policies --set LEGACY
```

#### DSA

Authentication mechanisms that are based on the deprecated Digital Signature Algorithm (DSA)
keys no longer work in the default configuration. OpenSSH clients do not accept DSA host keys
even when the system-wide cryptographic policy level is set to `LEGACY`.

#### `fapolicyd.rules`

Policies for allowing and denying execution rules used to be specified in the
`/etc/fapolicyd/fapolicyd.rules` file. This file is being replaced by
files inside the `/etc/fapolicyd/rules.d` directory.

The `fagenrules` script now merges all component rule files in this
directory to the `/etc/fapolicyd/compiled.rules` file. Rules in
`/etc/fapolicyd/fapolicyd.trust` are still processed by the
`fapolicyd` framework but only for ensuring backward compatibility.

#### SSL2 Client Hello

Secure Socket Layer 2's `Client Hello` message used to be supported by earlier
versions of the Transport Layer Security (TLS) protocol. Being deprecated in the NSS library,
this feature is now disabled by default.

If your application requires support for `Client Hello`, enable the
feature by using the `SSL_ENABLE_V2_COMPATIBLE_HELLO` API.

#### Runtime Disabling of SELinux

Setting the `SELINUX=disabled` option in `/etc/selinux/config`
to disable SELinux at runtime has deprecated support. If you use only this option to disable
SELinux, then SELinux remains enabled but with no loaded policy.

To completely disable SELinux, add the `selinux=0` parameter to the kernel
command line.

#### `ipa` SELinux Module

This module is no longer maintained and hence removed from the
`selinux-policy` package. The functionality is now included in the
`ipa-selinux` package.

#### TPM 1.2

The Trusted Platform Module (TPM) is updated to 2.0 with multiple improvements. However,
the updated version is not backward compatible with earlier versions. Consequently,
version 1.2 is deprecated.

#### `crypto-policies`

The introduction of scopes for `crypto-policies` directives in custom policies
has resulted in the deprecation of the following derived properties of
`crypto-policies`:

- `tls_cipher`
- `ssh_cipher`
- `ssh_group`
- `ike_protocol`
- `sha1_in_dnssec`

Use of the `protocol` property now requires a scope. For more information, see
the `crypto-policies(7)` manual page.

### Networking

The following network related features and functionalities are deprecated in Oracle Linux
8.

#### `PF_KEYv2` Kernel API

The `PF_KEYv2` kernel API, used for configuring IPSec, is deprecated in
favor of the `netlink` API, which is actively maintained to provide
important security features and updates.

#### Network Scripts

Network scripts are no longer available by default. New versions of `ifup`
and `ifdown` scripts call the NetworkManager service through the
`nmcli` tools. Therefore, to run these scripts in Oracle Linux 8, the
NetworkManager service must be running.

Other commands in `/sbin/ifup-local`, `ifdown-pre-local`, and
`ifdown-local` scripts are ignored. If you manually install the legacy
`network-scripts` package and use the scripts, a warning is displayed about
their deprecated state.

#### `dropwatch` Tool

Instead of the `dropwatch` tool, use the replacement `perf`
command line tool in future Oracle Linux deployments, which provides the same
functionality.

#### `xinetd` Service

The `xinetd` service is replaced by `systemd`.

#### `cgdcbxd` Package

The deprecated control group data center bridging exchange daemon (`cgdcbxd`)
monitors data center bridging (DCB) netlink events and manages the `net_prio
control` group subsystem. Support for this feature might be removed.

#### WEP Wi-Fi Connection

Instead of using this connection method, use the Wi-Fi Protected Access 3 (WPA3) or WPA2
connection methods.

#### `xt_u32` Module

The `xt_32` module enables users to match arbitrary 32 bits in the packet
header or payload for their `iptables`. Because this module is
unsupported, migrate to the `nftables` packet filtering framework.

First, change the firewall to use `iptables` with native matches to
incrementally replace individual rules. Then, use the
`iptables-translate` command and accompanying utilities to migrate to
`nftables`. If the `iptables` rules have no native
match in `nftables`, use the raw payload matching feature of
`nftables` instead.

For more information, see the raw payload expression section in the
`nft(8)` manual page.

### Kernel

The following kernel related features and functionalities are deprecated in Oracle Linux
8.

#### `rdma-rxe` Driver

Software Remote Direct Memory Access over Converged Ethernet (Soft-RoCE), or RXE,
emulates RDMA. Because of instability issues, this driver is now deprecated.

#### Linux `firewire` Subsystems and Associated User Space Components

The `firewire` subsystem provides interfaces to use and maintain any resources
on the IEEE 1394 bus. This subsystem is deprecated in the `kernel`
package and likewise, associated user space components that are provided by the
`libavc1394`, `libdc1394`, and
`libram1394` packages.

#### `crash-ptdump-command` Package

The `crash-ptdump-command` package is a `ptdump` extension
module for the crash utility. The package isn't maintained upstream and is deprecated in this
Oracle Linux 8 release.

### Bootloader

The following features and functionalities that are related to the bootloader are
deprecated in Oracle Linux 8.

#### `kernelopts` Environment Variable

The `kernelopts` environment variable stores the defined kernel command
line parameters for systems that use the GRUB2 bootloader. The variable was stored in
the `/boot/grub2/grubenv` file for each kernel boot entry. The variable
is deprecated and kernel command line parameters are stored in the Boot Loader
Specification (BLS) snippet as a replacement.

### File Systems and Storage

The following features and functionalities related to file systems and storage are deprecated
in Oracle Linux 8.

#### `elevator` Kernel Command

The `elevator` kernel command line parameter sets the disk scheduler for all
devices. If you require a different scheduler than what the kernel automatically selects, use
`udev` rule or the TuneD service to configure the preferred scheduler.

#### NFSv3 Over UDP

The NFS server no longer opens or listens on a User Datagram Protocol (UDP) socket by
default. Therefore, NFSv3 over UDP is disabled and no longer supported.

#### `peripety` Package

The `peripety` package is deprecated. The Peripety storage event
notification daemon parses system storage logs into structured storage events to enable
you investigate storage issues.

#### VDO Write Modes

- `sync`
- `async-unsafe`
- `auto`

In place of these modes, `async` is the recommended write mode to use.

#### VDO Manager

The VDO Manager is deprecated and is replaced by the LVM-VDO integration. To create VDO
volumes, preferably use the `lvcreate` command instead.

You can use the `/usr/sbin/lvm_import_vdo` script in the `lvm2`
package to convert existing volumes that were created with the VDO Manager. In this manner,
these volumes can be managed through the LVM-VDO integration.

#### cramfs Kernel Module

In place of the deprecated `cramfs` kernel module, use
`squashfs`, which is the recommended replacement.

### High Availability and Clusters

The following features and functionalities that related to high availability and clusters
are deprecated in Oracle Linux 8.

#### `pcs` Commands Support for `clufter` Tool

The `clufter` tool is used for analyzing cluster configuration formats. The
`pcs` commands that support the `clufter` tool are deprecated.
Using these commands generate a warning about their deprecations. Sections that are related to
these commands are removed from the `pcs` help display and the
`pcs(8)` manual page.

Specifically, the following commands are deprecated:

- `pcs config import-cman`
- `pcs config export`

### Dynamic programming languages, web, and database servers

The following dynamic programming languages, web, and database servers are deprecated in
Oracle Linux 8.

#### `mod_php` Module

The `mod_php` module used to enable PHP on the Apache HTTP Server is
available but is deprecated and not enabled in the default configuration. The module is
no longer available in Oracle Linux 9. The module is deprecated in favor of the FastCGI
Process Manager (`php-fpm`).

### Compilers and Development Tools

The following compilers and development tools are deprecated in Oracle Linux 8.

#### `libdwarf` Library

In place of the deprecated `libdwarf` library, use the
`elfutils` and `libdw` libraries for applications that
need to process ELF/DWARF files.

As an alternative to the `libdwarf-tools dwarfdump` program, you can use
the `binutils readelf` program or the `elfutils
eu-readelf` program. Both programs can be used by passing the
`--debug-dump` flag.

#### `gdb.i686` Packages

These packages were distributed in earlier Oracle Linux releases to support 32-bit
versions of the GNU Debugger (GDB). With the removal of support for 32-bit hardware,
these packages are no longer supported or available. The 64-bit version of GDB in
`gdb.x86_64` packages can debug 32-bit applications.

### Identity Management

The following identity management features are deprecated in Oracle Linux 8.

#### OpenSSH LDAP

The `openssh-ldap` subpackage is deprecated in favor of SSSD and the
`sss_ssh_authorizedkeys` helper on Oracle Linux 8.

#### DES and 3DES

The Data Encryption Standard (DES) algorithm was deprecated and disabled by default in
Oracle Linux 7. Single-DES (DES) and triple-DES (3DES) encryption types are removed in
Oracle Linux 8.

#### SSSD `libwbclient`

The SSSD implementation of the `libwbclient` package is deprecated and has
been removed.

#### Standalone `ctdb`

Standalone use of the `ctdb` clustered Samba service is deprecated. You
can continue to use this service as a Pacemaker resource with the `ctdb`
resource agent.

#### Samba NT4-style Domain Controllers

Use of Samba configured as either a Primary Domain Controller (PDC) or Backup Domain
Controller (BDC) in an NT3-style domain is deprecated. Oracle doesn't support using
Samba as an AD domain controller.

#### SMB1

The insecure Server Message Block version 1 (SMB1) protocol is deprecated. To improve
security, SMB1 is disabled in the Samba server and client utilities.

### Desktop

The following desktop related features and functionalities are deprecated in Oracle Linux
8.

#### `libgnome-keyring` Library

The `libgnome-keyring` library is deprecated in favor of the
`libsecret` library, which is more compliant with security standards.

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
Linux 8.

#### `virsh iface-*` Commands

`virsh iface-*` commands such as `virsh iface-start`,
`virsh iface-destroy`, and so on are deprecated. To configure and
manage host network connections, use instead the NetworkManager tool and its related
management applications, for example `nmcli`.

#### Virtual Machine Manager

In place of the deprecated Virtual Machine Manager (`virt-manager`), use
the web console, otherwise known as Cockpit.

#### Virtual Machine Snapshots

Support for creating snapshots of VMs is limited only to those that don't use UEFI firmware.
However, the operation might cause the QEMU monitor to become blocked and affects hypervisor
operations.

As an alternative, use external snapshots.

#### Cirrus VGA Virtual GPU Type

The Cirrus VGA GPU device is deprecated and support for it might be removed in KVM
virtual machines. In its place, use `stdvga`,
`virtio-vga`, or `qxi` devices.

#### Signatures Using SHA-1

The use of SHA1-based signatures to perform SecureBoot image verification on UEFI (PE/COFF)
executable files is deprecated. Instead, use signatures that are based on SHA-2 or later.

#### SPICE Remote Display Protocol

With the deprecation of the SPICE remote display protocol, the functionality of attaching
smart card readers to virtual machines (VMs) will be provided by third party remote
virtualization solutions.

Also, the deprecation of this protocol has the following consequences:

- For remote console access, use the VNC protocol.
- For advanced remote display functions, use third-party tools such as RDP, HP RGS, or
  Mechdyne TGX.

### Containers

The following features and functionalities that are related to containers are deprecated in
Oracle Linux 8.

#### `container-tools` Modules

The `container-tools:1.0`, `container-tools:2.0`, and
`container-tools:3.0` modules are deprecated and no longer support security
updates.

Use newer supported stable module streams, such as `container-tools:4.0`
instead.

#### CNI

The Container Network Interface (CNI) network stack is deprecated in favor of Netavark.

### Deprecated Packages

The support status of deprecated packages remains unchanged within Oracle Linux 8. For
more information about the length of support, see [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

The following packages are deprecated in Oracle Linux 8 and might be removed in a future
release of Oracle Linux:

- 389-ds-base-legacy-tools
- abrt
- abrt-addon-ccpp
- abrt-addon-kerneloops
- abrt-addon-pstoreoops
- abrt-addon-vmcore
- abrt-addon-xorg
- abrt-cli
- abrt-console-notification
- abrt-dbus
- abrt-desktop
- abrt-gui
- abrt-gui-libs
- abrt-libs
- abrt-tui
- adobe-source-sans-pro-fonts
- adwaita-qt
- alsa-plugins-pulseaudio
- amanda
- amanda-client
- amanda-libs
- amanda-server
- ant-contrib
- antlr3
- antlr32
- aopalliance
- apache-commons-collections
- apache-commons-compress
- apache-commons-exec
- apache-commons-jxpath
- apache-commons-parent
- apache-ivy
- apache-parent
- apache-resource-bundles
- apache-sshd
- apiguardian
- aspnetcore-runtime-3.0
- aspnetcore-runtime-3.1
- aspnetcore-runtime-5.0
- aspnetcore-targeting-pack-3.0
- aspnetcore-targeting-pack-3.1
- aspnetcore-targeting-pack-5.0
- assertj-core
- authd
- auto
- autoconf213
- autogen
- autogen-libopts
- awscli
- base64coder
- batik
- batik-css
- batik-util
- bea-stax
- bea-stax-api
- bind-export-devel
- bind-export-libs
- bind-libs-lite
- bind-pkcs11
- bind-pkcs11-devel
- bind-pkcs11-libs
- bind-pkcs11-utils
- bind-sdb
- bind-sdb
- bind-sdb-chroot
- bluez-hid2hci
- boost-jam
- boost-signals
- bouncycastle
- bpg-algeti-fonts
- bpg-chveulebrivi-fonts
- bpg-classic-fonts
- bpg-courier-fonts
- bpg-courier-s-fonts
- bpg-dedaena-block-fonts
- bpg-dejavu-sans-fonts
- bpg-elite-fonts
- bpg-excelsior-caps-fonts
- bpg-excelsior-condenced-fonts
- bpg-excelsior-fonts
- bpg-fonts-common
- bpg-glaho-fonts
- bpg-gorda-fonts
- bpg-ingiri-fonts
- bpg-irubaqidze-fonts
- bpg-mikhail-stephan-fonts
- bpg-mrgvlovani-caps-fonts
- bpg-mrgvlovani-fonts
- bpg-nateli-caps-fonts
- bpg-nateli-condenced-fonts
- bpg-nateli-fonts
- bpg-nino-medium-cond-fonts
- bpg-nino-medium-fonts
- bpg-sans-fonts
- bpg-sans-medium-fonts
- bpg-sans-modern-fonts
- bpg-sans-regular-fonts
- bpg-serif-fonts
- bpg-serif-modern-fonts
- bpg-ucnobi-fonts
- brlapi-java
- bsh
- buildnumber-maven-plugin
- byaccj
- cal10n
- cbi-plugins
- cdparanoia
- cdparanoia-devel
- cdparanoia-libs
- cdrdao
- cmirror
- codehaus-parent
- codemodel
- compat-exiv2-026
- compat-guile18
- compat-hwloc1
- compat-libpthread-nonshared
- compat-libtiff3
- compat-openssl10
- compat-sap-c++-11
- compat-sap-c++-10
- compat-sap-c++-9
- createrepo\_c-devel
- ctags
- ctags-etags
- custodia
- cyrus-imapd-vzic
- dbus-c++
- dbus-c++-devel
- dbus-c++-glib
- dbxtool
- dhcp-libs
- directory-maven-plugin
- directory-maven-plugin-javadoc
- dirsplit
- dleyna-connector-dbus
- dleyna-core
- dleyna-renderer
- dleyna-server
- dnssec-trigger
- dnssec-trigger-panel
- dotnet-apphost-pack-3.0
- dotnet-apphost-pack-3.1
- dotnet-apphost-pack-5.0
- dotnet-host-fxr-2.1
- dotnet-host-fxr-2.1
- dotnet-hostfxr-3.0
- dotnet-hostfxr-3.1
- dotnet-hostfxr-5.0
- dotnet-runtime-2.1
- dotnet-runtime-3.0
- dotnet-runtime-3.1
- dotnet-runtime-5.0
- dotnet-sdk-2.1
- dotnet-sdk-2.1.5xx
- dotnet-sdk-3.0
- dotnet-sdk-3.1
- dotnet-sdk-5.0
- dotnet-targeting-pack-3.0
- dotnet-targeting-pack-3.1
- dotnet-targeting-pack-5.0
- dotnet-templates-3.0
- dotnet-templates-3.1
- dotnet-templates-5.0
- dotnet5.0-build-reference-packages
- dptfxtract
- drpm
- drpm-devel
- dump
- dvd+rw-tools
- dyninst-static
- eclipse-ecf
- eclipse-ecf-core
- eclipse-ecf-runtime
- eclipse-emf
- eclipse-emf-core
- eclipse-emf-runtime
- eclipse-emf-xsd
- eclipse-equinox-osgi
- eclipse-jdt
- eclipse-license
- eclipse-p2-discovery
- eclipse-pde
- eclipse-platform
- eclipse-swt
- ed25519-java
- ee4j-parent
- elfutils-devel-static
- elfutils-libelf-devel-static
- enca
- enca-devel
- environment-modules-compat
- evince-browser-plugin
- exec-maven-plugin
- farstream02
- felix-gogo-command
- felix-gogo-runtime
- felix-gogo-shell
- felix-scr
- felix-osgi-compendium
- felix-osgi-core
- felix-osgi-foundation
- felix-parent
- file-roller
- fipscheck
- fipscheck-devel
- fipscheck-lib
- firewire
- fonts-tweak-tool
- forge-parent
- freeradius-mysql
- freeradius-perl
- freeradius-postgresql
- freeradius-rest
- freeradius-sqlite
- freeradius-unixODBC
- fuse-sshfs
- fusesource-pom
- future
- gamin
- gamin-devel
- gavl
- gcc-toolset-9
- gcc-toolset-9-annobin
- gcc-toolset-9-build
- gcc-toolset-9-perftools
- gcc-toolset-9-runtime
- gcc-toolset-9-toolchain
- gcc-toolset-10
- gcc-toolset-10-annobin
- gcc-toolset-10-binutils
- gcc-toolset-10-binutils-devel
- gcc-toolset-10-build
- gcc-toolset-10-dwz
- gcc-toolset-10-dyninst
- gcc-toolset-10-dyninst-devel
- gcc-toolset-10-elfutils
- gcc-toolset-10-elfutils-debuginfod-client
- gcc-toolset-10-elfutils-debuginfod-client-devel
- gcc-toolset-10-elfutils-devel
- gcc-toolset-10-elfutils-libelf
- gcc-toolset-10-elfutils-libelf-devel
- gcc-toolset-10-elfutils-libs
- gcc-toolset-10-gcc
- gcc-toolset-10-gcc-c++
- gcc-toolset-10-gcc-gdb-plugin
- gcc-toolset-10-gcc-gfortran
- gcc-toolset-10-gdb
- gcc-toolset-10-gdb-doc
- gcc-toolset-10-gdb-gdbserver
- gcc-toolset-10-libasan-devel
- gcc-toolset-10-libatomic-devel
- gcc-toolset-10-libitm-devel
- gcc-toolset-10-liblsan-devel
- gcc-toolset-10-libquadmath-devel
- gcc-toolset-10-libstdc++-devel
- gcc-toolset-10-libstdc++-docs
- gcc-toolset-10-libtsan-devel
- gcc-toolset-10-libubsan-devel
- gcc-toolset-10-ltrace
- gcc-toolset-10-make
- gcc-toolset-10-make-devel
- gcc-toolset-10-perftools
- gcc-toolset-10-runtime
- gcc-toolset-10-strace
- gcc-toolset-10-systemtap
- gcc-toolset-10-systemtap-client
- gcc-toolset-10-systemtap-devel
- gcc-toolset-10-systemtap-initscript
- gcc-toolset-10-systemtap-runtime
- gcc-toolset-10-systemtap-sdt-devel
- gcc-toolset-10-systemtap-server
- gcc-toolset-10-toolchain
- gcc-toolset-10-valgrind
- gcc-toolset-10-valgrind-devel
- gcc-toolset-11-make-devel
- gcc-toolset-12-annobin-annocheck
- gcc-toolset-12-annobin-docs
- gcc-toolset-12-annobin-plugin-gcc
- gcc-toolset-12-binutils
- gcc-toolset-12-binutils-devel
- gcc-toolset-12-binutils-gold
- GConf2
- GConf2-devel
- gegl
- genisoimage
- genwqe-tools
- genwqe-vpd
- genwqe-zlib
- genwqe-zlib-devel
- geoipupdate
- geronimo-annotation
- geronimo-jms
- geronimo-jpa
- geronimo-parent-poms
- gfbgraph
- gflags
- gflags-devel
- glassfish-annotation-api
- glassfish-el
- glassfish-fastinfoset
- glassfish-jaxb-core
- glassfish-jaxb-txw2
- glassfish-jsp
- glassfish-jsp-api
- glassfish-legal
- glassfish-master-pom
- glassfish-servlet-api
- glew-devel
- glib2-fam
- glog
- glog-devel
- gmock
- gmock-devel
- gnome-abrt
- gnome-boxes
- gnome-menus-devel
- gnome-online-miners
- gnome-shell-extension-disable-screenshield
- gnome-shell-extension-horizontal-workspaces
- gnome-shell-extension-no-hot-corner
- gnome-shell-extension-window-grouper
- gnome-themes-standard
- gnu-free-fonts-common
- gnu-free-mono-fonts
- gnu-free-sans-fonts
- gnu-free-serif-fonts
- gnupg2-smime
- gnuplot
- gnuplot-common
- gobject-introspection-devel
- google-gson
- google-noto-sans-syriac-eastern-fonts
- google-noto-sans-syriac-estrangela-fonts
- google-noto-sans-syriac-western-fonts
- google-noto-sans-tibetan-fonts
- google-noto-sans-ui-fonts
- gphoto2
- gsl-devel
- gssntlmssp
- gtest
- gtest-devel
- gtkmm24
- gtkmm24-devel
- gtkmm24-docs
- gtksourceview3
- gtksourceview3-devel
- gtkspell
- gtkspell-devel
- gtkspell3
- guile
- gutenprint-gimp
- gutenprint-libs-ui
- gvfs-afc
- gvfs-afp
- gvfs-archive
- hamcrest-core
- hawtjni
- hawtjni
- hawtjni-runtime
- HdrHistogram
- HdrHistogram-javadoc
- highlight-gui
- hivex-devel
- hostname
- hplip-gui
- httpcomponents-project
- hwloc-plugins
- hyphen-fo
- hyphen-grc
- hyphen-hsb
- hyphen-ia
- hyphen-is
- hyphen-ku
- hyphen-mi
- hyphen-mn
- hyphen-sa
- hyphen-tk
- ibus-sayura
- icedax
- icu4j
- idm-console-framework
- inkscape
- inkscape-docs
- inkscape-view
- iptables
- ipython
- isl
- isl-devel
- isorelax
- istack-commons-runtime
- istack-commons-tools
- iwl3945-firmware
- iwl4965-firmware
- iwl6000-firmware
- jacoco
- jaf
- jaf-javadoc
- jakarta-oro
- janino
- jansi-native
- jarjar
- java-1.8.0-ibm
- java-1.8.0-ibm-demo
- java-1.8.0-ibm-devel
- java-1.8.0-ibm-headless
- java-1.8.0-ibm-jdbc
- java-1.8.0-ibm-plugin
- java-1.8.0-ibm-src
- java-1.8.0-ibm-webstart
- java-1.8.0-openjdk-accessibility
- java-1.8.0-openjdk-accessibility-slowdebug
- java\_cup
- java-atk-wrapper
- javacc
- javacc-maven-plugin
- javaewah
- javaparser
- javapoet
- javassist
- javassist-javadoc
- jaxen
- jboss-annotations-1.2-api
- jboss-interceptors-1.2-api
- jboss-logmanager
- jboss-parent
- jctools
- jdepend
- jdependency
- jdom
- jdom2
- jetty
- jetty-continuation
- jetty-http
- jetty-io
- jetty-security
- jetty-server
- jetty-servlet
- jetty-util
- jffi
- jflex
- jgit
- jline
- jmc
- jnr-netdb
- jolokia-jvm-agent
- js-uglify
- jsch
- json\_simple
- jss-javadoc
- jtidy
- junit5
- jvnet-parent
- jzlib
- kernel-cross-headers
- ksc
- kurdit-unikurd-web-fonts
- kyotocabinet-libs
- ldapjdk-javadoc
- lensfun
- lensfun-devel
- lftp-scripts
- libaec
- libaec-devel
- libappindicator-gtk3
- libappindicator-gtk3-devel
- libatomic-static
- libavc1394
- libblocksruntime
- libcacard
- libcacard-devel
- libcgroup
- libcgroup-tools
- libchamplain
- libchamplain-devel
- libchamplain-gtk
- libcroco
- libcroco-devel
- libcxl
- libcxl-devel
- libdap
- libdap-devel
- libdazzle-devel
- libdbusmenu
- libdbusmenu-devel
- libdbusmenu-doc
- libdbusmenu-gtk3
- libdbusmenu-gtk3-devel
- libdc1394
- libdnet
- libdnet-devel
- libdv
- libdwarf
- libdwarf-devel
- libdwarf-static
- libdwarf-tools
- libeasyfc
- libeasyfc-gobject
- libepubgen-devel
- libertas-sd8686-firmware
- libertas-usb8388-firmware
- libertas-usb8388-olpc-firmware
- libgdither
- libGLEW
- libgovirt
- libguestfs-benchmarking
- libguestfs-devel
- libguestfs-gfs2
- libguestfs-gobject
- libguestfs-gobject-devel
- libguestfs-java
- libguestfs-java-devel
- libguestfs-javadoc
- libguestfs-man-pages-ja
- libguestfs-man-pages-uk
- libguestfs-tools
- libguestfs-tools-c
- libhugetlbfs
- libhugetlbfs-devel
- libhugetlbfs-utils
- libIDL
- libIDL-devel
- libidn
- libiec61883
- libindicator-gtk3
- libindicator-gtk3-devel
- libiscsi-devel
- libjose-devel
- libkkc
- libkkc-common
- libkkc-data
- libldb-devel
- liblogging
- libluksmeta-devel
- libmalaga
- libmcpp
- libmemcached
- libmemcached-libs
- libmetalink
- libmodulemd1
- libmongocrypt
- libmtp-devel
- libmusicbrainz5
- libmusicbrainz5-devel
- libnbd-devel
- liboauth
- liboauth-devel
- libpfm-static
- libpng12
- libpurple
- libpurple-devel
- libraw1394
- libreport-plugin-mailx
- libreport-plugin-rhtsupport
- libreport-plugin-ureport
- libreport-ol
- libreport-ol-bugzilla
- librpmem
- librpmem-debug
- librpmem-devel
- libsass
- libsass-devel
- libselinux-python
- libsqlite3x
- libtalloc-devel
- libtar
- libtdb-devel
- libtevent-devel
- libtpms-devel
- libunwind
- libusal
- libvarlink
- libverto-libevent
- libvirt-admin
- libvirt-bash-completion
- libvirt-daemon-driver-storage-gluster
- libvirt-daemon-driver-storage-iscsi-direct
- libvirt-devel
- libvirt-docs
- libvirt-gconfig
- libvirt-gobject
- libvirt-lock-sanlock
- libvirt-wireshark
- libvmem
- libvmem-debug
- libvmem-devel
- libvmmalloc
- libvmmalloc-debug
- libvmmalloc-devel
- libvncserver
- libwinpr-devel
- libwmf
- libwmf-devel
- libwmf-lite
- libXNVCtrl
- libyami
- log4j12
- log4j12-javadoc
- lohit-malayalam-fonts
- lohit-nepali-fonts
- lorax-composer
- lua-guestfs
- lucene
- lucene-analysis
- lucene-analyzers-smartcn
- lucene-queries
- lucene-queryparser
- lucene-sandbox
- lz4-java
- lz4-java-javadoc
- mailman
- mailx
- make-devel
- malaga
- malaga-suomi-voikko
- marisa
- maven-antrun-plugin
- maven-assembly-plugin
- maven-clean-plugin
- maven-dependency-analyzer
- maven-dependency-plugin
- maven-doxia
- maven-doxia-sitetools
- maven-install-plugin
- maven-invoker
- maven-invoker-plugin
- maven-parent
- maven-plugins-pom
- maven-reporting-api
- maven-reporting-impl
- maven-resolver-api
- maven-resolver-connector-basic
- maven-resolver-impl
- maven-resolver-spi
- maven-resolver-transport-wagon
- maven-resolver-util
- maven-scm
- maven-script-interpreter
- maven-shade-plugin
- maven-shared
- maven-verifier
- maven-wagon-file
- maven-wagon-http
- maven-wagon-http-shared
- maven-wagon-provider-api
- maven2
- meanwhile
- mercurial
- mercurial-hgk
- metis
- metis-devel
- mingw32-bzip2
- mingw32-bzip2-static
- mingw32-cairo
- mingw32-expat
- mingw32-fontconfig
- mingw32-freetype
- mingw32-freetype-static
- mingw32-gstreamer1
- mingw32-harfbuzz
- mingw32-harfbuzz-static
- mingw32-icu
- mingw32-libjpeg-turbo
- mingw32-libjpeg-turbo-static
- mingw32-libpng
- mingw32-libpng-static
- mingw32-libtiff
- mingw32-libtiff-static
- mingw32-openssl
- mingw32-readline
- mingw32-sqlite
- mingw32-sqlite-static
- mingw64-adwaita-icon-theme
- mingw64-bzip2
- mingw64-bzip2-static
- mingw64-cairo
- mingw64-expat
- mingw64-fontconfig
- mingw64-freetype
- mingw64-freetype-static
- mingw64-gstreamer1
- mingw64-harfbuzz
- mingw64-harfbuzz-static
- mingw64-icu
- mingw64-libjpeg-turbo
- mingw64-libjpeg-turbo-static
- mingw64-libpng
- mingw64-libpng-static
- mingw64-libtiff
- mingw64-libtiff-static
- mingw64-nettle
- mingw64-openssl
- mingw64-readline
- mingw64-sqlite
- mingw64-sqlite-static
- modello
- mojo-parent
- mongo-c-driver
- mousetweaks
- mozjs52
- mozjs52-devel
- mozjs60
- mozjs60-devel
- mozvoikko
- msv-javadoc
- msv-manual
- munge-maven-plugin
- mythes-mi
- mythes-ne
- nafees-web-naskh-fonts
- nbd
- nbdkit-devel
- nbdkit-example-plugins
- nbdkit-gzip-plugin
- nbdkit-plugin-python-common
- nbdkit-plugin-vddk
- ncompress
- ncurses-compat-libs
- net-tools
- netcf
- netcf-devel
- netcf-libs
- network-scripts
- network-scripts-ppp
- nkf
- nodejs-devel
- nodejs-packaging
- nss\_nis
- nss-pam-ldapd
- objectweb-asm
- objectweb-asm-javadoc
- objectweb-pom
- ocaml-bisect-ppx
- ocaml-camlp4
- ocaml-camlp4-devel
- ocaml-lwt
- ocaml-mmap
- ocaml-ocplib-endian
- ocaml-ounit
- ocaml-result
- ocaml-seq
- opencryptoki-tpmtok
- opencv-contrib
- opencv-core
- opencv-devel
- openhpi
- openhpi-libs
- OpenIPMI-perl
- openssh-cavs
- openssh-ldap
- openssl-ibmpkcs11
- opentest4j
- os-maven-plugin
- pakchois
- pandoc
- paps-libs
- paranamer
- parfait
- parfait-examples
- parfait-javadoc
- pcp-parfait-agent
- pcp-pmda-rpm
- pcp-pmda-vmware
- pcsc-lite-doc
- peripety
- perl-B-Debug
- perl-B-Lint
- perl-Class-Factory-Util
- perl-Class-ISA
- perl-DateTime-Format-HTTP
- perl-DateTime-Format-Mail
- perl-File-CheckTree
- perl-homedir
- perl-libxml-perl
- perl-Locale-Codes
- perl-Mozilla-LDAP
- perl-NKF
- perl-Object-HashBase-tools
- perl-Package-DeprecationManager
- perl-Pod-LaTeX
- perl-Pod-Plainer
- perl-prefork
- perl-String-CRC32
- perl-SUPER
- perl-Sys-Virt
- perl-tests
- perl-YAML-Syck
- phodav
- php-recode
- php-xmlrpc
- pidgin
- pidgin-devel
- pidgin-sipe
- pinentry-emacs
- pinentry-gtk
- pipewire0.2-devel
- pipewire0.2-libs
- platform-python-coverage
- plexus-ant-factory
- plexus-bsh-factory
- plexus-cli
- plexus-component-api
- plexus-component-factories-pom
- plexus-components-pom
- plexus-i18n
- plexus-interactivity
- plexus-pom
- plexus-velocity
- plymouth-plugin-throbgress
- pmreorder
- postgresql-test-rpm-macros
- powermock
- prometheus-jmx-exporter
- prometheus-jmx-exporter-openjdk11
- ptscotch-mpich
- ptscotch-mpich-devel
- ptscotch-mpich-devel-parmetis
- ptscotch-openmpi
- ptscotch-openmpi-devel
- purple-sipe
- pygobject2-doc
- pygtk2
- pygtk2-codegen
- pygtk2-devel
- pygtk2-doc
- python-nose-docs
- python-nss-doc
- python-podman-api
- python-psycopg2-doc
- python-pymongo-doc
- python-redis
- python-schedutils
- python-slip
- python-sqlalchemy-doc
- python-varlink
- python-virtualenv-doc
- python2-backports
- python2-backports-ssl\_match\_hostname
- python2-bson
- python2-coverage
- python2-docs
- python2-docs-info
- python2-funcsigs
- python2-ipaddress
- python2-mock
- python2-nose
- python2-numpy-doc
- python2-psycopg2-debug
- python2-psycopg2-tests
- python2-pymongo
- python2-pymongo-gridfs
- python2-pytest-mock
- python2-sqlalchemy
- python2-tools
- python2-virtualenv
- python3-bson
- python3-click
- python3-coverage
- python3-cpio
- python3-custodia
- python3-docs
- python3-flask
- python3-gevent
- python3-gobject-base
- python3-hivex
- python3-html5lib
- python3-hypothesis
- python3-ipatests
- python3-itsdangerous
- python3-jwt
- python3-libguestfs
- python3-mock
- python3-networkx-core
- python3-nose
- python3-nss
- python3-openipmi
- python3-pillow
- python3-ptyprocess
- python3-pydbus
- python3-pymongo
- python3-pymongo-gridfs
- python3-pyOpenSSL
- python3-pytoml
- python3-reportlab
- python3-schedutils
- python3-scons
- python3-semantic\_version
- python3-slip
- python3-slip-dbus
- python3-sqlalchemy
- python3-syspurpose
- python3-virtualenv
- python3-webencodings
- python3-werkzeug
- python38-asn1crypto
- python38-numpy-doc
- python38-psycopg2-doc
- python38-psycopg2-tests
- python39-numpy-doc
- python39-psycopg2-doc
- python39-psycopg2-tests
- qemu-kvm-block-gluster
- qemu-kvm-block-iscsi
- qemu-kvm-block-ssh
- qemu-kvm-hw-usbredir
- qemu-kvm-device-display-virtio-gpu-gl
- qemu-kvm-device-display-virtio-gpu-pci-gl
- qemu-kvm-device-display-virtio-vga-gl
- qemu-kvm-tests
- qpdf
- qpdf-doc
- qpid-proton
- qrencode
- qrencode-devel
- qrencode-libs
- qt5-qtcanvas3d
- qt5-qtcanvas3d-examples
- rarian
- rarian-compat
- re2c
- recode
- redhat-lsb
- redhat-lsb-core
- redhat-lsb-cxx
- redhat-lsb-desktop
- redhat-lsb-languages
- redhat-lsb-printing
- redhat-lsb-submod-multimedia
- redhat-lsb-submod-security
- redhat-lsb-supplemental
- redhat-lsb-trialuse
- redhat-menus
- redhat-support-lib-python
- redhat-support-tool
- reflections
- regexp
- relaxngDatatype
- rhsm-gtk
- rpm-plugin-prioreset
- rpmemd
- rsyslog-udpspoof
- ruby-hivex
- ruby-libguestfs
- rubygem-abrt
- rubygem-abrt-doc
- rubygem-bson
- rubygem-bson-doc
- rubygem-bundler-doc
- rubygem-mongo
- rubygem-mongo-doc
- rubygem-net-telnet
- rubygem-xmlrpc
- s390utils-cmsfs
- samba-pidl
- samba-test
- samba-test-libs
- samyak-devanagari-fonts
- samyak-fonts-common
- samyak-gujarati-fonts
- samyak-malayalam-fonts
- samyak-odia-fonts
- samyak-tamil-fonts
- sane-frontends
- sanlk-reset
- sat4j
- scala
- scotch
- scotch-devel
- SDL\_sound
- selinux-policy-minimum
- sendmail
- sgabios
- sgabios-bin
- shrinkwrap
- sisu-inject
- sisu-mojos
- sisu-plexus
- skkdic
- SLOF
- smc-anjalioldlipi-fonts
- smc-dyuthi-fonts
- smc-fonts-common
- smc-kalyani-fonts
- smc-raghumalayalam-fonts
- smc-suruma-fonts
- softhsm-devel
- sonatype-oss-parent
- sonatype-plugins-parent
- sos-collector
- sparsehash-devel
- spax
- spec-version-maven-plugin
- spice
- spice-client-win-x64
- spice-client-win-x86
- spice-glib
- spice-glib-devel
- spice-gtk
- spice-gtk-tools
- spice-gtk3
- spice-gtk3-devel
- spice-gtk3-vala
- spice-parent
- spice-protocol
- spice-qxl-wddm-dod
- spice-server
- spice-server-devel
- spice-qxl-xddm
- spice-server
- spice-streaming-agent
- spice-vdagent-win-x64
- spice-vdagent-win-x86
- sssd-libwbclient
- star
- stax-ex
- stax2-api
- stringtemplate
- stringtemplate4
- subscription-manager-initial-setup-addon
- subscription-manager-migration
- subscription-manager-migration-data
- subversion-javahl
- SuperLU
- SuperLU-devel
- supermin-devel
- swig
- swig-doc
- swig-gdb
- swtpm-devel
- swtpm-tools-pkcs11
- system-storage-manager
- tcl-brlapi
- testng
- tibetan-machine-uni-fonts
- timedatex
- tpm-quote-tools
- tpm-tools
- tpm-tools-pkcs11
- treelayout
- trousers
- trousers-lib
- tuned-profiles-compat
- tuned-profiles-nfv-host-bin
- tuned-utils-systemtap
- tycho
- uglify-js
- unbound-devel
- univocity-output-tester
- univocity-parsers
- usbguard-notifier
- usbredir-devel
- utf8cpp
- uthash
- velocity
- vinagre
- vino
- virt-dib
- virt-p2v-maker
- vm-dump-metrics-devel
- weld-parent
- wodim
- woodstox-core
- wqy-microhei-fonts
- wqy-unibit-fonts
- xdelta
- xmlgraphics-commons
- xmlstreambuffer
- xinetd
- xorg-x11-apps
- xorg-x11-drv-qxl
- xorg-x11-server-Xspice
- xpp3
- xsane-gimp
- xsom
- xz-java
- xz-java-javadoc
- yajl-devel
- yp-tools
- ypbind
- ypserv


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.9/ol8-KnownIssues.html -->

This chapter lists known issues in the current Oracle Linux 8 release. The list covers issues
that might affect both x86 and aarch64 platforms. In the list, additional issues that are
specific only to aarch64 platforms are labeled `aarch64 only:`.

The following guides provide additional information about known issues that related to
specific Oracle Linux components:

- Podman container management tool: [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/)
- System and Oracle Cloud Infrastructure instance upgrade using Leapp: [Oracle Linux 8: Upgrading Systems With Leapp](https://docs.oracle.com/en/operating-systems/oracle-linux/8/leapp/)

### Installation and Upgrade Issues

The following are known installation and upgrade issues for
Oracle Linux 8.6.

#### Messages Referring to `tmpfiles.d` Files Appear During Upgrade

During an upgrade from Oracle Linux
8.5 to Oracle Linux 8.6, and with the appropriate Oracle Linux 8 repositories enabled, the
`dnf upgrade` command displays messages similar to the following:

```
Running scriptlet: systemd-239-44.0.1.el8.x86_64                    
4550/4550
[/usr/lib/tmpfiles.d/dnssec-trigger.conf:1] Line references path below legacy
directory /var/run/, updating /var/run/dnssec-trigger â /run/dnssec-trigger;
please update the tmpfiles.d/ drop-in file accordingly.
[/usr/lib/tmpfiles.d/krb5-krb5kdc.conf:1] Line references path below legacy
directory /var/run/, updating /var/run/krb5kdc â /run/krb5kdc; please update
the tmpfiles.d/ drop-in file accordingly.
[/usr/lib/tmpfiles.d/nss-pam-ldapd.conf:2] Line references path below legacy
directory /var/run/, updating /var/run/nslcd â /run/nslcd; please update the
tmpfiles.d/ drop-in file accordingly.
[/usr/lib/tmpfiles.d/pesign.conf:1] Line references path below legacy
directory /var/run/, updating /var/run/pesign â /run/pesign; please update
the tmpfiles.d/ drop-in file accordingly.
[/usr/lib/tmpfiles.d/portreserve.conf:1] Line references path below legacy
directory /var/run/, updating /var/run/portreserve â /run/portreserve; please
update the tmpfiles.d/ drop-in file accordingly.
.
.
.
```

These messages can be safely ignored, as the upgrade or
package installation completes successfully.

As an alternative workaround, update the configuration by following the instructions in the
message. Change the legacy `var/run/`<...> directory
path to `/run/`<...>.

(Bug ID 32852433)

#### Installer Automatically Enables Ethernet Over USB Network Interface During a PXE Installation

During a Preboot
Execution Environment (PXE) installation of Oracle Linux 8, the installer automatically
enables the Ethernet over USB network interface with the `bootproto=dhcp` and
`ONBOOT=yes` parameters. These default settings causes the
`NetworkManager` service to fail to start.

To prevent this issue from occurring, or to resolve the issue
if you have already encountered it, use one of the following
workarounds:

- Prior to installation, disable the
  `ONBOOT` parameter for the Ethernet over
  USB network interface in the kickstart file, as follows:

  ```
  network --bootproto=dhcp --device=enp0s20f0u8u3c2 --onboot=off --ipv6=auto
  ```
- During installation, on the Network & Host Name
  screen, do not select the Connect
  automatically with priority check box to
  connect automatically on every reboot for the Ethernet
  over USB network interface.
- If you have already encountered this issue, then after the installation, change the
  network configuration setting for the Ethernet over USB network interface to
  `ONBOOT=no`. Then reboot the system.

(Bug ID 31888490)

#### Interactive Text-Based Installation Wizard Unable to Complete When An Alternate Language Is Selected

If you selected an alternate language while
using the text-based installer to install the OS, you cannot proceed with the installation.
The installation is blocked with [!] flags for Software Selection and Installation
Destination regardless of what you have set for these two options.

However, this issue does not occur if you are performing an installation by using the
default English language selection or by using the graphical installation program.

(Bug IDs 30535416, 29648703)

#### Graphical Installation Program Fails to Produce Error When an Unacceptable Kdump Value Is Entered

A minor upstream usability error affects the graphical installation program
during the configuration of Kdump.

If you specify an unacceptable value when manually configuring the Kdump memory reservation,
you can click `Done` to return to the Installation Summary screen. The
installer does not generate a warning or error message. Instead, the installer automatically
resets the value either to the last known acceptable value or the default value of 512 MB,
which enables the installation to succeed. However, because this corrected setting is not
displayed on the screen, you might not become aware that your specified value was ignored.

This issue does not occur with the text-based installer, which correctly returns an error if
you enter an unacceptable value and prevents you from continuing.

(Bug IDs 31133351, 31182708)

#### Graphical Installation Program Does Not Display the Reserved Memory That's Manually Set For Kdump

A minor usability error affects the graphical installation program
during the configuration of Kdump. If you manually change the default memory size that is
reserved for Kdump, the new setting is not displayed when the screen is refreshed. Instead,
only the values for the total system memory and usable system memory are displayed.
Consequently, the limits for the parameter "Memory to be reserved (Mb)" become unknown for
future Kdump configuration.

Note:

The default setting `auto` for Kdump memory reservation is adequate as the
kernel determines what size to use when it boots

(Bug IDs 31133287 and 31182699)

#### Scriptlet-Related Error for `microcode_ctl` Might Be Displayed During Upgrade

A scriplet-related
error message might be displayed during an upgrade of an Oracle Linux 8 release to its next
version. When you run the `dnf update` command, an output similar to the
following might appear:

```
  Running scriptlet: tuned-2.13.0-6.0.2.el8.noarch                            
             1089/1089
  Running scriptlet: microcode_ctl-4:20191115-4.el8.x86_64                    
             1089/1089
realpath: weak-updates/kmod-kvdo/vdo/kvdo.ko: No such file or directory
realpath: weak-updates/kmod-kvdo/uds/uds.ko: No such file or directory
dracut: installkernel failed in module kernel-modules-extra
warning: %posttrans(microcode_ctl-4:20191115-4.el8.x86_64) scriptlet failed,
exit status 1

Error in POSTTRANS scriptlet in rpm package microcode_ctl
  Running scriptlet: libgcc-8.3.1-4.5.0.7.el8.x86_64                          
             1089/1089
  Running scriptlet: glibc-common-2.28-101.0.1.el8.x86_64                    
             1089/1089
  Running scriptlet: info-6.5-6.el8.x86_64                                    
             1089/1089
```

This error message is displayed if you use the Server with GUI environment to install Oracle
Linux 8 and then you reboot the server by using RHCK. This installation method installs the
kernel dependent, `kmod-kvdo` package or module, which is a different version
in the previous Oracle Linux 8 release.

However, you can safely ignore the message because the `kmod-kvdo` package is
successfully installed during the upgrade process.

Note:

This error does not occur if you install the Minimal Install
base environment or if you boot the server with UEK R6 or
UEK R7.

(Bug ID 31292199)

#### `rhnreg_ks` Register Command Might Fail If `python3-rhn-virtualization-host` Package Is Installed

Beginning with
Oracle Linux 8.1, using the `rhnreg_ks` command to register a system with the
Unbreakable Linux Network (ULN)might fail if the
`python3-rhn-virtualization-hosts` package is installed on the system. This
issue has been observed when the `libvirtd` service is not running.

To work around this issue, ensure that the `libvirtd` packages are installed
on your system and that the service is enabled and running prior to issuing the
`rhnreg_ks` command.

(Bug ID 30366521)

#### Package Conflict Between `usbguard-1.0.0-2.el8.i686` And `usbguard-1.0.0-8.el8.x86_64` on Oracle Linux 8 Upgrades

Beginning with Oracle Linux 8.5, when you upgrade Oracle Linux 8 with both the
`ol8_baseos_latest` and `ol8_appstream` yum repositories
enabled, a conflict between the `usbguard-1.0.0-2.el8.i686` and
`usbguard-1.0.0-8.el8.x86_64` packages occurs.

The following error is produced:

```
Problem: package usbguard-1.0.0-8.el8.x86_64 conflicts with usbguard
provided by usbguard-1.0.0-2.el8.i686
  - cannot install the best candidate for the job
  - problem with installed package usbguard-1.0.0-2.el8.i686
(try to add '--allowerasing' to command line to replace conflicting packages
or '--skip-broken' to skip uninstallable packages or '--nobest' to use not
only best candidate packages)
```

This conflict occurs because in Oracle Linux 8.6 and later releases, the
`usbguard-1.0.0-2.el8.i686` and the
`usbguard-1.0.0-8.el8.x86_64` packages conflict with each other and could no
longer be installed together, unlike in previous Oracle Linux 8 releases.

To work around this issue, remove the
`usbguard-1.0.0-2.el8.i686` package from your
Oracle Linux 8 system prior to upgrading to the current release.

(Bug ID 34097708)

#### Presence of `beignet` Package Could Result in Dependency Issue During An Upgrade

While upgrading a system to the current Oracle Linux 8 release,
you might encounter a dependency issue if the `beignet` package exists on the
system to be upgraded.

This issue exists specifically in cases where you upgrade systems running Oracle Linux 8.2 or
earlier releases to the current Oracle Linux version. In these earlier releases, the
`beginet` package requires earlier versions of the
`clang-libs` package.

However, the `beignet` package is currently not available for Oracle Linux
8.4 and later Oracle Linux 8 releases. Therefore, the issue does not exist for these
cases.

To work around this issue, remove the `beignet` package from the system prior
to upgrading to the current Oracle Linux 8 release.

(Bug ID 31213935)

#### ULN Registration Wizard Not Displayed on First Boot After An Installation

On new
installations of Oracle Linux 8, the ULN registration wizard that presents the options to
register with ULN and to use Oracle Ksplice isn't displayed on first boot.

As an alternative, you can register with ULN after the installation completes. For
instructions, see <https://linux.oracle.com/>.

(Bug ID 29933974)

#### Graphics Controller Requirements for an Installation on an Oracle VM VirtualBox Guest

To successfully
install Oracle Linux 8 on an Oracle VM VirtualBox guest, where the graphical installation
program is used and the default `Server with GUI` environment is selected, you
must set the guest to use the VMSVGA graphics controller and configure the guest with at least
64MB of memory. Otherwise, the graphical display is unable to start correctly.

Beginning with Oracle VM VirtualBox 6.0, the VMSVGA graphics controller is the default
controller for guests running Linux operating systems. This issue is more likely to appear if
install Oracle Linux 8 on an existing guest that was created on an earlier Oracle VM
VirtualBox release. To configure Oracle Linux 8 guests, Oracle recommends that you use Oracle
VM VirtualBox 6.0 or later.

(Bug ID 30004543)

#### `aarch64` Only: Installer Displays Error: 'Failed to set new efi boot target' on Systems With a Multipath-Enabled NVMe Controller

The Oracle Linux 8.7 installer displays the following error on
aarch64 systems that have a multipath-enabled NVMe controller:

```
Failed to set new efi boot target . This is most likely a kernel or firmware bug.
```

To work around this issue, disable native multipath support
for the installation at boot time by adding the
`nvme_core.multipath=N` command-line argument
on the target system.

(Bug IDs 34233800, 34215333, 31758304)

#### Mellanox NIC interface name subject to change after upgrading from RHCK or UEK R6 to UEK R7

During a kernel upgrade of x86\_64 systems from RHCK
or UEK R6 to UEK R7, the `mlx5_core` device name is subject to change, from
`ens2f0` (RHCK or UEK R6) to `ens2f0np0` (UEK R7).

You might encounter this issue if you selected Server With GUI as the
installation profile and under the following circumstances:

- When upgrading an Oracle Linux 8 system that's running RHCK or UEKR6 to UEK R7.
- When upgrading an Oracle Linux 8 system that's running RHCK or UEK R6 to Oracle Linux 9,
  which ships with UEK R7 by default.
- When upgrading an Oracle Linux 8 system that's already running UEK R7 to Oracle Linux 9.

  Note:

  In the case where an Oracle Linux 8 system is already running UEK R7, if you
  previously configured the system to use backward-compatible device names
  (`ens2f0`), you might need to apply the workaround that follows to the
  GRUB configuration after the upgrade to Oracle Linux 9 has completed.

Note that fresh installations of UEK R7 on Oracle Linux 8 and Oracle Linux 9 use
the default naming convention for UEK R7
(`enp2s0f0np0`) by default.

To retain backward-compatible (RHCK) device names for the `mlx5_core`
driver-based network interface card (NIC), perform the following workaround after upgrading to
UEK R7, prior to rebooting the system. We recommended that you back up the existing
`grub.cfg` file before making this change.

1. Edit the `/etc/default/grub` file and
   append the end of the line in the
   `GRUB_CMDLINE_LINUX=` module as follows:

   ```
   GRUB_CMDLINE_LINUX="console=xxxx mlx5_core.expose_pf_phys_port_name=0"
   ```
2. After editing the file, locate the `grub.cfg` file on the system, then
   run the command to update GRUB configuration, as appropriate:

   - On BIOS-based systems, the `grub.cfg` output/target file is typically
     located at `/boot/grub2/grub.cfg` and you would run the following
     command:

     ```
     sudo grub2-mkconfig -o /boot/grub2/grub.cfg
     ```
   - On UEFI-based systems, the `grub.cfg`
     output/target file could be located at
     `/etc/grub2-efi.cfg` or
     `/boot/efi/EFI/redhat/grub.cfg`.
     Depending on the location of the file, you would run one
     of the following commands:

     ```
     sudo grub2-mkconfig -o /etc/grub2-efi.cfg
     ```

     ```
     sudo grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg
     ```
3. Reboot the system for the changes to take effect.

(Bug IDs 34103369, 34145887, 35270018)

#### openssh-askpass Installation Fails on Systems With Locked Channels

On Oracle Linux 8 systems that are locked to the `ol8_u8_baseos_base`
repository, updating the `openssh-askpass` package for Oracle Linux 8.8
might fail because updating the package requires that the system is subscribed to the
`baseos_latest` channel.

To work around this issue, ensure that the system is subscribed to the
`baseos_latest` channel or repository to obtain the latest
`openssh` packages.

If you need to lock the system to the `baseos_base` repository, you must
also lock the `appstream` repository to the one that is provided in the
Oracle Linux 8.8 ISO image. If you intend to lock a system to a particular update
release for a period, consider configuring a mirror of all of the repositories that you
require and schedule system updates appropriately.

Bug 35406432

### Removing `container-selinux` Package Might Also Remove The `selinux-policy-targeted` Package

If you remove the `container-selinux`
package from the system after installing the current Oracle Linux 8 release, the
`selinux-policy-targeted` package might also be removed.

When this problem occurs, you might also see an error message about being unable to load
SELinux policy.

To avoid this issue, use the following syntax with the `dnf remove`
command:

```
sudo dnf remove container-selinux --setopt=exclude=selinux-policy-targeted
```

(Bug ID 32860334)

### Running `dnf update glusterfs-*` Command Fails to Upgrade Previously Installed Packages

If
`glusterfs-*.i686` packages exist on an Oracle Linux 8 system which you then
upgrade to the next update version, running the `dnf update glusterfs*` command
later fails to upgrade GlusterFS packages.

As a workaround, first remove the `glusterfs-*.i686` packages from
the system, and then run the `dnf update glusterfs*` command.

(Bug ID 30279840)

### Updating `libss` Package Might Fail if `libss-devel` Package Is Installed

The `libss` package might fail to update if the
`libss-devel` package is installed on the system.

This issue persists if UEK R6 is enabled. However, after updating the kernel and enabling UEK
R7, the issue is no longer encountered.

However, this issue is fixed in UEK R7. Therefore, to work around this issue, enable the UEK
R7 yum repository or ULN channel, and then install UEK R7. Reboot the system after the
installation.

(Bug ID 32005190)

### ACPI Error Messages Displayed on Dell EMC PowerEdge Server During Boot

During a system
boot of an Intel-based Dell EMC PowerEdge Server, error messages similar to the following
might be displayed if the Dell Active Power Controller (DAPC) setting is enabled in the BIOS:

```
kernel: ACPI Error: No handler for Region [SYSI] (0000000061df8ef3) [IPMI] (20190816/evregion-132)
kernel: ACPI Error: Region IPMI (ID=7) has no handler (20190816/exfldio-265)
kernel: ACPI Error: Aborting method \_SB.PMI0._GHL due to previous error (AE_NOT_EXIST) (20190816/psparse-531)
kernel: ACPI Error: Aborting method \_SB.PMI0._PMC due to previous error (AE_NOT_EXIST) (20190816/psparse-531)
kernel: ACPI Error: AE_NOT_EXIST, Evaluating _PMC (20190816/power_meter-743)
```

To work around this issue, disable the `apci_power_meter` kernel module as
follows:

```
echo "blacklist acpi_power_meter" >> /etc/modprobe.d/hwmon.conf
```

After disabling the `apci_power_meter` kernel
module, reboot the system for the change to take effect.

For environments that do not require the DAPC feature, as an
alternative workaround, you can disable the DAPC BIOS setting.

(Bug ID 32105233)

### Oracle Linux 8 Doesn't Recognize SAS Controllers on Older Oracle Sun Hardware

The Oracle Linux 8
installer does not recognize some Serial Attached SCSI (SAS) controllers that are found in
older Oracle Sun server models. If you attempt to install Oracle Linux 8 on these server
models, the installer does not recognize the local disk and the installation fails. Examples
of these server models include, but are not limited to, the following: Oracle Sun Fire X4170
M2 Server, Oracle Sun Fire X4170 M3 Server, Oracle Sun OVCA X3-2 Server, and the Oracle Sun
X4-2 Server.

The following SAS controllers are removed from the
`mpt2sas` driver in RHCK:

- SAS2004, PCI ID 0x1000:0x0070
- SAS2008, PCI ID 0x1000:0x0072
- SAS2108\_1, PCI ID 0x1000:0x0074
- SAS2108\_2, PCI ID 0x1000:0x0076
- SAS2108\_3, PCI ID 0x1000:0x0077
- SAS2116\_1, PCI ID 0x1000:0x0064
- SAS2116\_2, PCI ID 0x1000:0x0065
- SSS6200, PCI ID 0x1000:0x007E

The following SAS controllers are removed from the
`megaraid_sas` driver in RHCK:

- Dell PERC5, PCI ID 0x1028:0x15
- SAS1078R, PCI ID 0x1000:0x60
- SAS1078DE, PCI ID 0x1000:0x7C
- SAS1064R, PCI ID 0x1000:0x411
- VERDE\_ZCR, PCI ID 0x1000:0x413
- SAS1078GEN2, PCI ID 0x1000:0x78
- SAS0079GEN2, PCI ID 0x1000:0x79
- SAS0073SKINNY, PCI ID 0x1000:0x73
- SAS0071SKINNY, PCI ID 0x1000:0x71

The workaround for this issue to use the Unbreakable Enterprise Kernel Release 6 (UEK R6) boot
ISO, and then run UEK R6 with Oracle Linux 8, as these controllers are
supported in the Unbreakable Enterprise Kernel release.

(Bug ID 29120478)

### File System Issues

The following are known file systems issues that have been
encountered in this release of Oracle Linux 8.

#### BTRFS File System Not Supported on RHCK

The Btrfs file system is removed from RHCK in Oracle Linux 8, which
means you cannot create or mount this file system when using
this kernel. Also, any Btrfs user space packages that are
provided are not supported with RHCK.

Support for the Btrfs file system is enabled in UEK R7 and
UEK R6. Starting with Oracle Linux 8.3, during an installation, you
have the option to create a Btrfs root file system, as well as
select Btrfs as the file system type when formatting devices.

For further details about these changes, see the following
documentation:

- For information about creating a Btrfs root file system
  during an installation, see [Oracle Linux 8: Installing Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/8/install/).
- For information about managing the Btrfs file system, see
  [Oracle Linux 8: Managing Local File Systems](https://docs.oracle.com/en/operating-systems/oracle-linux/8/fsadmin/).
- For the latest information about other enhancements that
  have been made to Btrfs in UEK R6, see
  [Unbreakable Enterprise Kernel Release 6 Update 3:
  Release Notes (5.4.17-2136)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.3/).

  For information about UEK R7, see
  [Unbreakable Enterprise Kernel Release 7: Release
  Notes (5.15.0-0.30)](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/).

#### OCFS2 File System Not Supported on RHCK

The OCFS2 file system is removed from RHCK in Oracle Linux 8, which
means you cannot create or mount this file system when using
this kernel. Also, OCFS2 user space packages that are provided
are not supported with RHCK.

Note that support for OCFS2 file systems is enabled in UEK R7
and UEK R6. For the latest information and other enhancements
that have been made to OCFS2 in UEK R6, see
[Unbreakable Enterprise Kernel Release 6 Update 3:
Release Notes (5.4.17-2136)](https://docs.oracle.com/en/operating-systems/uek/6/relnotes6.3/). See also [Unbreakable Enterprise Kernel Release 7: Release
Notes (5.15.0-0.30)](https://docs.oracle.com/en/operating-systems/uek/7/relnotes7.0/).

#### `ext4`: Frequent or Repeated System Shutdowns Can Cause File System Corruption

If a system that is using the `ext4` file system is repeatedly or frequently
shut down, the file system might become corrupted. This issue is difficult to replicate and is
therefore considered to be a corner-case issue. The issue exists in the upstream code and
proposed patches are currently under review.

(Bug ID 27547113)

#### Systems With Btrfs Fail to Boot in FIPS Mode

When booted in FIPS mode, a system using Btrfs fails with the following message:

```
FATAL: FIPS integrity test failed
Refusing to continue
```

Bug ID 36028061

### Kernel Issues

The following are known kernel issues that have been encountered
in this release of Oracle Linux 8.

#### KVM Guests Boot With "amd64\_edac\_mod: Unknown symbol" Errors on AMD 64-Bit Platforms

The following errors might be displayed repeatedly when KVM
guests are booting on 64-bit AMD hosts:

```
[   12.474069] amd64_edac_mod: Unknown symbol amd_register_ecc_decoder (err [ 120)
[   12.474083] amd64_edac_mod: Unknown symbol amd_report_gart_errors (err 0)
[   12.852250] amd64_edac_mod: Unknown symbol amd_unregister_ecc_decoder (err 0)
[   12.852297] amd64_edac_mod: Unknown symbol amd_register_ecc_decoder (err 0)
.
.
.
```

These errors occur because the module code for the kernel
erroneously returns `-EEXIST` for modules
that failed to load and are in the process of being removed
from the module list. The `amd64_edac_mod`
module will not be loaded in a VM. These errors can be
ignored, as they do not impact functionality in any way.

This issue occurs on Oracle Linux 8 hosts that are running RHCK only and is not
encountered on UEK R6 hosts.

(Bug ID 29853602)

#### Output of `modinfo` Command Doesn't Show Retpoline Support

A bug in the
Oracle Linux 8 code causes Retropline support to not be displayed in the output of the
`modinfo -F retpoline` command, even though the
`CONFIG_RETPOLINE` flag is set to `Y`, for example:

```
sudo modinfo -F retpoline
/usr/lib/modules/4.18.0-80.el8.x86_64/kernel/sound/usb/usx2y/snd-usb-us122l.ko
.xz
```

The `CONFIG_RETPOLINE=Y` flag is still
required to add and display Retpoline support. If the
parameter is enabled, the kernel builds with a retpoline
capable compiler.

To confirm that the `CONFIG_RETPOLINE` flag is enabled, search
for the parameter in the kernel's `config-kernel`
configuration file, for example:

```
cat /boot/config-5.4.17-2011.7.4.el8uek.x86_64 | grep RETPOLINE.
```

```
CONFIG_RETPOLINE=y
```

(Bug ID 29894295)

#### Kdump Might Fail on Some AMD Hardware

Kdump might fail on some AMD hardware that is running the current Oracle
Linux release. Impacted hardware includes the AMD EPYC CPU servers.

To work around this issue, modify the `/etc/sysconfig/kdump` configuration
file and remove the `iommu=off` command-line option from the
`KDUMP_COMMANDLINE_APPEND` variable. Restart the `kdump`
service for the changes to take effect.

(Bug ID 31274238, 34312626)

#### Kdump Fails to Generate a `vmcore` on FIPS Enabled System

When FIPS mode is enabled on a system, Kdump might fail to generate a `vmcore`
when a system panic is triggered. The issue is caused if the Kdump initramfs image isn't also
regenerated with FIPS mode enabled.

To resolve the issue, if FIPS mode is enabled on the system you must rebuild the Kdump
initramfs image and restart the `kdump` service. The Kdump initramfs image is
automatically rebuilt when the `kdump` service is restarted if
`/etc/kdump.conf` is changed in any
way.

```
sudo touch /etc/kdump.conf
sudo systemctl restart kdump
```

You can verify that Kdump is working correctly by running:

```
sudo systemctl status kdump
```

Check that the service is active and that a new image file was created by ensuring that the
date and timestamp for the Kdump initramfs image corresponds with the date and time when you
restarted the service:

```
ls -lah /etc/kdump.conf /boot/initramfs-$(uname -r)kdump.img
```

(Bug 35982140)

#### Limitations of the LVM `dm-writecache` Caching Method

The new LVM
`dm-writecache` caching method has certain limitations that don't exist with
the `dm-cache` method, including the following:

- Can't attach or detach `dm-writecache` when a logical volume is active.
- Can't take a snapshot of a logical volume when the logical volume is using
  `dm-writecache`.
- Must use a `dm-writecache` block size
  that matches the existing file system block size when
  attaching `dm-writecache` to an inactive
  logical volume.
- Can't resize a logical volume when `dm-writecache` is attached to the
  volume.
- Can't use `pvmove` commands on devices that are used with
  `dm-writecache`.
- Can't use logical volumes with `dm-writecache` when using thin pools or
  the virtual data optimizer (VDO).

For more information about the `dm-writecache` caching method, see the File
Systems and Storage features section of [Oracle Linux 8: Release Notes for Oracle Linux
8.2](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.2/). See
also the `lvmcache(7)` manual page.

### Error: "mcelog service does not support this processor"

An error indicating that the
`mcelog` service doesn't support the processor can appear in the system
log on systems with AMD processors, such as some Oracle Server hardware. The message might be
displayed as follows:

```
mcelog: ERROR: AMD Processor family
23: mcelog does not support this processor.  Please use the edac_mce_amd
module instead.
```

The `mcelog` daemon is a service that is used on x86\_64 platforms to
log and handle hardware error messaging. However, on AMD systems, the
`edac_mce_amd` kernel module handles machine exception logging. AMD systems
do not require the `mcelog` daemon. Therefore, the `mcelog`
error on these systems can be disregarded.

(Bug ID 29501190)

### Power Button Defaults to ACPI Suspend Mode

By default, the Oracle Linux 8 graphical user interface (GUI) console
mode treats the hardware power button as the equivalent of the
ACPI "Sleep" button, which puts the system into low-power sleep
mode. This behavior is specific to the GNOME desktop
environment.

In previous Oracle Linux releases, the hardware power button initiated a
system shutdown. To ensure that Oracle Linux 8 behaves the same way, do
the following:

1. Create a file named
   `/etc/dconf/db/local.d/01-shutdown-button-action`
   with following content:

   ```
   [org/gnome/settings-daemon/plugins/power]
   power-button-action='interactive'
   ```
2. Create a file named
   `/etc/dconf/db/local.d/locks/01-power` with
   the following content:

   ```
   /org/gnome/settings-daemon/plugins/power/power-button-action
   ```
3. Run the following command:

   ```
   sudo dconf update
   ```
4. Log out of the desktop environment and then log back in for
   the new settings to take effect.

(Bug ID 25597898)

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

### (aarch64) Some GUI Elements Aren't Displayed During Installation and Boot Using VGA Output

During installations on the Arm platform, the Oracle Linux installer does not display some
GUI elements, such as the progress update screen, on VGA output. Output is displayed on the
serial console, instead.

Additionally, if you install Oracle Linux with GUI on an encrypted disk, for example, by
choosing Server with GUI during the installation stage, and VGA is enabled,
the password prompt doesn't appear on the VGA output at system boot, and
consequently, the boot process can not be completed. The prompt appears only
on a serial console, and therefore, you would need to switch to a serial
console to provide the password there.

This issue is specific to systems on the Arm platform only and occurs regardless of whether
you are using secure boot or non secure boot. Further, the issue applies to Oracle Linux 8 or
Oracle Linux 9 systems that use UEKR6 or UEKR7. The issue occurs wherever Plymouth graphical
elements are loaded in the GUI.

To resolve these GUI issues and to cause these elements to display on VGA output without
using a serial console, add `plymouth.ignore-serial-consoles`
to the kernel command line in the GRUB configuration. For instructions, see
the Managing Kernels and System Boot chapter in [Oracle Linux 8: Managing Core System Configuration](https://docs.oracle.com/en/operating-systems/oracle-linux/8/osmanage/).

(Bug ID 35034465 and 35270637)

### Virtual Function MAC Address Differences With Host After VF Migration

On some VF hardware, after a VF migration, the MAC address of the VF might be different
from the MAC address of the destination host, unless you preset the destination host's
address on the VF guest before starting the migration. When migration is completed, the
guest and host MAC addresses match without requiring a guest reboot.

As an alternative to presetting the address, reboot the guest after migration to synchronize
the guest VF's MAC address with that of the destination host.

(Bug ID 35508407)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.9/ol8-PackageChangesfromtheUpstreamRelease.html -->

The following sections list the changes to binary and source
packages from the upstream release.

### Changes to Binary Packages

This section contains information about the removed, modified, and new binary packages in this release. For information about the source package changes, see [Changes to Source Packages](ol8-PackageChangesfromtheUpstreamRelease.html#ol8-packages-source) .

#### Added Binary Packages for BaseOS by Oracle

The following binary packages have been added to BaseOS by Oracle:

- `bcache-tools`
- `btrfs-progs`
- `dtrace`
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
- `linux-firmware-core`
- `NetworkManager-config-connectivity-oracle`
- `ocfs2-tools`
- `oracle-backgrounds`
- `oracle-indexhtml`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`
- `oracle-logos-httpd`
- `oracle-logos-ipa`

#### Added Binary Packages for AppStream by Oracle:

The following binary packages have been added to AppStream by Oracle:

- `dtrace-devel`
- `dtrace-testsuite`
- `libblockdev-btrfs`
- `oracle-database-preinstall-21c`
- `python3-dnf-plugin-ulninfo`

#### Added Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages have been added to CodeReady Linux Builder by Oracle:

- `qemu-kvm-tests`
- `shim-unsigned-ia32`

#### Modified BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been modified:

- `autofs`
- `binutils`
- `biosdevname`
- `boom-boot`
- `boom-boot-conf`
- `boom-boot-grub2`
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
- `dbus-daemon`
- `dbus-libs`
- `dbus-tools`
- `dbxtool`
- `device-mapper`
- `device-mapper-event`
- `device-mapper-event-libs`
- `device-mapper-libs`
- `dnf`
- `dnf-automatic`
- `dnf-data`
- `dnf-plugins-core`
- `dracut`
- `dracut-caps`
- `dracut-config-generic`
- `dracut-config-rescue`
- `dracut-live`
- `dracut-network`
- `dracut-squash`
- `dracut-tools`
- `efibootmgr`
- `efi-filesystem`
- `expat`
- `expat-devel`
- `firewalld`
- `firewalld-filesystem`
- `fuse`
- `fuse3`
- `fuse3-devel`
- `fuse3-libs`
- `fuse-common`
- `fuse-devel`
- `fuse-libs`
- `fwupd`
- `fwupdate`
- `fwupdate-efi`
- `fwupdate-libs`
- `glibc`
- `glibc-all-langpacks`
- `glibc-common`
- `glibc-devel`
- `glibc-doc`
- `glibc-gconv-extra`
- `glibc-headers`
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
- `glibc-locale-source`
- `glibc-minimal-langpack`
- `grub2-common`
- `grub2-efi-aa64-modules`
- `grub2-efi-ia32`
- `grub2-efi-ia32-cdboot`
- `grub2-efi-ia32-modules`
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
- `iptables`
- `iptables-arptables`
- `iptables-devel`
- `iptables-ebtables`
- `iptables-libs`
- `iptables-services`
- `iptables-utils`
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
- `kmod-redhat-oracleasm`
- `krb5-devel`
- `krb5-libs`
- `krb5-pkinit`
- `krb5-server`
- `krb5-server-ldap`
- `krb5-workstation`
- `ksc`
- `libasan`
- `libatomic`
- `libatomic-static`
- `libblkid`
- `libblkid-devel`
- `libdb`
- `libdb-utils`
- `libdnf`
- `libertas-sd8686-firmware`
- `libertas-sd8787-firmware`
- `libertas-usb8388-firmware`
- `libertas-usb8388-olpc-firmware`
- `libfdisk`
- `libfdisk-devel`
- `libgcc`
- `libgfortran`
- `libgomp`
- `libgomp-offload-nvptx`
- `libipa_hbac`
- `libitm`
- `libkadm5`
- `libkcapi`
- `libkcapi-hmaccalc`
- `liblsan`
- `libmount`
- `libnsl`
- `libquadmath`
- `libreport-filesystem`
- `libsmartcols`
- `libsmartcols-devel`
- `libsss_autofs`
- `libsss_certmap`
- `libsss_idmap`
- `libsss_nss_idmap`
- `libsss_simpleifp`
- `libsss_sudo`
- `libstdc++`
- `libtsan`
- `libubsan`
- `libuuid`
- `libuuid-devel`
- `libxslt`
- `libzstd`
- `libzstd-devel`
- `linux-firmware`
- `linux-firmware-core`
- `lvm2`
- `lvm2-dbusd`
- `lvm2-libs`
- `lvm2-lockd`
- `mcelog`
- `mdadm`
- `microcode_ctl`
- `mokutil`
- `mozjs52`
- `mozjs60`
- `netconsole-service`
- `net-snmp-libs`
- `NetworkManager`
- `NetworkManager-adsl`
- `NetworkManager-bluetooth`
- `NetworkManager-config-connectivity-oracle`
- `NetworkManager-config-server`
- `NetworkManager-dispatcher-routing-rules`
- `NetworkManager-initscripts-updown`
- `NetworkManager-libnm`
- `NetworkManager-ovs`
- `NetworkManager-ppp`
- `NetworkManager-team`
- `NetworkManager-tui`
- `NetworkManager-wifi`
- `NetworkManager-wwan`
- `network-scripts`
- `nscd`
- `nss_db`
- `ntsysv`
- `nvme-cli`
- `nvmetcli`
- `opa-address-resolution`
- `opa-basic-tools`
- `opa-fastfabric`
- `opa-fm`
- `opa-libopamgt`
- `OpenIPMI`
- `OpenIPMI-lanserv`
- `OpenIPMI-libs`
- `OpenIPMI-perl`
- `os-prober`
- `parted`
- `platform-python`
- `policycoreutils`
- `policycoreutils-dbus`
- `policycoreutils-devel`
- `policycoreutils-newrole`
- `policycoreutils-python-utils`
- `policycoreutils-restorecond`
- `polkit`
- `polkit-devel`
- `polkit-docs`
- `polkit-libs`
- `procps-ng`
- `procps-ng-i18n`
- `python3-boom`
- `python3-configshell`
- `python3-dnf`
- `python3-dnf-plugin-post-transaction-actions`
- `python3-dnf-plugins-core`
- `python3-dnf-plugin-versionlock`
- `python3-firewall`
- `python3-hawkey`
- `python3-iscsi-initiator-utils`
- `python3-libdnf`
- `python3-libipa_hbac`
- `python3-libs`
- `python3-libsss_nss_idmap`
- `python3-openipmi`
- `python3-policycoreutils`
- `python3-rtslib`
- `python3-sss`
- `python3-sssdconfig`
- `python3-sss-murmur`
- `python3-test`
- `rasdaemon`
- `readonly-root`
- `redhat-release`
- `sanlock-lib`
- `selinux-policy`
- `selinux-policy-devel`
- `selinux-policy-doc`
- `selinux-policy-minimum`
- `selinux-policy-mls`
- `selinux-policy-sandbox`
- `selinux-policy-targeted`
- `shim-ia32`
- `shim-x64`
- `sos`
- `sos-audit`
- `sqlite`
- `sqlite-devel`
- `sqlite-doc`
- `sqlite-libs`
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
- `systemd-devel`
- `systemd-journal-remote`
- `systemd-libs`
- `systemd-pam`
- `systemd-tests`
- `systemd-udev`
- `target-restore`
- `trace-cmd`
- `tuned`
- `tuned-profiles-atomic`
- `tuned-profiles-compat`
- `tuned-profiles-cpu-partitioning`
- `tuned-profiles-mssql`
- `tuned-profiles-oracle`
- `unzip`
- `util-linux`
- `util-linux-user`
- `uuidd`
- `vim-minimal`
- `yum`
- `yum-utils`

#### Modified Binary Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `anaconda-widgets-devel`
- `crash-devel`
- `cups-filters-devel`
- `dconf-devel`
- `device-mapper-devel`
- `device-mapper-event-devel`
- `dotnet-sdk-3.1-source-built-artifacts`
- `dotnet-sdk-5.0-source-built-artifacts`
- `dotnet-sdk-6.0-source-built-artifacts`
- `dotnet-sdk-7.0-source-built-artifacts`
- `fwupd-devel`
- `galera`
- `gcc-plugin-devel`
- `gcc-toolset-10-gcc-plugin-devel`
- `glibc-benchtests`
- `glibc-nss-devel`
- `glibc-static`
- `guile-devel`
- `iscsi-initiator-utils-devel`
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
- `java-1.8.0-openjdk-accessibility-fastdebug`
- `java-1.8.0-openjdk-accessibility-slowdebug`
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
- `Judy`
- `Judy-devel`
- `kmod-devel`
- `libblockdev-crypto-devel`
- `libblockdev-devel`
- `libblockdev-fs-devel`
- `libblockdev-loop-devel`
- `libblockdev-lvm-devel`
- `libblockdev-mdraid-devel`
- `libblockdev-part-devel`
- `libblockdev-swap-devel`
- `libblockdev-utils-devel`
- `libblockdev-vdo-devel`
- `libcephfs2`
- `libcephfs-devel`
- `libdb-cxx`
- `libdb-cxx-devel`
- `libdb-devel-doc`
- `libdb-sql`
- `libdb-sql-devel`
- `libdnf-devel`
- `librados-devel`
- `libradosstriper1`
- `libradosstriper-devel`
- `librbd-devel`
- `libreoffice-sdk`
- `libreoffice-sdk-doc`
- `libsss_nss_idmap-devel`
- `libstdc++-static`
- `libvirt`
- `libvirt-client`
- `libvirt-daemon`
- `libvirt-daemon-config-network`
- `libvirt-daemon-config-nwfilter`
- `libvirt-daemon-driver-interface`
- `libvirt-daemon-driver-network`
- `libvirt-daemon-driver-nodedev`
- `libvirt-daemon-driver-nwfilter`
- `libvirt-daemon-driver-secret`
- `libvirt-daemon-driver-storage`
- `libvirt-daemon-driver-storage-core`
- `libvirt-daemon-driver-storage-disk`
- `libvirt-daemon-driver-storage-iscsi`
- `libvirt-daemon-driver-storage-iscsi-direct`
- `libvirt-daemon-driver-storage-logical`
- `libvirt-daemon-driver-storage-mpath`
- `libvirt-daemon-driver-storage-scsi`
- `libvirt-devel`
- `libvirt-docs`
- `libvirt-libs`
- `libvirt-nss`
- `libvirt-wireshark`
- `lvm2-devel`
- `mariadb`
- `mariadb-backup`
- `mariadb-common`
- `mariadb-devel`
- `mariadb-embedded`
- `mariadb-embedded-devel`
- `mariadb-errmsg`
- `mariadb-gssapi-server`
- `mariadb-oqgraph-engine`
- `mariadb-server`
- `mariadb-server-galera`
- `mariadb-server-utils`
- `mariadb-test`
- `mozjs52-devel`
- `mozjs60-devel`
- `NetworkManager-libnm-devel`
- `nss_hesiod`
- `ocaml-libguestfs`
- `ocaml-libguestfs-devel`
- `OpenIPMI-devel`
- `openscap-engine-sce-devel`
- `PackageKit`
- `PackageKit-glib-devel`
- `parted-devel`
- `procps-ng-devel`
- `sanlock-devel`
- `sblim-cmpi-devel`
- `sendmail-milter-devel`
- `tog-pegasus-devel`

#### Modified AppStream Binary Packages

The following binary packages from the AppStream upstream release have been modified:

- `aardvark-dns`
- `abrt`
- `abrt-addon-ccpp`
- `abrt-addon-coredump-helper`
- `abrt-addon-kerneloops`
- `abrt-addon-pstoreoops`
- `abrt-addon-vmcore`
- `abrt-addon-xorg`
- `abrt-cli`
- `abrt-cli-ng`
- `abrt-console-notification`
- `abrt-dbus`
- `abrt-desktop`
- `abrt-gui`
- `abrt-gui-libs`
- `abrt-java-connector`
- `abrt-libs`
- `abrt-plugin-machine-id`
- `abrt-plugin-sosreport`
- `abrt-tui`
- `adwaita-gtk2-theme`
- `anaconda`
- `anaconda-core`
- `anaconda-dracut`
- `anaconda-gui`
- `anaconda-install-env-deps`
- `anaconda-tui`
- `anaconda-user-help`
- `anaconda-widgets`
- `ansible-pcp`
- `aspnetcore-runtime-3.0`
- `aspnetcore-runtime-3.1`
- `aspnetcore-runtime-5.0`
- `aspnetcore-runtime-6.0`
- `aspnetcore-runtime-7.0`
- `aspnetcore-targeting-pack-3.0`
- `aspnetcore-targeting-pack-3.1`
- `aspnetcore-targeting-pack-5.0`
- `aspnetcore-targeting-pack-6.0`
- `aspnetcore-targeting-pack-7.0`
- `authd`
- `autocorr-af`
- `autocorr-bg`
- `autocorr-ca`
- `autocorr-cs`
- `autocorr-da`
- `autocorr-de`
- `autocorr-en`
- `autocorr-es`
- `autocorr-fa`
- `autocorr-fi`
- `autocorr-fr`
- `autocorr-ga`
- `autocorr-hr`
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
- `autocorr-zh`
- `binutils-devel`
- `blivet-data`
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
- `compat-libpthread-nonshared`
- `composer-cli`
- `containernetworking-plugins`
- `containers-common`
- `cpp`
- `crash`
- `cups-filters`
- `cups-filters-libs`
- `dbus-devel`
- `dbus-x11`
- `dconf`
- `delve`
- `dnf-plugin-spacewalk`
- `dotnet`
- `dotnet-apphost-pack-3.0`
- `dotnet-apphost-pack-3.1`
- `dotnet-apphost-pack-5.0`
- `dotnet-apphost-pack-6.0`
- `dotnet-apphost-pack-7.0`
- `dotnet-host`
- `dotnet-hostfxr-3.0`
- `dotnet-hostfxr-3.1`
- `dotnet-hostfxr-5.0`
- `dotnet-hostfxr-6.0`
- `dotnet-hostfxr-7.0`
- `dotnet-runtime-3.0`
- `dotnet-runtime-3.1`
- `dotnet-runtime-5.0`
- `dotnet-runtime-6.0`
- `dotnet-runtime-7.0`
- `dotnet-sdk-3.0`
- `dotnet-sdk-3.1`
- `dotnet-sdk-5.0`
- `dotnet-sdk-6.0`
- `dotnet-sdk-7.0`
- `dotnet-targeting-pack-3.0`
- `dotnet-targeting-pack-3.1`
- `dotnet-targeting-pack-5.0`
- `dotnet-targeting-pack-6.0`
- `dotnet-targeting-pack-7.0`
- `dotnet-templates-3.0`
- `dotnet-templates-3.1`
- `dotnet-templates-5.0`
- `dotnet-templates-6.0`
- `dotnet-templates-7.0`
- `eclipse-ecf-core`
- `eclipse-ecf-runtime`
- `eclipse-emf-core`
- `eclipse-emf-runtime`
- `eclipse-emf-xsd`
- `eclipse-equinox-osgi`
- `eclipse-jdt`
- `eclipse-p2-discovery`
- `eclipse-pde`
- `eclipse-platform`
- `eclipse-swt`
- `efi-srpm-macros`
- `fapolicyd`
- `fapolicyd-selinux`
- `firefox`
- `firewall-applet`
- `firewall-config`
- `gcc`
- `gcc-c++`
- `gcc-gdb-plugin`
- `gcc-gfortran`
- `gcc-offload-nvptx`
- `gcc-plugin-annobin`
- `gcc-toolset-10-gcc`
- `gcc-toolset-10-gcc-c++`
- `gcc-toolset-10-gcc-gdb-plugin`
- `gcc-toolset-10-gcc-gfortran`
- `gcc-toolset-10-libasan-devel`
- `gcc-toolset-10-libatomic-devel`
- `gcc-toolset-10-libitm-devel`
- `gcc-toolset-10-liblsan-devel`
- `gcc-toolset-10-libquadmath-devel`
- `gcc-toolset-10-libstdc++-devel`
- `gcc-toolset-10-libstdc++-docs`
- `gcc-toolset-10-libtsan-devel`
- `gcc-toolset-10-libubsan-devel`
- `gcc-toolset-11-binutils`
- `gcc-toolset-11-binutils-devel`
- `gcc-toolset-11-gcc`
- `gcc-toolset-11-gcc-c++`
- `gcc-toolset-11-gcc-gdb-plugin`
- `gcc-toolset-11-gcc-gfortran`
- `gcc-toolset-11-gcc-plugin-devel`
- `gcc-toolset-11-gdb`
- `gcc-toolset-11-gdb-doc`
- `gcc-toolset-11-gdb-gdbserver`
- `gcc-toolset-11-libasan-devel`
- `gcc-toolset-11-libatomic-devel`
- `gcc-toolset-11-libgccjit`
- `gcc-toolset-11-libgccjit-devel`
- `gcc-toolset-11-libgccjit-docs`
- `gcc-toolset-11-libitm-devel`
- `gcc-toolset-11-liblsan-devel`
- `gcc-toolset-11-libquadmath-devel`
- `gcc-toolset-11-libstdc++-devel`
- `gcc-toolset-11-libstdc++-docs`
- `gcc-toolset-11-libtsan-devel`
- `gcc-toolset-11-libubsan-devel`
- `gcc-toolset-12-gdb`
- `gdb`
- `gdb-doc`
- `gdb-gdbserver`
- `gdb-headless`
- `git-clang-format`
- `glibc-utils`
- `gnome-boxes`
- `gnome-session`
- `gnome-session-kiosk-session`
- `gnome-session-wayland-session`
- `gnome-session-xsession`
- `gnome-themes-standard`
- `guile`
- `httpd`
- `httpd-devel`
- `httpd-filesystem`
- `httpd-manual`
- `httpd-tools`
- `icedtea-web`
- `icedtea-web-javadoc`
- `idm-pki-acme`
- `idm-pki-base`
- `idm-pki-base-java`
- `idm-pki-ca`
- `idm-pki-kra`
- `idm-pki-server`
- `idm-pki-symkey`
- `idm-pki-tools`
- `initial-setup`
- `initial-setup-gui`
- `ipa-client`
- `ipa-client-common`
- `ipa-client-epn`
- `ipa-client-samba`
- `ipa-common`
- `ipa-python-compat`
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
- `java-1.8.0-openjdk-accessibility`
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
- `Judy`
- `kernel-rpm-macros`
- `kernelshark`
- `ksh`
- `leapp`
- `leapp-deps`
- `leapp-upgrade-el8toel9`
- `leapp-upgrade-el8toel9-deps`
- `lemon`
- `libasan6`
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
- `libblockdev-utils`
- `libblockdev-vdo`
- `libcmpiCppImpl0`
- `libdb-devel`
- `libguestfs`
- `libguestfs-appliance`
- `libguestfs-bash-completion`
- `libguestfs-devel`
- `libguestfs-gfs2`
- `libguestfs-gobject`
- `libguestfs-gobject-devel`
- `libguestfs-inspect-icons`
- `libguestfs-java`
- `libguestfs-java-devel`
- `libguestfs-javadoc`
- `libguestfs-man-pages-ja`
- `libguestfs-man-pages-uk`
- `libguestfs-rescue`
- `libguestfs-rsync`
- `libguestfs-tools`
- `libguestfs-tools-c`
- `libguestfs-xfs`
- `libitm-devel`
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
- `libreoffice-langpack-es`
- `libreoffice-langpack-et`
- `libreoffice-langpack-eu`
- `libreoffice-langpack-fa`
- `libreoffice-langpack-fi`
- `libreoffice-langpack-fr`
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
- `libreport-newt`
- `libreport-plugin-bugzilla`
- `libreport-plugin-kerneloops`
- `libreport-plugin-logger`
- `libreport-plugin-mailx`
- `libreport-plugin-reportuploader`
- `libreport-plugin-ureport`
- `libreport-web`
- `libreswan`
- `libstdc++-devel`
- `libstdc++-docs`
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
- `libvirt-daemon-driver-storage-gluster`
- `libvirt-daemon-driver-storage-iscsi`
- `libvirt-daemon-driver-storage-iscsi-direct`
- `libvirt-daemon-driver-storage-logical`
- `libvirt-daemon-driver-storage-mpath`
- `libvirt-daemon-driver-storage-rbd`
- `libvirt-daemon-driver-storage-scsi`
- `libvirt-daemon-kvm`
- `libvirt-devel`
- `libvirt-docs`
- `libvirt-libs`
- `libvirt-lock-sanlock`
- `libvirt-nss`
- `libvirt-wireshark`
- `libxslt-devel`
- `llvm`
- `llvm-devel`
- `llvm-doc`
- `llvm-googletest`
- `llvm-libs`
- `llvm-static`
- `llvm-test`
- `llvm-toolset`
- `lorax`
- `lorax-composer`
- `lorax-lmc-novirt`
- `lorax-lmc-virt`
- `lorax-templates-generic`
- `lorax-templates-rhel`
- `lua-guestfs`
- `mecab-ipadic`
- `mecab-ipadic-EUCJP`
- `mod_ldap`
- `mod_proxy_html`
- `mod_session`
- `mod_ssl`
- `netavark`
- `net-snmp`
- `net-snmp-agent-libs`
- `net-snmp-devel`
- `net-snmp-perl`
- `net-snmp-utils`
- `netstandard-targeting-pack-2.1`
- `NetworkManager-cloud-setup`
- `nginx`
- `nginx-all-modules`
- `nginx-filesystem`
- `nginx-mod-devel`
- `nginx-mod-http-image-filter`
- `nginx-mod-http-perl`
- `nginx-mod-http-xslt-filter`
- `nginx-mod-mail`
- `nginx-mod-stream`
- `npm`
- `openchange`
- `openscap`
- `openscap-devel`
- `openscap-engine-sce`
- `openscap-python3`
- `openscap-scanner`
- `openscap-utils`
- `open-vm-tools`
- `open-vm-tools-desktop`
- `open-vm-tools-salt-minion`
- `open-vm-tools-sdmp`
- `osinfo-db`
- `pacemaker-cluster-libs`
- `pacemaker-libs`
- `pacemaker-schemas`
- `PackageKit`
- `PackageKit-command-not-found`
- `PackageKit-cron`
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
- `perl-PCP-LogImport`
- `perl-PCP-LogSummary`
- `perl-PCP-MMV`
- `perl-PCP-PMDA`
- `perl-Sys-Guestfs`
- `perl-XML-Parser`
- `pesign`
- `platform-python`
- `platform-python-debug`
- `platform-python-devel`
- `plymouth`
- `plymouth-core-libs`
- `plymouth-graphics-libs`
- `plymouth-plugin-fade-throbber`
- `plymouth-plugin-label`
- `plymouth-plugin-script`
- `plymouth-plugin-space-flares`
- `plymouth-plugin-throbgress`
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
- `podman-remote`
- `podman-tests`
- `policycoreutils-gui`
- `policycoreutils-sandbox`
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
- `python2`
- `python2-debug`
- `python2-devel`
- `python2-libs`
- `python2-test`
- `python2-tkinter`
- `python2-tools`
- `python3-abrt`
- `python3-abrt-addon`
- `python3-abrt-container-addon`
- `python3-abrt-doc`
- `python3-blivet`
- `python3-blockdev`
- `python3-clang`
- `python3-dnf-plugin-modulesync`
- `python3-dnf-plugin-spacewalk`
- `python3-idle`
- `python3-idm-pki`
- `python3-ipaclient`
- `python3-ipalib`
- `python3-ipaserver`
- `python3-ipatests`
- `python3-kickstart`
- `python3-leapp`
- `python3-libguestfs`
- `python3-libmount`
- `python3-libreport`
- `python3-pcp`
- `python3-rhncfg`
- `python3-rhncfg-actions`
- `python3-rhncfg-client`
- `python3-rhncfg-management`
- `python3-rhn-check`
- `python3-rhn-client-tools`
- `python3-rhnlib`
- `python3-rhnpush`
- `python3-rhn-setup`
- `python3-rhn-setup-gnome`
- `python3-rhn-virtualization-common`
- `python3-rhn-virtualization-host`
- `python3-sanlock`
- `python3-spacewalk-backend-libs`
- `python3-spacewalk-oscap`
- `python3-spacewalk-usix`
- `python3-test`
- `python3-tkinter`
- `rear`
- `redfish-finder`
- `redhat-lsb`
- `redhat-lsb-core`
- `redhat-lsb-cxx`
- `redhat-lsb-desktop`
- `redhat-lsb-languages`
- `redhat-lsb-printing`
- `redhat-lsb-submod-multimedia`
- `redhat-lsb-submod-security`
- `redhat-rpm-config`
- `rhel-system-roles`
- `rhncfg`
- `rhncfg-actions`
- `rhncfg-client`
- `rhncfg-management`
- `rhn-check`
- `rhn-client-tools`
- `rhn-custom-info`
- `rhnlib`
- `rhnpush`
- `rhnsd`
- `rhn-setup`
- `rhn-setup-gnome`
- `rhn-virtualization-host`
- `rpmdevtools`
- `rpmlint`
- `ruby-libguestfs`
- `runc`
- `sanlk-reset`
- `sanlock`
- `scap-security-guide`
- `scap-security-guide-doc`
- `scap-workbench`
- `scl-utils`
- `scl-utils-build`
- `sendmail`
- `sendmail-cf`
- `sendmail-doc`
- `sendmail-milter`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `setroubleshoot-server`
- `skopeo`
- `skopeo-tests`
- `snactor`
- `sos-collector`
- `spacewalk-oscap`
- `spacewalk-remote-utils`
- `spacewalk-usix`
- `spice-streaming-agent`
- `sssd-idp`
- `sysstat`
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
- `thunderbird`
- `tog-pegasus`
- `tog-pegasus-libs`
- `tuned-gtk`
- `tuned-profiles-postgresql`
- `tuned-utils`
- `tuned-utils-systemtap`
- `vim-common`
- `vim-enhanced`
- `vim-filesystem`
- `vim-X11`
- `virt-dib`
- `virt-install`
- `virt-manager`
- `virt-manager-common`
- `virt-p2v-maker`
- `WALinuxAgent`
- `WALinuxAgent-udev`
- `wget`
- `xdg-desktop-portal`
- `xsane`
- `xsane-common`
- `xsane-gimp`
- `zstd`

#### Removed BaseOS Binary Packages

The following binary packages from the BaseOS upstream release have been removed:

- `dnf-plugin-subscription-manager`
- `grub2-ppc64le-modules`
- `kpatch`
- `kpatch-dnf`
- `NetworkManager-config-connectivity-redhat`
- `python3-cloud-what`
- `python3-subscription-manager-rhsm`
- `python3-syspurpose`
- `redhat-indexhtml`
- `redhat-logos`
- `redhat-logos-httpd`
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
- `coreos-installer`
- `coreos-installer-bootinfra`
- `coreos-installer-dracut`
- `insights-client`
- `libreport-plugin-rhtsupport`
- `libreport-rhel`
- `libreport-rhel-anaconda-bugzilla`
- `libreport-rhel-bugzilla`
- `redhat-backgrounds`
- `redhat-cloud-client-configuration`
- `redhat-logos-ipa`
- `redhat-support-lib-python`
- `redhat-support-tool`
- `rhc`
- `rhc-worker-playbook`
- `rhsm-gtk`
- `rt-tests`
- `spice-client-win-x64`
- `spice-client-win-x86`
- `spice-qxl-wddm-dod`
- `spice-vdagent-win-x64`
- `spice-vdagent-win-x86`
- `subscription-manager-initial-setup-addon`
- `subscription-manager-migration`
- `subscription-manager-migration-data`
- `toolbox`
- `toolbox-tests`
- `virtio-win`
- `virt-who`

#### Removed CodeReady Linux Builder Binary Packages

The following binary packages from the CodeReady Linux Builder upstream release have been removed:

- `asio`
- `Cython`
- `Cython-debugsource`
- `galera-debuginfo`
- `galera-debugsource`
- `hivex-debuginfo`
- `hivex-debugsource`
- `Judy-debuginfo`
- `Judy-debugsource`
- `libiscsi-debuginfo`
- `libiscsi-debugsource`
- `libiscsi-utils-debuginfo`
- `libnbd-debuginfo`
- `libnbd-debugsource`
- `libserf-debuginfo`
- `libserf-debugsource`
- `libvirt-client-debuginfo`
- `libvirt-daemon-debuginfo`
- `libvirt-daemon-driver-interface-debuginfo`
- `libvirt-daemon-driver-network-debuginfo`
- `libvirt-daemon-driver-nodedev-debuginfo`
- `libvirt-daemon-driver-nwfilter-debuginfo`
- `libvirt-daemon-driver-secret-debuginfo`
- `libvirt-daemon-driver-storage-core-debuginfo`
- `libvirt-daemon-driver-storage-disk-debuginfo`
- `libvirt-daemon-driver-storage-iscsi-debuginfo`
- `libvirt-daemon-driver-storage-iscsi-direct-debuginfo`
- `libvirt-daemon-driver-storage-logical-debuginfo`
- `libvirt-daemon-driver-storage-mpath-debuginfo`
- `libvirt-daemon-driver-storage-scsi-debuginfo`
- `libvirt-dbus-debuginfo`
- `libvirt-dbus-debugsource`
- `libvirt-debuginfo`
- `libvirt-debugsource`
- `libvirt-libs-debuginfo`
- `libvirt-nss-debuginfo`
- `libvirt-python-debugsource`
- `libvirt-wireshark-debuginfo`
- `mariadb-backup-debuginfo`
- `mariadb-debuginfo`
- `mariadb-debugsource`
- `mariadb-embedded-debuginfo`
- `mariadb-gssapi-server-debuginfo`
- `mariadb-oqgraph-engine-debuginfo`
- `mariadb-server-debuginfo`
- `mariadb-server-utils-debuginfo`
- `mariadb-test-debuginfo`
- `mod_dav_svn-debuginfo`
- `nbdfuse-debuginfo`
- `netcf-debuginfo`
- `netcf-debugsource`
- `netcf-libs-debuginfo`
- `ocaml-hivex-debuginfo`
- `ocaml-libguestfs-debuginfo`
- `ocaml-libnbd-debuginfo`
- `perl-hivex-debuginfo`
- `perl-Sys-Virt-debuginfo`
- `perl-Sys-Virt-debugsource`
- `pybind11`
- `pytest`
- `python39-Cython-debuginfo`
- `python3-hivex-debuginfo`
- `python3-libnbd-debuginfo`
- `python3-libvirt-debuginfo`
- `python3x-pyparsing`
- `python-atomicwrites`
- `python-attrs`
- `python-iniconfig`
- `python-more-itertools`
- `python-packaging`
- `python-pluggy`
- `python-py`
- `python-wcwidth`
- `ruby-hivex-debuginfo`
- `SLOF`
- `subversion-debuginfo`
- `subversion-debugsource`
- `subversion-devel-debuginfo`
- `subversion-gnome-debuginfo`
- `subversion-libs-debuginfo`
- `subversion-perl-debuginfo`
- `subversion-ruby-debuginfo`
- `subversion-tools-debuginfo`
- `utf8proc-debuginfo`
- `utf8proc-debugsource`

### Changes to Source Packages

This section contains information about the removed, modified, and new source packages in this release. For information about the binary package changes, see [Changes to Binary Packages](ol8-PackageChangesfromtheUpstreamRelease.html#ol8-packages-binary) .

#### Added Source Packages for BaseOS by Oracle

The following source packages have been added to the BaseOS by Oracle:

- `bcache-tools`
- `btrfs-progs`
- `dtrace`
- `kernel-uek`
- `ocfs2-tools`
- `oracle-indexhtml`
- `oraclelinux-release`
- `oraclelinux-release-el8`
- `oracle-logos`

#### Added Source Packages for AppStream by Oracle

The following source packages have been added to AppStream by Oracle:

- `dtrace`
- `oracle-database-preinstall-21c`
- `python3-dnf-plugin-ulninfo`

#### Modified BaseOS Source Packages

The following source packages from the BaseOS upstream release have been modified:

- `autofs`
- `binutils`
- `biosdevname`
- `boom-boot`
- `chkconfig`
- `chrony`
- `cockpit`
- `coreutils`
- `dbus`
- `dbxtool`
- `dnf`
- `dnf-plugins-core`
- `dracut`
- `efibootmgr`
- `efi-rpm-macros`
- `expat`
- `firewalld`
- `fuse`
- `fwupd`
- `fwupdate`
- `gcc`
- `glibc`
- `grub2`
- `grubby`
- `initscripts`
- `iptables`
- `iscsi-initiator-utils`
- `kexec-tools`
- `kmod`
- `kmod-kvdo`
- `kmod-redhat-oracleasm`
- `krb5`
- `ksc`
- `libdb`
- `libdnf`
- `libkcapi`
- `libreport`
- `libxslt`
- `linux-firmware`
- `lvm2`
- `mcelog`
- `mdadm`
- `microcode_ctl`
- `mokutil`
- `mozjs52`
- `mozjs60`
- `net-snmp`
- `NetworkManager`
- `nvme-cli`
- `nvmetcli`
- `opa-ff`
- `opa-fm`
- `OpenIPMI`
- `os-prober`
- `parted`
- `policycoreutils`
- `polkit`
- `procps-ng`
- `python3`
- `python-configshell`
- `python-rtslib`
- `rasdaemon`
- `redhat-release`
- `sanlock`
- `selinux-policy`
- `shim`
- `sos`
- `sqlite`
- `sssd`
- `systemd`
- `trace-cmd`
- `tuned`
- `unzip`
- `util-linux`
- `vim`
- `zstd`

#### Modified AppStream Source Packages

The following source packages from the AppStream upstream release have been modified:

- `abrt`
- `abrt-java-connector`
- `anaconda`
- `anaconda-user-help`
- `ansible-pcp`
- `authd`
- `binutils`
- `buildah`
- `ceph`
- `clang`
- `cloud-init`
- `cockpit-appstream`
- `cockpit-composer`
- `cockpit-session-recording`
- `compat-libgfortran-48`
- `containernetworking-plugins`
- `containers-common`
- `crash`
- `cups-filters`
- `dbus`
- `dconf`
- `delve`
- `dnf-plugins-core`
- `dnf-plugin-spacewalk`
- `dotnet3.0`
- `dotnet3.1`
- `dotnet5.0`
- `dotnet6.0`
- `dotnet7.0`
- `eclipse`
- `eclipse-ecf`
- `eclipse-emf`
- `efi-rpm-macros`
- `fapolicyd`
- `firefox`
- `firewalld`
- `gcc`
- `gcc-toolset-10-gcc`
- `gcc-toolset-11-binutils`
- `gcc-toolset-11-gcc`
- `gcc-toolset-11-gdb`
- `gcc-toolset-12-gdb`
- `gdb`
- `glibc`
- `gnome-boxes`
- `gnome-session`
- `gnome-themes-standard`
- `guile`
- `httpd`
- `icedtea-web`
- `initial-setup`
- `ipa`
- `java-11-openjdk`
- `java-17-openjdk`
- `java-1.8.0-openjdk`
- `java-21-openjdk`
- `Judy`
- `ksh`
- `leapp`
- `leapp-repository`
- `libblockdev`
- `libdb`
- `libguestfs`
- `libreoffice`
- `libreport`
- `libreswan`
- `libvirt`
- `libxslt`
- `llvm`
- `lorax`
- `lorax-templates-rhel`
- `mecab-ipadic`
- `net-snmp`
- `NetworkManager`
- `nginx`
- `nodejs`
- `openchange`
- `openscap`
- `open-vm-tools`
- `osinfo-db`
- `pacemaker`
- `PackageKit`
- `pcp`
- `perl-XML-Parser`
- `pesign`
- `pki-core`
- `plymouth`
- `podman`
- `policycoreutils`
- `postgresql`
- `pykickstart`
- `python2`
- `python3`
- `python-blivet`
- `rear`
- `redfish-finder`
- `redhat-lsb`
- `redhat-rpm-config`
- `rhel-system-roles`
- `rhncfg`
- `rhn-client-tools`
- `rhn-custom-info`
- `rhnlib`
- `rhnpush`
- `rhnsd`
- `rhn-virtualization`
- `rpmdevtools`
- `rpmlint`
- `runc`
- `sanlock`
- `sblim-cmpi-devel`
- `scap-security-guide`
- `scap-workbench`
- `sendmail`
- `setroubleshoot`
- `setroubleshoot-plugins`
- `skopeo`
- `sos-collector`
- `spacewalk-backend`
- `spacewalk-oscap`
- `spacewalk-remote-utils`
- `spacewalk-usix`
- `spice-streaming-agent`
- `sqlite`
- `sssd`
- `sysstat`
- `systemtap`
- `thunderbird`
- `tog-pegasus`
- `trace-cmd`
- `tuned`
- `util-linux`
- `vim`
- `virt-manager`
- `virt-p2v`
- `WALinuxAgent`
- `wget`
- `xdg-desktop-portal`
- `xsane`
- `zstd`

#### Modified Source Packages for CodeReady Linux Builder by Oracle

The following binary packages to CodeReady Linux Builder by Oracle have been modified:

- `anaconda`
- `ceph`
- `crash`
- `cups-filters`
- `dconf`
- `dotnet3.1`
- `dotnet5.0`
- `dotnet6.0`
- `dotnet7.0`
- `fwupd`
- `galera`
- `gcc`
- `gcc-toolset-10-gcc`
- `glibc`
- `guile`
- `iscsi-initiator-utils`
- `java-11-openjdk`
- `java-17-openjdk`
- `java-1.8.0-openjdk`
- `java-21-openjdk`
- `Judy`
- `kmod`
- `libblockdev`
- `libdb`
- `libdnf`
- `libguestfs`
- `libreoffice`
- `libvirt`
- `lvm2`
- `mariadb`
- `mozjs52`
- `mozjs60`
- `NetworkManager`
- `OpenIPMI`
- `openscap`
- `PackageKit`
- `parted`
- `procps-ng`
- `sanlock`
- `sblim-cmpi-devel`
- `sendmail`
- `sssd`
- `tog-pegasus`

#### Removed BaseOS Source Packages

The following source packages from the BaseOS upstream release have been removed:

- `kpatch`
- `libica`
- `redhat-indexhtml`
- `redhat-logos`
- `subscription-manager`

#### Removed AppStream Source Packages

The following source packages from the AppStream upstream release have been removed:

- `ansible-collection-microsoft-sql`
- `ansible-collection-redhat-rhel_mgmt`
- `coreos-installer`
- `insights-client`
- `libica`
- `redhat-cloud-client-configuration`
- `redhat-logos`
- `redhat-support-lib-python`
- `redhat-support-tool`
- `rhc`
- `rhc-worker-playbook`
- `rt-tests`
- `spice-client-win`
- `spice-qxl-wddm-dod`
- `spice-vdagent-win`
- `subscription-manager`
- `subscription-manager-migration-data`
- `toolbox`
- `virtio-win`
- `virt-who`