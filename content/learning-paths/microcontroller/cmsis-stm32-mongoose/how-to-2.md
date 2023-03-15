---
title: "Makefile"
weight: 3

# FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Create Makefile

Makefile is a configuration file for the `make` utility, which is used to
automate firmware build and flash. Instead of running build / flash commands
manually, we record them in the Makefile.

Create a new file, called `Makefile`, and copy-paste the following contents
in it:

```make
CFLAGS  = -W -Wall -Wextra -Werror -Wundef -Wshadow -Wdouble-promotion
CFLAGS += -Wformat-truncation -fno-common -Wconversion -Wno-sign-conversion
CFLAGS += -g3 -Os -ffunction-sections -fdata-sections
CFLAGS += -I. -Icmsis_core/CMSIS/Core/Include -Icmsis_h7/Include
CFLAGS += -mcpu=cortex-m7 -mthumb -mfloat-abi=hard -mfpu=fpv5-sp-d16
LDFLAGS ?= -Tlink.ld -nostdlib -nostartfiles --specs nano.specs -lc -lgcc -Wl,--gc-sections -Wl,-Map=$@.map

SOURCES = main.c syscalls.c sysinit.c
SOURCES += cmsis_h7/Source/Templates/gcc/startup_stm32h743xx.s # ST startup file. Compiler-dependent!

firmware.bin: firmware.elf
	arm-none-eabi-objcopy -O binary $< $@

firmware.elf: cmsis_core cmsis_h7 $(SOURCES) hal.h link.ld 
	arm-none-eabi-gcc $(SOURCES) $(CFLAGS) $(LDFLAGS) -o $@

flash: firmware.bin
	st-flash --reset write $< 0x8000000

cmsis_core:     # ARM CMSIS core headers
	git clone --depth 1 -b 5.9.0 https://github.com/ARM-software/CMSIS_5 $@
cmsis_h7:       # ST CMSIS headers for STM32H7 series
	git clone --depth 1 -b v1.10.3 https://github.com/STMicroelectronics/cmsis_device_h7 $@
```

This file contains build instructions on how exactly to build a firmare:
- `CFLAGS` is a variable that contains GCC compiler compilation flag
  - For STM32F4, please change the line with `-mcpu` to the following line:
  ```
  CFLAGS += -mcpu=cortex-m4 -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16
  ```
- `SOURCES` is a variable that contains a list of project source code files
- A default build target is `firmware.bin`, which is a flashable binary
- In order to build `firmware.bin`, we should build `firmware.elf`
- In order to build `firmware.elf`, we must download:
  - ARM CMSIS core headers, which contain definitions for Cortex-M
  - ST CMSIS headers, which contain definitions for our exact MCU
- We are going to use a `startup_stm32h743xx.s` startup file provided by
  the ST CMSIS, by adding that file to the `SOURCES` variable
