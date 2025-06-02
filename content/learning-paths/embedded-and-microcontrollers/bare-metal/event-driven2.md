---
# User change
title: Create event-driven application (2)

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Vector tables have a relatively small and fixed number of entries. A real system will likely require many different interrupts, triggered by different sources. An additional piece of hardware is needed to manage these interrupts. The [Arm Generic Interrupt Controller, GIC](https://developer.arm.com/Architectures/Generic%20Interrupt%20Controller) does exactly this.

## Set up Generic Interrupt Controller (GIC)

Create `gic.s` with the following code to initialize the GICv3 implemented in the FVP, and define the timer as a source of interrupts.

For detail on this code, see the [GICv3 and GICv4 Software Overview](https://developer.arm.com/documentation/dai0492).

#### gic.s
```C
	.section GIC,"ax"
	.global gicInit
	.type gicInit, "function"

gicInit:
	// Configure Distributor
	MOV      x0, #0x2f000000	// GIC Distributor, GICD
	// Set ARE bits and group enables in the Distributor
	ADD      x1, x0, #0x0	// GICD_CTLROffset
	MOV      x2,     #0x20  // GICD_CTLR.ARE_NS
	ORR      x2, x2, #0x10  // GICD_CTLR.ARE_S
	STR      w2, [x1]
	
	ORR      x2, x2, #0x01	// GICD_CTLR.EnableG0
	ORR      x2, x2, #0x04	// GICD_CTLR.EnableG1S
	ORR      x2, x2, #0x02	// GICD_CTLR.EnableG1NS
	STR      w2, [x1]
	DSB      SY
	
	// Configure Redistributor
	// Clearing ProcessorSleep signals core is awake
	MOV      x0, #0x2f100000	// GIC Redistributor, RD_base
	MOV      x1, #0x14		// GICR_WAKERoffset
	ADD      x1, x1, x0
	STR      wzr, [x1]
	DSB      SY

waiting:   // Wait for ChildrenAsleep to read 0
	LDR      w0, [x1]
	AND      w0, w0, #0x6
	CBNZ     w0, waiting

	// Configure CPU interface
	// Set the SRE bits for each EL to enable
	// access to the interrupt controller registers
	MOV      x0, #0x8		// ICC_SRE_ELn.Enable
	ORR      x0, x0, #0x1	// ICC_SRE_ELn.SRE
	MSR      ICC_SRE_EL3, x0
	ISB
	
	MSR      ICC_SRE_EL1, x0
	MRS      x1, SCR_EL3
	ORR      x1, x1, #1		// Set NS bit, to access Non-secure registers
	MSR      SCR_EL3, x1
	ISB
	
	MSR      ICC_SRE_EL2, x0
	ISB
	
	MSR      ICC_SRE_EL1, x0
	
	MOV      w0, #0xFF
	MSR      ICC_PMR_EL1, x0 // Set PMR to lowest priority
	
	MOV      w0, #3
	MSR      ICC_IGRPEN1_EL3, x0
	MSR      ICC_IGRPEN0_EL1, x0

	// Secure Physical Timer source defined
	MOV      x0, #0x2f110000	// GIC Redistributor, SGI_base

	ADD      x1, x0, #0x80		// GICR_IGROUPRoffset
	STR      wzr, [x1]          // Mark INTIDs 0..31 as Secure
	
	ADD      x1, x0, #0xD00		// GICR_IGRPMODRoffset
	STR      wzr, [x1]          // Mark INTIDs 0..31 as Secure Group 0
	
	ADD      x1, x0, #0x100		// GICR_ISENABLERoffset
	MOV      w2, #(1 << 29)     // Enable INTID 29
	STR      w2, [x1]           // Enable interrupt source
		
	RET
```

## Other functions

Define these functions in your `gic.s` source:
* `readIAR0()` reads the value of the [Interrupt Controller Interrupt Acknowledge Register 0, ICC_IAR0_EL1](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/ICC-IAR0-EL1--Interrupt-Controller-Interrupt-Acknowledge-Register-0). The lower 24 bits of this register give the interrupt identifier, `INTID`.
* `writeEOIR0()` writes `INTID` to the [Interrupt Controller End of Interrupt Register 0, ICC_EOIR0_EL1](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/ICC-EOIR0-EL1--Interrupt-Controller-End-Of-Interrupt-Register-0), which tells the processor that that interrupt is complete.

#### gic.s
```C
// ------------------------------------------------------------
	.global readIAR0
	.type readIAR0, "function"
readIAR0:
	MRS       x0, ICC_IAR0_EL1  // Read ICC_IAR0_EL1 into x0
	RET

// ------------------------------------------------------------
	  .global writeEOIR0
	  .type writeEOIR0, "function"
writeEOIR0:
	MSR        ICC_EOIR0_EL1, x0 // Write x0 to ICC_EOIR0_EL1
	RET
```
These functions will be used in your `fiqHandler()` implementation (written in C).

## Generic Timer

A [Generic Timer](https://developer.arm.com/documentation/102379) is present in all Armv8-A processors.

Create `timer.s` defining the following functions:
* `setTimerPeriod()` which writes to [CNTPS_TVAL_EL1, Counter-timer Physical Secure Timer TimerValue register](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/CNTPS-TVAL-EL1--Counter-timer-Physical-Secure-Timer-TimerValue-Register).
* `enableTimer()` and `disableTimer()` which write to [CNTPS_CTL_EL1, Counter-timer Physical Secure Timer Control register](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/CNTPS-CTL-EL1--Counter-timer-Physical-Secure-Timer-Control-Register).

#### timer.s
```C
	.section  AArch64_GenericTimer,"ax"

	.global setTimerPeriod
	.type setTimerPeriod, "function"
setTimerPeriod:
	MSR     CNTPS_TVAL_EL1, x0
	ISB
	RET
// ------------------------------------------------------------
	.global enableTimer
	.type enableTimer, "function"
enableTimer:
	MOV    x0, #0x1            // Set Enable bit, and clear Mask bit
	MSR    CNTPS_CTL_EL1, x0
	ISB
	RET
// ------------------------------------------------------------
	.global disableTimer
	.type disableTimer, "function"
disableTimer:
	MSR    CNTPS_CTL_EL1, xzr // Clear the enable bit
	ISB
	RET
```
## Enable GIC and Timer

Modify `hello.c` to enable the GIC and timer, and create a simple test. You can use `printf()` statements to follow execution flow.

#### hello.c
```C
#include <stdio.h>
#include <stdint.h>

#include "uart.h"
__asm(".global __use_no_semihosting\n\t");

// defined in gic.s
extern void		gicInit(void);
extern uint32_t readIAR0(void);
extern void		writeEOIR0(uint32_t);

// defined in timer.s
extern void 	setTimerPeriod(uint32_t);
extern void 	enableTimer(void);
extern void 	disableTimer(void);

volatile uint32_t flag;

int main (void) {
  uartInit((void*)(0x1C090000));
  printf("Hello World!\n");

  flag = 0;
  gicInit();

  setTimerPeriod(0x10000);
  enableTimer();

  printf("Waiting for interrupt...\n");
  while(flag==0){};
  printf("Returned from interrupt!\n");
  
  return 0;
}
```
## Create fiqHandler()

Create the `fiqHandler()` function in `hello.c`. It reads the `INTID` register when triggered, disables the timer, and sets `flag`.

#### hello.c
```C
void fiqHandler(void) {
  uint32_t intid;
  intid = readIAR0(); // Read the interrupt id
  printf("Interrupt %d occurred\n", intid);

  if (intid == 29) {
    disableTimer();
	flag = 1;
  }
  else
	printf("Another interrupt occurred??\n");

  writeEOIR0(intid); // Clear interrupt
  return;
}
```

## Build and run the complete project

You are now ready to test the application. Build the project with:
```command
armclang -c -g --target=aarch64-arm-none-eabi startup_el3.s
armclang -c -g --target=aarch64-arm-none-eabi uart.c
armclang -c -g --target=aarch64-arm-none-eabi vectors.s
armclang -c -g --target=aarch64-arm-none-eabi gic.s
armclang -c -g --target=aarch64-arm-none-eabi timer.s
armclang -c -g --target=aarch64-arm-none-eabi hello.c
armlink --scatter=scatter.txt --entry=el3_entry startup_el3.o uart.o vectors.o gic.o timer.o hello.o -o hello.axf
```
To enable the timer in the FVP, add the `-C bp.refcounter.non_arch_start_at_default=1` option to the command line.
```command
FVP_Base_AEMvA -C bp.refcounter.non_arch_start_at_default=1 -a hello.axf
```
Observe the application reporting that the exception occurred.
```output
Hello World!
Waiting for interrupt...
Interrupt 29 occurred
Returned from interrupt!
In _sys_exit. Use Ctrl+C to quit.
```
