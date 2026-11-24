---
title: "NXP FRDM i.MX 93: Build the Zephyr heartbeat" 
description: "Compile the supplied board-specific MCU firmware with the pinned toolchain."
weight: 4
layout: "learningpathall"
---

## Build preparation

Ubuntu hosts may be either **x86_64/amd64 or arm64/aarch64**. Install native host
packages and Python 3.12+ for that Ubuntu release. West automatically selects
the matching SDK host archive; arm-zephyr-eabi remains the MCU compiler target.
After extracting the source bundle, `bash setup-zephyr-sdk.sh` installs or
checks SDK 0.17.4. Keep SDKs and virtual environments local to each host; an
incompatible existing SDK is preserved and reported before compilation.


For these MCU builds, the following native Ubuntu packages work on either host
architecture. Apt chooses amd64 or arm64 packages automatically; the Zephyr SDK
supplies the MCU cross-compiler, so host gcc-multilib/g++-multilib are unnecessary.
Ubuntu 24.04 supplies Python 3.12; on Ubuntu 22.04 provide Python 3.12+ and its
matching venv support before creating the virtual environment below.

```bash
sudo apt-get update
sudo apt-get install -y git cmake ninja-build gperf ccache device-tree-compiler python3-dev python3-pip python3-venv xz-utils file make gcc g++ wget
```

## Prepare a dedicated west workspace

On the Ubuntu host, use Python 3.12 or newer, CMake, Ninja, and the host dependencies from the [Zephyr getting-started guide](https://docs.zephyrproject.org/4.3.0/develop/getting_started/index.html). Ubuntu 24.04 provides Python 3.12 and its matching venv package.

First, lets create a venv for python3.12:

```bash
python3.12 -m venv "$HOME/nxp-imx93-zephyr-venv"
source "$HOME/nxp-imx93-zephyr-venv/bin/activate"
```

Confirm that we now have a venv with python3.12:

```bash
python3 --version
```

You should see some version of 3.12 reported. Next lets install west:

```bash
python3 -m pip install west
export PATH="$HOME/.local/bin:$PATH"
```

Now, lets initialize our zephyr build workspace:

```bash
python3 -m  west init -m https://github.com/zephyrproject-rtos/zephyr --mr v4.3.0 "$HOME/nxp-imx8uplus-zephyr-workspace"
cd "$HOME/nxp-imx93-zephyr-workspace"
python3 -m west update
python3 -m west zephyr-export
python3 -m pip install -r zephyr/scripts/requirements.txt
```

## Build the heartbeat

Download and extract [this board's MCU source bundle](../mcu-source.zip). Then:

```bash
mkdir -p "$HOME/nxp-imx93-mcu"
unzip mcu-source.zip -d "$HOME/nxp-imx93-mcu"
cd "$HOME/nxp-imx93-mcu"
source "$HOME/nxp-imx93-zephyr-venv/bin/activate"
export ZEPHYR_WORKSPACE="$HOME/nxp-imx93-zephyr-workspace"
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
export ZEPHYR_SDK_INSTALL_DIR="$HOME/zephyr-sdk-0.17.4"
bash setup-zephyr-sdk.sh
bash build-zephyr.sh heartbeat
ls -al build/heartbeat/zephyr/zephyr.elf
```

## Inspect the heartbeat MCU ELF artifact

The following command allows you to introspect the ELF:

```bash
python3 inspect-elf.py build/heartbeat/zephyr/zephyr.elf
"$ZEPHYR_SDK_INSTALL_DIR/arm-zephyr-eabi/bin/arm-zephyr-eabi-readelf" -h -S -l build/heartbeat/zephyr/zephyr.elf
```

## What you have learned

You can build the NXP FRDM i.MX 93 heartbeat with the pinned toolchain, apply the Linux-owned resource-table policy, and inspect the ELF before transferring it to the application core.
