---
# User change
title: "Modify the example to use the UART for printf output"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
In the previous section, a mechanism called [semihosting](https://developer.arm.com/documentation/100966/latest/Getting-Started-with-Fixed-Virtual-Platforms/FVP-debug) was used to handle the output from our application. We will modify the example to send output to a UART serial port. This is useful because embedded systems often have limited display capabilities, or no display capabilities. However, during the debug process it is often useful to be able to print diagnostic messages while a program is running.

## Understanding Semihosting

Semihosting enables code running on a target system, the model, to interface with a debugger running on a host system, the computer, and to use its input and output (I/O) facilities. This means that you can interact with a model or microcontroller that may not possess I/O functionality.

We used a `printf()` call in the code to display the "Hello World!" message. This printf() call triggers a request to a connected debugger through the library function `_sys_write.` To see how this works, we can use `fromelf` to disassemble the compiled code:
```console
fromelf --text -c hello.axf --output=disasm.txt
```
Within the disassembly, search for `_sys_write`, which contains a `HLT` (halt) instruction:
```
_sys_write
    0x00003a74:    d100c3ff    ....    SUB      sp,sp,#0x30
    0x00003a78:    a9027bfd    .{..    STP      x29,x30,[sp,#0x20]
    ...
    0x00003a9c:    d45e0000    ..^.    HLT      #0xf000
    ...
    0x00003aa8:    d65f03c0    .._.    RET
```

The FVP detects this halt as a semihosting operation, and interprets the `_sys_write` as a request to output to the console. If running on real hardware (without a debugger connected), this would just stop execution.

You can check if you are using semihosting by adding `__asm(".global __use_no_semihosting\n\t");` to your source. Linking the image will now throw an error for any functions that use semihosting.
```
Error: L6915E: Library reports error: __use_no_semihosting was requested, but _ttywrch was referenced
```
## Retarget fputc to use the UART

Many library functions depend on semihosting. You must modify, or `retarget`, these functions to use the hardware of the target instead of the host system.

Here we will retarget `printf()` to use the [PL011 UART](https://developer.arm.com/documentation/ddi0183) of the FVP:

Write a driver for the UART. Copy and paste the following code into a new file with the filename `pl011_uart.c`. This contains code to initialize the UART (`uartInit()`), and a retargeted version of `fputc()` (which is what `printf()` ultimately calls) to make use of the UART. It also retargets `__sys_exit()` to sit in an infinite loop.
```C
#include <stdio.h>
#include "pl011_uart.h"

struct __FILE {
  int handle;
};

/* FILE is typedef’d in stdio.h. */

FILE __stdout;

// Useful defines for control/status registes
#define PL011_LCR_WORD_LENGTH_8   (0x60)
#define PL011_LCR_WORD_LENGTH_7   (0x40)
#define PL011_LCR_WORD_LENGTH_6   (0x20)
#define PL011_LCR_WORD_LENGTH_5   (0x00)

#define PL011_LCR_FIFO_ENABLE     (0x10)
#define PL011_LCR_FIFO_DISABLE    (0x00)

#define PL011_LCR_TWO_STOP_BITS   (0x08)
#define PL011_LCR_ONE_STOP_BIT    (0x00)

#define PL011_LCR_PARITY_ENABLE   (0x02)
#define PL011_LCR_PARITY_DISABLE  (0x00)

#define PL011_LCR_BREAK_ENABLE    (0x01)
#define PL011_LCR_BREAK_DISABLE   (0x00)

#define PL011_IBRD_DIV_38400      (0x27)
#define PL011_FBRD_DIV_38400      (0x09)

#define PL011_ICR_CLR_ALL_IRQS    (0x07FF)

#define PL011_FR_TXFF_FLAG        (0x20)
#define PL011_FR_RXFF_FLAG        (0x40)

#define PL011_CR_UART_ENABLE      (0x01)
#define PL011_CR_TX_ENABLE        (0x0100)
#define PL011_CR_RX_ENABLE        (0x0200)


struct pl011_uart {
        volatile unsigned int UARTDR;        // +0x00
        volatile unsigned int UARTECR;       // +0x04
  const volatile unsigned int unused0[4];    // +0x08 to +0x14 reserved
  const volatile unsigned int UARTFR;        // +0x18 - RO
  const volatile unsigned int unused1;       // +0x1C reserved
        volatile unsigned int UARTILPR;      // +0x20
        volatile unsigned int UARTIBRD;      // +0x24
        volatile unsigned int UARTFBRD;      // +0x28
        volatile unsigned int UARTLCR_H;     // +0x2C
        volatile unsigned int UARTCR;        // +0x30
        volatile unsigned int UARTIFLS;      // +0x34
        volatile unsigned int UARTIMSC;      // +0x38
  const volatile unsigned int UARTRIS;       // +0x3C - RO
  const volatile unsigned int UARTMIS;       // +0x40 - RO
        volatile unsigned int UARTICR;       // +0x44 - WO
        volatile unsigned int UARTDMACR;     // +0x48
};

// Instance of the dual timer
struct pl011_uart* uart;

// ------------------------------------------------------------

void uartInit(void* addr) {
  uart = (struct pl011_uart*) addr;

  // Ensure UART is disabled
  uart->UARTCR  = 0x0;

  // Set UART 0 Registers
  uart->UARTECR   = 0x0;  // Clear the recieve status (i.e. error) register
  uart->UARTLCR_H = 0x0 | PL011_LCR_WORD_LENGTH_8 | PL011_LCR_FIFO_DISABLE | PL011_LCR_ONE_STOP_BIT | PL011_LCR_PARITY_DISABLE | PL011_LCR_BREAK_DISABLE;

  uart->UARTIBRD = PL011_IBRD_DIV_38400;
  uart->UARTFBRD = PL011_FBRD_DIV_38400;

  uart->UARTIMSC = 0x0;                     // Mask out all UART interrupts
  uart->UARTICR  = PL011_ICR_CLR_ALL_IRQS;  // Clear interrupts

  uart->UARTCR  = 0x0 | PL011_CR_UART_ENABLE | PL011_CR_TX_ENABLE | PL011_CR_RX_ENABLE;
  
  return;
}

// ------------------------------------------------------------

int fputc(int c, FILE *f) {
  // Wait until FIFO or TX register has space
  while ((uart->UARTFR & PL011_FR_TXFF_FLAG) != 0x0) {}

  // Write packet into FIFO/tx register
  uart->UARTDR = c;

  // Model requires us to manually send a carriage return
  if ((char)c == '\n') {
    while ((uart->UARTFR & PL011_FR_TXFF_FLAG) != 0x0) {}
    uart->UARTDR = '\r';
  }
  return 0;
}

// ------------------------------------------------------------

void  __attribute__ ((noreturn)) _sys_exit(int x){
	while(1);
}
```
Create `pl011_uart.h` header file:
```C
#ifndef __uart_h
#define __uart_h

void uartInit(void* addr);
void uartSendString(const char*);

#endif
```
Modify `hello_world.c` to use the UART driver, and check that semihosting is no longer used:
```C
#include <stdio.h>
#include "pl011_uart.h"

__asm(".global __use_no_semihosting\n\t");

int main (void) {
  uartInit((void*)(0x1C090000));
  printf("Hello World!\n");
  return 0;
}
```
## Rebuild the example including the retargeted code:
```console
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a startup.s
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a hello_world.c
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a pl011_uart.c
armlink --scatter=scatter.txt --entry=start64 startup.o pl011_uart.o hello_world.o -o hello.axf
```
## Inspect the image
```console
fromelf --text -c hello.axf --output=disasm.txt
```
The disassembly in `disasm.txt` now shows no calls to `_sys_write`.

## Use telnet to interface with the UART

All output is now directed to the model's UART serial port.

We will now launch the simulation model with the newly compiled image. 
```console
FVP_Base_Cortex_A73x2_A53x4 -a hello.axf
```
You will see a telnet terminal pop-up when you run the simulation model with the output "Hello World!".

The code ends in an infinite loop (in the retargeted `__sys_exit()`), and so you must manually terminate (for example with `Ctrl+C`) the FVP.
