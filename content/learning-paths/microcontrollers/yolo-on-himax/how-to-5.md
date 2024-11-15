---
title: Object detection and additional models
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

TODO some more intro here, and showing how to test the model
Also double check this section

## Modify the Makefile

TODO: why are we doing this?

Change the directory to the where the Makefile is located. If you cloned the repository to a different location, replace $HOME with the path.

```bash
cd $HOME/Seeed_Grove_Vision_AI_Module_V2/EPII_CM55M_APP_S/
```

Modify the `APP_TYPE` field in the Makefile from the default value of `allon_sensor_tflm` to one of the values in the table below


|APP_TYPE =|Description|
|---|---|
|tflm_folov8_od|Object detection|
|tflm_folov8_pose|Pose detection|
|tflm_fd_fm|Face detection|

## Regenerate the firmware image

Go back to the [Flash firmware onto the microcontroller](/learning-paths/microcontrollers/yolo-on-himax/how-to-3/) section and run the python command to regenerate the firmware image.

The images below are examples images from the model.

### Objection detection
![object_detection](./object_detection.jpg)

### Pose estimation
![Pose estimation](./pose_estimation.jpg)

### Face detection
![object_detection](./face_detection.jpg)

