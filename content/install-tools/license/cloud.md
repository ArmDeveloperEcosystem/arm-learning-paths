---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm User-Based License (UBL) Cloud server

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- licensing
- success-kits

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://developer.arm.com/documentation/107573

weight: 4                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
## Generate activation code

To generate an activation code you need access to the Arm user-based licensing portal with the account that the licenses were assigned to. This is likely to be an assigned license administrator rather than the end-user.
```url
https://developer.arm.com/support/licensing/user-based
```
Click on `View Details` of the product of interest, and then navigate to `Cloud Server` > `Generate Activation Code`. This code can be shared with the end-user to [activate](#activate).

Once activated, the user information will be shown along side the activation code.

### Activate license {#activate}

Open a command prompt, and navigate to the bin directory of any UBL enabled product.

Use the following command with your assigned activation code.
```console
armlm activate --code xxxxxxxx-xxxx-xxxx-xxxxxxxx
```
## Activate via tools IDE

The license can also be activated in the various Arm tool IDEs.

For example [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio)), via `Help` > `Arm License Manager` > `Manage Arm User-Based Licenses`.

## Confirm license check-out

To confirm you have checked-out a license, enter the command:
```console
armlm inspect
```