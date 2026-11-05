---
title: "Prepare the board and wire the external sensor"
description: Start with an offline M4, reserve the MCU GPIOs, and connect external temperature sensing and an on-board UART bridge.
weight: 3
layout: "learningpathall"
---

## Return the M4 to an offline state

Save work, shut down Linux, disconnect power, and power up again to end Part 2's heartbeat. Do not issue `stop` against that older firmware: it has no shutdown acknowledgment. On the board, check:

```bash
uname -m
pb2-m4 status
python3 -c 'import sys; print(sys.version)'
python3 -m pip --version
systemctl status --with-dependencies greengrass-lite.target
```

Expect `aarch64`, Python 3.12 from the Scarthgap image, healthy Greengrass services, and the M4 named `5000000.m4fss` in state `offline`. If it is attached or running after a power cycle, resolve bootloader ownership as described in Part 2 before continuing. No service should automatically load the heartbeat.

## Check exclusive peripheral ownership

This example uses MCU GPIO0 pins 16 and 15 for software I2C, and MCU_UART0 for telemetry. The Part 1 image already disables Linux's MCU_UART0 and enables MAIN_UART0. The Zephyr GPIO driver initializes the entire MCU GPIO0 bank to inputs, so this application requires exclusive ownership of that bank. Do not use a cape or Linux GPIO consumer that controls it or any of the paired header pads.

On the board, inspect line consumers and the UART mapping:

```bash
gpioinfo
readlink -f /sys/class/tty/ttyS7/device
cat /proc/cmdline
systemctl status serial-getty@ttyS7.service
```

In the pinned board device tree, `serial7` is MAIN_UART0 at `0x02800000`; the device path for `ttyS7` must identify `2800000.serial`. It must not be a kernel console or a login terminal. If a serial getty is enabled on this dedicated port, disable it with `systemctl disable --now serial-getty@ttyS7.service`. Leave the Linux debug console on MAIN_UART6 available. If your numbering differs, identify MAIN_UART0 by its controller address and use that device in the bridge deployment configuration.

Check pinctrl ownership where available:

```bash
mountpoint -q /sys/kernel/debug || mount -t debugfs debugfs /sys/kernel/debug
grep -E '1d0|1d4|0408403c|04084040' /sys/kernel/debug/pinctrl/*/pinmux-pins
```

The paired MAIN pads on P2.09/P2.11 (`GPIO1_22/23`, offsets `0x1d0/0x1d4`) must remain unused inputs, and MCU pads `0x04084040/0x0408403c` belong to Zephyr. An active pinmux or GPIO consumer on these pads is a conflict to resolve before loading firmware. Debug output formats differ; do not treat an empty grep as proof of ownership. Use the running device tree, `gpioinfo`, and your cape configuration together. This path does not take over the PMIC I2C bus, the MSPM0 ADC/EEPROM, or Linux's header I2C2.

## Wire while power is disconnected

Use the [PocketBeagle 2 header tables](https://docs.beagleboard.org/boards/pocketbeagle-2/04-expansion.html) to confirm orientation. The same physical header pin can connect two processor pads; both sides must obey the ownership rules above.

| Connection | PocketBeagle 2 pin | Notes |
| --- | --- | --- |
| BMP280 VCC / 3V3 | P1.14, 3.3 V | Use the module's documented 3.3 V power input |
| BMP280 GND | P1.16, GND | Common reference |
| BMP280 SCL / SCK | P2.09 | MCU_GPIO0_16; software I2C clock |
| BMP280 SDA / SDI | P2.11 | MCU_GPIO0_15; software I2C data |
| BMP280 CS / CSB, if exposed | P1.14, 3.3 V | Selects I2C; keep high from power-up |
| BMP280 SDO, if exposed | P1.16, GND | Selects `0x76`; 3.3 V selects `0x77` |
| Telemetry jumper | P2.07 to P1.32 | MCU_UART0 TX to MAIN_UART0 RX |

Four-pin I2C modules normally strap CSB and the address internally; follow the module's labels and schematic. The firmware checks both legal addresses and requires exactly one BMP280. It rejects a BME280 chip ID. Confirm the detected address in the MCU UART diagnostic after deployment. The [Bosch connection diagram](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf) documents the underlying sensor pins; breakout connector order varies.

Fit pull-ups from SCL and SDA to **3.3 V**, typically 4.7 kΩ, unless the breakout already provides suitable pull-ups. Keep wires short. The software releases a line by making it an input and drives it only low, because the pinned GPIO driver rejects hardware open-drain mode. No Linux `i2cdetect` scan can find this private software bus.

Do not connect a 5 V pull-up, a UART adapter's power lead, or two UART transmitters together. P1.30, the Linux UART TX, is unused. You may retain Part 2's USB UART adapter as an output-only monitor on P2.07 and GND, with its TX lead disconnected. The bridge runs on PocketBeagle 2 and needs no USB UART adapter.

Power up and rerun `pb2-m4 status`:

```bash
pb2-m4 status
```

Output should resemble:

```output
device=/sys/class/remoteproc/remoteproc0 name=5000000.m4fss state=offline firmware=am62-mcu-m4f0_0-fw
```

Leave the M4 offline until Greengrass deploys the new firmware.

Since the pocketbeagle2 has been rebooted, open a SSH shell into the pocketbeagle2 from the ubuntu host and ensure that name resolution is enabled:

```bash
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
```

Confirm by pinging `google.com` from that shell:

```bash
ping google.com
```

Output should resemble:

```output
PING google.com (172.217.72.102) 56(84) bytes of data.
64 bytes from lcdfwna-in-f102.1e100.net (172.217.72.102): icmp_seq=1 ttl=106 time=26.3 ms
64 bytes from lcdfwna-in-f102.1e100.net (172.217.72.102): icmp_seq=2 ttl=106 time=23.8 ms
```

## Prepare the source bundle

Download [the Part 3 source bundle](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-gglite-zephyr-combined-part3/pb2-temperature-part3.zip) to the Ubuntu host and extract it:

```bash
mkdir -p "$HOME/pb2-temperature-part3"
unzip pb2-temperature-part3.zip -d "$HOME/pb2-temperature-part3"
cd "$HOME/pb2-temperature-part3"
```

When working from this sandbox checkout, copy the contents of this path's `bundle/` directory to that workspace instead. The workspace contains `firmware/`, `components/`, and `tools/`; it contains no credentials.

## What you have learned

You have learned how to prepare an offline M4, check peripheral ownership, and wire the BMP280 and UART jumper without conflicting with Linux. You can now identify the sensor's I2C mode and address connections, select the Linux UART for the bridge, and prepare the source workspace for building the firmware.
