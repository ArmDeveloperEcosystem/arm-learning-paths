---
# User change
title: "Modify the example to use the UART for printf output"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
You have been using `printf()` to output your message. A mechanism called [semihosting](https://developer.arm.com/documentation/100966/latest/Getting-Started-with-Fixed-Virtual-Platforms/FVP-debug) was used to handle this output. While this is supported in the FVP, it would not be available on real hardware (without a debugger being present), and so execution would simply stop when the `HLT` instruction that is used by the debugger/FVP to detect semihosting is executed.

Modify the example to send output to the [PL011 UART](https://developer.arm.com/documentation/ddi0183) of the FVP.

You can check if you are using semihosting by importing the symbol `__use_no_semihosting` to your project.

Modify `hello.c` to import the symbol:
#### hello.c
```C
#include <stdio.h>
__asm(".global __use_no_semihosting\n\t");

int main(void) {
  printf("Hello World!\n");
  return 0;
}
```
Rebuild the example:
```command
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a hello.c
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a startup_el3.s
armlink --scatter=scatter.txt hello.o startup_el3.o -o hello.axf --entry=el3_entry
```
The linker will error for any functions that use semihosting:
```output
Error: L6915E: Library reports error: __use_no_semihosting was requested, but _sys_exit was referenced
Error: L6915E: Library reports error: __use_no_semihosting was requested, but _sys_open was referenced
Error: L6915E: Library reports error: __use_no_semihosting was requested, but _ttywrch was referenced
```

## Retarget fputc to use the UART

Many library functions depend on semihosting. You must retarget these functions to use the hardware of the target instead of the host system.

Copy and paste the following code into a new file `uart.c`.

This contains code to initialize the UART (`uartInit()`), and a retargeted version of `fputc()` (which is called by `printf()` and other functions) to write to the UART directly, not via the semihosted `_ttywrch()` function.

#### uart.c
```C
#include <stdio.h>
#include "uart.h"

/* FILE is typedef’d in stdio.h. */
struct __FILE {
  int handle;
};
FILE __stdout;


struct pl011_uart* uart;

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

void  __attribute__ ((noreturn)) _sys_exit(int x){
	printf("In _sys_exit. Use Ctrl+C to quit.\n");
	while(1);
}
```
{{% notice __sys_exit%}}
The source also retargets `__sys_exit()` as an infinite while loop.

Typically an embedded application will never return.
{{% /notice %}}

Create `uart.h` containing various macros used above. This code is taken from extended examples supplied with Arm Development Studio.
#### uart.h
```C
#ifndef __uart_h
#define __uart_h

void uartInit(void* addr);
// void uartSendString(const char*);

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

#endif
```
### Modify hello.c

Modify `hello.c` to initialize the UART before any messages are printed. From the [memory map](https://developer.arm.com/documentation/100964/latest/Base-Platform/Base---memory/Base-Platform-memory-map), `UART0` is located at `0x1C090000`.

#### hello.c
```C
#include <stdio.h>
#include "uart.h"

__asm(".global __use_no_semihosting\n\t");

int main (void) {
  uartInit((void*)(0x1C090000));
  printf("Hello World!\n");
  return 0;
}
```
No changes are needed to the scatter file. The additional code will be placed by the catch-all `* (+RO)` line.

## Rebuild the example including the retargeted code:
```console
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a startup_el3.s
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a hello.c
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a uart.c
armlink --scatter=scatter.txt --entry=el3_entry startup_el3.o uart.o hello.o -o hello.axf
```
The application now builds without linker errors.

## Run the example on the FVP

Launch the simulation model with the newly built image. 
```console
FVP_Base_AEMvA -a hello.axf
```
All `printf()` output is now directed to `UART0` of the FVP.

You will see a terminal pop-up with the output:
```output
Hello World!
In _sys_exit. Use Ctrl+C to quit.
```

{{% notice Telnet Client%}}
Windows users may need to first [enable Telnet Client](https://social.technet.microsoft.com/wiki/contents/articles/38433.windows-10-enabling-telnet-client.aspx) to see the output message.
{{% /notice %}}


The code ends in an infinite loop (in the retargeted `__sys_exit()`), and so you must manually terminate (for example with `Ctrl+C`) the FVP.
