---
title: Set up the SmolVLA environment
description: Set up an Arm Linux environment with the pinned SmolVLA model and LeRobot source for ONNX export and validation.
weight: 2
layout: learningpathall
---

## Download the scripts

Download the scripts for this Learning Path by copying and pasting the following commands into your terminal:

```bash
mkdir -p scripts
cd scripts
base_url="https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/cross-platform/smolvla-onnx-conversion/scripts"
for f in check_assets.py compare_onnx_outputs.py export_onnx.py quantize_onnx_torchao.py setup.sh workspace.py; do
    wget -q "$base_url/$f"
done
cd ..
```

## Check the system requirements

You'll run the exported models on an Arm Linux CPU.

Review the processor, Python version, and available space on the system you'll use to run the project:

```bash
lscpu
python3 --version
df -h .
```
Install Git and Python 3.12 if they aren't already available on your system.

If `python3 -m venv` fails, install the venv module for your distribution. On
Ubuntu or Debian, run the following command:

```bash
sudo apt install python3.12-venv
```

## Create the environment

Run the setup script:

```bash
bash scripts/setup.sh
```

The script downloads model weights, clones the LeRobot source, and installs
PyTorch and other Python dependencies.

{{% notice Note %}}
The setup might take 30 minutes or more, depending on your network speed.
{{% /notice %}}

The script:

- Creates `work/venv`
- Checks out the pinned LeRobot source
- Installs the conversion and runtime dependencies
- Downloads the SmolVLA policy and its SmolVLM2 dependency
- Records the installed Python packages in `work/environment.freeze.txt` and the source and model revisions in `work/revisions.json`

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

The output is similar to:

```output
PASS: public policy, base model, LeRobot source, and environment are ready
```

## What you've accomplished and what's next

You've prepared an Arm Linux environment with the pinned SmolVLA checkpoint,
source, and Python dependencies.

Next, you'll export SmolVLA as an FP32 ONNX model and validate it with ONNX Runtime.
