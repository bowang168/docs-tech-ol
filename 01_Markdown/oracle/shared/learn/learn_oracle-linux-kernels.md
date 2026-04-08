---
title: "oracle-linux-kernels"
source_url: "https://docs.oracle.com/en/learn/oracle-linux-kernels"
fetched: 2026-03-26
tags:
  - "oracle-linux"
type: "oracle-doc"
sensitivity: public
---

Note:

- This tutorial is available in an [Oracle-provided free lab environment](https://luna.oracle.com/?ojr=lab%3Blid%3D67f106f2-8c50-442c-b24f-108b806be84f).
- It uses example values for Oracle Cloud Infrastructure credentials, tenancy, and compartments. When completing your lab, substitute these values with ones specific to your cloud environment.

# Manage the Boot Kernel for Oracle Linux

## Introduction

This tutorial describes how to set the default kernel of an Oracle Linux system from the command line. This tutorial is targeted at Oracle Linux 8 users, but the commands are also available on other Oracle Linux releases.

### Background

By default, Oracle Linux systems are configured to boot the most recent kernel version first. In most cases, changing the default kernel is unnecessary.

In previous releases, setting the default kernel was performed by configuring the GRUB boot loader or by using other alternative commands. Now, however, you should preferrably use the **grubby** command to control and manage all of your boot requirements. This tool offers the benefit of being scriptable and can abstract bootloader configuration from the user.

### Objectives

In this lab, youâll learn how to:

- determine the current loaded kernel
- determine the default kernel
- determine which kernel versions are available on the system
- use **grubby** to manage kernels

### What Do You Need?

- Any Oracle Linux system that has the `grubby` package installed

## Check available kernels

> **Note:** Use the free lab environment, see [Oracle Linux Lab Basics](https://luna.oracle.com/lab/c84a78db-4e92-4a58-86d1-a332bf47f99a/steps) for connection and other usage instructions.

Several methods are available for checking which kernels are available on a system:

- Using the **rpm** command.

  ```
  sudo rpm -qa kernel*
  ```

  Note that the command output also includes other kernel related packages and can therefore be confusing.
- Listing the kernels in the `/boot` directory.

  ```
  sudo ls -l /boot/vmlinuz*
  ```

  The command produces an accurate list of kernels available on the system. However, due to the way kernels are named, the kernel version that the system currently uses is not easily identifiable.
- Using the **grubby** command on specific kernels or using the ALL option.

  ```
  sudo grubby --info /boot/vmlinuz-4.18.0*
  sudo grubby --info=ALL
  ```

  The command provides fuller information about the boot configuration associated with each kernel in the systemâs `/boot` directory. The details are based on the GRUB title configuration.

In general, kernels are named to include the upstream version number and the distribution build numbering. The kernel names on Oracle Linux also include indications of whether or not they are standard RHCK or whether they are UEK based. Additionally, the names also identify their system architecture. For example, the `el8` suffix would indicate an RHCK, while `el8uek` would indicate a UEK.

## Check the current default kernel

To check which kernel is already configured as the current default kernel to use at boot, run:

```
sudo grubby --default-kernel
```

To check which kernel is currently running on a system, run:

```
sudo uname -r
```

If the default kernel and the currently running kernel are not identical, the underlying reasons might be one of the following:

- A newer kernel is installed, but the system has not been rebooted.
- During a system reboot, an alternative kernel was manually selected to be the operative kernel.
- The default kernel was manually updated but the system has not been rebooted after the update.

## Change the default kernel

To switch to a different default kernel, run the following command making sure to specify the full path to the designated default kernel:

```
grubby --set-default /boot/vmlinuz-5.2.14-1937.el8uek.x86_64
```

The change takes effect immediately and persists across system reboots.

You can also use the `--set-default-index` option to set the default kernel by its boot entry number. For example, run the following command to set the first boot entry as your default kernel:

```
grubby --set-default-index=0
```

The **grubby** command has additional boot arguments for configuring kernel and boot operations. Refer to the documentation for more information.

## Change kernel command line boot parameters

Use the `--update-kernel` option to update a kenel entry in combination with `--args` to add new arguments or `--remove-args` to remove existing arguments. Multiple arguments can be specified for each option in a quoted space-separated list. You can add and remove arguments in the same operation.

To update a specific kernel, provide the `--update-kernel` option with the full path to the kernel that you wish to update. To update all kernel entries to use a specific kernel boot argument, you can set `--update-kernel=ALL`.

For the purpose of this tutorial you can update all kernel entries to change the loglevel and LANG arguments:

```
grubby --update-kernel=ALL --args "loglevel=3,LANG=en_GB.UTF-8"
```

Use the **grubby info=ALL** command to check that the change is implemented across kernels:

```
grubby --info=ALL
```

## Video Demonstrations

An introductory video that provides an overview of the kernel and underlying system architecture and which demonstrates switching kernel using the **grubby** command is provided at <https://www.youtube.com/watch?v=a0zXGhzPRp8>.

[Linux Architecture and the Kernel](https://www.youtube.com/watch?v=a0zXGhzPRp8)

A more advanced video demonstration and tutorial is provided at <https://www.youtube.com/watch?v=0dv87RFGcKI> if you need more information on working with GRUB2 on Oracle Linux 8.

Note that this tutorial does not describe use of the **grubby** command and explains the underlying components that **grubby** interacts with. For most kernel management requirements on Oracle Linux, the **grubby** tool is sufficient.

[Grub2 Bootloader on Oracle Linux 8](https://www.youtube.com/watch?v=0dv87RFGcKI)

## Additional Information

- `grubby(8)` manual page
- [Oracle Linux 8: Managing Core System Configuration](https://docs.oracle.com/en/operating-systems/oracle-linux/8/osmanage/index.html)
- [Oracle Linux 8 Documentation](https://docs.oracle.com/en/operating-systems/oracle-linux/8/)
- [Oracle Linux and Unbreakable Enterprise Kernel (UEK)
  Releases](https://docs.oracle.com/en/operating-systems/uek/)

## More Learning Resources

Explore other labs on [docs.oracle.com/learn](https://docs.oracle.com/learn) or access more free learning content on the [Oracle Learning YouTube channel](https://www.youtube.com/user/OracleLearning). Additionally, visit [education.oracle.com/learning-explorer](https://education.oracle.com/learning-explorer) to become an Oracle Learning Explorer.

For product documentation, visit [Oracle Help Center](https://docs.oracle.com).

---

[Title and Copyright Information](#copyright-information)

Manage the Boot Kernel for Oracle Linux

F24269-14

November 2023

[Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2021, Oracle and/or its affiliates.