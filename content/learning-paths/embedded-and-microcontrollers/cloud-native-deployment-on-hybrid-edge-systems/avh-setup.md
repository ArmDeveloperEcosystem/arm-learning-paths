---
title: AVH device setup
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup i.MX 8M Plus model

AVH offers a 30-day free trial to use.
-	Create an account in [Arm Virtual Hardware](https://app.avh.arm.com/login)
-	Once logged in, you should see a similar screen as shown in the image below. Click on **Create device**:
  
![Screenshot of the Arm Virtual Hardware dashboard showing the Create device button in the top right corner#center](avh_images/avh1.png "Arm Virtual Hardware dashboard with Create device button")
- Next, click on **Default Project**:
  
![Screenshot showing the project selection screen with Default Project highlighted#center](avh_images/avh2.png "Project selection screen")
- Select the **i.MX 8M Plus** device. The platform runs four Cortex-A53 processors:

![Screenshot of the device selection list with i.MX 8M Plus highlighted, showing it contains four Cortex-A53 processors and one Cortex-M7#center](avh_images/avh3.png "Device selection showing i.MX 8M Plus")

- Select the Yocto Linux (full) (2.2.1) image and click **Select**:
  
![Screenshot of the firmware image selection showing Yocto Linux (full) version 2.2.1 selected#center](avh_images/avh4.png "Firmware image selection for Yocto Linux")
- Click on **Create device** (note that this could take few minutes):

![Screenshot showing the device configuration summary with the Create device button at the bottom#center](avh_images/avh5.png "Device creation confirmation screen")

-	A console to Linux running on the Cortex-A should appear. Use “root” to login.

-	Find the IP address for the board model by running the following command (this will be needed to access the device using SSH):
```bash
ip addr
```
![Screenshot of the AVH interface showing the running i.MX 8M Plus model with Linux console on the left and GUI display on the right#center](avh_images/avh6.png "Running AVH model with console and display")

{{% notice Note %}}
The GUI on the right side may not work. You can safely ignore the error you see in the picture above and continue with the learning path.
{{% /notice %}}

### Useful AVH tips

The **Connect** pane shows the different ways that you can connect to the simulated board. The IP address specified should be the same as that visible in the output of the `ip addr` command.

![Screenshot of the AVH Connect pane displaying connection options including VPN configuration, Quick Connect with SSH commands, and the device IP address#center](avh_images/avh7.png "AVH Connect interface with connection options")

**Quick Connect** lets you connect SSH to the AVH model without having to use a VPN configuration. Similarly, you can replace `ssh` for `scp` to copy files from and to the virtual device. In order to use Quick Connect, it's necessary to add your public key via the **Manage SSH keys here** link.

![Screenshot showing the SSH key management interface where you can add or generate SSH keys for Quick Connect access#center](avh_images/avh8.png "SSH key management interface")

To generate an SSH key, you can run the following command on your machine:
```bash
ssh-keygen -t ed25519
```


## Download the pre-built hybrid-runtime

Once your AVH model is set up, you can download the pre-built hybrid-runtime. This GitHub package contains the runtime and some necessary scripts:

```console
wget https://github.com/smarter-project/hybrid-runtime/releases/download/v1.5/hybrid.tar.gz
```

Extract the files to /usr/local/bin using:
```console
tar -C /usr/local/bin/ -xvf hybrid.tar.gz
```
{{% notice Note %}}
If you want to build the hybrid-runtime on your own, instructions can be found in the section of this learning path called [Building the hybrid-runtime and container image](/learning-paths/embedded-and-microcontrollers/cloud-native-deployment-on-hybrid-edge-systems/build-runtime/).
{{% /notice %}}

## Download Firmware container image

For this learning path, there is also a pre-built lightweight Docker container image available on GitHub. You can use it for the `i.MX8M-PLUS-EVK` board. The container image contains a simple FreeRTOS hello-world application built using the NXP SDK.

You can pull the pre-built image onto the AVH model by running the following command:

```console
ctr image pull ghcr.io/smarter-project/hybrid-runtime/hello_world_imx8mp:latest
```
Make sure the container image was pulled successfully. An image with the name *ghcr.io/smarter-project/hybrid-runtime/hello_world_imx8mp:latest* should appear as an output to the following:

```console
ctr image ls
```

