---
title: Run MCA with Arm assembly
weight: 3
### FIXED, DO NOT MODIFY
layout: learningpathall
---
### MCA example with Arm assembly

You have learned what MCA is and what kind of information it provides. Now you are going to use MCA to identify a performance issue and improve a snippet of Arm assembly.

The example below demonstrates how to run `llvm-mca`, what the expected output is, and the conclusions you can draw using the performance metrics MCA provides.

The example below computes the sum of 6 numbers.

Use a text editor to save the program below in a file named `sum_test1.s`:

```
add x1, x1, x2
add x1, x1, x3
add x1, x1, x4
add x1, x1, x5
add x1, x1, x6
```

Now run `llvm-mca` on this code:

```console
llvm-mca -mtriple=aarch64  -mcpu=neoverse-v2 sum_test1.s
```

The printed output is similar to:

```output
Iterations:        100
Instructions:      500
Total Cycles:      503
Total uOps:        500

Dispatch Width:    16
uOps Per Cycle:    0.99
IPC:               0.99
Block RThroughput: 0.8


Instruction Info:
[1]: #uOps
[2]: Latency
[3]: RThroughput
[4]: MayLoad
[5]: MayStore
[6]: HasSideEffects (U)

[1]    [2]    [3]    [4]    [5]    [6]    Instructions:
 1      1     0.17                        add   x1, x1, x2
 1      1     0.17                        add   x1, x1, x3
 1      1     0.17                        add   x1, x1, x4
 1      1     0.17                        add   x1, x1, x5
 1      1     0.17                        add   x1, x1, x6


Resources:
[0.0] - V2UnitB
[0.1] - V2UnitB
[1.0] - V2UnitD
[1.1] - V2UnitD
[2]   - V2UnitL2
[3.0] - V2UnitL01
[3.1] - V2UnitL01
[4]   - V2UnitM0
[5]   - V2UnitM1
[6]   - V2UnitS0
[7]   - V2UnitS1
[8]   - V2UnitS2
[9]   - V2UnitS3
[10]  - V2UnitV0
[11]  - V2UnitV1
[12]  - V2UnitV2
[13]  - V2UnitV3


Resource pressure per iteration:
[0.0]  [0.1]  [1.0]  [1.1]  [2]    [3.0]  [3.1]  [4]    [5]    [6]    [7]    [8]    [9]    [10]   [11]   [12]   [13]
 -      -      -      -      -      -      -     0.83   0.83   0.83   0.83   0.84   0.84    -      -      -      -

Resource pressure by instruction:
[0.0]  [0.1]  [1.0]  [1.1]  [2]    [3.0]  [3.1]  [4]    [5]    [6]    [7]    [8]    [9]    [10]   [11]   [12]   [13]   Instructions:
 -      -      -      -      -      -      -     0.17   0.17   0.17   0.16   0.16   0.17    -      -      -      -     add      x1, x1, x2
 -      -      -      -      -      -      -     0.17   0.17   0.16   0.16   0.17   0.17    -      -      -      -     add      x1, x1, x3
 -      -      -      -      -      -      -     0.17   0.16   0.16   0.17   0.17   0.17    -      -      -      -     add      x1, x1, x4
 -      -      -      -      -      -      -     0.16   0.16   0.17   0.17   0.17   0.17    -      -      -      -     add      x1, x1, x5
 -      -      -      -      -      -      -     0.16   0.17   0.17   0.17   0.17   0.16    -      -      -      -     add      x1, x1, x6
```

