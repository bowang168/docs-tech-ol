---
title: "Oracle Linux Automation Manager 2.3: Release Notes"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/relnotes2.3"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "olam"
  - "release-notes"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux Automation Manager 2.3

Release Notes

G32908-03

August 2025

---

[Title and Copyright Information](#copyright-information)

Oracle Linux Automation Manager 2.3 Release Notes

G32908-03

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2022, 2025, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/relnotes2.3/awx-relnotesPreface.html -->

## Preface

[Oracle Linux Automation Manager 2.3: Release
Notes](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/relnotes2.3/) provides release information about Oracle
Linux Automation Manager. This document includes information on component versions, new
features, and documentation changes for Oracle Linux Automation Manager.

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
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/relnotes2.3/awx-AboutOracleLinuxAutomationManagerandOracleLinuxAutomationEngine.html -->

## 1 About Oracle Linux Automation Manager and Oracle Linux Automation Engine

Oracle Linux Automation Manager version 2.3, based on the open source projects Ansible and
AWX, is a task engine and Web interface for scheduling and running Oracle Linux Automation
Engine playbook tasks on the inventories the playbooks interact with. The Oracle Linux
Automation Engine is an automation tool for deploying software, configuring systems, and
orchestrating tasks such as upgrades and updates, in the form of playbooks.

Oracle Linux Automation Manager version 2.3 is based on the AWX version 24.6.1 open source
software. The AWX development branch and documentation are maintained at <https://github.com/ansible/awx/tree/24.6.1>.

Oracle Linux Automation Manager, includes Oracle Linux Automation Engine which is based on
the open source software package `ansible-core-2.16.6`. The development branch
and documentation are maintained at <https://github.com/ansible/ansible/tree/v2.16.6>.

Ansible is a registered trademark of Red Hat, Inc. in the United States and other
countries.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/relnotes2.3/awx_components.html -->

## 2 Component Versions

This section lists the version numbers of the major components included with Oracle Linux
Automation Manager.

Table 2-1 Oracle Linux Automation Manager Components

|  |  |
| --- | --- |
| `NGINX` | 1.14 |
| `olam-ee:2.3` (`ansible-core`) | 2.16 on Oracle Linux 8  2.14 on Oracle Linux 9 |
| `ol-automation-manager` | 2.3 |
| `ol-automation-manager-cli` | 2.3 |
| `postgresql` | 16 |
| `receptor` | 1.4 |
| `redis` | 5.0 |
| Private Automation Hub (`galaxy_ng`) | 4.9.1 |
| Builder Utility (`ansible_builder`) | 3.0.1 |

Table 2-2 Oracle Linux Automation Engine, Python Versions, OCI SDK, and Ansible OCI
Collection

| olam-ee Version | ansible-core Version | python Version | `python-oci-sdk` Version | `oci-ansible-collection` Version |
| --- | --- | --- | --- | --- |
| 2.3-ol9 | 2.14 | 3.9 | 2.154 | 5.5 |
| 2.3-minimal-ol9 | 2.14 | 3.9 | n/a | n/a |
| 2.3-ol8 | 2.16 | 3.11 | 2.154 | 5.5 |
| 2.3-minimal-ol8 | 2.16 | 3.11 | n/a | n/a |
| 2.2 | 2.16.6 | 3.11 | 2.137.1 | 5.3.0 |
| 2.2-minimal | 2.16.6 | 3.11 | n/a | n/a |
| 2.1.2 | 2.15.3 | 3.11 | 2.85.0 | n/a |
| 2.1.1 | 2.15.3 | 3.11 | 2.85.0 | n/a |
| 2.1 | 2.12.2 | 3.8 | 2.85.0 | n/a |
| 2.0 | 2.12.2 | 3.8 | 2.85.0 | n/a |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/relnotes2.3/awx-NotableUpdatesandNewFeatures.html -->

## 3 New Features and Notable Changes

This section contains information on notable changes, release updates
and new features. For more information about upgrading Oracle Linux Automation Manager, see [Oracle Linux Automation Manager 2.3: Installation
Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.3/).

### Release 2.3.1

Some notable changes in Oracle Linux Automation Manager Release 2.3.1 are:

- A new patching procedure when updating Oracle Linux Automation Manager.
- New support for Oracle Cloud Infrastructure (OCI) source type.
- New support for Oracle Linux Virtualization Manager source type.
- New support for Oracle Linux Virtualization Manager credential type.

### Release 2.3

Some notable changes in Oracle Linux Automation Manager Release 2.3 are:

- Oracle Linux 9 is now supported
- New support for Oracle Cloud Infrastructure (OCI) credential type and instructions for
  accessing a remote OCI inventory source.
- The Builder utility now supports format 3 when building Private Automation Hub images.
  This format no longer requires referencing the `olam-builder` container
  image from the Oracle Container Registry.
- New support for inventory features, such as:
  - Configuring smart inventories based on existing inventory sources.
  - Configuring external Inventory sources, existing in remote repositories, such as Git
    projects. Inventories source can use formats include yaml, yml, json, ini, toml, or
    python scripts that dynamically query other inventory files.
- New Groups functionality, including the ability to run jobs and ad hoc commands against
  grouped hosts
- Project Source Control Credential Type now includes support for Subversion and Remote
  Archives.

Note:

The Builder utility format 1 and 2 are now deprecated. Consider
using format 3 going forward.

### Release 2.2

Some notable changes in Oracle Linux Automation Manager Release 2.2 are:

- Oracle Linux Automation Manager is now based on awx 24.6.1
- Builder Utility Python version is now 3.11
- `ansible-core` version is now 2.16.6
- Topology Viewer now available in the UI. For more information about using the viewer to verify
  the Oracle Linux Automation Manager server installation, see [Oracle Linux Automation Manager 2.2: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.2/). This is a technology preview.
- The Oracle Linux Automation Manager images in Oracle Container Registry no longer use the
  `latest` tag. Always use the `2.2` tag when pulling images
  from the registry for the `2.2` release. The `latest` tag is
  deprecated and only applies to the Oracle Linux Automation Manager 2.1 release.

### Release 2.1

Some notable changes in Oracle Linux Automation Manager Release 2.1 are:

- Private Automation Hub:

  This Oracle Linux Automation Manager feature is based on the
  galaxy\_ng open source project that lets you synchronize custom collections and execution
  environment images to use with Oracle Linux Automation Manager deployments. Private
  Automation Hub can also synchronize collections and execution environments from remote
  container registries that you want to host locally. For more information about Private
  Automation Hub, see [Oracle Linux Automation Manager 2.2: Private Automation
  Hub Installation Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install-private-hub2.2/) and [Oracle Linux Automation Manager 2.2: Private Automation
  Hub User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide-private-hub2.2/).
- Builder Utility

  The builder utility is based on the `ansible-builder`
  open source project that lets you customize and create execution environments and then
  upload them to Private Automation Hub. Being able to use customized container images as
  execution environments to run playbooks lets you ensure you have all the packages and
  dependencies you need on the container image necessary to run playbooks in a consistent
  and dependable way. For more information about the Builder utility, see [Oracle Linux Automation Manager 2.2: Private Automation
  Hub Installation Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install-private-hub2.2/) and [Oracle Linux Automation Manager 2.2: Private Automation
  Hub User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide-private-hub2.2/).

### Release 2.0

Some notable changes in Oracle Linux Automation Manager Release 2.0 are:

- Service Mesh: Service Mesh provides a multi-service network
  that links control and execution nodes within a secure mesh that enables the sharing of
  job execution. The Service Mesh can include up to 20 nodes. For more information about
  configuring the Service Mesh, see [Oracle Linux Automation Manager 2.2: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.2/) and
  [Oracle Linux Automation Manager 2.2: User's
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide2.2/).
- Control Plane: The control plane is part of the Service Mesh
  that consists of control plane nodes that provide the user interface, role-based access
  control, and content management functionality. The Control Plane defines how automation is
  initiated, deployed, audited and delegated to the Execution Plane. From the Control Plane
  user interface or through the RESTful API, users can manage features such as inventory,
  schedule workflows, track changes, initiate reporting and so on. For more information, see
  [Oracle Linux Automation Manager 2.2: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.2/) and [Oracle Linux Automation Manager 2.2: User's
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide2.2/).
- Execution Plane: The Execution Plane is part of the Service
  Mesh that consists of execution plane nodes that execute Oracle Linux Automation Engine
  playbooks. Execution plane nodes use a ready-built container with Oracle Linux,
  ansible-core, python and provides collections and libraries, which enables a consistent
  and defined environment every time they run. Execution environments replace python virtual
  environments. For more information, see [Oracle Linux Automation Manager 2.2: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.2/)
  and [Oracle Linux Automation Manager 2.2: User's
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide2.2/).
- Hop Nodes: Hop nodes are connecting nodes that can link together cluster nodes
  within the Service Mesh, such as control and execution nodes, that cannot directly reach
  one another. These nodes do not appear as part of instance groups, but do appear as part of
  the Service Mesh peer relationships.
- Remote Database Options: You can now optionally install a PostgreSQL database
  on a separate host. For more information, see [Oracle Linux Automation Manager 2.2: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.2/).
- Upgrade Path from Release 1.0 to 2.0: You can upgrade Oracle Linux
  Automation Manager Release 1.0 instances to Release 2.0. The upgrade path includes
  remaining on a single node instance to upgrading to a full clustered instance. For
  more information, see [Oracle Linux Automation Manager 2.2: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.2/).
- Workflow Templates: You can create workflow templates using the Workflow Visualizer
  graphical tool. You can use the tool to specify the run sequence of disparate components
  such as job templates and management jobs, as nodes in a linear graph-like design. For more
  information, see [Oracle Linux Automation Manager 2.2: User's
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide2.2/).
- Instance Groups: You can group control plane nodes and execution plane node into
  instance groups. By default, the Oracle Linux Automation Manager installation process
  creates a default instance group for control plane nodes and a default instance group for
  execution plane nodes. You can add or remove control and execution plane nodes to an
  instance group. And you can create additional instance groups for execution plane nodes to
  further manage what execution plane node runs a specific job. For more information, see
  [Oracle Linux Automation Manager 2.2: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.2/) and [Oracle Linux Automation Manager 2.2: User's
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide2.2/).

### Release 1.0.1

Some highlighted features in Oracle Linux Automation Manager Release 2.0 are:

- Oracle Linux Automation Manager REST API: You can now
  use the REST API to programmatically interact with Oracle Linux Automation Manager
  servers. The API is based on AWX version 15.0.1 open-source
  software and all upstream features are exposed in the REST
  API; however, support is limited to those features discussed
  in Getting Started With Oracle Linux Automation Manager. For more information, see
  [Oracle Linux Automation Manager 1.0: CLI and API Reference Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/1.0/olam-api-cli/).
- Oracle Linux Automation Manager CLI: You can now
  install and use the Oracle Linux Automation Manager CLI to interact with Oracle Linux Automation Manager
  servers. The CLI is based on AWX version 15.0.1 open-source
  software and all upstream features are exposed in the CLI;
  however, support is limited to those features discussed in
  Getting Started With Oracle Linux Automation Manager. For more information, see
  [Oracle Linux Automation Manager 1.0: CLI and API Reference Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/1.0/olam-api-cli/).
- Oracle Cloud Infrastructure Ansible
  Collection credential type: Oracle Linux Automation Manager now includes
  the OCI credential type for accessing the OCI Ansible
  collection within an Oracle Linux Automation Engine
  playbook. If your Oracle Linux Automation Engine playbook
  uses the OCI Ansible collection, see
  <https://docs.oracle.com/iaas/Content/API/SDKDocs/ansible.htm>
  and find the setup instructions relating to AWX. The OCI
  credential type removes the need to manually create the OCI
  credential type as described in the
  [Using
  Oracle Cloud Infrastructure with Ansible Tower and
  AWX](https://blogs.oracle.com/cloud-infrastructure/post/using-oracle-cloud-infrastructure-with-ansible-tower-and-awx) blog post.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/relnotes2.3/awx_documentation_changes.html -->

## 4 Documentation Changes

For the latest Oracle Linux Automation Manager Release 2.0 and Release 1.0 documentation,
see [Oracle Linux Automation Manager documentation](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/).

### Release 2.3.1

Release 2.3.1 includes the following notable changes to existing documentation:

- [Oracle Linux Automation Manager 2.3: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.3/): Includes a new procedure for patching Oracle
  Linux Automation Manager software.
- [Oracle Linux Automation Manager 2.3: User's
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide2.3/): Includes instructions for setting up external
  inventory sources with the Oracle Cloud Infrastructure or Oracle Linux Virtualization
  Manager inventory types. It also includes instructions for creating Oracle Linux
  Virtualization Manager credentials.

  Note:

  All documentation remains
  at the 2.3 release, but are updated with the 2.3.1 patch information.

### Release 2.3

Release 2.3 includes the following notable changes to existing documentation:

- [Oracle Linux Automation Manager 2.3: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.3/): Includes upgrade and migration
  procedures to release 2.3.
- [Oracle Linux Automation Manager 2.3: User's
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide2.3/): Includes new inventory and group feature
  updates.
- [Oracle Linux Automation Manager 2.3: Private Automation
  Hub Installation Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install-private-hub2.3/): Now includes ugrade procedures to
  release 2.3.
- [Oracle Linux Automation Manager 2.3: Private Automation
  Hub User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide-private-hub2.3/): The Builder Utility now supports
  format 3 which no longer requires the use of the `olam-builder` container
  image from the Oracle Container Registry.

### Release 2.2

Release 2.2 includes the following notable changes to existing documentation:

- [Oracle Linux Automation Manager 2.2: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.2/): Includes upgrade procedures to release 2.2.
- [Oracle Linux Automation Manager 2.2: User's
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide2.2/): The uplift to awx 24.6.1 includes some UI changes in various locations.
- [Oracle Linux Automation Manager 2.2: Private Automation
  Hub Installation Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install-private-hub2.2/): Now includes upgrade procedures to
  release 2.2.
- [Oracle Linux Automation Manager 2.2: Private Automation
  Hub User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide-private-hub2.2/): Some changes to the Builder Utility
  discussions about Python versions and some small changes to the format 1 and format 2
  examples.
- [Oracle Linux Automation Manager 2.2: CLI and API
  Reference Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.2/): The uplift to awx 24.6.1 includes some
  changes to the REST API and CLI.

### Release 2.1

Release 2.1 includes the following new documents:

- [Oracle Linux Automation Manager 2.2: Private Automation
  Hub Installation Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install-private-hub2.2/): This document provides
  instructions about installing, backing up, and restoring Private Automation Hub
  and installing the Builder utility.
- [Oracle Linux Automation Manager 2.2: Private Automation
  Hub User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide-private-hub2.2/): This document provides instructions
  about using Private Automation Hub to manage collections and execution
  environments for use with Oracle Linux Automation Manager. In addition, this
  document provides instructions for using the Builder utility to create custom
  execution environments and upload them to Private Automation Hub.

Release 2.1 also includes the following notable changes to existing documentation:

- [Oracle Linux Automation Manager 2.2: User's
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide2.2/): A new section is available about creating execution
  environments for using custom execution environment container images hosted on
  Private Automation Hub or on some other local container registry. New
  instructions are available about creating credentials for accessing custom
  execution environments and about creating credentials for accessing collections
  hosted on Private Automation Hub.
- [Oracle Linux Automation Manager 2.2: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.2/): Existing installation procedures now includes
  information about using custom execution environments when defining default
  execution environments when running playbooks in Oracle Linux Automation
  Manager.

### Release 2.0

The contents of [Oracle Linux Automation Manager 1.0: Getting Started](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/1.0/get-started/) has been split into the
following books in release 2.0:

- [Oracle Linux Automation Manager 2.2: Installation
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.2/): The Installation Guide
  provides the following information
  - Hardware requirements
  - Installation options
  - Service Mesh topology examples
  - instructions for installing on a single host with a collocated
    database
  - instructions for installing on a single host with a remote database
  - instructions for installing in a cluster of host with a remote
    database
  - Instructions for configuring the Service Mesh nodes
  - Instructions for adding and removing cluster nodes
  - Instructions for upgrading Oracle Linux Automation Manager release 1.0
    to release 2.0
- [Oracle Linux Automation Manager 2.2: User's
  Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/user-guide2.2/): The User's Guide provides
  information about setting up permissions, teams, and users, setting up
  resources, and using views. Notable additions in Release 2.0 include the
  following:
  - Setting up Work flow Templates
  - Creating Schedules for Resources
  - Viewing Execution Environments
  - Managing Instance Groups
- [Oracle Linux Automation Manager 2.2: Administrator's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/admin-guide2.2/): The Administrator's Guide
  includes information about general administrative tasks, configuring credential
  types, configuring notification templates, scheduling management jobs, and
  configuring settings. Notable additions in Release 2.0 include instructions for
  setting up LDAP authentication for user accounts configured in an LDAP server
  that log on to Oracle Linux Automation Manager.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/relnotes2.3/awx_lifecycle.html -->

## 5 About the Oracle Linux Automation Manager Life Cycle

Support for product enhancements, Common Vulnerabilities, Exposures (CVEs) and bug fix
updates are available for Oracle Linux Automation Manager as described in [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/relnotes2.3/awx_errata.html -->

## 6 Obtaining Errata and CVE Notices

To be notified when Oracle releases new errata packages for Oracle Linux Automation Manager,
you can subscribe to the Oracle Linux errata mailing lists at <https://oss.oracle.com/mailman/listinfo/el-errata>.

If you're logged in to ULN, you can also subscribe to these mailing lists by following the
Subscribe to Enterprise Linux Errata mailing list links that are provided in the Errata tab.

Oracle publishes a complete list of errata made available on ULN at <https://linux.oracle.com/errata>. You can also see a
published listing of Common Vulnerabilities and Exposures (CVEs) and explore their details and
status at <https://linux.oracle.com/cve>. You can
also track updates to Oracle Linux yum server repositories by visiting <https://yum.oracle.com/whatsnew.html>, where you can
see which packages were updated within each repository for the previous six months.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/relnotes2.3/awx_known_issues.html -->

## 7 Known Issues

This chapter contains information about known issues and limitations in this release.

### Duplicate Collection Upload Error

If a user mistakenly publishes a collection that already exists in Private Automation Hub and
the collection has the same version information, then an error appears when attempting to
approve the collection in the Private Automation Hub Approval screen which normally moves a
collection from the staged repository to the published repository. For example, the following
is a duplicate version of the ansible posix v2.0.0 collection that had been uploaded and this
is the error message that appears in the UI when trying to approve the collection:

```
Changes to certification status for collection "ansible posix v2.0.0" could not be saved.
Error 404 - Not Found: The server could not find the requested URL.
```

You can also see the error in the Private Automation Hub server /var/log/messages directory:

```
May 12 11:34:50 example_host pulpcore-api[412891]: pulp [0dba18feb7614ebe94de27845cbedead]: django.request:WARNING: Not Found: /api/galaxy/v3/collections/ansible/posix/versions/2.0.0/move/staging/published/
```

There is no workaround for this problem because Private Automation Hub doesn't overwrite
identical collections during the approval process. For more information about enabling and
disabling the approvals function when uploading collections, see the chapter about configuring
the parameter file in [Oracle Linux Automation Manager 2.3: Private Automation
Hub Installation Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install-private-hub2.3/). If the approvals
`olpah_require_content_approval: False` function disabled using the
`olpah_require_content_approval: False` parameter, this message doesn't
appear because the collection goes directly into the published repository.

### Deprecation Warning on Oracle Linux 9 Custom Execution Environment

When running a job template with a custom execution environment built on Oracle Linux 9, the
following deprecation warning might
appear:

```
Identity added: /runner/artifacts/36/ssh_key_data (/runner/artifacts/36/ssh_key_data)
/usr/local/lib/python3.9/site-packages/paramiko/pkey.py:82: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
  "cipher": algorithms.TripleDES,
/usr/local/lib/python3.9/site-packages/paramiko/transport.py:253: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
  "class": algorithms.TripleDES,
```

No action is required. This warning can be ignored.

### Builder Error or Warning when Creating Oracle Linux 9 Execution Environment

When creating a custom execution environment with the builder utility using Oracle Linux 9,
the following error or warning message might appear relating to potential scenarios where
systemd session is already actively
running:

```
sd-bus call: Interactive authentication required.: Permission denied
```

or

```
WARN[0000] The cgroupv2 manager is set to systemd but there is no systemd user session available 
WARN[0000] For using systemd, you may need to log in using a user session 
WARN[0000] Alternatively, you can enable lingering with: `loginctl enable-linger 1001` (possibly as root) 
WARN[0000] Falling back to --cgroup-manager=cgroupfs
```

A workaround for this problem
is to set the following `loginctl` user setting before logging into the user
account:

```
sudo loginctl enable-linger <user_name>
```

In the previous, <user\_name> is the Oracle Linux 9 user account being
used to run the builder utility to create a custom execution environment based on Oracle Linux
9. This setting is persistent and must only be set one time.

### Topology Viewer Download Bundle Fails

The download bundle function on the topology viewer feature returns the following error
message:

```
"A server error has occurred."
```

This
issue is being investigated.