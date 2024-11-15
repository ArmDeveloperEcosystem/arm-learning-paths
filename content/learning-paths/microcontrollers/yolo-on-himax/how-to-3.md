---
title: Flash firmware onto the microcontroller
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that we have generated a firmware file on our local machine, we need to flash the microcontroller with this firmware.

## Install xmodem

`Xmodem` is a basic file transfer protocol. Run the following command to install the dependencies for xmodem. If you cloned the repository to a different location replace $HOME with the path.

```bash
cd $HOME/Seeed_Grove_Vision_AI_Module_V2
pip install -r xmodem/requirements.txt
```

## Connect the module

Insert the FPC cable cable into the Grove Vision AI V2 module. Lift the dark grey latch on the connector as per the image below.

![unlatched](./unlatched.jpg)

Then, slide the FPC connector in with the metal pins facing down and close the dark grey latch to fasten the connector.

![latched](./latched.jpg)

Then connect the Groove Vision AI V2 Module to your computer via the USB-C cable.

### Flash the firmware onto the module

Run the python script below to flash the firmware.

```bash
python xmodem\xmodem_send.py --port=[your COM number] --baudrate=921600 --protocol=xmodem --file=we2_image_gen_local\output_case1_sec_wlcsp\output.img
```

{{% notice Note %}}
When you run other example models demonstrated in the later section [Object detection and additional models](/learning-paths/microcontrollers/yolo-on-himax/how-to-5/), you need to adapt this command.
{{% /notice %}}

TODO: how will the command really change? How to find COM number?

After the firmware image burning is completed, the message `Do you want to end file transmission and reboot system? (y)` is displayed. Press the reset button indicated in the image below.

![reset button](./reset_button.jpg)