The MCA output shows a lot of information. The most relevant parts are covered below. For further details, you can look at the [llvm-mca documentation](https://llvm.org/docs/CommandGuide/llvm-mca.html#how-llvm-mca-works).

The first part of the output, up to the `Instruction Info` section, is general information about the loop and the hardware. MCA simulated the execution of the code in a loop for 100 iterations. It executed a total of 500 instructions in 503 cycles. If you calculate the instructions per cycle (IPC), on average you get 500/503≈0.99 IPC. The dispatch width of 16 means the CPU is capable of dispatching 16 instructions per cycle.

The second part of the output, up to the `Resources` section, gives information about each individual instruction. Latency represents how many cycles each instruction takes to execute. Throughput represents the rate at which instructions are executed per cycle. Reciprocal throughput (RThroughput) is the inverse of throughput (1/throughput) and represents cycles per instruction.

An important part of this output is the `Resource pressure by instruction` section. It shows the instructions that are are executed on each pipeline. You can see that the add instructions use resources `[4]-[9]` and that pressure is equally spread through the available resources.

The [Arm Neoverse V2 Software Optimization Guide](https://developer.arm.com/documentation/109898/latest/) shows which pipelines are used by which instructions.

After going through the MCA output, you will conclude that the `sum_test1.s` program is not achieving the throughput the processor is capable of. It can only compute 1 instruction per cycle, despite putting a lot of pressure on resources `[4]-[9]`. 

In order to understand what causes this behavior, you can look into how the instruction state changes throughout the execution pipeline. 

Run again, this time with the `-timeline` flag:

```console
llvm-mca -mtriple=aarch64  -mcpu=neoverse-v2  -timeline sum_test1.s
```

The MCA output now includes a timeline view of execution to the output, which looks like this:

```output
Timeline view:
                    0123456789          0123456789          012
Index     0123456789          0123456789          0123456789

[0,0]     DeER .    .    .    .    .    .    .    .    .    . .   add   x1, x1, x2
[0,1]     D=eER.    .    .    .    .    .    .    .    .    . .   add   x1, x1, x3
[0,2]     D==eER    .    .    .    .    .    .    .    .    . .   add   x1, x1, x4
[0,3]     D===eER   .    .    .    .    .    .    .    .    . .   add   x1, x1, x5
[0,4]     D====eER  .    .    .    .    .    .    .    .    . .   add   x1, x1, x6
[1,0]     D=====eER .    .    .    .    .    .    .    .    . .   add   x1, x1, x2
[1,1]     D======eER.    .    .    .    .    .    .    .    . .   add   x1, x1, x3
[1,2]     D=======eER    .    .    .    .    .    .    .    . .   add   x1, x1, x4
[1,3]     D========eER   .    .    .    .    .    .    .    . .   add   x1, x1, x5
[1,4]     D=========eER  .    .    .    .    .    .    .    . .   add   x1, x1, x6
[2,0]     D==========eER .    .    .    .    .    .    .    . .   add   x1, x1, x2
[2,1]     D===========eER.    .    .    .    .    .    .    . .   add   x1, x1, x3
[2,2]     D============eER    .    .    .    .    .    .    . .   add   x1, x1, x4
[2,3]     D=============eER   .    .    .    .    .    .    . .   add   x1, x1, x5
[2,4]     D==============eER  .    .    .    .    .    .    . .   add   x1, x1, x6
[3,0]     D===============eER .    .    .    .    .    .    . .   add   x1, x1, x2
[3,1]     .D===============eER.    .    .    .    .    .    . .   add   x1, x1, x3
[3,2]     .D================eER    .    .    .    .    .    . .   add   x1, x1, x4
[3,3]     .D=================eER   .    .    .    .    .    . .   add   x1, x1, x5
[3,4]     .D==================eER  .    .    .    .    .    . .   add   x1, x1, x6
[4,0]     .D===================eER .    .    .    .    .    . .   add   x1, x1, x2
[4,1]     .D====================eER.    .    .    .    .    . .   add   x1, x1, x3
[4,2]     .D=====================eER    .    .    .    .    . .   add   x1, x1, x4
[4,3]     .D======================eER   .    .    .    .    . .   add   x1, x1, x5
[4,4]     .D=======================eER  .    .    .    .    . .   add   x1, x1, x6
[5,0]     .D========================eER .    .    .    .    . .   add   x1, x1, x2
[5,1]     .D=========================eER.    .    .    .    . .   add   x1, x1, x3
[5,2]     .D==========================eER    .    .    .    . .   add   x1, x1, x4
[5,3]     .D===========================eER   .    .    .    . .   add   x1, x1, x5
[5,4]     .D============================eER  .    .    .    . .   add   x1, x1, x6
[6,0]     .D=============================eER .    .    .    . .   add   x1, x1, x2
[6,1]     .D==============================eER.    .    .    . .   add   x1, x1, x3
[6,2]     . D==============================eER    .    .    . .   add   x1, x1, x4
[6,3]     . D===============================eER   .    .    . .   add   x1, x1, x5
[6,4]     . D================================eER  .    .    . .   add   x1, x1, x6
[7,0]     . D=================================eER .    .    . .   add   x1, x1, x2
[7,1]     . D==================================eER.    .    . .   add   x1, x1, x3
[7,2]     . D===================================eER    .    . .   add   x1, x1, x4
[7,3]     . D====================================eER   .    . .   add   x1, x1, x5
[7,4]     . D=====================================eER  .    . .   add   x1, x1, x6
[8,0]     . D======================================eER .    . .   add   x1, x1, x2
[8,1]     . D=======================================eER.    . .   add   x1, x1, x3
[8,2]     . D========================================eER    . .   add   x1, x1, x4
[8,3]     . D=========================================eER   . .   add   x1, x1, x5
[8,4]     . D==========================================eER  . .   add   x1, x1, x6
[9,0]     . D===========================================eER . .   add   x1, x1, x2
[9,1]     . D============================================eER. .   add   x1, x1, x3
[9,2]     . D=============================================eER .   add   x1, x1, x4
[9,3]     .  D=============================================eER.   add   x1, x1, x5
[9,4]     .  D==============================================eER   add   x1, x1, x6


Average Wait times (based on the timeline view):
[0]: Executions
[1]: Average time spent waiting in a scheduler's queue
[2]: Average time spent waiting in a scheduler's queue while ready
[3]: Average time elapsed from WB until retire stage

      [0]    [1]    [2]    [3]
0.     10    22.6   0.1    0.0       add        x1, x1, x2
1.     10    23.5   0.0    0.0       add        x1, x1, x3
2.     10    24.4   0.0    0.0       add        x1, x1, x4
3.     10    25.3   0.0    0.0       add        x1, x1, x5
4.     10    26.3   0.0    0.0       add        x1, x1, x6
       10    24.4   0.0    0.0       <total>
```

These states are represented by the following characters:
- D : Instruction dispatched.
- e : Instruction executing.
- E : Instruction executed.
- R : Instruction retired.
- = : Instruction already dispatched, waiting to be executed.
- \- : Instruction executed, waiting to be retired.

Looking at the `Index` in the timeline view, on the horizontal axis you have cycles and on the vertical axis you have a pair of indices representing iterations and instructions. Since you did not pass the `-timeline-max-iterations` flag to specify an iteration number to be used for the timeline view, `llvm-mca` used its default (10 iterations) so the iteration indices range from 0-9 inclusively. Since there are 5 instructions in `sum_test1`, the instruction indices range from 0-4 inclusively.

From the timeline view of `sum_test1.s` you can see the following:

- Instruction `[0, 4]` corresponds to the first iteration of the fifth instruction `add x1, x1, x6`. This instruction was dispatched on cycle 0, it started execution on cycle 5, finished execution at cycle 6 and retired at cycle 7.

- Instruction `[2, 2]` corresponds to the third iteration of the third instruction `add x1, x1, x4`. This instruction was dispatched on cycle 0, it started execution on cycle 13, finished execution at cycle 14 and retired at cycle 15.

The iterations timeline shows that in subsequent iterations, instructions spend a longer time waiting to start the execution. That is because all add instructions in the code block are in a Read After Write (RAW) dependency chain. 

Register x1 written by the first instruction `add x1, x1, x2` is immediately used by the next instruction `add x1, x1, x3` and so on. Long register dependencies negatively impact performance. The `Average Wait times` section of the timeline view also highlights this. The number of cycles spent in the ready state is very small compared to the number of cycles spent waiting in a scheduler's queue.

After analyzing the information provided by MCA, you now understand that a long chain of dependencies is affecting the performance of the program. 

With this understanding, you can write new assembly code to compute the sum of 6 numbers, this time avoiding register dependencies.

Use a text editor to save the program below in a file named `sum_test2.s`:

```
add x10, x1, x2
add x11, x3, x4
add x12, x5, x6
add x13, x10, x11
add x14, x12, x13
```

Run `llvm-mca` on the new program using:

```console
llvm-mca -mtriple=aarch64  -mcpu=neoverse-v2 sum_test2.s
```

The new output is shown below:

```output
Iterations:        100
Instructions:      500
Total Cycles:      88
Total uOps:        500

Dispatch Width:    16
uOps Per Cycle:    5.68
IPC:               5.68
Block RThroughput: 0.8


Instruction Info:
[1]: #uOps
[2]: Latency
[3]: RThroughput
[4]: MayLoad
[5]: MayStore
[6]: HasSideEffects (U)

[1]    [2]    [3]    [4]    [5]    [6]    Instructions:
 1      1     0.17                        add   x10, x1, x2
 1      1     0.17                        add   x11, x3, x4
 1      1     0.17                        add   x12, x5, x6
 1      1     0.17                        add   x13, x10, x11
 1      1     0.17                        add   x14, x12, x13


Resources:
[0.0] - V2UnitB
[0.1] - V2UnitB
[1.0] - V2UnitD
[1.1] - V2UnitD
[2]   - V2UnitL2
[3.0] - V2UnitL01
[3.1] - V2UnitL01
[4]   - V2UnitM0
[5]   - V2UnitM1
[6]   - V2UnitS0
[7]   - V2UnitS1
[8]   - V2UnitS2
[9]   - V2UnitS3
[10]  - V2UnitV0
[11]  - V2UnitV1
[12]  - V2UnitV2
[13]  - V2UnitV3


Resource pressure per iteration:
[0.0]  [0.1]  [1.0]  [1.1]  [2]    [3.0]  [3.1]  [4]    [5]    [6]    [7]    [8]    [9]    [10]   [11]   [12]   [13]
 -      -      -      -      -      -      -     0.83   0.83   0.83   0.83   0.84   0.84    -      -      -      -

Resource pressure by instruction:
[0.0]  [0.1]  [1.0]  [1.1]  [2]    [3.0]  [3.1]  [4]    [5]    [6]    [7]    [8]    [9]    [10]   [11]   [12]   [13]   Instructions:
 -      -      -      -      -      -      -     0.17   0.48   0.17   0.17    -     0.01    -      -      -      -     add      x10, x1, x2
 -      -      -      -      -      -      -     0.48   0.17   0.18   0.16   0.01    -      -      -      -      -     add      x11, x3, x4
 -      -      -      -      -      -      -     0.17   0.18   0.16   0.33   0.16    -      -      -      -      -     add      x12, x5, x6
 -      -      -      -      -      -      -      -      -     0.32   0.17   0.49   0.02    -      -      -      -     add      x13, x10, x11
 -      -      -      -      -      -      -     0.01    -      -      -     0.18   0.81    -      -      -      -     add      x14, x12, x13
```

You can immediately see an improvement in the performance of the program by looking a the number of total cycles it took to execute and the IPC. 

Below you can see a comparison between the MCA performance metrics of `sum_test1.s` and `sum_test2.s`:

|                   | sum_test1 | sum_test2 |
| ----------------- | --------- | --------- |
| Iterations        | 100       | 100       |
| Instructions      | 500       | 500       |
| Total Cycles      | 503       | 88        |
| Total uOps        | 500       | 500       |
| Dispatch Width    | 16        | 16        |
| uOps Per Cycle    | 0.99      | 5.68      |
| IPC               | 0.99      | 5.68      |
| Block RThroughput | 0.8       | 0.8       |

The improved version of the code now has a higher IPC and takes fewer cycles to run. 

You can also see that there is less pressure on resources `[4]-[9]`, which allows for instructions to execute in parallel.

Look at the timeline view and see how the lack of register dependencies improved performance. 

Run `llvm-mca` again using: 

```console
llvm-mca -mtriple=aarch64  -mcpu=neoverse-v2  -timeline sum_test2.s
```

The produced output is: 

```output
Timeline view:
                    012
Index     0123456789

[0,0]     DeER .    . .   add   x10, x1, x2
[0,1]     DeER .    . .   add   x11, x3, x4
[0,2]     DeER .    . .   add   x12, x5, x6
[0,3]     D=eER.    . .   add   x13, x10, x11
[0,4]     D==eER    . .   add   x14, x12, x13
[1,0]     DeE--R    . .   add   x10, x1, x2
[1,1]     DeE--R    . .   add   x11, x3, x4
[1,2]     DeE--R    . .   add   x12, x5, x6
[1,3]     D=eE-R    . .   add   x13, x10, x11
[1,4]     D==eER    . .   add   x14, x12, x13
[2,0]     D=eE-R    . .   add   x10, x1, x2
[2,1]     D=eE-R    . .   add   x11, x3, x4
[2,2]     D=eE-R    . .   add   x12, x5, x6
[2,3]     D==eER    . .   add   x13, x10, x11
[2,4]     D===eER   . .   add   x14, x12, x13
[3,0]     D=eE--R   . .   add   x10, x1, x2
[3,1]     .D=eE-R   . .   add   x11, x3, x4
[3,2]     .D=eE-R   . .   add   x12, x5, x6
[3,3]     .D==eER   . .   add   x13, x10, x11
[3,4]     .D===eER  . .   add   x14, x12, x13
[4,0]     .D=eE--R  . .   add   x10, x1, x2
[4,1]     .D==eE-R  . .   add   x11, x3, x4
[4,2]     .D==eE-R  . .   add   x12, x5, x6
[4,3]     .D===eER  . .   add   x13, x10, x11
[4,4]     .D====eER . .   add   x14, x12, x13
[5,0]     .D==eE--R . .   add   x10, x1, x2
[5,1]     .D==eE--R . .   add   x11, x3, x4
[5,2]     .D===eE-R . .   add   x12, x5, x6
[5,3]     .D===eE-R . .   add   x13, x10, x11
[5,4]     .D====eER . .   add   x14, x12, x13
[6,0]     .D===eE-R . .   add   x10, x1, x2
[6,1]     .D===eE-R . .   add   x11, x3, x4
[6,2]     . D===eER . .   add   x12, x5, x6
[6,3]     . D===eER . .   add   x13, x10, x11
[6,4]     . D====eER. .   add   x14, x12, x13
[7,0]     . D===eE-R. .   add   x10, x1, x2
[7,1]     . D===eE-R. .   add   x11, x3, x4
[7,2]     . D====eER. .   add   x12, x5, x6
[7,3]     . D====eER. .   add   x13, x10, x11
[7,4]     . D=====eER .   add   x14, x12, x13
[8,0]     . D====eE-R .   add   x10, x1, x2
[8,1]     . D====eE-R .   add   x11, x3, x4
[8,2]     . D====eE-R .   add   x12, x5, x6
[8,3]     . D=====eER .   add   x13, x10, x11
[8,4]     . D======eER.   add   x14, x12, x13
[9,0]     . D=====eE-R.   add   x10, x1, x2
[9,1]     . D=====eE-R.   add   x11, x3, x4
[9,2]     . D=====eE-R.   add   x12, x5, x6
[9,3]     .  D=====eER.   add   x13, x10, x11
[9,4]     .  D======eER   add   x14, x12, x13


Average Wait times (based on the timeline view):
[0]: Executions
[1]: Average time spent waiting in a scheduler's queue
[2]: Average time spent waiting in a scheduler's queue while ready
[3]: Average time elapsed from WB until retire stage

      [0]    [1]    [2]    [3]
0.     10    3.0    3.0    1.3       add        x10, x1, x2
1.     10    3.1    3.1    1.1       add        x11, x3, x4
2.     10    3.3    3.3    0.8       add        x12, x5, x6
3.     10    3.9    0.0    0.2       add        x13, x10, x11
4.     10    4.9    0.0    0.0       add        x14, x12, x13
       10    3.6    1.9    0.7       <total>
```

You can see by looking at the timeline view that instructions no longer depend on each other and can execute in parallel.

Instructions also spend less time waiting in the scheduler's queue. This explains why the performance of `sum_test2.s` is so much better than `sum_test1.s`.

Note the use of the flag `-mcpu=neoverse-v2` throughout all of those examples. This flag tells MCA to simulate the performance of the code in `sum_test1.s` and `sum_test2.s` on a Neoverse V2 core. This flag can be changed to any core supported in MCA. You can find what cores are supported in MCA by running `llvm-mca -mcpu=help <<<''`. You can also look at the LLVM sources in [llvm-project](https://github.com/llvm/llvm-project/tree/main/llvm/test/tools/llvm-mca/AArch64), which will give you more detailed examples. For instance, when looking at the Neoverse cores, there is currently support for the N1, N2, N3 and the V1, V2, V3 cores.

In the next section, you can try running `llvm-mca` with Compiler Explorer.
