---
title: Set up a Jetson Thor as an AWS IoT Greengrass core device

weight: 4

layout: "learningpathall"
---

### About Jetson Thor

In this section, you prepare a Jetson Thor device to become an AWS IoT Greengrass core device. Jetson Thor uses the Arm Neoverse V3AE processor, which is Armv9-A. Because PAC and BTI are mandatory in Armv9-A, the Jetson Thor fully supports both features. It serves as the positive comparison platform in this test.

### Basic OS install

To install NVIDIA JetPack 7.1 on Jetson Thor, follow the [NVIDIA JetPack 7.1 installation guide](https://www.youtube.com/watch?v=IpiZyoqQTl8).


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

Your output should resemble:

```output
openjdk 25.0.2 2026-01-20
OpenJDK Runtime Environment (build 25.0.2+10-Ubuntu-124.04)
OpenJDK 64-Bit Server VM (build 25.0.2+10-Ubuntu-124.04, mixed mode, sharing)
```

### Install AWS IoT Greengrass

Before you complete these steps, create an AWS access key pair for the account you will use. You can follow the [AWS Setup Tutorial: Create Account, IAM User & AWS CLI](https://www.youtube.com/watch?v=QzTkIfQNsVw) or ask your AWS administrator.

1. Open the AWS Console and go to **IoT Core** > **Greengrass devices** > **Core devices**.

2. Select **Set up core device** > **Set up one core device**.

3. Enter a core device name that is different from your RPi5 device.

4. Select **Select an existing group** and choose `My_PAC_BTI_Test_Devices`.

5. Select **Greengrass nucleus** for installation.

6. Select **Linux**.

![AWS IoT Greengrass setup wizard showing Linux selected and the existing device group My_PAC_BTI_Test_Devices selected#center](images/greengrass-1a.png "Greengrass core device setup — selecting the existing thing group")

7. Select **Set up a device by downloading and running an installer locally on device**.

8. Follow the generated installer instructions on the Jetson Thor and authenticate with your AWS credentials.

![Generated Greengrass installer commands to run on the Jetson Thor to complete core device registration#center](images/greengrass-2.webp "Generated installer commands for the Jetson Thor")

9. Confirm registration by selecting **View core devices**.

   You should see the Jetson Thor listed with recent activity.

### What's next

Your Jetson Thor is now set up as an AWS IoT Greengrass core device. Next, you'll create the custom component used to test PAC/BTI on both devices.