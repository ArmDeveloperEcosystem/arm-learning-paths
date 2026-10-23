---
title: "Build the Zephyr Cortex-M4F heartbeat"
description: Compile the supplied heartbeat with Zephyr v4.3.0 for the PocketBeagle 2 AM6254 M4 target.
weight: 4
layout: "learningpathall"
---

## Prepare the Zephyr workspace

First, on our ubuntu build host, lets check if we have python v3.12:

```bash
python3.12 --version
```

If a version string is returned, we can proceed to install the host dependencies for Zephyr. If python 3.12 is not installed (likely the case if our build host is ubuntu 22.04), lets install python3.12:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv
```

Install host dependencies using the [Zephyr getting started guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html), including a supported Python, CMake, Ninja, and compiler environment. Create a separate virtual environment and pin the source release:

```bash
python3.12 -m venv "$HOME/pb2-zephyr-venv"
source "$HOME/pb2-zephyr-venv/bin/activate"
pip install west
west init -m https://github.com/zephyrproject-rtos/zephyr \
  --mr v4.3.0 "$HOME/pb2-zephyr-workspace"
cd "$HOME/pb2-zephyr-workspace"
west update
west zephyr-export
pip install -r zephyr/scripts/requirements.txt
```

Use this dedicated workspace so another project's west manifest does not select different board sources. Reactivate the virtual environment in each new terminal.

Install the SDK version recommended by this checkout using west, then confirm your revision:

```bash
cd "$HOME/pb2-zephyr-workspace/zephyr"
west sdk install
cat SDK_VERSION
git describe --tags --exact-match
```

For v4.3.0, `SDK_VERSION` is `0.17.4`, and the Git tag must be `v4.3.0`. The SDK installer chooses a host-compatible package. Check the [SDK installation guidance](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html) if download or host-tool installation fails.

## Inspect the sample

Download the [heartbeat application](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-zephyr-part2/pb2-m4-heartbeat.zip), copy it to the `$HOME` directory on the Ubuntu host, and extract it into the workspace:

```bash
cd "$HOME/pb2-zephyr-workspace"
unzip $HOME/pb2-m4-heartbeat.zip -d "$HOME/pb2-zephyr-workspace"
```

The archive contains `heartbeat/CMakeLists.txt`, `heartbeat/prj.conf`, `heartbeat/src/main.c`, and `heartbeat/src/resource_table.c`. The main source is:

```c
/* SPDX-License-Identifier: Apache-2.0 */
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>

int main(void)
{
    unsigned int count = 0;

    printk("PocketBeagle 2: Zephyr on Cortex-M4F\n");
    while (1) {
        printk("M4 heartbeat %u\n", count++);
        k_sleep(K_SECONDS(1));
    }
    return 0;
}
```

`printk()` writes to the board target's MCU_UART0 console. `k_sleep()` yields the thread for one second between messages. The sample does not configure a GPIO, change the Linux heartbeat LED, or implement a mailbox shutdown protocol.

## Build the ELF executable

Build for the M4 qualifier, not the board's A53 target:

```bash
cd "$HOME/pb2-zephyr-workspace"
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
west build -p always -b pocketbeagle_2/am6254/m4 \
  heartbeat -d build/pb2-m4-heartbeat
file build/pb2-m4-heartbeat/zephyr/zephyr.elf
```

The result must be a 32-bit Arm ELF executable. Linux remains 64-bit `aarch64`; the MCU firmware is a different executable for a different core.

Use the SDK's `arm-zephyr-eabi-readelf` tool to inspect the ELF sections if needed. The board's SoC configuration reserves a section for an OpenAMP resource table. The sample's `resource_table.c` supplies a version-one table with zero resource entries because this UART-only application does not create RPMsg devices. The ELF must retain its `.resource_table` section. Do not strip the ELF or replace it with `zephyr.bin`: the Linux remoteproc loader needs the ELF program headers and resource information.

## What you have accomplished

You have a Zephyr ELF built for the Cortex-M4F and a source tree pinned to v4.3.0. Next, transfer it to the running board and start the offline M4 from Linux.
