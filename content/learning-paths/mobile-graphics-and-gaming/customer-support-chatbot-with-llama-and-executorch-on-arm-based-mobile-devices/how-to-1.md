---
title: Create a development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this Learning Path, you will build and deploy an on-device customer support chatbot to an Android smartphone using ExecuTorch and XNNPACK with [KleidiAI](https://gitlab.arm.com/kleidi/kleidiai). Arm has worked with the Meta team to integrate KleidiAI into ExecuTorch through XNNPACK. These optimizations increase the throughput of quantized LLMs running on Arm chips with the i8mm (8-bit integer matrix multiply) feature. Running the chatbot entirely on-device means no cloud dependency, lower latency, and greater privacy for your users.

The first step is to prepare a development environment with the required software:

- Android Studio (latest version recommended).
- Android NDK version 29.0.14206865 or later.
- Java 17 JDK.
- Git.
- Python 3.10 or later (these instructions have been tested with 3.10 and 3.12).

The instructions assume macOS with Apple Silicon, or a Debian or Ubuntu Linux machine, with at least 16GB of RAM.

## Install Java 17 JDK

Open the [Java SE 17 Archive Downloads](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) page in your browser.

Select an appropriate download for your development machine operating system. Downloads are available for macOS as well as Linux.

## Install and configure Android Studio

Download and install the latest version of Android Studio from the Downloads page:

```
https://developer.android.com/studio/
```

### For macOS: Using the UI

Configure Android Studio:

- Start Android Studio and open the **Settings** dialog
- Navigate to **Languages & Frameworks**, then **Android SDK**
- In the **SDK Platforms** tab, check **Android 14.0 ("UpsideDownCake")**. Select **Apply** to install
- In the **SDK Tools** tab, check **NDK (Side by side)**. Select **Apply** to install

Set the `ANDROID_HOME` environment variable:

```bash
export ANDROID_HOME="$(realpath ~/Library/Android/sdk)"
```

### For Linux: Using the CLI

Command-line tools let you manage Android SDK components without the GUI. Create the SDK directory and download the command-line tools:

```bash
mkdir -p ~/Android/cmdline-tools
cd ~/Android/cmdline-tools
wget https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip
```

Unzip and move the directory:

```bash
unzip commandlinetools-linux-*.zip
mv cmdline-tools latest
```

Set the `ANDROID_HOME` environment variable and add `sdkmanager` to `PATH`:

```bash
export ANDROID_HOME="~/Android"
export PATH="$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH"
```

Accept the license agreements. Press `y`, then **Enter**, as many times as prompted.

```bash
sdkmanager --licenses
```

Install the required Android SDK components:

```bash
sdkmanager "platform-tools" \
           "platforms;android-34" \
           "build-tools;34.0.0" \
           "ndk;29.0.14206865"
```

## Verify NDK installation

Verify that the NDK was installed in the same directory where Android Studio installed the SDK.

{{% notice Default Path %}}
On macOS, this is generally `~/Library/Android/sdk`, and on Linux, it's `~/Android/Sdk`. Update the command to use your installed NDK version.
{{% /notice %}}

## What you've learned and what's next

You have set up a complete Android development environment with:
- Android Studio configured with the required SDK and NDK
- Environment variables set for Android development
- All necessary build tools installed

In the next section, you will set up ExecuTorch, the runtime that enables efficient on-device inference for PyTorch models on mobile platforms.
