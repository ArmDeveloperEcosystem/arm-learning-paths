---
title: Arm FlexNet Publisher Floating licenses
minutes_to_complete: 15
official_docs: https://developer.arm.com/documentation/dui0209
author_primary: Ronan Synnott
weight: 5                 

### FIXED, DO NOT MODIFY
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
Users who do not yet have access to UBL licenses will have FlexNet Publisher floating licenses. You will be supplied with license key(s) to generate your license(s).

## Download the latest FlexNet Publisher software

License Administrators should download and install the latest FlexNet Publisher software to your internal license server.
```url
https://developer.arm.com/downloads/-/download-flexnet-publisher
```
## Generate license file

Access the [Software Licensing Portal](https://developer.arm.com/support/licensing) to generate your license. You will need the `HOSTID` of the license server and your product license key from Arm.

## End-user set up
Users should set the environment variable `ARMLMD_LICENSE_FILE` to map to the location of your license server.

### Windows
```console
set ARMLMD_LICENSE_FILE=port@server
```
### Linux
```console
export ARMLMD_LICENSE_FILE=port@server
```
## Activate via tools IDE

The license can also be activated in the various Arm tool IDEs.

For example [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio)), via `Help` > `Arm License Manager`. You will also need to specify the Development Studio `Edition` that the license supports.
