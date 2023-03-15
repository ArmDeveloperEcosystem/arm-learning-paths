---
title: "Blinky"
weight: 8

# FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Bare metal blinky firmware

On this step, we create a simple blinky bare metal firmware using our HAL API
defined in `hal.h`. The firmware functionality goes into `main.c` file.

Create a new `main.c` file with the following contents:

```c
// Copyright (c) 2022 Cesanta Software Limited
#include "hal.h"

static volatile uint32_t s_ticks;
void SysTick_Handler(void) { s_ticks++; }

// t: expiration time, prd: period, now: current time. Return true if expired
bool timer_expired(uint32_t *t, uint32_t prd, uint32_t now) {
  if (now + prd < *t) *t = 0;                    // Time wrapped? Reset timer
  if (*t == 0) *t = now + prd;                   // Firt poll? Set expiration
  if (*t > now) return false;                    // Not expired yet, return
  *t = (now - *t) > prd ? now + prd : *t + prd;  // Next expiration time
  return true;                                   // Expired, return true
}

int main(void) {
  uint16_t led = PIN('E', 1);        // Blue LED.
  gpio_output(led);                  // Set blue LED to output mode
  uart_init(UART_DEBUG, 115200);     // Initialise UART
  uint32_t timer = 0, period = 500;  // Declare timer and 500ms period
  for (;;) {
    if (timer_expired(&timer, period, s_ticks)) {
      static bool on;       // This block is executed
      gpio_write(led, on);  // Every `period` milliseconds
      on = !on;             // Toggle LED state
      printf("LED: %d, tick: %lu\r\n", on, s_ticks);  // Write message
    }
    // Here we could perform other activities!
  }
  return 0;
}
```

Note: on STMF4/STMF7 Nucleo boards, use `PIN('B', 7)` for a LED.

This firmware defines a SysTick IRQ handler, which increments `s_ticks`
variable every millisecond. A `timer_expired()` helper function is used
in a superloop, where we blink an LED and print a debug message.

## Build firmware

Now it is time to build the firmware! Start a terminal / command prompt,
and enter the following commands:

```
cd PATH_TO_YOUR_PROJECT_DIRECTORY
make
```

You should see an output like this:

```
arm-none-eabi-gcc main.c syscalls.c sysinit.c cmsis_h7/Source/Templates/gcc/startup_stm32h743xx.s  -W -Wall -Wextra -Werror -Wundef -Wshadow -Wdouble-promotion -Wformat-truncation -fno-common -Wconversion -Wno-sign-conversion -g3 -Os -ffunction-sections -fdata-sections -I. -Icmsis_core/CMSIS/Core/Include -Icmsis_h7/Include -mcpu=cortex-m7 -mthumb -mfloat-abi=hard -mfpu=fpv5-sp-d16 -Tlink.ld -nostdlib -nostartfiles --specs nano.specs -lc -lgcc -Wl,--gc-sections -Wl,-Map=firmware.elf.map -o firmware.elf
arm-none-eabi-objcopy -O binary firmware.elf firmware.bin
```

That means, our firmare file `firmware.bin` is built and ready to be flashed

## Flash firmware

Make sure your hardware board is plugged to the USB.
In the terminal, enter the following command:

```
make flash
```

The blue LED on your board should start blinking.

## Observe debug logs

Those Nucleo boards by ST all contain a built-in hardware debugger. That
debugger connects USART3 port to the debugger's USB interface.
When a board is plugged to the USB, a COM port device should appear on your
workstation. If we attach a serial monitor, like `putty` on Windows or
`cu` on Mac/Linux, we can observe debug logs printed by our firmware:

```
LED: 1, tick: 250
LED: 0, tick: 500
LED: 1, tick: 750
LED: 0, tick: 1000
```
