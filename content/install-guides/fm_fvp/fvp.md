---
title: Fixed Virtual Platforms (FVP)
minutes_to_complete: 15
official_docs: https://developer.arm.com/documentation/100966/
author: Ronan Synnott
<<<<<<< HEAD
weight: 3
=======
weight: 3    
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

### FIXED, DO NOT MODIFY
tool_install: false              # Set to true to be listed in main selection page, else false
multi_install: false             # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
<<<<<<< HEAD

{{% notice Note %}}
Arm Fixed Virtual Platforms (FVPs) were available as a library of ready to use platforms (and as a component of Arm Development Studio) up until version 11.28.

From 11.29 onwards the FVPs are provided solely as part of Arm Development Studio.

This install guide is only applicable to the legacy FVP library.

See the [Arm Development Studio Install Guide](/install-guides/armds) and the [Introduction to FVPs](https://developer.arm.com/documentation/110379/1129/Introduction-to-FVPs) documentation.
=======
Arm Fixed Virtual Platforms (FVPs) are provided as a library of ready to use platforms.

{{% notice  Arm Development Tools%}}
An appropriate subset of the FVP library is installed with [Arm Development Studio](/install-guides/armds) and [Keil MDK](/install-guides/mdk) Professional Edition.
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
{{% /notice %}}

## Download installer packages

<<<<<<< HEAD
You can download the FVP library installer from the [Product Download Hub](https://developer.arm.com/downloads/view/FMFVP).
=======
You can download the FVP library installer from the [Product Download Hub](https://developer.arm.com/downloads/view/FM000A).
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

Linux (AArch64 and x86) and Windows (x86 only) hosts are supported.

For more information about the Product Download Hub, refer to the [Product Download Hub installation guide](/install-guides/pdh).

## Install FVP library

### Windows

Unzip the downloaded installation archive.

It is easiest to run the installation wizard (`setup.exe`), and follow on-screen instructions.

### Linux
Unpack the downloaded package, and install the FVP library with the supplied script.
```command
./FVP_ARM_Std_Library.sh --i-agree-to-the-contained-eula --no-interactive
```
For full list of available options, use:
```command
./FVP_ARM_Std_Library.sh --help
```

## Set up the product license

FVPs are license managed. License setup instructions are available in the [Arm Licensing install guide](/install-guides/license).

<<<<<<< HEAD
=======
{{% notice  Arm Development Tools%}}
The FVPs provided with Arm Development Studio and/or Keil MDK Professional Edition use the license of that product, not that of the FVP library.
{{% /notice %}}


>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
## Verify installation

To verify everything is working OK, navigate to the install directory, and launch any of the supplied FVP executables. No additional command options are needed.

For example:
```command
./FVP_MPS2/FVP_MPS2_Cortex-M3
```
The FVP will launch, and output text in a terminal similar to:
```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
```
A visualization of the FVP will also be displayed.

Terminate the FVP with `Ctrl+C`.
<<<<<<< HEAD

{{% notice %}}
You might run into an enablement issue related to the stack:
```
cannot enable executable stack as shared object requires: Invalid argument
```
This stems from the status of the the exec flag, a security feature which helps prevent certain types of buffer overflow attacks. FVPs use just-in-time compilation and require an executable stack to function properly. 

You can a workaround this error using `execstack` on each of the runtime binaries in the error trace.
```
execstack -c <binary>
```
{{% /notice %}}

=======
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
