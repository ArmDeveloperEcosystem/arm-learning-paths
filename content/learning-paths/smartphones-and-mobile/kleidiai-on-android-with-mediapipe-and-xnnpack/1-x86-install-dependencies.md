---
title: Install dependencies on an x86_64 Linux machine running Ubuntu
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install dependencies on an x86_64 Linux machine running Ubuntu

## Dependencies to install

In order to cross-compile your inference engine, you'll need the following installed/downloaded within your local development environment:

* Package Installer for Python (pip)
* JDK
* Bazel
* MediaPipe Github repo
* MediaPipe Python package requirements
* Android NDK v25, with configurations
* Android SDK
* OpenCV

### Install pip3

```bash
sudo apt install unzip python3-pip -y
```

### Install Java

```bash
sudo apt-get install openjdk-11-jdk -y
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$PATH:$JAVA_HOME
```

{{% notice Note %}}
If you want these environment variables to persist the next time you open a shell, add them to your [.bashrc](https://unix.stackexchange.com/questions/129143/what-is-the-purpose-of-bashrc-and-how-does-it-work) file or similar.
{{% /notice %}}

### Install Bazel

To build mediapipe, you will use Bazel version 6.1.1.

```bash
wget https://github.com/bazelbuild/bazel/releases/download/6.1.1/bazel-6.1.1-installer-linux-x86_64.sh

$ sudo bash bazel-6.1.1-installer-linux-x86_64.sh
```

### Clone the Mediapipe repo


```bash
git clone --depth 1 https://github.com/google/mediapipe.git

cd mediapipe
```

### Install MediaPipe python packages

```bash
pip3 install -r requirements.txt
```

### Install Android NDK and SDK

Bazel does not natively support newer versions of NDK, it supports up to r21. Use the script included in mediapipe to install Android NDK and SDK.

```bash
bash setup_android_sdk_and_ndk.sh
```

### Add android_ndk_repository() and android_sdk_repository() rules into the WORKSPACE file:

```bash
echo "android_sdk_repository(name = \"/home/ubuntu/Android/Sdk\")" >> WORKSPACE

echo "android_ndk_repository(name = \"/home/ubuntu/Android/Sdk/ndk-bundle/android-ndk-r21\", api_level=21)" >> WORKSPACE
```

### Add NDK bin folder to your PATH variable

```bash

export PATH=$PATH:/home/ubuntu/Android/Sdk/ndk-bundle/android-ndk-r21/toolchains/llvm/prebuilt/linux-x86_64/bin/

```

### Install OpenCV and its dependencies:

In the setup_opencv.sh script change libc1394-22-dev to libc1394-dev due to [libc1394-dev replacing libc1394-22-dev in Ubuntu 21.10.](https://github.com/ros/rosdistro/issues/34921)

Run ```bash setup_opencv.sh```

Verify your setup by running a simple hello world example in MediaPipe:

```bash
export GLOG_logtostderr=1

bazel run --define MEDIAPIPE_DISABLE_GPU=1 mediapipe/examples/desktop/hello_world:hello_world
```

Note: You need the bazel flag 'MEDIAPIPE_DISABLE_GPU=1' since desktop GPU is not currently supported.

The output from this test run will be ```Hello World!``` printed ten times, like this:

```output
INFO: Build completed successfully, 371 total actions
INFO: Running command line: bazel-bin/mediapipe/examples/desktop/hello_world/hello_world
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1715712039.171598 59236 hello_world.cc:58] Hello World!
I0000 00:00:1715712039.171651 59236 hello_world.cc:58] Hello World!
I0000 00:00:1715712039.171667 59236 hello_world.cc:58] Hello World!
I0000 00:00:1715712039.171679 59236 hello_world.cc:58] Hello World!
I0000 00:00:1715712039.171719 59236 hello_world.cc:58] Hello World!
I0000 00:00:1715712039.171754 59236 hello_world.cc:58] Hello World!
I0000 00:00:1715712039.171773 59236 hello_world.cc:58] Hello World!
I0000 00:00:1715712039.171804 59236 hello_world.cc:58] Hello World!
I0000 00:00:1715712039.171829 59236 hello_world.cc:58] Hello World!
I0000 00:00:1715712039.171859 59236 hello_world.cc:58] Hello World!
```


