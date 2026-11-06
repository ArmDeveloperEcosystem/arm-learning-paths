---
title: "Load the firmware from running Yocto Linux"
description: Transfer the Zephyr ELF over SSH and start an offline Cortex-M4F through the supplied helper.
weight: 5
layout: "learningpathall"
---

## Transfer the ELF to the board

Keep the MCU serial terminal open. From the development host, copy the built executable over the Part 1 network connection:

```bash
cd "$HOME/pb2-zephyr-workspace"
scp build/pb2-m4-heartbeat/zephyr/zephyr.elf root@192.168.7.2:/root/pb2-heartbeat.elf
ssh root@192.168.7.2
```

Use the board's actual address if you changed its network setup. All remaining commands on this page run as root on PocketBeagle 2.

## Check the M4's current state

On the pocketbeagle2 via an SSH shell, inspect the remote processor and driver logs:

```bash
pb2-m4 status
dmesg | grep -E 'remoteproc|m4f|5000000'
```

Continue only when the M4 reports `offline`; the helper refuses other states. `running` means firmware is already executing. `attached` or `detached` can indicate bootloader ownership. Changing the firmware name does not replace running code.

The kernel can report a missing default `am62-mcu-m4f0_0-fw` file during boot. If the M4 still registers and remains offline, the sample helper can select its own firmware filename. Missing reserved-memory, mailbox, or driver errors need to be fixed before proceeding.

## Start the heartbeat

Load the sample while Yocto Linux is running:

```bash
pb2-m4 load /root/pb2-heartbeat.elf
pb2-m4 status
```

The helper validates that the file is a 32-bit, little-endian Arm ELF, installs it as `/lib/firmware/pb2-zephyr-heartbeat.elf`, and writes that filename and `start` to the selected M4's remoteproc controls. It never overwrites TI's default firmware filename or resets the R5 system-management processor.

The final status must show `state=running` and `firmware=pb2-zephyr-heartbeat.elf`. That proves the kernel started the core; the UART heartbeat on the next page proves that your application reached its loop.

The helper does not configure automatic startup. The tutorial's ELF is loaded into MCU memory, rather than flashed to the MSPM0 or used as a replacement for Linux's boot image.

## Plan another firmware run

The [pinned driver's stop implementation](https://github.com/beagleboard/linux/blob/2eea568f445af33f3280261904bf1027b02512d8/drivers/remoteproc/ti_k3_common.c) waits for a firmware shutdown acknowledgment. This heartbeat does not implement that protocol. For this simple sample on the pinned kernel, use a controlled board restart before another load. Save work first: restarting interrupts SSH and Greengrass until Linux reconnects. Do not use a `stop` command, driver unbinding, or a forced reset as a workaround for the missing shutdown handshake.

After a restart, check `pb2-m4 status` again. If a warm restart leaves the M4 attached or running, shut down Linux and power-cycle the board. If your bootloader is configured to preload M4 firmware, that configuration must be disabled before Linux can own an offline core. This tutorial does not replace a bootloader-owned firmware in place.

Do not copy the sample over the default firmware filename to make it start automatically: boot-time ownership and shutdown handling need a separate integration design.

## What you have accomplished

You have transferred the Zephyr ELF to the board and used `pb2-m4` to start the offline Cortex-M4F. The M4 now runs your firmware alongside Yocto Linux on the Cortex-A53 cores.

Next, observe the numbered heartbeat on MCU_UART0 and verify that Linux and Greengrass remain active.
