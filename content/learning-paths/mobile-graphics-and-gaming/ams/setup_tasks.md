---
# User change
title: Set up an Android application

description: Prepare a debuggable Android application and device connection so Arm Performance Studio can capture profiling data.

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Before you begin

Complete the following prerequisites:

1. Install [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb). `adb` is available with the Android SDK platform tools, which are installed as part of Android Studio. Alternatively, you can download them separately as part of the Android SDK platform tools.
2. Performance Advisor uses a Python script to connect to your device. To run this script, you'll need [Python](https://www.python.org/downloads/) 3.8 or later installed.

## Build your application

Compile the application with debug enabled, as well as additional options to facilitate call stack unwinding by Streamline.

- To set [Unity](https://unity.com/) applications to be debuggable, enable **[Development Build](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)** in **Build settings**.
- In Android Studio, use a build variant that includes `debuggable true` (`isDebuggable = true` in Kotlin scripts) in the build configuration.
- In Unreal Engine, open **Project Settings > Project > Packaging > Project**, and ensure that the **For Distribution** checkbox is not set.
- For instructions to compile your C++ or Java applications with the right options, see the [Target setup guide for Android](https://developer.arm.com/documentation/101813/latest/Target-Setup/Compile-your-application).

{{% notice Tip %}}
To assist with readability and add context, you can optionally include [annotations](https://developer.arm.com/documentation/101816/latest/Annotate-your-code/Add-annotations-to-your-code) in your code, which are then displayed in Streamline.
{{% /notice %}}

## Set up the Android device

To set up your Android device, follow these steps:

1. On the device, ensure that **[Developer Mode](https://developer.android.com/studio/debug/dev-options)** is enabled.
2. Enable **USB Debugging** under **Settings > Developer options**. If your device asks you to authorize connection to your computer, confirm the connection.
3. Connect the device to the host through USB and approve the debug connection on the device when prompted.
4. To test the connection, run the `adb devices` command in a terminal. If successful, this returns the ID of your device:

    ```command
    adb devices
    List of devices attached
    ce12345abcdf1a1234       device
    ```

    If you see that the device is listed as `unauthorized`, try disabling and re-enabling `USB Debugging` on the device, and accept the authorization prompt to enable connection to the computer.

5. Install the [debuggable](https://developer.android.com/studio/debug) application on the device.

## What you've accomplished and what's next

You've now set up your Android device and built the application you'll use for profiling.

Next, you'll look at an example Arm Streamline report to understand the Streamline component of Arm Performance Studio.
