---
title: "NXP FRDM i.MX 93: Build a connected edge device"
description: "Understand the board, BSP release, and three-part workflow."
weight: 2
layout: "learningpathall"
---

## Three part series 

This three-part series connects an embedded Linux processor, a Zephyr MCU, and AWS on **NXP FRDM i.MX 93**. Part 1 builds and boots Yocto Linux on Cortex-A55, provisions Greengrass Lite, and deploys Hello World to an AWS IoT thing group. Part 2 adds a Zephyr heartbeat on the application Cortex-M33. Part 3 connects a BMP280 sensor and deploys a Zephyr temperature reader and a Linux-to-IoT-Core bridge as two custom AWS Greengrass components.

| Resources Used | Details |
| --- | --- |
| Yocto machine | `imx93-11x11-lpddr4x-frdm` |
| BSP | NXP LF6.12.49_2.2.0, Yocto 5.2 Walnascar |
| Linux | NXP 6.12.49, pinned source revision |
| Runtime | Greengrass nucleus lite 2.3.0 from the pinned Walnascar meta-aws layer |
| Linux / MCU | Cortex-A55 / Cortex-M33 |
| AWS IoTCore device name / group | `MyNXPIMX93` / `NXPIMX93Devices` |

Allow several additional hours for a first uncached Yocto build. The image retains development login settings and is intended for a controlled development network.

## Part 1 - Building Yocto: Use the supplied build bundle

Download [the NXP FRDM i.MX 93 build bundle](../yocto-build.zip), extract it to a fixed Linux filesystem path, and keep the local layer with the script. The script uses the official NXP release manifest and this board's actual machine configuration. It adds Greengrass, Python, MCU tools, RPMsg TTY support, and explicit peripheral ownership for the later parts.

These are source-level adaptations with local checks. The build, device journal, sensor response, and repeatable remove/redeploy checks in the following sections establish acceptance on your hardware. Downloadable bundles include the exact revisions and limits in `AUDIT.md`.

## Technical References

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

YYou understand how NXP FRDM i.MX 93, its NXP BSP machine, and its AWS identity fit together and are used in these 3 part series. You can follow the build path: Yocto → Hello World → MCU heartbeat app → managed sensor telemetry progression into AWS IoTCore using the above platform-specific resources.
