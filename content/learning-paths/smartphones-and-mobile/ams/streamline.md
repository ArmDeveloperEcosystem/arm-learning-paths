---
# User change
title: "Streamline with your application"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Now that you have seen an example Streamline capture, you can use it with your own application.

## Build your application

The application must be compiled with debug enabled, as well as additional options to facilitate call stack unwinding by Streamline.

The [Target setup guide for Android](https://developer.arm.com/documentation/101813/latest/Target-Setup/Compile-your-application) provides appropriate instructions for C++ or Java applications.

These settings are enabled as default within [Unity](https://unity.com/) when [Development Build](https://docs.unity3d.com/2021.1/Documentation/Manual/UnityCloudBuildDevelopmentBuilds.html) is selected in `Build settings`.

You can optionally provide [annotations](https://developer.arm.com/documentation/101816/latest/Annotate-your-code/Add-annotations-to-your-code) to your code which will be displayed in the Streamline report, to assist readability of the report.

### Open-source projects

Arm provides open-source projects that can be used by application developers as part of their development.

* [Unity Integration](https://github.com/ARM-software/mobile-studio-integration-for-unity/)
* [Arm ASTC Encoder texture compressor](https://github.com/ARM-software/astc-encoder)
* [libGPUInfo library](https://github.com/ARM-software/libGPUInfo)

## Set up Android device

Ensure that [Developer Mode](https://developer.android.com/studio/debug/dev-options) is enabled, then enable `USB Debugging` under `Settings > Developer options`.

Connect the device to the host through USB and approve the debug connection when prompted.

If the connection is successful, running the `adb devices` command on the host returns the ID of your device, and you can run `adb shell`.

Install the [debuggable](https://developer.android.com/studio/debug) application.

## Connect to the device

In the Streamline `Start` view, select `Android (adb)` as your device type, then select your device from the list of detected devices.

This will install the `gatord` daemon and connect to the device.

Wait for the list of available packages to populate, then select the one you wish to profile from the list of available packages on the selected device.

Select an appropriate [counter template](https://developer.arm.com/documentation/101813/latest/Debuggable-application-profiling/Profile-your-application/Choose-a-counter-template) for the GPU present in your device.

## Set location to store data (optional)

Navigate to `Window` > `Preferences` > `Data Locations`, and configure location to store data. New reports will be created in the topmost folder specified.

## Profile application

Click on `Start capture` to start capturing profile data from the target.

Start the application on the device., and interact as desired for the profiling run you wish to do.

When satisfied, simply click on `Stop capture`. Streamline will stop capturing data, remove the daemon, and process the captured data.

Doublie-click on the capture to display in the timeline.
