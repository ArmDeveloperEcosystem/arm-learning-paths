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

This Learning Path runs the exported models on an aarch64 Linux CPU. Review the
processor, Python version, and available space on the filesystem where you will
keep the project:

```bash
lscpu
python3 --version
df -h .
```

Use Python 3.12. Make sure the filesystem can hold the model data, checkpoint
weights, Python environment, and generated FP32 and INT4 ONNX models.

## Create the environment

Run the setup script:

```bash
bash scripts/setup.sh
```

The script creates `work/venv`, checks out the pinned LeRobot source, installs
the conversion and runtime dependencies, and downloads the SmolVLA policy and
its SmolVLM2 dependency. It records the installed Python packages in
`work/environment.freeze.txt` and the source and model revisions in
`work/revisions.json`.

## Verify the downloaded assets

Check the downloaded files and revisions:

```bash
work/venv/bin/python scripts/check_assets.py
```

The expected output ends with:

```output
PASS: public policy, base model, LeRobot source, and environment are ready
```

## What you've accomplished and what's next

You have prepared an Arm Linux environment with the pinned SmolVLA checkpoint,
source, and Python dependencies. Next, you will export SmolVLA as an FP32 ONNX
model and validate it with ONNX Runtime.
