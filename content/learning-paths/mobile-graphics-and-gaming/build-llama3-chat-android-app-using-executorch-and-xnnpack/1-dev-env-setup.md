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
- Android NDK version 28.0.12433566.
- Java 17 JDK.
- Git.
- Python 3.10 or later (these instructions have been tested with 3.10 and 3.12).

The instructions assume macOS with Apple Silicon, an x86 Debian, or an Ubuntu Linux machine, with at least 16GB of RAM.

## Install Android Studio and Android NDK

Follow these steps to install and configure Android Studio:

1. Download and install the latest version of [Android Studio](https://developer.android.com/studio/).

2. Start Android Studio and open the **Settings** dialog.

3. Navigate to **Languages & Frameworks**, then **Android SDK**.

4. In the **SDK Platforms** tab, check **Android 14.0 ("UpsideDownCake")**.

Next, install the specific version of the Android NDK that you require by first installing the Android command line tools:

Linux:

```
curl https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -o commandlinetools.zip
```

macOS:

```
curl https://dl.google.com/android/repository/commandlinetools-mac-11076708_latest.zip -o commandlinetools.zip
```

Unzip the Android command line tools:

```
unzip commandlinetools.zip -d android-sdk
```

Install the NDK in the same directory that Android Studio installed the SDK. This is generally `~/Library/Android/sdk` by default. Set the requirement environment variables:

```
export ANDROID_HOME="$(realpath ~/Library/Android/sdk)"
export PATH=$ANDROID_HOME/cmdline-tools/bin/:$PATH
sdkmanager --sdk_root="${ANDROID_HOME}" --install "ndk;28.0.12433566"
export ANDROID_NDK=$ANDROID_HOME/ndk/28.0.12433566/
```

## Install Java 17 JDK

Open the [Java SE 17 Archive Downloads](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) page in your browser.

Select an appropriate download for your development machine operating system.

Downloads are available for macOS as well as Linux.

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
