---
title: Build and install the image-segmentation application on an Arm-based Android phone
description: Connect an Arm-based Android phone, prepare the MobileSAM model downloader, and build and install the example application.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connect an Android phone

Enable **Developer options** and **USB debugging** on the phone. Connect the phone with a data-capable USB cable, unlock it, and accept the debugging authorization prompt.

Verify the connection:

```console
adb devices -l
```

The output lists the authorized phone and its device serial. If the output reports `unauthorized`, unlock the phone and accept the debugging prompt. Windows might also need the phone manufacturer's USB driver. If the phone doesn't appear, see [Run apps on a hardware device](https://developer.android.com/studio/run/device).

## Prepare the application and model downloader

Clone the example application, then create the Python environment used to download MobileSAM:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
mkdir -p "$HOME/image-to-image-android"
cd "$HOME/image-to-image-android"
git clone https://github.com/arm-education/ai-portal-android-app-image-to-image.git
cd ai-portal-android-app-image-to-image

python3 -m venv .hf-venv
.hf-venv/bin/python -m pip install --upgrade pip huggingface_hub
.hf-venv/bin/hf auth login
.hf-venv/bin/hf auth whoami
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$IMAGE_MODEL_WORKSPACE = Join-Path $env:USERPROFILE "image-to-image-android"
New-Item -ItemType Directory -Force -Path $IMAGE_MODEL_WORKSPACE | Out-Null
Set-Location $IMAGE_MODEL_WORKSPACE
git clone https://github.com/arm-education/ai-portal-android-app-image-to-image.git
Set-Location ai-portal-android-app-image-to-image

python -m venv .hf-venv
.\.hf-venv\Scripts\python.exe -m pip install --upgrade pip huggingface_hub
.\.hf-venv\Scripts\hf.exe auth login
.\.hf-venv\Scripts\hf.exe auth whoami
  {{< /tab >}}
{{< /tabpane >}}

Sign in with an account that has access to the Arm model repository and use a read token when prompted.

## Build and install the application

Build and lint the debug APK, install it, and start the main activity:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
chmod +x gradlew
./gradlew :app:assembleDebug :app:lintDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n com.arm.learningpath.imagetoimage/.ui.MainActivity
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
.\gradlew.bat :app:assembleDebug :app:lintDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n com.arm.learningpath.imagetoimage/.ui.MainActivity
  {{< /tab >}}
{{< /tabpane >}}

The application opens with MobileSAM selected. Its status reports `(placeholder bundled)` because you haven't copied the real Hugging Face model into application-private storage yet.

## What you've accomplished and what's next

You've connected an Arm-based Android phone, prepared the application and model downloader, and installed the debug APK. 

Next, you'll run the MobileSAM model on the phone.
