---
title: UBL Cloud server setup
minutes_to_complete: 15
official_docs: https://developer.arm.com/documentation/107573
author_primary: Ronan Synnott
weight: 4

### FIXED, DO NOT MODIFY
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
## Generate activation code

Access to the Arm user-based licensing portal with the account that the licenses were assigned to. This is likely to be an assigned license administrator rather than the end-user.

```url
https://developer.arm.com/support/licensing/user-based
```
Click on `View Details` of the product of interest, and then navigate to `Cloud Server` > `Generate Activation Code`.

This code can be shared with the end-user to [activate](#activate).

Once activated, the user information will be visible on the licensing portal dashboard along side the activation code.


### Activate license {#activate}

On the end-user machine, open a command prompt, and navigate to the `bin` directory of any UBL enabled product.

Use the following command with your assigned activation code.
```console
armlm activate --code xxxxxxxx-xxxx-xxxx-xxxxxxxx
```

### Activate via tools IDE

The license can also be activated in the various Arm tool IDEs.

For example [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio), via `Help` > `Arm License Manager` > `Manage Arm User-Based Licenses`.

Select `Activate with` > `Activation Code`, and enter your product activation code. Click `Activate`.

## Confirm license check-out

To confirm you have checked-out a license, enter the command:
```console
armlm inspect
```

## License refresh

Your license is cached on your local machine, and is valid for 7 days.

There will be an automatic attempt to refresh this timer on the first usage of a UBL enabled tool in a day. If it fails to communicate to the server (see [Network requirements for user-based licensing](https://developer.arm.com/documentation/102516/latest/User-based-licensing-overview/Network-requirements-for-user-based-licensing) for the most common reasons) the tools can still be used provided there is still time on the locally cached license.

To manually refresh the cached license, you can deactivate and reactivate your license (assuming above network requirements are fulfilled):
```command
armlm deactivate --code xxxxxxxx-xxxx-xxxx-xxxxxxxx
armlm reactivate --code xxxxxxxx-xxxx-xxxx-xxxxxxxx
```
Verify that you have refreshed successfully with:
```command
armlm inspect
```
