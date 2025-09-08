---
title: UBL Local License Server (LLS) setup
minutes_to_complete: 15
official_docs: https://developer.arm.com/documentation/107573
author: Ronan Synnott
weight: 2                      

### FIXED, DO NOT MODIFY
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

<<<<<<< HEAD
## How do I access the Arm license portal?
=======
## Arm license portal
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

To generate your licenses you need access to the Arm user-based licensing portal, with the account that the licenses were assigned to.

Verify you can access the following and see your assigned licenses before you begin.
```url
https://developer.arm.com/support/licensing/user-based
```

<<<<<<< HEAD
## How do I set up the license server?
=======
## License server set up
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

UBL license server software is supported on a variety of operating systems or virtual machines. 

The license server uses a number of standard Linux utilities, including Python and Java.

```console
sudo apt update
sudo apt install -y openjdk-11-jre-headless python-is-python3
```
See [Hardware and software requirements](https://developer.arm.com/documentation/107573/latest/Installing-and-populating-the-license-server/Hardware-and-software-requirements) in the [User-based Licensing Administration Guide](https://developer.arm.com/documentation/107573).

<<<<<<< HEAD
### How do I download and install the server software?
=======
### Download and install server software
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

The local license server (LLS) software can be downloaded from:
```url
https://lm.arm.com/downloads
```
Expand the tarball (named `flexnetls-armlmd-<version>.tar.gz`), and install the license server software.
```console
tar -xf flexnetls-armlmd-1.2024050.0.tar.gz
sudo ./flexnetls-armlmd-1.2024050.0/install_license_server
```
Additional options are described in the [License Server Administration Guide](https://developer.arm.com/documentation/107573/latest/Installing-and-populating-the-license-server/Install-your-license-server).

The installer will automatically start the license server software. When complete, you will see output similar to:
```output
License server service flexnetls-armlmd is starting, and will start automatically on system start-up.
Waiting for license server... (up to 120 seconds, or press CTRL-C to stop waiting)

License server running and ready to accept requests at http://<external server name or IP address>:7070
```

<<<<<<< HEAD
### How do I add the install directory to the search path?
=======
### Add install directory to PATH
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

It is recommended to add the server install directory to the `PATH` so that license server commands can be easily called. For example the default location:
```console
export PATH=/opt/flexnetls-armlmd/bin:$PATH
```

<<<<<<< HEAD
### How do I set the administrator password?
=======
### Set administrator password
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

You must set an appropriate administrator password to be able to execute subsequent commands. Use the following:
```console
armlm_change_admin_password
```
{{% notice Note %}}
The administrator password is only stored locally. If you forget the password, you must uninstall and reinstall the license server.

See the [License Server Administrator Guide](https://developer.arm.com/documentation/107573/latest/License-server-administration/Reset-the-administrator-password).
{{% /notice %}}


<<<<<<< HEAD
### How do I verify the server hostid?
=======
### Verify server hostid
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

The default `hostid` was selected by the license server installer. To view the selected hostid use:
```console
armlm_show_hostid
```
which will output all available hostids, and highlight as `selected` the one that will be used. For example:
```output
{
  "selected" : {
    "hostidType" : "ETHERNET",
    "hostidValue" : "001122334455"
  },
  "hostids" : [ {
    "hostidType" : "ETHERNET",
    "hostidValue" : "001122334455"
  }, {
    "hostidType" : "ETHERNET",
    "hostidValue" : "445566778899"
  } ]
}
```
If you wish to change the `selected` hostid, edit the `/server/local-configuration.yaml` file. See the [documentation](https://developer.arm.com/documentation/107573/1-2024500/Installing-and-populating-the-license-server/Configure-your-license-server) for full details.
```yml
# Specify the hostid to be used. Syntax: 001122334455/ETHERNET. Has to be one
# of the hostids reported by armlm_show_hostid.
active-hostid: 445566778899/ETHERNET
```

<<<<<<< HEAD
### How do I register the license server with Arm?
=======
### Register license server with Arm
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

Create a license server identity file (`identity.bin`) using:
```console
armlm_generate_server_identity
```
Access the Arm user-based licensing portal.
```url
https://developer.arm.com/support/licensing/user-based
```
Navigate to `Manage License Servers`, and click on `Register Local License Server`. Upload the identity file.


<<<<<<< HEAD
### How do I add licenses to the server? {#addlicenses}
=======
### Add licenses to server {#addlicenses}
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

Click on `Add Products` and select the quantity of the available licenses to assign to that server. When satisfied, click on `Add Products` and a license file will be generated.

If not automatically downloaded or if to consolidate with existing licenses, click on `Download all licenses allocated to this server`.

Install the license file on the license server with:
```console
armlm_update_licenses --data-file <license_file>
```
You will see the following output when successful.
```output
Licenses have been successfully updated. No confirmation is required.
```
The licenses are now ready to use by the [end-users](/install-guides/license/ubl_license_enduser/).


<<<<<<< HEAD
## How do I change installed licenses per server?

### How do I add more licenses to the server?
=======
## Changing installed licenses per server

### Adding licenses to server
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

To **add** licenses to the server, update the licenses assigned to the server appropriately in the portal.

Download and install the new license file on the server, as described [above](#addlicenses).

<<<<<<< HEAD
### How do I delete licenses from the server?
=======
### Deleting licenses from server
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

To **remove** licenses, first update the licenses assigned to the server appropriately in the portal.

Download and install the new license file on the server, as described [above](#addlicenses).

You must then generate a `confirmation` that the licenses have been removed from that server:
```command
armlm_generate_server_confirmation
```
Upload the generated `confirmation.bin` file to the portal. The licenses will be returned to your pool for reassignment to another server.

{{% notice Note%}}
You must delete all licenses from a server before decommissioning.
{{% /notice %}}

If the license server is no longer in use, you can delete it from the portal by clicking `Obsolete server`.


<<<<<<< HEAD
## How do I monitor license server status and usage?

### How do I check server status?
=======
## Monitoring license server status and usage

### Status
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

To check the status of the server application, use:
```console
armlm_check_server_status
```
A working server will output:
```output
License server running and ready to accept requests at http://<external server name or IP address>:7070
```

<<<<<<< HEAD
### How do I check license usage?
=======
### License usage
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

To list the number of licenses (total and used) use:
```console
armlm_list_products
```
Example output:
```output
1 product found on license server:

Hardware Success Kit (Early Access), HWSKT-EAC0, 2 seats, 1 seat used
    Order Id: 0000000000, valid until: 2023-Dec-31 23:59:59 UTC, 2 seats, 1 seat used
```
<<<<<<< HEAD
### How do I check which users are active?
=======
### Active users
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

To list the current active users of the licenses use:
```console
armlm_list_users
```
Example output:
```output
User   Product Code   Product Name                          Last Access                Held Until
----   ------------   ------------                          -----------                ----------
usr1   HWSKT-EAC0     Hardware Success Kit (Early Access)   2023-Jun-13 12:40:30 UTC   2023-Jun-20 12:40:30 UTC
```
