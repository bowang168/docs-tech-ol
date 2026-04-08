---
title: "Oracle Linux Extended Support"
source_url: "https://www.oracle.com/a/ocom/docs/linux/oracle-linux-extended-support-ds.pdf"
source_file: "oracle-linux-extended-support-ds.pdf"
converted: 2026-03-26
conversion: "claude-ocr"
tags:
  - "oracle-linux"
  - "extended-support"
  - "support-policy"
  - "lifecycle"
type: "pdf-converted"
sensitivity: public
---

# Oracle Linux Extended Support

Operating system upgrades can be lengthy and complex. While preparing to upgrade, you may need support on your current operating system version(s) beyond the normal support lifecycle. Oracle offers Extended Support for Oracle Linux, Red Hat Enterprise Linux, and CentOS Linux to enable you to receive this support.

## Manage your operating system upgrade lifecycle

Oracle Linux Basic and Premier Support are available for 10 years after the initial release of every version of Oracle Linux, Red Hat Enterprise Linux (RHEL), and CentOS Linux. This is the production support period. After this period, Oracle Linux Extended Support is available for a number of years, depending upon the release and version. Oracle Linux Extended Support requires an underlying Oracle Linux Premier Support contract. At the end of Extended Support, Oracle provides Lifetime Sustaining Support indefinitely.

Extended Support can provide continued access to updates for versions that are past their production support period, enabling you to maintain your operating system for production usage. Extended Support also provides you with the flexibility to choose when to upgrade your operating systems.

## Benefits of Extended Support

During the Extended Support period, Oracle Linux Extended Support includes the following:

- Unlimited service requests. Service request assistance also includes, but is not limited to, support topics as provided in the Scope of Coverage document.
- Access to patches and fixes for critical security errata and select high-impact critical bug fixes.
- Access to certain security patches that may be applied while your supported systems are operating and that do not require a system reboot.
- 24x7 access to My Oracle Support, including the ability to log service requests online.
- 24x7 access to the Oracle Unbreakable Linux Network to obtain patches and updates.

Oracle Linux Extended Support does not include:

- New hardware certification.
- Backporting of fixes, patches, or updates.

> Note: CentOS Linux is supported, which includes CentOS 6 and 7. CentOS Stream, versions 8 and higher, is not covered by Oracle Linux Support.

## Extended Support for Red Hat Enterprise Linux and CentOS Linux

Oracle Linux Extended Support, in addition to an Oracle Linux Premier Support subscription, can provide extended support for both Red Hat Enterprise Linux and CentOS Linux.

Red Hat Enterprise Linux (RHEL) versions 6, 7, 8, and 9 are eligible for extended support. CentOS Linux versions 6 and 7 are eligible for extended support. CentOS Stream is not eligible for Oracle Linux support.

Support for RHEL and CentOS Linux is limited to the packages and versions provided on the Oracle Linux installation media and the topics identified in the Scope of Coverage document. All security and bug fix errata will be Oracle Linux binaries. These binaries are compatible and will work without reinstallation or other coding changes.

If you're migrating from Red Hat Enterprise Linux ELS (Extended Life Cycle Support), ELS packages may need to be removed or you may need to perform a forced update to use packages from Oracle Linux Extended Support channels. View the Oracle Open Source Support Policies for more details.

## Extended Support for Oracle Linux 7

The Extended Support maintenance policy for Oracle Linux 7 has been updated to provide expanded coverage of security issues and includes select high-impact critical bug fixes for a specified list of packages as detailed below. Please refer to the Lifetime Support Policy for details on the Oracle Linux lifecycle including the Oracle Linux 7 Extended Support timeline.

### Supported Oracle Linux version and architecture

This policy applies to **Oracle Linux version 7.9 for x86_64**. Oracle Linux 7 systems covered by Extended Support must be updated to Oracle Linux 7.9 with the Unbreakable Enterprise Kernel Release 6 (UEK6), and to the most recently released packages available from the Oracle Linux 7 Server Latest (ol7_latest) repository.

If you're running an older release of the Unbreakable Enterprise Kernel (UEK5 or UEK4), you must upgrade to Latest Unbreakable Enterprise Kernel Release 6 (ol7_UEKR6) and update the latest kernel packages available.

If you're using Oracle Linux Kernel-based Virtual Machine (KVM), you will need to update to the latest packages available from Oracle Linux 7 Server KVM Utilities (ol7_kvm_utils) repository.

