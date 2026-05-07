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

The shell command tree is independent of the backend transport. The same commands can run over UART, RTT, MQTT, or another enabled backend. You select a backend by setting a single Kconfig option, with no code changes in `main.c`.

In this Learning Path you will use two shell backends:

- `CONFIG_SHELL_BACKEND_MQTT=y` routes shell commands and responses over MQTT topics:

  - Inbound: `<device_id>/sh/rx`

  - Outbound: `<device_id>/sh/tx`  

  The backend connects automatically once the board has an IPv4 address. The MQTT backend is IPv4-only.

- `CONFIG_SHELL_BACKEND_RTT=y` routes shell commands and responses over SEGGER RTT channel 0. The shell is reachable from the first instruction after reset, with no network and no UART required, as long as a J-Link debug interface is available.

Multiple backends can be enabled at the same time in a single application when the board has the required peripherals and memory.

A minimal shell build with only the kernel and device modules typically adds roughly 10 to 15 KB to flash and a few hundred bytes to RAM, depending on the configuration and enabled modules.

## What you will do next

You will build two small Zephyr applications, each enabling one backend:

- **MQTT shell** on the NXP FRDM-MCXN947, with a local Mosquitto broker running in Docker. You will send commands and read responses with the `mosquitto_pub` and `mosquitto_sub` command-line tools.

- **RTT shell** on the Silicon Labs xG27 Dev Kit, with the SEGGER J-Link RTT Viewer.

Each example is portable to any Zephyr-supported board with the right peripheral (Ethernet for MQTT, J-Link for RTT). The "Switch to a different board" section near the end of each page shows how to change the target board on an existing project.

For more information on the shell subsystem, see the [Zephyr Shell documentation](https://docs.zephyrproject.org/latest/services/shell/index.html).
