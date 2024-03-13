---
title: Capture a trace
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
1. Open Frame Advisor and select `New Trace`.

    ![Frame Advisor's launch screen alt-text#center](fa_launch_screen.png "Figure 1. Frame Advisor's launch screen")

1. Frame Advisor lists the connected devices and the applications installed. Select your device, and the application containing the frames that you want to capture.

    ![Frame Advisor's connection screen alt-text#center](fa_connect.png "Figure 1. Frame Advisor's connection screen")

1. If your application is Vulkan, change the selection in the API settings.

1. Click `Next` to start the capture session. The application starts automatically on the device.

    ![Frame Advisor's capture screen alt-text#center](fa_capture.png "Figure 1. Frame Advisor's capture screen")

1. Play the application until you find your problem area. Just before you reach the part of the application where you have a frame rate drop or where the device overheats, click `Pause`, or hit the space bar. You can use the step button to move forward frame by frame.

1. You can capture a frame burst of up to 3 consecutive frames. Here, we will capture one frame. Click the capture button, and Frame Advisor will capture the next frame.

    By default, we capture only the color attachment. Change the `Capture mode` to `All attachments` to also include any depth and stencil attachments, and any attachments from multiple render targets. Or you can capture the overdraw in the scene.

    When the capture completes, the frame is shown in the `Captured frames` list.

    Currently, you can only capture one frame burst of up to 3 frames. In future releases you will be able to continue the application and capture more frames.

1. Click `Analyze` to see the results. This might take a few minutes, depending on your content and how many frames you captured.
