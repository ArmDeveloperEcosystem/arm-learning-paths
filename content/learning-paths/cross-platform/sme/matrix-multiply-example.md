---
title: Matrix multiply example
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

A single-precision floating-point matrix multiply (vector length agnostic) bare-metal example to illustrate Scalable Matrix Extension (SME) is provided with Arm Development Studio, 2023.0 and later.

The example shows a reference C implementation compared to an optimized version in assembler using SME2 instructions.

The example builds with Arm Compiler for Embedded 6, executes on the Arm Architecture Envelope Model for A-class (AEMvA) Fixed Virtual Platform (FVP) model, and can be run/debugged with the Arm Debugger.

The compiler, FVP model, and debugger are all provided in Arm Development Studio.

## Import the example

Open the Arm Development Studio IDE. Navigate to `File` > `Import...` > `Arm Development Studio` > `Examples & Programming Libraries` > `Examples` > `Armv9 Bare-Metal`, and select the `sme2_matmul_fp32` example. Using the text filter at the top of the pane can help locate the example. Click `Finish` to import.

Alternatively extract the example on the command line from the `<install_dir>\examples\Bare-metal_examples_Armv9.zip` archive. For interactive debug (see later) using the IDE is recommended.

Though the project is provided pre-compiled, you can also rebuild with the `Build` icon, or the `make` command from the command line.

The example is compiled with `-march=armv9-a+sme2`, as set in the `makefile`.

See the supplied `readme.html` for more information.

## Load the example

There is a supplied `sme2_matmul_fp32.launch` debug connection which has all necessary settings configured.

Double-click on the `.launch` file to open.

The AEMvA FVP model is a generic Arm implementation, which can be configured appropriately to enable Arm architectural features.

The model is launched with appropriate settings to implement full SME2 support, including:

`-C SVE.ScalableVectorExtension.has_sme=1 -C SVE.ScalableVectorExtension.has_sme2=1 -C SVE.ScalableVectorExtension.sme_veclens_implemented=7`

The `has_sme=1` and `has_sme2=1` parameters enable support for SME and SME2 respectively.

The `sme_veclens_implemented` parameter sets which SME vector lengths are implemented in the model.  This is represented as a bitfield where bit[n]==1 implies a vector length of 128*2^n bits is implemented.  The default `sme_veclens_implemented=7` means vector lengths of 128, 256, and 512 are supported.  You can change this to fix a particular vector length by setting, for example, `sme_veclens_implemented=2` for 256 bits.
The vector length can also be read by software at run-time using the `RDSVL` instruction (see later).

For more information on the model parameters, launch the model with `FVP_Base_AEMvA --list-params`

Click `Debug` to launch the FVP and load the image.

Execution can be controlled by the `Debug Control` pane icon bar (eg `Step Instruction` ), the command line (`stepi`), or short-cut keys (`F5`).

## Understand the example

