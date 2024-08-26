---
title: FlexNet Publisher Floating license setup
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
Older Arm products do not support user-based licenses. These will be enabled with FlexNet Publisher floating licenses.

You will be supplied with license key(s) to generate such license(s).

## License server set up

### Download the latest FlexNet Publisher software

License Administrators should download and install the latest FlexNet Publisher software to your internal license server.
```url
https://developer.arm.com/downloads/-/download-flexnet-publisher
```
### Generate license file

Access the [Software Licensing Portal](https://developer.arm.com/support/licensing) to generate your license. You will need the `HOSTID` of the license server and your product license key from Arm.

Optionally add license server names and network port to the `SERVER` line of the license file:
```output
SERVER HOSTNAME HOSTID PORT
```
### Launch the license server

Start the license server with:
```command
lmgrd -c license_file
```
See the [FlexNet for Arm Tools License Management Guide](https://developer.arm.com/documentation/dui0209) for full options.


## End-user set up

End-users should set the environment variable `ARMLMD_LICENSE_FILE` to map to the location of your license server.

#### Windows
```console
set ARMLMD_LICENSE_FILE=port@server
```
#### Linux
```console
export ARMLMD_LICENSE_FILE=port@server
```

### Activate via tools IDE

The license can also be activated in the various Arm tool IDEs.

For example [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio), via `Help` > `Arm License Manager`.

If `ARMLMD_LICENSE_FILE` is not set, use `Add` > `Add product license`, and specify `port` and `server` information for your license server.

Arm Development Studio will also ask to specify the appropriate [Edition](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio#Editions) as the `Active Product`.

### Verify setup

To verify that the license is set up correctly, set the following environment variable:

#### Windows
```console
set FLEXLM_DIAGNOSTICS=3
```
#### Linux
```console
export FLEXLM_DIAGNOSTICS=3
```

and execute an appropriate Arm tool, for example `Arm Compiler for Embedded`:
```command
armclang --version
```

Observe the output, which will be similar to:
```output
Checkout succeeded: ds_suite_rowan/04C6 0E2A CDA4 6344
        License file: port@server
        License Server: port@server
Checkout succeeded: ds_compiler_rowan/141D C968 2E7F 4187
        License file: port@server
        License Server: port@server
Product: Arm Development Studio Gold Edition 2023.1
Component: Arm Compiler for Embedded 6.21
```

{{% notice Note %}}
Unset the `FLEXLM_DIAGNOSTICS` environment variable afterwards, as this will impact the tools performance.
{{% /notice %}}
