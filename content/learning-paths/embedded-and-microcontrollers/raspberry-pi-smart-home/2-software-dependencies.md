---
title: Set up software dependencies
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

{{% notice Note %}}
This guide assumes you have set up your Raspberry Pi with Raspberry Pi OS and network connectivity. For Raspberry Pi 5 setup help, see: [Raspberry Pi Getting Started](https://www.raspberrypi.com/documentation/)
{{% /notice %}}

## Connect to Your Raspberry Pi 5

### Option 1: Using a display

The easiest way to work on your Raspberry Pi is connecting it to an external display through one of the micro HDMI ports. This setup also requires a keyboard and mouse to navigate.

### Option 2: Using SSH

You can also use SSH to access the terminal. To use this approach you need to know the IP address of your device. Ensure your Raspberry Pi 5 connects to the same network as your host computer. Access your device remotely via SSH using the terminal or any SSH client.

Replace `<user>` with your Pi's username (typically `pi`), and `<pi-ip>` with your Raspberry Pi 5's IP address.

```bash
ssh <user>@<pi-ip>
```

## Set up the dependencies

Create a directory called `smart-home` in your home directory and navigate into it:

```bash
mkdir $HOME/smart-home
cd $HOME/smart-home
```

The Raspberry Pi 5 includes Python 3 pre-installed, but you need additional packages:

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip python3-venv git curl build-essential gcc python3-lgpio
```

### Configure the virtual environment

The next step is to create and activate a Python virtual environment. This approach keeps project dependencies isolated and prevents conflicts with system-wide packages:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install all required libraries and dependencies:

```bash
pip install ollama gpiozero lgpio psutil httpx orjson numpy fastapi uvicorn uvloop numpy
```

### Install Ollama

Install Ollama using the official installation script for Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify the installation:

```bash
ollama --version
```
If installation was successful, the output from the command should match that below.
```output
ollama version is 0.11.4
```

## Download and Test a Language Model

Ollama supports various models. This guide uses deepseek-r1:7b as an example, but you can also use `tinyllama:1.1b`, `qwen:0.5b`, `gemma2:2b`, or `deepseek-coder:1.3b`.

The `run` command will set up the model automatically. You will see download progress in the terminal, followed by the interactive prompt when ready.

```bash
ollama run deepseek-r1:7b
```

{{% notice Troubleshooting %}}
If you run into issues with the model download, here are some things to check:

- Confirm internet access and sufficient storage space on your microSD card
- Try downloading smaller models like `qwen:0.5b` or `tinyllama:1.1b` if you encounter memory issues. 16 GB of RAM is sufficient for running smaller to medium-sized language models. Very large models may require more memory or run slower.
- Clear storage or connect to a more stable network if errors occur
{{% /notice %}}

With the model set up through `ollama`, move on to the next section to start configuring the hardware.