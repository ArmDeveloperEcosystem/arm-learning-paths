---
# User change
title: Prepare development environment

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this Learning Path, you will build a neural network model with TensorFlow and deploy the model on the [STM32 B-L475E-IOT01A2 board](https://www.st.com/en/evaluation-tools/b-l475e-iot01a.html). This board has an MCU based on the [Arm Cortex-M4](https://developer.arm.com/Processors/Cortex-M4) processor.

You will implement a letter recognition model which takes accelerometer data from the board and predicts the letter based on the accelerometer data. 

## Set up Anaconda

Anaconda is a distribution of Python language for data science and machine learning. With Anaconda, you can easily install open-source machine learning packages.

1. Visit the official [Anaconda](https://www.anaconda.com/) page.
2. Download the Anaconda Installer, and install using default options.

With Anaconda installed, you will now install the necessary `conda` packages for data collection and machine learning including [Jupyter notebook](https://jupyter.org/).

Follow the steps as shown below:

1. Open `Anaconda Prompt`
2. Create an environment with:
```console
conda create -n ml_lab python=3.8
```
3. Activate your environment with:
```console
conda activate ml_lab
```
4. Add `conda-forge` channel to install packages:
```console
conda config --add channels conda-forge
```
5. Then install necessary python packages:
```console
conda install jupyter pandas pyserial scikit-learn tensorflow matplotlib
```
## Set up development board

Next, you need to program the STM32 `B-L475E-IOT01A2` board to acquire accelerometer data for your neural network model.

The data collection code for this Learning Path is provided, so you can just import the project and program the board using [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html).

Download the [zip file](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/Project_Files/tf_stm32.zip) and extract it into a `tf_stm32` folder.

### Install STM32CubeIDE

Download and run the installer from the `Get Software` section of the [STMicroelectronics website](https://www.st.com/en/development-tools/stm32cubeide.html).

### Program the board 

Within `STM32CubeIDE` follow the steps below:

1. Select `Import project` and navigate to `General` > `Existing Projects into Workspace`.
2. Select the `MCU Dataset Creation` folder from the unzipped package as the root directory, and select `Dataset_Creation` project. Click `Finish` to import.
2. Connect board to host computer via USB. You may need to reset your board before you program the board. Click the black button on the board for the reset.
3. Right click the project and select `Run As`. The project will rebuild, and be flashed to the device. If prompted, accept any suggested firmware updates.

## Open Jupyter Notebook

In the same environment you activated using Anaconda earlier, navigate to your `tf_stm32` folder and enter:
```console
jupyter notebook tf_stm32.ipynb
```
You are now ready to train your first neural network model with TensorFlow and deploy the inference with STM Cube AI. 
