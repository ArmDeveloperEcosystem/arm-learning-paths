---
# User change
title: Switching Exception Levels

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
So far, everything has been at the most privileged `EL3` exception level, which the processor starts in at reset.

In general, you would want your application code to run at a lower level so that it cannot corrupt system settings, maliciously or otherwise.

Switching between levels is performed by the `ERET` exception return instruction.

## Changing exception levels

Extend the example to make use of `EL1`.

Create `startup_el1.s` as below. The `el1_entry` function will be the `EL1` entry point, and this function will call our application code starting from `__main()`.

#### startup_el1.s
```C
	.section  EL1_ENTRY,"ax"
	.global el1_entry
	.type el1_entry, "function"

el1_entry:
	LDR		x0, =vectors
	MSR		VBAR_EL1, x0	// Set EL1 Vector Table

	MOV		x0, #(0x3 << 20)
	MSR		CPACR_EL1, x0	// Disable instruction traps for EL1
	ISB

	.global  __main
	B        __main
```

## Modify EL3 initialization

You will also need to modify the `EL3` initialization from before:
* Create an `EL3` stack (as `__main` will now be called in `EL1`)
* Disable timer exceptions at `EL3`
* Execute any privileged code (`gicInit`)
* Set `EL1` execution state to be `Aarch64` (before entering `EL1`)
* Switch to `EL1` level

### EL3 stack
Create a new execution region `STACK_EL3` in the scatter file for the EL3 stack.
##### scatter.txt
```
	STACK_EL3 0x04020000 EMPTY 0x10000{}
```
The linker will generate a symbol `Image$$STACK_EL3$$ZI$$Limit` which can be referenced in code as follows:
#### startup_el3.s
```C
boot:
	// Set EL3 Stack pointer
	ADRP x0, Image$$STACK_EL3$$ZI$$Limit
	MOV  sp, x0
```

### SCR_EL3
In the code to set up [SCR_EL3](https://developer.arm.com/documentation/ddi0595/2021-06/AArch64-Registers/SCR-EL3--Secure-Configuration-Register), set the `ST` bit to disable timer exceptions, and the `RW` bit so that `EL1` executes in `Aarch64` state.

Also, remove the code to set the `FIQ` bit, as you now want to trap this exception in `EL1`.
#### startup_el3.s
```C
	// Configure SCR_EL3
	MOV  w1, #0
	ORR  w1, w1, #(1 << 11)  // set ST bit (disable trapping of timer control registers)
	ORR  w1, w1, #(1 << 10)  // set RW bit (next lower EL in aarch64)
	MSR  SCR_EL3, x1
```
### Perform other EL3 tasks
The code to initialize the `GIC` must be executed in `EL3`. Call `gicInit()` function before leaving `EL3`. This function sets the `NS` bit in `SCR_EL3`. Clear it here to avoid issues with [security settings](https://developer.arm.com/documentation/den0024/a/Security), which is beyond the scope of this article.

#### startup_el3.s
```C
// Initialize GIC
	BL	gicInit
	MRS      x1, SCR_EL3
	BIC      x1, x1, #1  // Clear NS bit
	MSR      SCR_EL3, x1
```
Remove the call to `gicInit()` from your `main()` function.
#### hello.c
```C
  // gicInit();
```

### Switch to EL1
Rather than branching to `__main`, the `EL3` reset handler must instead perform an exception return (`ERET`) to `EL1`. Set this up by configuring the appropriate registers:

* Initialize [SCTLR_EL1, System Control Register (EL1)](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/SCTLR-EL1--System-Control-Register--EL1-) so that `EL1` is in a known state
* Set [SPSR_EL3, Saved Program Status Register (EL3)](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/SPSR-EL3--Saved-Program-Status-Register--EL3-) so that the code will return to `EL1` exception level.
* Set [ELR_EL3, Exception Link Register (EL3)](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/ELR-EL3--Exception-Link-Register--EL3-?lang=en) with the address of the `EL1` entry point.

#### startup_el3.s
```C
// Switch to EL1
	MSR		SCTLR_EL1, xzr	// Initialize state of EL1

	MOV		x1, #0x5
	MSR		SPSR_EL3,x1		// Set return level to EL1

	LDR		x0, =el1_entry
	MSR		ELR_EL3, x0		// Set return address to EL1 entry point

	ISB						// Ensure all above fully executes before...
	ERET					// Returning to EL1
```
Delete the call to `__main()` in `EL3`.
```C
	.global  __main
	B        __main
```
Save your `startup_el3.s` file.

{{% notice %}}
The complete source for this file is provided as an [appendix](#appendix) below for reference.
{{% /notice %}}

## Build and run the example
You are now ready to rebuild the complete example as before:
```command
armclang -c -g --target=aarch64-arm-none-eabi startup_el3.s
armclang -c -g --target=aarch64-arm-none-eabi startup_el1.s
armclang -c -g --target=aarch64-arm-none-eabi uart.c
armclang -c -g --target=aarch64-arm-none-eabi vectors.s
armclang -c -g --target=aarch64-arm-none-eabi gic.s
armclang -c -g --target=aarch64-arm-none-eabi timer.s
armclang -c -g --target=aarch64-arm-none-eabi hello.c
armlink --scatter=scatter.txt --entry=el3_entry startup_el3.o startup_el1.o uart.o vectors.o gic.o timer.o hello.o -o hello.axf
```
```command
FVP_Base_AEMvA -C bp.refcounter.non_arch_start_at_default=1 -a hello.axf
```
The output is the same as before, though the exception level the code executes in is different.
```output
Hello World!
Waiting for interrupt...
Interrupt 29 occurred
Returned from interrupt!
In _sys_exit. Use Ctrl+C to quit.
```
## Appendix {#appendix}

#### startup_el3.s
```C
.section  BOOT,"ax"   // Define an executable ELF section, BOOT
	.global el3_entry
	.type el3_entry, "function"

el3_entry:
	MRS      x0, MPIDR_EL1		// Read Affinity register
	AND      x0, x0, #0xFFFF	// Mask off Aff0/Aff1 fields
	CBZ      x0, boot			// Branch to boot if Aff0/Aff1 are zero (Core 0 of Cluster 0)
sleep:							// Else put processor to sleep
	WFI
	B        sleep

boot:
	// Set EL3 Stack pointer
	ADRP x0, Image$$STACK_EL3$$ZI$$Limit
	MOV  sp, x0
	
	// Clear all trap bits
	MSR      CPTR_EL3, xzr
	
	// Configure SCR_EL3
	MOV  w1, #0
	ORR  w1, w1, #(1 << 11)		// set ST bit (disable trapping of timer control registers)
	ORR  w1, w1, #(1 << 10)		// set RW bit (next lower EL in aarch64)
	MSR  SCR_EL3, x1
	
	// Install vector table
	.global vectors
	LDR  x0, =vectors
	MSR  VBAR_EL3, x0
	ISB
	
	// Clear interrupt masks
	MSR  DAIFClr, #0xF
  
	// Initialize GIC
	BL	gicInit
	MRS      x1, SCR_EL3
	BIC      x1, x1, #1		// Clear NS bit
	MSR      SCR_EL3, x1

	// Switch to EL1
	MSR		SCTLR_EL1, xzr	// Initialize state of EL1

	MOV		x1, #0x5
	MSR		SPSR_EL3,x1		// Set return level to EL1

	LDR		x0, =el1_entry
	MSR		ELR_EL3, x0		// Set return address to EL1 entry point

	ISB						// Ensure all above fully executes before...
	ERET					// Returning to EL1
```
