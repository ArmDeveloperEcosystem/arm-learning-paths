---
title: Use RenderDoc with NFRU for debugging and analysis
description: Capture a packaged NFRU application with RenderDoc for Arm GPUs and inspect Vulkan events, resources, and pipeline stages for debugging.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why use RenderDoc with NFRU

When you integrate neural upscaling into your game, you need visual debugging and performance profiling. RenderDoc is a frame capture and analysis tool that you can use to review frames, Vulkan API calls, shader inputs and outputs, and GPU resource states. 

Arm provides additional features for RenderDoc in [RenderDoc for Arm GPUs](https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs).

Use RenderDoc to:

- Investigate unexpected visual output or step through the rendering process
- Analyze the sequence of Vulkan API calls your engine makes
- Inspect memory usage or GPU resource states
- Validate your data graph pipeline or identify synchronization issues

## Install Arm Performance Studio

Download Arm Performance Studio from the [Arm Performance Studio Downloads](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio#Downloads) page. For NFRU, use version `2025.6` or later.

For setup instructions, see the [Arm Performance Studio install guide](/install-guides/ams).

After installation, you'll find RenderDoc for Arm GPUs in the Windows **Start** menu.

## Build a Windows package in Unreal Engine

To prepare your Unreal Engine project for profiling:

1. Open your Unreal Engine project.
2. Select **Platforms > Windows > Package Project**.
3. Choose an output directory for the packaged build.
4. Wait for packaging to complete.

Your packaged build is ready for profiling with RenderDoc.

## Launch the packaged build from RenderDoc

To profile your build:

1. Open RenderDoc for Arm GPUs.
2. Select **Launch Application**.
3. Enter the full path to your packaged `.exe` in the **Executable Path** field.
4. (Optional) Add command-line arguments in the **Command-line Arguments** field.
5. Set the **Working Directory** to your packaged build folder if needed.
6. Click **Launch**.

![RenderDoc for Arm GPUs Launch Application tab showing the NFRU_Sample executable and working directory, with the Launch button highlighted#center](./images/renderdoc_launch.png "Launch the packaged NFRU application from RenderDoc")

Your application launches under RenderDoc. You can now capture frames and analyze GPU activity.

## Capture a frame in RenderDoc

To capture a frame:

1. With your application running, return to the RenderDoc window.
2. Select the **Capture Frame Immediately** button (camera icon) or press `F12` while your game window is focused.

The captured frame appears in RenderDoc.

![RenderDoc for Arm GPUs interface showing the capture frame button and a running application. This demonstrates how to capture a frame during execution#center](./images/renderdoc_capture.png "Capture a frame from the running NFRU application")

You can now analyze the rendering pipeline, inspect Vulkan API calls, and debug visual output at each stage.

## Analyze the event list

After capturing a frame, use the RenderDoc event browser to review the sequence of Vulkan API calls and draw events. Select individual events to inspect their details, view associated resources, and debug specific pipeline stages.

![RenderDoc event browser displaying a list of Vulkan API calls and draw events. This helps you trace rendering operations and debug pipeline stages#center](./images/renderdoc_event.png "Inspect NFRU rendering events in RenderDoc")

With RenderDoc, you can:

- Step through draw calls and dispatches
- Inspect bound resources, descriptor sets, and shaders
- Explore your data graph pipeline execution frame by frame

For more information, see the [Debug With RenderDoc User Guide](https://developer.arm.com/documentation/109669/latest).

## What you've accomplished

You've now learned how to set up and use RenderDoc for debugging your game. You've completed a full workflow for NFRU in Unreal Engine.

You can integrate neural frame generation into Unreal Engine, optimize it for your hardware, and debug your rendering pipeline.
