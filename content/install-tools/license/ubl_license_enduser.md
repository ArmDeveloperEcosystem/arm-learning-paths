---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm User-Based License (UBL) End-user setup

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- licensing
- success-kits

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://developer.arm.com/documentation/102516

weight: 3                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
## Set up by environment variable

Create `ARMLM_ONDEMAND_ACTIVATION` environment variable referencing the success kit product code and your internal server.

{{< tabpane code=true >}}
  {{< tab header="HSK" >}}
export ARMLM_ONDEMAND_ACTIVATION=HWSKT-STD0@https://internal.ubl.server
{{< /tab >}}
  {{< tab header="SSK" >}}
export ARMLM_ONDEMAND_ACTIVATION=SWSKT-STD0@https://internal.ubl.server
{{< /tab >}}
{{< /tabpane >}}

A license will be checked out whenever a UBL enabled tool is used.

## Activate via tools IDE

The license can also be activated in the various Arm tool IDEs.

For example [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio)), via `Help` > `Arm License Manager` > `Manage Arm User-Based Licenses`.

## Manually set up

Open a command prompt, and navigate to the bin directory of any UBL enabled product. Activate an appropriate success kit license:

{{< tabpane code=true >}}
  {{< tab header="HSK" >}}
armlm activate --server https://internal.ubl.server --product HWSKT-STD0
{{< /tab >}}
  {{< tab header="SSK" >}}
armlm activate --server https://internal.ubl.server --product SWSKT-STD0
{{< /tab >}}
{{< /tabpane >}}

## Confirm license check-out

To confirm you have checked-out a license, enter the command:
```console
armlm inspect
```
