---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: NXP MCUXpresso for VS Code

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- cortex-m
- microcontroller
- mcu
- iot
- ide
- vs code
- vscode
- visual studio
- cmsis
- nxp


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author: Ronan Synnott

### Link to official documentation
official_docs: https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
[MCUXpresso for Visual Studio Code](https://www.nxp.com/design/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC) provides an optimized embedded developer experience for code editing and development.

`MCUXpresso` is available as a [VS Code](https://code.visualstudio.com/) extension.

See [The New Era of MCUXpresso Starts Today with VS Code and Open-CMSIS-Packs](https://www.nxp.com/company/blog/the-new-era-of-mcuxpresso-starts-today-with-vs-code-and-open-cmsis-packs:BL-THE-NEW-ERA-OF-MCUXPRESSO) for more information.


## What do I need before installing MCUXpresso for VS Code?

[Download](https://code.visualstudio.com/download), install, and start `Visual Studio Code` on your desktop.

Linux, macOS, and Windows are supported. 

## How do I install MCUXpresso for VS Code?

`MCUXpresso for VS Code` is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=NXPSemiconductors.mcuxpresso).

Install the `MCUXpresso` extension: 

1. Open the `Extensions` view in Visual Studio Code
2. Search for `MCUXpresso`
3. Click the `Install` button

Visual Studio Code will install the extension. `MCUXpresso` is now available in the `Activity Bar`.

### How do I install additional dependencies?

Additional software packages can be installed with the [MCUXpresso Installer](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Dependency-Installation) for your host operating system.

Download and run the installer. 

Select one or more packages and click `Install`. 

![MCUXpresso Installer #center](/install-guides/_images/mcuxpresso_installer.png)

### Are there other embedded development extensions for VS Code?

[Keil Studio for VS Code](https://www.keil.arm.com/) is also available. Refer to the [Arm Keil Studio for VS Code install guide](/install-guides/keilstudio_vs/) for more information.



