---
title: Build and run the hello_world sample on the Corstone-320 MPS4 platform
description: Build the Zephyr hello_world sample for the Corstone-320 MPS4 FPGA target, split the ELF image, and run the application on the MPS4 board.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the hello_world example for MPS4

The Zephyr `hello_world` example prints "Hello World" to the console. Use it to validate that your board support and toolchain configuration work correctly.

Activate your Python virtual environment:

```bash
source ~/zephyrproject/.venv/bin/activate
```

If you haven't set the toolchain environment variables in your current terminal, set them now. For full setup steps, see [Set up the Zephyr build environment](/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/how-to-1/):

```bash
export ZEPHYR_TOOLCHAIN_VARIANT=gnuarmemb
export GNUARMEMB_TOOLCHAIN_PATH=$HOME/arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi
```

Replace the path with the path to your toolchain directory. On x86_64, the directory name starts with `x86_64` instead of `aarch64`.

From the `~/zephyrproject/zephyr` directory, build the `hello_world` example for the Corstone-320 FPGA variant:

```bash
west build -p always -b mps4/corstone320/fpga zephyr/samples/hello_world -- -DCONFIG_ROMSTART_RELOCATION_ROM=y
```

The output is similar to:

```output
[xxx/xxx] Linking C executable zephyr/zephyr.elf
Memory region         Used Size  Region Size  %age Used
 ROMSTART_REGION:         xxx B       128 KB      x.xx%
           FLASH:       xxxxx B         4 MB      x.xx%
             RAM:        xxxx B         2 MB      x.xx%
```

Verify that the ELF image was created:

```bash
ls build/zephyr/zephyr.elf
```

The output is similar to:

```output
build/zephyr/zephyr.elf
```

The ELF image contains the application and the Zephyr kernel libraries. You can now load it onto the MPS4 board.

## Run the application on the MPS4 board

To run the application on the MPS4 board, follow these steps:

1. Download the board files from [FI101](https://developer.arm.com/downloads/view/FI101?sortBy=availableBy&revision=r1p0-00eac0-2).
2. Set up the MPS4 platform according to the [Using the FI101 on MPS4 board](https://developer.arm.com/documentation/109762/0100/?lang=en).

3. For the hello_world application, place the vector table in the FPGA boot ROM at address `0x11000000`, and place the remaining code and data in SRAM at address `0x31000000`. Use `arm-none-eabi-objcopy` to extract these two regions from `build/zephyr/zephyr.elf`:

```bash
arm-none-eabi-objcopy  -O binary --only-section=rom_start zephyr.elf vector.bin
arm-none-eabi-objcopy  -O binary --remove-section=rom_start zephyr.elf app.bin
```

4. Update `images.txt` under `/MB/HBI0376B/FI101` to load the two images. The paths use the `\SOFTWARE\` folder on the MPS4 SD card, which is where you will copy the binary files:

```text
IMAGE0PORT: 2
IMAGE0ADDRESS: 0x00_1100_0000           ; Address to load into
IMAGE0UPDATE: RAM
IMAGE0FILE: \SOFTWARE\vector.bin        ; Image/data to be loaded

IMAGE1PORT: 1
IMAGE1ADDRESS: 0x31000000               ; Address to load into
IMAGE1UPDATE: RAM
IMAGE1FILE: \SOFTWARE\app.bin           ; Image/data to be loaded
```

5. Copy `vector.bin` and `app.bin` to the `\SOFTWARE\` folder on the MPS4 SD card, then power on the board.
If the setup is correct, the UART console prints the “Hello World” message, similar to the following example:

![UART console output showing "Hello World! arm" from Zephyr running on the Corstone-320 MPS4 board#center](image.png)

## What you've accomplished

You've now built and run the Zephyr `hello_world` example on the MPS4 board. 

You can use the workflow outlined in this Learning Path as a foundation to further customize Zephyr on the Corstone-320 MPS4 platform and validate a complete build-and-run workflow.
