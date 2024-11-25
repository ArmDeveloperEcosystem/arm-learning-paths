---
title: Run and view model results
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will view a live camera feed with the ML application running.

## Download the Himax AI web toolkit

The Himax AI web toolkit enables a browser-based graphical user interface (GUI) for the live camera feed.

```bash
wget https://github.com/HimaxWiseEyePlus/Seeed_Grove_Vision_AI_Module_V2/releases/download/v1.1/Himax_AI_web_toolkit.zip
unzip Himax_AI_web_toolkit.zip
```

Open the unzipped directory in your file browsing system and double click `index.html`. This will open the GUI within your default browser.

## Connect to the Grove Vision AI

Select `Grove Vision AI(V2)` in the top-right hand corner and press `Connect` button. Follow the instructions to set up the connection.

![Himax web UI](./himax_web_ui.jpg)

The image will run the YOLOv8 on your device. By using the camera to identify things from the [Common Objects in Context (COCO) dataset](https://cocodataset.org/#home), which the model has been trained on, you can put the it to the test. Get some common objects ready and move on to the next section.

## View model results

TODO have running section here?