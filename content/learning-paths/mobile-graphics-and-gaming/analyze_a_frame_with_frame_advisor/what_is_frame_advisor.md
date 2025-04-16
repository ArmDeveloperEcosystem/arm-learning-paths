---
title: What is Frame Advisor?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

[Frame Advisor](https://developer.arm.com/Tools%20and%20Software/Frame%20Advisor) provides fast frame analysis for mobile graphics in Android applications. In this learning path, you will learn how to capture frame data from an Android application and explore how a frame was built. You will also get content metrics about the objects in the scene to help you identify and optimize expensive meshes. Frame Advisor is available to use for free as part of the [Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio) (formerly known as Arm Mobile Studio) suite of profiling tools.

To see Frame Advisor in action, [watch this video](https://developer.arm.com/Additional%20Resources/Video%20Tutorials/Capture%20and%20analyze%20a%20problem%20frame%20with%20Frame%20Advisor)

## Before you begin

1. [Download the Arm Performance Studio package](https://developer.arm.com/downloads/view/MOBST-PRO0) from the Arm Developer website. You’ll need to log in with an Arm account to access the downloads. If you don’t already have one, you can create one easily for free.

    Arm Performance Studio is available for Windows, Linux, and macOS platforms. See this [Install Guide](/install-guides/ams) for installation instructions.

1. Frame Advisor uses [Android Debug bridge (adb)](https://developer.android.com/studio/command-line/adb) to capture data from your device, so you’ll need to install [Android SDK Platform tools](https://developer.android.com/studio/releases/platform-tools.html), and add the path to ADB to your `PATH` environment variable.

1. Install a debuggable version of your application on the device.

1. You’ll need to put your device into developer mode, and enable USB Debugging.

1. Ensure your device is connected via USB and accessible through ADB. To test the connection, open a command prompt, and enter the `adb devices` command.
