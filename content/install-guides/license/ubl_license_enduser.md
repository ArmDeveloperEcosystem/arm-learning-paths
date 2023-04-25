---
title: Arm User-Based License (UBL) End-user setup
minutes_to_complete: 15
official_docs: https://developer.arm.com/documentation/102516
author_primary: Ronan Synnott
weight: 3                       

### FIXED, DO NOT MODIFY
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
{{% notice License end-users%}}
The below is for those who are using Arm tools managed by Arm UBL licenses.
{{% /notice %}}

## Set up by environment variable

Create `ARMLM_ONDEMAND_ACTIVATION` environment variable referencing the Success Kit product code and your internal UBL license server. Contact your internal license administrators for information on your internal server.

### HSK
```console
export ARMLM_ONDEMAND_ACTIVATION=HWSKT-STD0@https://internal.ubl.server
```
### SSK
```console
export ARMLM_ONDEMAND_ACTIVATION=SWSKT-STD0@https://internal.ubl.server
```
A license will be checked out whenever a UBL enabled tool is used.

## Activate via tools IDE

The license can also be activated in the various Arm tool IDEs.

For example [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio)), via `Help` > `Arm License Manager` > `Manage Arm User-Based Licenses`.

## Manually set up

Open a command prompt, and navigate to the bin directory of any UBL enabled product. Activate an appropriate success kit license:
### HSK
```console
armlm activate --server https://internal.ubl.server --product HWSKT-STD0
```
### SSK
```
armlm activate --server https://internal.ubl.server --product SWSKT-STD0
```
## Confirm license check-out
To confirm you have checked-out a license, enter the command:
```console
armlm inspect
```
