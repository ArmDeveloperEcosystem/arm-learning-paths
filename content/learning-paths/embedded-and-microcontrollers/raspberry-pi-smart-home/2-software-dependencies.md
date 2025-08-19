---
title: Set up software dependencies on Raspberry Pi 5 for Ollama and LLMs
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you’ll prepare your Raspberry Pi 5 by installing Python, required libraries, and Ollama, so you can run large language models (LLMs) locally.

{{% notice Note %}}
This guide assumes you have set up your Raspberry Pi with Raspberry Pi OS and network connectivity. For Raspberry Pi 5 setup help, see: [Raspberry Pi Getting Started](https://www.raspberrypi.com/documentation/)
{{% /notice %}}

## Connect to your Raspberry Pi 5

### Option 1: Use a display

The easiest way to work on your Raspberry Pi is by connecting it to an external display through one of the micro‑HDMI ports. This setup also requires a keyboard and mouse.

### Option 2: Use SSH

You can also use SSH to access the terminal. To use this approach, you need to know the IP address of your device. Ensure your Raspberry Pi 5 is on the same network as your host computer. Access your device remotely via SSH using the terminal or any SSH client.

Replace `<user>` with your Pi's username (typically `pi`), and `<pi-ip>` with your Raspberry Pi 5's IP address.

```bash
ssh <user>@<pi-ip>
```

## Install Python and system dependencies

Create a directory called `smart-home` in your home directory and navigate into it:

```bash
mkdir -p "$HOME/smart-home"
cd "$HOME/smart-home"
```

The Raspberry Pi 5 includes Python 3 preinstalled, but you need additional packages:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv git curl build-essential gcc python3-lgpio
```

### Configure a virtual environment

Create and activate a Python virtual environment to isolate project dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required libraries:

```bash
pip install ollama gpiozero lgpio psutil httpx orjson numpy fastapi uvicorn uvloop
```

## Install Ollama

Install Ollama using the official installation script for Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify the installation:

```bash
ollama --version
```

If installation was successful, the output should be similar to:

```output
ollama version is 0.11.4
```

## Run a test LLM with Ollama on Raspberry Pi 5

Ollama supports various models. This guide uses `deepseek-r1:7b` as an example, but you can also use `tinyllama:1.1b`, `qwen:0.5b`, `gemma2:2b`, or `deepseek-coder:1.3b`.

The `run` command sets up the model automatically. You will see download progress in the terminal, followed by an interactive prompt when ready.

```bash
ollama run deepseek-r1:7b
```

{{% notice Troubleshooting %}}
If you run into issues with the model download, try the following:

- Confirm internet access and sufficient storage space on your microSD card.
- Try smaller models like `qwen:0.5b` or `tinyllama:1.1b` if you encounter memory issues. 16 GB of RAM is sufficient for small to medium models; very large models may require more memory or run slower.
- Clear storage or connect to a more stable network if errors occur.
{{% /notice %}}

With the model set up through Ollama, move on to the next section to start configuring the hardware.
