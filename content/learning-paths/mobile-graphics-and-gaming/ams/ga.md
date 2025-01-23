---
# User change
title: "Graphics Analyzer"

weight: 9 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Graphics Analyzer is a tool to help `OpenGL ES` and `Vulkan` developers get the best out of their applications through analysis at the API level.

The tool allows you to observe API call arguments and return values, and interact with a running target application to investigate the effect of individual API calls. It highlights attempted misuse of the API, and gives recommendations for improvements.

## Prerequisites

Build your application, and setup your Android device as described in [Setup tasks](/learning-paths/mobile-graphics-and-gaming/ams/setup_tasks/).

## Capture data from the device

1. In Graphics Analyzer, select `Debug` > `Device Manager`, then select your device from the list of detected devices.

1. Select the required APIs (OpenGL ES and/or Vulkan) for your application.
![Device Manager #center](images/ga_device_manager.png "Device Manager")

1. Click `Start capture` to connect to the device and install Graphics Analyzer daemon on the device.

1. Start the application on the device, and interact as desired. Graphics Analyzer will collect API calls from the device.

    * To collect `Frame Buffer` data, pause the application when you reach the frame of interest.

    * Click the `camera` icon to capture the frame buffer output.

    * You can also enable `Overdraw`, `Shader`, and/or `Fragment count` data to be captured. Click the `camera` icon to capture this data.

1. When you have captured enough data, click `Stop tracing`. Graphics Analyzer will stop collecting data, remove the daemon(s), and process the captured data.

## Analyze the capture

The captured data will be processed into a report that the user can manually examine. The frames are listed in the `Trace Outline` view. A full description of the capabilities is given in the [Graphics Analyzer User Guide](https://developer.arm.com/documentation/101545/latest/The-Graphics-Analyzer-interface).

Understanding the output of the report is key to the usefulness of Graphics Analyzer. This [video tutorial](https://developer.arm.com/Additional%20Resources/Video%20Tutorials/Arm%20Mali%20GPU%20Training%20-%20EP3-4) shows how to make use of the features of Graphics Analyzer.
