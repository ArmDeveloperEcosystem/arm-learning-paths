---
title: Set up your environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your environment

In this section, you will prepare your host computer and identify the hardware needed for two Zephyr shell examples. You will use the shell over two transports:

- MQTT over Ethernet
- SEGGER RTT over a J-Link debug connection

By the end of this section, you will know which boards to use, which host tools to install, and how the Zephyr shell fits into an embedded application.

## Before you begin

Make sure you have a working Zephyr development environment set up in Visual Studio Code using the Workbench for Zephyr extension, including:

- The Workbench for Zephyr extension installed
- A Zephyr SDK toolchain imported in Workbench
- A West workspace initialized

If you have not done this yet, complete [Build Zephyr projects with Workbench for Zephyr in VS Code learnin path](/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/) first.

You also need:

- Docker Desktop, Docker Engine, or another Docker-compatible runtime
- A USB cable for each development board

## Hardware requirements

For the MQTT shell example, use a Zephyr-supported development board with Ethernet. The instructions use the [FRDM-MCXN947](https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-MCXN947), with the Zephyr board identifier `frdm_mcxn947/mcxn947/cpu0`.

For the RTT shell example, use a Zephyr-supported development board with an onboard or external SEGGER J-Link debug interface. The instructions use the [xG27 Dev Kit (BRD2602A)](https://www.silabs.com/development-tools/wireless/efr32xg27-development-kit?tab=overview), with the Zephyr board identifier `xg27_dk2602a` and the J-Link device name `EFR32BG27CxxxF768`.

To check whether another board is supported by Zephyr, refer to the [Zephyr Supported Boards list](https://docs.zephyrproject.org/latest/boards/index.html).

## Install SEGGER J-Link tools

For the RTT shell example, install the [**SEGGER J-Link Software and Documentation Pack**](https://www.segger.com/products/debug-probes/j-link/) on your host computer. The package includes **J-Link RTT Viewer**, which you will use to open an interactive shell over the debug connection.

Download the installer from [www.segger.com/downloads/jlink](https://www.segger.com/downloads/jlink/) and install the package for your operating system.

{{% notice Note %}}
Workbench for Zephyr can install and configure some debug runners from the extension panel. Install the SEGGER J-Link package separately so that J-Link RTT Viewer is available on your host computer.
{{% /notice %}}

## Network requirements

For the MQTT shell example, the board needs access to an MQTT broker over Ethernet. You will run Mosquitto locally with Docker Compose and use the Mosquitto command-line tools to send and receive shell messages.

Make sure that:

- The board is connected to the same network as the host computer.
- The network provides DHCP, or you configure a static IPv4 address in `prj.conf`.
- The board can reach the MQTT broker on port `1883`.

{{% notice Note %}}
The example configuration uses IPv4. If your network does not provide DHCP, use the static IPv4 settings shown in the next section.
{{% /notice %}}

## What's next?

In the next section, you will read a short overview of the Zephyr shell subsystem and the two transports used in this Learning Path. After that, you will build the MQTT shell on the FRDM-MCXN947 and the RTT shell on the xG27 Dev Kit.
