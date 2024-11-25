---
title: Object detection and additional models
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

There are other computer vision applications to try. In this section, you will re-flash the module with a different one and check the results.

## Modify the Makefile

Change the directory to the where the Makefile is located. If you cloned the repository to a different location, replace $HOME with the path.

```bash
cd $HOME/Seeed_Grove_Vision_AI_Module_V2/EPII_CM55M_APP_S/
```

The table shows the different options available to use with the web toolkit. Modify the `APP_TYPE` field in the Makefile to one of the values in the table.

|APP_TYPE =|Description|
|---|---|
|tflm_folov8_od|Object detection|
|tflm_folov8_pose|Pose detection|
|tflm_fd_fm|Face detection|


## Regenerate the firmware image

Now you can run `make` to re-generate the `.elf` file.

```bash
make clean
make
```
Use the command from [Flash firmware onto the microcontroller](/learning-paths/microcontrollers/yolo-on-himax/how-to-3/) section to run re-generate the firmware image.

```bash
python xmodem\xmodem_send.py --port=<COM port> --baudrate=921600 --protocol=xmodem --file=we2_image_gen_local\output_case1_sec_wlcsp\output.img
```

The images below are captured images from the models run in the toolkit.

### Objection detection
![object_detection](./object_detection.jpg)

### Pose estimation
![Pose estimation](./pose_estimation.jpg)

### Face detection
![object_detection](./face_detection.jpg)

