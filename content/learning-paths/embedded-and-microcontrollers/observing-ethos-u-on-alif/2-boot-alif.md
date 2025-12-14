---
# User change
title: "Hardware Setup and Connections"

weight: 3

# Do not modify these elements
layout: "learningpathall"
---

In this section, you will set up the Alif [Ensemble E8 Series Development Kit](https://alifsemi.com/ensemble-e8-series/) hardware connections for ML development and debugging.

## Hardware Requirements

You need the following hardware:

- **Alif DK-E8 Board** (Ensemble E8 Development Kit)
- **USB-C Cable** for JLink programming (connects to PRG USB port)
- **USB-TTL Converter** (1.8V logic level) for UART debug output (optional but recommended)

## Connect the Programming Interface

1. Locate the **PRG USB** port on the underside of the board:

   ![The PRG USB Port on the Underside of the Board alt-text#center](./prg-usb-port.png "The PRG USB Port on the Underside of the Board")

2. Connect the board's `PRG USB` port to your computer using a USB Type-C cable

3. The board powers on automatically, with an LED in the bottom right alternating red-green-blue:

   <center>
   <iframe src='/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/e8-board-connected.mp4' allowfullscreen frameborder=0 width="800" height="400"></iframe>

   *Alif Ensemble E8 Board Connected and Powered On*
   </center>

## Set Up UART Debug Output (Optional)

For real-time debug output, you can connect an external USB-TTL converter to the board's UART2 pins. This is useful for monitoring inference results and debugging.

{{% notice Note %}}
Due to potential SW4 switch soldering issues on some boards, using an external USB-TTL converter is more reliable than the onboard USB-to-serial.
{{% /notice %}}

### UART Connection Table

Connect your USB-TTL converter to the J8 header on the board:
### UART Connection Table

Connect your USB-TTL converter to the J8 header on the board:

| USB-TTL Pin | J8 Header Pin | Signal      |
|-------------|---------------|-------------|
| GND         | Pin 1         | Ground      |
| TXD         | Pin 12        | P1_1 (UART2_TX) |
| RXD         | Pin 14        | P1_0 (UART2_RX) |

{{% notice Note %}}
Use a 1.8V logic level USB-TTL converter. Standard 3.3V or 5V converters can damage the board.
{{% /notice %}}

### J8 Header Pin Layout

The J8 header is a 2x20 pin connector. When looking down at the board:

```
J8 Header (2x20, looking down at board)

Pin 2   Pin 1  ← GND (connect here)
Pin 4   Pin 3
Pin 6   Pin 5
Pin 8   Pin 7
Pin 10  Pin 9
Pin 12  Pin 11 ← UART TX (connect here)
Pin 14  Pin 13 ← UART RX (connect here)
...     ...
```

### Verify UART Connection

After connecting the USB-TTL converter:

1. Find the serial port on your computer:
   ```bash
   ls /dev/tty.*
   ```

2. Connect using a terminal program:
   ```bash
   screen /dev/cu.usbserial-XXXX 115200
   ```

   Or use the baud rate scanner if output appears garbled:
   ```bash
   ./scan_baud.sh
   ```

## LED Status Indicators

The Alif E8 board uses an RGB LED to indicate system status:

| LED Color | Timing | Meaning |
|-----------|--------|---------|
| Red-Green-Blue alternating | Continuous | Board powered, waiting for program |
| White flash | 500ms at startup | Board initialized successfully |
| Green flash | 500ms after init | System ready |
| Blue blink | 1 Hz | Application running normally |

## Verify Board is Ready

Before proceeding to the next steps, confirm:

- ✅ PRG USB cable is connected
- ✅ Board LED is alternating red-green-blue
- ✅ (Optional) UART connections are made and verified
- ✅ Board appears as a USB device on your computer

You're now ready to install the required software tools.
* Now you can enter Fastboot mode by typing the following command in the `u-boot=>` prompt:
  ```bash
  fastboot 0
  ```
* You will be required to enter Fastboot mode on the next page of this learning path

## [Optional] Run the Built-In NXP Demos
* Connect the NXP board to a monitor via HDMI
* Connect a mouse to the NXP board's USB-A port

![NXP board built-in ML demos alt-text#center](./nxp-board-built-in-ml-demos.png "NXP board built-in ML demos")