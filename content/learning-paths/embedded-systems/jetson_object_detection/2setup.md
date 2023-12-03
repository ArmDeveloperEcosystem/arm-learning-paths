---
title: Set up your Jetson Orin Nano
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

Download and install [balenaEtcher](https://etcher.balena.io/) in order to write the image to the microSD card

### Download the latest image

Head to [NVIDIA's site](https://developer.nvidia.com/embedded/jetpack). Click on the box titled "JETSON XAVIER NX DEVELOPER KIT & ORIN NANO DEVELOPER KIT" to expand, and click on "JETSON Orin Nano DEVELOPER KIT" to download the latest image.

![sdCard Image](./sdcardimage.png)

### Write to the microSD card with balenaEtcher

1. Launch balenaEtcher
2. Click "Flash from file"
![balenaEtcher interface](./balenaEtcher1.png)
3. Select the zip file of the image you just downloaded previously. You don't need to unzip it first
4. Click "Select target", and choose your microSD card
5. Click "Flash" and wait for the process to complete. You may be prompted to enter a username and password before it will start, and it will take around ten minutes
6. Eject the card from your computer, and insert the microSD card into the Jetson Orin Nano. Don't power on the device yet

### Connect the camera to the Jetson Orin Nano

Insert the 22 pin side (it is smaller than the 15 pin side) of the ribbon into the CSI connector labeled "CAM0." It should be inserted silver pin side down.
If you are unsure of how to insert one of these ribbons into the connector [here is a useful video explaining the process](https://www.youtube.com/watch?v=EuRXAUU61yM&t=7s)

**Note:** You can use a USB camera for object detection as well, but it is outside the scope of this learning path

![image of the ribbon inserted into the connector](./cam0connector.jpg)

### Power on the Jetson Orin Nano

The initial startup process will take a while, just follow along with the prompts. When you finally get the the desktop with NVIDIA's wallpaper, make sure to run the following commands to get up to date:
```
sudo apt update
sudo apt upgrade
```

At some point you may be prompted to reboot. Do so before continuing.

### Verify that the camera is working

In the terminal, check that the camera is detected.
```
ls /dev/video0
```

If everything is connected properly you should see the following output:
```
/dev/video0
```

To test the capture, enter the following command. The number following --orientation determines how the picture is rotated. Options are 0 - 3. It might take a couple minutes to start up the first time, during which your device will be locked up. Subsequent use of the command should only take a few seconds.
```
nvgstcapture-1.0 --orientation 2
```
Use Ctrl + C in the terminal to end the capture
