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
- Python 3.10 or newer. This learning path has been tested with Python 3.10
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

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
```

You can verify successful python installation and correct version is being used

```console
python3.10 --version
```

In order to eliminate dependencies issues, it is recommended that you use a virtual environment tool like conda or virtualenv. For example, you can use this command:

```bash
python3.10 -m venv litert-venv
source litert-venv/bin/activate
```

## Install CMake

CMake is an open-source tool that automates the build process for software projects, helping to generate platform-specific build configurations.

```bash
sudo apt update
sudo apt install cmake
```

You can verify successful python installation and correct version is being used
```console
cmake --version
```

You can refer to the [CMake install guide](/install-guides/cmake/) for troubleshooting instructions.

## Install other dependencies

```bash
sudo apt update
sudo apt install python3-venv python3-pip g++ unzip protobuf-compiler -y
```

## Install Android NDK

To run the model on Android, we need to install Android Native Development Kit (Android NDK).

```bash
cd $WORKSPACE
wget https://dl.google.com/android/repository/android-ndk-r25b-linux.zip
unzip android-ndk-r25b-linux.zip
```

For easier access and execution of Android NDK tools, add these to the `PATH`

```bash
export PATH=$WORKSPACE/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/bin/:$PATH
export ANDROID_NDK=$WORKSPACE/android-ndk-r25b/
```


