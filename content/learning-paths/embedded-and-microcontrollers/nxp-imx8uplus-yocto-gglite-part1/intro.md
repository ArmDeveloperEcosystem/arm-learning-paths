---
title: "NXP FRDM i.MX 8M Plus: Build a connected edge device"
description: "Introduction: the board, resources used, and three-part workflow objectives."
weight: 2
layout: "learningpathall"
---

## Three part series

This three-part series connects an embedded Linux processor, a Zephyr MCU, and AWS IoTCore present in the **NXP FRDM i.MX 8M Plus** device. Part 1 builds and boots Yocto Linux running on its Cortex-A53, provisions Greengrass Lite, and deploys a simple Hello World component to the device via Greengrass. Part 2 adds a custom Zephyr heartbeat on the devices' Cortex-M7 MCU. Part 3 connects a BMP280 sensor, deploys both a Zephyr BMP280 reader application on the MCU as well as a Yocto-based Linux-to-IoT-Core bridge as two custom AWS Greengrass components. With the two custom components deployed in part 3 the temperature values, read in Zephyr, are conveyed through the bridge in Yocto up to AWS IoTCore where they are published as JSON-based messages in IoTCore.

| Resources Used | Details |
| --- | --- |
| Yocto machine name | `imx8mp-lpddr4-frdm` |
| BSP | NXP LF6.12.49_2.2.0, Yocto 5.2 Walnascar |
| Linux | NXP 6.12.49, pinned source revision |
| AWS Greengrass Runtime | Greengrass nucleus lite 2.3.0 from the pinned Walnascar meta-aws layer |
| MCU | Cortex-A53 / Cortex-M7 |
| AWS IoTCore device name / group | `MyNXPIMX8MPlus` / `NXPIMX8MPlusDevices` |

Allow several additional hours for a first uncached Yocto build. The image retains development login settings and is intended for a controlled development network.

## Part 1 - Building Yocto: Use the supplied build bundle

Download [the NXP FRDM i.MX 8M Plus yocto build bundle](../yocto-build.zip), extract it to a fixed Linux filesystem path, and keep the local layer with the script. The script uses the official NXP release manifest and this board's actual machine configuration. It adds Greengrass, Python, MCU tools, RPMsg TTY support, and explicit peripheral ownership for the later parts.

These are source-level adaptations with local checks. The build, device journal, sensor response, and repeatable remove/redeploy checks in the following sections establish acceptance on your hardware. Downloadable bundles include the exact revisions and limits in `AUDIT.md`.

## Technical References

| Topic | Source |
| --- | --- |
| Board setup and boot | [NXP FRDM i.MX 8M Plus guide](https://www.nxp.com/document/guide/getting-started-with-frdm-imx8mplus:GS-FRDM-IMX8MPLUS) and [hardware manual](https://www.nxp.com/webapp/Download?colCode=UM12340) |
| Release and machine selection | [NXP BSP manifest](https://github.com/nxp-imx/imx-manifest/blob/07d7cd3f29a18e809f6391eea1be01103b1d6e13/imx-6.12.49-2.2.0.xml) and [machine configuration](https://github.com/nxp-imx/meta-imx/blob/1cfbbb8f9ce1d6071775ea6083b79d98597c8206/meta-imx-bsp/conf/machine/imx8mp-lpddr4-frdm.conf) |
| Kernel and remoteproc | [Linux recipe](https://github.com/nxp-imx/meta-imx/blob/1cfbbb8f9ce1d6071775ea6083b79d98597c8206/meta-imx-bsp/recipes-kernel/linux/linux-imx_6.12.bb), [driver](https://github.com/nxp-imx/linux-imx/blob/df24f9428e38740256a410b983003a478e72a7c0/drivers/remoteproc/imx_rproc.c), and [board DTS](https://github.com/nxp-imx/linux-imx/blob/df24f9428e38740256a410b983003a478e72a7c0/arch/arm64/boot/dts/freescale/imx8mp-frdm.dts) |
| Zephyr baseline and RPMsg | [FRDM MCU build profile](../nxp-imx8uplus-yocto-zephyr-part2/bundle/README.md) and [OpenAMP resource-table sample](https://github.com/zephyrproject-rtos/zephyr/tree/v4.3.0/samples/subsys/ipc/openamp_rsc_table) |
| Greengrass Lite packaging | [Pinned Walnascar recipe](https://github.com/aws4embeddedlinux/meta-aws/blob/5d73130967dce143f44fe2f80d65361f6b653c5e/recipes-iot/aws-iot-greengrass/greengrass-lite_2.3.0.bb) and [2.3.0 provisioning](https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.3.0/docs/Provisioning.md) |
| Component authoring and delivery | [Recipe reference](https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html), [S3 role permissions](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html), and [deployment creation](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) |
| Cloud publishing | [MQTT IPC authorization](https://docs.aws.amazon.com/greengrass/v2/developerguide/ipc-iot-core-mqtt.html) |
| FRDM sensor header | [NXP FRDM-IMX8MPLUS schematic, sheet 21](https://www.nxp.com/downloads/en/schematics/FRDM-IMX8MPLUS-SCH-95022_B1.zip) |
| BMP280 | [Bosch datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf) |

## What you have learned

You understand how NXP FRDM i.MX 8M Plus, its NXP BSP machine, and its AWS identity fit together and are used in these 3 part series. You can follow the build path: Yocto → Hello World → MCU heartbeat app → managed sensor telemetry progression into AWS IoTCore using the above platform-specific resources.