![example image alt-text#center](/learning-paths/cross-platform/sme/armds_sme2.png "Figure 2. Debugging the SME2 example in Arm Development Studio")

1. In the Registers view, expand AArch64 > System > ID > ID_AA64PFR1_EL1. Notice the SME bits are set to 2, meaning the SME2 architectural state and programmers model are implemented on this target.
2. This bit can also be inspected in the Commands view, by entering `output $AArch64::$System::$ID::$ID_AA64PFR1_EL1.SME`. Other bits in other registers may be inspected similarly.
3. In the Registers view, expand AArch64 > System > PSTATE > SVCR. Notice the ZA bit is currently 0, meaning the ZA array storage is invalid and not accessible. This will change to 1 later, when an SMSTART instruction is executed.
4. In `main.c`, observe that `main()` initializes the sizes (M, N, K) of the matrices, prints a welcome banner, then disables SVE and SIMD traps.
5. Set a breakpoint on the `disable_sve_traps` function with `break disable_sve_traps` and run to it (press F8). It is written in assembler.
6. In the Registers view, expand AArch64 > System > Secure > CPTR_EL3. To avoid SME, SVE, or SIMD instructions being trapped, the ESM and EZ bits must be set to 1 and the TFP bit must be cleared to 0, respectively, in CPTR_EL3. These bits reset to an architecturally unknown value on startup.
7. In the Debug Control view, select Stepping By Instruction (press F10) to switch stepping mode to instruction level.
8. Single-step (press F5) over the MRS, BIC, ORR, MSR, ISB instructions, and observe those bits are set/cleared as required.
9. The vector length is read at run-time using an `RDSVL` instruction.  To see this, set a breakpoint on `sve_cntw()` with `break sve_cntw` and run to it (press F8).  Single-step (press F5) the `RDSVL` instruction.  The value returned by `RDSVL` in the specified register is SVL DIV 8.
10. In the Debug Control view, select Stepping By Source (press F10) to switch stepping mode back to C source level.
11. The C code then initializes the matLeft and matRight arrays with random single-precision floating-point values. The input (and result) matrices are stored in memory in a row-major memory layout. To see the input values matLeft and matRight, set a breakpoint on the call to matmul() on line 85 and run to it (press F8). Open the Memory view, select Xn (Format) > Float > 4 bytes, then enter either matLeft or matRight in the address field (top-left text entry box).
12. The C code then calls two functions, `matmul()` and `matmul_opt()`, to multiply the matLeft and matRight values. `matmul()` is a generic reference C implementation. `matmul_opt()` is an optimized version in assembler using SME2 instructions.
13. Set a breakpoint on `matmul()` with `break matmul` and run to it (press F8). In the Registers view, expand AArch64 > Core, and note the value of X5. Parameters are passed here in registers, so X5 (6th parameter) will contain the address where the matResult will be stored.
14. In the Disassembly view, notice that the inner loop calculations are performed using FMADD instructions on the SIMD single-precision registers S0, S1, S2.
15. In the Registers view, expand AArch64 > SIMD > Single.
16. In the Disassembly view, set a breakpoint on the FMADD instruction and run to it (press F8), and see the SIMD single-precision registers S0, S1, S2 changing. Run again and again.
17. Delete the breakpoint on the FMADD instruction, then step-out of the function (press F7) back into main().
18. To see the result matResult, in the Memory view, enter the previously noted address from X5 in the address field.
19. Set a breakpoint on `matmul_opt()` with `break matmul_opt` and run to it (press F8). The optimized SME2 assembler is displayed in the Editor and Disassembly views.
20. In the Registers view, expand AArch64 > Core, and again note the value of X5, which will now contain the address where the matResult_opt will be stored.
21. In the Registers view, expand AArch64 > System > PSTATE > SVCR. Notice the ZA and SM bits are still 0.
22. Single-step (press F5) up to and over the SMSTART instruction, and see the ZA changing to 1, meaning the ZA array storage is now valid and accessible.
23. Set a breakpoint on the first instruction (`fmopa za2.s ...`) in `.Loop_K` at line 124 and run to it (press F8). This instruction performs a floating-point outer product and accumulate, putting the result in tile ZA2.
24. To see a full description of this instruction, or any other instruction in this example, simply hover the mouse over the instruction, in either the Editor or Disassembly views.
25. In the Registers view, expand AArch64 > SME > Tiles > ZA2H_S > F32 > [0]. This shows the contents of the zeroth row ('H') of tile ZA2 as floats, initially all zero.
26. In the Registers view, expand AArch64 > SME > Tiles > ZA2V_S > F32 > [0]. This shows the contents of the zeroth column ('V') of tile ZA2 as floats, also initially all zero.
27. Double-click on ZA2H_S.F32[0][0], and change its value to e.g. 99. Notice that ZA2V_S.F32[0][0] changes to the same value, because the zeroth element of the zeroth column is the same as the zeroth element of the zeroth row (the top-left element of the matrix).
28. In the Commands view, notice that the equivalent command is also shown, e.g. `set var $AARCH64::$SME::$Tiles::$ZA2H_S.F32[0][0] = 99`. This may be abbreviated to `set $ZA2H_S.F32[0][0] = 99`.
29. Single-step (press F5) to execute the `fmopa` instruction. Notice the values in ZA2H_S.F32[0] and ZA2V_S.F32[0] have updated.
30. Run again and again to see the values changing. You can do the same for ZA0, ZA1, etc.
31. The contents of the tile may also be viewed in the Commands view using the CLI, for example:
    To view the zeroth element of the zeroth row, enter `output $ZA2H_S.F32[0][0]`.
    To view all elements of the zeroth row, enter `output $ZA2H_S.F32[0]`.
    To view all elements of the zeroth column, enter `output $ZA2V_S.F32[0]`.
    To view the whole tile (as rows), enter `output $ZA2H_S.F32`.
    To view the whole tile (as columns), enter `output $ZA2V_S.F32`.
    Sequences of commands such as these may be easily scripted to construct groups of automated tests.
32. Delete all breakpoints, then set a breakpoint on the first instruction (`st1w {za0h.s[w13, #0]}, p4, [x10]`) in `.Ktail_end` at line 176 and run to it (press F8). This instruction stores words from ZA0, from the row in w13 to memory at the address in x10.
33. In the Commands view, enter `output /x $ZA0H_S.F32[$w13]` to show the w13th row of ZA0 in hexadecimal.
34. In the Commands view, enter `x /16 $x10` to show the memory at x10, or open a Memory view and enter x10 in the starting address field.
35. Single-step (press F5) to execute the st1w instruction.
36. In the Commands view, enter `x /16 $x10` again to show the memory at x10. Notice in the Commands view or the Memory view that the memory has been loaded with the content of the w13th row of ZA0.
37. Delete all breakpoints, then step-out of the function (press F7) back into main().
38. To see the result matResult_opt, in the Memory view, enter the previously noted address from X5 in the address field.
39. Continue running until the example completes normally.
