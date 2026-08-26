---
title: Set up the SmolVLA environment
description: Create a Python environment and download the pinned SmolVLA model and LeRobot source.
weight: 2
layout: learningpathall
---

## Get the companion files

Clone the Arm Learning Paths repository and open this Learning Path directory:

```bash
git clone https://github.com/ArmDeveloperEcosystem/arm-learning-paths.git
cd arm-learning-paths/content/learning-paths/embedded-and-microcontrollers/smolvla-onnx-conversion
```

## Check the system requirements

This Learning Path runs the exported models on an Arm Linux CPU. Review the
processor, Python version, and available space on the filesystem where you will
keep the project:

```bash
lscpu
python3 --version
df -h .
```

Use Python 3.12 and confirm at least 50 GB of free storage. Install Git and
Python 3.12 if they are not already available on your system.

If `python3 -m venv` fails, install the venv module for your distribution. On
Ubuntu or Debian, run `sudo apt install python3.12-venv`.

## Create the environment

Run the setup script:

```bash
bash scripts/setup.sh
```

The script downloads model weights, clones the LeRobot source, and installs
PyTorch and other Python dependencies. It may take 30 minutes or more depending
on your network speed.

The script creates `work/venv`, checks out the pinned LeRobot source, installs
the conversion and runtime dependencies, and downloads the SmolVLA policy and
its SmolVLM2 dependency. It records the installed Python packages in
`work/environment.freeze.txt` and the source and model revisions in
`work/revisions.json`.

Activate the virtual environment so you can use `python` directly in later
commands:

```bash
source work/venv/bin/activate
```

## Verify the downloaded assets

Check the downloaded files and revisions:

```bash
python scripts/check_assets.py
```

The expected output ends with:

```output
PASS: public policy, base model, LeRobot source, and environment are ready
```

## What you've accomplished and what's next

You have prepared an Arm Linux environment with the pinned SmolVLA checkpoint,
source, and Python dependencies. Next, you will export SmolVLA as an FP32 ONNX
model and validate it with ONNX Runtime.
