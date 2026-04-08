---
title: "Oracle Linux Product Life Cycle Information"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle"
fetched: 2026-03-26
tags:
  - "oracle-linux"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux

Product Life Cycle Information

F75988-31

January 2026

---

[Title and Copyright Information](#copyright-information)

Oracle Linux Product Life Cycle Information

F75988-31

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2023, 2026, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/notice-NoticeDescription.html -->

## Preface

[Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/) provides information about product release
life cycles that fall outside of the standard Lifetime Support Policy: Coverage for Oracle Open Source Software
available at <https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf>. Product life cycles describe the period for which Common
Vulnerabilities and Exposures (CVEs) and bug fix updates are provided for different products
that are available as part of the Oracle Linux offering.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/OracleLinux.html -->

## 1 Oracle Linux

For supported Oracle Linux components not listed elsewhere in this document, support life cycle dates are listed at [Lifetime Support Policy: Coverage for Oracle Open Source Service Offerings](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/ApplicationStreamModuleLifeCycle.html -->

## 2 Application Stream Module Life Cycle

While the core operating system packages in the BaseOS repository for Oracle Linux 8, Oracle
Linux 9, and Oracle Linux 10 retain a [standard Oracle Linux support life cycle](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf), the separate AppStream
packages have their own major version releases and might have shorter lifespans from 2 to 5
years.

Support for the AppStream packages is limited to package
installation assistance only. Additional support for AppStream
modules might be provided if references to these modules and their
use are included in other official Oracle Linux documentation from
Oracle. Critical security errata and select high-impact critical bug
fixes are provided in the newer versions of AppStream packages.

For more information about Oracle Linux Application Streams, see [Oracle Linux: Managing Software on Oracle
Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/ol10_application_streams.html -->

## Oracle Linux 10 Application Streams

The following tables list AppStream packages available in Oracle Linux 10. As best
practice, upgrade to the latest release of these packages as soon as possible. Oracle
continues to provide support for modules in the AppStream channel until the specified
retirement date, as listed in the tables provided.

Note:

Application Streams released on Oracle Linux 10 aren't released in modular format to
simplify user experience. Therefore, when installing an initial Application Stream
on Oracle Linux 10, you can use the `dnf install` command
syntax without any need to reference a module.

### Oracle Linux 10 Full Life Application Streams

Where possible, if several shorter-lived Application Streams are available, a single stream
that extends the duration of the underlying Oracle Linux release might be offered.

Table 2-1 Oracle Linux 10 Full Life Application Streams Release Life Cycle

| Application Stream | Release Date | Release |
| --- | --- | --- |
| Ansible Core 2.16 | 2025-06 | 10.0 |
| Apache httpd 2.4 | 2025-06 | 10.0 |
| NGINX 1.26 | 2025-06 | 10.0 |
| Perl 5.40 | 2025-06 | 10.0 |
| PHP 8.3 | 2025-06 | 10.0 |
| PostgreSQL 16 | 2025-06 | 10.0 |
| Python 3.12 | 2025-06 | 10.0 |
| Ruby 3.3 | 2025-06 | 10.0 |

### Oracle Linux 10 Standard Application Streams

During the Oracle Linux lifecycle, updated versions of most Application Streams are released as needed. Each stream's support lifecycle is aligned either with upstream support or specific product requirements. Several versions of an Application Stream might be available simultaneously, and their support periods might overlap.

Note:

Retirement dates apply at the end of the documented month.

Table 2-2 Oracle Linux 10 Application Stream Life Cycle

| Application Stream | Release Date | Retirement Date | Release |
| --- | --- | --- | --- |
| .NET 8 | 2025-06 | 2026-11 | 10.0 |
| .NET 9 | 2025-06 | 2026-05 | 10.0 |
| .NET 10 | 2025-11 | 2028-11 | 10.1 |
| IDM | 2025-06 | 2027-05 | 10.0 |
| OpenJDK 21 | 2025-06 | 2029-12 | 10.0 |
| OpenJDK 25 | 2025-11 | 2030-12 | 10.1 |
| gcc-toolset 15 | 2025-11 | 2029-11 | 10.1 |
| MySQL 8.4 | 2025-06 | 2029-05 | 10.0 |
| Node.js 22 | 2025-06 | 2027-04 | 10.0 |
| Node.js 24 | 2025-11 | 2028-04 | 10.1 |
| Apache Tomcat 9 | 2025-06 | 2026-05 | 10.0 |

### Oracle Linux 10 Rolling Application Streams

Rolling application streams are supported for the full life of the Oracle Linux 10 release.
New versions of the streams replace existing versions in update releases. Rolling streams
are only used when it's essential to have new versions of the stream. Users of rolling
streams understand when and how the streams are updated and be prepared for newer
versions.

| Application Stream | Release Date | Version |
| --- | --- | --- |
| container-tools | 2025-06 | 1.14.0 |
| Git | 2025-06 | 2.47.1 |
| Go | 2025-09 | 1.25.0 |
| LLVM | 2025-06 | 20.1.8 |
| Rust | 2025-06 | 1.88.0 |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/ol9_application_streams.html -->

## Oracle Linux 9 Application Streams

The following tables list AppStream packages currently in Oracle Linux 9. As best practice,
you should upgrade to the latest release of these packages as possible. Oracle continues to
provide support for modules in the AppStream channel until the specified retirement date, as
listed in the tables below.

Note:

Initial Application Streams released on Oracle Linux 9 are not released in modular format
to simplify user experience. Therefore, when installing an initial Application Stream on
Oracle Linux 9, you can use the `dnf install` command syntax without
any need to reference a module.

Some Application Streams with shorter life cycles will be released in modular format with
updated application stream versions in subsequent update releases.

### Oracle Linux 9 Full Life Application Streams

Where possible, if several shorter-lived Application Streams are available, a single stream
that extends the duration of the underlying Oracle Linux release might be offered.

Table 2-3 Oracle Linux 9 Full Life Application Streams Release Life Cycle

| Application Stream | Release Date | Release |
| --- | --- | --- |
| Ansible Core 2.14 | 2022-06 | 9.0 |
| Apache httpd 2.4 | 2022-06 | 9.0 |
| NGINX 1.20 | 2022-06 | 9.0 |
| Perl 5.32 | 2022-06 | 9.0 |
| PHP 8.0 | 2022-06 | 9.0 |
| PostgreSQL 13 | 2022-06 | 9.0 |
| Python 3.9 | 2022-06 | 9.0 |
| Ruby 3.0 | 2022-06 | 9.0 |

### Oracle Linux 9 Standard Application Streams

During the Oracle Linux lifecycle, updated versions of most Application Streams are released as needed. Each stream's support lifecycle is aligned either with upstream support or specific product requirements. Several versions of an Application Stream might be available simultaneously, and their support periods might overlap.

Note:

Retirement dates apply at the end of the documented month.

Table 2-4 Oracle Linux 9 Application Stream Life Cycle

| Application Stream | Release Date | Retirement Date | Release |
| --- | --- | --- | --- |
| BIND 9.18 | 2024-11 | 2027-05 | 9.5 |
| .NET 6 | 2022-06 | 2024-11 | 9.0 |
| .NET 7 | 2022-11 | 2024-05 | 9.1 |
| .NET 8 | 2023-11 | 2026-11 | 9.3 |
| .NET 9 | 2024-11 | 2026-11 | 9.5 |
| .NET 10 | 2025-11 | 2028-11 | 9.7 |
| gcc-toolset 12 | 2022-11 | 2024-11 | 9.1 |
| gcc-toolset 13 | 2023-11 | 2025-11 | 9.3 |
| gcc-toolset 14 | 2024-11 | 2026-11 | 9.5 |
| gcc-toolset 15 | 2025-11 | 2029-11 | 9.7 |
| IDM | 2022-06 | 2027-05 | 9.0 |
| Maven 3.8 | 2022-11 | 2025-11 | 9.1 |
| Maven 3.9 | 2025-05 | 2028-05 | 9.6 |
| MySQL 8.0 | 2022-06 | 2026-04 | 9.0 |
| MySQL 8.4 | 2025-05 | 2029-04 | 9.6 |
| NGINX 1.22 | 2023-05 | 2025-11 | 9.2 |
| NGINX 1.24 | 2024-05 | 2027-05 | 9.4 |
| NGINX 1.26 | 2025-05 | 2028-05 | 9.6 |
| Node.js 16 | 2022-06 | 2024-04 | 9.0 |
| Node.js 18 | 2022-11 | 2025-04 | 9.1 |
| Node.js 20 | 2023-11 | 2026-04 | 9.3 |
| Node.js 22 | 2024-11 | 2027-04 | 9.5 |
| Node.js 24 | 2025-11 | 2028-04 | 9.7 |
| OpenJDK 1.8.0 | 2022-06 | 2026-05 | 9.0 |
| OpenJDK 11 | 2022-06 | 2024-10 | 9.0 |
| OpenJDK 17 | 2022-06 | 2027-12 | 9.0 |
| OpenJDK 21 | 2023-11 | 2029-12 | 9.3 |
| PHP 8.1 | 2022-11 | 2025-05 | 9.1 |
| PHP 8.2 | 2024-05 | 2029-05 | 9.4 |
| PHP 8.3 | 2025-05 | 2029-05 | 9.6 |
| PostgreSQL 15 | 2023-05 | 2028-05 | 9.2 |
| PostgreSQL 16 | 2024-05 | 2029-05 | 9.4 |
| Python 3.11 | 2023-05 | 2026-05 | 9.2 |
| Python 3.12 | 2024-05 | 2027-04 | 9.4 |
| Redis 7 | 2023-11 | 2026-11 | 9.3 |
| Ruby 3.1 | 2022-11 | 2025-03 | 9.1 |
| Ruby 3.3 | 2024-05 | 2027-03 | 9.4 |
| Tomcat mod\_jk connector for Apache | 2022-06 | 2027-05 | 9.0 |
| Valkey 8 | 2025-11 | 2029-05 | 9.7 |

### Oracle Linux 9 Rolling Application Streams

Rolling application streams are supported for the full life of the Oracle Linux 9 release.
New versions of the streams replace existing versions in update releases. Rolling streams
are only used when it's essential to have new versions of the stream. Users of rolling
streams understand when and how the streams are updated and be prepared for newer
versions.

| Application Stream | Release Date | Version |
| --- | --- | --- |
| container-tools | 2023-05 | ol9 |
| Git | 2023-05 | 2.39.1 |
| GNU Autoconf | 2024-05 | 2.71 |
| GNU Make | 2024-11 | 4.4.1 |
| Go | 2025-08 | 1.24.6 |
| Java Mission Control | 2023-05 | 7.1.1 |
| LLVM | 2025-05 | 19.1.7 |
| Rust | 2025-05 | 1.84.1 |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/ol8_application_streams.html -->

## Oracle Linux 8 Application Streams

The following tables lists AppStream packages currently in Oracle Linux 8. As best practice,
you should upgrade to the latest release of these packages as possible. Oracle continues to
provide support for modules in the AppStream channel until the specified retirement date, as
listed in the tables.

### Oracle Linux 8 Full Life Application Streams

Where possible, if several shorter-lived Application Streams are available, a single stream
that extends the duration of the underlying Oracle Linux release might be offered.

Table 2-5 Oracle Linux 8 Full Life Application Streams Release Life Cycle

| Application Stream | Release Date | Release |
| --- | --- | --- |
| Ansible Core 2.16 | 2022-05 | 8.6 |
| Apache Ant 1.10 | 2019-07 | 8.0 |
| Apache Subversion 1.10 | 2019-07 | 8.0 |
| FreeRADIUS 3.0 | 2019-07 | 8.0 |
| Git 2 | 2019-07 | 8.0 |
| Apache httpd 2.4 | 2019-07 | 8.0 |
| Identity Management Client | 2019-07 | 8.0 |
| Maven 3.8 | 2022-11 | 8.7 |
| mod\_auth\_openidc for Apache | 2019-07 | 8.0 |
| MySQL 8.4 | 2024-05 | 8.10 |
| osinfo-db | 2019-07 | 8.0 |
| NGINX 1.24 | 2024-05 | 8.10 |
| Perl 5.26 | 2019-07 | 8.0 |
| Perl 5.32 | 2022-05 | 8.6 |
| PHP 7.4 | 2020-11 | 8.3 |
| PostgreSQL 12 | 2020-02 | 8.1 |
| Python 3.6 | 2019-07 | 8.0 |
| Python 3.12 | 2024-05 | 8.10 |
| Redis 6 | 2021-05 | 8.4 |
| Ruby 2.5 | 2019-07 | 8.0 |
| Squid 4 | 2019-07 | 8.0 |
| Varnish 6 | 2019-07 | 8.0 |
| virt ol | 2019-07 | 8.0 |

### Oracle Linux 8 Standard Application Streams

During the Oracle Linux lifecycle, updated versions of most Application Streams are released as needed. Each stream's support lifecycle is aligned either with upstream support or specific product requirements. Several versions of an Application Stream might be available simultaneously, and their support periods might overlap.

Note:

Retirement dates apply at the end of the documented month.

Table 2-6 Oracle Linux 8 Application Stream Life Cycle

| Application Stream | Release Date | Retirement Date | Release |
| --- | --- | --- | --- |
| Apache Subversion 1.14 | 2021-05 | 2024-05 | 8.4 |
| authd 1.4.4 | 2019-07 | 2021-05 | 8.0 |
| container-tools 1.0 | 2019-07 | 2021-05 | 8.0 |
| container-tools 2.0 | 2020-05 | 2022-05 | 8.2 |
| container-tools 3.0 | 2021-05 | 2023-05 | 8.4 |
| container-tools 4.0 | 2022-05 | 2024-05 | 8.6 |
| .NET 2.1 | 2019-07 | 2021-08 | 8.0 |
| .NET 3.0 | 2019-11 | 2020-03 | 8.1 |
| .NET 3.1 | 2020-02 | 2022-12 | 8.1 |
| .NET 5.0 | 2020-11 | 2022-05 | 8.3 |
| .NET 6.0 | 2021-11 | 2024-11 | 8.5 |
| .NET 7.0 | 2022-11 | 2024-05 | 8.7 |
| .NET 8.0 | 2023-11 | 2026-11 | 8.9 |
| .NET 9.0 | 2024-05 | 2026-11 | 8.10 |
| .NET 10.0 | 2024-05 | 2028-11 | 8.10 |
| gcc-toolset 9 | 2019-11 | 2021-11 | 8.1 |
| gcc-toolset 10 | 2020-11 | 2022-11 | 8.3 |
| gcc-toolset 11 | 2021-11 | 2023-11 | 8.5 |
| gcc-toolset 12 | 2022-11 | 2024-11 | 8.7 |
| gcc-toolset 13 | 2023-11 | 2025-11 | 8.9 |
| gcc-toolset 14 | 2024-05 | 2026-11 | 8.10 |
| gcc-toolset 15 | 2024-05 | 2029-11 | 8.10 |
| Mailman 2.1 | 2019-07 | 2024-06 | 8.0 |
| Maven 3.5 | 2019-07 | 2022-05 | 8.0 |
| Maven 3.6 | 2020-05 | 2023-04 | 8.2 |
| Mercurial 4.8 | 2019-07 | 2022-11 | 8.0 |
| Mercurial 6.2 | 2022-11 | 2025-11 | 8.7 |
| MySQL 8 | 2019-07 | 2026-04 | 8.0 |
| NGINX 1.14 | 2019-07 | 2021-05 | 8.0 |
| NGINX 1.16 | 2019-11 | 2021-10 | 8.1 |
| NGINX 1.18 | 2020-11 | 2022-11 | 8.3 |
| NGINX 1.20 | 2021-11 | 2023-11 | 8.5 |
| NGINX 1.22 | 2023-05 | 2025-11 | 8.8 |
| NGINX 1.24 | 2024-05 | 2029-05 | 8.10 |
| Node.js 10 | 2019-07 | 2021-04 | 8.0 |
| Node.js 12 | 2019-11 | 2022-04 | 8.1 |
| Node.js 14 | 2020-11 | 2023-04 | 8.3 |
| Node.js 16 | 2021-11 | 2024-04 | 8.5 |
| Node.js 18 | 2022-11 | 2025-04 | 8.7 |
| Node.js 20 | 2023-11 | 2026-04 | 8.9 |
| Node.js 22 | 2024-05 | 2027-04 | 8.10 |
| Node.js 24 | 2024-05 | 2028-04 | 8.10 |
| OpenJDK 8 | 2019-07 | 2026-05 | 8.0 |
| OpenJDK 11 | 2019-07 | 2024-10 | 8.0 |
| OpenJDK 17 | 2021-11 | 2027-12 | 8.5 |
| OpenJDK 21 | 2023-11 | 2029-12 | 8.9 |
| Perl 5.24 | 2019-07 | 2021-05 | 8.0 |
| Perl 5.30 | 2020-11 | 2023-11 | 8.3 |
| PHP 7.2 | 2019-07 | 2021-05 | 8.0 |
| PHP 7.3 | 2019-11 | 2021-11 | 8.1 |
| PHP 8.0 | 2022-05 | 2024-11 | 8.6 |
| PHP 8.2 | 2024-05 | 2029-05 | 8.10 |
| PostgreSQL 9.6 | 2019-07 | 2021-11 | 8.0 |
| PostgreSQL 10 | 2019-07 | 2024-05 | 8.0 |
| PostgreSQL 13 | 2021-05 | 2026-05 | 8.4 |
| PostgreSQL 15 | 2023-05 | 2028-05 | 8.8 |
| PostgreSQL 16 | 2024-05 | 2029-05 | 8.10 |
| Python 2.7 | 2019-07 | 2024-06 | 8.0 |
| Python 3.8 | 2020-05 | 2023-05 | 8.2 |
| Python 3.9 | 2021-05 | 2025-11 | 8.4 |
| Python 3.11 | 2023-05 | 2026-05 | 8.8 |
| Redis 5 | 2019-07 | 2022-05 | 8.0 |
| Ruby 2.6 | 2019-11 | 2022-03 | 8.1 |
| Ruby 2.7 | 2020-11 | 2023-03 | 8.3 |
| Ruby 3.0 | 2021-11 | 2024-03 | 8.5 |
| Ruby 3.1 | 2022-11 | 2025-03 | 8.7 |
| Ruby 3.3 | 2024-05 | 2027-03 | 8.10 |
| Scala 2.10 | 2019-05 | 2023-05 | 8.0 |
| SWIG 3 | 2019-07 | 2022-05 | 8.0 |
| SWIG 4 | 2021-05 | 2024-05 | 8.4 |
| SWIG 4.1 | 2023-05 | 2027-05 | 8.8 |

### Oracle Linux 8 Rolling Application Streams

Rolling application streams are supported for the full life of the Oracle Linux 8 release.
New versions of the streams replace existing versions in update releases. Rolling streams
are only used when it's essential to have new versions of the stream. Users of rolling
streams understand when and how the streams are updated and be prepared for newer
versions.

| Application Stream | Release Date | Version |
| --- | --- | --- |
| container-tools | 2019-07 | ol8 |
| Gnu Make (Last version) | 2022-11 | ol8 |
| Go | 2025-04 | 1.23.6 |
| Java Mission Control | 2021-11 | 8.0.1 |
| LLVM | 2025-05 | 19.1.7 |
| Rust | 2025-05 | 1.84.1 |

### Oracle Linux 8 Dependent Application Streams

Dependent application streams are only supported while used by other "Full Life",
"Rolling" or "Standard" application streams and not as standalone packages.

Table 2-7 Dependent Application Streams

| Application Stream |
| --- |
| `389-ds 1.4` |
| `pki-core` |
| `pki-deps` |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/oracle_cloud_native_environment.html -->

## 3 Oracle Cloud Native Environment

Oracle Cloud Native Environment releases are supported for CVE and bug fixes based on a time
period following each release of the product. Support periods are based the major and minor
release numbers (for example 1.9, 2.0), not on the patch releases (for example: 1.9.5 or
2.0.1, and so on).

For more information about Oracle Cloud Native Environment, see [Oracle Cloud Native Environment documentation](https://docs.oracle.com/en/operating-systems/olcne/).

Table 3-1 Oracle Cloud Native Environment Support Schedules

| Description | Full Support (0-4 months) | Maintenance Support 1 (4-8 months) | Maintenance Support 2 (8-16 months) |
| --- | --- | --- | --- |
| Qualified Security Fixes Critical (C) and Important (I) | C, I | C, I | C |
| Bug fix by severity Critical (C) and Important (I) | C, I | C | No |
| Security Announcements | Yes | Yes | Yes |
| Bug Fix Errata Announcements | Yes | Yes | No |

The following table lists the dates on which each major product release was made available.
Any product releases not listed in this table are no longer supported.

Table 3-2 Oracle Cloud Native Environment Release Dates

| Oracle Cloud Native Environment Release Number | Release Date | Kubernetes Release Number |
| --- | --- | --- |
| 2.3 | January 2026 | 1.33 |
| 2.2 | July 2025 | 1.32 |
| 2.1 | February 2025 | 1.31 |
| 2.0 | September 2024 | 1.30 |
| 1.9 | June 2024 | 1.29 |
| 1.8 | January 2024 | 1.28 |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/oracle_linux_automation_manager.html -->

## 4 Oracle Linux Automation Manager

Oracle Linux Automation Manager releases are supported for CVE and bug fixes based on a time
period following each release of the product. Support periods are based the major release
numbers (for example 1 and 2), not on the minor or patch releases (for example: 1.0.1 or 2.1,
and so on).

For more information about Oracle Linux Automation Manager, see [Oracle Linux Automation Manager documentation](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/).

Table 4-1 Oracle Linux Automation Manager Support Schedules

| Description | Full Support (0-6 months) | Maintenance Support 1 (6-12 months) | Maintenance Support 2 (12-18 months) |
| --- | --- | --- | --- |
| Qualified Security Fixes Critical (C) and Important (I) | C, I | C, I | C |
| Bug fix by severity Critical (C) and Important (I) | C, I | C | No |
| Security Announcements | Yes | Yes | Yes |
| Bug Fix Errata Announcements | Yes | Yes | No |
| Select Software Enhancements | Yes | No | No |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/oracle_linux_virtualization_manager.html -->

## 5 Oracle Linux Virtualization Manager

Oracle Linux Virtualization Manager receives CVE and bug fix updates for the current and the
previous major and minor releases (N and N-1). A release that's at N-1 receives CVE and bug
fix updates for a 6 month period following the N release date. Updates are based on the major
and minor release numbers (for example 1.0 to 2.0 or 1.3 to 1.4, and so on), not on the patch
releases (for example: 1.2.1 or 1.2.2, and so on).

For more information about Oracle Linux Virtualization Manager, see [Oracle Linux Virtualization Manager
documentation](https://docs.oracle.com/en/virtualization/oracle-linux-virtualization-manager/).

Table 5-1 Oracle Linux Virtualization Manager CVE and Bug Fix Updates

| Oracle Linux Virtualization Manager | Release Date | CVE and Bug Fix Updates |
| --- | --- | --- |
| Release 4.5 (N) | December 2023 | Yes |
| Release 4.4 (N-1) | April 2022 | Available until July 2024 |
| Release 4.3 (N-2) | April 2020 | Ended October 2022 |