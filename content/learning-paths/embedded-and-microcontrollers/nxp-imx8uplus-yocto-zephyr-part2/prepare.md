---
title: "NXP FRDM i.MX 8M Plus: Prepare Linux and the MCU console"
description: "Verify the Part 1 integration and identify the correct MCU UART."
weight: 3
layout: "learningpathall"
---

## Confirm the same board and image from part 1

On NXP FRDM i.MX 8M Plus through SSH:

```bash
uname -m
cat /etc/nxp-lp/board.json
nxp-mcore status
systemctl status --with-dependencies greengrass-lite.target
```

You should see the NXP FRDM i.MX 8M Plus profile, `aarch64`, healthy Greengrass, and an **offline application Cortex-M7**. The helper selects by `fsl,imx8mn-cm7` in the running device tree. It refuses ambiguous matches.

## Open the MCU DEBUG console

When connecting the DEBUG USB port to your Ubuntu host, two specific USB ports will be discovered.  The first USB UART is for the serial console.  The second is for the M7 DEBUG console. Both ports should be set to **115200 baud, eight data bits, no parity, one stop bit, no flow control**. Use the board manual to identify the correct enumerated COM port; Linux's debug console and the MCU port are separate.

On the Ubuntu host:

```bash
ls /dev/ttyUSB*
picocom -b 115200 --flow n /dev/YOUR_MCU_DEBUG_PORT
```

## Additional Details: FRDM boot and memory reservations

First inspect U-Boot's control tree with `fdt addr ${fdtcontroladdr}`,
`fdt print / model`, and `fdt print / compatible`. Require FRDM identity. The
reported failing board was using an EVK control DT despite FRDM Linux DTBs being
present on the card. Boot matching FRDM firmware from the correct SD/eMMC device
before loading M7. The bundle's `BOOT-SETUP.md` gives the detailed repair path.


Before loading any M7 ELF, use the corrected Part 1 image. Its reserved-memory
nodes must be named `vdev0vring0@55000000`, `vdev0vring1@55008000`,
`vdev0buffer@55400000`, and `rsc-table@550ff000`. Older bundles used `vring@...`
names which Linux does not match to its requested vring carveouts. Updating the
Zephyr ELF alone does not repair the deployed Linux DTB.

The corrected Part 1 image automatically runs `prepare_mcore`, then
`bsp_bootcmd`, and selects its custom `imx8mp-frdm.dtb`. No additional manual
U-Boot settings are needed when that boot path is active. On Linux, view:

```bash
cat /proc/device-tree/model
cat /proc/cmdline
```

You should see the FRDM identity and `clk-imx8mp.mcore_booted` in the command line on every
boot. An old saved U-Boot environment can override the corrected defaults;
`BOOT-SETUP.md` documents a temporary recovery boot and Part 1's setup page
explains the conditional one-time saved-environment repair. Use `bsp_bootcmd`
in that recovery path so a prior `bootflow` command cannot bypass `mmcargs`.
NXP's stock FRDM instructions instead select `imx8mp-frdm-rpmsg.dtb`; that tree
is a separate demo integration. This path modifies `imx8mp-frdm.dtb` directly.

## What you have learned

You can verify the matching image and offline application core, keep Linux and Greengrass available, and monitor the actual MCU serial console via the DEBUG serial port on the board.
