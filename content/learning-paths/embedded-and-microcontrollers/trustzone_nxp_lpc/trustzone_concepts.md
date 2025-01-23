---
# User change
title: "Breaking down the application"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this section, the application is broken down to understand some basic concepts of TrustZone which include:

* Switching security states
* Calling secure functions from the non-secure world

## Switching security states

Start another debug session with the application. This time, instead of hitting "Run" and viewing the complete output you will walk through some key TrustZone concepts used in this application.
At the start of execution, the program counter is at the start of `main()` in `hello_world_s.c`. The secure mode copy of the startup code has already been executed right at reset time. 

In the `main()` function, board hardware initialization is performed followed by the first 2 `printf` statements you saw in the console output:

```output
PRINTF("Hello from secure world!\r\n");
PRINTF("Entering normal world.\r\n");
```
The Cortex-M33 processor on the NXP board is running in secure mode up to this point. After these prints, the `TZM_JumpToNormalWorld(NON_SECURE_START)` function is called which initiates the switch to the non-secure world. This function is defined in the `tzm_api.c` source file. This function sets up the non-secure main stack and vector table and gets a pointer to the non-secure reset handler with `__attribute__((cmse_nonsecure_call))`. This key attribute directs the compiler (Arm compiler for embedded in this example) to generate a `BLXNS` instruction. This instruction causes the processor to switch from secure to non-secure world.

## Call a secure function from non-secure world

Now that the processor has switched to non-secure mode it will not be able to access memory and peripherals of the secure world. The processor now executes the non-secure copy of the startup code and reaches the `main()` function of the `hello_world_ns.c` source file. 

Here again there are two key print statements which you previously saw in the output:

```output
PRINTF_NSE("Welcome in normal world!\r\n");
PRINTF_NSE("This is a test printed from the normal world!\r\n");
```
`PRINTF_NSE()` function is defined with `__attribute__((cmse_nonsecure_entry))`. This attribute is used to call the `PRINTF()` function. which is defined in secure mode. 
Using this attribute, a secure function can be called from the non-secure world. The functions executes an `SG` instruction which is a Secure Gateway instruction. Non-secure code can only call a secure function if the first instruction is a Secure Gateway instruction and it is in a non-secure callable memory region. If these rules are not followed during execution then it results in a security violation. 

You have now summarized some important attributes and instructions used while building TrustZone applications all using the simple hello world example on the NXP LPCXpresso55S69 board.
