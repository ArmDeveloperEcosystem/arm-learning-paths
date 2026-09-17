---
title: Build and install Arm AI Portal Image Analysis
description: Clone Arm AI Portal Image Analysis, prepare the model downloader, and install the debug application on an Arm-based phone.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clone Arm AI Portal Image Analysis

Clone Arm AI Portal Image Analysis, which contains the validated Depth Anything V2 adapter:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
mkdir -p "$HOME/depth-anything-android"
cd "$HOME/depth-anything-android"
git clone https://github.com/arm-education/ai-portal-android-app-image-to-image.git
cd ai-portal-android-app-image-to-image

python3 -m venv .hf-venv
.hf-venv/bin/python -m pip install --upgrade pip huggingface_hub
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$DEPTH_WORKSPACE = Join-Path $env:USERPROFILE "depth-anything-android"
New-Item -ItemType Directory -Force -Path $DEPTH_WORKSPACE | Out-Null
Set-Location $DEPTH_WORKSPACE
git clone https://github.com/arm-education/ai-portal-android-app-image-to-image.git
Set-Location ai-portal-android-app-image-to-image

py -m venv .hf-venv
.\.hf-venv\Scripts\python.exe -m pip install --upgrade pip huggingface_hub
  {{< /tab >}}
{{< /tabpane >}}

The commands invoke the virtual environment's Python executable directly, so you don't need to activate the environment or change the PowerShell script-execution policy. If Python reports that `venv` is unavailable on Debian or Ubuntu, install the `python3-venv` package and rerun the command.

The repository contains Kotlin adapters and placeholder files, but it doesn't contain model weights or credentials.

## Build and install Arm AI Portal Image Analysis

Build the debug APK, run the unit tests and lint checks, install the application, and start it:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
chmod +x gradlew
./gradlew :app:testDebugUnitTest :app:assembleDebug :app:lintDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n com.arm.learningpath.imagetoimage/.ui.MainActivity
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebug :app:lintDebug
adb install -r app\build\outputs\apk\debug\app-debug.apk
adb shell am start -n com.arm.learningpath.imagetoimage/.ui.MainActivity
  {{< /tab >}}
{{< /tabpane >}}

You don't need to install Gradle separately because the repository includes the Gradle wrapper.

Select **Depth Anything V2 Small INT8** in the model menu. Its status reports `placeholder bundled` because the real `.pte` file hasn't been copied to the phone.

## What you've accomplished and what's next

You've built, tested, and installed the application with its model-specific Depth Anything adapter. Next, you'll download and stage the exact model artifact.
