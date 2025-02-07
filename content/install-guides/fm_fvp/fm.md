---
title: Arm Fast Models
minutes_to_complete: 15
official_docs: https://developer.arm.com/documentation/107572
author: Ronan Synnott
weight: 2

### FIXED, DO NOT MODIFY
tool_install: false              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
{{% notice  EDA integration%}}
This article discusses the Arm Fast Model stand alone use case.

If using as part of an EDA partner's environment, please contact the relevant vendor for guidance.
{{% /notice %}}

## Before you begin

Arm Fast Models are a library of components that are used to build a virtual platform. This virtual platform is an executable that runs on your Linux or Windows host.

Therefore to build such an executable, you must ensure that the appropriate host toolchain is installed.

For Windows hosts, [Visual Studio 2019](https://visualstudio.microsoft.com/vs/older-downloads/) 16.11 (or later). Express or Community editions can NOT be used.

For Linux hosts, the supported `gcc` version depends on the Host OS.

The [Fast Models User Guide](https://developer.arm.com/documentation/100965/latest/Installing-Fast-Models/Requirements-for-Fast-Models) provides full details.

## Download installer packages

You can download the Fast Models installation package from the [Product Download Hub](https://developer.arm.com/downloads/view/FM000A).

Linux (AArch64 and x86) and Windows (x86 only) hosts are supported.

For more information about the Product Download Hub, refer to the [Product Download Hub installation guide](/install-guides/pdh).

## Install Arm Fast Models

### Windows

Unzip the downloaded installation archive.

It is easiest to run the installation wizard (`setup.exe`), and follow on-screen instructions.

Once installed, open the `System Canvas` IDE, and select `File` > `Preferences` > `Applications` from the menu.

Set the `Path to Microsoft Viaual C++ application devenv.com` to your Visual Studio installation (`<install_dir>\Common7\IDE`). Click `OK` to save.

### Linux

Use the `setup.sh` script to install:
```command
./setup.sh --i-accept-the-end-user-license-agreement --no-interactive
```
You may be prompted to install additional libraries before proceeding.
```command
sudo apt-get install -y libsm6 libxcursor1 libxft2 libxrandr2 libxt6 libxinerama1
```
Once installed, set up environment with script of the form:
```command
. <install_directory>/FastModelTools_<version>/etc/source_all.sh
```
The installer will output the exact script for your setup.

Full instructions are provided in the [Fast Models User Guide](https://developer.arm.com/documentation/100965/latest/Installing-Fast-Models/Installation).

## Set up the product license

Arm Fast Models are license managed. License setup instructions are available in the [Arm Licensing install guide](/install-guides/license).


## Verify installation

To verify everything is working OK, you can build one of the many example projects provided.
 - Launch the `System Canvas` IDE from your desktop, or from a terminal:
 ```command
 sgcanvas &
 ```
 - From the menu, select `File` > `Load Project`, and browse to the `FastModelsPortfolio_<version>\examples` folder.
 - Select any example (such as `\LISA\FVP_MPS2\Build_Cortex-M3\FVP_MPS2_Cortex-M3.sgproj`).
 - Ensure an appropriate Project Configuration is selected from the pulldown in the upper toolbar (such as `Win64_Release-VC19`).
 - Click `Build` in the upper toolbar to build the virtual platform.
 - Once built, click `Run` and select `ISIM system`.
 - Click `OK` to launch the virtual platform.

The FVP will launch, and output text in the terminal similar to:
```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
```
A visualization of the FVP will also be displayed.

Terminate the FVP with `Ctrl+C`.
