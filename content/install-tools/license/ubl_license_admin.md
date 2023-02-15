---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm User-Based License (UBL) Server setup

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- licensing
- success-kits

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://developer.arm.com/documentation/107573

weight: 2                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
## License portal

To generate your licenses you need access to the Arm user-based licensing portal, with the account that the licenses were assigned to. Verify you can access before you begin.
```url
https://developer.arm.com/support/licensing/user-based
```

### License server set up

UBL license server software is supported on the following host operating systems:
* Red Hat Enterprise Linux / CentOS 7 and 8
* Ubuntu 20.04 LTS

The license server uses a number of standard Linux [utilities](https://developer.arm.com/documentation/107573/latest/Getting-started-with-user-based-licensing/Hardware-and-software-requirements), including Python and Java.
```console
sudo apt update
sudo apt install -y openjdk-11-jre-headless python
```

### Download and install server software

The local license server (LLS) software can be downloaded from:
```url
https://lm.arm.com/downloads
```
Expand the tarball, and install the license server software.
```console
tar -xf flexnetls-armlmd-<version>.tar.gz
sudo flexnetls-armlmd-<version>/install_license_server
```
The installer will automatically start the license server software. You will see the following output:
```
Waiting for license server... (up to 120 seconds)
License server ready.
```
To check the status of the server application, use:
```console
sudo systemctl status flexnetls-armlmd
```
### Set environment variables

It is recommended to add the install directory to the `PATH`, and to set the `FLEXNETLS_BASEURL` environment variable. For example:
```console
export PATH=/opt/flexnetls-armlmd/bin:$PATH
export FLEXNETLS_BASEURL=http://localhost:7070/api/1.0/instances/~
```
### Set administrator password

The first time you install the LLS server, you must set an appropriate password so as to be able to configure it. Use the following command:
```console
armlm_change_admin_password
```
### Verify server hostid

The default `hostid` was selected by the license server installer. To view the selected hostid use:
```console
armlm_show_hostid
```
which will output (in JSON format) a list of the selected and all available hostids.

If you wish to change the selected hostid, edit the `/server/local-configuration.yaml` file. See the [documentation](https://developer.arm.com/documentation/107573/latest/Getting-started-with-user-based-licensing/Register-your-license-server) for full details.

### Register license server with Arm

Create a license server identity file (`identity.bin`) using:
```console
armlm_generate_server_identity --identity-file identity.bin
```
Access the Arm user-based licensing portal.
```url
https://developer.arm.com/support/licensing/user-based
```
Navigate to `Manage License Servers`, and click on `Register Local License Server`. Upload the identity file.

### Add licenses to server

Click on `Add Products` and select the quantity of the available licenses to assign to that server. When satisfied, click on `Add Products` and a license file will be generated.

If not automatically downloaded or if to consolidate with existing licenses, click on `Download all licenses allocated to this server`.

Install the license file on the license server with:
```console
armlm_update_licenses --data-file <license_file>
```
You will see the following output when successful.
```
Licenses have been successfully updated. No confirmation is required.
```
The licenses are now ready to use by the end-users.

## Monitor license server usage

To list the number of licenses (total and used) use:
```console
armlm_list_products
```
To list the current active users of the licenses use:
```console
armlm_list_users
```
