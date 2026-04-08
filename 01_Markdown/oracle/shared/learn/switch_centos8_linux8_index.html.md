---
title: "Switch from CentOS to Oracle Linux"
source_url: "https://docs.oracle.com/en/learn/switch_centos8_linux8/index.html"
fetched: 2026-03-26
tags:
  - "oracle-linux"
type: "oracle-doc"
sensitivity: public
---

# Switch from CentOS 8 to Oracle Linux 8

## Introduction

The following tutorial provides step-by-step procedures to automatically switch a CentOS 8 instance to Oracle Linux 8 by removing or replacing any CentOS-specific packages with the Oracle Linux equivalent. The [README.md](https://github.com/oracle/centos2ol) in the Oracle `centos2ol` repository on GitHub states that the script used in this tutorial is a work in progress and not designed to handle all possible configurations.

Please ensure you have a *complete backup* of the system before starting this process if the script cannot successfully convert the system.

Be sure to review the centos2ol project [README.md](https://github.com/oracle/centos2ol) file for the latest details.

### Objectives

In this lab, youâll:

- Check for non-standard kernels
- Ensure the `dnf` configuration is working
- Disable or remove stale and non-CentOS repositories
- Ensure 5GB free space in `/var/cache`
- Disable all automatic updates, including `dnf-automatic`

### Prerequisite

- A system with CentOS 8 installed.

## Check the CentOS Version

1. Open a terminal and connect to your instance.
2. Get the version of CentOS.

   ```
   sudo cat /etc/redhat-release
   ```

   ```
   sudo cat /etc/os-release
   ```

   Both of these commands show the instance is running CentOS 8.

## Check for Non-Standard Kernels

1. Get a list of installed kernels using `yum`.

   ```
   sudo yum list installed kernel
   ```

   The listing shows all the kernels installed using `yum`. We strongly recommend removing all non-standard kernels; for example, any kernel installed and not provided by the base or updates repo. Includes removing any `centosplus` kernels.
2. Get a list of other installed kernels using `grubby`.

   ```
   sudo grubby --info=ALL | grep ^kernel
   ```

   The list shows all the kernels configured for use. Again, we strongly recommend removing all non-standard kernels.

## Remove Non-Standard Kernels with Yum

Because of the [GRUB2 BootHole](https://blogs.oracle.com/linux/cve-2020-10713-grub2-boothole) vulnerability, the Oracle Linux Secure Boot shim can only boot kernels signed by Oracle, and we can only replace the default CentOS kernels. While this may not impact a system if SecureBoot is disabled, enabling it later could render it unbootable. For that reason, we strongly recommend removing all non-standard kernels; for example, any installed kernel not provided by either the `base` or `updates` repo, including the [CentOSPlus](https://wiki.centos.org/AdditionalResources/Repositories/CentOSPlus) kernels.

> **Note:** Skip this section if your system does not have non-standard kernels based on the description above.

1. Remove any non-standard kernels.

   ```
   sudo yum remove <KERNEL>
   ```

   Where `<KERNEL>` is is the complete package name provided by `rpm -q kernel`.

## Remove Non-Standard Kernels with Grubby

`grubby` is a command-line tool for updating and displaying information about the grub boot loaderâs configuration files. This tool allows an administrator to disable kernels installed outside of `yum`.

> **Note:** Skip this section if your system does not have non-standard kernels based on the description in the previous section.

1. Get the index assigned to each of the installed kernelâs boot entries.

   ```
   sudo grubby --info=ALL | grep -E "^kernel|^index"
   ```
2. Remove any non-standard kernelâs boot entries.

   ```
   grubby --remove-kernel=<MENU_INDEX>
   ```

   Where `<MENU_INDEX>` is the index value returned from the previous commandâs output.

## Check DNF Configuration

1. Get a list of enabled repositories.

   ```
   sudo dnf repolist
   ```
2. Update all installed packages.

   ```
   sudo dnf -y upgrade
   ```

## Remove or Disable Non-CentOS Repositories

Disable all non-CentOS repositories. This step helps avoid package conflicts with third-party repositories during the switch. You can re-enable the repos after the switch.

1. Disable non-CentOS repositories.

   ```
   sudo dnf config-manager --set-disabled <REPOSITORY_NAME>
   ```

   Replace `<REPOSITORY_NAME>` with the repository name of any non-CentOS repository enabled on your system.

## Check Free Space in `/var/cache`

1. Get a disk space usage report.

   ```
   df -h
   ```

## Check for Automatic Updates in Cron

There are several ways an administrator can enable automatic updates. This section checks for cron jobs that execute `dnf` directly or using a script. Disable these jobs, if found, to avoid them running during the switching process.

1. List rootâs cron jobs.

   ```
   sudo crontab -l
   ```
2. List the userâs cron jobs.

   ```
   sudo crontab -u <username> -l
   ```

   Where `<username>` is the name of your user account on the system.
3. List daily, hourly, weekly, and monthly cron jobs.

   ```
   sudo ls -al /etc/cron*
   ```

   Then, check the individual files using `less` or the editor of choice.
4. List contents of `/etc/crontab`.

   ```
   sudo less /etc/crontab
   ```

## Disable DNF Automatic Updates

Another way to automatically apply updates is with `dnf-automatic`.

1. Check for the `dnf-automatic` package.

   ```
   sudo dnf list installed dnf-automatic
   ```

   If the output shows the `dnf-automatic` package not installed on your system, skip to the next section.
2. Check the state of the `dnf-automatic` systemd timer.

   ```
   sudo systemctl is-enabled dnf-automatic.timer
   sudo systemctl is-active dnf-automatic.timer
   ```
3. Disable the `dnf-automatic` systemd timer if it is active and running.

   ```
   sudo systemctl stop dnf-automatic.timer
   sudo systemctl disable dnf-automatic.timer
   ```

## Download and Run centos2ol Script

1. Download the `centos2ol.sh` script from GitHub.

   The simplest way to get the script is to use curl:

   ```
   curl -O https://raw.githubusercontent.com/oracle/centos2ol/main/centos2ol.sh
   ```

   If you have Git installed, use the `clone` option to pull the repository from GitHub.

   ```
   git clone https://github.com/oracle/centos2ol.git
   ```
2. Run the `centos2ol.sh` script.

   > If you used `git clone`, change the current working directory to the centos2ol directory.

   See the usage options for the script by passing the option `-h`.

   ```
   sudo bash centos2ol.sh -h
   ```

   Now, run the script and wait for it to complete.

   ```
   sudo bash centos2ol.sh
   ```

   As part of the process, the default kernel is switched to the latest release of Oracleâs Unbreakable Enterprise Kernel (UEK) to enable extensive performance and scalability improvements to the process scheduler, memory management, file systems, and networking stack. We also replace the existing CentOS kernel with the equivalent Red Hat Compatible Kernel (RHCK), which specific hardware or application may require if it has imposed strict kernel version restrictions.
3. Reboot the system.

   ```
   sudo reboot
   ```

## Confirm System Switch to Oracle Linux

1. Using the terminal, again connect to your instance.
2. Check the distribution version and kernel details.

   ```
   cat /etc/os-release
   cat /etc/redhat-release
   uname -r
   ```

## Contribute to the centos2ol GitHub Project

1. Get support.

   Open a [GitHub issue](https://github.com/oracle/centos2ol/issues) for non-security-related bug reports, questions, or requests for enhancements.

## For More Information

[Oracle Linux Documentation](https://docs.oracle.com/en/operating-systems/oracle-linux/index.html)   
[Oracle Linux Training](https://www.oracle.com/goto/oraclelinuxlearning)   
[Oracle Linux Training Station](https://www.oracle.com/goto/oltrain)

## More Learning Resources

Explore other labs on [docs.oracle.com/learn](https://docs.oracle.com/learn) or access more free learning content on the [Oracle Learning YouTube channel](https://www.youtube.com/user/OracleLearning). Additionally, visit [education.oracle.com/learning-explorer](https://education.oracle.com/learning-explorer) to become an Oracle Learning Explorer.

For product documentation, visit [Oracle Help Center](https://docs.oracle.com).

---

[Title and Copyright Information](#copyright-information)

Switch from CentOS 8 to Oracle Linux 8

F41673-08

August 2024

[Copyright Â©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2021,

Oracle and/or its affiliates.