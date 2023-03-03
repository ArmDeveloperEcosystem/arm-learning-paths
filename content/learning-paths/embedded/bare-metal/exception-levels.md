---
# User change
title: Switching Exception Levels

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
So far, everything we have ran has been at the most privileged `EL3` exception level, which the processor starts in at reset. In general, you would want your application code to run at a lower level so that it cannot corrupt system settings, maliciously or otherwise. Switching between levels is performed by the `ERET` exception return instruction.

## Changing exception levels

We shall extend the example to make use of `El1`. In your `startup.s` source, add the following. `el1_entry` to be the `EL1` entry point, and continue to the `main()` function from there.
#### startup.s
```C
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

We will also need to modify the `EL3` initialization:
* Create an `EL3` stack (as `__main` will now be called in `EL1`)
* Disable timer exceptions at `EL3`
* Set `EL1` execution state to be `Aarch64`
* Execute priviledged code (`gicInit`) before switching to `EL1`
* Switch to `EL1` level

### EL3 stack
We will create a new execution egion `STACK_EL3` in our scatter file for the EL3 stack.
##### scatter.txt
```
	STACK_EL3 0x04020000 EMPTY 0x10000{}
```
We can reference this in our code as follows:
### startup.s
```C
boot:
	ADRP x0, Image$$STACK_EL3$$ZI$$Limit
	MOV  sp, x0
```
### SCR_EL3
In the code to set up [SCR_EL3](https://developer.arm.com/documentation/ddi0595/2021-06/AArch64-Registers/SCR-EL3--Secure-Configuration-Register), set the `ST` bit to disable timer exceptions, and the `RW` bit so that `EL1` executes in `Aarch64` state. Also, remove the code to set the `FIQ` bit, as we now want to trap this exception in `EL1`.
#### startup.s
```C
// Configure SCR_EL3
	MOV  w1, #0
	ORR  w1, w1, #(1 << 11)  // set ST bit (disable trapping of timer control registers)
	ORR  w1, w1, #(1 << 10)  // set RW bit (next lower EL in aarch64)
	MSR  SCR_EL3, x1
```
### Perform other EL3 tasks
The code to initialize the `GIC` must be executed in `EL3`. Call `gicInit()` function before leaving `EL3`. This function sets the `NS` bit in `SCR_EL3`. Clear it here to avoid issues with [security settings](https://developer.arm.com/documentation/den0024/a/Security), which is beyond the scope of this article.

#### startup.s
```C
	BL	gicInit
	MRS      x1, SCR_EL3
	BIC      x1, x1, #1  // Clear NS bit
	MSR      SCR_EL3, x1
```
Remove the call to `gicInit()` from your `main()` function.

### Switch to EL1
Rather than branching to `__main`, the `EL3` reset handler must instead perform an exception return (`ERET`) to `EL1`. This must be artificially set up by configuring the appropriate registers:

* Initialize [SCTLR_EL1, System Control Register (EL1)](https://developer.arm.com/documentation/ddi0595/latest/AArch64-Registers/SCTLR-EL1--System-Control-Register--EL1-) so that `El1` is in a known state
* Set [SPSR_EL3, Saved Program Status Register (EL3)](https://developer.arm.com/documentation/ddi0595/latest/AArch64-Registers/SPSR-EL3--Saved-Program-Status-Register--EL3-) so that the code will return to `EL1` exception level.
* Set [ELR_EL3, Exception Link Register (EL3)](https://developer.arm.com/documentation/ddi0595/latest/AArch64-Registers/ELR-EL3--Exception-Link-Register--EL3-) with the address of the `EL1` entry point.

#### startup.s
```C
	MSR		SCTLR_EL1, xzr	// Initialize state of EL1

	MOV		x1, #0x5
	MSR		SPSR_EL3,x1		// Set return level to EL1

	LDR		x0, =el1_entry_aarch64
	MSR		ELR_EL3, x0		// Set return address to EL1 entry point

	ISB						// Ensure all above fully executes before...
	ERET					// Returning to EL1
```
## Build and run the example
We are now ready to rebuild the complete example as before:
```command
armclang -c -g --target=aarch64-arm-none-eabi startup.s
armclang -c -g --target=aarch64-arm-none-eabi uart.c
armclang -c -g --target=aarch64-arm-none-eabi vectors.s
armclang -c -g --target=aarch64-arm-none-eabi gic.s
armclang -c -g --target=aarch64-arm-none-eabi timer.s
armclang -c -g --target=aarch64-arm-none-eabi hello.c
armlink --scatter=scatter.txt --entry=start64 startup.o uart.o vectors.o gic.o timer.o hello.o -o hello.axf
```
```command
FVP_Base_Cortex-A73x2-A53x4 -C bp.refcounter.non_arch_start_at_default=1 -a hello.axf
```

