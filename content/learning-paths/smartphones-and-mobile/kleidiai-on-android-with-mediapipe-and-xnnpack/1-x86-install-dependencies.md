---
title: Install dependencies 
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Option 1: Run a docker container with dependencies pre-installed

We have created a Dockerfile and built a Docker image that contains all the requirements for running this learning path. If you'd like to install the dependencies yourself, please jump to (Option 2: Install dependencies on an x86_64 Linux machine running Ubuntu)[##option-2-install-dependencies-on-an-x86-64-linux-machine-running-ubuntu].

#### Obtaining the pre-built image from Docker Hub

To get a pre-built image from Docker Hub, run:

TODO: add in docker hub path here.

```
docker pull
```

#### Build the image yourself

Save the following lines in a Dockerfile:

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

RUN sudo apt install unzip python3-pip -y 
RUN sudo apt-get install openjdk-11-jdk -y

ENV JAVA_HOME "/usr/lib/jvm/java-11-openjdk-amd64"
ENV PATH "$PATH:$JAVA_HOME"

RUN wget https://github.com/bazelbuild/bazel/releases/download/6.1.1/bazel-6.1.1-installer-linux-x86_64.sh
RUN sudo bash bazel-6.1.1-installer-linux-x86_64.sh

RUN git clone --depth 1 https://github.com/google/mediapipe.git

WORKDIR /home/$USER/mediapipe

RUN pip3 install -r requirements.txt
RUN bash setup_android_sdk_and_ndk.sh $HOME/Android/Sdk $HOME/Android/Sdk/ndk-bundle r21 --accept-licenses

ENV PATH "$PATH:$HOME/Android/Sdk/ndk-bundle/android-ndk-r21/toolchains/llvm/prebuilt/linux-x86_64/bin"

RUN sed -i 's/libdc1394-22-dev/libdc1394-dev/g' setup_opencv.sh
RUN sed -i 's/apt install/apt -y install/g' setup_opencv.sh
RUN bash setup_opencv.sh

ENV GLOG_logtostderr=1
```

Build the Docker image:

```
docker build -t ubuntu-x86 -f Dockerfile .
```

Run a shell on the Docker container:

```
docker run -it --rm ubuntu-x86 /bin/bash
```

You can now jump to (testing your setup)[##test-your-setup].

## Option 2: Install dependencies on an x86_64 Linux machine running Ubuntu

In order to cross-compile your inference engine, you'll need the following installed/downloaded within your local Ubuntu development environment:

* Package Installer for Python (pip)
* JDK
* Bazel
* MediaPipe Github repo
* MediaPipe Python package requirements
* Android NDK v25, with configurations
* Android SDK
* OpenCV

#### Install pip3

```bash
sudo apt install unzip python3-pip -y
```

#### Install Java

```bash
sudo apt-get install openjdk-11-jdk -y
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$PATH:$JAVA_HOME
```

{{% notice Note %}}
If you want these environment variables to persist the next time you open a shell, add them to your [.bashrc](https://unix.stackexchange.com/questions/129143/what-is-the-purpose-of-bashrc-and-how-does-it-work) file.
{{% /notice %}}

#### Install Bazel

To build MediaPipe, you will use Bazel version 6.1.1.

```bash
wget https://github.com/bazelbuild/bazel/releases/download/6.1.1/bazel-6.1.1-installer-linux-x86_64.sh
sudo bash bazel-6.1.1-installer-linux-x86_64.sh
```

#### Clone the MediaPipe repo


```bash
git clone --depth 1 https://github.com/google/mediapipe.git
cd mediapipe
```

#### Install MediaPipe python packages

```bash
pip3 install -r requirements.txt
```

#### Install and configure the Android NDK and SDK

Bazel only natively supports the Android NDK up to version 21. Use the script included in MediaPipe to install the Android NDK and SDK:

```bash
bash setup_android_sdk_and_ndk.sh $HOME/Android/Sdk $HOME/Android/Sdk/ndk-bundle r21 --accept-licenses
```

Add the NDK bin folder to your PATH variable:

```bash

export PATH=$PATH:$HOME/Android/Sdk/ndk-bundle/android-ndk-r21/toolchains/llvm/prebuilt/linux-x86_64/bin/

```

#### Install OpenCV and its dependencies

{{% notice Note %}}
In Ubuntu 21.10, [libc1394-dev replaced libc1394-22-dev.](https://github.com/ros/rosdistro/issues/34921)

Check your Ubuntu version using `lsb_release -a`, and if you're running 21.10 or later, change libc1394-22-dev to libc1394-dev in the setup_opencv.sh script.
{{% /notice %}}

To install opencv, run:

```
bash setup_opencv.sh
```

## Test your setup

Verify your setup by running a simple hello world example in MediaPipe:

```bash
export GLOG_logtostderr=1
bazel run --define MEDIAPIPE_DISABLE_GPU=1 mediapipe/examples/desktop/hello_world:hello_world
```

The bazel flag `MEDIAPIPE_DISABLE_GPU=1` disables the desktop GPU since it's not required.

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


