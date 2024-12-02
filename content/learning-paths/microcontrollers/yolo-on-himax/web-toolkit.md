---
title: Run additional models in the web toolkit
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will view a live camera feed with a computer vision application running.

## Modify the Makefile

Change the directory to the where the Makefile is located. If you cloned the repository to a different location, replace $HOME with the path.

```bash
cd $HOME/Seeed_Grove_Vision_AI_Module_V2/EPII_CM55M_APP_S/
```

The table shows the different options available to use with the web toolkit. Modify the `APP_TYPE` field in the `makefile` to one of the values in the table. Then pass the `--model` argument to the python `xmodem` command.

|APP_TYPE           |Description        | Model argument |
|---                |---                |---
|tflm_yolov8_od     |Object detection   | model_zoo\tflm_yolov8_od\yolov8n_od_192_delete_transpose_0xB7B000.tflite 0xB7B000 0x00000 |
|tflm_fd_fm         |Face detection     | model_zoo\tflm_fd_fm\0_fd_0x200000.tflite 0x200000 0x00000 model_zoo\tflm_fd_fm\1_fm_0x280000.tflite 0x280000 0x00000 model_zoo\tflm_fd_fm\2_il_0x32A000.tflite 0x32A000 0x00000 |

{{% notice Note %}}
For `tflm_fd_fm`, you need to pass all three models as separate `--model` arguments.
{{% /notice %}}



## Regenerate the firmware image

Now you can run `make` to re-generate the `.elf` file.

```bash
make clean
make
```

Use the commands from [Flash firmware onto the microcontroller](/learning-paths/microcontrollers/yolo-on-himax/flash-and-run/) section to run re-generate the firmware image.

```bash
cd ../we2_image_gen_local/
cp ../EPII_CM55M_APP_S/obj_epii_evb_icv30_bdv10/gnu_epii_evb_WLCSP65/EPII_CM55M_gnu_epii_evb_WLCSP65_s.elf input_case1_secboot/
```
Run the script corresponding to the OS of your host machine.

{{< tabpane code=true >}}
  {{< tab header="Linux" language="shell">}}
./we2_local_image_gen project_case1_blp_wlcsp.json
  {{< /tab >}}
  {{< tab header="MacOS" language="shell">}}
./we2_local_image_gen_macOS_arm64 project_case1_blp_wlcsp.json
  {{< /tab >}}
{{< /tabpane >}}


Finally, use `xmodem` to flash the image.

```bash
python xmodem\xmodem_send.py --port=<COM port> \
--baudrate=921600 --protocol=xmodem \
--file=we2_image_gen_local\output_case1_sec_wlcsp\output.img \
--model=<model argument>
```

Press the reset button when prompted before moving on.

## Download the Himax AI web toolkit

The Himax AI web toolkit enables a browser-based graphical user interface (GUI) for the live camera feed.

```bash
wget https://github.com/HimaxWiseEyePlus/Seeed_Grove_Vision_AI_Module_V2/releases/download/v1.1/Himax_AI_web_toolkit.zip
unzip Himax_AI_web_toolkit.zip
```

Open the unzipped directory in your file browsing system and double click `index.html`. This will open the GUI within your default browser.

## Connect to the Grove Vision AI

Select `Grove Vision AI(V2)` in the top-right hand corner and press `Connect` button. Follow the instructions to set up the connection. Now you should see a video feed with a bounding box showing identified objects, poses or face detection.

![Himax web UI](./himax_web_ui.jpg)

The images below are captured images from the models run in the toolkit.

### Objection detection
![object_detection](./object_detection.jpg)

### Face detection
![object_detection](./face_detection.jpg)

