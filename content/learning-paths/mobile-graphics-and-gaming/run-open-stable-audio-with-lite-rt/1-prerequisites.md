---
title: Create a development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this learning path, you will learn how to build and deploy a simple LLM-based chat app to an Android device using ONNX Runtime. You will learn how to build the ONNX Runtime and ONNX Runtime generate() API and how to run the Phi-3 model for the Android application.

Your first task is to prepare a development environment with the required software:

- Android Studio (latest version recommended)
- Android NDK (tested with - TODO)
- Python 3.10 or newer
- CMake (tested with - 3.28.1)


## Install Python 3.10

Download and install [Python version 3.10](https://www.python.org/downloads/release/python-3100/)

In order to eliminate dependencies issues, It is recommended that you use a virtual environment tool like conda  or virtualenv. In this guide, we will use virtualenv:

to test for mac 

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
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

## Install CMake

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


You can verify successful python installation and correct version is being used
```console
cmake --version
```

You can refer to [CMake install tutorial](/install-guides/cmake/) for troubleshooting instructions.


{{% notice Note %}}
The instructions were tested with version 3.28.1
{{% /notice %}}

## Install Android NDK

To run the model on Android, we need to install Android Native Development Kit (Android NDK).

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
wget https://dl.google.com/android/repository/android-ndk-r25b-linux.zip
unzip android-ndk-r25b-linux.zip
  {{< /tab >}}
  {{< tab header="MacOS">}}
brew install --cask android-studio temurin
  {{< /tab >}}
{{< /tabpane >}}

For easier access and execution of Android NDK tools, add these to the `PATH`

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
export $PATH=$PATH:<path-to-android-ndk-r25b-linux>

  {{< /tab >}}
  {{< tab header="MacOS">}}
nano ~/.zshrc
export PATH=$PATH:~/Library/Android/sdk/ndk/27.0.12077973/toolchains/llvm/prebuilt/darwin-x86_64/bin
export PATH=$PATH:~/Library/Android/sdk/cmdline-tools/latest/bin
source ~/.zshrc

  {{< /tab >}}
{{< /tabpane >}}



