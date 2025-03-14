---
title: Environment Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview 
In this course, you will learn how to train and run inference using a Tiny Sentiment Classifier. You'll deploy the model on the Arm Corstone-320 FVP for sentiment analysis. 

We will train a lightweight convolutional neural network (CNN)-based sentiment classifier using synthetic text data. This model is optimized for small devices, using embedding layers and 1D convolutions for efficient text classification.


## Environment Setup
Setup your development environment for TinyML by following the first 3 chapters of the [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm) Learning Path (LP).


If you just followed the LP above, you should already have your virtual environment activated. If not, activate it using: 

```console
source $HOME/executorch-venv/bin/activate
```
The prompt of your terminal now has `(executorch-venv)` as a prefix to indicate the virtual environment is active.

Run the commands below to install the dependencies.

```bash
pip install argparse json
```
You are now ready to build the model


