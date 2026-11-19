---
title: "NXP FRDM i.MX 8M Plus: Prepare and wire the BMP280"
description: "Verify the image/core and wire the board-specific sensor bus."
weight: 3
layout: "learningpathall"
---

## Start with an offline application MCU

On NXP FRDM i.MX 8M Plus, lets ensure our M7 is offline:

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
| VCC / 3V3 | J18.1 (3.3V) |
| GND | J18.6 (GND) |
| SDA / SDI | J18.3 (I2C3_SDA_3V3) |
| SCL / SCK | J18.5 (I2C3_SCL_3V3) |
| CS / CSB | J18.20 (GND) |
| SDO | J18.17 (3.3V for `0x77`) |


## Additional details: wiring the BMP280 sensor

Keep CSB high from power-up to select I2C. Grounding CSB selects SPI and
disables I2C until the BMP280 is power-cycled; see
[Bosch's datasheet, section 5.1](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf#page=27).
After a power cycle, reload a manual MCU test. If loading reports a stale owner
record, use the updated manager's recovery procedure in `MCU-RECOVERY.md` in
the source bundle. Successful readings travel over RPMsg; the debug console
prints sensor discovery once and reports acquisition failures.

## Extract the complete Part 3 MCU temperature sources

On the Ubuntu host, download [the NXP FRDM i.MX 8M Plus Part 3 MCU temperature source bundle](../temperature-source.zip) to your HOME directory:

```bash
mkdir -p "$HOME/nxp-imx8uplus-temperature-part3"
unzip $HOME/temperature-source.zip -d "$HOME/nxp-imx8uplus-temperature-part3"
cd "$HOME/nxp-imx8uplus-temperature-part3"
```

This source zip file includes the MCU source, FRDM clock override, both resource-table patches, build/ELF inspection helpers, Linux preflight, manager, bridge, recipe generator, upload script, and host checks.

Next, we will build the temperature application.

## What you have learned

You can verify an offline Cortex-M7, wire the BMP280 to the verified NXP FRDM i.MX 8M Plus bus signals, and prepare to build our temperature application.
