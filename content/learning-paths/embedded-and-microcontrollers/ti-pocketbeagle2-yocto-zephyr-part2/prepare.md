---
title: "Prepare Yocto Linux and the MCU serial console"
description: Check the Part 1 M4 integration and connect a 3.3 V serial adapter to MCU_UART0.
weight: 3
layout: "learningpathall"
---

## Check the updated Part 1 image

Continue with the same pocketbeagle2 board, Yocto image, and Greengrass identity from Part 1. Part 2 creates no new AWS resources or IAM roles.

On the pocketbeagle2 board, check your Linux architecture and M4 support:

```bash
uname -m
command -v pb2-m4
pb2-m4 status
```

Expect `aarch64`, a path to `pb2-m4`, and a device name containing `5000000`. For a core ready to load, the output is similar to:

```output
device=/sys/class/remoteproc/remoteproc0 name=5000000.m4fss state=offline firmware=am62-mcu-m4f0_0-fw
```

The remoteproc index can differ. The helper selects the M4 by its device name; it does not assume that index zero is the M4. The firmware value is a filename, not proof that firmware is running.

{{% notice Important Note %}}

### Update an earlier Part 1 build

Skip this section if your image includes `pb2-m4` and the M4 device appears. If you built Part 1 before the Part 2 additions, download its updated [build bundle](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/pocketbeagle2-scarthgap-build.zip). Back up your local bundle edits, then extract the new bundle over the original bundle directory on the Linux build host:

```bash
unzip -o pocketbeagle2-scarthgap-build.zip -d "$HOME/ti"
cd "$HOME/ti/pocketbeagle2"
WORKDIR="$HOME/yocto-pocketbeagle2" JOBS=4 \
  ./build-pocketbeagle2.sh --no-sdk
```

Reuse the work directory from Part 1. The updated script packages `pb2-m4-tools` and builds a kernel with the M4 driver. Its AM6254 device-tree patch reserves the regions beginning at `0x9cb00000` and `0x9cc00000`, enables the M4 mailbox and remoteproc node, and leaves MCU_UART0 disabled in Linux. Other board revisions are outside this tutorial's scope.

Boot the rebuilt image using the [Part 1 flashing instructions](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/setup/). Use a spare card if you need to preserve the current installation. A fresh image does not contain your device credentials or configuration database: repeat Part 1 networking and provisioning before continuing, using the same board identity only on this board. Do not reset a working Greengrass configuration merely to install the MCU helper.

Copying the helper alone is insufficient when the running device tree lacks the M4's reserved memory. Loading a new device tree requires a restart. After boot, rerun `pb2-m4 status` and confirm the core is `offline`.

{{% /notice %}}

## Connect the MCU UART

Shut down the board and disconnect its power before wiring. Connect a USB-to-UART adapter with 3.3 V logic as follows:

| PocketBeagle 2 connection | Adapter connection | Purpose |
| --- | --- | --- |
| P2.07, MCU_UART0 TX | RX | Read the heartbeat |
| Board GND | GND | Common reference |
| P2.05, MCU_UART0 RX | TX, optional | Not needed by this output-only sample |

Leave the adapter's power lead disconnected. Do not use 5 V logic or an RS-232 voltage-level adapter. Confirm header orientation and a GND pin using the [PocketBeagle 2 hardware documentation](https://docs.beagleboard.org/boards/pocketbeagle-2/03-design-and-specifications.html).

Power the board again and open the adapter's serial port at **115200 baud, eight data bits, no parity, one stop bit, and no flow control**. On an Ubuntu workstation with `picocom` installed, identify the adapter and open its actual device node:

```bash
ls /dev/serial/by-id/
picocom -b 115200 --flow n /dev/serial/by-id/YOUR_USB_UART_ADAPTER
```

Use a separate terminal for SSH. The MCU UART is not the Linux MAIN_UART6 debug connector and is not the USB gadget serial console. Open the MCU terminal before loading firmware so you capture the first message.

## What you have accomplished

Your image exposes the M4 loader and the workstation can listen on its UART. Next, build the heartbeat ELF on your development host.
