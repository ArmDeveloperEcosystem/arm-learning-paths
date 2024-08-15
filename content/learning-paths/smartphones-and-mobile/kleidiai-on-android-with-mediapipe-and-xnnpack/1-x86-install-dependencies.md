---
title: Install dependencies 
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install dependencies

There are two options outlined in this Learning Path to install the dependencies. Click on the option of your choice:

  * [Option 1: Build a Docker container with the dependencies](#option-1-build-a-docker-container-with-the-dependencies).
  * [Option 2: Install dependencies on an x86_64 Linux machine running Ubuntu](#option-2-install-dependencies-on-an-x86_64-linux-machine-running-ubuntu).

#### Option 1: Build a Docker container with the dependencies
Install [docker engine](/install-guides/docker/docker-engine) on your machine.

Use a file editor of your choice and save the following lines in a file named `Dockerfile`:

```
FROM amd64/ubuntu:22.04 

ENV USER=ubuntu 

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update 
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y upgrade
RUN apt-get -y --no-install-recommends install sudo vim wget curl jq git bzip2 make cmake automake autoconf libtool pkg-config clang-format

RUN useradd --create-home -s /bin/bash -m $USER && echo "$USER:$USER" | chpasswd && adduser $USER sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /home/$USER
USER ubuntu

RUN sudo apt-get install unzip python3-pip -y
RUN sudo apt-get install openjdk-11-jdk -y

ENV JAVA_HOME "/usr/lib/jvm/java-11-openjdk-amd64"
ENV PATH "$PATH:$JAVA_HOME"

RUN wget https://github.com/bazelbuild/bazel/releases/download/6.1.1/bazel-6.1.1-installer-linux-x86_64.sh
RUN sudo bash bazel-6.1.1-installer-linux-x86_64.sh

RUN git clone --depth 1 https://github.com/google/mediapipe.git

WORKDIR /home/$USER/mediapipe

RUN pip3 install -r requirements.txt
RUN bash setup_android_sdk_and_ndk.sh $HOME/Android/Sdk $HOME/Android/Sdk/ndk-bundle r26d --accept-licenses

ENV PATH "$PATH:$HOME/Android/Sdk/ndk-bundle/android-ndk-r26d/toolchains/llvm/prebuilt/linux-x86_64/bin"

ENV GLOG_logtostderr=1
```

Build the Docker image:

```
docker build -t ubuntu-x86 -f Dockerfile . --platform=linux/amd64
```

Run a shell on the Docker container:

```
docker run -it --rm ubuntu-x86 /bin/bash
```

You can now jump to [testing your setup](#test-your-setup).

#### Option 2: Install dependencies on an x86_64 Linux machine running Ubuntu

In order to cross-compile the inference engine, you will need the following packages installed or downloaded on your Ubuntu development machine:

* Package Installer for Python (pip).
* JDK.
* Bazel.
* MediaPipe GitHub repository.
* MediaPipe Python package requirements.
* Android NDK v25, with configurations.
* Android SDK.

#### Install pip3

```bash
sudo apt update
sudo apt install unzip python3-pip -y
```

#### Install Java

```bash
sudo apt-get install openjdk-11-jdk -y
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$PATH:$JAVA_HOME
```

{{% notice Note %}}
If you would like these environment variables to persist the next time you open a shell, add them to your [.bashrc](https://unix.stackexchange.com/questions/129143/what-is-the-purpose-of-bashrc-and-how-does-it-work) file.
{{% /notice %}}

#### Install Bazel

To build MediaPipe, you will use Bazel version 6.1.1.

```bash
wget https://github.com/bazelbuild/bazel/releases/download/6.1.1/bazel-6.1.1-installer-linux-x86_64.sh
sudo bash bazel-6.1.1-installer-linux-x86_64.sh
```

#### Clone the MediaPipe repository


```bash
git clone --depth 1 https://github.com/google/mediapipe.git
cd mediapipe
```

{{% notice Note %}}
These steps have been tested with MediaPipe commit 7c625938d8074b77e6cefcc29beabd995c613e2b.
{{% /notice %}}

#### Install MediaPipe python packages

```bash
pip3 install -r requirements.txt
```

#### Install and configure the Android NDK and SDK

Use the script included in MediaPipe to install the Android NDK and SDK:

```bash
bash setup_android_sdk_and_ndk.sh $HOME/Android/Sdk $HOME/Android/Sdk/ndk-bundle r26d --accept-licenses
```

Add the NDK bin folder to your PATH variable:

```bash

export PATH=$PATH:$HOME/Android/Sdk/ndk-bundle/android-ndk-r26d/toolchains/llvm/prebuilt/linux-x86_64/bin/

```

## Test your setup

Verify your setup by running a simple "hello world" example in MediaPipe:

```bash
export GLOG_logtostderr=1
bazel run --define MEDIAPIPE_DISABLE_GPU=1 mediapipe/examples/desktop/hello_world:hello_world
```

The bazel flag `MEDIAPIPE_DISABLE_GPU=1` disables the desktop GPU as it is not required.

The output from this test run is ```Hello World!``` printed ten times, like this:

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


