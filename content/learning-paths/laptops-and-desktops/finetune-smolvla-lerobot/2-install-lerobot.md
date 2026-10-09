---
title: Install LeRobot and prepare a Python environment
description: Prepare and verify a LeRobot environment for SO-101 data collection and SmolVLA fine-tuning.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the software environment

The tested workflow uses LeRobot v0.6.0, Python 3.12.3, and PyTorch 2.11.0 with CUDA 12.8.

Check that `git`, `ffmpeg`, and `uv` are installed:

```bash
git --version
ffmpeg -version
uv --version
```

If one of these tools is missing, follow the [LeRobot installation documentation](https://huggingface.co/docs/lerobot/installation).

## Create an isolated environment

Clone the official LeRobot repository and check out the tested revision, then create a virtual environment:

```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot
git checkout 30da8e687a6dfc617fcd94afc367ac7071c376ce

uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -e ".[core_scripts,training,feetech,smolvla]"
```

The extras install the robot command-line tools, training dependencies, Feetech motor support, and SmolVLA dependencies.

## Verify LeRobot and CUDA

Print the core versions and confirm that PyTorch can see CUDA:

```bash
python -c "import platform, torch; from importlib.metadata import version; print({'python': platform.python_version(), 'lerobot': version('lerobot'), 'torch': torch.__version__, 'cuda': torch.cuda.is_available()})"
```

The output from the DGX Spark is similar to:

```output
{'python': '3.12.3', 'lerobot': '0.6.0', 'torch': '2.11.0+cu128', 'cuda': True}
```

Verify the commands that you'll use later:

```bash
for cli in lerobot-calibrate lerobot-find-cameras lerobot-find-port \
           lerobot-record lerobot-rollout lerobot-teleoperate lerobot-train; do
    command -v "$cli" > /dev/null || exit 1
done
```

The loop exits without output when all commands are available.

## Authenticate with Hugging Face

Sign in to Hugging Face interactively:

```bash
hf auth login
hf auth whoami
```

Follow the browser or terminal prompt to complete authentication.

## What you've accomplished and what's next

You now have a Python environment with CUDA, LeRobot's SO-101 tools, and SmolVLA dependencies. Keep this terminal active. 

Next, you'll connect the two arms and cameras to the DGX Spark and identify their device paths.
