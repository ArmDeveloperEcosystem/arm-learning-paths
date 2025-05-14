---
title: Create a development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this learning path, you will learn about Stable Audio Open models, how to convert these to LiteRT format (`.tflite`). You will then create and build a simple test program to generation audio on a mobile device.

Your first task is to prepare a development environment with the required software:

- Android NDK r25b or newer
- Python 3.10 or newer. This learning path has been tested with Python 3.10.
- CMake 3.16.0 or newer. This learning path has been tested with CMake 3.28.1.
- [Arm GNU Toolchain](/install-guides/gcc/arm-gnu)

## Create workspace directory

You will create a separate directory for all dependencies and repositories used in this learning path. Export the `WORKSPACE` variable to point to this directory, which is used in the next steps.

```bash
mkdir my-workspace
export WORKSPACE=$PWD/my-workspace
```

## Install Python 3.10

Download and install [Python version 3.10](https://www.python.org/downloads/release/python-3100/)

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

You can verify successful python installation and correct version is being used

```console
python3.10 --version
```

### Install CMake

CMake is an open-source tool that automates the build process for software projects, helping to generate platform-specific build configurations.

```bash
sudo apt update
sudo apt install cmake
```

You can verify successful python installation and correct version is being used
```console
cmake --version
```

You can refer to the[CMake install guide](/install-guides/cmake/) for troubleshooting instructions.

```bash
sudo apt update
sudo apt install python3-venv python3-pip g++ unzip protobuf-compiler -y
```

## Install Bazel

Bazel is an open-source build tool which we will use to build LiteRT libraries.

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
cd $WORKSPACE
wget https://github.com/bazelbuild/bazel/releases/download/6.1.1/bazel-7.4.1-installer-linux-x86_64.sh
sudo bash bazel-7.4.1-installer-linux-x86_64.sh
  {{< /tab >}}
  {{< tab header="MacOS">}}
brew install bazel
  {{< /tab >}}
{{< /tabpane >}}

### Install Android NDK

To run the model on Android, we need to install Android Native Development Kit (Android NDK).

```bash
cd $WORKSPACE
wget https://dl.google.com/android/repository/android-ndk-r25b-linux.zip
unzip android-ndk-r25b-linux.zip
```

We also set `ANDROID_NDK` variable to allow easier access to Android SDK tools in further steps.
For easier access and execution of Android NDK tools, add the prebuild toolchains to the `PATH`.

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
export ANDROID_NDK=$WORKSPACE/android-ndk-r25b/
export PATH=$ANDROID_NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/:$PATH
  {{< /tab >}}
  {{< tab header="MacOS">}}
nano ~/.zshrc
export ANDROID_NDK=~/Library/Android/sdk/ndk/27.0.12077973/
export PATH=$PATH:$ANDROID_NDK/toolchains/llvm/prebuilt/darwin-x86_64/bin
export PATH=$PATH:~/Library/Android/sdk/cmdline-tools/latest/bin
source ~/.zshrc
  {{< /tab >}}
{{< /tabpane >}}

Now that your development environment is ready and all pre-requisites installed, you can test the Audio Stable Open model.
