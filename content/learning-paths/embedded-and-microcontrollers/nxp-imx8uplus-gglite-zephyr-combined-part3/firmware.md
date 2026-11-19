---
title: "NXP FRDM i.MX 8M Plus: Build and test the BMP280 temperature firmware"
description: "Compile the MCU sensor app and validate its operation manually."
weight: 4
layout: "learningpathall"
---

## Build the temperature sensor MCU application ELF

On the Ubuntu host, lets initiate a build of the temperature sensor MCU source:

```bash
source "$HOME/nxp-imx8uplus-zephyr-venv/bin/activate"
export ZEPHYR_WORKSPACE="$HOME/nxp-imx8uplus-zephyr-workspace"
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
export ZEPHYR_SDK_INSTALL_DIR="$HOME/zephyr-sdk-0.17.4"
cd "$HOME/nxp-imx8uplus-temperature-part3"
bash setup-zephyr-sdk.sh
bash build-zephyr.sh temperature
python3 inspect-elf.py build/temperature/zephyr/zephyr.elf
"$ZEPHYR_SDK_INSTALL_DIR/arm-zephyr-eabi/bin/arm-zephyr-eabi-readelf" -h -S -l build/temperature/zephyr/zephyr.elf
```

## Manually run the ELF on the MCU and verify sensor connectivity

In a SSH shell on the Ubuntu host, manually copy over the compiled elf to the i.MX8MPLUS dev board:

```bash
scp $HOME/nxp-imx8uplus-temperature-part3/build/temperature/zephyr/zephyr.elf root@OUR_BOARD_IP_ADDRESS:./temperature-zephyr.elf
```

In a SSH onto our dev board, lets manually invoke the elf to confirm it is working:

```bash
ssh root@OUR_BOARD_IP_ADDRESS
nxp-mcore load ./temperature-zephyr.elf
nxp-mcore status
```

You should see output similar to:

```output
device=/sys/class/remoteproc/remoteproc0 name=imx-rproc state=running firmware=nxp-imx8uplus-gg-34be8b5189faa9e9.elf
```

With your access to the MCU UART DEBUG console previously setup, you should see output similar to:

```output
*** Booting Zephyr OS build v4.3.0 ***
NXP FRDM i.MX 8M Plus: Zephyr on application MCU
External BMP280 found at I2C address 0x77
```

Lastly, we can confirm that temperature JSONs are being published locally on the dev board. On the dev board, type:

```bash
stty -F /dev/nxp-temperature raw -echo
printf 'HELLO\n' > /dev/nxp-temperature
timeout 60 cat /dev/nxp-temperature
```

You get approximately 60 seconds of periodic output that resembles:

```output
{"type":"nxp.external.temperature","schema":1,"seq":14,"uptime_ms":70298,"temperature_uC":25730000}
{"type":"nxp.external.temperature","schema":1,"seq":15,"uptime_ms":75308,"temperature_uC":25570000}
{"type":"nxp.external.temperature","schema":1,"seq":16,"uptime_ms":80318,"temperature_uC":25550000}
```

This output indicates that the MCU has proper wiring to the BMP280 temperature sensor and that the elf is correctly reading and publishing temperature values. 

We can now stop the ELF:

```bash
nxp-mcore stop
nxp-mcore status
```

Output should resemble:

```output
device=/sys/class/remoteproc/remoteproc0 name=imx-rproc state=offline firmware=rproc-imx-rproc-fw
```

## Additional detail: Acquire and compensate actual temperature

The application detects the BMP280 at `0x76` or `0x77`, verifies chip ID, resets it, reads factory `dig_T1/2/3` calibration, and triggers one forced temperature measurement approximately every five seconds. It skips pressure and uses the signed integer compensation helper tested on the host.

The hundredths-of-a-degree result is scaled into the existing microdegree transport field. It does not imply microdegree sensor precision. A frame looks like:

```json
{"type":"nxp.external.temperature","schema":1,"seq":12,"uptime_ms":60320,"temperature_uC":25080000}
```

A failed sensor read emits a diagnostic and no temperature frame. The bridge does not substitute a SoC thermal reading, a fixed value, or a Linux sensor value. The NXP FRDM i.MX 8M Plus overlay selects the physical bus described on the preparation page.

## Additional Detail: Manage the full MCU lifecycle

The first recipe downloads `zephyr.elf`, `firmware_manager.py` and
`check-linux.py` before installation. `install` validates and stages the ELF.
Before modifying firmware or sysfs, `run` checks FRDM Linux identity, the running
`clk-imx8mp.mcore_booted` argument, exact named reserved-memory ranges, released
UART4 and an offline M7. A failed preflight aborts the start. It then records
ownership, installs a digest-derived firmware filename, starts remoteproc and
completes the control endpoint's HELLO/READY exchange.

On normal SIGTERM, the manager exchanges `STOP` / `QUIESCED`, waits briefly for the MCU to enter WFI, requests remoteproc stop, requires offline state, restores the previous firmware filename, and removes its installed ELF and ownership record. It leaves a safe lock inode and the runtime's own cache infrastructure.


## What you have learned

You can compile the actual NXP FRDM i.MX 8M Plus BMP280 firmware and manually confirm that the firmware runs successfully on the MCU and that the BMP280 temperature sensor is reachable and connected to the firmware when it runs.
