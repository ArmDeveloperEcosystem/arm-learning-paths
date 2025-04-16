---
# User change
title: "RenderDoc for Arm GPUs"

weight: 9 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
RenderDoc for Arm GPUs is an Arm fork of the RenderDoc open-source graphics API debugger. The Arm release includes support for API features and extensions that are available on the latest Arm GPUs, but are not yet supported in upstream RenderDoc.

The primary purpose of RenderDoc is to help you diagnose rendering problems that occur in your application. When you have captured a frame you can use the tool to interactively explore all of its API calls and rendering events. By stepping through the frame you can identify the problematic rendering events, and then review the configuration used by the event to root cause the problem.

## Prerequisites

Build a debuggable version of your application, and setup your Android device as described in [Setup tasks](/learning-paths/smartphones-and-mobile/ams/setup_tasks/).

## Capture data from the device

1. Connect your Android device to your host machine using USB.
1. Select your connected Android device from the **Replay Context** dropdown list at the bottom left of the RenderDoc UI.

    ![Replay Context dropdown location in RenderDoc](images/rd_replay_context.png "Replay Context dropdown location in RenderDoc")

    If you do not see your target listed in the dropdown list, run adb devices in a command-line utility. The utility returns the ID and prompts RenderDoc to list the target. If it does not, see the setup tasks to check you have set up the target correctly.

    {{% notice %}}
    A red cross next to your target indicates that you have not run RenderDoc on this target before. When you connect for the first time, RenderDoc installs its capture and replay application on the target. Now the target is shown as connected in the dropdown list.
    {{% /notice %}}

    After connecting, the RenderDoc app starts running on your target.

1. Navigate to the Launch Application tab in RenderDoc for Arm® GPUs. Here:
    1. Set the Executable Path to the application you want to debug. Click the Browse button to view all the installed application packages on the target. Choose the required application package folder and select the activity executable within it.
    1. Optionally, you can specify the Working Directory. If you do not specify this, the capture is temporarily saved in the same location as the executable.
    1. You can also specify additional Capture Options and specify a list of frames to capture, in the Actions section.

1. Click Launch, to start the application running on your target. After a successful launch, a new target-specific tab opens in the UI and from here you can capture your frames. You can:
    1. Capture one or more frames immediately
    1. Capture one or more frames after a delay
    1. Capture one or more frames after a specific frame

    ![Capture frame controls](images/rd_capture_controls.png "Capture frame controls in RenderDoc")

    Captured frames are stored temporarily on the target.

1. When you have finished capturing the frames of interest, keep the application running on the target while you save the frames you want to debug. Click Save and then choose a location on your machine. Or you can click Open to view them directly without saving. When you click Save, RenderDoc disconnects from the target.

1. To stop the mobile application running, use the Android swipe control to close the application. Keep the RenderDoc application running though, so that you can analyze and debug your captures.

## Load a saved capture

You can either load a frame capture for analysis directly after capture, or you can load a previously saved frame capture.

1. Ensure that your Android target is connected to your computer, and select your target from the Replay Context dropdown list.

1. If you have just taken a new frame capture, select the capture from the Captures collected window and click Open. Alternatively, you can load a previously saved frame capture from the File > Open Capture menu.

    When the frame has loaded, it is displayed on the target and in the Texture Viewer tab, and the Event Browser is populated in RenderDoc for Arm GPUs.

## Analyze the capture



