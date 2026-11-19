---
title: "NXP FRDM i.MX93: Prepare and wire the BMP280" 
description: "Verify the image/core and wire the board-specific sensor bus."
weight: 3
layout: "learningpathall"
---

## Start with an offline application MCU

On NXP FRDM i.MX 93, lets ensure our M33 is offline:

```bash
nxp-mcore stop
nxp-mcore status
cat /etc/nxp-lp/board.json
cat /proc/cmdline
python3 /usr/libexec/nxp-lp/check-linux.py
python3 -c 'import sys; print(sys.version)'
python3 -m pip --version
```

Stopping an already inactive test service is harmless.  Power down your board now. 

## Wire up the BMP280 with board power disconnected

With the board powered down, connect the BMP280 as follows to our dev board:

| BMP280 connection | NXP FRDM i.MX 8M Plus connection |
| --- | --- |
| VCC / 3V3 | P11.1 (VRPi_3V3) |
| GND | P11.6 |
| SDA / SDI | P11.3 (GPIO_IO02) |
| SCL / SCK | P11.5 (GPIO_IO03) |
| CS / CSB | P11.17 (VRPi_3V3; selects I²C) |
| SDO | P11.20 (GND; selects `0x76`) |

## Additional details: wiring the BMP280 sensor

CSB must be high when the sensor powers on to select I²C. Swapping CSB and SDO
holds CSB low and prevents I²C communication. Correct the wiring with power
disconnected, then fully power-cycle the sensor. Use SDA/SCL pull-ups
to 3.3 V (typically 4.7 kΩ if the module has none); the firmware also enables
weak pad pull-ups. See the [Bosch I²C connection diagram](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf).

## Extract the complete Part 3 MCU temperature sources

On the Ubuntu host, download [the NXP FRDM i.MX 93 Part 3 MCU temperature source bundle](../temperature-source.zip) to your HOME directory:

```bash
mkdir -p "$HOME/nxp-imx93-temperature-part3"
unzip $HOME/temperature-source.zip -d "$HOME/nxp-imx93-temperature-part3"
cd "$HOME/nxp-imx93-temperature-part3"
```

This source zip file includes the MCU source, FRDM clock override, both resource-table patches, build/ELF inspection helpers, Linux preflight, manager, bridge, recipe generator, upload script, and host checks.

Next, we will build the temperature application.

## What you have learned

You can verify an offline Cortex-M33, wire the BMP280 to the verified NXP FRDM i.MX 93 bus signals, and prepare to build our temperature application.