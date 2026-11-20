---
title: "NXP FRDM i.MX 8M Plus: Run Zephyr alongside Linux"
description: "Understand the board-specific application MCU and remoteproc lifecycle."
weight: 2
layout: "learningpathall"
---

## Keep Linux and add a real-time application

Retain the Part 1 image, Greengrass identity, and Hello World deployment on NXP FRDM i.MX 8M Plus. Build Zephyr for the application Cortex-M7 while Linux stays on Cortex-A53. The firmware prints a numbered heartbeat on the MCU console and also exposes an RPMsg TTY to Linux.

| Resource | Details |
| --- | --- |
| Yocto machine | `imx8mp-lpddr4-frdm` |
| Zephyr target | `imx8mp_evk/mimx8ml8/m7` |
| Runtime control | Linux remoteproc compatible `fsl,imx8mn-cm7` |
| Host versions | Zephyr v4.3.0 / SDK 0.17.4 |
| Telemetry / control | `/dev/nxp-temperature` / `/dev/nxp-mcore-control` |

The FRDM profile reuses Zephyr v4.3.0's `imx8mp_evk/mimx8ml8/m7` target for i.MX 8M Plus SoC support. This is an upstream software identifier; the physical board is FRDM-IMX8MPLUS. Keep the supplied application overlay and resource-table patch with that target.

## Understand startup and shutdown

The application announces two `rpmsg-tty` endpoints. Fixed remote addresses distinguish telemetry (`0x400`) and lifecycle control (`0x401`); the image's udev rules create stable aliases. The MCU owns its resources; Linux loads the ELF and manages the application's power state.

The resource-table patch prevents Zephyr from copying its original table over the vring addresses that Linux has already populated. It is specific to the Linux-managed firmware in this series. Keep a dedicated west workspace for these apps.

Before stopping the core, the foreground Linux manager requests `STOP` over the separate control endpoint and requires `QUIESCED`. The MCU enters WFI after completing its work. The NXP driver then performs the platform's SMC/SCMI stop. The source and image use this NXP SoC's mailbox and memory map.

## Additional Technical References

| Topic | Source |
| --- | --- |
| Board setup and boot | [NXP FRDM i.MX 8M Plus guide](https://www.nxp.com/document/guide/getting-started-with-frdm-imx8mplus:GS-FRDM-IMX8MPLUS) and [hardware manual](https://www.nxp.com/webapp/Download?colCode=UM12340) |
| Release and machine selection | [NXP BSP manifest](https://github.com/nxp-imx/imx-manifest/blob/07d7cd3f29a18e809f6391eea1be01103b1d6e13/imx-6.12.49-2.2.0.xml) and [machine configuration](https://github.com/nxp-imx/meta-imx/blob/1cfbbb8f9ce1d6071775ea6083b79d98597c8206/meta-imx-bsp/conf/machine/imx8mp-lpddr4-frdm.conf) |
| Kernel and remoteproc | [Linux recipe](https://github.com/nxp-imx/meta-imx/blob/1cfbbb8f9ce1d6071775ea6083b79d98597c8206/meta-imx-bsp/recipes-kernel/linux/linux-imx_6.12.bb), [driver](https://github.com/nxp-imx/linux-imx/blob/df24f9428e38740256a410b983003a478e72a7c0/drivers/remoteproc/imx_rproc.c), and [board DTS](https://github.com/nxp-imx/linux-imx/blob/df24f9428e38740256a410b983003a478e72a7c0/arch/arm64/boot/dts/freescale/imx8mp-frdm.dts) |
| Zephyr baseline and RPMsg | [FRDM MCU build profile](bundle/README.md) and [OpenAMP resource-table sample](https://github.com/zephyrproject-rtos/zephyr/tree/v4.3.0/samples/subsys/ipc/openamp_rsc_table) |
| Greengrass Lite packaging | [Pinned Walnascar recipe](https://github.com/aws4embeddedlinux/meta-aws/blob/5d73130967dce143f44fe2f80d65361f6b653c5e/recipes-iot/aws-iot-greengrass/greengrass-lite_2.3.0.bb) and [2.3.0 provisioning](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.3.0/docs/Provisioning.md) |
| Component authoring and delivery | [Recipe reference](https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html), [S3 role permissions](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html), and [deployment creation](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) |
| Cloud publishing | [MQTT IPC authorization](https://docs.aws.amazon.com/greengrass/v2/developerguide/ipc-iot-core-mqtt.html) |
| FRDM sensor header | [NXP FRDM-IMX8MPLUS schematic, sheet 21](https://www.nxp.com/downloads/en/schematics/FRDM-IMX8MPLUS-SCH-95022_B1.zip) |
| BMP280 | [Bosch datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf) |

## What you have learned

You understand how NXP FRDM i.MX 8M Plus runs Linux and Zephyr together, which MCU and board target to select, and how the RPMsg control channel makes a normal stop repeatable.