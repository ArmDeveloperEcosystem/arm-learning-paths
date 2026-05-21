---
title: Overview
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is the Zephyr shell?

The Zephyr shell subsystem (`CONFIG_SHELL=y`) adds an interactive command-line interface to your firmware. After the shell is enabled, you can inspect system state, run subsystem commands, and trigger application behavior at runtime without rebuilding or reflashing the application.

Several Zephyr subsystems register shell commands automatically. Common built-in modules include:

| Module | Example commands |
|--------|------------------|
| `kernel` | `version`, `uptime`, `thread list`, `thread stacks` |
| `net` | `iface`, `ping`, `dns`, `tcp` |
| `device` | `list` |
| `log` | `enable`, `disable`, `levels` |
| `shell` | `help`, `history`, `resize` |

## How shell backends work

The shell command tree is independent of the transport. The same commands can run over UART, RTT, MQTT, or another enabled backend. You select a transport by setting a single Kconfig option, with no code changes in `main.c`.

In this Learning Path you will work with two transports:

- `CONFIG_SHELL_BACKEND_MQTT=y` routes shell commands and responses over MQTT topics. Inbound on `<device_id>/sh/rx`, outbound on `<device_id>/sh/tx`. The backend connects automatically once the board has an IPv4 address. The MQTT backend is IPv4-only.
- `CONFIG_SHELL_BACKEND_SERIAL=y` routes shell commands and responses over the board's UART interface. The shell is accessible through a USB serial connection using a terminal application such as PuTTY on Windows or the built-in `screen` utility on macOS. The UART backend works on a wide range of Zephyr-supported development boards with no additional debug hardware required.

Multiple backends can be enabled at the same time in a single application when the board has the required peripherals and memory.

A minimal shell build with only the kernel and device modules adds roughly 10 to 15 KB to flash and a few hundred bytes to RAM.

## What you will do next

The two following sections each build a small Zephyr application that enables one of these backends:

- **MQTT shell** on the NXP FRDM-MCXN947, with a local Mosquitto broker running in Docker. You will send commands and read responses with the `mosquitto_pub` and `mosquitto_sub` command-line tools.
- **UART shell** on the FRDM-MCXN947, using a USB serial connection with PuTTY on Windows or the built-in `screen` utility on macOS.

Each example is portable to any Zephyr-supported board with the right peripheral (Ethernet for MQTT, J-Link for RTT). The "Switch to a different board" section near the end of each page shows how to change the target board on an existing project.

For more information on the shell subsystem, see the [Zephyr Shell documentation](https://docs.zephyrproject.org/latest/services/shell/index.html).

## What's next?

In the next section, you will build the MQTT shell on the FRDM-MCXN947, run Mosquitto in Docker, and exchange shell commands with the board over MQTT topics.
