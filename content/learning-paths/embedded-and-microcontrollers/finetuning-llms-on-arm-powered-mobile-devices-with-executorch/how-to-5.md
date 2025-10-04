---
title: Mobile Plartform for Fine Tuning Large Language Model 
weight: 6 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

##  Development environment
You will learn to build the ExecuTorch runtime for fine-tuning models using KleidiAI, create JNI libraries for an mobile application, and integrate these libraries into the application.

The first step is to set up a development environment with the necessary software:
- Python 3.10 or later
- Git
- Java 17 JDK
- Latest Version of Android Studio
- Android NDK

###### Installation of Android Studio and Android NDK
- Download and install the latest version of Android Studio
- Launch Android Studio and open the Settings dialog.
- Go to Languages & Frameworks > Android SDK.
- In the SDK Platforms tab, select Android 14.0 ("UpsideDownCake").
- Install the required version of Android NDK by first setting up the Android command line tools.

###### Install Java 17 JDK  
- Open the [Java SE 17 Archive Downloads](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) Downloads page in your browser.  
- Choose the appropriate version for your operating system.  
- Downloads are available for macOS and Linux.

###### Install Git and cmake

For macOS use [Homebrew](https://brew.sh/):

``` bash
brew install git cmake
```

For Linux, use the package manager for your distribution:

``` bash
sudo apt install git-all cmake
```

###### Install Python 3.10

For macOS:

``` bash
brew install python@3.10
```

For Linux:

``` bash
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install Python3.10 python3.10-venv
```


###### Setup the [Executorch](https://pytorch.org/executorch/stable/intro-overview.html) Environments  
For mobile device execution, [ExecuTorch](https://pytorch.org/executorch/stable/intro-overview.html) is required. It enables efficient on-device model deployment and execution

- Python virtual environment creation 

```bash
python3.10 -m venv executorch
source executorch/bin/activate
```

The prompt of your terminal has `executorch` as a prefix to indicate the virtual environment is active.

- Conda virtual environment creation 

Install Miniconda on your development machine by following the [Installing conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) instructions.

Once `conda` is installed, create the environment:

```bash
conda create -yn executorch python=3.10.0
conda activate executorch
```

###### Clone ExecuTorch and install the required dependencies

From within the conda environment, run the commands below to download the ExecuTorch repository and install the required packages:

- You need to download Executorch from this [GitHub repository](https://github.com/pytorch/executorch/tree/main)
- Download the executorch.aar file from [executorch.aar](https://ossci-android.s3.us-west-1.amazonaws.com/executorch/release/executorch-241002/executorch.aar )
- Add a libs folder in this path \executorch-main\executorch-main\examples\demo-apps\android\LlamaDemo\app\libs and add executorch.aar

``` bash
git submodule sync
git submodule update --init
./install_requirements.sh
./install_requirements.sh --pybind xnnpack
./examples/models/llama/install_requirements.sh
```

###### Mobile Device Setup
- Enable the mobile device in [Android Studio](https://support.google.com/android/community-guide/273205728/how-to-enable-developer-options-on-android-pixels-6-secret-android-tips?hl=en)
- On the Android phone, enable Developer Options
    - First, navigate to Settings > About Phone.
    - At the bottom, locate Build Number and tap it seven times. A message will appear confirming that you are now a developer.(if only it were that easy to become one XD)
    - Access Developer Options by navigating to Settings > System > Developer Options.
    - You will see a large number of options, I repeat: DO NOT TOUCH ANYTHING YOU DO NOT KNOW.
    - Enable USB Debugging to connect your mobile device to Android Studio.
