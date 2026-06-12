---
title: Understand the Zephyr shell subsystem and backends
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How the Zephyr shell subsystem works

The Zephyr shell subsystem (`CONFIG_SHELL=y`) adds an interactive command-line interface to your firmware. After the shell is enabled, you can inspect system state, run subsystem commands, and trigger application behavior at runtime without rebuilding or reflashing the application.

Several Zephyr subsystems register shell commands automatically. Common built-in modules include:

| Module | Example commands |
|--------|------------------|
| `kernel` | `version`, `uptime`, `thread list`, `thread stacks` |
| `net` | `iface`, `ping`, `dns`, `tcp` |
| `device` | `list` |
| `log` | `enable`, `disable`, `levels` |
| `shell` | `help`, `history`, `resize` |

For more information on the shell subsystem, see the [Zephyr Shell documentation](https://docs.zephyrproject.org/latest/services/shell/index.html).

## How shell backends work

The shell command tree is independent of the transport. The same commands can run over UART, RTT, MQTT, or another enabled backend. You can select a transport by setting a single Kconfig option, with no code changes in `main.c`.

In this Learning Path you'll work with two transports:

### MQTT backend (`CONFIG_SHELL_BACKEND_MQTT=y`)

Routes shell commands and responses over MQTT topics. The board subscribes to `<device_id>/sh/rx` for inbound commands and publishes responses to `<device_id>/sh/tx`. The backend connects automatically once the board has an IPv4 address. This backend is IPv4-only.

### UART backend (`CONFIG_SHELL_BACKEND_SERIAL=y`)

Routes shell commands and responses over the board's UART interface, accessible through a USB serial connection. Use PuTTY on Windows, or `screen` on macOS and Linux. This backend works on a wide range of Zephyr-supported development boards with no additional debug hardware required.

Multiple backends can be enabled at the same time in a single application when the board has the required peripherals and memory.

A minimal shell build with only the kernel and device modules adds roughly 10 to 15 KB to flash and a few hundred bytes to RAM on a Cortex-M target. The exact footprint depends on the modules enabled and the toolchain optimization level.

## What you will build next

You've now learned how the Zephyr shell subsytem and shell backends work.

Next, you'll build a small Zephyr application that enables the MQTT shell on the NXP FRDM-MCXN947, with a local Mosquitto broker running in Docker. You'll send commands and read responses with the `mosquitto_pub` and `mosquitto_sub` command-line tools.