Oracle Linux Virtualization Manager is not covered by the Extended Support program. If you're running Oracle Linux Virtualization Manager on Oracle Linux 7, it is recommended that you upgrade your systems to Oracle Linux 8.

### Security maintenance

Oracle may provide security fixes for Critical and Important CVEs for packages covered under Oracle Linux 7 Extended Support.

This security maintenance policy applies to packages released in Oracle Linux 7 Latest (ol7_latest), Latest Unbreakable Enterprise Kernel Release 6 (ol7_UEKR6), and Oracle Linux 7 KVM Utilities (ol7_kvm_utils) repositories.

Packages released from other Oracle Linux 7 repositories (Optional Latest, Add-ons, etc.) are not covered under extended support and may only receive fixes at Oracle's discretion. For example, Oracle Linux Manager is eligible for Extended Support from January 2025 to June 2026.

### Bug fix maintenance

The below inclusion list is the set of packages included as part of the select high-impact critical bug fix maintenance:

- bind, bash, chrony, grub2, grubby, glibc, gnutls, httpd, kernel, kernel-uek (5.4), libgcrypt, libvirt, nss, openssh, openssl, python 2.7, qemu-kvm, rpm, sudo, systemd, wget, yum
- OpenJDK 1.8 is eligible for Extended Support from January 2025 to November 2026, and OpenJDK 11 is eligible for Extended support from January 2025 to October 2027.

Other bugs in packages not on this list may be addressed at Oracle's discretion.

### Oracle Linux 7 Extended Support exclusions

This policy excludes **Oracle Linux version 7.9 for aarch64**. If you're running Oracle Linux 7 on aarch64, it is recommended that you upgrade your systems to Oracle Linux 8.

The following software packages released from Oracle Linux 7 Server Latest (ol7_latest) are excluded from Oracle Linux 7 Extended Support and will not receive security or bug maintenance updates:

- .NET and .NET Core
- Apache Tomcat

Oracle Linux 7 Extended Support is limited to the following yum or ULN repositories: Oracle Linux 7 Server Latest (ol7_latest), Latest Unbreakable Enterprise Kernel Release 6 (ol7_UEKR6), and Oracle Linux 7 Server KVM Utilities (ol7_kvm_utils). Any other Oracle Linux 7 repositories are excluded from extended support, including but not limited to:

- Ceph storage
- Oracle Cloud Native Environment
- Gluster
- MySQL
- Oracle Linux Virtualization Manager
- Oracle RDMA/OFED
- Software Collection Library
- UEK Release 5, UEK Release 4

### Containers

Oracle Linux 7 as a host environment for launching and using containers is not covered under the extended support program.

Oracle will not build, or release, Oracle Linux 7 container images based on extended support content. You can build container images using Oracle Linux 7 Extended Support content, however, the addition of updates and other content to the container image is for you to manage.

## Extended Support for Oracle Linux 6

The Extended Support maintenance policy for Oracle Linux 6 consists of access to patches and fixes for critical security errata and select high-impact critical bug fixes. These updates will be limited to the packages listed on the inclusion list. This policy applies to **Oracle Linux version 6.10 for x86_64**. Oracle Linux 6 systems covered by Extended Support must be updated to Oracle Linux 6.10 with the Unbreakable Enterprise Kernel Release 4 (UEK4).

## Extended Support Pricing

Pricing is available in the Oracle Linux Support and Oracle VM Support Global Price List.

Pricing metric definitions are available in the Oracle License Definitions and Rules Booklet.

### Oracle Cloud Infrastructure

Oracle Linux Premier Support and Oracle Linux Extended Support are included with an Oracle Cloud Infrastructure subscription.

### Third-party hardware and third-party cloud providers

- Year 1 after the production support period: Oracle Linux Extended Support is equal to the Oracle Linux Premier Subscription fee plus 10%
- Year 2 and remaining years through the remainder of the extended support window: Oracle Linux Extended Support is equal to the Oracle Linux Premier Subscription fee plus 20%

### Oracle hardware

The Oracle Linux Extended Support fee is an uplift over your base support subscription for the hardware; either Premier Support for Systems or Premier Support for Operating Systems. There may be exceptions for certain Oracle Engineered Systems. Visit Oracle Hardware and Systems Support Policies for details.

## Contact

Call +1.800.ORACLE1 or visit oracle.com/linux. Outside North America, find your local office at: oracle.com/contact.
