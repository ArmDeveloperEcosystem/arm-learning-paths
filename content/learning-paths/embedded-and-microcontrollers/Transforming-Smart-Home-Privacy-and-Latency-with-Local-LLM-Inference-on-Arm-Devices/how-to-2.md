---
title: Installation Guide
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Installation Guide

{{% notice Note %}}
This guide assumes you have already set up your Raspberry Pi or NVIDIA Jetson board with an operating system and network connectivity.For board setup help, see: [Raspberry Pi Getting Started](https://www.raspberrypi.com/documentation/) or [Jetson Getting Started](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit).
{{% /notice %}}

### Step 1: Connect to Your Board via SSH

Before proceeding, make sure your SBC is connected to the same network as your host computer. Then, access your device remotely via SSH. You can use the terminal in Visual Studio Code on your host PC, the built-in terminal, Command Prompt, or any other preferred SSH client.

Replace `<user>` with your device’s username , and `<board-ip>` with your device’s IP address.

**General SSH Command:**

```bash
ssh <user>@<board-ip>

```

Create a directory called smart-home in your home directory and navigate into it by running the following commands:

```bash
mkdir ~/smart-home
cd ~/smart-home
```

### Step 2: System Preparation

Update your system and ensure Python 3 and pip are installed.

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip python3-venv git
```

### Step 3: Requirements Installation

Create and activate a Python virtual environment using the following commands. This is recommended, as it keeps your project dependencies isolated and prevents conflicts with system-wide packages:

```bash
python3 -m venv venv
source venv/bin/activate
```

This approach helps ensure that your system’s Python environment remains stable and avoids breaking other projects.

Next, install all the required libraries and dependencies for the project by running the appropriate command for your board:

{{< tabpane code=true >}}
{{< tab header="Jetson (NVIDIA)" language="bash">}}
pip install flask flask-cors requests schedule ollama adafruit-blinka adafruit-circuitpython-dht Jetson.GPIO

{{< /tab >}}
{{< tab header="Raspberry Pi" language="bash">}}
pip install flask flask-cors requests schedule ollama adafruit-blinka adafruit-circuitpython-dht RPi.GPIO
{{< /tab >}}
{{< /tabpane >}}

If you prefer, you can also run the above pip install commands directly, without creating a virtual environment. However, using a virtual environment is strongly recommended for most development workflows.

### Step 4: Install Ollama

Run the following command to install **Ollama**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

On most recent Linux distributions (including Raspberry Pi OS and Ubuntu for Jetson), curl is usually pre-installed by default. However, in some minimal installations, it might not be present. If you get a **command not found** error for curl, you can easily install it with:

```bash
sudo apt update
sudo apt install curl
```

After installation, verify it by running the following command:

```bash
ollama --version
```

### Step 5: Download and Test a Language Model

Ollama supports a variety of models. This guide uses Deepseek-R1:7B as an example, but you can also use other models such as Mistral or Phi. To pull and run Deepseek-R1:7B:

```bash
ollama run deepseek-r1:7b
```

Ollama will automatically download deepseek -r1:7b first before running it. You’ll see download progress in the terminal, followed by the interactive prompt once it’s ready. An example is shown in the image below:

![deepseek test image alt-text#center](deepseek.png "Figure 1. deepseek test image caption")

### Step 6: Verify GPIO Functionality

To test the GPIO functionality, you’ll begin by connecting an LED to your board. For **Jetson Xavier AGX**, connect the anode (the long leg) of an LED, in series with a suitable resistor, to pin 12 . For **Raspberry Pi**, connect the anode of the LED (again, in series with a resistor) to GPIO 17 . In both cases, connect the cathode (the short leg) of the LED to a ground (GND) pin on your SBC. Once your wiring is complete, create a Python script named `testgpio.py` using your favorite editor.

```bash
vim testgpio.py
```

Copy the appropriate code below into the testgpio.py file you just created, then save and close the file.

{{< tabpane code=true >}}
{{< tab header="Jetson" language="python" output_lines="8">}}
import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.HIGH)
time.sleep(2)
GPIO.output(12, GPIO.LOW)
GPIO.cleanup()
{{< /tab >}}
{{< tab header="Raspberry Pi" language="python" output_lines="8">}}
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH)
time.sleep(2)
GPIO.output(17, GPIO.LOW)
GPIO.cleanup()
{{< /tab >}}
{{< /tabpane >}}

Once you’ve saved your script, run the code using the following command in your terminal:

```bash
python testgpio.py
```

The LED should blink according to the set timing in your script—turning on for two seconds and then off. If you see this behavior, your GPIO setup is working correctly.
![Xavier AGX LED image alt-text#center](hardware2.png "Figure 1. Jetson Xavier AGX GPIO Test")

### Troubleshooting

- Missing dependencies?

  Run the following command to resolve the issue:

  ```bash
  sudo apt-get install -f
  ```

- GPIO permission errors?

  - Run Python scripts with **sudo**.

- Model download issues?

  - Confirm you have internet access and sufficient storage space on your device.

  - Check the model size before downloading to ensure your SBC has enough space to store and run it.
  - Try downloading a smaller model
  - If you encounter errors, clear up storage or try connecting to a more stable network

- Hardware not responding?

  - Double-check wiring and pin numbers.
