---
title: Set up your development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Identify software requirements

In this Learning Path, you'll learn how to convert the Stable Audio Open Small model to the LiteRT (.tflite) format, then build a simple test program to generate audio on a mobile device.

Your first task is to prepare a development environment with the required software:

- Android NDK: version r27b or newer.
- Python: version 3.10 or newer (tested with 3.10).
- CMake: version 3.16.0 or newer (tested with 3.28.1).

### Create workspace directory

Create a separate directory for all the dependencies and repositories that this Learning Path uses.

Export the `WORKSPACE` variable to point to this directory, which you will use in the following steps:

```bash
mkdir my-workspace
export WORKSPACE=$PWD/my-workspace
```

### Install Python 3.10

Download and install [Python version 3.10](https://www.python.org/downloads/release/python-3100/) using the following commands:

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
sudo apt install -y python3.10 python3.10-venv
  {{< /tab >}}
  {{< tab header="macOS">}}
brew install python@3.10
brew link python@3.10 --force
  {{< /tab >}}
{{< /tabpane >}}

You can verify the installation and check the version with:

```console
python3.10 --version
```

### Install CMake

CMake is an open-source tool that automates the build process for software projects, helping to generate platform-specific build configurations.

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
sudo apt update
sudo apt install cmake g++ git
  {{< /tab >}}
  {{< tab header="macOS">}}
brew install cmake
  {{< /tab >}}
{{< /tabpane >}}

You can verify the installation and check the version with:

```console
cmake --version
```

See the [CMake install guide](/install-guides/cmake/) for troubleshooting instructions.

### Install Bazel

Bazel is an open-source build tool which you will use to build LiteRT libraries.

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
cd $WORKSPACE
export BAZEL_VERSION=7.4.1
wget https://github.com/bazelbuild/bazel/releases/download/{$BAZEL_VERSION}/bazel-{$BAZEL_VERSION}-installer-linux-x86_64.sh
sudo bash bazel-7.4.1-installer-linux-x86_64.sh
export PATH="/usr/local/bin:$PATH"
  {{< /tab >}}
  {{< tab header="macOS">}}
cd $WORKSPACE
export BAZEL_VERSION=7.4.1
curl -fLO "https://github.com/bazelbuild/bazel/releases/download/{$BAZEL_VERSION}/bazel-{$BAZEL_VERSION}-installer-darwin-arm64.sh"
sudo bash bazel-7.4.1-installer-darwin-arm64.sh
export PATH="/usr/local/bin:$PATH"
  {{< /tab >}}
{{< /tabpane >}}

You can verify the installation and check the version with:

```console
bazel --version
```

### Install Android SDK and NDK

To build a native Android application you will need to install the Android SDK:

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
cd $WORKSPACE
sudo apt install openjdk-21-jdk openjdk-21-jre unzip
wget https://dl.google.com/android/repository/commandlinetools-linux-13114758_latest.zip
unzip -o commandlinetools-linux-13114758_latest.zip
mkdir -p $WORKSPACE/Android/Sdk
export ANDROID_HOME=$WORKSPACE/Android
export ANDROID_SDK_HOME=$ANDROID_HOME/Sdk
$WORKSPACE/cmdline-tools/bin/sdkmanager --sdk_root=$ANDROID_SDK_HOME --install "platform-tools" "platforms;android-35" "build-tools;35.0.0"
  {{< /tab >}}
  {{< tab header="macOS">}}
cd $WORKSPACE
wget https://dl.google.com/android/repository/commandlinetools-mac-13114758_latest.zip
unzip -o commandlinetools-linux-13114758_latest.zip
mkdir -p $WORKSPACE/Android/Sdk
export ANDROID_HOME=$WORKSPACE/Android
export ANDROID_SDK_HOME=$ANDROID_HOME/Sdk
$WORKSPACE/cmdline-tools/bin/sdkmanager --sdk_root=$ANDROID_SDK_HOME --install "platform-tools" "platforms;android-35" "build-tools;35.0.0"
  {{< /tab >}}
{{< /tabpane >}}

To run the model on Android, install Android Native Development Kit (Android NDK):

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
cd $WORKSPACE
wget https://dl.google.com/android/repository/android-ndk-r27b-linux.zip
unzip android-ndk-r27b-linux.zip
  {{< /tab >}}
  {{< tab header="macOS">}}
cd $WORKSPACE
wget https://dl.google.com/android/repository/android-ndk-r27b-darwin.zip
unzip android-ndk-r27b-darwin.zip
  {{< /tab >}}
{{< /tabpane >}}

For easier access and execution of Android NDK tools, add these to the `PATH` and set the `NDK_PATH` variable:

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
export NDK_PATH=$WORKSPACE/android-ndk-r27b/
export ANDROID_NDK_HOME=$NDK_PATH
export PATH=$NDK_PATH/toolchains/llvm/prebuilt/linux-x86_64/bin/:$PATH
  {{< /tab >}}
  {{< tab header="macOS">}}
export NDK_PATH=$WORKSPACE/android-ndk-r27b/
export ANDROID_NDK_HOME=$NDK_PATH
export PATH=$NDK_PATH/toolchains/llvm/prebuilt/darwin-x86_64/bin/:$PATH
  {{< /tab >}}
{{< /tabpane >}}

Now that your development environment is ready and all the prerequisites are installed, you can move on to test the Stable Audio Open Small model.
