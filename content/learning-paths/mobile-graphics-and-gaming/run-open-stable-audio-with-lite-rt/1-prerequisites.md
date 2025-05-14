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

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
```

You can verify the installation and check the version with:

```console
python3.10 --version
```

To avoid dependency issues, it's recommended to use a virtual environment. For example, you can use Python’s built-in `venv`:

```bash
python3.10 -m venv litert-venv
source litert-venv/bin/activate
```

### Install CMake

CMake is an open-source tool that automates the build process for software projects, helping to generate platform-specific build configurations.

```bash
sudo apt update
sudo apt install cmake
```

You can verify the installation and check the version with:

```console
cmake --version
```

See the [CMake install guide](/install-guides/cmake/) for troubleshooting instructions.

### Install other dependencies

These packages include essential tools for Python environments, C++ compilation, file handling, and model conversion support:

```bash
sudo apt update
sudo apt install python3-venv python3-pip g++ unzip protobuf-compiler -y
```

### Install Android NDK

To run the model on Android, install Android Native Development Kit (Android NDK):

```bash
cd $WORKSPACE
wget https://dl.google.com/android/repository/android-ndk-r25b-linux.zip
unzip android-ndk-r25b-linux.zip
```

For easier access and execution of Android NDK tools, add these to the `PATH`:

```bash
export PATH=$WORKSPACE/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/bin/:$PATH
export ANDROID_NDK=$WORKSPACE/android-ndk-r25b/
```


