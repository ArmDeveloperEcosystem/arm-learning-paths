---
title: Set up the Zephyr shell development environment
description: Prepare the host tools, hardware, UART terminal, and network requirements needed to build Zephyr shell examples on Arm Cortex-M.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

In this section, you'll prepare your host computer and identify the hardware needed for two Zephyr shell examples. You'll use the shell over two transports:

- MQTT over Ethernet
- UART over a USB serial connection

Make sure that you have a working Zephyr development environment set up in Visual Studio Code with:

- The Workbench for Zephyr extension installed 
- A Zephyr SDK toolchain imported in Workbench
- A West workspace initialized

Before working through this Learning Path, complete [Build Zephyr projects with Workbench for Zephyr in VS Code](/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/).

The two examples in this Learning Path have additional requirements:

- MQTT shell example: Docker Desktop, Docker Engine, or another Docker-compatible runtime on your host computer. The board communicates with a Mosquitto broker running in a container.
- UART shell example: A USB cable to connect the development board to your host computer. The board exposes a shell prompt over the USB serial interface.

## Hardware requirements

Both examples use the [FRDM-MCXN947](https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-MCXN947) as the development board (Zephyr identifier `frdm_mcxn947/mcxn947/cpu0`). The FRDM-MCXN947 includes an Ethernet port for the MQTT shell example and a USB UART interface for the UART shell example. This allows both examples to run on the same board.

To check whether another board is supported by Zephyr, see the [Zephyr supported boards list](https://docs.zephyrproject.org/latest/boards/index.html).

## Set up UART terminal tools

For the UART shell example, you'll need a serial terminal application on your host computer. You'll use the terminal application to connect to the Zephyr shell over the board's UART interface.

You can complete this Learning Path on Windows, macOS, and Linux host computers.

### Windows

Install [PuTTY](https://www.putty.org/index.html), which provides a lightweight serial terminal for UART communication on Windows.

### macOS

macOS includes a built-in UART terminal utility through the `screen` command, so you don't need additional software to connect to the shell.

### Linux

Linux includes `screen` in most distributions, so you don't need additional software to connect to the shell. If `screen` isn't installed, use your package manager to install it:

```bash
sudo apt install screen
```
{{% notice Note %}}
Workbench for Zephyr supports multiple debug runners depending on the connected board. The FRDM-MCXN947 board uses the onboard CMSIS-DAP/LinkServer interface for flashing and debugging, and UART over USB for shell access.
{{% /notice %}}

## Network requirements for the MQTT shell example

For the MQTT shell example, the board needs access to an MQTT broker over Ethernet. You'll run Mosquitto locally with Docker Compose and use the Mosquitto command-line tools to send and receive shell messages.

Make sure that:

- The board is connected to the same network as the host computer.
- The network provides DHCP, or you configure a static IPv4 address in `prj.conf`.
- The board can reach the MQTT broker on port `1883`.

{{% notice Note %}}
The example configuration uses IPv4. If your network doesn't provide DHCP, use the static IPv4 settings shown in the next section.
{{% /notice %}}

## What you've accomplished and what's next

You've now learned which boards to use, which host tools to install, and how the Zephyr shell fits into an embedded application.

In the next section, you'll learn about the Zephyr shell subsystem and the two transports used in this Learning Path. 
