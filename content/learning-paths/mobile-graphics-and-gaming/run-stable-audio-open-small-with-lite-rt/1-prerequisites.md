---
title: Set up your development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Identify software requirements

In this Learning Path, you'll learn how to convert the Stable Audio Open Small model to the LiteRT (.tflite) format, then build a simple test program to generate audio on a mobile device.

Your first task is to prepare a development environment with the required software:

- Android NDK: version r25b or newer.
- Python: version 3.10 or newer (tested with 3.10).
- CMake: version 3.16.0 or newer (tested with 3.28.1).
- [Arm GNU Toolchain](/install-guides/gcc/arm-gnu).

### Create workspace directory

Create a separate directory for all dependencies and repositories that this Learning Path uses.

Export the `WORKSPACE` variable to point to this directory, which you will use in the following steps:

```bash
mkdir my-workspace
export WORKSPACE=$PWD/my-workspace
```

### Install Python 3.10

Download and install [Python version 3.10](https://www.python.org/downloads/release/python-3100/) using the following commands:

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-pip
  {{< /tab >}}
  {{< tab header="MacOS">}}
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
sudo apt install cmake
  {{< /tab >}}
  {{< tab header="MacOS">}}
brew install cmake
  {{< /tab >}}
{{< /tabpane >}}

You can verify the installation and check the version with:

```console
cmake --version
```

See the [CMake install guide](/install-guides/cmake/) for troubleshooting instructions.

### Install Bazel

Bazel is an open-source build tool which we will use to build LiteRT libraries.

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
cd $WORKSPACE
wget https://github.com/bazelbuild/bazel/releases/download/7.4.1/bazel-7.4.1-installer-linux-x86_64.sh
sudo bash bazel-7.4.1-installer-linux-x86_64.sh
  {{< /tab >}}
  {{< tab header="MacOS">}}
brew install bazel@7
  {{< /tab >}}
{{< /tabpane >}}

### Install Android NDK

To run the model on Android, install Android Native Development Kit (Android NDK):

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
cd $WORKSPACE
wget https://dl.google.com/android/repository/android-ndk-r25b-linux.zip
unzip android-ndk-r25b-linux.zip
  {{< /tab >}}
  {{< tab header="MacOS">}}
brew install --cask android-studio temurin
  {{< /tab >}}
{{< /tabpane >}}

For easier access and execution of Android NDK tools, add these to the `PATH` and set the `ANDROID_NDK` variable:

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
export ANDROID_NDK=$WORKSPACE/android-ndk-r25b/
export PATH=$ANDROID_NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/:$PATH
  {{< /tab >}}
  {{< tab header="MacOS">}}
export ANDROID_NDK=~/Library/Android/sdk/ndk/27.0.12077973/
export PATH=$PATH:$ANDROID_NDK/toolchains/llvm/prebuilt/darwin-x86_64/bin
export PATH=$PATH:~/Library/Android/sdk/cmdline-tools/latest/bin
  {{< /tab >}}
{{< /tabpane >}}

Now that your development environment is ready and all pre-requisites installed, you can test the Audio Stable Open model.
