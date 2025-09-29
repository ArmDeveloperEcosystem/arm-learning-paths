---
title: Environment Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
This learning path (LP) is a direct follow-up to the [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm) learning path. While the previous one introduced you to the core concepts and the toolchain, this one puts that knowledge into practice with a fun, real-world example. You will move from the simple [Feedforward Neural Network](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/4-build-model) in the previous LP, to a more practical computer vision task: A tiny Rock-Paper-Scissors game, to demonstrate how these tools can be used to solve a tangible problem and run efficiently on Arm-based edge devices.

You will train a lightweight CNN to classify images of the letters R, P, and S as "rock," "paper," or "scissors." The script uses a synthetic data renderer to create a large dataset of these images with various transformations and noise, eliminating the need for a massive real-world dataset.

### What is a Convolutional Neural Network (CNN)?
A Convolutional Neural Network (CNN) is a type of deep neural network primarily used for analyzing visual imagery. Unlike traditional neural networks, CNNs are designed to process pixel data by using a mathematical operation called **convolution**. This allows them to automatically and adaptively learn spatial hierarchies of features from input images, from low-level features like edges and textures to high-level features like shapes and objects.

A convolutional neural network (CNN) is a deep neural network designed to analyze visual data using the **convolution** operation. CNNs learn spatial hierarchies of features - from edges and textures to shapes and objects - directly from pixels.

CNNs are the backbone of many modern computer vision applications, including:

- **Image Classification:** Identifying the main object in an image, like classifying a photo as a "cat" or "dog".
- **Object Detection:** Locating specific objects within an image and drawing a box around them.
- **Facial Recognition:** Identifying and verifying individuals based on their faces.

For the Rock-Paper-Scissors game, you'll use a tiny CNN to classify images of the letters R, P, and S as the corresponding hand gestures.



## Environment Setup
To get started, follow the first three chapters of the [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm) Learning Path. This will set up your development environment and install the necessary tools. Return to this LP once you've run the `./examples/arm/run.sh` script in the ExecuTorch repository.

If you just followed the LP above, you should already have your virtual environment activated. If not, activate it using:

```console
source $HOME/executorch-venv/bin/activate
```
The prompt of your terminal now has `(executorch-venv)` as a prefix to indicate the virtual environment is active.

Run the commands below to install the dependencies.

```bash
pip install argparse numpy pillow torch
```
You are now ready to create the model.

