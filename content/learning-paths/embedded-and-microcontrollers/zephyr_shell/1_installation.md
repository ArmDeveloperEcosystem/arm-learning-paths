---
title: Set up your environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your environment

In this section, you will prepare your host computer and identify the hardware needed for two Zephyr shell examples. You will use the shell over two transports:

- MQTT over Ethernet
- UART over a USB serial connection

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

For the UART shell example, use a Zephyr-supported development board with a USB UART interface. The instructions use the [FRDM-MCXN947](https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-MCXN947), with the Zephyr board identifier `frdm_mcxn947/mcxn947/cpu0`.

To check whether another board is supported by Zephyr, refer to the [Zephyr Supported Boards list](https://docs.zephyrproject.org/latest/boards/index.html).

## Install UART terminal tools

For the UART shell example, install a serial terminal application on your host computer. You will use the terminal application to connect to the Zephyr shell over the board's UART interface.

### Windows

Install [PuTTY](https://www.putty.org/index.html), which provides a lightweight serial terminal for UART communication.

After installation:

1. Connect the development board over USB.

2. Open **Device Manager** and locate the board's COM port under **Ports (COM & LPT)**.

3. Open PuTTY and configure:

   - **Connection type**: `Serial`

   - **Serial line**: your board's COM port (for example `COM5`)

   - **Speed**: `115200`

Select **Open** to connect to the Zephyr UART shell.

<p style="text-align:center;">
  <img src="/learning-paths/embedded-and-microcontrollers/zephyr_shell/images/putty_installation.png"
       alt="PuTTY Installation"
       width="640"
       style="max-width:100%;height:auto;" />
  <br/>
  <em>PuTTY Serial Terminal Configuration</em>
</p>

### macOS

macOS includes a built-in UART terminal utility through the `screen` command, so no additional software is required.

After connecting the development board over USB:

1. Open a terminal window.

2. List available serial devices:

```bash

ls /dev/tty.*

```

3. Identify the board's serial device.

4. Connect to the UART shell with:

```bash

screen /dev/tty.usbmodemXXXX 115200

```

Replace `/dev/tty.usbmodemXXXX` with the serial device shown on your system.

To exit `screen`:

1. Press `Ctrl + A`

2. Press `K`

3. Press `Y` to confirm

{{% notice Note %}}

Workbench for Zephyr supports multiple debug runners depending on the connected board. The FRDM-MCXN947 board uses the onboard CMSIS-DAP / LinkServer interface for flashing and debugging, while shell access in this Learning Path uses UART over USB.

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

In the next section, you will read a short overview of the Zephyr shell subsystem and the two transports used in this Learning Path. After that, you will build the MQTT shell and the UART shell on the FRDM-MCXN947 using a USB serial connection and a UART terminal application such as PuTTY or the built-in macOS `screen` utility.
