---
title: "Using the Cockpit Web Console"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "system-management"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux

Using the Cockpit Web Console

F51970-15

October 2025

---

[Title and Copyright Information](#copyright-information)

Oracle Linux Using the Cockpit Web Console

F51970-15

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2022, 2025, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/preface.html -->

## Preface

Oracle Linux includes a web console you can use for system administration. The web
console is called Cockpit. For non-minimal installations, Cockpit is automatically installed,
although not automatically enabled. Cockpit provides a web browser interface for performing
system configuration and administration tasks, either locally or remotely on multiple servers.
These tasks include system resource monitoring and log review, network and firewall
configuration, and package management and updates. Cockpit uses the same APIs to access system
services, so any changes you make using operating system command line tools are updated in
real time in Cockpit.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-install.html -->

## 1 Get Started: Cockpit Web Console

To get started with using the Cockpit web console, administrators should review the following
topics to become familiar with Cockpit features. Instructional information covered in these
topics include steps to install Cockpit, as well as information to optionally create a Login
Banner, specify a background theme, setup a multiple host configuration, or add additional
functionality to the Cockpit web interface.

- [Cockpit Web Console Overview](cockpit_overview.html)
- [Installation and Log In](cockpit-install_section.html)
- [Cockpit Login Banner](banner_creation_dita.html)
- [Cockpit Background Theme](display_mode.html)
- [Management of Multiple Hosts](cockpit-manage_multiple_hosts.html)
- [Extend Cockpit's Functionality](extend_cockpit.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit_overview.html -->

## Cockpit Web Console Overview

The Cockpit web console is an Oracle Linux server administration tool designed for managing
and monitoring Linux systems both locally and remotely. The graphical web console for
management and administration is user-friendly and accessible to administrators at all levels
of experience with Linux. The Cockpit installation package arrives out of the box and ready
for use in most Oracle Linux distributions.

Intuitive Server Administration

Choosing Cockpit as an Oracle Linux server administration tool can help make server
administration with Oracle Linux more discoverable and intuitive. For example, the web console
interface doesn't require you to remember commands to input at a command line. Although, you
can still access and use the command line, it's often easier to complete those same
administration tasks from the web console interface.

Standard and Add-On Server Administration Tools

System administrators can conveniently administer different areas of a host server by
clicking the Cockpit navigational menu in the left side panel of the web console. This menu,
by default, presents a standard set of system administration tools that are ready for use.
Optionally, other add-on administration tools can be added to the web console as needed.

A list of the system administration menu options that are typically included in the Cockpit
web console upon first time use are as follows:

Table 1-1 Administration Tools - Menu Navigation

| Use: | To: | Details: |
| --- | --- | --- |
| Host (Disabled by default starting in Oracle Linux 10) | - View the system hostname of the connected Oracle Linux server. - Add secondary host systems to manage from a primary single web console   instance. | [Management of Multiple Hosts](cockpit-manage_multiple_hosts.html) |
| Overview | - Examine host system health, usage, hardware, and general configuration   details. - Set the system hostname and time. - View and change the generated Secure Shell fingerprint. - Set system recommended performance profile settings. - View system usage statistics and graphs for CPU and Memory. - View the host system hardware configuration details. | [Health, Usage, and System Details](view_system.html) |
| Logs | - View and filter log entries collected on the host system. - Pause or resume the log view entries captured by the system. | [View and Filter Log Entries](cockpit-monitor_using_available_quantifiers.html) |
| Storage | - View and change partitions on disk devices. - Encrypt block devices with LUKS. - Create and manage logical volumes. - Create and configure RAID storage arrays. - Connect to NFS servers and iSCSI targets. | [Storage Management Tasks](cockpit-storage_management.html) |
| Networking | - View the host system firewall setup and network interfaces. - Set firewall rules and zones. - Set properties to configure network bonding, teaming, bridges, and VLANs. | [Network Management Tasks](cockpit-network.html) |
| Accounts | - Manage host user access. - Set properties to create, edit, lock, or suspend user access. | [User Management Actions](cockpit-usermanage.html) |
| Services | - Administer host System and User processes, targets, sockets, timers, and   paths. - Find System or User processes by filtering the view with criteria of interest.   For example, filter by description, name, Active State, or File state. - Change the state of a service by selecting a different action (for example,   start, stop, reload, activate, or deactivate). - Click Relationships to view a service's dependencies with other system   services. - View log entries collected for a specific service. | [View and Manage Services](cockpit-services.html) |
| Diagnostic Reports | - Generate a diagnostic report to gain insight on the overall operation of the   host system. - Download a report, delete a report, or generate other reports. | [Evaluate System Problems Using Diagnostic Reports](diag_reports_evaluate_issues.html) |
| Kernel Dump | - View and manage the properties of the kernel crash dump configuration. - Test the kernel crash dump configuration by intentionally crashing the kernel   on the host system. | [Capture Crash Dump Details Using Kdump](cockpit-kdump.html) |
| SELinux | - View and manage properties of the SELinux policy configuration. - View recent SELinux policy modifications applied to the host system. - View and manage access control policy errors generated on the host Linux   system. | [Manage SELinux Security Policy and Messages](cockpit-selinux_manage.html) |
| Terminal | - Directly access and use the host system Terminal command line user interface. Sometimes, the completion of administration tasks requires the use of the   CLI. | To access the host CLI, click Terminal In the Cockpit navigation pane. |

Add-On Server Administration Applications

System administrators can optionally extend the Cockpit web console functionality by
installing extra administration tool packages that were developed for Cockpit. For more
details, see [Extend Cockpit's Functionality](extend_cockpit.html).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-install_section.html -->

## Installation and Log In

The following topics step you through the process of installing the Cockpit package and logging you in to the Cockpit web console for the first time.

- [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html)
- [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-install_install_the_cockpit_package.html -->

## Install and Enable Cockpit

The `cockpit` package is, by default, included in all non-minimal Oracle
Linux software installations.

What Do You Need?

- A system with Oracle Linux installed.
- Root administrator privileges on the host Linux system.

  Note:

  The steps in this procedure use the `sudo` command to run commands as the root user.

Steps

Using a terminal on the Oracle Linux machine, perform the following steps to install and enable the `cockpit` package.

1. To verify the version of the `cockpit` package that's available for
   installation, type: 

   ```
   sudo dnf info cockpit
   ```

   The versioning information and other
   information describing the `cockpit` package appears in the command line
   output.
2. To install the Cockpit package on the Oracle Linux host system, type:

   ```
   sudo dnf install cockpit
   ```
3. To enable the systemd socket service and automatically start it upon a system restart,
   type:

   ```
   sudo systemctl enable --now cockpit.socket
   ```

   The socket web service, by
   default, is configured to accept connections on TCP port 9090.
4. To verify that the socket web service is enabled for Cockpit, type:

   ```
   sudo systemctl status cockpit.socket
   ```

   An Active status and the default
   listening port of 9090 appears in the command line output to indicate the service
   is enabled.
5. **Optional:** If a firewall is enabled, perform the following to enable the Cockpit service to receive inbound connections. 
   1. Open the firewall for the cockpit service as follows:

      ```
      sudo firewall-cmd --add-service=cockpit --permanent
      ```
   2. Apply the firewall configuration change in the runtime environment by reloading the firewall configuration as follows:

      ```
      sudo firewall-cmd --reload
      ```

      Note:

      The firewall restricts access to the cockpit system. Remote authorized users can access the system securely by using port forwarding over SSH. For example, the user can type the following command from the user's local system:

      ```
      ssh -L 9090:localhost:9090 user@cockpit-system
      ```

      The cockpit-system can be the system's fully qualified domain name (FQDN), such as `myserver.example.com` or the system's IP address. Then the user can sign in to `localhost`, as explained in [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-install_logging_into_cockpit.html -->

## Log in to the Cockpit Web Console

Cockpit lets you log in directly to any Oracle Linux system that permits connections to the
application using TCP port 9090.

Note:

If the 9090 port isn't accessible on the system, you can still use Cockpit to administer the system by adding it as a secondary host server. For details on how to add a secondary server, see [Management of Multiple Hosts](cockpit-manage_multiple_hosts.html).

What Do You Need?

- The IP address or hostname of the Oracle Linux server where Cockpit is installed.
- A valid Oracle Linux user account on the server where Cockpit is installed.

  Note:

  Cockpit uses PAM for authentication and the configuration is available in `/etc/pam.d/cockpit`. With PAM authentication, you can sign in with a username and password on any system account that has administrator privileges.
- (Optional) Signed Certificate by Certificate Authority on Oracle Linux host.

  Note:

  To avoid granting a security exception each time you access the Cockpit web console, install a certificate signed by a certificate authority (CA) in the `/etc/cockpit/ws-certs.d` directory. The last file (in alphabetical order) with a `.cert` extension is used. For more details, see Managing Certificates and Public Key Infrastructure in [Oracle Linux: Managing Certificates and Public Key
  Infrastructure](https://docs.oracle.com/en/operating-systems/oracle-linux/certmanage/).

Steps

Perform the following steps to sign in to the Cockpit web console.

1. In a web browser, access the Cockpit web console using the hostname or IP address of
   the system at port 9090 using HTTPS. For example:

   ```
   https://myserver.example.com:9090
   ```

   If you're signed in on the local host, you can use:

   ```
   https://localhost:9090
   ```

   If you aren't using a signed security certificate, a warning message appears indicating the browser doesn't trust the site's security certificate. To continue, you can choose to bypass this error by clicking the browser option available (such as Advanced or More details) for adding a security exception for this site.

   The Cockpit Login page appears.
2. In the Cockpit Login page, enter the system username and
   password. 

   Note:

   As an alternative, you can remotely connect to another Linux host system on the network by clicking: (1) Other Options, (2) Connect to, and then entering the URL of the remote host.

   Important:

   On some Oracle Linux installations, you can't log in to Cockpit using a root account. For example, a root account can't be used to log in to Cockpit on new Oracle Linux 9.2 and later installations. In cases where the system was upgraded to Oracle Linux 9.2 or later, you can continue to log in to Cockpit with a root user account. On new Oracle Linux 9.2 or later installations, you can control which accounts can or can't be used for log in by editing the `etc/cockpit/disallowed-users` file.

   ```
   cat /etc/cockpit/disallowed-users 
   # List of users which are not allowed to login to Cockpit
   root
   ```
3. Click Log in. 

   After successful authentication, the Cockpit web page appears.

   Important:

   The Cockpit web console takes on the privileges and security context of the signed in
   user. Upon first time sign in, Limited access mode is enabled
   by default. To elevate privileges to Administrative access
   mode, click the toggle switch to Turn on administrative access.
   Upon successful authentication of the user password, administrative privileges are
   granted.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/banner_creation_dita.html -->

## Cockpit Login Banner

Administrators can choose to communicate changes to host users by displaying a banner
message on the Cockpit Login page. Typically, a banner message is
useful for enforcing a security policy or to inform users of scheduled maintenance
events.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- An existing `cockpit.conf` file must be saved in the
  `/etc/cockpit/` directory.

  Important:

  The Cockpit
  configuration file (`cockpit.conf`) isn't a system required file. In
  cases where the file doesn't already exist, the file must be manually created before
  performing the steps in this procedure. For more details about the use of this file, see
  the `cockpit.conf(5)` manual page.
- Administrator privileges.

Steps

Using the command line, perform the following steps to add a prelogin banner message to the
Cockpit configuration file.

1. Specify the text for the banner message in the `issue.cockpit` file, for example:
   1. Open or create the `/etc/issue.cockpit` file in a text editor.
   2. In the `issue.cockpit` file edit or add the content that you want to display as a prelogin banner message.

      Don't include any macros in this file as no reformatting is handled between the file content and the displayed content. Use line breaks and indentation to format the banner content. You can also use ASCII art.
   3. Save the file.
2. If you haven't done so already, add the banner file properties to the Cockpit
   configuration file as follows:
   1. Open the `cockpit.conf` file in the `/etc/cockpit/`
      directory. For example:

      ```
      sudo vi cockpit.conf
      ```
   2. In the `cockpit.conf` file, add the following information:

      ```
      [Session]
      Banner=/etc/issue.cockpit
      ```
   3. Save the file.
3. Restart Cockpit for the configuration file changes to take effect.

   ```
   sudo systemctl try-restart cockpit
   ```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/display_mode.html -->

## Cockpit Background Theme

Cockpit users can optionally set a dark or light background theme on the web console.
Cockpit automatically sets a dark theme on the web console whenever it detects a dark
background is in use by the system. Cockpit users can choose to change the theme mode by
clicking the Session menu and specifying the applicable theme mode
(dark or light).

Light mode can offer users more contrast to help focus on the finer details. While dark mode
is considered an accessibility setting that can help in the following scenarios:

- When viewing Cockpit at night within a dark room.
- To reduce eye strain.
- As a personal preference for users with various eyesight conditions or migraines.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-manage_multiple_hosts.html -->

## Management of Multiple Hosts

Cockpit enables administrators flexibility when it comes to the number of hosts they can manage from a single Cockpit session. Administrators requiring the configuration of a multi-host setup in Cockpit must ensure that all the proper prerequisites are met first.

Important:

Adding and connecting to secondary hosts is deprecated in the Cockpit web console for Oracle Linux 10 hosts, and is disabled by default. The Cockpit web console for Oracle Linux 8 or 9 hosts still provides this function. For more information, see [Deprecation of Host Switching](cockpit-deprecation-of-host-switching.html).

For details on how to set up a multi-host configuration in Cockpit, see the following topics:

- [Security Considerations for Multiple Host Management](cockpit_host_security_considerations.html)
- [Add and Connect to Secondary Host](cockpit-hosts_add_secondary_host.html)
- [Edit or Remove Secondary Host](cockpit-hosts_remove_secondary_host.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-deprecation-of-host-switching.html -->

## Deprecation of Host Switching

Starting in Oracle Linux 10, host switching is disabled by default in the Cockpit web console.

Connecting simultaneously to multiple hosts through the Cockpit web console introduces the opportunity for a single malicious host to run programs on all connected hosts. Given this risk, when connecting to an Oracle Linux 10 host, the Host drop-down menu in the upper left corner of the web interface is disabled by default.

Note:

To preserve user workflows in previous Oracle Linux releases, the Host menu is still enabled when you connect to Oracle Linux 8 or 9 hosts.

As an alternative to switching hosts in the Host menu, you can still connect to other hosts from the Cockpit login page. Click Other options, Connect to, then enter the hostname or IP address. If you connect only to a single host within a browser session, you can avoid the security risks of connecting to multiple hosts.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit_host_security_considerations.html -->

## Security Considerations for Multiple Host Management

For optimal security, consider implementing the following configurations when accessing and managing multiple host systems from a single Cockpit web console instance.

Important:

Adding and connecting to secondary hosts is deprecated in the Cockpit web console for Oracle Linux 10 hosts, and is disabled by default. The Cockpit web console for Oracle Linux 8 or 9 hosts still provides this function. For more information, see [Deprecation of Host Switching](cockpit-deprecation-of-host-switching.html).

- Optimal topology configuration over SSH connection:
  - Install Cockpit on a bastion host and use it to connect and manage other secondary Cockpit hosts. The Cockpit bastion host should be configured with a certificate-authority-issued TLS certificate.
  - Configure all secondary hosts to communicate over an SSH connection. For example, in this scenario:
    - All secondary Cockpit hosts are reachable through the SSH protocol (which defaults to port 22).
    - The SSH firewall port is open on all secondary Cockpit hosts.
    - Enabling the `cockpit.socket` service on the secondary Cockpit hosts is not required.
    - A certificate-authority-issued TLS certificate isn't required on the secondary Cockpit hosts. However, the primary Cockpit bastion host must be configured with a certificate-authority-issued TLS certificate.

    For SSH configuration details, see Configuring OpenSSH Server  in [Oracle Linux: Connecting to Remote Systems With
    OpenSSH](https://docs.oracle.com/en/operating-systems/oracle-linux/openssh/).

    Note:

    Cockpit Project - Authentication: For additional information when managing primary and secondary servers using Cockpit, see <https://cockpit-project.org/guide/latest/authentication.html>.
- Use of SSH for remote host authentication:
  - SSH key-based authentication (preferred authentication method) – Key-based authentication helps to prevent brute force password attacks against SSH and it provides administrators with password-less key-based authentication.

    If an SSH key-based authentication isn't already set up, it's easily configurable by selecting the Authorize SSH Key check box when logging in to a remote host. For details, see Step 3 in this procedure [Add and Connect to Secondary Host](cockpit-hosts_add_secondary_host.html).

    -OR-
  - SSH password authentication – Password authentication of the SSH client requires entering the user id and password from the host on which the SSH server resides. While SSH password authentication might be convenient for some users, password authentication is discouraged because it can make accounts more susceptible to intrusion.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-hosts_add_secondary_host.html -->

## Add and Connect to Secondary Host

The Cockpit web console enables system administrators to manage multiple Linux host systems
all from a single Cockpit web console instance.

Important:

Adding and connecting to secondary hosts is deprecated in the Cockpit web console for Oracle Linux 10 hosts, and is disabled by default. The Cockpit web console for Oracle Linux 8 or 9 hosts still provides this function. For more information, see [Deprecation of Host Switching](cockpit-deprecation-of-host-switching.html).

What Do You Need?

- For optimal security access requirements, see [Security Considerations for Multiple Host Management](cockpit_host_security_considerations.html).

  Attention:

  The Steps appearing in this topic assume that the security access
  considerations have been met for the primary and secondary Cockpit hosts.

  - Cockpit is installed and enabled on a bastion host.
  - The primary Cockpit bastion host is configured with a certificate-authority-issued
    TLS certificate.
  - Cockpit is installed on all secondary hosts.
  - All secondary Cockpit hosts are configured to support OpenSSH.

    For SSH
    configuration details, see Configuring OpenSSH Server  in [Oracle Linux: Connecting to Remote Systems With
    OpenSSH](https://docs.oracle.com/en/operating-systems/oracle-linux/openssh/).
- Established connection with the primary Cockpit (bastion enabled) host.
- Administrator privileges.

Steps

Follow these steps to add and connect a secondary Cockpit host to a primary Cockpit
host.

1. In the primary Cockpit web console, do the following:
   1. In the username@hostname section that appears
      above the navigation pane, expand the hidden Host menu by
      clicking the down-arrow.
   2. In the Host menu, select Add new host.

      The Add new host dialog appears.
2. In the Add new host dialog, configure the following properties
   and click Add.

   |  |  |
   | --- | --- |
   | Host | Enter a hostname or IP address of the secondary host that you want to add. |
   | User Name | Enter the username configured on the secondary host. |
   | Color | Select a top-border color to distinguish this secondary host from other secondary hosts. |
3. If this is a first-time SSH connection to the newly added secondary host, one of the
   following dialogs appears. 
   1. New Host dialog - If this dialog appears, follow the
      instructions on the dialog to confirm the SSH key fingerprint, then click
      Accept Key and Connect.
   2. Log in to [host] dialog. If this dialog appears, configure
      the following properties and click Log in.

      Note:

      If SSH key authentication isn't already set up, the
      Log in to: [host] dialog appears.

      |  |  |
      | --- | --- |
      | Password | Enter the user password on configured on the secondary host. Note that when the Automatic Login option isn't configured, future authentication for the secondary host prompts for a user password. |
      | Automatic Login | (Optional) Authorize SSH Key Perform these steps:  1. Select the Automatic Login checkbox to    configure SSH key authentication on the secondary host. 2. In the Key password text box and the    Confirm key password text box, specify the key    password. When Automatic Login is enabled, future logins to this secondary host are no longer prompted for a user password. |

      A connection is established to the secondary host. The name of the secondary host
      appears on the Host menu at the upper left corner on the
      page.
4. To log in to the newly added secondary host, click the Host
   menu, and then select the name of the secondary host. 

   A dialog prompting for a user password only appears if the secondary host isn't
   configured with SSH key authentication.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-hosts_remove_secondary_host.html -->

## Edit or Remove Secondary Host

System administrators can use the Host menu on the primary Cockpit web console to
edit or remove secondary host configurations.

Important:

Adding and connecting to secondary hosts is deprecated in the Cockpit web console for Oracle Linux 10 hosts, and is disabled by default. The Cockpit web console for Oracle Linux 8 or 9 hosts still provides this function. For more information, see [Deprecation of Host Switching](cockpit-deprecation-of-host-switching.html).

What Do You Need?

- Established connection with the primary Cockpit web console.

  Note:

  The primary
  Cockpit web console is the management web console that's configured with secondary
  hosts.
- Administrator privileges.

Steps

Using the primary Cockpit web console, follow these steps to edit or remove a secondary
host configuration.

1. In the upper left corner of the web console, click the down arrow next to the primary
   host name.

   The Host drop-down menu appears listing the name of each
   secondary host configuration.
2. In the Host drop-down menu, click Edit
   hosts and then perform one of the following:

   Remove secondary host configuration:

   1. Click the red [-] minus button next to the secondary host
      name that you want to remove. A prompt appears to confirm the removal operation, click
      Yes to proceed.
   2. Click Stop editing host

   - OR -

   Edit existing secondary host configuration:

   1. Click the pencil () icon next to the secondary host name that you want to edit.
   2. In the Edit [hostname] dialog, make the necessary changes, and click Set.
   3. Click Stop editing hosts.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/extend_cockpit.html -->

## Extend Cockpit's Functionality

To include extra server administration functionality in Cockpit, administrators can optionally install add-on applications that are included in the Oracle Linux distribution.

Note:

Depending on the Oracle Linux version installed, some add-on application packages might not be available for installation.

Table 1-2 Oracle Linux Cockpit Add-on Applications

| Application | Install Package | Usage |
| --- | --- | --- |
| Applications and Software Updates | `cockpit-packagekit` | Add-on Application management and software updates (typically installed by default). |
| Diagnostic Reports | `cockpit-sosreport` | Reports to help diagnose system problems. |
| Image Builder | - Oracle Linux 10: `cockpit-image-builder` - Oracle Linux 9 and Oracle Linux 8: `cockpit-composer` | Generates custom images suitable for deploying systems or uploading to the cloud. |
| File Browser | `cockpit-files` | Provides a graphical file manager. |
| Kernel Dump | `cockpit-kdump` | Helps to catch stack traces. |
| Machines | `cockpit-machines` | Manage libvirt virtual machines. |
| Performance Data (on-demand) | `cockpit-pcp` | Installed on demand from the Cockpit web console upon clicking View Usage metrics and history. |
| Podman | `cockpit-podman` | Manage Podman containers as of Oracle Linux 8.1. |
| SELinux | `cockpit-selinux` | View and manage SELinux exceptions. |
| Storage | `cockpit-storaged` | Manage host systemâs storage devices. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/manage_add_on_applications.html -->

## Install and Manage Add-on Applications

The Cockpit add-on applications are installable by either issuing a command in the CLI or
by clicking a button on the Applications page of the Cockpit web
console.

Note:

The Applications page is available when the `cockpit-packagekit` add-on application is installed on the system. In some instances, `cockpit-packagekit` might already be installed and available for use in the web console.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: and [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html)
- Administrator privileges.
- Names of the add-on application packages to install. For a list of package names, see
  [Extend Cockpit's Functionality](extend_cockpit.html).

Steps

Follow these steps to install and manage Cockpit add-on applications in the web
console.

1. Install add-on applications using one of the following methods: 

   | Option | Steps |
   | --- | --- |
   | **Using the command line** | In the Cockpit navigation pane, click Terminal and then use the following command syntax to install add-on application packages:  ``` sudo dnf install [packagename] ```  For example, to install the `cockpit-packagekit` package, type:  ``` sudo dnf install cockpit-packagekit ``` |
   | **Using the Applications page** | In the Cockpit navigation pane, click Applications, and then for each add- on package you want to install, click Install. |
2. In the Cockpit navigation pane, click Applications to manage all existing add-on applications. 

   For example, on the Applications page, you can choose to perform any of the following tasks:
   - View the add-on application names already installed.
   - Click Remove to remove a selected application from Cockpit.
   - Click Install to re-install a selected application that was previously removed from Cockpit.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/common_administration.html -->

## 2 Common Host Administration Tasks

Common host administration tasks that are often performed from the command line can be performed from the Cockpit web console. These common tasks involve basic host configuration, security management, user management, system monitoring actions, and software updates. For more information about performing these tasks from the Cockpit web console, see the following topics:

- [General Host Configuration Actions](cockpit-config_host_tasks.html)
- [Security Management Actions](securitypractice.html)
- [User Management Actions](cockpit-usermanage.html)
- [System Monitoring Actions](cockpit-monitor.html)
- [Software Updates](cockpit-softwaremanage.html)
- [File Management](cockpit-filemanagement.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-config_host_tasks.html -->

## General Host Configuration Actions

Using the Configuration panel on the Overview page, Cockpit administrators can conveniently
access and perform any of the following host configuration actions.

- [Change System Hostname](set_host_name.html)
- [Change System Date and Time](set_system_time.html)
- [Change TuneD Performance Profile](cockpit-tuned.html)
- [Restart or Power Off System](reboot.html)
- [Join an Active Directory Domain](cockpit-system_join_a_domain.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/set_host_name.html -->

## Change System Hostname

When you access the Cockpit web console the hostname assigned to the system appears in the
Configuration section of the Overview page.
Cockpit administrators can choose to change the properties assigned to the Real
hostname (Static or Transient) or the Pretty hostname
(free-form UTF8) as needed.

Note:

A transient hostname, such as `localhost`
appears by default whenever a Static or Pretty hostname isn't configured.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html)
  and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to change the existing hostname assigned
to the host system.

1. In the Cockpit navigation pane, click Overview.

   The Overview page appears.
2. In the Overview page, navigate to the Configuration section and
   find the Hostname field, then click Edit. 

   The Change host name dialog box appears.
3. In the Change host name dialog box, change either the Pretty host name field or the Real host name field, and click Change.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/set_system_time.html -->

## Change System Date and Time

When you access the Cockpit web console, the host system date and time appears in the
Configuration section of the Overview page.
As needed, Cockpit administrators can use the configurable properties on the
Overview page to change the date, time, and timezone options set on
the host system.

What Do You Need?

- The Cockpit web console must be installed and accessible on a host machine.

  For
  details, see these topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to change the date, time, and time
zone properties set on a host system.

1. In the Cockpit navigation pane, click Overview.

   The Overview pane appears.
2. In the Overview page, navigate to the
   Configuration section and find the System time property, then
   click the current date and time.

   The Change system time dialog box appears.
3. In the Change system time dialog box, perform the following:

   |  |  |
   | --- | --- |
   | Time zone | Set the appropriate timezone by region and city location. Tip: To navigate through the list, type the first few letters of the closest city. |
   | Set time | Select one of the following options to set the system time. Important: Some options might not be available for configuration on all host systems.  - Manually – When selected, configurable properties appear to set the exact time and date specific to the time zone specified. - Automatically using NTP – When selected, the system uses any available NTP service to obtain the correct time. For example, the Oracle Linux `chrony` NTP service is typically available and configured, by default, to use the `pool.ntp.org` servers. - Automatically using additional NTP servers – When selected, configurable properties appear enabling you to specify a specific NTP server for synchronizing the system clock. |
4. Click Change.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-tuned.html -->

## Change TuneD Performance Profile

Oracle Linux uses the `TuneD` service to monitor connected devices and dynamically tune the system performance according to a selected profile. By default, the `TuneD` service assigns a recommended performance profile. In cases where the performance profile requires modification, Cockpit administrators can use the Overview page in the web console to assign a different performance profile.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The TuneD service in Oracle Linux must be started and enabled on the host system. For more information about configuring the TuneD service, see one of the following guides:
  - [Oracle Linux 8: Optimize Performance and Power Consumption With TuneD and PowerTOP](https://docs.oracle.com/en/operating-systems/oracle-linux/8/tuned/)
  - [Oracle Linux 9: Optimize Performance and Power Consumption With TuneD and PowerTOP](https://docs.oracle.com/en/operating-systems/oracle-linux/9/tuned/)
  - [Oracle Linux 10: Optimize Performance and Power Consumption With TuneD and PowerTOP](https://docs.oracle.com/en/operating-systems/oracle-linux/10/tuned/)
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to change the performance profile
assigned to the host system.

1. In the Overview page, navigate to the
   Configuration panel and find the Performance
   profile property, then click the assigned profile link.
2. In the Change performance profile dialog box, select one of the following profiles and then click Change profile to apply the change.

   | Profile | Description |
   | --- | --- |
   | None | Disables the TuneD service state. |
   | accelerator-performance | Provides the same tuning as the throughput-performance profile and improves the performance of certain accelerators, such as GPUs. |
   | balanced | Provides a generalized performance profile and is considered suitable for systems requiring a compromise between power saving and performance. |
   | balanced-battery | Optimizes performance for laptop systems and saves power to preserve battery life. |
   | desktop | Optimizes performance for desktop environments based on the balanced profile. |
   | hpc-compute | Optimizes the performance for high-performance computing (HPC) and is based on the latency-performance profile. |
   | intel-sst | Optimized for system configurations with user-defined Intel Speed Select Technology. |
   | latency-performance | Optimized for deterministic performance at the cost of increased power consumption. |
   | network-latency | Optimized for deterministic performance at the cost of increased power consumption and focuses on low latency network performance. |
   | network-throughput | Optimized for streaming network throughput. This profile is only necessary on older CPUs or 40G+ networks. |
   | optimize-serial-console | Optimized for using with a serial console. |
   | powersave | Optimized for low power consumption. |
   | throughput-performance | Optimized for increased performance across various common server workloads. |
   | virtual-guest | Optimized when running virtual guests based on the throughput-performance profile. |
   | virtual-host | Optimized for maximum performance when running KVM host. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/reboot.html -->

## Restart or Power Off System

Using the Overview page in the web console, Cockpit administrators
can restart or power off the host, set a time delay, and send a message to warn users to
save their changes prior to signing out.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html)
- Administrator privileges.

Steps:

Using the Cockpit web console, follow these steps to perform actions related to
powering off or restarting a managed host system.

1. In the Cockpit navigation pane, click Overview.
2. In the Overview page, click the Reboot
   arrow and then select one of the following: 

   - Reboot – To restart the host system.
   - Shutdown – To power off the host system.
3. In the Reboot or Shutdown dialog box,
   perform the following:
   1. **Optional:** In the text box, type a brief message warning users to save their work and sign out.
   2. **Optional:** Click the Delay arrow and select a time interval for delaying the action (reboot or shutdown).
   3. Click Reboot or Shut down.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-system_join_a_domain.html -->

## Join an Active Directory Domain

For system environments where Active Directory authentication is already set up, Cockpit
administrators can use the Overview page in the web console to join
an existing Active Directory domain service.

Note:

The Join a domain process is similar to using the `realm
join` command from the command line. More information is available on the
`realm(8)` manual page.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- An Active Directory service must already be set up and running on the server
  instance.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to join the host system to an existing
Active Directory domain service.

1. In the Cockpit navigation pane, click Overview.
2. In the Overview page, navigate to the
   Configuration panel, find the Domain
   property, and then click Join domain. 

   The Join a domain dialog box appears.
3. In the Join a domain dialog box, perform the following:
   1. Enter the Domain address, Domain administrator, and the Domain administrator password.
   2. Click Join.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/securitypractice.html -->

## Security Management Actions

To help increase system security, Cockpit administrators can perform the following security
management actions from the web console.

- [Disable SMT to Prevent CPU Security Issues](disable_smt.html)
- [Change System-Wide Cryptographic Policy](modify_crypto.html)
- [Set a Timeout for Inactive Sessions](set_session_time_out_for_web_console.html)
- [Manage SELinux Security Policy and Messages](cockpit-selinux_manage.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/disable_smt.html -->

## Disable SMT to Prevent CPU Security Issues

For host systems supporting CPU SMT, system administrators should consider disabling the use of this configuration to prevent system security vulnerabilities. The CPU SMT configuration is typically enabled by default to enhance CPU workload performance.

For more details relating to the CPU SMT usage notice, see [Oracle Linux: Simultaneous Multithreading
Notice](https://docs.oracle.com/en/operating-systems/oracle-linux/notice-smt/).

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

WARNING:

Disabling SMT on the host requires restarting the
system.

Steps

Using the Cockpit web console, follow these steps to disable the SMT configuration on
the host system.

1. In the Cockpit navigation pane, click Overview.
2. In the Overview page, perform the following:
   1. Navigate to the System Information panel and click
      View hardware details.
   2. In the Hardware information page, find the CPU
      Security property, and, if available, click
      Mitigations.

      Important:

      For system configurations where CPU SMT isn't available, the
      Security link for Mitigations doesn't appear. In these instances, the system
      configuration isn't considered vulnerable to security related attacks because of the
      misuse of CPU SMT.

      The CPU security toggle dialog box appears.
3. In the CPU security toggle dialog box, perform the following: 
   1. **Optional:** Click Read to access further details about CPU SMT configurations.
   2. Click the toggle button to set the Disable simultaneous multi-threading (nosmt) property.
   3. Click Save and Reboot

      The host system restarts and disables the CPU use of SMT.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/modify_crypto.html -->

## Change System-Wide Cryptographic Policy

As of Oracle Linux 8 and later, a default system-wide cryptographic policy no longer permits host systems to communicate with older, insecure protocols. For system configurations that require a different level of protection, Cockpit administrators can change the assigned cryptographic policy level (Default, Legacy, Future, FIPS) by using the web console.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

WARNING:

Changing the cryptographic policy on the host requires restarting the system.

Using the Cockpit web console, follow these steps to change the cryptographic policy configuration on the host system.

1. In the Cockpit navigation pane, click Overview.
2. In the Overview page, navigate to the Configuration panel, find the Cryptographic policy property, and then click Default (or the policy name that appears). 

   The Change cryptographic policy dialog box appears with a brief description of each policy level.
3. In the Change cryptographic policy dialog box, select a policy level that best meets the requirements of the managed system, and then click Apply and reboot.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/set_session_time_out_for_web_console.html -->

## Set a Timeout for Inactive Sessions

Cockpit, by default, doesn't automatically expire inactive user sessions. To prevent
unauthorized use of an unattended session, consider specifying a duration for when inactive
user sessions expire.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- An existing `cockpit.conf` file must be saved in the
  `/etc/cockpit/` directory.

  Important:

  The Cockpit
  configuration file (`cockpit.conf`) isn't a system required or provided
  file. In cases where it doesn't already exist, you must manually create the file before
  performing the steps in this procedure. For more details about the use of this file, see
  the `cockpit.conf(5)` manual page.
- Administrator privileges.

Steps

Using the Cockpit Terminal CLI, perform the following steps to configure a session idle
timeout duration in the Cockpit configuration file.

1. In the Cockpit navigation pane, click Terminal.
2. In the Terminal page, open the `cockpit.conf`
   file in the `/etc/cockpit/` directory in a text editor. For example:

   ```
   sudo vi /etc/cockpit/cockpit.conf
   ```
3. Add the following information to the `cockpit.conf` file:

   ```
   [Session]
   IdleTimeout=value
   ```

   The `IdleTimeout` property specifies how many minutes until an inactive
   user session in Cockpit is automatically logged out.
4. To set the `IdleTimeout` property, perform one of the following:
   - To disable the `IdleTimeout` property, set the
     `value` to `0`. For example:
     `IdleTimeout=0`

     -OR-
   - To enable the `IdleTimeout` property, set the value to
     reflect the number of minutes allowed before a user session times out. For example, to
     set an hour of inactivity before a user is logged out, you would set the value to 60.
     (`IdleTimeout=60`).
5. Save the changes to the `cockpit.conf` file.
6. Restart Cockpit for the configuration file changes to take effect. 

   ```
   sudo systemctl try-restart cockpit
   ```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-selinux_manage.html -->

## Manage SELinux Security Policy and Messages

Security Enhanced Linux (SELinux) provides an additional layer of security on a host system
by applying security policies that enable administrators to control who can access the system.
The SELinux package is by default included at installation by most Oracle Linux distributions.
Upon starting the system, SELinux automatically applies security restrictions to users,
programs, processes, and files based on the access permissions defined in the policy.

Administration tasks for setting SELinux policy rules and users are administered from the
command line. However, tasks for changing the SELinux policy mode and managing the SELinux
alert messages and automation script are conveniently supported in the Cockpit web console.
For more details on how administrators can use the Cockpit web console to perform these tasks,
see:

- [Change SELinux Policy Mode](cockpit-selinux_manage_policy_mode.html)
- [View SELinx Modifications and Copy Automation Script](cockpit-selinux_manage_script.html)
- [Manage SELinux Alert Message](cockpit-selinux_manage_logs.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-selinux_manage_policy_mode.html -->

## Change SELinux Policy Mode

Cockpit administrators can choose to use SELinux page in the web console to change the way SELinux runs at boot by changing its policy mode. The SELinux policy mode, by default, is set to enforcing.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to change the SELinux Policy mode
on the local host.

1. In the Cockpit navigation pane, click SELinux.

   The SELinux page appears.
2. In the SELinux page, click the SELinux policy toggle button to switch the mode (Enforcing (default) | Permissive.)

   WARNING:

   In Cockpit, you can switch the SELinux policy mode between enforcing and permissive. Enforcing mode is the default, and the recommended mode. Permissive mode doesn't deny operations based on SELinux security policy. Permissive mode can be helpful for SELinux policy development or debugging purposes.

   To prevent incorrectly labeled and unlabeled files from causing problems, SELinux automatically relabels file systems when changing from the disabled state to permissive or enforcing mode. Use the `sudo fixfiles -F onboot` command to create the `/.autorelabel` file containing the `-F` option to ensure that files are relabeled upon next reboot.

   Before rebooting the system for relabeling, ensure the system boots in permissive mode, for example by using the `enforcing=0` kernel option. This setting prevents the system from failing to boot in case the system contains unlabeled files required by `systemd` before starting the `selinux-autorelabel` service.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-selinux_manage_script.html -->

## View SELinx Modifications and Copy Automation Script

Cockpit administrators can view SELinux system modifications made to the local system using the SELinux page in the web console. If required, Cockpit administrators can also use the View automation script link on the SELinux page to copy the same settings to other hosts.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The `policycoreutils-python-utils` package must be installed to transfer
  SELinux configuration settings to other Oracle Linux hosts.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to view the SELinux policy modifications
that were applied to the local host, and optionally, to apply the same settings to other
hosts.

1. In the Cockpit navigation pane, click SELinux.
2. In the SELinux page, perform any of the following: 
   - To view the SELinux policy modifications, navigate to the System modifications section. The SELinux policy modifications applied to the host appear in a table format.
   - To apply the same SELinux policy settings to other hosts, perform these steps:
     1. Click View automation script. The Automation script dialog box appears.
     2. To copy the automation settings, click Copy to clipboard.
     3. To copy and import the configuration settings to other hosts, use the command line. For example, the syntax you use to copy and import the configuration settings might look similar to:

        ```
        scp ./my-selinux-settings new-system-hostname:
        ```

        ```
        new-system-hostname$ sudo semanage import -f ./my-selinux-settings
        ```

        For more details, see the `scp` (secure copy) command line utility and the `semanage-import(8)` manual page.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-selinux_manage_logs.html -->

## Manage SELinux Alert Message

Cockpit administrators can monitor and manage access denial alert messages generated by
SELinux using the SELinux page in the web console.

Note:

To perform
similar tasks from the command line use `setenforce` and
`sealert` tools. For more information, see Troubleshooting Access
Denial Messages in [Oracle Linux: Administering SELinux](https://docs.oracle.com/en/operating-systems/oracle-linux/selinux/).

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to view or dismiss access denial
messages that are generated by SELinux on the local host.

1. In the Cockpit navigation pane, click SELinux.

   The SELinux page appears.
2. In the SELinux page, perform any of the following: 
   - To view alert-generated access denial messages, navigate to the SELinux
     access control errors section. The messages appear in a table
     format.
   - To dismiss one or more alert generated message, select the check box for each message that you want to dismiss, and then click Dismiss selected alerts.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-usermanage.html -->

## User Management Actions

Administrators can use the web console to manage user access on the host system. For example,
configurable options are available on the Accounts page to create or change user
account profiles that define access privileges, account expiration, password management, and
SSH authentication. Additionally, the Accounts page includes configurable options that
enable administrators to remove a user account or end a user session.

For more details about performing user management tasks from the Accounts page in the
Cockpit web console, see these topics:

- [Create or Change User Accounts](cockpit-usermanage_create_a_user.html)
- [Disconnect User Sessions or Remove User Accounts](cockpit-usermanage_access_the_accounts_page.html)
- [Find and Manage Account Information](search_sort_view_accts.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-usermanage_create_a_user.html -->

## Create or Change User Accounts

The Accounts page in the web console provides configurable properties that enable
Cockpit administrators to manage user access on the host system. Upon accessing the
Accounts page, a list of user accounts that are configured with management access
appear. At a minimum, the root user account appears on the Accounts page.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- For SSH authentication configurations only, the generated SSH key pair must be stored on
  the Cockpit system, the SSH key pair password must be known, and the file contents of the
  RSA key must be copied to the clipboard.

  Note:

  For more SSH key
  generation details, see [Oracle Linux: Connecting to Remote Systems With
  OpenSSH](https://docs.oracle.com/en/operating-systems/oracle-linux/openssh/).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to manage user access on the host system.

1. Click Accounts in the Cockpit navigation pane.

   The Accounts page appears.
2. In the Account page, perform one of the following:
   - Add a New User Account - In the Accounts page, click Create new account to access the Create new account dialog box. Enter the following account properties for the user and click Create.

     | Property | Description |
     | --- | --- |
     | Full name | The full name of the user. |
     | User Name | The log in account name for the user. |
     | Home directory | The path for the new user's home directory. |
     | Shell | The path to the default shell for the user. |
     | User ID | A unique number assigned to the user. |
     | Authentication | The policy setting that either allows or prohibits the user from logging in to the host with a password. Select one of the following: - Use passwordâThe user is permitted to log in to the host using a password. Select Require password change on first login to force the user to reset the password the first time they log in to the system. - Disallow password authenticationâThe user is prohibited from logging in to the host using a password. |
     | Password and Confirm Password | The password used to log in to the user's account. |
   - Edit an Existing User Account - In the Accounts page, click an existing account name and change any of the following properties as needed.

     | Property | Description |
     | --- | --- |
     | Full name | The full name of the user. |
     | Groups | A list of groups the user account is assigned to. A group is an entity which ties together multiple user accounts for a common purpose, such as granting access to particular files. Select any group(s) you want to assign to the user account from the drop-down list, or remove access to any groups. |
     | Options | Sets password access and account expiration: - Disallow interactive passwordâSelect the checkbox to prohibit the user from logging in using a password. - Never expire accountâEnabled by default. To set an expiration date for the account, click Edit, then select Expire account on YYYY-MM-DD and set a date in the date editor. This option is helpful when managing a temporary user. |
     | Password | Sets the applicable Password properties: - Set passwordâChange the current user password. - Force changeâRequire the user to enter a new password at next sign in. - Never expire passwordâEnabled by default. Click Edit to require the user to change the password within a defined number of days. |
     | Shell | The path to the default shell for the user. Click Change to select a different shell. |
     | Add key | Assigns authorized SSH public keys to the user account. 1. Click Add key. 2. Paste the contents of the public key file into the text field and click Add. The newly added public key assigned to the user account appears in the Authorized public SSH keys section of the Account page. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-usermanage_access_the_accounts_page.html -->

## Disconnect User Sessions or Remove User Accounts

Using the Account page in the web console, Cockpit administrators
can disconnect a specified user session or remove a specified user account configuration.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to disconnect user sessions or to remove
user account profiles from the host system.

1. In the Accounts page of the web console, select a user account, and then perform one of the following actions:
   - Disconnect User Session – In the selected user account page, click Terminate session to disconnect the web console session.

     Note:

     If the Terminate session button is unavailable, the selected user isn't signed in to the web console.
   - Remove a User Account – In the selected user account page, click Delete to remove the user account from the host system.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/search_sort_view_accts.html -->

## Find and Manage Account Information

The Cockpit web console, as of Oracle Linux 9.2 and 8.8, includes additonal user management
capabilities for finding and managing user account information. For example:

- Find and Sort Account Information – On the
  Accounts page, you can:
  - Use the Search box to find account information by
    entering keywords such as username, user group name, user ID, and so on.
  - Use the up and down arrows in the table columns
    to sort the content by descending or ascending order.
- Edit Account and Assign or Unassign a Group – In the Edit user
  account dialog, click the Group drop down
  list to either: 1) add the account to an existing user group, or 2) remove the
  account from an assigned user group.
- View or Create User Groups From Group Table – In the
  Group table, you can view all existing user groups
  defined on the system or click Create new group to define
  a new user group.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-monitor.html -->

## System Monitoring Actions

Cockpit makes it easy to monitor the system health, hardware inventory, event logs, and
services running on the host system. For more details on how perform these system monitoring
actions from Cockpit, see the following topics:

- [Health, Usage, and System Details](view_system.html)
- [View and Manage Services](cockpit-services.html)
- [View and Filter Log Entries](cockpit-monitor_using_available_quantifiers.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/view_system.html -->

## Health, Usage, and System Details

Cockpit collects system health, usage, and hardware details from the host in real time. Using
the panels on the Overview page, Cockpit administrators can find
relevant information about the system's health, resource usage, and hardware configuration.

The following table provides a brief description of each panel appearing on the
Overview page.

| Panel | Description |
| --- | --- |
| Health | Provides a general assessment of the system's health, including an indication of any failed services. |
| Usage | Provides a graphical presentation of how the system CPU and memory resources are used. Clicking the View metrics and history link displays a further information about the CPU, Memory, Disk, and Network usage. Note: The `cockpit-pcp` package is required to display the performance metrics on the system. |
| System Information | Identifies information about the system hardware. Clicking the View hardware details link displays more information about the hardware components detected on the system. |
| Configuration | Identifies general host configuration settings (host name, system time and date, and so on). Cockpit administrators, as needed can edit these settings to meet their needs. For more details about these settings, see [General Host Configuration Actions](cockpit-config_host_tasks.html) |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-services.html -->

## View and Manage Services

Cockpit administrators can use the Services page to monitor and manage the services running on the host system. For example:

- includes properties for activating, deactivating, restarting, or managing the automatic start-up setting at boot.
- provides filters that help you find the service you want to change.
- The names of the services appear in an easy-to-read table format. Each row displays the service name, description, state, and automatic start-up behavior.
- The tabs at the top of the Services page enable you to switch the view between Services, Targets, Sockets, Timers, and Paths.

The Services page has the following components:

- [Properties] for activating, deactivating, or restarting services, or managing the automatic start-up setting at boot.
- Filters help you find the service you want to view or change.
- The names of the services appear in an easy-to-read table format. Each row displays the service name, description, state, and automatic start-up behavior.
- Tabs at the top of the Services page correspond to a selection of `systemd` units. You can view a list of Services, Targets, Sockets, Timers, and Paths.

Note:

Cockpit uses `systemd` to manage host service processes.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to view and manage the behavior of system
processes on the host system:

1. In the Cockpit navigation pane, click Services.

   The Services page appears.
2. In the Services page, click a tab to display the `systemd` unit type you want to view. 

   For example, Services, Targets, Sockets, Timers, and Paths. A list of processes for that unit type appears in a table format as follows:

   | Column | Displays |
   | --- | --- |
   | 1 | Name of service process. |
   | 2 | Description of service process. |
   | 3 | Status of service process. |
   | 4 | Operating state of service process. |
3. In the selected unit type tab page, perform any of the following operations:

   | Operation | Instructions |
   | --- | --- |
   | Filter page output | Filter the page output by: - User or system processes – Click System or User (at top right side of page). - Process name or description – In the text box, enter a process name or process description of interest. - Active process state or file process state – Select the state of interest from the Active State drop-down list or File State drop-down list. |
   | Change the operating state | Perform these steps: 1. In the first column of the table, select a service name of interest. The service-name page appears. 2. Perform the applicable action(s):    - To activate or deactivate the process, turn on or off the Account Service toggle switch.    - To start, stop, or reload the process, click the Account Service      Additional Actions [â®] menu. |
   | View system logs | Perform these steps: 1. In the first column of the table, select the service name of interest. The service-name page appears. 2. Navigate to the Service Logs panel and then click View all logs. |
   | Create Timer (Timer tab only) | Perform these steps in the Timer tab:  1. Click Create timer at the upper right top of the page. A Create timer dialog appears. 2. Configure the required properties. For more details about creating `systemd` timers, see Systemd Timers in [Manage System Time and Schedule Tasks on    Oracle Linux](https://docs.oracle.com/en/learn/ol-chrony-systemd-timers/). |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-monitor_using_available_quantifiers.html -->

## View and Filter Log Entries

The Logs page in Cockpit web console displays events and messages generated by the kernel, applications, and users signed in to the system. Cockpit administrators can exclude or include log entries appearing on the page by using predefined filter options or a free-form text search. In addition to the log filtering options, Cockpit administrators can also pause and resume the on-going reporting of log entries appearing on the Logs page as needed.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).

Steps

Using the Cockpit web console, follow these steps to manage the event and messages
appearing on the Logs page.

1. In the Cockpit navigation pane, click Logs.

   The Logs page appears displaying a listing of logged events.

   Note:

   On this page, the text field, by default, contains a text string expression that
   filters the list of displayed events. To see all the logged events, clear the text field
   of the filter.
2. Perform any of the following tasks on the Logs page. You might
   need to clear the filter to see all the logged events.

   - View event details: In the list, click an event to access further details
     about that event. A journal page appears listing the details about the event, such as
     the priority level, syslog facility, syslog identifier, and the audit login UID and
     session.
   - Pause or resume the log view:  Click Pause to stop new
     log entries from appearing on the page. Click Resume to display
     all on-going log entries, including the entries that were paused earlier from
     displaying.
   - Change log view with predefined filter options: Filter the log view by using
     the following predefined filters options:

     | Filter | Options |
     | --- | --- |
     | Time | Select a relative time period for the events you want to display in the log view. For example: - `Current boot` - `Previous boot` - `Last 24 hours` (default) - `Last 7 days` |
     | Priority | Select a priority level for the events that you want to display in log view. For example: - `Only emergency` - `Alert and above` - `Critical and above` - `Error and above` (default) - `Warning and above` - `Notice and above` - `Info and above` - `Debug and above` Note: The `Debug and above` option displays the most expansive list of events. |
     | Identifier | Select a syslog identifier for the type of events you want to include in the log view. For example: - `All` (default) - `cockpit-session` - `kernel` - `password` - `sshd` - `sudo` - `systemd` Note: The syslog identifier options correspond to the  `journalctl --identifier` options. |
   - Change log view with free-form search expression:
     1. Click the down-arrow in the `text` field to apply extra
        qualifiers to the search, or to create a free-form search expression.

        | Search Parameters | Description |
        | --- | --- |
        | Since and Until | Use the following date specification format to filter log entries by a specific date or time. - `YYYY-MM-DD HH:MM:SS` Or, you can: - Apply the following search strings: `now`,   `today`, `tomorrow,` and   `yesterday`. - Express relative times by prefixing "`-`" or   "`+`" to the search string. |
        | Boot | By default, when a boot ID is omitted the logs for the current boot appear. To display logs from a specific boot, specify a boot ID, for example: - `boot=[ID]` Where   ID equals the boot order number (1, 2, and so   on) found in the journal. |
        | Unit | Filter log entries by a `systemd` unit (such as a service unit), or for units matching a specific pattern, for example: - `unit=UNIT|PATTERN` Note that when a pattern is specified, a list of unit names in the journal are compared with the specified pattern to display a list of all units matching the specified pattern. |
        | Free-form search | Filter log entries by entering: - Any text string OR - A search string expression, for example: `priority:err   identifier:kernel` |

        Important:

        Each search parameter
        corresponds to a `journalctl` command parameter.
     2. Click Search to apply the search parameters to the log
        view; or, click Reset to clear the search fields.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-softwaremanage.html -->

## Software Updates

Cockpit administrators can conveniently use the web console to keep their system software
up-to-date with new improved functionality while addressing fixes for known issues. For more
information on how to apply pending software updates from the Cockpit web console, see these
topics:

- [Apply Pending Software Updates Manually](cockpit-softwaremanage_manage_manual_software_updates.html)
- [Schedule Automatic Software Updates](cockpit-softwaremanage_manage_automatic_software_updates.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-softwaremanage_manage_manual_software_updates.html -->

## Apply Pending Software Updates Manually

Cockpit administrators can use the Software updates page in the web console to manually apply software updates to the host system. The Software updates page includes a Status section that tracks when the system was last checked for updates. If updates are available, Cockpit administrators can choose to manually apply them. If the system is up-to-date with the latest software, a green check mark appears with an up-to-date status message.

Note:

Alternatively, administrators can apply pending software updates from the command line using the `dnf upgrade` command. For more information on how to perform this task from the command line, see Updating Software on Oracle Linux.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Cockpit Software Update package (`cockpit-packagekit`) must be
  installed. In the case where the Software Update module doesn't appear in the web console
  navigation panel, see [Install and Manage Add-on Applications](manage_add_on_applications.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these instructions to manually apply pending software
updates on the host system.

1. In the Cockpit navigation pane, click Software updates. 

   The Software updates page appears.
2. In the Status section of the Software
   updates page, perform any of the following:
   - Verify when last check for updates occurred – A status message appears indicating the last time the system was checked for pending software updates.
   - Manually check and install pending updates
     1. Click Check for updates (curved blue arrow icon).

        The system checks for pending updates. In the case that software updates are pending, a list of the pending updates appear.
     2. To apply the software updates:
        1. Perform one of the following:
           - Click Install all updates to apply all pending updates listed.
           - Click Install security updates to apply the pending security updates listed.
           - Click Install kpatch updates to apply the pending `kpatch` updates listed.
        2. Turn on the Reboot toggle switch to automatically reboot the system after applying the selected software updates.

           Important:

           Avoid restarting the system until the updates are applied. If the Reboot toggle mode is turned off, a message appears to Restart the system. In message dialog, click Ignore to postpone the system restart until the updates are applied. After the updates are applied, a message appears to restart the system, click Restart Now.
     3. To ensure that the selected updates were successfully applied, log in to the Cockpit web console and verify the Status on the Software updates page.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-softwaremanage_manage_automatic_software_updates.html -->

## Schedule Automatic Software Updates

Cockpit administrators can use the Software updates page in the web console to automatically schedule when software updates occur on the host system. Configurable properties for scheduling an automatic software update include selecting the update type (none, security, or all) and the frequency for how often the automatic update occurs.

Note:

Alternatively, administrators can use the command line to configure automatic software
updates. For more information about using the command line to perform
this task, see Updating Software Automatically  in [Oracle Linux: Managing Software on Oracle
Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/software-management/).

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Cockpit Software Update package (`cockpit-packagekit`) must be installed. In the case where the Software Update module does not appear in the web console navigation panel, see [Install and Manage Add-on Applications](manage_add_on_applications.html).

  Note:

  A first time set up is also required for automatic updates after installing `cockpit-packagekit`. The steps for performing the first time set up is covered in the following procedure.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these instructions to configure automatic software
updates on the host system.

1. In the Cockpit navigation pane, click Software updates. 

   The Software updates page appears.
2. In the Settings section of the Software updates page, view the Automatic updates status message to determine what steps to take: 

   | Message | Summary | Action to take |
   | --- | --- | --- |
   | Not set up | The system is unable to perform automatic updates because the `dnf-automatic` package is not installed. | Proceed to the First time set up only step to install the `dnf-automatic` package. |
   | Disabled | The software required to enable automatic updates is installed, but automatic updates are disabled. | To enable automatic updates, click Edit. |
   | Security updates will be applied | An automatic update schedule is active for security updates, and the message indicates how often and when the automatic updates occur. | To change automatic update settings, click Edit. |
   | Updates will be applied | An automatic update schedule is active for all software packages, and the message indicates how often and when the automatic updates occur. | To change automatic update settings, click Edit. |
3. First time set up onlyâInstall the software required to enable automatic software updates.

   Important:

   If `dnf-automatic` is already installed, proceed to the next step.

   1. In the Settings pane, click Enable. 

      The Install software dialog displays a message stating that `dnf-automatic` will be installed.
   2. Click Install to install the `dnf-automatic` package.

      After the `dnf-automatic` package installs, the Automatic updates dialog opens.
4. In the Automatic updates dialog, specify the following properties, then click Save changes:

   | Property | Options |
   | --- | --- |
   | Type | Select the update type that you want to automate (or disable): - No updatesâDisables all automatic updates. - Security updates onlyâAutomates security related updates only. - All updatesâAutomates all updates (patches, bug fixes, security updates and so on). |
   | When | In the drop-down lists, specify the frequency (daily or a specific day of week) and the time for the automatic updates to occur. |

After you configure automatic updates, the system applies the updates according to the schedule you defined in the Automatic Updates dialog. Upon completing the updates, the system automatically restarts.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-filemanagement.html -->

## File Management

As of Oracle Linux 9.5, a file browser add-on package is available for the Cockpit web console. The file browser provides a graphical interface for managing files and directories on the server. You can interact with the file browser in many of the same ways you would interact with the file browser in a graphical desktop environment: create directories, rename and delete files, copy and paste files, and bookmark favorite directories. The file browser complements the user and group management tasks you might perform in Cockpit, with graphical controls for viewing and changing file permissions. You can also open text files and make edits in a simple text editor.

Before you can use the graphical file browser in the Cockpit web console, install the `cockpit-files` add-on application.

For more information about managing files with Cockpit, see the following topics:

- [Changing File Permissions](cockpit-change_file_permissions.html)
- [Transferring Files to or from the Server](cockpit-transfering_files.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-change_file_permissions.html -->

## Changing File Permissions

The file browser provides a graphical interface where you can change file and directory permissions without using the command line.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Cockpit Files package (`cockpit-files`) must be installed. In the case where the File Browser module doesn't appear in the web console navigation panel, see [Install and Manage Add-on Applications](manage_add_on_applications.html).
- User accounts and groups must be provisioned.

  For details, see [Create or Change User Accounts](cockpit-usermanage_create_a_user.html) and [Find and Manage Account Information](search_sort_view_accts.html).
- Administrator or ownership privileges for the file or directory you are managing.

  Note:

  When you sign in to the Cockpit web console, limited access mode is enabled by default. To gain administrative access, click Turn on administrative access and authenticate when prompted.

  With administrative access, you can change the file owner and group in addition to the file permissions.

  Additionally, users with administrative access can select either root or their account as the owner when they create a directory.

Steps

Follow these instructions to change permissions for a file or directory on the server.

1. In the Cockpit navigation pane, click File browser.
2. Navigate to the parent directory of the file or directory whose permissions you want to change.
3. Right-click the file or directory, then select Edit permissions.
4. Select permissions for the file or directory.

   The permissions available for you to edit depend on whether you're using Cockpit in a Limited or Administrator mode:

   | Access Mode | Permissions |
   | --- | --- |
   | **Administrator** | Under Ownership, select the owner and group you want to assign from the drop-down lists. |
   | **Limited or Administrator** | Under Access, select the access permissions you want to assign from each drop-down list. If you are signed in with limited access, you can edit permissions only for the files you own. |
5. Click Change.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-transfering_files.html -->

## Transferring Files to or from the Server

The file browser provides a graphical interface where you can transfer files between your local computer and the server.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Cockpit Files package (`cockpit-files`) must be installed. In the case where the File Browser module doesn't appear in the web console navigation panel, see [Install and Manage Add-on Applications](manage_add_on_applications.html).
- Access permissions enabling the task you want to perform:
  - Uploading a file: your account must have read, write, and execute permissions for the directory where you want to upload a file.
  - Downloading a file: your account must have read permission for the file you want to download.

Steps

Follow these instructions to transfer files between your local computer and the server using the file browser.

1. In the Cockpit navigation pane, click File browser.
2. Navigate to the directory where you want to make a file transfer.
3. Perform one of the following operations to transfer files:

   | Operation | Steps |
   | --- | --- |
   | **Upload a file to the server** | 1. Click Upload. 2. Browse your local computer, select the file you want to upload, then click Open. |
   | **Download a file from the server** | 1. Right-click the file you want to download, then click Download. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-network.html -->

## 3 Network Management Tasks

Cockpit administrators can use the Networking page in the web console
to help optimize network performance and prevent network disruptions. For more details about
performing network management tasks from the Cockpit web console, see the following topics:

- [Manage Firewall Zoning Properties](cockpit-network_configure_the_firewall.html)
- [Monitor or Change Interface Connections](cockpit-network_control_access_to_interface.html)
- [Configure Network Bonding Properties](cockpit-network_configure_a_network_bond.html)
- [Configure Network Teaming Properties](cockpit-network_configure_a_network_team.html)
- [Configure Network Bridging Properties](configure_network_bridging.html)
- [Configure Network VLAN Properties](configure_networking_vlans.html)
- [View Network Host Log Files](cockpit-networ_view_firewall_log_files.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-network_configure_the_firewall.html -->

## Manage Firewall Zoning Properties

Using the Networking page in the web console, Cockpit administrators can monitor and manage properties related to firewall zoning rules.

Note:

The firewall properties in the Cockpit web console work directly with the `firewalld` management service.

- [Change Host Firewall State](cockpit-network_enable_disable_firewalld_service.html)
- [Display Firewall Zone Properties](cockpit-network_access_zone_information.html)
- [Control Access to Zone Services](add_and_enable_a_firewall_service.html)
- [Add a New Predefined Zone](cockpit-network_add_a_pre_defined_zone.html)
- [Remove an Existing Predefined Zone](cockpit-network_remove_or_modify_zone.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-network_enable_disable_firewalld_service.html -->

## Change Host Firewall State

Using the Networking page, Cockpit administrators can enable or
disable the firewall state on the host system.

Note:

By default, the firewall management service (`firewalld`) is enabled on the host system. When this service is enabled, all incoming network traffic is blocked with the exception where firewall zoning rules are set to enable incoming traffic for services and their ports.

For more information about a zone-based firewall implementation and the firewall management service in Oracle Linux, see one of the following:

- [Oracle Linux 8: Configuring the Firewall](https://docs.oracle.com/en/operating-systems/oracle-linux/8/firewall/)
- [Oracle Linux 9: Configuring the Firewall](https://docs.oracle.com/en/operating-systems/oracle-linux/9/firewall/)
- [Oracle Linux 10: Configuring the Firewall](https://docs.oracle.com/en/operating-systems/oracle-linux/10/firewall/)

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to enable or disable the firewall
management service (`firewalld`) state on the host system.

1. In the Cockpit navigation pane, click Networking.

   The Networking page appears.
2. In the Firewall panel of the Networking page, click the toggle switch to change the firewall state. 

   The Firewall panel displays the current state of the firewall: either Enabled or Disabled.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-network_access_zone_information.html -->

## Display Firewall Zone Properties

The `firewalld` management service filters all incoming interface traffic
into one or more predefined zones. Each predefined zone has its own set of firewall rules
for accepting or denying packets.

A default zone, called public, is automatically assigned to the host system during the installation of Oracle Linux. In cases where a host system is configured as a multi-zoned system, other predefined zones are available to view in addition to the default public zone.

Using the Networking page in the web console, Cockpit administrators can view the firewall management rules associated with each zone.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to review the host system's current zone information:

1. In the Cockpit navigation pane, click Networking. 

   The Networking page appears.
2. In the Networking page, find the Firewall panel and perform one of the following to access and view the predefined zoning information:

   - Click the active zone link appearing under the Firewall heading.

     Important:

     The name of the active zone link indicates the number of active zones. A zone is only active if it has at least one interface or source assigned.
   - Click Edit rules and zones in the Firewall panel.

     Note:

     For information on how to edit the firewall management rules associated with a predefined zone, see [Control Access to Zone Services](add_and_enable_a_firewall_service.html).

     Information about each predefined zone appears in tables, for example:

     - `Firewalld` predefined zone name. The name of the predefined zone appears. For example: Public, External, DMZ, Work, Home, or Internal.
     - Interfaces and source addresses. The names of the interfaces and source addresses that are allowed access through the predefined zone appear.

       Important:

       `Firewalld` doesn't automatically pair the interface source IP address ranges to the default public zone. It does, however, automatically pair all the interface names to the default public zone. Interface names are the host names for the physical and virtual network interfaces that are configured on the system.
     - Services and ports. The names of the access-allowed services and ports associated with the predefined zone appear.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/add_and_enable_a_firewall_service.html -->

## Control Access to Zone Services

Cockpit administrators can control access to zone services by either adding access to a new
service or removing access from an existing service. Configuration properties for adding or
removing access to zone services are easily configurable using the
Networking page in the web console.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to add or remove access to zone
services.

1. In the Networking page, find the Firewall panel and click Edit rules and zones.

   The names for the allowed services appear in a table under each Zone name.

   Note:

   For single-zone systems, only one zone name appears.
2. In the table, find the zone configuration you want to edit, and perform any of the
   following actions: 
   - Add access to a new service
     1. Click Add services.

        The Add services to zone dialog box appears and displays a list of services you can add to the current zone.
     2. In the Add services to zone dialog box, perform one of the following:
        - Click Services to add services using standard ports.

          Select the individual check boxes for the host system services that you want to add.

          Note:

          Zone services assigned to standard ports are, by default, opened to accept traffic.
        - Click Custom ports to add a service using custom port.

          Enter the following information:

          | Property | Description |
          | --- | --- |
          | TCP or UDP | Enter comma separated ports, ranges, and service accepted. Example:  ``` 22,SSH,80:80,5900-5910 ``` |
          | ID | The ID field automatically generates a custom ID based on the information entered in the TCP or UDP fields. Example:  ``` custom--ssh-ssh-5900-5910 ``` |
          | Description | Enter a description for the accepted service and its custom port numbers. |

          Caution:

          Adding a service with custom ports can automatically reload the `firewalld` service, which can result in the loss of the runtime configurations.
     3. Click Add services.

        The selected services and their associated ports appear in the allowed service access list under the Zone name.
   - Remove access for an existing service

     In the row containing the service you want to remove from the zone, click the actions [â®] menu, then click Delete.

     The selected service disappears from the list of allowed services for the zone.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-network_add_a_pre_defined_zone.html -->

## Add a New Predefined Zone

In addition to the default public predefined zone, the `firewalld`
service provides several other predefined zones for configuration. Configuration properties
for adding other predefined zones are easily configurable using the
Networking page in the Cockpit web console.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to add other
`firewalld` predefined zones to the host system.

1. In the Networking page, find the Firewall panel and click Edit rules and zones. 

   A Firewall page appears listing information for the current zone configurations.
2. In the Firewall page, click Add new
   zone.

   The Add zone dialog box appears.
3. In the Add zone dialog box, perform the following:
   1. Specify the following information: 

      | Property | Description |
      | --- | --- |
      | Trust Level | Select a predefined zone from the list. Upon selecting a predefined zone, the Description property and Service included property identify information about the selected predefined zone and the `firewalld` services included. |
      | Interfaces | Assign host interfaces to the predefined zone. Select the names of the available interfaces from the host interface list. Note: A host interface can't be assigned to more than one zone at a time. By default, `firewalld` pairs all interfaces with the public zone. Therefore, the public zone is the only active zone. A zone is only active if it has at least one interface or source assigned. The `firewalld` service doesn't automatically pair sources (interface IP address ranges) to the public zone. |
      | Allowed addresses | Select one of the following: - Entire subnet. Allows firewall access to the entire subnet. - Range. Enter a specific range of IP addresses that are allowed access through the firewall. |
   2. Click Add zone.

      The name of the newly added zone appears on the Firewall page.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-network_remove_or_modify_zone.html -->

## Remove an Existing Predefined Zone

Cockpit administrators can remove an existing `firewalld` predefined zone using the Networking page in the web console.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to remove an existing zone-based
firewall configuration on the host system.

1. In the Networking page, find the Firewall panel and click Edit rules and zones.

   The Firewall page appears listing information for the current zone configuration(s).
2. In the Firewall page, perform the following steps: 
   1. Find the name of the zone (for example, work zone).
   2. Click the actions [â®] menu (associated with the zone to be
      removed) and select Delete.

      The selected zone is removed from the Firewall page.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-network_control_access_to_interface.html -->

## Monitor or Change Interface Connections

The Interfaces section, on the Networking page of the web console, displays host network information about each configured network interface. Selecting an interface name provides details about the interface, and configurable properties that Cockpit administrators can choose to change. These properties include IP address, MAC address, connection state at reboot, and the interface status state (active or inactive).

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to monitor the host interface network traffic, and to change their configuration.

1. In the Networking page, navigate to the Interfaces panel and view the following information about each host interface. 

   - Interface name, IP address, and inbound and outbound traffic load.
   - At the top of the page, a set of line charts appear. These line charts depict the total traffic load seen across all host interfaces.

     Click the drop-down list to change the interval values appearing on the chart axis labels. By default, each chart depicts the data in 5-minute increments.
2. Click the name of an interface and perform any of the following tasks:

   - Monitor interface performance or review device related details. For example,
     the following interface-specific information appears.
     - Real-time line charts displaying the inbound and outbound traffic load. Click
       the drop-down menu to change the interval values on the line chart axis labels. By
       default, each chart depicts the data in 1-hour increments.
     - Connection name, device manufacturer model name, device status, and carrier
       speed.
     - Configured property values for: device MAC address, IP4 address, IP6 address,
       MTU packet or frame size, and the current toggle switch setting depicting the
       current interface state (inactive or active).
   - Edit the interface configuration properties. Choose to change any of the
     following properties:

     | Property | Action |
     | --- | --- |
     | MAC address Note: This address appears as a 12 digit hexadecimal number with a colon or hyphen separating every two digits (2C:54:91:28:C7:E3). | Click the mac-address link, edit the mac-address shown by selecting an option from the drop-down list, then click Save. |
     | Automatic Connection | Activate or deactivate the network interface connection after a reboot. Do one of the following: - Select the checkbox to automatically activate the connection after a reboot. - Clear the checkbox to automatically deactivate the connection after a   reboot. |
     | IPv4 or IPv6 | Click edit to view and change the IPv4 or IPv6 configuration properties. Choose to set automatic generated IP property values or specify user-defined IP property values. |
     | MTU | Click edit to change the interface maximum transfer unit size (MTU). Choose to set an automatic generated MTU value or specify a user-defined MTU property value. |
     | Toggle switch | Click the toggle switch to control the network interface state (inactive or active). By default, the toggle switch appears blue with a check mark to indicate that the state is active. Clearing the toggle switch deactivates the state. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-network_configure_a_network_bond.html -->

## Configure Network Bonding Properties

Network bonding is the method of joining multiple interfaces together on a host
system to create a bonded interface. A bonded interface can improve network throughput, and
also provide a redundancy plan in the event of a failed interface. The behavior of a bonded
interface is decided by the bonding mode. For example, different modes implement different
levels of bonding for features like load balancing, fault tolerance, and failsafe.

Cockpit administrators can easily create, change, or delete a bonded interface by using the
bonding configuration properties available on the Networking page.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Two or more physical or virtual network devices are installed on the host system.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to create, change, or remove a bonded
interface on the host system.

1. In the Networking page, navigate to the Interfaces panel and perform any of the following: 

   - Create a bonded interface configuration.
     1. Click Add bond.

        The Add bond dialog box appears.
     2. In the Add bond dialog box, specify the following properties and then click Add.

     | Property | Description |
     | --- | --- |
     | Name | Use the default name (for example, Bond0) or type in a user-specified bond name such as bond0 (round robin). |
     | Interfaces | Select the interfaces you want bond from the available interface list. |
     | MAC | In the drop-down list, select the MAC address for the bonded interfaces, or type a user-specified MAC address. |
     | Mode | In the drop-down list, select one of the following bonding modes for the selected bonded interfaces. - Active Backup: A single interface is configured as the primary interface and other interfaces in the bond act as backups if the primary interface fails. - Round Robin: Network traffic is balanced by transmitting in sequential order beginning with the first available interface. If an interface fails, it's skipped in the round-robin selection. - XOR: Network traffic is balanced based on a hash policy derived from interface MAC addresses. This mode ensures that network traffic destined for specific peers always comes from the same physical interface. - Broadcast: All network traffic is sent on all network interfaces. This option includes fault tolerance, but it doesn't include load balancing. - 802.3ad: Uses the IEEE 802.3ad dynamic link aggregation policy and requires an 802.3ad capable switch. Traffic is broadcast in aggregation groups to maximize fault tolerance and to provide load balancing functionality. - Adaptive transmit load balancing: Outgoing traffic is balanced across interfaces within the bond based on each interface's current load. Incoming traffic is delivered to the current active interface. - Adaptive load balancing: This option is similar to dynamic link aggregation, but it requires the use an 802.3ad capable switch. Outgoing traffic is handled in the same manner as adaptive transmit load balancing. Incoming traffic is balanced based on ARP negotiation. |
     | Primary | The Primary property only appears when the Mode is set to Active Backup. In the drop-down list, select the primary active interface device. |
     | Link Monitoring | In the drop-down list, select the applicable link monitoring option. For example: - MII (Recommended): The MII (Media Independent Interface) option is enabled by default. When enabled, this option detects the carrier signal for each interface using the local device driver or the MII registers. Optionally, you can set the    - `Monitoring Interval`check status. Set the interval time (in milliseconds) between the end of the last check and the beginning of the next.   - `Link up delay` timer to prevent fail-overs. Set this delay timer in milliseconds between when a device link is reestablished and when it can used to service network traffic.   - `Link down delay` timer to prevent fail-overs. Set this delay time to indicate how long to wait before switching to another interface when an interface is marked as down. - ARP: The ARP monitor sends ARP queries to peer systems on the network and uses the response to indicate whether an interface is up. The ARP monitor relies on the device driver to track the last transmission and receipt times. If the information isn't updated by the device driver, the interface is marked as down. |
     | Monitoring Level; Link Up; and Link Down | Edit these properties as required. Typically, the default values for these properties are only changed for troubleshooting purposes. |

     The name of the newly bonded interface appears in the Interfaces panel of the Networking page.
   - Edit, disable, or remove existing bonded interface properties.
     1. In the Interfaces panel, click the name of the bonded interface that you want edit.

        The Networking > [bond name] page appears.
     2. In the Networking > [bond name] page, edit the configurable bonding properties as needed. For example:

        | Action | Steps |
        | --- | --- |
        | Toggle the connection state of a bonded interface. | Click the toggle switch to either activate or deactivate the bonded link state. |
        | Delete a bonded configuration | Click Delete (next to the bonded interface name) to remove the bonded interface configuration. |
        | Toggle the connection state of an interface | Click the toggle switch to either activate or deactivate an interface that is part of the bonded interface. |
        | Automatically connect a bonded interface (after reboot) | Select the check box to enable automatic connection after reboot, or clear the check box to disable automatic connection after reboot. |
        | Change addresses (MAC, IPv4, IPv6 addresses) or the MTU size | Click the applicable edit link to change the IPv4 or IPv6 network addressing properties, or the MTU size. |
        | Bond: Modename | Click the edit link to edit any of the applicable properties appearing on the Bond Settings dialog box. For example, mode option, interface assignment, and so on. |
        | Edit interface-specific properties | In the Interface members table, click the name of one of interfaces that's part of the bonded interface, and then as needed, edit any of properties appearing on the Bond Settings dialog box. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-network_configure_a_network_team.html -->

## Configure Network Teaming Properties

Network interface teaming is a feature-rich alternative to network interface
bonding. Teaming, like bonding, is another way to implement network link aggregation, where
one or more interfaces are bundled together to act as one logical link. Network teaming
functionality is provided by the small kernel driver while network bonding functionality is
provided by the bonding driver. For a comparison of the features, see [Teaming and Bonding Feature Comparison](cockpit-network_team_and_bond_feature_comparison.html).

Cockpit administrators can easily create, change, or delete a network teaming interface by
using the teaming configuration properties provided on the Networking
page.

Important:

Starting in Oracle Linux 9, network teaming has been deprecated as a feature in favor of network bonding. If you're using Oracle Linux 9 or later, see [Configure Network Bonding Properties](cockpit-network_configure_a_network_bond.html) for further details.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Two or more physical or virtual network devices are installed on the host system.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to create, change, or remove a network
teaming interface configuration on the host system.

1. In the Networking page, navigate to the Interface panel and
   perform any of the following:

   - Create a bonded interface.
     1. Click Add Team. The Team Settings
        dialog appears.
     2. In the Team Settings dialog, specify the following
        properties and then click Save.

        | Property | Description |
        | --- | --- |
        | Name | Use the default name (for example, team0) or type in a user-specified team name such as team0 (round robin). |
        | Interface Ports | Select the interfaces that you want bundle together from the available port list. |
        | Runner | Runner modes determine the load balancing and fail-over schemes applied to the teamed port interfaces. In the drop-down list menu, select one of the following runner modes for the selected teamed port interfaces.  - Broadcast. All network traffic is sent   across all port interfaces. - Round Robin. Network traffic is balanced   by transmitting in sequential order beginning with the first   available port interface. If an interface fails, it's skipped in   the round-robin selection. - Active Backup. A single port interface or   link is used while other port interfaces act as backups. - LACP. Uses the IEEE 802.3ad dynamic link   aggregation policy and requires an 802.3ad capable switch. Traffic   is broadcast in aggregation groups to maximize fault tolerance and   to provide load balancing functionality. |
        | Link watch | Link watch monitors the state of the teamed port interfaces. In the drop-down list box, select the applicable link watch option. For example:  - Ethtool (Default). Link watch uses the   Oracle Linux ethtool utility for managing the teamed port   interfaces. - ARP. Link watch uses the Oracle Linux   `arp_ping` utility and the Address Resolution   Protocol (ARP) at the data layer to send ARP requests to   destination hosts. |
        | Link Up and Link Down | Set the link up or link down timer delays in milliseconds. Delays enable the teamed port interfaces to synchronize. For `Link up delay`, you might want to specify a time between when a device link is reestablished and when the device can be used to service network traffic. For `Link down delay`, some devices and switches might take some time before their backup mode becomes activated. Specifying a delay prevents a fail-over to immediately occur before those backup devices are ready to be used. |

        The name of the newly teamed port interface appears in
        Interface section of the
        Networking page.
   - Edit, disable, or remove existing team interface properties.
     1. In the Interface table, click the name of a team
        interface that you want edit.

        The Networking [team name]
        page appears.
     2. In the Networking [team name] page, edit the configurable
        teaming properties as needed. For example:

        | Action | Steps |
        | --- | --- |
        | Toggle the connection state of the team interface. | Turn off the toggle switch to deactivate the team interface state or turn on the toggle switch to activate the team interface state. |
        | Delete the team interface configuration | Click Delete (next to the team interface name) to remove the bonded interface configuration. |
        | Toggle the connection state of an interface port | In the Ports table, turn off the toggle switch to deactivate a port or turn on the toggle switch to activate the port. |
        | Automatically connect team interface (after reboot) | Select the checkbox to enable or clear the check box to disable. |
        | Edit the Team: name properties | Click the link to edit any of the applicable properties appearing on the Bond Settings dialog. For example, runner option, interface assignment, and so on. |
        | Edit port-specific properties | In the Port table, click the name of one of ports that's part of the team interface, and then as needed, edit any of properties appearing on the Team Settings dialog |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-network_team_and_bond_feature_comparison.html -->

## Teaming and Bonding Feature Comparison

The following table provides a comparison of the features in Bonding and Teaming.

| Feature | Bonding | Teaming |
| --- | --- | --- |
| broadcast Tx policy | Yes | Yes |
| round-robin Tx policy | Yes | Yes |
| active-backup Tx policy | Yes | Yes |
| LACP (802.3ad) | Yes (active only) | Yes |
| Hash-based Tx policy | Yes | Yes |
| User can set hash function | Yes | Yes |
| Tx load-balancing (TLB) | No | Yes |
| LACP hash port select | Yes | Yes |
| load-balancing for LACP | No | Yes |
| Ethtool link monitoring | Yes | Yes |
| ARP link monitoring | Yes | Yes |
| NS/NA (IPv6) link monitoring | No | Yes |
| ports up/down delays | Yes | Yes |
| port priorities and stickiness (âprimaryâ option enhancement) | No | Yes |
| separate per-port link monitoring setup | No | Yes |
| multiple link monitoring setup | Limited | Yes |
| lockless Tx/Rx path | No (rwlock) | Yes (RCU |
| VLAN | Yes | Yes |
| user-space runtime control | Limited | Full |
| Logic in user-space | No | Yes |
| Extensibility | Hard | Easy |
| Modular design | No | Yes |
| Performance overhead | Low | Very low |
| D-Bus interface | No | Yes |
| multiple device stacking | Yes | Yes |
| zero config using LLDP | No | (in planning) |
| Network Manager integration | Yes | Yes |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/configure_network_bridging.html -->

## Configure Network Bridging Properties

A network bridge joins two or more network segments and enables them to work as a single network. Bridging is implemented at the datalink layer (L2) of the networking stack. Bridges use a packet-forwarding mechanism based on MAC addresses to connect subnetworks together.

Using the bridge properties on the Networking page in the web
console, Cockpit administrators can easily create and maintain host bridge configurations.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Two or more physical or virtual network devices are installed on the host system.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to create, change, or remove a network
bridged configuration on the host system.

1. In the Networking page, navigate to the Interfaces panel and perform any of the following: 

   - Create Linux bridge configuration. Click Add Bridge, specify the following properties in the Add bridge dialog box, and then click Add.

     | Property | Description |
     | --- | --- |
     | Name | In the Name text box, choose to use the default bridge name provided (for example, bridge0) or enter a user-specific bridge name. |
     | Ports | Select the checkbox for each interface you want to add to the bridge. |
     | Options | Select or clear the checkbox for Spanning Tree Protocol support. Note: For multiple or redundant bridge configurations, enabling the Spanning Tree Protocol helps to prevent multiple hops and cyclic routes. |

     The name of the new bridge configuration appears in Interfaces panel of the Networking page.
   - Edit, disable, or remove existing Linux bridge properties.
     1. In the Interfaces panel, click the name of a bridge (for example bridge0) that you want edit.

        The Networking [bridge name] page appears.
     2. In the Networking [bridge name] page, edit the configurable bridge properties as needed. For example:

        | Action | Steps |
        | --- | --- |
        | Toggle the state of a bridge connection | Click the toggle switch to either activate or deactivate the bridge connection state. |
        | Delete a bridge configuration | Click Delete (next to the bridge name) to remove the bridge configuration on the host. |
        | Toggle the state of a bridge port. connection | In the Interface members table, click the toggle switch to either activate or deactivate a port. |
        | Automatically connect bridge configuration (after reboot) | Select the checkbox to enable or clear the check box to disable. |
        | IPv4 or IPv6 Network Address | Click the applicable edit link to change the IPv4 or IPv6 network addressing. |
        | Edit bridge port: bridge name properties | Click the edit link to edit any of the applicable properties appearing on the Add bridge dialog box. For example, bridge name, assigned ports, and to set the spanning tree protocol option. |
        | Edit port-specific bridge properties | In the Interface members table, click a port name that's part of the bridge configuration, and then as needed, edit any of the following port specific property values for MTU, bridge port, and Automatic Connection. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/configure_networking_vlans.html -->

## Configure Network VLAN Properties

A Virtual Local Area Network (VLAN) is a logical network within a physical network. Cockpit administrators can build a VLAN configuration from any of the available network interfaces on the host system. Properties for creating and maintaining a VLAN configuration are available on the Networking page of the Cockpit web console.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The parent VLAN network interface must support VLAN tags.
- The network switch connected to the host system must support VLAN. For more details, see the documentation provided with the switch.
- If you configure the VLAN on top of a bonded interface, the following requirements
  apply:
  - The port connections must be up to support a VLAN configuration over a bonded
    interface.
  - The bond `fail_over_mac=follow` option isn't supported for VLAN
    configurations over a bonded interface.
  - IPv4 from a DHCP server and IPv6 auto configuration options aren't supported on a
    VLAN over a bonded interface.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to create, change, or remove a VLAN
configuration on the host system.

1. In the Networking page, navigate to the Interfaces panel and perform any of the following: 

   - Create VLAN configuration. Click Add VLAN, specify the following properties in the Add VLAN dialog box, and click Add.

     | Property | Description |
     | --- | --- |
     | Parent | In the Parent drop-down list, assign a parent interface to the VLAN configuration. For example, `enp0s3` |
     | VLAN ID | In the VLAN ID field, use the default VLAN ID provided (for example, 1) or enter a user-specified VLAN ID. |
     | Name | In the Name field, keep the default name provided (for example, `enp0s3.1`) or enter a user-specified VLAN name. |

     The name of the new VLAN configuration appears in the Interfaces panel on the Networking page.
   - Edit or remove existing VLAN properties.
     1. In the Interfaces panel, click the name of a VLAN (for example, `enp0s3.1` ) that you want edit.

        The Networking [VLAN name] page appears.
     2. In the Networking [VLAN name] page, edit the configurable VLAN properties as needed. For example:

        | Action | Steps |
        | --- | --- |
        | Toggle the state of a VLAN connection | Click the toggle switch to either activate or deactivate the VLAN connection state. |
        | Delete a VLAN configuration | Click Delete (next to the VLAN name) to remove the VLAN configuration. |
        | Automatically connect the VLAN configuration (after reboot) | Select the checkbox to enable automatic connection after reboot, or clear the check box to disable automatic connection after reboot. |
        | Edit IPv4 or IPv6 Network Address | Click the applicable edit link to change the IPv4 or IPv6 network addressing properties. |
        | Set MTU size | Click edit to change the set MTU size. |
        | Edit VLAN: Parent:  name properties | Click edit to edit any of the applicable properties appearing on the VLAN Settings dialog box. For example, VLAN name, interface assignment, and VLAN ID. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-networ_view_firewall_log_files.html -->

## View Network Host Log Files

The network logs appearing on the Networking page are specific to the NetworkManager service. By default, the 10 most recent log entries appear. The list is identical to the output of the following command:

```
sudo journalctl -u NetworkManager -n 10
```

Using the Networking page in the web console, Cockpit users can click the View all logs option to view a full list of network-related log events. Clicking a log entry in the Networking page or Logs page provides further details about the logged event.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_management.html -->

## 4 Image Builder Management Tasks

Using the Image Builder page in the web console, Cockpit administrators can generate
ready-to-use images suitable for deploying systems or uploading to the cloud. For more details
on how to create images using Image Builder, see the following topics:

- [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- [Getting Started with Image Builder](image-bulder_workflow.html)
- [Create and Manage Blueprints](image_builder_blueprint_mgmnt.html)
- [Create and Manage Images](image_builder_image_mgnmt.html)
- [View and Manage Image Builder Repositories](image_builder_sources.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/install_enable_plugin.html -->

## Install and Configure Image Builder Packages for Cockpit

Before Cockpit administrators can access and use the image builder functionality in the web
console, the following tasks must be completed:

- Install image builder packages and enable the image builder service.

  Note:

  The Image Builder packages aren't typically included during the Oracle Linux installation.
- Verify that the Image Builder add-on application for Cockpit is installed and the Image Builder page is accessible from the web console.

The following instructions explain the process of installing Image Builder packages from the Cockpit web console. For instructions on using the terminal to install Image Builder packages, see:

- [Oracle Linux 10: Creating Custom Images With Image
  Builder](https://docs.oracle.com/en/operating-systems/oracle-linux/10/ibldr/)
- [Oracle Linux 9: Creating Custom Images With Image
  Builder](https://docs.oracle.com/en/operating-systems/oracle-linux/9/ibldr/)
- [Oracle Linux 8: Creating Custom Images With Image
  Builder](https://docs.oracle.com/en/operating-systems/oracle-linux/8/ibldr/)

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The following minimal system requirements must be met to run Image Builder:
  - 2-core processors
  - 4 GiB of memory
  - 20 GiB available disk space in the `/var` directory
  - Access to the Internet
  - Appropriate privileges for performing administrator tasks

Steps

Follow these steps to ensure that the host is properly configured with the Oracle Linux image builder packages and the add-on application for Cockpit.

1. In the web console navigation pane, click Applications.
2. In the Application page, find Image Builder, and then, click Install if the option to install Image Builder appears.

   Note:

   If the Install option doesn't appear, the add-on application is already installed.
3. In the Cockpit navigation pane, click Image Builder.

   When you open the Image Builder page immediately after installation, a message states that OSBuild Composer isn't running.
4. Click Start socket.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image-bulder_workflow.html -->

## Getting Started with Image Builder

You can easily generate ready-to-use images and deploy them to systems and or upload them to
a cloud environment with a basic understanding of the functionality and the workflow involved.
If you're new with building images and are looking to get started using Cockpit to build them,
see the following topics:

- [Image Builder User Interfaces](image-builder_interfaces.html)
- [Terminology and Concepts](image_builder_terminology.html)
- [Workflow for Building Images](image_builder_workflow.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image-builder_interfaces.html -->

## Image Builder User Interfaces

You can interact with Image Builder's functionality through two user interfaces:

- Cockpit web console. Choose this interface to create images through a
  graphical user interface that also provides the ability to switch to a
  text-based terminal environment.

  Note:

  This guide focuses
  on how to use Image Builder from the Cockpit web console interface.
- Command line interface (CLI). Choose this interface to create images by running commands in a text-based terminal or bash-shell environment.

  For more information about building images from the command line, see:

  - [Oracle Linux 10: Creating Custom Images With Image
    Builder](https://docs.oracle.com/en/operating-systems/oracle-linux/10/ibldr/)
  - [Oracle Linux 9: Creating Custom Images With Image
    Builder](https://docs.oracle.com/en/operating-systems/oracle-linux/9/ibldr/)
  - [Oracle Linux 8: Creating Custom Images With Image
    Builder](https://docs.oracle.com/en/operating-systems/oracle-linux/8/ibldr/)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_terminology.html -->

## Terminology and Concepts

Image Builder uses the following terms and concepts:

- Blueprint

  The blueprint functionality provided in Cockpit enables you to define a set of specifications for building a ready-to-use image. These specifications enable you to optionally: 1) select packages to add to an image, and 2) define custom settings, as required, for image properties such as users, groups, firewall ports, services, file systems, ssh keys, and so on.

  Defining a blueprint specification is the first step in the process for composing an image. You can define a blueprint in Cockpit by using the options: Create blueprint or Edit blueprint. You can add a blueprint to the Cockpit host by using the option: Import blueprint. Finally, you can delete a blueprint by using the option: Delete blueprint. For more information about creating and managing blueprints, see [Create and Manage Blueprints](image_builder_blueprint_mgmnt.html).
- Ready-to-Use Images

  Ready-to-Use images are images that are generated by the Image Builder application. They're the final product in image building. All generated images are typically composed using the default source Image Builder repositories and the blueprint.

  Note:

  All generated blueprint images are composed from the specifications defined in the blueprint and the source Image Builder repositories.
- Customizations

  Customizations are optional settings that let you decide what goes into an image.
  All customization settings appear under the section
  Customizations in the Create blueprint
  dialog and the Edit Blueprint dialog. For more
  information about defining customization blueprint properties, see this topic
- Image Builder Source Repositories

  The source repositories are the default repositories that Image Builder uses to compose an image. You can view the source repositories used to compose the image by navigating to the Source section of the Blueprint page. Optionally, you can override the default source by defining repositories other source repositories. For more information about viewing or adding a source repository, see [View and Manage Image Builder Repositories](image_builder_sources.html).
- Image Log File

  For each image created in Cockpit, a log file is generated and available for download on
  the Images section of the Blueprint page.
  This log file captures events associated with the Image Builder composer service. For more
  information about downloading the log file, see [Download an Image Log File](image_builder_dwnld_logdita.html).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_workflow.html -->

## Workflow for Building Images

The following steps outline the process for building a ready-to-use image using the
Cockpit web console.

1. Create or Import a Blueprint – Blueprints provide the specifications for creating a
   ready-to-use image. You can choose to accept all the default property settings, or you can
   optionally add packages and define custom settings for properties such as users, groups,
   firewall ports, ssh keys, services, and so on. For more information on how to create a
   blueprint, or, import a blueprint file to Cockpit, see this topic: [Create and Manage Blueprints](image_builder_blueprint_mgmnt.html).
2. Create an Image From a Blueprint – Creating an image from a blueprint involves
   selecting: 1) the blueprint, 2) an output file type, and 3) an image size. The image
   creation process can take up to 10 minutes to complete. A status message indicating the
   progress of the image appears in the Status column. A
   Ready state appears when the image process completes and is ready
   to download. For further details about creating an image, see [Create an Image From a Blueprint](image_builder_create_image.html).
3. Download the Generated Image – All generated blueprint images appear in the
   Images section of the Blueprint page.
   Clicking Download image enables you to download a generated image for
   use. Optionally, you can download the image log file by clicking Download
   logs. For further details about downloading an image, see [Download a Generated Image](image_builder_dwnldimage.html).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_blueprint_mgmnt.html -->

## Create and Manage Blueprints

Using the Image Builder page in the web console, Cockpit administrators can perform all
things to do with blueprints. The Image Builder page provides configurable options that enable
administrators to create, edit, import, export, or delete a blueprint. For more details, see
these topics:

- [Create a Blueprint](image_builder_createblueprint.html)
- [Import a Blueprint](image_builder_importblueprint.html)
- [Edit Blueprint](image_builder_editblueprint.html)
- [Export Blueprint](image_builder_exportblueprint.html)
- [Delete Blueprint](image_builder_deleteblueprintdita.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_createblueprint.html -->

## Create a Blueprint

Using the Image Builder web console page, Cockpit
administrators can create a blueprint specification for building an image.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For further
  details, see these topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- All Image Builder blueprints require a user-defined name. All other blueprint
  properties such as add on packages and customization properties are optional.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to create an Image Builder blueprint.

1. In the Cockpit navigation pane, click Image Builder, and
   then on the Image Builder page, click Create
   Blueprint.

   The Create Blueprint dialog appears.
2. In the Create Blueprint dialog, define the blueprint specifications as
   follows:
   1. Details section: In the
      Name text box, enter a user-defined name for
      the blueprint. In the Description text box,
      optionally identify the purpose of the blueprint.

      Click Next to advance to the Packages
      section
   2. Packages section (optional): In the
      Available Packages text box, optionally
      search for the names of the packages you want add to the image. Use the
      right-arrow-key to move a selected package to
      the Chosen Package list box. 

      Note:

      The entries appearing in the
      Available Packages text box reflect the
      default packages included in the Oracle Linux distribution that's
      installed on the Cockpit host. To list all the add-on packages
      available, type `*.*` in the
      Available packages text box, and then
      press Enter.

      Click Next to advance to the Customization
      section.
   3. Customization section (optional): Optionally
      define system image configuration properties that are typically defined
      post installation. 

      For example, scroll to Users, click
      Add user to define properties for adding
      a user to an image.

      For descriptions of each customization component, see [Blueprint Customization Components](image_builder_customizationreference.html)

      Click Next to advance to the Review
      section.
   4. Review section: Review the specified blueprint specifications and, if acceptable, click Save to compose the blueprint. 

      The [`user defined`] blueprint name page appears. From this page, you can optionally perform any of the following:
      - Click Back to blueprints to return to the Image Builder page listing all available blueprints on the host.
      - Click Edit blueprint to make further modifications to the newly created blueprint. For more details, see [Edit Blueprint](image_builder_editblueprint.html).
      - Click Create image to generate an image from the newly created blueprint. For more details, see [Create an Image From a Blueprint](image_builder_create_image.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_customizationreference.html -->

## Blueprint Customization Components

| Customization Component | Description |
| --- | --- |
| Kernel | Kernel Command Line Arguments An optional string that appends arguments to the bootloader kernel command line.  Example:  Name: `09_baseos_latest`  Append: `baseurl"https//yum.oracle.com/repo/Oracle``LinuxOL 9baseos/latest/x86_64/"` |
| File systems | File System Partitioning Recommend: Select Use automatic partitioning (default setting).  Manual partition requires setting the mount point and the minimum partition size. |
| Services | Systemd Services Optionally define enabled or disabled services.  Example:  Enabled Services: `"sshd", "cockpit.socket", "httpd"`  Disabled Services: `"postfix"` |
| Firewall | Firewall  - Ports: optional list of   strings containing ports (or port ranges) and protocols to   open. Ports example: `"22:tcp", "80:tcp",   "imap:tcp", "53:tcp"`  Notes:   - Ports are configured using the     `port:protocol` format.   - Port ranges are configured using     `portA-portB:protocol` format. - Enabled Services: Identify an   optional list of services to enable. For example:   `"ftp", "ntp", "dhcp"` - Disabled Services: Identify an   optional list of services to disable. For   example, `"telnet"`. |
| Users | Add user You can optionally add users to an image by defining the properties on the Add user dialog for each user. Note: You can optionally, at a later time, edit the Users section in the blueprint by removing all users or adding more users. |
| Groups | Groups You can optionally add group accounts to an image by defining the properties on the Add group dialog for each group. Note: You can optionally, at a later time, edit the Groups section in the blueprint by removing all groups or adding more groups. |
| SSH Keys | SSH Keys You can optionally add SSH Keys to an image by defining the properties on the Add Key dialog for each SSH Key. Note: You can optionally, at a later time, edit the SSH Keys section in the blueprint by removing all keys or adding more keys. |
| Timezone | Timezone and NTP Servers  - Timezone: Identify an   optional timezone string. The UTC timezone is   used by default. - NTP Servers: Identify an   optional list of strings containing NTP servers   to use. If not provided the distribution defaults are   used. |
| Locale | Local Keyboard and Language  - Keyboard: Identify an optional   string to set the local keyboard. For example, "US" - Language: Identify optional   strings to set the local language. For example,   `"en_US.UTF-8"`. If more than one   language is configured, the first one becomes the   primary, and the others are added as secondary. |
| Other | Host Name and Installation Device  - Hostname: Identify an optional   host name on the image. - Installation device: If image type is   applicable, identify an optional destination device   for the image. For example, `/dev/sda`. |
| FIDO | FIDO Device Onboarding If image type is applicable (such as FIDO images), set the following optional configuration parameters:   - Manufacturer server URL: Identify the   URL address for the manufacture server. - DIUN public key insecure: Identify   the insecure public key. - DIUN public key hash: Identify the   public key hash. - DIUN public key root certs: :   Identify the pubic key root certificates. |
| Ignition | Ignition If image type is applicable, set the optional configuration parameters:.   - Firstboot URL (optional): Identify   the package name you want to add to the generated   image. - Embedded Data: Identify a   `profile_id` security profile to add the   image. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_importblueprint.html -->

## Import a Blueprint

Using the Image Builder page, Cockpit administrators can import a
`toml` formatted blueprint file from another source.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- Blueprint file must be in a `toml` output file format.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to import a blueprint file from
another source.

1. In the Cockpit navigation pane, click Image Builder.

   The Image Builder page appears.
2. In the Image Builder page, do the following: 
   1. Click Import blueprint.
   2. In the Import blueprint dialog, choose to 1) click
      Upload to select a file to upload, or 2) drag a file on to
      the dialog, and then click Import.

      The name of the imported blueprint appears on the Image
      Builder page.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_editblueprint.html -->

## Edit Blueprint

Using the Image Builder page, Cockpit administrators can edit saved
blueprints on the host.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to edit a blueprint file saved on
the host.

1. In the Cockpit navigation pane, click Image Builder.

   The Image Builder page appears.
2. In the Image Builder page, do the following: 
   1. Click the Blueprints link to view all the saved
      blueprints.
   2. Navigate to the name of the blueprint that you want to edit, and then click the
      blueprint name.

      The user-defined blueprint page appears displaying
      the blueprint components.
   3. In the user-defined blueprint page, click Edit
      blueprint.

      The Edit blueprint dialog appears.
   4. In the Edit blueprint dialog, change any of the blueprint
      configuration settings (Details, Packages, Customizations) as needed, and then scroll
      to the Review section and click Save to
      apply the changes.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_exportblueprint.html -->

## Export Blueprint

Using the Image Builder page, Cockpit administrators can export the
`toml` formatted blueprint file saved on the host.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to export a blueprint file saved on
the host.

1. In the Cockpit navigation pane, click Image Builder.

   The Image Builder page appears.
2. In the Image Builder page, do the following:
   1. Click the Blueprints link to view all the saved
      blueprints.
   2. Navigate to the blueprint name that you want to export, and click Export blueprint.

      The Export blueprint dialog appears displaying the contents of the `toml` formatted blueprint file.
   3. In the upper-right corner of the Export blueprint dialog,
      click the down-arrow icon to export the
      `toml` blueprint file to the default file path set on the web
      browser.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_deleteblueprintdita.html -->

## Delete Blueprint

Using the Image Builder page, Cockpit administrators can remove a
saved blueprint on the host.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to remove a blueprint saved on the
host.

1. In the Cockpit navigation pane, click Image Builder.

   The Image Builder page appears.
2. In the Image Builder page, do the following:
   1. Click the Blueprints link to view all the saved
      blueprints.
   2. Navigate to the blueprint name that you want to remove, and then click
      Delete blueprint.

      A Delete blueprint confirmation dialog appears. In
      this dialog, click Delete to remove the blueprint from the
      host.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_image_mgnmt.html -->

## Create and Manage Images

Cockpit users can use the Image Builder page in the web console to
perform all image management tasks. For more details, see the following topics:

- [Create an Image From a Blueprint](image_builder_create_image.html)
- [Download a Generated Image](image_builder_dwnldimage.html)
- [Download an Image Log File](image_builder_dwnld_logdita.html)
- [Delete a Generated Image](image_builder_deleteimage.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_create_image.html -->

## Create an Image From a Blueprint

Using the Image Builder page, Cockpit administrators can create an
image from any saved blueprints on the host.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For further details, see
  these topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- A saved blueprint on the host.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to create an image from an existing
host blueprint.

1. In the Cockpit navigation pane, click Image Builder.

   The Image Builder page appears.
2. In the Image Builder page, do the following:
   1. Click the Blueprints link to view all the saved
      blueprints.
   2. Navigate to the blueprint name that you want to use to create an image, and then
      click Create image. 

      The Create image dialog appears.
   3. In the Create image dialog, do the following:

      |  |  |
      | --- | --- |
      | Specify the name of the blueprint | In the Select a blueprint list box, confirm the correct blueprint name appears. If you need to change the blueprint name, click the down arrow and select the appropriate blueprint name. |
      | Specify the image output type | In the Image output type list box, click the down arrow to select an output file type. Note: For more details about file type, see [Image Output File Types](image_builder_output_formats.html)  Based on the output file type selected, set the following configuration properties that apply, and then click Next.  - Upload to â¦ Select the Upload checkbox to   enable this option or clear the Upload checkbox to   disable this option.  For more details, click the   ? icon to view a description about how to use the   upload functionality. - Image size Click the Up and Down arrow to specify an image   size.  For details, click the ? icon to view a   description about selecting an image size. |

      The Review section appears.
   4. In the Review section, click Create
      to compose an image.

      A message appears indicating that creation of the
      `user-defined` image is added to the queue.

      Note:

      While the image is building, Image Builder automatically
      assigns an image ID and timestamp to the image.

      Note:

      Optionally, you can cancel the image creation process while the image is building
      by clicking Stop build.

      A Ready state appears in the Status
      column when the generated image is ready for use.

      When the Ready state appears, you can optionally perform
      any of the following:
      - [Download a Generated Image](image_builder_dwnldimage.html)
      - [Download an Image Log File](image_builder_dwnld_logdita.html)
      - [Delete a Generated Image](image_builder_deleteimage.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_output_formats.html -->

## Image Output File Types

Image Builder lets you create images in several output formats from the same blueprint. When
choosing an Image output file type in the Create
Image dialog, select the appropriate image output file type for the targeted
deployment environment.

| Image | Output File Type |
| --- | --- |
| Oracle Linux optical disc image | `.iso` |
| Oracle Cloud Infrastructure images | `.qcow2` |
| TAR Archive | `.tar` |
| QEMU QCOW2 image | `.qcow2` |
| Azure Disk Image | `.vhd` |
| Amazon Machine Image Disk | `.raw` |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_dwnldimage.html -->

## Download a Generated Image

Using the Image Builder page, Cockpit administrators can download a
generated image for use.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- A least one generated blueprint image must be available on the host.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to download a generated image for
use.

1. In the Cockpit navigation pane, click Image Builder.

   The Image Builder page appears.
2. In the Image Builder page, do the following: 
   1. Click the Blueprints link to view all the saved
      blueprints.
   2. Click the blueprint name that's associated with the image ID you want to
      download.
   3. In the selected blueprint [name] page, click
      Images to view all the images generated from this
      blueprint.
   4. In the image list, navigate to the image ID that you want to download, and then
      click Download image.

      The generated image is downloaded to the default file path set on the web
      browser. Click the download menu on the browser to open the location of the generated
      file.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_dwnld_logdita.html -->

## Download an Image Log File

Using the Image Builder page, Cockpit administrators can download
the log file that's associated with a blueprint image.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- A least one generated blueprint image must be available on the host.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to download a generated image for
use.

1. In the Cockpit navigation pane, click Image Builder.

   The Image Builder page appears.
2. In the Image Builder page, do the following:

   1. Click the Blueprints link to view all the saved
      blueprints.
   2. Click the blueprint name that's associated with image log file you want to
      download.
   3. In the selected blueprint [name] page, click
      Images to view all the images generated from this
      blueprint.
   4. In the image list, navigate to the image ID that's associated with the log files you
      want to download, and then click Download logs.

      The log files
      are downloaded to the default file path set on the web browser. Click the download
      menu on the browser to open the location of the downloaded log files.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_deleteimage.html -->

## Delete a Generated Image

Using the Image Builder page, Cockpit administrators can remove a
generated image on the host.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- At least one generated image must exist on the host.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to remove a generated image on the
host.

1. In the Cockpit navigation pane, click Image Builder.

   The Image Builder page appears.
2. In the Image Builder page, do the following:
   1. Click the Blueprints link to view all the saved
      blueprints.
   2. Click the user-defined blueprint name that's associated with the image ID you want
      to delete.
   3. In the `user-defined` blueprint page, click
      Images to view all the images generated from the
      blueprint.
   4. In the image list, navigate to the image ID that you want to delete, and then click
      Delete image.

      The Delete image confirmation dialog appears.
   5. In the Delete image confirmation dialog, click
      Delete to remove the image.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder_sources.html -->

## View and Manage Image Builder Repositories

Image Builder by default provides an official set of repositories to build an image. These
repositories are stored in the `/usr/share/osbuild-composer/repositories`
directory and are easily viewable in Cockpit on the Sources page.
Optionally, Cockpit administrators can override the default repositories used to build an
image by defining other source repositories to use. For more information about viewing the
default sources or optionally overriding the default sources, see the following topics:

- [View Repository Sources](image_builder-viewrepositories.html)
- [Add a Custom Repository Source](image_builder-addsources.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder-viewrepositories.html -->

## View Repository Sources

Using the Image Builder page in Cockpit, you can view the default repository sources used
to build an image on the Sources page. This page, for example, lets you identify the name,
type, and URL sources used for: appstream, baseos, and kernel release.

Note:

The default repository sources used for composing an image are also
viewable from the CLI in the `/usr/share/osbuild-composer/repositories`
directory.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)

Steps

Using the Cockpit web console, follow these steps to view the default repository
sources used for composing an image.

1. In the Cockpit navigation pane, click Image Builder.
2. In the Image Builder page, click Sources. 

   The source configuration parameters used for composing an image appear on the page for:
    appstream, baseos, and the
   linux kernel release.

   Optionally, you can:
   - Click the Copy icon to copy the source URLs to a
     clipboard.
   - Click the Add source option to define other sources for
     building an image. For more information about adding other source configurations,
     see [Add a Custom Repository Source](image_builder-addsources.html).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/image_builder-addsources.html -->

## Add a Custom Repository Source

Using the Image Builder page in the Cockpit web console,
administrators can optionally define other repository source configuration parameters for
composing images. For example, the Add source dialog in Cockpit lets
you point to other existing source repositories after defining a valid ID, Name, URL, and
Type.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- Image Builder packages and the web console add-on application must be installed on the host system.

  For details, see [Install and Configure Image Builder Packages for Cockpit](install_enable_plugin.html)
- A custom source repository defined on the Add source dialog must
  be accessible from the Cockpit host system.
- Administrator privileges.

Steps

Using the Cockpit web console, follow these steps to add a custom source repository
for building images.

1. In the Cockpit navigation pane, click Image Builder.
2. In the Image Builder page, click Sources. 

   The Sources page appears displaying the configuration
   parameters for the default repository sources used to build images.
3. In the Sources page, click Add source. 

   The Create source dialog appears.
4. In the Create source dialog, set the following configuration parameters and click Submit. 

   |  |  |
   | --- | --- |
   | ID (required) | In the ID text box, enter the ID assigned to the repository source that you want to add. Example: `ol8_baseos_latest` |
   | Name (required) | In the Name text box, enter the Name assigned to the repository source that you want to add. Example: `Oracle Linux 8 BaseOS Latest (x86_64)` |
   | URL (required) | In the URL text box, enter the URL address assigned to the repository source that you want to add. Example:   ``` https://yum$ociregion.$ocidomain/repo/OracleLinux/OL8/baseos/latest/$basearch/ ``` |
   | Type (required) | In the Type list box, select Yum repository. |
   | Check SSL Signature | Default: Disabled (clear checkbox) Select the Check SSL Signature checkbox to verify the configuration of a signed SSL signature. Otherwise, if checking for a signed SSL signature isn't required, clear the checkbox. |
   | Check GPG Key | Default: Disabled (clear checkbox) Select the Check GPG Key checkbox to verify the configuration of GPG encrypted public and private keys. Otherwise, if checking for the GPG key configuration parameters isn't required, clear the checkbox. |
   | Use RSHM | Default: Disabled (clear checkbox) Select the Use RSHM checkbox to verify the configuration for RSHM subscription management for cloud environments. Otherwise, if checking for an RSHM configuration parameter isn't required, clear the checkbox. |
5. Restart the Cockpit host for the source repository changes to take effect.
6. Log in to the Cockpit web console and verify that the parameters for the custom source
   repository appears in the Sources section of the Image
   Builder page. 

   Image Builder automatically uses the source configuration parameters that appear
   in the Sources section of the Image Builder
   page the next time an image is built.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-podman.html -->

## 5 Podman Management Tasks

Using the Podman page in the web console, Cockpit administrators can monitor and manage
containers, pods, and images on a host system. The Podman page provides configurable options
that enable administrators to create containers and pods, and download Podman images. Options
are also available on the Podman page for filtering container and pod view by owner (for
example, user, system-wide, or all).

For further details about how to use the Podman management functionality from the Cockpit web
console, see the following topics:

- [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html)
- [Podman Image Management](cockpit-podman_managing_podman_images.html)
- [Podman Container Management](cockpit-podman_managing_podman_containers.html)
- [Podman Pod Management](podman_pod_management.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-podman_enable_podman_service.html -->

## Install and Configure Cockpit-Podman

Before Cockpit administrators can access and use the Podman functionality in the web
console, the following tasks must be completed:

- Install the `cockpit-podman` add-on application in the web console.
- Verify that the Podman API socket service is enabled. If this service is disabled,
  start the Podman API socket service.
- Verify that the Podman proxy server settings on the host system are configured for use
  with the Cockpit web console service.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).

Steps

Follow these steps to install the Cockpit-Podman add-on application, start the Podman
API service if not already started, and to verify that the Podman proxy server
settings on the host are configured for use with Cockpit.

1. In the Cockpit web console, click Terminal. 

   The Terminal shell page appears.
2. Type the following to install the Cockpit-Podman add-on application in the web
   console.

   ```
   sudo dnf install -y cockpit-podman
   ```

   For more information about adding applications to the Cockpit web console, see [Install and Manage Add-on Applications](manage_add_on_applications.html).
3. Refresh the web browser to add Podman containers to the Cockpit web console menu.
4. Click Podman containers and verify that Podman API service is running. 

   For example, when the:
   - Podman API service is enabled and running – The Podman page displays the containers, pods, and images that are available on the local system.
   - Podman API service is disabled – The Podman page displays a warning indicating that the Podman service is disabled.

     In the warning dialog, perform the following steps to start the Podman API service.

     1. Select Automatically start podman on boot.

        When this option is checked, the Podman API service automatically starts upon each system power up.
     2. Click Start podman.
5. Ensure that the Podman proxy server settings on the host are configured for use with the Cockpit web console service. 

   For more information, see Configuring Proxy Server Settings in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-podman_managing_podman_images.html -->

## Podman Image Management

Cockpit administrators can easily view, inspect, and manage Podman images on the
Podman page in the web console. For more details, see the following topics:

- [Search and Download New Images](podman_image_download.html)
- [View and Inspect Available Images](podman_view_image.html)
- [Remove Images](podman_remove_image.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_image_download.html -->

## Search and Download New Images

Using the Podman containers page, Cockpit administrators can search and download images from configured Podman registries on the host system.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).

Steps

Using the Cockpit web console, follow these steps to search and download a copy of an
image from a Podman configured registry on the host system.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, navigate to the upper right corner of the Images section, click the actions menu [â®], and then select Download new image. 

   The Search for an image dialog box appears.
3. In the Search for an image dialog box, specify the following properties and then click Download to download a copy of the image to the local container image store. 

   | Property | Action |
   | --- | --- |
   | Owner | Select one of the following: - System: Download images as a system root user. Images are by default stored in the `/var/lib/containers` directory. - Username (logged in user): Download images as a standard user. Images are typically stored in `$HOME/.local/share/containers/storage/` directory. |
   | Search for | In the Search for section, perform the following: 1. Type the name of an image in the first field, and then select the name of the target registry to conduct the search. A list images appear below the search fields. Example: Type Oracle Linux in the first field and select All registries in the second field. A list of all the Oracle Linux images found in all configured registries appear. 2. In the list of images, select the image you want to download. |
   | Tag | The Tag identifies the image version. If a tag name isn't specified, the default tag `latest` is appended to the image filename (image:tag). WARNING: Many tools default to using the `latest` tag if no tag is specified but this can lead to errors and is now considered bad practice.  Recommended action: - In the Tag field, enter a unique name that represents the version of the image. Example: If the image name is Oracle Linux and you know that the software version is 8, in the tag field you would enter 8 (`OracleLinix:8`).  For more information about tagging images, see Oracle Linux Container Image Tagging Conventions in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/). |

   The Search for image dialog box closes and the name of the downloaded image appears in the Images table on the Podman containers page.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_view_image.html -->

## View and Inspect Available Images

Using the Podman containers page, Cockpit users can easily view a listing of all Podman images stored on the host system. Clicking an image provides more details about an image such as image name, owner, creation date, size, and so on.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).
- A copy of one or more images must appear in the Images section on the Podman containers page. For details on how to search and download images, see [Search and Download New Images](podman_image_download.html).

Steps

Using the Cockpit web console, follow these steps to view and inspect available
Podman images stored on the host system.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, use the following read-only properties to view and inspect Podman images appearing in the Images section. 

   | Property | Action |
   | --- | --- |
   | Image totals | At the top of the Podman containers page the following Image total properties appear. - Total number of images: Identifies the total number of images that are available for use on the local host. - Total number of unused images: Identifies the total number of images that aren't used by a container. - Total number of used images: Identifies the total number of images in use by a container. |
   | Show and Hide Images (toggle switch) | Under the Image Totals property, a toggle link appears enabling users to show or hide the current list of images. Tip: To find an image of interest, click Show image, and then use the Owner filtering options at the top of the page. |
   | Listing of Images | The Listing of images appear in a table format. Clicking an image in the table displays the following properties about the image: - Image directory path: Identifies the location of the image file relative to the registry host and the repository directory. For example: `registry.host/repository/imagename:tag` - Owner: Identifies the owner of the image file. - Created: Identifies the image file creation date. - ID: Identifies the unique system ID assigned to the image file. - Disk space: Identifies the size of the image file on the disk. - Used by: Identifies whether the image file is or isn't in use by a container. In addition, clicking the arrow next to the Image directory path displays the following information: - Details: Identifies the image configuration details such as entry point, runtime command, and the exposed ports when available. - History: Identifies the image file timestamp history. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_remove_image.html -->

## Remove Images

Using the Podman containers page, Cockpit administrators can remove a single unused image or remove all unused images on a host system. Typically, images are removed to free up disk space or to download newer versions of an image.

Note:

Images can't be removed when associated with a Podman container. All container image dependencies must be removed before removing an image. For more information about deleting container images, see Working With Container Images in the [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).
- A copy of one or more images must appear in the Images section on the Podman containers page. For details on how to search and download images, see [Search and Download New Images](podman_image_download.html).

Steps

Using the Cockpit web console, follow these steps to remove a single unused image or
all unused images on a host system.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, navigate to the Image section and expand the image listing (if not already expanded) by clicking Show images.
3. To remove unused images, perform the one of the following:

   - Remove all unused images:
     1. Navigate to the top right corner of the Podman containers page, click the actions menu [â®] and then select Prune unused images.

        The Prune unused images dialog box appears.
     2. In the Prune unused images dialog box, click Prune.

        The unused images are removed, and a refreshed image listing appears.
   - Remove a single unused image:
     1. In the Images table, click the row that contains the image you want to delete, and then find the actions [â®] menu in that same row and select Delete.

        The Delete [image file] dialog box appears.
     2. In the Delete [image file] dialog box, click Delete tagged images.

        The unused image is removed, and a refreshed image listing appears.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-podman_managing_podman_containers.html -->

## Podman Container Management

Cockpit users can use the Podman containers page in the web console to monitor and manage all things to do with containers. For example, the Podman containers page provides up-to-date container performance details, container CLI interaction ability, and options to create, run, and change container instances. For more information about using Cockpit to perform Podman container management tasks, see the following topics:

- [Create and Run Container](podman_container_mgmt.html)
- [Special Considerations for Non Administrator Containers](podman_special_considerations.html)
- [Inspect Container and Access Container Logs and CLI](podman_container_inspect_access_cli.html)
- [Rename, Pause, Stop, or Restart Container](podman_container_rename_stop_start.html)
- [Commit Container Changes to Create New Image](podman_commit_changes.html)
- [Checkpoint and Restore a System Container](podman_container_checkpoint_restore.html)
- [Remove Container or Pod Group](podman_container_remove.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_container_mgmt.html -->

## Create and Run Container

Using the Podman containers page, Cockpit administrators can create and run containers with registry images. The Podman containers page provides different options to create a container. For example, administrators can create a container from either the image table, container table, or inside an existing pod group.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).
- One or more registry images must exist in the Image table to create a container from an image. For details on how to search and download registry images, see [Search and Download New Images](podman_image_download.html).
- One or more pod groups must exist in the Container table to create a container inside a
  pod group. For instructions on how to create a pod group, see [Create a Pod Group](podman_create_pod_group.html).

Steps

Using the Cockpit web console, follow these steps to create or create and run a
container.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, perform one of the following:
   - Create a container from an image in the Image table: Navigate to the Image table, find the row with the image that you want to use to create a container, and then in that table row, click Create Container

     The Create container dialog box appears.
   - Create a container from the Container table: Navigate to the Container table and click Create Container.

     The Create container dialog box appears.
   - Create a container in a pod group. Navigate to the Container table, find the row with the pod group that you want to add a container to, and then in that table row click Create a container in pod.

     Note:

     The options to Create a container in a pod group only appear when one or more pod groups exist. For information on how to create a pod group, see [Create a Pod Group](podman_create_pod_group.html)

   The Create container in [pod name group] appears.
3. In the Create container dialog box, perform the following: 
   1. Specify the applicable properties: 

      |  |  |
      | --- | --- |
      | Name | By default, a system generated container name appears in the Name text box. Choose to keep this name or remove it and specify a new name. |
      | Details tab: Owner | The following Owner options appear only for users with administrator or root privileges. - System: Select to create a system ownership pod group. - Username (logged in user): Select to create a local user ownership pod group. Note: The local user ownership pod group is created by default for Cockpit users with limited access privileges. For more information about running pods or containers as a non-root user, see [Special Considerations for Non Administrator Containers](podman_special_considerations.html). |
      | Details tab: Image | Use the Image list box to specify a registry image for the container. For example:  If the Create container dialog box is created from an image in the Image table, the name of the image automatically appears in the Image list.  If an image isn't already specified, perform the following to specify a registry image. - Click the Image list box and select an image saved to cache. -or- - Type a search string in the Image drop down list box and then select one of the following search criteria: All, Local, Oracle Linux, or Docker. In the search results select the appropriate registry image. |
      | Details tab: Command | Use the Command text box to specify the applicable command to run the container image. By default, the run command appears. If required, you can change the command.  Select the option With Terminal to run the container in a terminal. |
      | Details tab: Memory limit | Use the Memory limit controls to specify the minimum memory allocated to run the container. Optional:  Select the Memory limit checkbox and then using the controls specify a minimum memory allocation value. |
      | Details tab: CPU Shares | Note: The CPU Shares property applies only to System container configurations.  CPU shares decide the priority for running containers by the amount of CPU shares allocated to the container. Default value: 1024  Optional:  Select the CPU Shares checkbox and then using the controls specify a CPU shares allocation value. |
      | Details tab: Restart Policy | Note: The Restart Policy property applies only to System container configurations.  Select one of the following: - No (default value): No action. - On Failure: Restarts a container on failure. - Always: Restarts container when exits or after system boot. |
      | Integration tab: Port Mapping | Use the Port Mapping properties to set port mappings between the container and host system. Specifying port mapping exposes services running inside a host container. To set port mappings, do the following: 1. Click Add Port Mapping. 2. Enter an IP address, host port, and container port. 3. Select a Protocol from the list.  For more information about configuring Port Mappings, see Configuring Port Mappings for Containers in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/). |
      | Integration tab: Volumes | Use the Volume properties to share file system space on host system with container. To configure the storage volume properties, do the following: 1. Click Add Volumes. 2. Enter a host path and container path. 3. (Optional) Select the Writable checkbox to create a writable volume. 4. In the SELinux drop down list, select one of the following options: No Label, Shared, or Private.    For more information about configuring SELinux with Podman, see Setting SELinux permission in Containers in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/). |
      | Integration tab: Environment variables | Use the Environment variable properties for when you want to start a process inside the container. To add variables, click Add Variables, and then enter a key and value.  For more information about the use of environment variables for container processes, see the Environment variables section in the Podman man-page. |
      | Health check tab: Command | Enter the command that's run in the container to decide the health of a container.  The command is the value that you might specify when you run a container with the `--healthcheck-command` option with the `podman create` or `podman run` commands.  Health check properties monitor the health or readiness of a process running in a container.  For more information about setting container health properties, see the `podman-run(1)` and `podman-healthcheck-run(1)` manual pages. |
      | Health check tab: Interval, Timeout, Start period, Retries | Set the following health check properties: - Interval (30 second default) - Timeout (30 second default) - Start period - Retries (3 default) |
      | Health check tab: When unhealthy | Select one of the following actions to perform when health checks fail: - No Action - Restart - Stop - Force Stop Note: To configure the custom health check actions, the latest version of Cockpit-Podman must be installed. |
   2. Click one of the following options: 

      - Create and Run – Creates the container, starts the container image, and lists the active container in the Container table as Running.
      - Create – Creates the container and lists the container in the Container table as Created.

        Note:

        You can later run a created container from the Container table by selecting Start from the actions [â®] menu.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_special_considerations.html -->

## Special Considerations for Non Administrator Containers

Review the following special considerations when you're running containers as a non
administrator:

- The storage path for the host container is different for root users (`/var/lib/containers/storage`) and non administrator users (`$HOME/.local/share/containers/storage`).
- Non administrators running containers are provided special permission to run as a range of
  user and group IDs on the host system. However, they have no root privileges to the host
  OS.
- In cases where a non administrator needs to change the `/etc/subuid` or
  `/etc/subgid` manually, the changes take effect only after issuing the
  `podman system migrate` command.
- Some system features are uneditable by non administrators. For example, non administrators
  are unable to change the system clock by setting a `SYS_TIME` capability
  inside a container and running the network time service (`ntpd`).
- A non administrator container is unable to access a port numbered less than 1024.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_container_inspect_access_cli.html -->

## Inspect Container and Access Container Logs and CLI

Using the Podman containers page, Cockpit users can inspect container configuration details, log files, and interact with the container CLI as needed.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).
- One or more containers or pod groups must already exist in the Container table. For
  information on how to create a container or a pod group, see [Create and Run Container](podman_container_mgmt.html) or [Create a Pod Group](podman_create_pod_group.html).
- Administrators or root users can access and change all containers and pods groups. Users
  with limited access privileges can access and change only the containers and pod groups
  that they created.

Steps

Using the Cockpit web console, follow these steps to view container details,
generated log files, and gain access to the container CLI.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, navigate to the Container table.
3. In the Container table, find the container that want you to view
   and then perform the following: 
   1. In the container row, view the following properties:

      - Container name.
      - Container owner (system or user)
      - Container usage properties for CPU and memory.
      - Container state (created, running, stopped, and so on)
   2. Click the arrow icon next to container name to view further details about the
      container. The row expands with the following properties: 

      |  |  |
      | --- | --- |
      | Details tab | View the container ID, creation date, image file path, runtime command, and the container process state. In addition, the following properties are viewable for system containers: IP address, MAC address, and Gateway address. |
      | Integration tab | View the environment variables, port mappings, and configured volumes associated with the container. |
      | Logs tab | View the log files associated with the container. |
      | Console tab | Display and interact with the container CLI. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_container_rename_stop_start.html -->

## Rename, Pause, Stop, or Restart Container

Use the Podman containers page in the Cockpit web console to rename a container or change its operating state.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).
- One or more containers or pod groups must already exist in the Container table. For
  information on how to create a container or a pod group, see [Create and Run Container](podman_container_mgmt.html) or [Create a Pod Group](podman_create_pod_group.html).
- Administrators and root users can access and change all containers. Users with limited
  access privileges can access and change only the containers they created.

Steps

Using the Cockpit web console, follow these steps to rename a container or change the
state of a container.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, navigate to the Container table.
3. In the Container table, find the container row of interest, and
   then within that row, click the actions [â®] menu and select one of
   the following: 
   - Rename. The Rename dialog box appears enabling you to rename the container.

     -OR-
   - Start, Stop, Restart, or Pause. Select one of the applicable actions to
     change the current operating state of the container.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_commit_changes.html -->

## Commit Container Changes to Create New Image

Use the Podman page in the Cockpit web console to commit container
changes to a new image.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).
- One or more containers or pod groups must already exist in the Container table. For
  information on how to create a container or a pod group, see [Create and Run Container](podman_container_mgmt.html) or [Create a Pod Group](podman_create_pod_group.html).
- Administrator or root users can access and change all containers. Users with limited
  access privileges can access and change only the containers they created.

Steps

Using the Cockpit web console, follow these steps to commit a new image based on the
container changes.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, navigate to the Container table.
3. In the Container table, find the container row of interest and click the actions [â®] menu, then select Commit.

   The Commit container dialog box appears.
4. In the Commit container dialog box, specify the following properties and then click Commit. 

   |  |  |
   | --- | --- |
   | New Image Name | Enter a name for the new image. |
   | Tag (Optional) | Enter information to describe the image. |
   | Author (Optional) | Enter the author's name that submitted the changes. |
   | Command (Optional) | Keep or change the runtime command. |
   | Options (Optional) | Select any of the following options that apply: - Pause container when creating image: When selected, the container, and its processes are paused while the image is committed. - Use legacy Docker format: When selected, the Docker image format is used. Otherwise, the OCI format is used. |

   The newly created image appears in the Image table.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_container_checkpoint_restore.html -->

## Checkpoint and Restore a System Container

Use the Podman containers page in the Cockpit web console to set a checkpoint on a system container and save its state to disk. After creating a checkpoint and rebooting the system, you can then as needed, restore the state of the system container to an earlier checkpoint in time.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).
- One or more running containers must already exist in the Container table. For
  information on how to create a container or a pod group, see [Create and Run Container](podman_container_mgmt.html).
- Users must have administrator or root privileges to checkpoint and restore a system
  container.

Steps

Using the Cockpit web console, follow these steps to create and restore a checkpoint on a system container.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, navigate to the Container table.
3. In the Container table, find the row with the running system
   container of interest and then in that same row select Checkpoint
   from the actions [â®] menu.

   The Checkpoint dialog box appears.
4. In the Checkpoint dialog box, select any of the following properties that apply and then click Checkpoint. 

   |  |  |
   | --- | --- |
   | Keep all temporary checkpoint files. (Optional) | Keeps all CRIU created logs and statistical data. |
   | Leave running after writing checkpoint to disk. (Optional) | Leaves the container running after the checkpoint process completes. |
   | Support preserving established TCP connections. (Optional) | Preserves the current container TCP property connections. |

   The checkpoint state for the running container is saved to disk.

   Note:

   The system container can be restored to the saved checkpoint state after a reboot.
5. To restore the checkpoint container, perform the following steps:

   1. If the system didn't reboot after creating the checkpoint, do the following:
      1. Manually reboot the system.
      2. Access the Cockpit web console and open the Podman containers page.
   2. In the Podman containers page of the Cockpit web console, navigate to the row with the checkpoint container and select Restore from the actions [â®] menu.

      The Restore dialog box appears.
   3. In the Restore dialog box, specify any of the following properties that apply and then click Restore.

      |  |  |
      | --- | --- |
      | Keep all temporary checkpoint files. (Optional) | Saves all CRIU temporary logs and properties created during checkpoint process. Note: In the case that the checkpoint operation fails, the temporary files, and their properties remain available for debugging purposes. |
      | Restore with established TCP connections. (Optional) | Reserves the current container TCP property connections. |
      | Ignore IP address if set statically. (Optional) | This option applies only when port mappings were configured. Tries to use the same IP address that was used earlier to start the container. |
      | Ignore MAC address if set statically. (Optional) | Tries to use the same MAC address that was used earlier to run the container. |

      After the system container is restored to the checkpoint state, it appears in the Container table as a running container.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_container_remove.html -->

## Remove Container or Pod Group

Using the Podman containers page, Cockpit users can choose to remove a single container or a pod group of containers.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).
- Stop the container to be remove. For more details, see [Rename, Pause, Stop, or Restart Container](podman_container_rename_stop_start.html).
- Users with limited access privileges can only remove containers and pod groups they
  created. For more details, see [Special Considerations for Non Administrator Containers](podman_special_considerations.html)

Steps

Using the Cockpit web console, follow these steps to remove a single container or
the containers associated with a pod group.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, navigate to the Container table.
3. In the Container table, perform any of the following: 

   - Remove a single container:
     1. Find the row with the stopped container.
     2. In the stopped container row, select Delete from the actions [â®] menu.

        A dialog box appears confirming that you want to delete the container.
     3. Click Delete.
   - Remove a container in a pod group.
     1. Find the pod group row with a stopped container.
     2. In the stopped container row, select Delete from the actions [â®] menu.

        A dialog box appears confirming that you want to delete the container.
     3. Click Delete.
   - Remove a pod group and all containers.
     1. Find the row with the stopped pod group.
     2. In the row with the stopped pod group, select Delete from actions [â®] menu.

        A dialog box appears confirming that you want to delete the pod group and all the containers in that group.
     3. Click Delete.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_pod_management.html -->

## Podman Pod Management

Pods consist of one or more containers that share the same network communication settings, namespace, and service processes. Cockpit users can use the Podman containers page in the web console to create and maintain pods. For example, the Podman containers page provides configurable options for creating pods, adding containers to pods, stopping pods, or starting pods. For more information about using Cockpit to perform pod management tasks, see the following topics:

- [Create a Pod Group](podman_create_pod_group.html)
- [Add a Container to a Pod Group](podman_add_pod_container.html)
- [Inspect and Change a Pod Group](podman_inspect_pod.html)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_create_pod_group.html -->

## Create a Pod Group

Using the Podman containers page, Cockpit users can create an empty pod group. After creating a pod group, users can add and manage containers within the pod group.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).

Steps

Using the Cockpit web console, follow these steps to create a pod group.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, navigate to the Container table and click Create pod.

   The Create pod dialog box appears.
3. In the Create pod dialog box, specify the following properties and then click Create. 

   |  |  |
   | --- | --- |
   | Name | By default, a system provided pod name appears in the Name field. Choose to keep this name or remove it and specify a new name. |
   | Owner | The following Owner options appear only for users with administrator or root privileges. - System: Select to create a system ownership pod group. - User: Select to create a local user ownership pod group. Note: The local user ownership pod group is created by default for Cockpit users with limited access privileges. For more information about running pods or containers as a non-root user, see [Special Considerations for Non Administrator Containers](podman_special_considerations.html). |
   | Port Mapping (optional) | Use the Port Mapping properties to set port mappings between the pod group containers and host system. Specifying port mapping exposes services running inside a host container. To set port mappings, do the following: 1. Click Add Port Mapping. 2. Enter the IP address, host name, and container port. 3. Select a protocol from the drop-down list.  For more information about configuring port mappings, see Configuring Port Mappings for Containers in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/). |
   | Volumes (optional) | Use the Volume properties to share file system space on host system with pod group containers. To configure the storage volume properties, do the following: 1. Click Add Volumes. 2. Enter a host path and container path. 3. (Optional) Select the Writable checkbox to create a writable volume. 4. In the SELinux drop down list, select one of the following options: No Label, Shared or Private.  For more information about volumes, see Setting Up Container Mounts in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).  For more information about configuring SELinux with Podman, see Setting SELinux Permissions for Container and Pod Service Wrappers in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/). |

   An empty pod group is created and appears in the Container table. To add a container to the pod group, see [Add a Container to a Pod Group](podman_add_pod_container.html).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_add_pod_container.html -->

## Add a Container to a Pod Group

Using the Podman web console page, Cockpit users can add a container
to a pod group by creating a container within that group.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).
- One or more pod groups must already exist in the Container table. For information on how
  to create a Pod Group, see [Create a Pod Group](podman_create_pod_group.html).
- Users with limited access privileges can only add containers to a pod group they
  created.

Steps

Using the Cockpit web console, follow these steps to add a container to a pod group.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, navigate to the Container table and find the row with the pod group that you want to add a container and click Create container in pod. 

   The Create container in [pod group name] dialog box appears.
3. In the Create container [pod group name] dialog box, provide the required properties to create a container. For more details, see Step 3 in [Create and Run Container](podman_container_mgmt.html) for instructions. 

   After creating a container in the pod group, the newly added container appears in pod group row of the Container table.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/podman_inspect_pod.html -->

## Inspect and Change a Pod Group

Using the Podman containers page in the Cockpit web console, you can inspect, and change existing pod group configurations as needed. For example, you can view pod groups to inspect container configurations. You can also commit changes, rename, or change the operating state of any container within a pod group. Finally, you can checkpoint, and restore a running pod group container, or remove a pod group as needed.

What Do You Need?

- The Cockpit web console must be installed and accessible.

  For details, see these
  topics: [Install and Enable Cockpit](cockpit-install_install_the_cockpit_package.html) and [Log in to the Cockpit Web Console](cockpit-install_logging_into_cockpit.html).
- The Podman container tools must be installed on the host system.
  For information on how to install Podman, see Installing Podman and Related
  Utilities in [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).
- The Cockpit-Podman add-on application must be installed. For further information on how
  to configure the Cockpit web console to interact with Podman, see [Install and Configure Cockpit-Podman](cockpit-podman_enable_podman_service.html).
- One or more pod groups must already exist in the Container table. For information on how
  to create a Pod Group, see [Create a Pod Group](podman_create_pod_group.html).
- Users with limited access privileges can only access and change the containers and pod
  groups they created.

Steps

Using the Cockpit web console, follow these steps to inspect and change a container
in a pod group.

1. In the Cockpit navigation pane, click Podman containers.

   The Podman containers page appears.
2. In the Podman containers page, navigate to the Container table and find the row with the pod group of interest and perform any of the following: 
   - Inspect a container and access logs or CLI within pod group: For instructions, see [Inspect Container and Access Container Logs and CLI](podman_container_inspect_access_cli.html).
   - Rename or change a container operating state within a pod group: For instructions, see [Rename, Pause, Stop, or Restart Container](podman_container_rename_stop_start.html).
   - Commit container changes to a new image: For instructions, see [Commit Container Changes to Create New Image](podman_commit_changes.html).
   - Checkpoint and restore a system container within a pod group: For instructions, see [Checkpoint and Restore a System Container](podman_container_checkpoint_restore.html).
   - Remove a pod group: For instructions, see [Remove Container or Pod Group](podman_container_remove.html).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-storage_management.html -->

## 6 Storage Management Tasks

Cockpit administrators can use the Storage page in the web console to
help plan and maintain their host system storage needs. The Storage
page provides configurable options for disk partitioning management, data security management,
virtual volume management, and data compression. The Storage page also
provides configurable options to manage NFS and iSCSI storage connections.

For further details about how to use the storage management options from the Cockpit web
console, see the following topics:

- [Storage Management Installation and Overview](cockpit_storage_information.html)
- [Manage Disk Devices and Partitions](cockpit-partition.html)
- [Encrypt Block Devices With LUKS](cockpit-luks.html)
- [Unlock Encrypted Devices Using Tang Server Key](cockpit-nbde.html)
- [Manage Logical Volumes With LVM](cockpit-lvm.html)
- [Build and Manage Software RAID Devices](cockpit-raid.html)
- [Manage NFS Mounted Connections](cockpit-nfsmounts.html)
- [Manage Connections to iSCSI Targets](cockpit_iscsi_targets.html)