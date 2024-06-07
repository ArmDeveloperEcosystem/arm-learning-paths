---
title: Create a development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this Learning Path, you will learn how to build and deploy a simple LLM-based chat app to an Android device using ExecuTorch and XNNPACK. You will learn how to build the ExecuTorch runtime for Llama models, build JNI libraries for the Android application, and use the libraries in the application.

The first step is to prepare a development environment with the required software:

- Android Studio (latest version recommended).
- Android NDK version 25.0.8775105.
- Java 17 JDK.
- Git.
- Python 3.10.

The instructions assume macOS with Apple Silicon, an x86 Debian, or Ubuntu Linux machine with at least 16GB of RAM.

## Install Android Studio and Android NDK

Follow these steps to install and configure Android Studio:

1. Download and install the latest version of [Android Studio](https://developer.android.com/studio/). 

2. Start Android Studio and open the `Settings` dialog.

3. Navigate to `Languages & Frameworks -> Android SDK`.

4. In the `SDK Platforms` tab, check `Android 14.0 ("UpsideDownCake")`.

Next, install the specific version of the Android NDK that you need by first installing the Android command line tools:

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
unzip commandlinetools.zip
```

Install the NDK in the directory that Android Studio installed the SDK. This is generally `~/Library/Android/sdk` by default:

```
export ANDROID_HOME="$(realpath ~/Library/Android/sdk)"
./cmdline-tools/bin/sdkmanager --sdk_root="${ANDROID_HOME}" --install "ndk;25.0.8775105"
```

## Install Java 17 JDK

Open the [Java SE 17 Archive Downloads](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) page in your browser.

Select an appropriate download for your development machine operating system. 

Downloads are available for macOS as well as Linux.

## Install Git

For macOS use [Homebrew](https://brew.sh/):
  
``` bash
brew install git
```

For Linux, use the package manager for your distribution:
  
``` bash
sudo apt install git-all
```

## Install Python 3.10

For macOS:
  
``` bash
brew install python@3.10
```

For Linux:
  
``` bash
sudo apt update
udo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install Python3.10
```

You now have the required development tools installed.
