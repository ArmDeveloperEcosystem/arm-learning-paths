---
title: "NXP FRDM i.MX 93: Prepare Linux and the MCU console" 
description: "Verify the Part 1 integration and identify the correct MCU UART."
weight: 3
layout: "learningpathall"
---

## Confirm the same board and image from part 1

On NXP FRDM i.MX 93 through SSH:

```bash
uname -m
cat /etc/nxp-lp/board.json
nxp-mcore status
systemctl status --with-dependencies greengrass-lite.target
```

You should see the NXP FRDM i.MX 93 profile, `aarch64`, healthy Greengrass, and an **offline application Cortex-M33**. The helper selects by `fsl,imx93-cm33` in the running device tree. It refuses ambiguous matches.

## Open the MCU DEBUG console

Use P16 USB debug, M33 serial port at **115200 baud, eight data bits, no parity, one stop bit, no flow control**. Use the board manual to identify the correct enumerated COM port; Linux's debug console and the MCU port are separate.

On the Ubuntu workstation:

```bash
ls /dev/ttyUSB*
picocom -b 115200 --flow n /dev/YOUR_MCU_DEBUG_PORT
```

## Additional Details: FRDM boot and memory reservations

Use the corrected Part 1 image for `imx93-11x11-lpddr4x-frdm`, including its complete
FRDM boot firmware. At the first U-Boot prompt verify the control-tree model and
compatible identify FRDM, then use the corrected default BSP boot path. Linux
must receive `clk-imx93.mcore_booted`. Part 1 now applies the preparation automatically;
manual recovery is only needed when an old saved environment overrides it.

On Linux, with the application MCU offline:

```bash
cat /proc/device-tree/model
cat /proc/cmdline
python3 /usr/libexec/nxp-lp/check-linux.py
```

The preflight checks this FRDM identity, required boot arguments, the four exact
named memory reservations, including the DDR table at `0xa4010000`,
released MCU peripherals and the matching offline
remoteproc. `nxp-mcore load` and the foreground manager run it before firmware
selection or `start`. It does not qualify TCM hardware access or firmware
execution. `collect-linux.py` in the source bundle captures a read-only report.
See `FRDM-INTEGRATION.md` for the addresses and board-specific ownership policy.

## What you have learned

You can verify the matching image and offline application core, keep Linux and Greengrass available, and monitor the actual MCU serial console via the DEBUG serial port on the board.
