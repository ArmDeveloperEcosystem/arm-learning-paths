---
title: (optional) Run additional models in the web toolkit
weight: 6

#draft: true

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will view a live camera feed with the ML application running.

## Modify the Makefile

Change the directory to the where the Makefile is located. If you cloned the repository to a different location, replace $HOME with the path.

```bash
cd $HOME/Seeed_Grove_Vision_AI_Module_V2/EPII_CM55M_APP_S/
```

The table shows the different options available to use with the web toolkit. Modify the `APP_TYPE` field in the `makefile` to one of the values in the table.

|APP_TYPE           |Description        |
|---                |---                |
|tflm_yolov8_od     |Object detection   |
|tflm_yolov8_pose   |Pose detection     |
|tflm_fd_fm         |Face detection     |


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

### Linux

```bash
./we2_local_image_gen project_case1_blp_wlcsp.json
```

### macOS
```console
./we2_local_image_gen_macOS_arm64 project_case1_blp_wlcsp.json
```

Finally, use `xmodem` to flash the image.

```bash
python xmodem\xmodem_send.py --port=<COM port> --baudrate=921600 --protocol=xmodem --file=we2_image_gen_local\output_case1_sec_wlcsp\output.img
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

### Pose estimation
![Pose estimation](./pose_estimation.jpg)

### Face detection
![object_detection](./face_detection.jpg)

