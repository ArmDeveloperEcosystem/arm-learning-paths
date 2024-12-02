---
title: Flash firmware onto the microcontroller
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you have generated an image file on the local host machine, you are ready to flash the microcontroller with the firmware.

## Install xmodem

`Xmodem` is a basic file transfer protocol which is easily installed using the Himax examples repository. 

Run the following command to install the dependency:

```bash
cd $HOME/Seeed_Grove_Vision_AI_Module_V2
pip install -r xmodem/requirements.txt
```

## Connect the module

It's time to get the board set up. 

Insert the Flexible printed circuit (FPC) into the Grove Vision AI V2 module. Lift the dark grey latch on the connector as per the image below.

![unlatched](./unlatched.jpg)

Slide the FPC connector in with the metal pins facing down and close the dark grey latch to fasten the connector.

![latched](./latched.jpg)

Now you can connect the Groove Vision AI V2 Module to your computer via the USB-C cable.

{{% notice Note %}}
The development board may have two USB-C connectors. If you are running into issues connecting the board in the next step, make sure you are using the right one.
{{% /notice %}}

## Find the COM port

You'll need to provide the communication port (COM) which the board is connected to in order to flash the image. There are commands to list all COMs available on your machine. Once your board is connected through USB, it'll show up in this list. The COM identifier will start with **tty**, which may help you determine which one it is. You can run the command before and after plugging in the board if you are unsure.


{{< tabpane code=true >}}
  {{< tab header="Linux" language="shell">}}
sudo grep -i 'tty' /var/log/dmesg
  {{< /tab >}}
  {{< tab header="MacOS" language="shell">}}
ls /dev/tty.*
  {{< /tab >}}
{{< /tabpane >}}


{{% notice Note %}}
If the port seems unavailable, try changing the permissions temporarily using the `chmod` command. Be sure to reset them afterwards, as this may pose a computer security vulnerability.

```bash
chmod 0777 <COM port>
```
{{% /notice %}}

The full path to the port is needed in the next step, so be sure to save it. 

## Flash the firmware onto the module

Run the python script below to flash the firmware:

```bash
python xmodem\xmodem_send.py --port=<COM port> \
--baudrate=921600 --protocol=xmodem \
--file=we2_image_gen_local\output_case1_sec_wlcsp\output.img
```

{{% notice Note %}}
When you run other example models demonstrated in the later section [Run additional models in the web toolkit](/learning-paths/microcontrollers/yolo-on-himax/web-toolkit/), you need to adapt this command with `--model` argument.
{{% /notice %}}

After the firmware image flashing is completed, the message `Do you want to end file transmission and reboot system? (y)` is displayed. Press the reset button shown in the image below.

![reset button](./reset_button.jpg)

## Run the model

After the reset button is pressed, the board will start inference with the object detection automatically. Observe the output in the terminal to verify that the image is built correctly. If a person is in front of the camera, you should see the `person_score` value go over `100`.

```output
b'SENSORDPLIB_STATUS_XDMA_FRAME_READY 240'
b'write frame result 0, data size=15284,addr=0x340e04e0'
b'invoke pass'
b'person_score:113'
b'EVT event = 10'
b'SENSORDPLIB_STATUS_XDMA_FRAME_READY 241'
b'write frame result 0, data size=15296,addr=0x340e04e0'
b'invoke pass'
b'person_score:112'
b'EVT event = 10'
```

This means the image works correctly on the device, and the end-to-end flow is complete.