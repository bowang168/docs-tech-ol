---
title: "sboot-module"
source_url: "https://docs.oracle.com/en/learn/sboot-module"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "system-management"
type: "oracle-doc"
sensitivity: public
---

Note:

- This tutorial requires access to Oracle Cloud. To sign up for a free account, see [Get started with Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/en/learn/cloud_free_tier/index.html).
- It uses example values for Oracle Cloud Infrastructure credentials, tenancy, and compartments. When completing your lab, substitute these values with ones specific to your cloud environment.

# Sign Kernel Modules for Use With UEFI Secure Boot

This tutorial explains how to sign your own modules to use with UEFI Secure Boot on Oracle Linux with Unbreakable Enterprise Kernel installed. The tutorial also explains how to add your own certificate to the kernelâs trusted certificate keyring in the case that you are using a UEK R6 kernel prior to UEK R6U3; and also how to use the mokutil utility to update the UEFI boot shim with the signing certificate.

> **Warning**  
> This tutorial is intended for developers who are performing software testing. **Do not use the procedures in this tutorial on production systems supported by Oracle.**

## Prerequisites

- Oracle Linux system (either Oracle Linux 7 or Oracle Linux 8)
- System is running the latest UEKR6 kernel
- Firmware implementation and configuration of the server supports MOK utility (see <https://docs.oracle.com/en/learn/mokutil-uefi/> for more information)

## Objectives

At the end of this tutorial, you should be able to do the following:

- Sign modules to use with UEFI Secure Boot
- Add certificates to the kernelâs trusted certificates keyring
- Use the `mokutil` utility to update the UEFI boot shim with the signing certificate

## Installing Required Packages

1. Run the following commands based on your Oracle Linux system.

   - Oracle Linux 8

     ```
     sudo dnf update
     sudo dnf group install "Development Tools"
     sudo dnf install kernel-uek kernel-uek-devel keyutils mokutil pesign
     ```
   - Oracle Linux 7

     ```
     sudo yum-config-manager --enable ol7_optional_latest
     sudo yum update
     sudo yum group install "Development Tools"
     sudo yum-config-manager --enable ol7_UEKR6 && yum-config-manager --disable ol7_UEKR5
     ```
2. Reboot the system.

## Creating a sample custom kernel module

For the purpose of this tutorial, we create and build a sample custom kernel module. In most cases, the module is already provided by an external vendor and this step is not necessary. The process described here is for illustrative purposes.

1. Create a `~/hello` directory.
2. Create the file `~/hello/hello.c` with the following entries:

   ```
   #include <linux/module.h>  
   #include <linux/kernel.h>  
   #include <linux/init.h>

   MODULE_LICENSE("GPL");  
   MODULE_AUTHOR("A.Developer");  
   MODULE_DESCRIPTION("Hello World Linux Kernel Module");

   static int __init hello_init(void)
   {  
     printk(KERN_INFO "Hello world!\n");  
     return 0;
   }

   static void __exit hello_exit(void)  
   {  
     printk(KERN_INFO "Unloading Hello world.\n");  
   }

   module_init(hello_init);
   module_exit(hello_exit);
   ```
3. Create the file `~/hello/Makefile` with the following entries:

   ```
   obj-m += hello.o

   all:  
     make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

   clean:  
     make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

   install:  
     cp hello.ko  /lib/modules/$(shell uname -r)/extra  
     depmod
   ```
4. Build and then install the module.

   ```
   cd ~/hello
   make && sudo make install
   ```
5. Test the module.

   ```
   sudo modprobe hello

   modprobe: ERROR: could not insert 'hello': Operation not permitted
   ```

   If the system is running in Secure Boot mode, `modprobe` fails because the module is not yet valid.

## Creating local certificates and signing the module

1. Create an OpenSSL configuration file to create a local signing certificate.

   Type:

   ```
   cat >>/tmp/x509.conf <<EOF
   [ req ]
   default_bits = 4096
   distinguished_name = req_distinguished_name
   prompt = no
   string_mask = utf8only
   x509_extensions = extensions

   [ req_distinguished_name ]
   O = Module Signing Example
   CN = Module Signing Example Key
   emailAddress = first.last@example.com

   [ extensions ]
   basicConstraints=critical,CA:FALSE
   keyUsage=digitalSignature
   subjectKeyIdentifier=hash
   authorityKeyIdentifier=keyid
   EOF
   ```

   For the *O*, *CN*, and *emailAddress* fields, enter values that are more appropriate.
2. Generate a new private/public key pair based on the new configuration.

   Note that the certificate is valid for 10 years (3,650 days).

   ```
   mkdir ~/certs
   cd ~/certs
   openssl req -x509 -new -nodes -utf8 -sha512 -days 3650 -batch -config /tmp/x509.conf -outform DER -out pubkey.der -keyout priv.key

   Generating a RSA private key
   ........................................................
   ............................++++
   writing new private key to 'priv.key'
   -----
   ```
3. Export the certificate in PEM format.

   ```
   openssl x509 -inform DER -in pubkey.der -out pubkey.pem
   ```
4. Create a PKCS#12 version of the certificate.

   Specify the export password when prompted.

   ```
   openssl pkcs12 -export -inkey priv.key -in pubkey.pem -name cert -out cert.p12

   Enter Export Password:
   Verifying - Enter Export Password:
   ```
5. Sign the module using the key you just generated.

   ```
   cd ~/certs
   sudo /usr/src/kernels/$(uname -r)/scripts/sign-file sha512 priv.key pubkey.der /lib/modules/$(uname -r)/extra/hello.ko
   ```
6. With the `modinfo` command, verify that the module is signed with the key that you created.

   ```
   modinfo hello

   filename:       /lib/modules/5.4.17-2036.103.3.1.el8uek.x86_64/extra/hello.ko
   description:    Hello World Linux Kernel Module
   author:         A.Developer
   license:        GPL
   srcversion:     D51FB4CF0B86314953EE797
   depends:        
   retpoline:      Y
   name:           hello
   vermagic:       5.4.17-2036.103.3.1.el8uek.x86_64 SMP mod_unload modversions 
   sig_id:         PKCS#7
   signer:         Module Signing Example Key
   sig_key:        AB:2C:E3:AB:87:D9:9C:6A:31:B8:80:20:D4:92:25:F3:9A:26:DC
   sig_hashalgo:   sha512
   signature:      9F:B0:25:CB:14:C1:C7:10:7F:60:1E:E6:66:82:64:58:91:1F:01:A5:
                   D9:03:1B:9C:2D:42:00:45:78:2B:FA:70:F8:C7:3B:1A:A2:42:00:09:
                   33:E0:81:1D:C6:E6:46:A5:FE:8B:9F:8C:3D:4E:A1:3A:05:52:ED:F6:
                   25:F9:88:98:D3:70:78:1D:7E:63:F3:73:C8:C8:14:C2:3A:52:B4:8F: 
                   ...
   ```

## Adding the certificate to the kernel trusted keyring (UEK R6U2 and below)

> **Note:**  
> You do not need to perform this step if you are running UEK R6U3 or later. The Secure Boot implementation in UEK R6U3 is updated to allow module loading for modules signed with keys that are in the MOK database. For UEK R6 releases prior to UEK R6U3, modules are only able to load if the keys with which they are signed are in the kernelâs built-in trusted keyring.

1. Create an NSS database to use with `pesign`.

   ```
   cd ~/certs
   certutil -d . -N

   Enter a password which will be used to encrypt your keys.
   The password should be at least 8 characters long,
   and should contain at least one non-alphabetic character.

   Enter new password:
   Re-enter password:
   ```
2. Add the PCKS#12 key to the database.

   ```
   cd ~/certs
   pk12util -d . -i cert.p12

   Enter Password or Pin for "NSS Certificate DB":
   Enter password for PKCS12 file:
   pk12util: PKCS12 IMPORT SUCCESSFUL
   ```
3. Insert the key into the kernelâs `bzImage`.

   > **Note:** Only a single additional custom certificate can be added to the kernel because the compressed size of the kernelâs boot image cannot increase.

   ```
   cd ~/certs
   sudo /usr/src/kernels/$(uname -r)/scripts/insert-sys-cert -s /boot/System.map-$(uname -r) -z /boot/vmlinuz-$(uname -r) -c pubkey.der

   INFO:    Executing: gunzip <vmlinux-ceDv0X >vmlinux-rFFumH
   WARNING: Could not find the symbol table.
   INFO:    sym:    system_extra_cert
   INFO:    addr:   0xffffffff828915d6
   INFO:    size:   8194
   INFO:    offset: 0x1c915d6
   INFO:    sym:    system_extra_cert_used
   INFO:    addr:   0xffffffff828935d8
   INFO:    size:   0
   INFO:    offset: 0x1c935d8
   INFO:    sym:    system_certificate_list_size
   INFO:    addr:   0xffffffff828935e0
   INFO:    size:   0
   INFO:    offset: 0x1c935e0
   INFO:    Inserted the contents of pubkey.der into ffffffff828915d6.
   INFO:    Used 1481 bytes out of 8194 bytes reserved.
   INFO:    Executing: gzip -n -f -9 <vmlinux-rFFumH >vmlinux-5wHA2r
   ```
4. Remove the existing PE signature and re-sign the kernel with the new one by using the NSS database password that you created previously.

   ```
   cd ~/certs
   sudo pesign -u 0 -i /boot/vmlinuz-$(uname -r) --remove-signature -o vmlinuz.unsigned
   sudo pesign -n . -c cert -i vmlinuz.unsigned -o vmlinuz.signed -s

   Enter Password or PIN for 'NSS Certificate DB":
   ```
5. Copy the signed kernel back to `/boot`.

   ```
   cd ~/certs
   sudo cp -bf vmlinuz.signed /boot/vmlinuz-$(uname -r)
   ```

## Enrolling the certificate into the UEFI Secure Boot key database

For UEK R6 kernels prior to UEK R6U3, you must enroll the key that was used to sign the kernel image into the MOK database. For all other kernels, the key that is used to sign the module itself is enrolled into the database. These keys might be the same if you used the same key to sign the module and the kernel.

> **Note:** For more information about using the `mokutil` utility, see <https://docs.oracle.com/learn/mokutil-uefi/>.

1. Add the appropriate key as a Machine Owner Key (MOK) to the UEFI boot shim.
   The `mokutil import` command prompts you to enter a password that you will need to provide in the next step.

   ```
   sudo mokutil --import pubkey.der

   input password:
   input password again:
   ```
2. Reboot your machine.

   On reboot, the UEFI SHIM should automatically start MokManager which is used to add the MOK key to the UEFI Secure Boot key database.

   1. Press a key to perform MOK Management.  
      Be sure to press a key within 10 seconds to interrupt the boot process to add your MOK key.
   2. Select Enroll MOK.
   3. Select View key 0.
   4. Verify that the key matches the values you want.
   5. Press any key, then select continue.
   6. Select Yes to enroll the key.
   7. Provide the password used when you imported the key using mokutil.
   8. Select reboot.
3. Verify that the certificate is installed in the trusted keyring.

   ```
   sudo keyctl show %:.builtin_trusted_keys

   Keyring
    892034081 ---lswrv      0     0  keyring: .builtin_trusted_keys
    367808024 ---lswrv      0     0   \_ asymmetric: Oracle CA Server: fbcd3d4d950c6b2b0e01f0a146c5a4e3855ae704
    230958440 ---lswrv      0     0   \_ asymmetric: Module Signing Example Key: a43b4e638874b0656db2bc26216f56c0ac39f72b
    408597579 ---lswrv      0     0   \_ asymmetric: Oracle America, Inc.: Ksplice Kernel Module Signing Key: 09010ebef5545fa7c54b626ef518e077b5b1ee4c
    839574974 ---lswrv      0     0   \_ asymmetric: Oracle Linux Kernel Module Signing Key: 2bb352412969a3653f0eb6021763408ebb9bb5ab
   ```
4. Verify that the module can load successfully.

   ```
   sudo modprobe hello
   lsmod | grep hello
   hello                  16384  0

   dmesg | tail -2
   [  108.848848] hello: loading out-of-tree module taints kernel.
   [  108.849191] Hello world!
   ```

## Known Issues

The following kernel versions on Oracle Linux 7 may have issues accepting a new certificate while maintaining the same (or smaller) compressed size for the resulting `vmlinuz` file. It is recommended that you update to the latest available UEKR6 release before starting this process.

- 5.4.17-2022.el7uek.x86\_64
- 5.4.17-2023.el7uek.x86\_64
- 5.4.17-2025.el7uek.x86\_64
- 5.4.17-2026.el7uek.x86\_64
- 5.4.17-2028.1.el7uek.x86\_64
- 5.4.17-2028.el7uek.x86\_64
- 5.4.17-2011.3.2.el7uek.x86\_64
- 5.4.17-2011.4.0.el7uek.x86\_64
- 5.4.17-2013.el7uek.x86\_64
- 5.4.17-2016.1.el7uek.x86\_64

The compression issue is not observed in the equivalent versions of these kernels on Oracle Linux 8.

## For more information

- [Oracle Linux: Working With UEFI Secure Boot](https://docs.oracle.com/en/operating-systems/oracle-linux/secure-boot/)
- [Oracle Linux UEFI Secure Boot Update Notices](https://docs.oracle.com/en/operating-systems/oracle-linux/notice-secure-boot/)
- [Oracle Linux: Managing Certificates and Public Key Infrastructure](https://docs.oracle.com/en/operating-systems/oracle-linux/certmanage/)
- [Oracle Linux and Unbrekable Enterprise Kernel (UEK) Releases](https://blogs.oracle.com/scoter/oracle-linux-and-unbreakable-enterprise-kernel-uek-releases)
- mokutil(1) manual page
- pesign(1) manual page
- `pesign --help` command

## More Learning Resources

Explore other labs on [docs.oracle.com/learn](https://docs.oracle.com/learn) or access more free learning content on the [Oracle Learning YouTube channel](https://www.youtube.com/user/OracleLearning). Additionally, visit [education.oracle.com/learning-explorer](https://education.oracle.com/learning-explorer) to become an Oracle Learning Explorer.

For product documentation, visit [Oracle Help Center](https://docs.oracle.com).

---

[Title and Copyright Information](#copyright-information)

Sign Kernel Modules for Use With UEFI Secure Boot

F40503-03

March 2022

[Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2021, Oracle and/or its affiliates.