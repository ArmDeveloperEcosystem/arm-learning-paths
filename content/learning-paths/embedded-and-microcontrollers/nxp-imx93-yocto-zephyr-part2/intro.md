---
title: "NXP FRDM i.MX 93: Run Zephyr alongside Linux"
description: "Understand the board-specific application MCU and remoteproc lifecycle." 
weight: 2
layout: "learningpathall"
---

## Keep Linux and add a real-time application

Retain the Part 1 image, Greengrass identity, and Hello World deployment on NXP FRDM i.MX 93. Build Zephyr for the application Cortex-M33 while Linux stays on Cortex-A55. The firmware prints a numbered heartbeat on the MCU console and also exposes an RPMsg TTY to Linux.

| Resource | Details |
| --- | --- |
| Linux machine | `imx93-11x11-lpddr4x-frdm` |
| Zephyr target | `lp_frdm_imx93/mimx9352/m33` |
| Runtime control | Linux remoteproc compatible `fsl,imx93-cm33` |
| Host versions | Zephyr v4.3.0 / SDK 0.17.4 |
| Telemetry / control | `/dev/nxp-temperature` / `/dev/nxp-mcore-control` |

The supplied `lp_frdm_imx93/mimx9352/m33` definition is a local MCU board port using the SoC definitions and board routing. Zephyr v4.3.0 does not provide an upstream FRDM-IMX93 target for this MCU. Use the supplied board root and application-core target.

## Understand startup and shutdown

The application announces two `rpmsg-tty` endpoints. Fixed remote addresses distinguish telemetry (`0x400`) and lifecycle control (`0x401`); the image's udev rules create stable aliases. The MCU owns its resources; Linux loads the ELF and manages the application's power state.

The resource-table patch prevents Zephyr from copying its original table over the vring addresses that Linux has already populated. It is specific to the Linux-managed firmware in this series. Keep a dedicated west workspace for these apps.

Before stopping the core, the foreground Linux manager requests `STOP` over the separate control endpoint and requires `QUIESCED`. The MCU enters WFI after completing its work. The NXP driver then performs the platform's SMC/SCMI stop. The source and image use this NXP SoC's mailbox and memory map.

## Additional Technical References

| Topic | Source |
| --- | --- |
| Board setup and boot | [NXP FRDM i.MX 93 guide](https://www.nxp.com/document/guide/getting-started-with-frdm-imx93:GS-FRDM-IMX93) and [hardware manual](https://www.nxp.com/webapp/Download?colCode=UM12181) |
| Release and machine selection | [NXP BSP manifest](https://github.com/nxp-imx/imx-manifest/blob/07d7cd3f29a18e809f6391eea1be01103b1d6e13/imx-6.12.49-2.2.0.xml) and [machine configuration](https://github.com/nxp-imx/meta-imx/blob/1cfbbb8f9ce1d6071775ea6083b79d98597c8206/meta-imx-bsp/conf/machine/imx93-11x11-lpddr4x-frdm.conf) |
| Kernel and remoteproc | [Linux recipe](https://github.com/nxp-imx/meta-imx/blob/1cfbbb8f9ce1d6071775ea6083b79d98597c8206/meta-imx-bsp/recipes-kernel/linux/linux-imx_6.12.bb), [driver](https://github.com/nxp-imx/linux-imx/blob/df24f9428e38740256a410b983003a478e72a7c0/drivers/remoteproc/imx_rproc.c), and [board DTS](https://github.com/nxp-imx/linux-imx/blob/df24f9428e38740256a410b983003a478e72a7c0/arch/arm64/boot/dts/freescale/imx93-11x11-frdm.dts) |
| Zephyr baseline and RPMsg | [v4.3.0 board sources](https://github.com/zephyrproject-rtos/zephyr/tree/v4.3.0/boards/nxp/frdm_imx93) and [OpenAMP resource-table sample](https://github.com/zephyrproject-rtos/zephyr/tree/v4.3.0/samples/subsys/ipc/openamp_rsc_table) |
| Greengrass Lite packaging | [Pinned Walnascar recipe](https://github.com/aws4embeddedlinux/meta-aws/blob/5d73130967dce143f44fe2f80d65361f6b653c5e/recipes-iot/aws-iot-greengrass/greengrass-lite_2.3.0.bb) and [2.3.0 provisioning](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.3.0/docs/Provisioning.md) |
| Component authoring and delivery | [Recipe reference](https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html), [S3 role permissions](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html), and [deployment creation](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) |
| Cloud publishing | [MQTT IPC authorization](https://docs.aws.amazon.com/greengrass/v2/developerguide/ipc-iot-core-mqtt.html) |
| BMP280 | [Bosch datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf) |

## What you have learned

You understand how NXP FRDM i.MX 93 runs Linux and Zephyr together, which MCU and board target to select, and how the RPMsg control channel makes a normal stop repeatable.
