---
title: Set up a Jetson Thor as an AWS IoT Greengrass core device

weight: 4

layout: "learningpathall"
---

## Configure a Jetson Thor as a positive comparison platform

In this section, you'll prepare a Jetson Thor device to become an AWS IoT Greengrass core device. Jetson Thor uses the Arm Neoverse V3AE processor, which is Armv9-A. Because PAC and BTI are mandatory in Armv9-A, the Jetson Thor fully supports both features. The device serves as the positive comparison platform in this test.

### Install JetPack

Install NVIDIA JetPack 7.1 on Jetson Thor. For instructions on getting started with a Jetson Thor device, see [Quick Start](https://docs.nvidia.com/jetson/agx-thor-devkit/user-guide/latest/quick_start.html).


### Install Java

Open a terminal on your Jetson Thor and run:

```bash
sudo apt update
sudo apt -y dist-upgrade
sudo apt install -y default-jdk
```

Confirm that Java is available:

```bash
java --version
```

The output is similar to:

```output
openjdk 25.0.2 2026-01-20
OpenJDK Runtime Environment (build 25.0.2+10-Ubuntu-124.04)
OpenJDK 64-Bit Server VM (build 25.0.2+10-Ubuntu-124.04, mixed mode, sharing)
```

### Install AWS IoT Greengrass

Use the same AWS account and its credentials that you used for the Raspberry Pi 5 in the previous section. To install AWS IoT Greengrass on the Jetson Thor device:

1. Open the AWS Console and go to **IoT Core** > **Greengrass devices** > **Core devices**.

2. Select **Set up core device** > **Set up one core device**.

3. Enter a core device name that is different from your RPi5 device.

4. For **Thing group**, select **Select an existing group** and choose `My_PAC_BTI_Test_Devices`.

5. For **Greengrass Core software runtime**, select **Greengrass nucleus** for installation.

6. For **Operating system**, select **Linux**.

![AWS IoT Greengrass setup wizard showing Linux selected and the existing device group My_PAC_BTI_Test_Devices selected#center](images/greengrass-1a.png "Greengrass core device setup — selecting the existing thing group")

7. For **Device setup method**, select **Set up a device by downloading and running an installer locally on device**.

8. Follow the generated installer instructions on the Jetson Thor and authenticate with your AWS credentials.

![Generated Greengrass installer commands to run on the Jetson Thor to complete core device registration#center](images/greengrass-2.webp "Generated installer commands for the Jetson Thor")

9. Confirm registration by selecting **View core devices**.

   You should see the Jetson Thor listed with recent activity.

## What you've accomplished and what's next

You've now set up your Jetson Thor as an AWS IoT Greengrass core device as the positive comparison platform for PAC/BTI tests. 

Next, you'll create the custom component used to test PAC/BTI on both devices.