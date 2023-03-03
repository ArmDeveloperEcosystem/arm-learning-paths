---
# User change
title: Create event-driven application (1)

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Embedded systems typically monitor inputs waiting for an event, which then triggers a response by the system. You need to write code that listens for these events and acts on them. With Armv8-A we enable asynchronous exceptions (`IRQs`, `FIQs`, and `SErrors`) which are taken when the processor needs to handle an event outside to the current flow of execution.

For example, a thermostat might monitor room temperature until it drops below a specified threshold. When the threshold is reached, the system must turn on the heating system.

## Configure exception routing to EL3

To keep things simple, this guide will specify that all exceptions are taken at the highest exception level, `EL3`.

Modify `startup.s` to extend the reset handler (`boot`) to perform the following before branching to `__main`.

### Enable exception routing to EL3

Configure the [SCR_EL3, Secure Configuration Register](https://developer.arm.com/documentation/ddi0595/2021-12/AArch64-Registers/SCR-EL3--Secure-Configuration-Register).

```C
// Configure SCR_EL3
  MOV  w1, #0              // Initial value of register is unknown
  ORR  w1, w1, #(1 << 3)   // Set EA bit (SError routed to EL3)
  ORR  w1, w1, #(1 << 2)   // Set FIQ bit (FIQs routed to EL3)
  ORR  w1, w1, #(1 << 1)   // Set IRQ bit (IRQs routed to EL3)
  MSR  SCR_EL3, x1
```
### Point to the exception vector table
Set the [VBAR_EL3, Vector Based Address Register](https://developer.arm.com/documentation/ddi0595/2021-12/AArch64-Registers/VBAR-EL3--Vector-Base-Address-Register--EL3-). We will create `vectors` in the next section.
```C
  // Install vector table
  .global vectors
  LDR  x0, =vectors
  MSR  VBAR_EL3, x0
  ISB
```
### Disable masking of exceptions at EL3 by PSTATE
Clear appropriate bits within [DAIF, Interrupt Mask Bits](https://developer.arm.com/documentation/ddi0595/2021-12/AArch64-Registers/DAIF--Interrupt-Mask-Bits).
```C
  // Clear interrupt masks
  MSR  DAIFClr, #0xF
```

## Create exception vector table

The [exception vector table](https://developer.arm.com/documentation/den0024/latest/AArch64-Exception-Handling/AArch64-exception-table) tells the processor what code to run in the event of an exception. The format of this table is fixed and architecturally defined.

Create `vectors.s` containing the following code. We will implement only the necessary handler for this example. A real system would need to implement all handlers.

### vectors.s
```C
   .section VECTORS,"ax"
   .align 12
    .global vectors
vectors:
	.space 0x300, 0x0
fiq_current_el_spx:
   B	fiqFirstLevelHandler
	.balign 0x80
	.space 0x480, 0x0
```

## Create first level FIQ Handler

The FIQ exception vector in fact branches to `fiqFirstLevelHandler`, which preserves all registers, before calling the main handler code, `fiqHandler` (which we shall implement later). When `fiqHandler` returns, we undo the register preservation, before returning to where the code was before the exception occured, using the `ERET` instruction.

Add the following to your `vectors.s`.
```C
   .global fiqHandler
fiqFirstLevelHandler:
	STP      x29, x30, [sp, #-16]!
	STP      x18, x19, [sp, #-16]!
	STP      x16, x17, [sp, #-16]!
	STP      x14, x15, [sp, #-16]!
	STP      x12, x13, [sp, #-16]!
	STP      x10, x11, [sp, #-16]!
	STP      x8, x9, [sp, #-16]!
	STP      x6, x7, [sp, #-16]!
	STP      x4, x5, [sp, #-16]!
	STP      x2, x3, [sp, #-16]!
	STP      x0, x1, [sp, #-16]!
	
	BL       fiqHandler
	
	LDP      x0, x1, [sp], #16
	LDP      x2, x3, [sp], #16
	LDP      x4, x5, [sp], #16
	LDP      x6, x7, [sp], #16
	LDP      x8, x9, [sp], #16
	LDP      x10, x11, [sp], #16
	LDP      x12, x13, [sp], #16
	LDP      x14, x15, [sp], #16
	LDP      x16, x17, [sp], #16
	LDP      x18, x19, [sp], #16
	LDP      x29, x30, [sp], #16

	ERET
```
