---
title: Create a development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this Learning Path, you will learn how to build and deploy a simple LLM-based chat app to an Android device using ExecuTorch and XNNPACK with [KleidiAI](https://gitlab.arm.com/kleidi/kleidiai). Arm has worked with the Meta team to integrate KleidiAI into ExecuTorch through XNNPACK. These improvements increase the throughput of quantized LLMs running on Arm chips that contain the i8mm (8-bit integer matrix multiply) processor feature. You will learn how to build the ExecuTorch runtime for Llama models with KleidiAI, build JNI libraries for the Android application, and use the libraries in the application.

The first step is to prepare a development environment with the required software:

- Android Studio (latest version recommended).
- Android NDK version 28.0.12433566 or later.
- Java 17 JDK.
- Git.
- Python 3.10 or later (these instructions have been tested with 3.10 and 3.12).

The instructions assume macOS with Apple Silicon, an x86 Debian, or an Ubuntu Linux machine, with at least 16GB of RAM.

## Install Java 17 JDK

Open the [Java SE 17 Archive Downloads](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) page in your browser.

Select an appropriate download for your development machine operating system.

Downloads are available for macOS as well as Linux. 

## Install and configure Android Studio

Start by downloading and installing the latest version of Android Studio by navigating to the Downloads page:

```
https://developer.android.com/studio/
```

### For macOS: Using UI

Follow these steps to configure Android Studio:

1. Start Android Studio and open the **Settings** dialog.

2. Navigate to **Languages & Frameworks**, then **Android SDK**.

3. In the **SDK Platforms** tab, check **Android 14.0 ("UpsideDownCake")**. Click **Apply** to install. 

4. In the **SDK Tools** tab, check **NDK (Side by side)**. Click **Apply** to install.

Initiate the `ANDROID_HOME` environment variable:

```bash
export ANDROID_HOME="$(realpath ~/Library/Android/sdk)"
```

### For Linux: Using the CLI

Command-line tools allow you to manage Android SDK components without the GUI. Create SDK directory and download command-line tools:

```bash
mkdir -p ~/Android/cmdline-tools
cd ~/Android/cmdline-tools
wget https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip
```

Unzip and move into the `cmdline-tools` directory.

```bash
unzip commandlinetools-linux-*.zip
mv cmdline-tools latest
```

Initiate the `ANDROID_HOME` environment variable and add the `sdkmanager` to `PATH`:

```bash
export ANDROID_HOME="~/Android"
export PATH="$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH"
```

The next step is to accept the license agreements. Press 'y', then 'Enter', as many times as prompted.

```bash
sdkmanager --licenses
```

Finally, you can install the required Android SDK components:

```bash
sdkmanager "platform-tools" \
           "platforms;android-34" \
           "build-tools;34.0.0" \
           "ndk;29.0.14206865"
```

## Verify NDK installation 

Verify by checking that the NDK was installed in the same directory that Android Studio installed the SDK. 

{{% notice Default Path %}}
On macOS, this is generally `~/Library/Android/sdk`, and on Linux, it's `~/Android/Sdk`. You should also update the command to use the installed NDK version.
{{% /notice %}}

```bash
ls $ANDROID_HOME
```

It should print the installed version, for example:

```output
29.0.14206865
```

Set the required environment variable:

```
export ANDROID_NDK="$ANDROID_HOME/ndk/29.0.14206865/"
```

## Install Git and cmake

For macOS use [Homebrew](https://brew.sh/):

``` bash
brew install git cmake
```

For Linux, use the package manager for your distribution:

``` bash
sudo apt install git-all cmake
```

## Install Python 3.10

For macOS:

``` bash
brew install python@3.10
```

For Linux:

``` bash
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install Python3.10 python3.10-venv
```

You now have the required development tools installed.
