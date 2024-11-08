---
title: UBL LLS End-user setup
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
## Local License Server

A [Local License Server (LLS)](/install-guides/license/ubl_license_admin/) must first be set up by your license administration team.

## Activate license on end user machine

The user-based license can be activated on the end user machine in different ways. Select the most appropriate for your needs.

* [Activate via environment variable](#envvar)
* [Activate within tools IDE](#ide)
* [Activate manually](#manual)

## Activate via environment variable {#envvar}

Create `ARMLM_ONDEMAND_ACTIVATION` environment variable referencing the product code and your internal license server. Contact your internal license administrators for information on your internal server.

### HSK
```console
export ARMLM_ONDEMAND_ACTIVATION=HWSKT-STD0@https://internal.ubl.server
```
### SSK
```console
export ARMLM_ONDEMAND_ACTIVATION=SWSKT-STD0@https://internal.ubl.server
```

A license will be automatically checked out whenever a user-based licensing enabled tool is run, for example:
```command
armclang --version
```
You can now [confirm your license has been checked out](#confirm).

## Activate within tools IDE {#ide}

The license can also be activated in the various Arm tool IDEs.

For example [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio), via `Help` > `Arm License Manager` > `Manage Arm User-Based Licenses`.

Select `Activate with` > `License Server`, and enter the appropriate license server address. Click `Query` to see what license types are available, and select the appropriate one from the pull down. Click `Activate`.

## Activate manually {#manual}

Open a command prompt, and navigate to the bin directory of any user-based licensing enabled product.

Activate your user-based license with `armlm`:
```console
armlm activate --server https://internal.ubl.server --product HWSKT-STD0
```

## Confirm license check-out {#confirm}

To confirm you have checked-out a license, enter the command:
```console
armlm inspect
```

You should see an output similar to:
```output
1 active product in your local cache:

Hardware Success Kit
    Product code: HWSKT-STD0
    Order Id: xxxxxxxx
    License valid until: 2025-12-31
    Local cache expires in: 6 days and 23 hours
    License server: https://internal.ubl.server
```

## License refresh {#refresh}

Your license is cached on your local machine, and is valid for 7 days.

There will be an automatic attempt to refresh this license once per day. If that fails (for example, if tools are run whilst not connected to your network) the tools can still be used provided there is still time on the locally cached license.

To manually refresh the license, you can deactivate and reactivate your license (when connected to your network). For example:
```command
armlm deactivate --server https://internal.ubl.server --product SWSKT-STD0
armlm reactivate --server https://internal.ubl.server --product SWSKT-STD0
```

Verify that you have refreshed successfully with:
```command
armlm inspect
```
