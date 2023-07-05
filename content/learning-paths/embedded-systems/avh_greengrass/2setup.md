---
title: Setup your AWS IoT Greengrass account
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

You will need a user account for [Arm Virtual Hardware 3rd Party Hardware](https://avh.arm.com/). Refer to [Arm Virtual Hardware install guide](/install-guides/avh#thirdparty) for more information.

You will also need a user account for [Amazon AWS](https://aws.amazon.com). This service requires a credit card to use, but this tutorial will only use resources that fall under the free tier, so you can follow along without paying anything.

## Create a Device

From the AVH dashboard, click on the `Create Device` button. You will be presented with a list of devices to choose from, for this tutorial we are using a Raspberry Pi 4, so select that device.

![create device](./create_device.png)

On the next screen you will be asked to configure your device by choosing the firmware to use. AWS IoT Greengrass Core will run on either the Ubuntu Server or Raspberry Pi OS firmware images. For this tutorial we will be using the Ubuntu Server firmware. Select that and click `Next`.

The last step is to give your new AVH device a unique name. You can use whatever you'd like, or go with `greengrass-testing-device` for this tutorial. You do not need to set any advances boot options.

![device ready](device_ready.png)

Once the device creation is complete, log in with the default username `pi` and password `raspberry`.

You are now ready to install AWS IoT Greengrass Core onto your virtual Raspberry Pi.

## Install AWS IoT Greengrass Core

AWS IoT Greengrass Core is the software component that runs on your IoT devices. You will need to install and configure it on your new AVH device, using the console provided by AVH or over an SSH connection.

Follow the [AWS IoT Greengrass install guide](../../../install-guides/aws-greengrass-v2.md) to finish setting up your device.

