---
title: Environment Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview 
#TODO: Add intro on Distil

In this course, you will learn how to train and run inference using DistilBERT. You'll deploy the model on the Arm Corstone-320 FVP and optionally on a Raspberry Pi 5 for sentiment analysis.

## Environment Setup
Setup your development environment for TinyML by following the first 3 chapters of the [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm) Learning Path (LP).


If you just followed the LP above, you should already have your virtual environment activated. If not, activate it using: 

```console
source $HOME/executorch-venv/bin/activate
```
The prompt of your terminal now has `(executorch)` as a prefix to indicate the virtual environment is active.

Run the commands below to install the dependencies.

```bash
pip install transformers datasets torch
```
You are now ready to fine-tune the model


