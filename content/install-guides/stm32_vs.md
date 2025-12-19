---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: STM32 extensions for VS Code

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
- stm


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author: Ronan Synnott

### Link to official documentation
official_docs: 

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
STM provides a range of [software development tools](https://www.st.com/en/development-tools/stm32-software-development-tools.html) to simplify configuring and developing for [STM32](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html) devices.

The tools are available as a [VS Code](https://code.visualstudio.com/) extension.

See [STMicroelectronics provides full STM32 support for Microsoft Visual Studio Code](https://newsroom.st.com/media-center/press-item.html/t4536.html) for more information.


## Where can I download Visual Studio Code?

[Download](https://code.visualstudio.com/download), install, and start `Visual Studio Code` on your desktop.

Linux, macOS, and Windows are supported. 

## How do I install the STM32 VS Code Extension?

The `STM32 VS Code Extension` is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=stmicroelectronics.stm32-vscode-extension).

Install the `STM32` extension: 

1. Open the `Extensions` view in Visual Studio Code
2. Search for `STM32 VS Code Extension`
3. Click the `Install` button

Visual Studio Code will install the extension. `STM32 VS Code Extension` is now available in the `Activity Bar`.

### How do I install additional dependencies?

Additional software packages need to be downloaded from STM website. Click `Get Software` on each of the below, to download the appropriate installer for your host.

* [STM32CubeCLT](https://www.st.com/en/development-tools/stm32cubeclt.html)
* [STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html)
* [ST-MCU-FINDER-PC](https://www.st.com/en/development-tools/st-mcu-finder-pc.html)

Run the installer(s) and follow on-screen instructions.

### How do I install Git for version control functionality?

You can download the latest version from [git-scm.com](https://git-scm.com/).

### What about Keil Studio for VS Code?

[Keil Studio for VS Code](https://www.keil.arm.com/) is also available. Refer to the [Arm Keil Studio for VS Code install guide](/install-guides/keilstudio_vs/) for more information.
