---
# User change
title: Create event-driven application (1)

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Embedded systems typically monitor inputs waiting for an event, which then triggers a response by the system. You need to write code that listens for these events and acts on them. With Armv8-A, enable asynchronous exceptions (`IRQs`, `FIQs`, and `SErrors`) which are taken when the processor needs to handle an event outside to the current flow of execution.

For example, a thermostat might monitor room temperature until it drops below a specified threshold. When the threshold is reached, the system must turn on the heating system.

## Configure exception routing to EL3

This example will implement an FIQ. When this occurs, it will go to the highest exception level, `EL3`.

Modify `startup_el3.s` to extend the `boot` code to perform the following, before branching to `__main`.

### Enable exception routing to EL3

Configure the [SCR_EL3, Secure Configuration Register](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/SCR-EL3--Secure-Configuration-Register?lang=en) to route FIQ exceptions to `EL3`.
#### startup_el3.s
```C
// Configure SCR_EL3
	MOV  w1, #0
	ORR  w1, w1, #(1 << 2)   // Set FIQ bit (FIQs routed to EL3)
	MSR  SCR_EL3, x1
```
### Point to the exception vector table
Set the [VBAR_EL3, Vector Based Address Register](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/VBAR-EL3--Vector-Base-Address-Register--EL3-) to the location of the exception vector table. You will create `vectors` in the next section.
#### startup_el3.s
```C
// Install vector table
	.global vectors
	LDR  x0, =vectors
	MSR  VBAR_EL3, x0
	ISB
```
### Disable masking of exceptions at EL3 by PSTATE
Clear appropriate bits within [DAIF, Interrupt Mask Bits](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/DAIF--Interrupt-Mask-Bits).
#### startup_el3.s
```C
// Clear interrupt masks
	MSR  DAIFClr, #0xF
```
Save your `startup_el3.s` file.

## Create exception vector table

The [exception vector table](https://developer.arm.com/documentation/den0024/latest/AArch64-Exception-Handling/AArch64-exception-table) tells the processor what code to run in the event of an exception. The format of this table is fixed and architecturally defined.

Create `vectors.s` containing the following code.

{{% notice Note%}}
You will implement only the necessary FIQ exception for this example. A real system would need to implement all handlers.
{{% /notice %}}

#### vectors.s
```C
	.section VECTORS,"ax"
    .global vectors
	.balign 0x800
vectors:
	.space 0x100, 0x0		// Current EL with SP0
curr_el_sp0_fiq:
	B	fiqFirstLevelHandler
	.balign 0x80
	.space 0x80, 0x0

	.space 0x100, 0x0		// Current EL with SPx
curr_el_spx_fiq:
	B	fiqFirstLevelHandler
	.balign 0x80
	.space 0x80, 0x0

	.space 0x100, 0x0		// Lower EL using AArch64
lower_el_aarch64_fiq:
	B	fiqFirstLevelHandler
	.balign 0x80
	.space 0x80, 0x0

	.space 0x200, 0x0		// Lower EL using AArch32
```

## Create first level FIQ Handler

Each exception has a window of 0x80 bytes in the vector table area to use for its code. In this case you will simply branch to `fiqFirstLevelHandler`, which preserves all registers, before calling `fiqHandler()` (which shall be implemented later).

When `fiqHandler()` returns, undo the register preservation, before returning to where the code was before the exception occurred, using the `ERET` instruction.

Add the following to your `vectors.s`:
#### vectors.s
```C
	.global fiqHandler
fiqFirstLevelHandler:
	STP	x29, x30, [sp, #-16]!
	STP	x18, x19, [sp, #-16]!
	STP	x16, x17, [sp, #-16]!
	STP	x14, x15, [sp, #-16]!
	STP	x12, x13, [sp, #-16]!
	STP	x10, x11, [sp, #-16]!
	STP	 x8,  x9, [sp, #-16]!
	STP	 x6,  x7, [sp, #-16]!
	STP	 x4,  x5, [sp, #-16]!
	STP	 x2,  x3, [sp, #-16]!
	STP	 x0,  x1, [sp, #-16]!
	
	BL	fiqHandler
	
	LDP	 x0,  x1, [sp], #16
	LDP	 x2,  x3, [sp], #16
	LDP	 x4,  x5, [sp], #16
	LDP	 x6,  x7, [sp], #16
	LDP	 x8,  x9, [sp], #16
	LDP	x10, x11, [sp], #16
	LDP	x12, x13, [sp], #16
	LDP	x14, x15, [sp], #16
	LDP	x16, x17, [sp], #16
	LDP	x18, x19, [sp], #16
	LDP	x29, x30, [sp], #16

	ERET
```
