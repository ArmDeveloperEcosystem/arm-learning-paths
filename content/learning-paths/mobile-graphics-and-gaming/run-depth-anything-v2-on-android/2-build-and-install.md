---
title: Connect an Arm-based Android phone and build Image Analysis
description: Connect an Arm-based Android phone, prepare the Image Analysis repository, and install the debug application.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connect an Android phone

Enable **Developer options** and **USB debugging** on the Arm-based Android phone. Connect it with a data-capable USB cable, unlock it, and accept the debugging authorization prompt.

Verify the connection and architecture:

```console
adb devices -l
adb shell getprop ro.product.cpu.abi
```

The first command lists the phone as `device`. The second command returns `arm64-v8a`.

If the phone is `unauthorized`, unlock it and accept the prompt. On Windows, you might also need the manufacturer's USB driver.

## Clone the application repository

Clone Image Analysis, which contains the validated Depth Anything V2 adapter, then enter the project directory:

```console
git clone https://github.com/arm-education/ai-portal-android-app-image-to-image.git
cd ai-portal-android-app-image-to-image
```

Run the remaining terminal commands from this project directory.

The repository contains Kotlin adapters and placeholder files, but it doesn't contain model weights or credentials.

## Prepare the Arm AI Portal model downloader

Create a Python virtual environment and install the package used to download models from Hugging Face:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
python3 -m venv .hf-venv
.hf-venv/bin/python -m pip install --upgrade pip huggingface_hub
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
py -m venv .hf-venv
.\.hf-venv\Scripts\python.exe -m pip install --upgrade pip huggingface_hub
  {{< /tab >}}
{{< /tabpane >}}

The commands invoke the virtual environment's Python executable directly, so you don't need to activate the environment or change the PowerShell script-execution policy. If Python reports that `venv` is unavailable on Debian or Ubuntu, install the `python3-venv` package and rerun the command.

## Build and install Image Analysis

Before building, confirm the Gradle JVM configuration:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
chmod +x gradlew
./gradlew --version
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat --version
  {{< /tab >}}
{{< /tabpane >}}

The `Launcher JVM` entry should report JDK 17 or later. The `Daemon JVM` entry should report that Java 17 is configured by `gradle/gradle-daemon-jvm.properties`. Gradle downloads a compatible JDK 17 automatically when one isn't already available.

Build the debug APK, then run the unit tests and lint checks:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
./gradlew :app:testDebugUnitTest :app:assembleDebug :app:lintDebug
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebug :app:lintDebug
  {{< /tab >}}
{{< /tabpane >}}

You don't need to install Gradle separately because the repository includes the Gradle wrapper.

After Gradle reports `BUILD SUCCESSFUL`, install the APK and start Image Analysis:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n com.arm.learningpath.imagetoimage/.ui.MainActivity
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
adb install -r app\build\outputs\apk\debug\app-debug.apk
adb shell am start -n com.arm.learningpath.imagetoimage/.ui.MainActivity
  {{< /tab >}}
{{< /tabpane >}}

Select **Depth Anything V2 Small INT8** in the model menu. Its status reports `placeholder bundled` because the real `.pte` file hasn't been copied to the phone.

## What you've accomplished and what's next

You've built, tested, and installed the application with its model-specific Depth Anything adapter. Next, you'll download and stage the exact model artifact.
