---
title: "Configuring DHCP Services"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol10"
  - "networking"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux 10

Configuring DHCP Services

G24142-01

June 2025

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 10 Configuring DHCP Services

G24142-01

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2025, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/dhcp-Preface.html -->

## Preface

[Oracle Linux 10: Configuring DHCP Services](https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/) provides information about configuring DHCP services for Oracle Linux
10 systems.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/ref-copyright-ccbysa4.html -->

## Documentation License

The content in this document is licensed under the [Creative Commons Attribution–Share Alike 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/ref-conventions.html -->

## Conventions

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| boldface | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| italic | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/ref-doc-accessibility.html -->

## Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility
Program website at <https://www.oracle.com/corporate/accessibility/>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/ref-accessibility.html -->

## Access to Oracle Support for Accessibility

Oracle customers that have purchased support have access to electronic support through My
Oracle Support. For information, visit <https://www.oracle.com/corporate/accessibility/learning-support.html#support-tab>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/ref-diversity.html -->

## Diversity and Inclusion

Oracle is fully committed to diversity and inclusion. Oracle respects and values having a
diverse workforce that increases thought leadership and innovation. As part of our
initiative to build a more inclusive culture that positively impacts our employees,
customers, and partners, we are working to remove insensitive terms from our products and
documentation. We are also mindful of the necessity to maintain compatibility with our
customers' existing technologies and the need to ensure continuity of service as Oracle's
offerings and industry standards evolve. Because of these technical constraints, our effort
to remove insensitive terms is ongoing and will take time and external cooperation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/dhcp-AboutDHCPServices.html -->

## 1 About DHCP Services

The Dynamic Host Configuration Protocol (DHCP) enables client systems to obtain network configuration information from a DHCP server each time they connect to the network. The DHCP server is configured with a range of IP addresses and other network configuration parameters that clients need.

When you configure an Oracle Linux system as a DHCP client, the client daemon contacts the DHCP server to obtain the networking parameters. As DHCP is broadcast-based, the client must be on the same subnet as either a server or a relay agent. If a client can't be on the same subnet as the server, a DHCP relay agent can be used to pass DHCP messages between subnets.

The server provides a lease for the IP address that it assigns to a client. The client can request specific terms for the lease, such as the duration. You can configure a DHCP server to limit the terms that it can grant for a lease. If a client remains connected to the network, the client daemon automatically renews the lease before it expires. You can configure the DHCP server to provide the same IP address to a client, based on the MAC address of its network interface.

The advantages of using DHCP include the following:

- Centralized management of IP addresses
- Ease of adding new clients to a network
- Reuse of IP addresses reducing the total number of IP addresses that are required
- Reconfiguration of the IP address space on the DHCP server without needing to reconfigure each client

For more information about DHCP, see [RFC 2131](https://datatracker.ietf.org/doc/html/rfc2131).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/dhcp-DHCPServerSoftware-Kea.html -->

## DHCP Server Software

Kea is the DHCP server software available in Oracle Linux
10. Kea replaces the ISC DHCP server available in previous versions of Oracle Linux. The Kea software is modular, and you can run either the `kea-dhcp4` or `kea-dhcp6` service to provide DHCP on the network.

For instructions on installing and configuring Kea on an Oracle Linux
10 system, see [Configuring a Kea DHCPv4 Service](dhcp-ConfiguringAKeaDHCPv4Service.html#dhcp_SettingUpaKeaDHCPServer).

For more information about Kea, see the [Kea Administrator Reference Manual](https://kea.readthedocs.io).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/dhcp-DHCPClientSoftware-dhcpcd.html -->

## DHCP Client Software

On an Oracle Linux
10 system operating as a DHCP client, NetworkManager handles DHCP requests. For information about DHCP configuration in NetworkManager, see the following manual pages:

- `NetworkManager(8)`
- `NetworkManager.conf(5)`
- `nm-settings-nmcli(5)`

If you need a DHCP client daemon besides NetworkManager, the `dhcpcd` software package is available in the standard repositories for Oracle Linux
10.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/dhcp-SettingUpAKeaDHCPService.html -->

## 2 Setting Up a Kea DHCP Service

Before you can install and configure a Kea DHCP service, verify that network interfaces that will listen for DHCP messages have static IP addresses.

You must also obtain information about the system that will run the DHCP service and the network it will serve. This could include any of the following information:

- Interface names on the system that will run the DHCP service
- Default gateway or router addresses
- Name server IP addresses
- Intended subnet IP addresses and ranges

Complete the following steps to set up a DHCP service.

1. Install the Kea package.

   ```
   sudo dnf install kea
   ```
2. Complete either of the following procedures to configure and start the DHCP service.

   Kea provides two separate components for IPv4 networks and IPv6 networks: `kea-dhcp4` and `kea-dhcp6`. Each component runs as an independent service, and has separate configuration files.

   - [Configuring a Kea DHCPv4 Service](dhcp-ConfiguringAKeaDHCPv4Service.html#dhcp_SettingUpaKeaDHCPServer)
   - [Configuring a Kea DHCPv6 Service](dhcp-ConfiguringAKeaDHCPv6Service.html#dhcp_SettingUpaKeaService_DHCP6)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/dhcp-ConfiguringAKeaDHCPv4Service.html -->

## Configuring a Kea DHCPv4 Service

Complete the following steps to configure the `kea-dhcp4` service.

1. Make a backup copy of the original configuration file.

   The installed configuration files include comments and example settings that could be helpful as you configure a network. With a backup, you can edit the original copy while preserving the original file contents.

   ```
   sudo cp /etc/kea/kea-dhcp4.conf /etc/kea/kea-dhcp4.conf.bak
   ```
2. Open `/etc/kea/kea-dhcp4.conf`, then replace the contents with the following example text:

   ```
   { "Dhcp4": {

       "interfaces-config": {
           "interfaces": [ "<interface name>" ]
       },

       "lease-database": {
           "type": "memfile",
           "persist": true,
           "name": "/var/lib/kea/kea-leases4.csv"
       },

       "valid-lifetime": 4000,

       "option-data": [
           {
               "name": "domain-name-servers",
               "data": "<DNS server IP addresses>"
           }
       ],

       "subnet4": [
           {
               "id": 1,
               "subnet": "<subnet IP address/netmask>",
               "option-data": [
                   {
                       "name": "routers",
                       "data": "<router IP address>"
                   }
               ],

               "pools": [{ "pool": "<IP address range>" }]
           } 
       ],

       "loggers": [
           {
               "name": "kea-dhcp4",
               "output-options": [
                   { "output": "stdout" }
               ],
               "severity": "INFO"
           }
       ]
   }
   }
   ```
3. Replace placeholder values with values that apply to your network.
   1. Replace the value of `interfaces` with names of interfaces on which you want the service to listen for DHCP messages.

      For example:

      ```
      "interfaces": [ "eno1" ]
      ```
   2. Review the parameters and values in `lease-database` and make any changes that suit the needs of your network.

      Consider changing any of the following parameters:
      - `type`âThe type of database `kea-dhcp4` uses. `memfile` is the default. In this case, the service keeps lease information in memory and saves the information to a CSV file on disk.

        If you have set up a MySQL or PostgreSQL database for lease database storage, you can change the value to `mysql` or `postgresql`. See the Kea Administrator's Reference Manual for more information.
      - `persist`âBoolean that indicates whether `kea-dhcp4` saves lease database information to disk. `true` is the default. If you set to `false`, a system restart would cause `kea-dhcp4` to lose a record of which IP addresses have been assigned.
      - `name`âThe absolute path to the database file. Kea provides a default CSV file for `kea-dhcp4` in `/var/lib/kea/kea-leases4.csv`, but you can enter a custom value here.
   3. Review the value of `valid-lifetime` and change the value to suit the needs of your network.

      Enter an integer representing the number of seconds the leases assigned by the server are valid.
   4. In `option-data`, under `domain-name-servers`, replace the `data` value with the IP addresses of name servers you want to use.

      For example:

      ```
      "name": "domain-name-servers",
                  "data": "10.0.2.10, 10.0.2.11"
      ```
   5. Replace the `subnet` value with the subnet IP address on your network. 

      For example:

      ```
      "subnet": "10.0.2.0/24",
      ```
   6. Replace the `pool` value with a range of IP addresses within the subnet you have defined.

      For example:

      ```
      "pool": "10.0.2.20 - 10.0.2.100",
      ```
   7. Review the values in `loggers` and change any values to suit the needs of your network.
4. Save the configuration file.
5. Check the configuration file for syntax errors.

   ```
   kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
   ```
6. Enable and start the DHCP service.

   ```
   sudo systemctl enable --now kea-dhcp4
   ```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/dhcp/dhcp-ConfiguringAKeaDHCPv6Service.html -->

## Configuring a Kea DHCPv6 Service

Complete the following steps to configure the `kea-dhcp6` service.

1. Make a backup copy of the original configuration file.

   The installed configuration files include comments and example settings that could be helpful as you configure a network. With a backup, you can edit the original copy while preserving the original file contents.

   ```
   sudo cp /etc/kea/kea-dhcp6.conf /etc/kea/kea-dhcp6.conf.bak
   ```
2. Open `/etc/kea/kea-dhcp6.conf`, then replace the contents with the following example text:

   ```
   { "Dhcp6": {

       "interfaces-config": {
           "interfaces": [ "<interface-name>" ]
       },

       "lease-database": {
           "type": "memfile",
           "persist": true,
           "name": "/var/lib/kea/kea-leases6.csv"
       },

       "preferred-lifetime": 3000,
       "valid-lifetime": 4000,
       "renew-timer": 1000,
       "rebind-timer": 2000,

       "option-data": [
           {
               "name": "dns-servers",
               "data": "<DNS server IP addresses>"
           }
       ],

       "subnet6": [
           {
               "id": 1,
               "subnet": "<subnet IP address/netmask>",
               "interface": "<interface-name>",
               "pools": [
               {
                   "pool": "<IP address range>",
                   "user-context": { "charging": true }
               } ]

           }
         ],

       "loggers": [
           {
               "name": "kea-dhcp6",
               "output-options": [
                   {
                       "output": "stdout"
                   }
               ],
               "debuglevel": 0,
               "severity": "INFO"
           }
       ]
   }
   }
   ```
3. Replace placeholder values with values that apply to your network.
   1. Replace the value of `interfaces` with names of interfaces on which you want the service to listen for DHCP messages.

      For example:

      ```
      "interfaces": [ "eno1" ]
      ```
   2. Review the parameters and values in `lease-database` and make any changes that suit the needs of your network.

      Consider changing any of the following parameters:
      - `type`âThe type of database `kea-dhcp4` uses. `memfile` is the default. In this case, the service keeps lease information in memory and saves the information to a CSV file on disk.

        If you have set up a MySQL or PostgreSQL database for lease database storage, you can change the value to `mysql` or `postgresql`. See the Kea Administrator's Reference Manual for more information.
      - `persist`âBoolean that indicates whether `kea-dhcp4` saves lease database information to disk. `true` is the default. If you set to `false`, a system restart would cause `kea-dhcp4` to lose a record of which IP addresses have been assigned.
      - `name`âThe absolute path to the database file. Kea provides a default CSV file for `kea-dhcp6` in `/var/lib/kea/kea-leases6.csv`, but you can enter a custom value here.
   3. Review the value of `valid-lifetime` and change the value to suit the needs of your network.

      Enter an integer representing the number of seconds the leases assigned by the server are valid.
   4. In `option-data`, under `dns-servers` replace the `data` value with the IP addresses of name servers you want to use.

      For example:

      ```
      "name": "dns-servers",
                  "data": "fc00:1:1::10, fc00:1:1::11"
      ```
   5. Replace the `subnet` value with the subnet IP address on your network. 

      For example:

      ```
      "subnet": "fc00:0001:0001::/48",
      ```
   6. Enter the value of network interfaces that connect to the subnet you defined.

      For example:

      ```
      "interfaces": [ "eno1" ]
      ```
   7. Replace the `pool` value with a range of IP addresses within the subnet you have defined.

      For example:

      ```
      "pool": "fc00:1:1::20 - fc00:1:1::1000",
      ```
   8. Review the values in `loggers` and change any values to suit the needs of your network.
4. Save the configuration file.
5. Check the configuration file for syntax errors.

   ```
   kea-dhcp6 -t /etc/kea/kea-dhcp6.conf
   ```
6. Enable and start the DHCP service.

   ```
   sudo systemctl enable --now kea-dhcp6
   ```