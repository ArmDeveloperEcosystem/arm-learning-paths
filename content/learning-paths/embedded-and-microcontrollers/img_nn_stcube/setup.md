---
# User change
title: Prepare environment

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this Learning Path, you will build a convolution neural network model for image classification. You will train the model with CIFAR-10 dataset, one of the most popular image datasets, which contains 60,000 images with 10 different categories. The model takes an RGB image and predicts the category of the image.

## Set up Anaconda

Anaconda is a Python distribution for data science and machine learning. With Anaconda, you can easily install open-source machine learning packages.

1. Visit the [Anaconda website](https://www.anaconda.com/) and download the installer

2. Run the installer with the default options

With Anaconda installed, you can install the necessary `conda` packages for data collection and machine learning, including [Jupyter notebook](https://jupyter.org/).

Follow the steps as shown below:

1. First open Anaconda Prompt

2. Create an environment by typing:

```console
conda create -n ml_lab python=3.8
```
3. Activate your environment by typing:

```console
conda activate ml_lab
```
4. Add conda-forge channel to install packages:

```console
conda config --add channels conda-forge
```
5. Then install python packages:

```console
conda install jupyter pandas tensorflow matplotlib numpy 
```
6. Users have reported issues where the steps below result in `dead kernel` errors. To fix the problem, [described as a GitHub issue](https://github.com/dmlc/xgboost/issues/1715), use:

```console
conda install nomkl
```

## Get project files

Setup your development machine with the project files.

1. Download the [zip file](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/img_nn_stcube/Project_Files/img_class_stcube.zip) containing the project files

2. Unzip the files into a working folder

## Open Jupyter Notebook

In the same environment you activated using Anaconda earlier, navigate to the above folder and enter:
```console
jupyter notebook lab.ipynb
```
You are now ready to train your first neural network model with TensorFlow and deploy the inference with STM Cube AI.