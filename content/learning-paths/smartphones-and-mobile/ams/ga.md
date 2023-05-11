---
# User change
title: "Graphics Analyzer"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Graphics Analyzer is a tool to help `OpenGL ES` and `Vulkan` developers get the best out of their applications through analysis at the API level.

The tool allows you to observe API call arguments and return values, and interact with a running target application to investigate the effect of individual API calls. It highlights attempted misuse of the API, and gives recommendations for improvements.

## Prerequisites

Build your application, and setup Android device as per Streamline instructions.

## Connect to the device

In the Graphics Analyzer menu, select `Debug` > `Device Manager`, and select your device from the list of detected devices.

Select the required APIs (OpenGL ES and/or Vulkan) for your application.

## Profile application

Click `Start capture` to connect to the device and install Graphics Analyzer daemon on the device.

Start the application on the device., and interact as desired for the profiling run you wish to do.

When satisfied, simply click on `Stop tracing`. Graphics Analyzer will stop collecting data, remove the daemon(s), and process the captured data.

## Analyze the capture

The captured data will be processed into a report that the user can manually examine. The frames are listed in the `Trace Outline` view. A full description of the capabilities is given in the [Graphics Analyzer User Guide](https://developer.arm.com/documentation/101545/latest/The-Graphics-Analyzer-interface).

Understanding the output of the report is key to the usefulness of Graphics Analyzer. This brief [video tutorial](https://www.youtube.com/watch?v=6j68rtcTYRc) shows how to make use of the features of Graphics Analyzer.
