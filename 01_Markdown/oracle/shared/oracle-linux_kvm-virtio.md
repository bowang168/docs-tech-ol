---
title: "Oracle VirtIO Drivers for Microsoft Windows for Use With KVM"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "virtualization"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux

Oracle VirtIO Drivers for Microsoft Windows for Use With KVM

F54847-14

March 2026

---

[Title and Copyright Information](#copyright-information)

Oracle Linux Oracle VirtIO Drivers for Microsoft Windows for Use With KVM

F54847-14

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2020, 2026, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-Preface.html -->

## Preface

[Oracle Linux: Oracle VirtIO Drivers for Microsoft
Windows for Use With KVM](https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/) describes how to install, use, and troubleshoot the Oracle VirtIO Drivers for Microsoft Windows.
Use these instructions if you administer or use guests that run Microsoft Windows in virtualized environments where KVM is the hypervisor.

For Oracle documentation resources, see [Oracle Linux: Oracle VirtIO Drivers for Microsoft
Windows for Use With KVM](https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-WhatsNew.html -->

## 1 About Oracle VirtIO Drivers for Microsoft Windows

The Oracle VirtIO Drivers for Microsoft Windows are paravirtualized drivers for Microsoft Windows guests that run on KVM hypervisors; these drivers improve performance for network and block (disk) devices on Microsoft Windows guests and resolve common issues.

Features in 2.3.2

The Oracle VirtIO Drivers for Microsoft Windows 2.3.2 includes enhancements to the vioscsi
driver to fix an issue that caused page read errors that resulted in Microsoft SQL Server
failure.

Features in 2.3

The Oracle VirtIO Drivers for Microsoft Windows 2.3 provides new support for Microsoft Windows Server 2025.

Features in 2.2

The Oracle VirtIO Drivers for Microsoft Windows 2.2 provides:

- New features:
  - Enables the VirtIO balloon driver so the host can reclaim memory from the guest.
  - Changes the ISO driver folder layout to let the installer automatically load the correct driver, detect the virtual disks, and resume installation.
- Bug fix - VirtIO installer and service updated to support:
  - Support non-KVM to KVM migration for Windows guests that use PC and Q35 machine types.
  - Support installing and upgrading VirtIO drivers for PCI and PCIe devices.

Features in 2.1.0

The Oracle VirtIO Drivers for Microsoft Windows 2.1.0 provides:

- An updated installer which includes better messaging and improved workflows for
  unsupported platforms.
- Support for the VirtIO GPU driver that drives the VirtIO VGA display device designed for
  virtual machines. VirtIO GPU supports system power state S3. You can suspend and wake up
  the Windows system that uses the VirtIO VGA device.
- Bug fixes for the VirtIO storage and network drivers.

Features in 2.0.1

Release 2.0.1 of the Oracle VirtIO Drivers for Microsoft Windows fixes an issue that caused migration failure
when changing from non-KVM environments, such as VMWare or Hyper-V, to KVM environments, such as Oracle
Cloud Infrastructure.

Features in 2.0

The primary focus in release 2.0 of the Oracle VirtIO Drivers for Microsoft Windows is an
improvement in network and block performance. Also, a significant number of bugs are
resolved in this update and the codebase aligns more closely to the upstream release of
these drivers. The update also facilitates the coexistence of third-party vendor drivers
that previously resulted in conflicts and issues.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-SupportedReleasesOperatingSystemsandConfigurationLimits.html -->

## Supported Releases, Operating Systems, and Configuration Limits

The following information pertains to the Oracle Linux and Oracle
Cloud Infrastructure releases that are supported with the
Oracle VirtIO Drivers for Microsoft Windows, in addition to the supported operating systems for each
version of the Oracle VirtIO Drivers for Microsoft Windows.

Information about Microsoft Windows compatibility signing and details on
tested and recommended configuration limits for the Oracle VirtIO Drivers for Microsoft Windows is
also provided.

### Supported Environments

You can use the Oracle VirtIO Drivers for Microsoft Windows Release 2.3.2 with the following environments:

- Oracle Cloud Infrastructure
- Oracle Linux 10.0
- Oracle Linux 9.6
- Oracle Linux 8.10
- Oracle Linux 7.9

### Supported Guest Operating Systems

The following Microsoft Windows operating systems for guest virtual machines that run on KVM have been tested with Oracle VirtIO Drivers for Microsoft Windows:

- Microsoft Windows Server 2025
- Microsoft Windows Server 2022
- Microsoft Windows Server 2019
- Microsoft Windows Server 2016
- Microsoft Windows 11
- Microsoft Windows 10 (64-bit only)

Note:

For information about the supported Microsoft Windows operating systems for the Oracle VirtIO Drivers for Microsoft Windows in the Oracle Cloud Infrastructure environment, see [Bring your own image](https://docs.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm).

#### Virtual Machine Configuration

Virtual machine configuration for the Oracle VirtIO Drivers for Microsoft Windows complies with shape configurations for virtual machines in the Oracle Cloud Infrastructure environment. For more information, see: <https://www.oracle.com/cloud/compute/virtual-machines/>.

### Microsoft Windows Compatibility Signing

The following Microsoft Windows OS have been signed and certified for Oracle VirtIO Drivers
for Microsoft Windows. Oracle has also tested the drivers to ensure they work as expected.

- Microsoft Windows Server 2025
- Microsoft Windows Server 2022
- Microsoft Windows Server 2019
- Microsoft Windows Server 2016
- Microsoft Windows 11
- Microsoft Windows 10 (64-bit only)

Additional information on the certifications can be found at the [Windows Server Catalog](https://www.windowsservercatalog.com).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/discontinued_platforms.html -->

## Discontinued Platforms

The following Windows platforms are no longer supported in the VirtIO drivers because they have reached the end of their product life cycle with Microsoft:

- Microsoft Windows Server 2012
- Microsoft Windows Server 2012 R2
- Microsoft Windows Server 2008 R2
- Microsoft Windows Server 2008 SP2
- Microsoft Windows Server 2008
- Microsoft Windows Server 2003 R2
- Microsoft Windows Server 2003
- Microsoft Windows 2000
- Microsoft Windows NT 4.0
- Microsoft Windows 8
- Microsoft Windows 8.1
- Microsoft Windows 7
- Microsoft Windows 7 SP1
- Microsoft Windows Vista
- Microsoft Windows XP


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-DownloadingtheOracleVirtIODriversforMicrosoftWindows.html -->

## 2 Downloading the Oracle VirtIO Drivers for Microsoft Windows

Before you can install the Oracle VirtIO Drivers for Microsoft Windows you must download them from
[Oracle Software
Delivery Cloud](https://edelivery.oracle.com) or
[My Oracle
Support (MOS)](https://support.oracle.com/portal/).

Follow these steps to download the Oracle VirtIO Drivers for Microsoft Windows from Oracle Software Delivery Cloud:

1. Go to <https://edelivery.oracle.com> and sign in.
2. Search for Oracle Linux.
3. Select one of the following:
   - DLP: Oracle Linux 10.0.0.0.0 (Oracle Linux)
   - DLP: Oracle Linux 9.6.0.0.0 (Oracle Linux)
   - DLP: Oracle Linux 8.10.0.0.0 (Oracle Linux)
   - DLP: Oracle Linux 7.9.0.0.0 (Oracle Linux)
4. Select Continue.
5. In the Platforms / Languages column, select Microsoft Windows x64 (64 bit) and then select Continue.
6. Read and accept the Oracle License Agreement and select Continue.
7. Select the file with the description Oracle VirtIO Drivers for Microsoft Windows Version 2.3.2 and save it to your system.

To download the Oracle VirtIO Drivers for Microsoft Windows from My Oracle Support (MOS):

1. From the MOS home page, select the Patches & Updates tab.
2. In the Patch Search options, enter `27637937` in the Patch Name or Number field and then select Search. Do not select a Platform option.
3. In the search results table, click the `27637937` Patch Name that corresponds to the Oracle VirtIO Drivers for Microsoft Windows Version 2.3.2, which is shown in the Description field.
4. On the Patch Details page, select Download.

   The File Download window opens.
5. Click the link for the zip file and save it to your system.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-InstallingtheOracleVirtIODriversforMicrosoftWindows.html -->

## 3 Installing the Oracle VirtIO Drivers for Microsoft Windows

Installing the Oracle VirtIO Drivers for Microsoft Windows involves configuring Microsoft Windows policies,
running the installation program, and then verifying the
installation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-InstallingtheOracleVirtIODriversforMicrosoftWindowsonExistingMicrosoftWindowsGuests.html -->

## Installing the Oracle VirtIO Drivers for Microsoft Windows on Existing Microsoft Windows guests

To install the Oracle VirtIO Drivers for Microsoft Windows on existing Microsoft Windows guests, perform the
following procedures.

### Configuring Policies for Device Installation

Configure Microsoft Windows policies to let you install the Oracle VirtIO Drivers for Microsoft Windows. If these policies aren't configured, you might see the following error when installing:

```
The installation of this device is forbidden by system policy. 
Contact your system administrator.
```

To configure policies for installation, complete these steps:

1. Open the Microsoft Windows virtual machine on which you want to
   install the Oracle VirtIO Drivers for Microsoft Windows.
2. From the Start menu,
   select
   Run.
3. Enter `gpedit.msc` and
   then click
   OK.

   The Local Group Policy
   Editor is displayed.
4. From the Console Tree,
   display the list of device installation restrictions
   (Device Installation
   Restrictions) as follows:

   1. Expand Computer
      Configuration, and then expand
      Administrative
      Templates.
   2. Expand System, and
      then expand Device
      Installation.
   3. Select Device Installation
      Restrictions.
5. Edit the policy settings so that no device installation
   restrictions are configured.

   Alternatively, review each policy setting to determine the
   correct configuration for your business needs.
6. Close the Local Group Policy
   Editor.
7. Restart the Microsoft Windows virtual machine.

When you are finished configuring the policy settings for
device installation, you can proceed with the installation of
the Oracle VirtIO Drivers for Microsoft Windows.

### Installing Oracle VirtIO Drivers for Microsoft Windows

Before You Begin

Before you start installation, do the following:

- Obtain the Oracle VirtIO Drivers for Microsoft Windows from Oracle Software Delivery Cloud or MOS. See [Downloading the Oracle VirtIO Drivers for Microsoft Windows](kvm-virtio-DownloadingtheOracleVirtIODriversforMicrosoftWindows.html#kvm-virtio-download).
- Review the list of supported Microsoft Windows operating systems and any prerequisite hotfixes. See [Supported Guest Operating Systems](kvm-virtio-SupportedReleasesOperatingSystemsandConfigurationLimits.html#kvm-virtio-supported-os).
- Configure system policies to allow the installation. See [Configuring Policies for Device Installation](kvm-virtio-InstallingtheOracleVirtIODriversforMicrosoftWindowsonExistingMicrosoftWindowsGuests.html#kvm-virtio-install-policy).

Note:

If you're migrating Microsoft Windows guests to OCI, the installer copies the Oracle VirtIO Drivers for Microsoft Windows files, installs the drivers on the guest, and
configures the guest to support migration to OCI.
Migration source environments include OCI Classic, Hyper-V, VMWare, and so on.

You can install the Oracle VirtIO Drivers for Microsoft Windows using the graphical installation program or by performing a silent installation. Use the graphical installation program if you are installing a single instance. If you need to silently install multiple instances, run the installation program in a command line window on at least one Microsoft Windows guest to create a response file, then use this file for silent installations on your other instances.

To install the Oracle VirtIO Drivers for Microsoft Windows, complete the following steps:

1. Copy the Oracle VirtIO Drivers for Microsoft Windows installation program Setup.exe to the guest.
2. Start the installation by running Setup.exe in one of the following ways:

   - To install a single system, double-select `Setup.exe` to start the Oracle VirtIO Drivers for Microsoft Windows installer.
   - To create a response file for automated installations on multiple systems:

     1. Open a command line window.
     2. Go to the directory where you stored Setup.exe.
     3. Run `Setup.exe -r` to start the installer and generate a response file for silent installations.
3. If prompted, select Yes in the User Account Control dialog to allow the installer to continue.

   The Welcome window appears.
4. Select Next.

   The Start to install Oracle VirtIO Drivers for Microsoft Windows Release 2.3.2 window appears, displaying information about your selection.
5. Select Install to begin the installation.

   The installer copies the Oracle VirtIO Drivers for Microsoft Windows files and installs the drivers on the guest.
6. After the installation completes, select Finish.

   The virtual machine restarts.

   Note:

   If you're migrating Windows guests to Oracle Cloud Infrastructure, shut down the Windows guest VM in the source environment and then start the Windows guest VM in the OCI environment.

The Oracle VirtIO Drivers for Microsoft Windows are installed in the following directory:

```
C:\Program Files (x86)\Oracle Corporation\Oracle Windows VirtIO Drivers
```

If you used the `-r` option in the command line, the installation program creates a response file in the `C:\Windows` directory. You then use the response file, `setup.iss`, to perform silent installations on other Microsoft Windows guests. See [Silently Installing or Upgrading the Oracle VirtIO Drivers for Microsoft Windows](kvm-virtio-SilentlyInstallingorUpgradingtheOracleVirtIODriversforMicrosoftWindows.html#kvm-virtio-silent).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-InstallingtheOracleVirtIODriversforMicrosoftWindowsDuringMicrosoftWindowsGuestInstallation.html -->

## Installing the Oracle VirtIO Drivers for Microsoft Windows During Microsoft Windows Guest Installation

Before You Begin

Do the following before you start the installation process:

- Obtain the Oracle VirtIO Drivers for Microsoft Windows from Oracle Software Delivery Cloud or MOS. See [Downloading the Oracle VirtIO Drivers for Microsoft Windows](kvm-virtio-DownloadingtheOracleVirtIODriversforMicrosoftWindows.html#kvm-virtio-download).
- Review the list of supported Microsoft Windows operating systems and
  any prerequisite hotfixes. See
  [Supported Guest Operating Systems](kvm-virtio-SupportedReleasesOperatingSystemsandConfigurationLimits.html#kvm-virtio-supported-os).

To install the Oracle VirtIO Drivers for Microsoft Windows during installation of a Microsoft Windows guest, do the following:

1. Create the virtual machine, but do not start it.
2. Attach the Oracle VirtIO Drivers for Microsoft Windows ISO file to the virtual machine as an emulated IDE device. You can find the `winvirtio.iso` file in the Oracle VirtIO Drivers for Microsoft Windows zip file you downloaded.

   Ensure that the Microsoft Windows guest installation ISO is attached to the virtual machine as the first IDE device. The Oracle VirtIO Drivers for Microsoft Windows ISO file is typically the second IDE device.
3. Start the virtual machine and begin the Microsoft Windows installation process.
4. When the disk or partition screen displays, follow the
   prompts to browse and load drivers.
5. Navigate to the appropriate driver location on the Oracle VirtIO Drivers for Microsoft Windows ISO file and then select them.

   The contents of the Oracle VirtIO Drivers for Microsoft Windows ISO file are as follows:

   ```
   autorun.inf      # File that automatically runs the installation program.
   fwcfg            # Directory that contains the license file for fwcfg null drivers.
   Setup.exe        # The main graphical installation program.
   NetKVM           # Directory that contains the license file for NetKVM drivers.
   pvpanic          # Directory that contains the license file for pvpanic drivers.
   viogpu           # Directory that contains the license file for viogpu drivers.
   vioscsi          # Directory that contains the license file for vioscsi drivers.
   vioserial        # Directory that contains the license file for vioserial drivers.
   viostor         # Directory that contains the license file for viostor drivers.
   balloon          # Directory that contains the license file for balloon drivers.

   vio              # Base directory for drivers.
   vio/Common       # Fwcfg null drivers for all Windows versions.

   vio/Win10        # Drivers for Windows 10, Windows Server 2016, Windows Server 2019 and Windows Server 2022.
   vio/Win10/amd64  # 64-bit drivers.

   vio/Win11        # Drivers for Windows 11 and Windows Server 2025.
   vio/Win11/amd64  # 64-bit drivers.
   ```
6. Repeat the preceding step to install other drivers as necessary and then continue with the Microsoft Windows installation process.

After you install the Microsoft Windows guest, you must configure Microsoft Windows policies. See [Supported Guest Operating Systems](kvm-virtio-SupportedReleasesOperatingSystemsandConfigurationLimits.html#kvm-virtio-supported-os).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-UpgradingtheOracleVirtIODriversforMicrosoftWindows.html -->

## 4 Upgrading the Oracle VirtIO Drivers for Microsoft Windows

You can upgrade an installation of the Oracle VirtIO Drivers for Microsoft Windows using the graphical installation program or by performing a silent upgrade. Use the graphical program to upgrade one system, or run it once at the command line to create a response file for silent upgrades on multiple systems.

To upgrade the Oracle VirtIO Drivers for Microsoft Windows, follow these steps:

1. Copy the Oracle VirtIO Drivers for Microsoft Windows installation program, `Setup.exe`, to the guest.
2. Do one of the following:
   - Double-click `Setup.exe` to begin the upgrade.
   - Open a command line window and then do the following:
     1. Navigate to the directory where the `Setup.exe` file is located.
     2. Run the `Setup.exe -r` command to begin the upgrade and create a response file for silent installations.
3. If prompted, select Yes in the User Account Control dialog to allow the Oracle VirtIO Drivers for Microsoft Windows installer to proceed.

   Oracle VirtIO Drivers for Microsoft Windows user account control dialog

     
     

   The initial upgrade window is displayed.
4. Click Next to start the upgrade.

   The installation program then copies new versions of the Oracle VirtIO Drivers for Microsoft Windows to the system and updates the installed drivers. The Update Complete window is displayed.
5. Click Yes, I want to restart the system now and then click Finish to restart the virtual machine.

If you used the `-r` option in the command line,
the installation program creates a response file in the
`C:\Windows` directory. You then use the response
file, `setup.iss`, to perform silent upgrades on
other Microsoft Windows guests. See [Silently Installing or Upgrading the Oracle VirtIO Drivers for Microsoft Windows](kvm-virtio-SilentlyInstallingorUpgradingtheOracleVirtIODriversforMicrosoftWindows.html#kvm-virtio-silent).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-SilentlyInstallingorUpgradingtheOracleVirtIODriversforMicrosoftWindows.html -->

## 5 Silently Installing or Upgrading the Oracle VirtIO Drivers for Microsoft Windows

You can use a response file that you create with the graphical
installation program to silently install or upgrade the Oracle VirtIO Drivers for Microsoft Windows.
The response file provides the prompts that the installation
program requires to successfully install or upgrade the Oracle VirtIO Drivers for Microsoft Windows.

Important:

Oracle VirtIO Drivers for Microsoft Windows must be signed by Microsoft to perform a silent installation or upgrade. See [Microsoft Windows Compatibility Signing](kvm-virtio-SupportedReleasesOperatingSystemsandConfigurationLimits.html#kvm-virtio-signed-os).

To install or upgrade the Oracle VirtIO Drivers for Microsoft Windows silently, follow these steps:

1. Complete at least one installation or upgrade of the Oracle VirtIO Drivers for Microsoft Windows
   by using the GUI installation program to create a response
   file. See [Installing Oracle VirtIO Drivers for Microsoft Windows](kvm-virtio-InstallingtheOracleVirtIODriversforMicrosoftWindowsonExistingMicrosoftWindowsGuests.html#kvm-virtio-install)
   or [Upgrading the Oracle VirtIO Drivers for Microsoft Windows](kvm-virtio-UpgradingtheOracleVirtIODriversforMicrosoftWindows.html#kvm-virtio-upgrade).
2. Locate the response file, `setup.iss`, in the
   `C:\Windows` directory on the file system of
   the computer where you ran the graphical installation program.
3. Copy `setup.iss` to the same directory as the
   Oracle VirtIO Drivers for Microsoft Windows installation program. Alternatively you can specify
   the location of the response file at the command line.
4. Open a command line window.
5. Run the `Setup.exe -s` command to silently
   install or upgrade the Oracle VirtIO Drivers for Microsoft Windows with the response file.

   You can include the following options at the command line:

   - `-f1c:path\to\``setup.iss`
     to specify the location of `setup.iss`.

     For example, `Setup.exe -s
     -f1c:\Users\Username\setup.iss`.
   - `-f2c:path\to\setup.log`
     to specify the location of
     `setup.log`. By
     default, log files are written to the
     `C:\Windows` directory, for example,
     `Setup.exe -s
     -f2c:\Users\Username\setup.log`.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-UninstallingtheOracleVirtIODriversforMicrosoftWindows.html -->

## 6 Uninstalling the Oracle VirtIO Drivers for Microsoft Windows

You can uninstall the Oracle VirtIO Drivers for Microsoft Windows by using the Microsoft Windows control panel, or by running the installation program that you used to install the drivers.

To uninstall using the Microsoft Windows control panel, complete these steps:

1. Open the control panel and navigate to the
   Uninstall or change a
   program section.

   Note that the name of this section might be different, depending on your version of Microsoft Windows.
2. Locate, then select the Oracle VirtIO Drivers for Microsoft Windows.
3. Right-click the Uninstall
   option.

   The installation program starts and prompts you to confirm the
   uninstallation.
4. Select Yes when prompted
   to remove the application.

   The installation program removes the Oracle VirtIO Drivers for Microsoft Windows and deletes the
   binaries from your system.
5. When prompted, select Yes, restart
   the system and then click
   Finish to complete the
   uninstallation.

To uninstall using the installation program:

1. Double-click `Setup.exe` to start the
   Oracle VirtIO Drivers for Microsoft Windows installer.

   The installation program starts and prompts you to modify the current installation. You
   are able to select either Repair or
   Remove.
2. Select Remove and then
   click Next.
3. Select Yes from the pop-up
   dialog.

   The installation program removes the Oracle VirtIO Drivers for Microsoft Windows and deletes the
   binaries from your system.
4. When prompted, select Yes, restart the system and then click Finish to complete the uninstallation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/kvm-virtio/kvm-virtio-KnownLimitationsandWorkarounds.html -->

## 7 Known Limitations and Workarounds

There are no known limitations or workarounds.