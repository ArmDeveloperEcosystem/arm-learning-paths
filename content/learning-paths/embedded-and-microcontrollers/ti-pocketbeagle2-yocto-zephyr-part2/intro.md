---
title: "Run Linux and Zephyr on separate Arm cores"
description: Understand how Yocto Linux loads a Zephyr UART heartbeat onto the PocketBeagle 2 Cortex-M4F.
weight: 2
layout: "learningpathall"
---

## Add an MCU application to your Linux system

Keep Yocto Linux and Greengrass Lite on the Cortex-A53 cores from Part 1, and add a small Zephyr application on the AM6254's Cortex-M4F microcontroller (MCU). The application prints a numbered heartbeat once per second on the serial UART console. You verify this output while Linux remains reachable over SSH.

The [Zephyr board documentation](https://docs.zephyrproject.org/latest/boards/beagle/pocketbeagle_2/doc/pocketbeagle_2.html) identifies the Cortex-M4F target as `pocketbeagle_2/am6254/m4` and describes Linux remoteproc loading. This Learning Path uses Zephyr v4.3.0 and revision A1 hardware. It uses the M4 inside the AM6254, rather than the separate MSPM0L1105 used for board services.

## Use a UART heartbeat as the test

A repeating UART message provides the same visible liveness check as a blinking LED without taking control of a GPIO or user LED managed by Linux. The sample uses `printk()` and `k_sleep()`; it does not need an AWS deployment or changes to your Greengrass component.

| Processor | Software | How you observe it |
| --- | --- | --- |
| Cortex-A53 | Part 1 Yocto Linux and Greengrass Lite | SSH and the Linux journal |
| Cortex-M4F | Zephyr heartbeat | MCU_UART0 on the expansion header |

Linux remoteproc, the remote-processor framework, loads the ELF firmware executable and starts the M4. Linux and Zephyr must agree on peripheral ownership: the updated image leaves MCU_UART0 to Zephyr.

## Account for the pinned Linux driver

The [Part 1](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/deployment/) yocto image uses a pinned Linux 6.12 kernel. Load the sample only when the M4 reports `offline`. Because this sample does not implement the shutdown handshake expected by the driver, plan a board restart before loading another build.

## What you have learned

You have learned how Yocto Linux on the Cortex-A53 cores loads Zephyr firmware onto the Cortex-M4F. The MCU sends its heartbeat to MCU_UART0 while Linux remains available over SSH.

Next, check the M4 support in your image and connect the MCU serial console.
