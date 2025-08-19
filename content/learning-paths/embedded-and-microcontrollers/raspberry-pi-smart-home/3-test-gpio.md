---
title: Test Raspberry Pi 5 GPIO pins for smart home devices
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

The next step is to test the GPIO functionality. In this section, you configure an LED light to simulate a smart home device.

## Verify GPIO setup on Raspberry Pi 5

Gather your electronic components. Connect the anode (long leg) of an LED in series with a 220Ω resistor to GPIO 17 (physical pin 11). Connect the cathode (short leg) to a ground (GND) pin. 

See the image below for the full setup:

![Raspberry Pi connected to a breadboard with a green LED and jumper wires alt-text#center](pin_layout.jpg "Raspberry Pi connected to a breadboard with a green LED and jumper wires")

Create a Python script named `testgpio.py`:

```bash
cd $HOME/smart-home
vim testgpio.py
```

Add the following code to the file:

```python
#!/usr/bin/env python3
import time
from gpiozero import Device, LED
from gpiozero.pins.lgpio import LGPIOFactory

# Set lgpio backend for Raspberry Pi 5
Device.pin_factory = LGPIOFactory()

# Set up GPIO pin 17
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

{{% notice Troubleshooting %}}
If you run into issues with the hardware setup, check the following:

- Fix missing dependencies with:  
  ```bash
  sudo apt-get install -f
  ```
- If you encounter GPIO permission issues, run Python scripts with `sudo` or add your user to the `gpio` group. Don’t forget to log out for the changes to take effect:  
  ```bash
  sudo usermod -a -G gpio $USER
  ```
- Double-check wiring and pin numbers using the Raspberry Pi 5 pinout diagram
- Ensure proper LED and resistor connections
- Verify GPIO enablement in `raspi-config` if needed
- Use a high-quality power supply
{{% /notice %}}

With GPIO pins working, you can now move on to the next section to interact with devices using language models and the user interface.
