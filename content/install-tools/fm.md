---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Fast Models

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
  - virtual platform

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://developer.arm.com/documentation/102441

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Arm Fast Models](https://developer.arm.com/Tools%20and%20Software/Fast%20Models) are accurate, flexible programmer's view models of Arm IP. They are used to build a virtual platform, either standalone, or as part of Hybrid Simulation environment within EDA partner environments. Use the virtual platform for software development and verification throughout the development process, even long before any real hardware is available.

This article discusses the stand alone use case. If using as part of an EDA partner's environment, please contact the relevant vendor for guidance.

## Prerequisites

A Fast Model based virtual platform is an executable that runs on your Linux or Windows host. To **build** such an executable, you must ensure that the appropriate host toolchain is installed.

For Linux hosts, use `gcc 9.3.0`.

For Windows hosts use [Visual Studio 2019](https://visualstudio.microsoft.com/vs/older-downloads/) 16.7.3 (or later). Express or Community editions can NOT be used.

More information is given in [the documentation](https://developer.arm.com/documentation/100965/latest/Installing-Fast-Models/Requirements-for-Fast-Models).

## Download installer packages

You can download the Fast Models installer from the [Product Download Hub](https://developer.arm.com/downloads/view/FM000A). Linux and Windows hosts are supported.

Full installation instructions are provided [here](https://developer.arm.com/documentation/100965/latest/Installing-Fast-Models/Installation).

Windows users, once installed, open the System Canvas IDE, and select File > Preferences > Applications, and locate the folder containing `devenv.com` in your Visual Studio installation (`\\Common7\IDE`).

## Setting up product license

Arm Fast Models are license managed. License setup instructions are available [here](../license/).

## Verify installation

To verify everything is working OK, you can build one of the many example projects provided.

 - Launch the System Canvas IDE, and select `File` > `Load Project`, and browse to the `FastModelsPortfolio_<version>\examples' folder.
 - Select any example (such as `\LISA\FVP_MPS2\Build_Cortex-M3\FVP_MPS2_Cortex-M3.sgproj`).
 - Ensure an appropriate Project Configuration is selected from the pulldown in the upper toolbar (such as `Win64_Release-VC19`).
 - Click `Build` in the upper toolbar to build the virtual platform.
 - Once built, click `Run` and select `ISIM system` before launching the virtual platform.
   - If a suitable program image is available (such as the `startup_Cortex-M3_AC6.axf` example from [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio)), you can load this with the `-a` option.

## Fixed Virtual Platforms {#fvp}

Arm supplies a selection of ready made [Fixed Virtual Platforms (FVPs)](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms) that can be used without Arm Fast Models installed. See [this article](../fvp) for more information.
