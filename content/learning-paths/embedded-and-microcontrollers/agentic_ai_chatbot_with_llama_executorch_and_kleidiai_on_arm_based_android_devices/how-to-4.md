---
title: Environment Setup
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Android NDK and Android Studio -  Environment Setup

#### Plartform Required 
- An AWS Graviton4 r8g.16xlarge instance to test Arm performance optimizations, or any [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server or Arm based laptop.
- An Arm-powered smartphone with the i8mm feature running Android, with 16GB of RAM.
- A USB cable to connect your smartphone to your development machine.

The installation and configuration of Android Studio can be accomplished through the following steps:
1. Download and install the latest version of [Android Studio](https://developer.android.com/studio).
2. Launch Android Studio and access the Settings dialog.
3. Navigate to Languages & Frameworks → Android SDK.
4. Under the SDK Platforms tab, ensure that Android 14.0 (“UpsideDownCake”) is selected.

Next, proceed to install the required version of the Android NDK by first setting up the Android Command Line Tools.
Linux:
```bash
curl https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -o commandlinetools.zip
unzip commandlinetools.zip
./commandlinetools/bin/sdkmanager --install "ndk;26.1.10909697"
```
Install the NDK in the same directory where Android Studio has installed the SDK, which is typically located at ~/Library/Android/sdk by default. Then, configure the necessary environment variables as follows:  
```bash
export ANDROID_HOME="$(realpath ~/Library/Android/sdk)"
export PATH=$ANDROID_HOME/cmdline-tools/bin/:$PATH
sdkmanager --sdk_root="${ANDROID_HOME}" --install "ndk;28.0.12433566"
export ANDROID_NDK=$ANDROID_HOME/ndk/28.0.12433566/
```

#### Install Java 17 JDK
1. Open the Java SE 17 Archive [Downloads](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) page in your browser.
2. Select an appropriate download for your development machine operating system.

#### Install Git and cmake
```bash
sudo apt-get install git cmake
```

#### Install Python 3.10
```bash
sudo apt-get install python3.10
```

#### Set up ExecuTorch
ExecuTorch is an end-to-end framework designed to facilitate on-device inference across a wide range of mobile and edge platforms, including wearables, embedded systems, and microcontrollers. As a component of the PyTorch Edge ecosystem, it streamlines the efficient deployment of PyTorch models on edge devices. For further details, refer to the [ExecuTorch Overview](https://pytorch.org/executorch/stable/overview/).

It is recommended to create an isolated Python environment to install the ExecuTorch dependencies. Instructions are available for setting up either a Python virtual environment or a Conda virtual environment—you only need to choose one of these options.

##### Install Required Tools ( Python environment setup)
```python
python3 -m venv exec_env
source exec_env/bin/activate
pip install torch torchvision torchaudio
pip install executorch
```
##### Clone Required Repositories 
```bash
git clone https://github.com/pytorch/executorch.git
git clone https://github.com/pytorch/text.git
```
##### Download Pretrained Model (Llama 3.1 Instruct)
Download the quantized model weights optimized for mobile deployment from either the Meta AI Hub or Hugging Face.
```
git lfs install
git clone https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
```

##### Verify Arm SDK Path
```
ANDROID_SDK_ROOT=/Users/<you>/Library/Android/sdk
ANDROID_NDK_HOME=$ANDROID_SDK_ROOT/ndk/26.1.10909125
```