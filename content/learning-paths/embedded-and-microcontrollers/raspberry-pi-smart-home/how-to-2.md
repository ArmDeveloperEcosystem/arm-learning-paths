---
title: Installation Guide
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Installation Guide

{{% notice Note %}}
This guide assumes you have set up your Raspberry Pi with Raspberry Pi OS and network connectivity. For Raspberry Pi 5 setup help, see: [Raspberry Pi Getting Started](https://www.raspberrypi.com/documentation/)
{{% /notice %}}

## Connect to Your Raspberry Pi 5 via SSH

Ensure your Raspberry Pi 5 connects to the same network as your host computer. Access your device remotely via SSH using the terminal in Visual Studio Code, the built-in terminal, Command Prompt, or any other SSH client.

Replace `<user>` with your Pi's username (typically `pi`), and `<pi-ip>` with your Raspberry Pi 5's IP address.

```bash
ssh <user>@<pi-ip>
```

Create a directory called smart-home in your home directory and navigate into it:

```bash
mkdir ~/smart-home
cd ~/smart-home
```

## Prepare the System

Update your system and install necessary packages. The Raspberry Pi 5 includes Python 3 pre-installed, but you need additional packages:

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip python3-venv git curl build-essential gcc python3-lgpio
```

## Install Python Dependencies

Create and activate a Python virtual environment. This approach keeps project dependencies isolated and prevents conflicts with system-wide packages:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install all required libraries and dependencies:

```bash
pip install ollama gpiozero lgpio psutil httpx orjson numpy fastapi uvicorn uvloop
```

You can run the pip install commands without creating a virtual environment, but using a virtual environment is recommended for development workflows.

## Install Ollama

Install Ollama using the official installation script:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify the installation:

```bash
ollama --version
```

## Download and Test a Language Model

Ollama supports various models. This guide uses deepseek-r1:7b as an example, but you can also use tinyllama:1.1b, qwen:0.5b, gemma2:2b, or deepseek-coder:1.3b.

Pull and run deepseek-r1:7b:

```bash
ollama run deepseek-r1:7b
```

Ollama automatically downloads deepseek-r1:7b before running it. You will see download progress in the terminal, followed by the interactive prompt when ready.

{{% notice Note %}}
The Raspberry Pi 5 supports up to 16GB of RAM, which is sufficient for running smaller to medium-sized language models. Very large models may require more memory or run slower.
{{% /notice %}}

## Verify GPIO Functionality

Test GPIO functionality by connecting an LED. Connect the anode (long leg) of an LED in series with a 220Ω resistor to GPIO 17 (physical pin 11). Connect the cathode (short leg) to a ground (GND) pin.

Create a Python script named `testgpio.py`:

```bash
nano testgpio.py
```

Copy this code into the file:

```python
#!/usr/bin/env python3
import time
from gpiozero import Device, LED
from gpiozero.pins.lgpio import LGPIOFactory

# Set lgpio backend for Raspberry Pi 5
Device.pin_factory = LGPIOFactory()

# Setup GPIO pin 17
pin1 = LED(17)

try:
    while True:
        pin1.toggle()  # Switch pin 17 state
        time.sleep(2)  # Wait 2 seconds
except KeyboardInterrupt:  # Ctrl+C pressed
    pin1.close()  # Clean up pin 17
```

Run the script:

```bash
python testgpio.py
```

The LED should blink every two seconds. If you observe this behavior, your GPIO setup works correctly.

## Raspberry Pi 5 Specific Features

**GPIO Compatibility**: The Raspberry Pi 5 maintains GPIO compatibility with previous models. Existing GPIO code works without modification.

**Performance**: The Raspberry Pi 5 features a quad-core Arm Cortex-A76 CPU running at 2.4 GHz. This processor provides significantly improved performance for AI workloads compared to previous Raspberry Pi models. The Arm Cortex-A76 cores support NEON SIMD (Single Instruction, Multiple Data) extensions, enabling efficient parallel processing and accelerating compute-intensive tasks such as machine learning inference and signal processing.

**Power Requirements**: Use the official Raspberry Pi 5 power supply (5V/5A USB-C) for optimal performance when running AI models.

## Troubleshooting

**Missing dependencies**

Resolve dependency issues:

```bash
sudo apt-get install -f
```

**GPIO permission errors**

Run Python scripts with sudo or add your user to the gpio group:

```bash
sudo usermod -a -G gpio $USER
```

Log out and back in for changes to take effect.

**Model download issues**

- Confirm internet access and sufficient storage space on your microSD card
- Check model size before downloading to ensure adequate space
- Try downloading smaller models like `qwen:0.5b` or `tinyllama:1.1b` if you encounter memory issues
- Clear storage or connect to a more stable network if errors occur

**Hardware not responding**

- Double-check wiring and pin numbers using the Raspberry Pi 5 pinout diagram
- Ensure proper LED and resistor connections
- Verify GPIO enablement in `raspi-config` if needed
