---
title: Connect an Arm-based Android device and run Scene Detector
description: Connect an Arm-based Android phone, prepare the Scene Detector repository, and verify that the application starts.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connect an Android phone

Enable **Developer options** and **USB debugging** on the phone. Connect it to your development computer with USB, unlock it, and accept the debugging authorization prompt.

Verify that your phone is listed in `adb`:

```console
adb devices -l
```

The output lists the authorized phone and its device serial. If the phone reports `unauthorized`, unlock it and accept the debugging prompt. If the phone doesn't appear, see [Run apps on a hardware device](https://developer.android.com/studio/run/device).

{{% notice Note %}}
On Linux, a phone that doesn't appear in `adb` might need Android `udev` rules and membership in the `plugdev` group. On Windows, you might need the phone manufacturer's USB driver. You don't normally need an additional USB driver on macOS.
{{% /notice %}}

## Clone the application repository

Clone the repository with Git, then enter the project directory:

```console
git clone https://github.com/arm-education/ai-portal-android-app-object-detection.git
cd ai-portal-android-app-object-detection
```

Run the remaining terminal commands from this project directory.

## Prepare the Arm AI Portal model downloader

The sample repository includes a downloader for its supported Arm AI Portal model packages.

Create a Python virtual environment and install the package used by the downloader:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
python3 -m venv .hf-venv
.hf-venv/bin/python -m pip install --upgrade pip huggingface_hub
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
python -m venv .hf-venv
.\.hf-venv\Scripts\python.exe -m pip install --upgrade pip huggingface_hub
  {{< /tab >}}
{{< /tabpane >}}

The later commands invoke the environment's Python executable directly, so PowerShell script-execution policy doesn't need to be changed.

If Python reports that `venv` is unavailable on Debian or Ubuntu, install the `python3-venv` package and rerun the command.

## Build and run the application

Use the Gradle wrapper to build and lint the debug APK. You don't need to install Gradle separately because the repository includes the wrapper.

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
chmod +x gradlew
./gradlew :app:assembleDebug :app:lintDebug
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat :app:assembleDebug :app:lintDebug
  {{< /tab >}}
{{< /tabpane >}}

The `chmod` command is needed only on macOS or Linux when the executable bit isn't already set.

Install the APK and start Scene Detector with the commands used on every operating system:

```console
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n org.arm.learningpath.objectdetection/.MainActivity
```

Scene Detector opens without a model. You can choose a saved image or open the live camera, but detection remains unavailable until you import a supported `.pte` file. 

![Scene Detector first-launch screen with ExecuTorch detection selected. The empty image area and Model setup needed message show that no model or image has been imported yet.#center](scene-detector-startup.png "Scene Detector before a model or image is added")

## What you've accomplished and what's next

You've connected an Arm-based Android phone, prepared the model downloader, and confirmed that Scene Detector builds and starts. 

Next, you'll download an optimized object-detection model from the Arm AI Portal and analyze an image.
