---
title: Set up your development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this Learning Path, you will learn how to convert the Stable Audio Open Small model to ExecuTorch (.pte) format, then build an audio generation application to run on Android or macOS. ExecuTorch is a PyTorch framework designed for on-device inference on edge and mobile devices.

## Identify requirements

Before you begin, you need a development environment with the required software:

- An Android device with an Arm CPU supporting FEAT_DotProd (dotprod) and optionally FEAT_I8MM (i8mm), with at least 8 GB of RAM.
- Python 3.10 or newer.
- CMake version 3.16.0 or newer.
- Android NDK r27c (if building for Android).

## Create workspace directory

Create a workspace directory to manage the dependencies and repositories.

Export the `WORKSPACE` variable to point to this directory:

```bash
mkdir my-workspace
export WORKSPACE=$PWD/my-workspace
cd $WORKSPACE
```

## Install Python 3.10

Install Python 3.10 or newer for compatibility with the required packages:

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
sudo apt install -y python3.10 python3.10-venv
  {{< /tab >}}
  {{< tab header="macOS">}}
brew install python@3.10
brew link python@3.10 --force
  {{< /tab >}}
{{< /tabpane >}}

Verify the installation:

```console
python3 --version
```

The output is similar to:

```output
Python 3.10.19
```

## Install CMake

Install CMake to automate the build process for the audio generation application:

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
sudo apt update
sudo apt install cmake g++ git
  {{< /tab >}}
  {{< tab header="macOS">}}
brew install cmake
  {{< /tab >}}
{{< /tabpane >}}

Verify the installation:

```console
cmake --version
```

The output is similar to:

```output
cmake version 4.2.1
```

See the [CMake install guide](/install-guides/cmake/) for additional help.

## Clone the ML examples repository

Clone the Arm ML examples repository, which contains the scripts and application code:

```bash
cd $WORKSPACE
git clone https://github.com/Arm-Examples/ML-examples.git
cd ML-examples/kleidiai-examples/audiogen-et/
```

## What you've accomplished and what's next

Your development environment is ready with Python 3.10, CMake, and the ML examples repository. In the next section, you'll download the Stable Audio Open Small model from Hugging Face.
