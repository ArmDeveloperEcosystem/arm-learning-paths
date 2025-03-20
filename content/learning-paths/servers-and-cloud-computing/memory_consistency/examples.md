---
# User change
title: "Thread Synchronization Examples"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Arm Instructions with Acquire-Release Ordering

Most of the examples below use the instructions `LDAR` and `STLR` which are load-acquire and store-release respectively. However, there are other instructions that support acquire-release ordering. More specifically, the various atomic instructions that were made mandatory as of Armv8.1. These include Compare and Swap (`CAS`), Swap (`SWP`), Load-Add (`LDADD`), Store-ADD (`STADD`), and more. We leave it as an exercise for the reader to explore these.

## Litmus7 Switches

Since `litmus7` executes code on the machine, it needs to build the assembly snippets into executable code. `litmus7` compiles with GCC, however, GCC uses default options. If running on an Arm Neoverse platform, we strongly recommend using the `-ccopts="-mcpu=native"` switch. This is the easiest way to avoid all possible run time failures. For example, if the Compare and Swap example below is executed without this switch, it will fail to run because by default, GCC will not emit the Compare and Swap instruction (`CAS`). This instruction is supported in Armv8.1, but GCC by default builds for Armv8.0. If in the future, the GCC default is updated to build for a newer version of the Arm architecture (e.g. Armv9.0). The `-ccopts` switch will not be needed to run tests that use atomic instructions like Compare and Swap (`CAS`).

## Example 1: Message passing without barriers

The first example highlights one of the pitfalls that may occur under a relaxed memory model.

```
AArch64 MP+Loop
{
0:X1=x; 0:X3=y;
1:X1=y; 1:X3=x;
}
  P0                 |  P1               ;
   MOV    W0,  #1    |L1:                ;
   STR    W0,  [X1]  |  LDR    W0,  [X1] ;
   MOV    W2,  #1    |  CBZ    W0,  L1   ;
   STR    W2,  [X3]  |  LDR    W2,  [X3] ;
exists
(1:X0=1 /\ 1:X2=0)
```
This example is similar to what we saw in the previous section, except this time we've added a loop to check for the message ready flag. If we think about this assembly in a Sequentially Consistent way, we can convince ourselves that the only valid outcome of these two threads executing will be `(1,1)`. Below is the output of this test with `herd7`.

```
Test MP+Loop Allowed
States 2
1:X0=1; 1:X2=0;
1:X0=1; 1:X2=1;
```
We see the outcome of `(1,0)`. Let's try `litmus7` on a Neoverse platform to see if it shows us the same outcomes.

```
Test MP+Loop Allowed
Histogram (2 states)
458   *>1:X0=1; 1:X2=0;
999542:>1:X0=1; 1:X2=1;
```
`litmus7` shows that most of the time we see the outcome `(1,1)`, but occasionally we see `(1,0)`. This result also highlights why we might want to increase the number of test iterations with `litmus7`. Notice that the `(1,0)` result is rare relative to the result of `(1,1)`. Increasing the number of test iterations will increase the probability that we see all outcomes, including those that are rare.

We see the outcome of `(1,0)` because `LDR` and `STR` are ordinary memory accesses. This means that if there are no dependencies between them (there aren't in this case), they can be reordered by the CPU. Both `herd7` and `litmus7` confirm that this can and will happen. The result of `(1,0)` is not desired because it represents reading the payload of a message before the ready flag is set. This is likely not what the programmer intended.

## Example 2: Message passing with two-way barriers

Let's fix the message passing by adding two-way barriers. Namely, the instruction `DMB` which is a data memory barrier.
```
AArch64 MP+Loop+DMB
{
0:X1=x; 0:X3=y;
1:X1=y; 1:X3=x;
}
  P0                 |  P1               ;
   MOV    W0,  #1    |L1:                ;
   STR    W0,  [X1]  |  LDR    W0,  [X1] ;
   DMB    ISH        |  CBZ    W0,  L1   ;
   MOV    W2,  #1    |  DMB    ISH       ;
   STR    W2,  [X3]  |  LDR    W2,  [X3] ;
exists
(1:X0=1 /\ 1:X2=0)
```
In this example we add the `DMB` instruction between the `STR` instructions in `P0`, and between the `LDR` instructions in `P1`. The `DMB` prevents the reordering of memory accesses across it. Note that non-memory access instructions can still be reordered across the `DMB`. For example, it's possible for the second `MOV` in `P0` to be executed before the `DMB` because it's not a memory access instruction. Also, on Arm, `DMB` instructions are Sequentially Consistent with respect to other `DMB` instructions.

Below is the `herd7` output of this test.

```
Test MP+Loop+DMB Allowed
States 1
1:X0=1; 1:X2=1;
...
Warning: File "test.litmus": unrolling limit exceeded at L1, legal outcomes may be missing.
```
Now that we have the memory barriers in place, we only see the outcome `(1,1)` which is what is desired for message passing between threads. When we run tests that contain loops with `herd7`, a warning will be shown. This warning appears because `herd7` is a simulator that interleaves instructions to figure out all possible outcomes. A consequence of it working this way means that it will unroll loops first, then test against the unrolled loops. By default, it unrolls loops two times. It is possible to increase this with with `-unroll` switch. That said, it doesn't seem useful to increase the number of unrolls unless there is some very specific and unusual sequencing occurring between the threads being tested. Overall, we strongly recommend that complex scenarios be broken into smaller and more primitive tests.

Below is the `litmus7` output of this test on a Neoverse platform.

```
Test MP+Loop+DMB Allowed
Histogram (1 states)
1000000:>1:X0=1; 1:X2=1;
```
100% of the test runs observed `(1,1)`. This builds confidence that our barriers are working.

A last point is that the `DMB` in `P1` can be relaxed by changing it to `DMB ISHLD`. This relaxation could potentially yield performance improvements in real applications. However, doing the same relaxation to the `DMB` in `P0` will break the message passing. We encourage readers to try this experiment and also read the Arm documentation on the differences between `DMB ISH`, `DMB ISHLD`, and `DMB ISHST`.

## Example 3: Message passing with One-Way Barriers

Let's test message passing with one-way barriers next. This is done by using instructions that support acquire-release ordering.

```
AArch64 MP+Loop+ACQ_REL
{
0:X1=x; 0:X3=y;
1:X1=y; 1:X3=x;
}
  P0                 |  P1               ;
   MOV    W0,  #1    |L1:                ;
   STR    W0,  [X1]  |  LDAR   W0,  [X1] ;
   MOV    W2,  #1    |  CBZ    W0,  L1   ;
   STLR   W2,  [X3]  |  LDR    W2,  [X3] ;
exists
(1:X0=1 /\ 1:X2=0)
```

In this example, we drop the `DMB` instructions and instead use a properly placed `STLR` in `P0` and `LDAR` in `P1`. `STLR` is a store-release instruction and `LDAR` is a load-acquire instruction. These are synchronizing memory accesses (as opposed to ordinary memory accesses). The `STLR` prevents earlier memory accesses from reordering after it, while the `LDAR` prevents later memory accesses from reordering before it. This is why these are also called one-way barriers; they block reordering only in one direction. `LDAR` and `STLR` instructions are Sequentially Consistent with respect to other `LDAR` and `STLR` instructions, while ordinary `LDR` and `STR` are not. There is also a more relaxed version of `LDAR` called `LDAPR`, this is a Load-Acquire with Processor Consistency. The Arm documentation on [Load-Acquire and Store-Release instructions](https://developer.arm.com/documentation/102336/0100/Load-Acquire-and-Store-Release-instructions) has more information on this.

Below is the `herd7` output of this test.

```
Test MP+Loop+ACQ_REL Allowed
States 1
1:X0=1; 1:X2=1;
```

We see the result we want. Only an outcome of `(1,1)` is possible.

Below is the `litmus7` output of this test on a Neoverse platform.
```\
Test MP+Loop+ACQ_REL Allowed
Histogram (1 states)
1000000:>1:X0=1; 1:X2=1;
```

`litmus7` shows us the same as `herd7`.

## Example 4: Compare and Swap with One-Way Barriers

Atomic instructions support acquire-release semantics. In this example we look at Compare and Swap with acquire ordering (`CASA`).

```
AArch64 Lock+Loop+CAS+ACQ_REL
{
y = 1;
0:X1=x; 0:X3=y;
1:X1=y; 1:X3=x;
}
  P0                 |  P1                    ;
   MOV    W0,  #1    |  MOV    W0,  #0        ;
   STR    W0,  [X1]  |  MOV    W4,  #1        ;
   MOV    W2,  #0    |L1:                     ;
   STLR   W2,  [X3]  |  CASA   W0,  W4,  [X1] ;
                     |  CBNZ   W0,  L1        ;
                     |  MOV    W0,  W4        ;
                     |  LDR    W2,  [X3]      ;
exists
(1:X0=1 /\ 1:X2=0)
```

This test is a representation of a basic spin lock. The lock variable is in address `y`. When it is set to 1, it's locked, when it's set to 0, it's available. This test starts with the lock variable at address `y` set to 1, which means it's locked. `P0` is assumed to be the owner of the lock at the start of the test. `P0` will write to address `x` (the payload), then release the lock by writing a 0 to address `y`. The store to address `y` is a `STLR` (store-release), this ensures that the write to the payload is visible before the release of the lock at address `y`. On `P1`, we spin on address `y` (the lock) with a `CASA`. At each loop iteration, `CASA` checks the value at address `y`. If it's 0 (available), then it will write a 1 to take ownership. If it's 1, the `CASA` fails and loops back to try the `CASA` again. It will continue to loop until it successfully takes the lock. The `CASA` instruction does this operation atomically, and with acquire ordering to ensure that the later `LDR` of address `x` (the payload) is not ordered before the `CASA`.

Below is the `herd7` output of this test.
```
Test Lock+Loop+CAS+ACQ_REL Allowed
States 1
1:X0=1; 1:X2=1;
```
We see the result we want. Only an outcome of `(1,1)` is possible.

Below is the `litmus7` output of this test on a Neoverse platform. Note that when we ran this, we used the switch `-ccopts="-mcpu=native"`. If we didn't, `litmus7` would fail with a message saying that the `CASA` instruction cannot be emitted by the compiler.
```
Test Lock+Loop+CAS+ACQ_REL Allowed
Histogram (1 states)
1000000:>1:X0=1; 1:X2=1;
```
Only an outcome of `(1,1)` has been observed. More test iterations can be executed to build confidence that this is the only possible result.

Try changing the `CASA` to a `CAS` (Compare and Swap with no ordering) to see what happens.

## Example 5: Dependency as a Barrier

It is possible to create barriers that are more relaxed than acquire-releases. This is done by creating dependencies between instructions that block the CPU's scheduler from reordering them. This is what the C/C++ ordering of `memory_order::consume` aims to achieve. However, over the years, it has been challenging for compilers to support this dependency based barrier concept. Thus,`memory_order::consume` gets upgraded to `memory_order::acquire` in practice. In fact, this ordering is in discussion to be dropped from the C/C++ standard. Still, it makes for an interesting example to show here.

To be able to show the difference, we first need to look at the one-way barrier example from before but with a modification. That modification is that we add a second payload memory address. We'll call it `w`. The new test with this additional memory location is shown below.

```
AArch64 MP+Loop+ACQ_REL2
{
0:X1=x; 0:X3=y; 0:X4=w;
1:X1=y; 1:X3=x; 1:X4=w;
}
  P0                 |  P1               ;
   MOV    W5,  #1    |L1:                ;
   STR    W5,  [X4]  |  LDAR   W0,  [X1] ;
   MOV    W0,  #1    |  CBZ    W0,  L1   ;
   STR    W0,  [X1]  |  LDR    W2,  [X3] ;
   MOV    W2,  #1    |  LDR    W5,  [X4] ;
   STLR   W2,  [X3]  |                   ;
exists
(1:X0=1 /\ (1:X2=0 \/ 1:X5=0))
```
On `P0`, we are writing to both `w` and `x` before we do the store-release on address `y`. This ensures that the writes to both `x` and `w` (the payloads) will be ordered before the write to address `y` (the flag). On `P1`, we loop with a load-acquire on address `y` (the flag). Once it is observed to be set, we load the two payload addresses. The load-acquire ensures that we do not read the payload addresses `w` and `x` until the flag is observe to be set. The condition at the bottom has been updated to check for any cases where either `w` or `x` are 0. Either of these being observed as 0 will be an indication of reading the payload before the ready flag is observed to be set (not what we want). Overall, this code should result in only the outcome `(1,1,1)`.

Below is the `herd7` output of this test.
```
Test MP+Loop+ACQ_REL2 Allowed
States 1
1:X0=1; 1:X2=1; 1:X5=1;
```

Below is the `litmus7` output of this test on a Neoverse platform.
```
Test MP+Loop+ACQ_REL2 Allowed
Histogram (1 states)
1000000:>1:X0=1; 1:X2=1; 1:X5=1;
```

Both `herd7` and `litmus7` show us the expected result. It might be worth increasing the number of iterations on `litmus7` to build more confidence in the result.

Now let's remove the load-acquire in `P1` and use a dependency as a barrier.
```
AArch64 MP+Loop+Dep
{
0:X1=x; 0:X3=y; 0:X4=w;
1:X1=y; 1:X3=x; 1:X4=w;
}
  P0                 |  P1                    ;
   MOV    W5,  #1    |L1:                     ;
   STR    W5,  [X4]  |  LDR    W0,  [X1]      ;
   MOV    W0,  #1    |  CBZ    W0,  L1        ;
   STR    W0,  [X1]  |  AND    W6,  W0,  WZR  ;
   MOV    W2,  #1    |  LDR    W2,  [X3, X6]  ;
   STLR   W2,  [X3]  |  LDR    W5,  [X4]      ;
exists
(1:X0=1 /\ (1:X2=0 \/ 1:X5=0))
```
What we've done to `P1` is create a dependency between the first `LDR` which is in the loop, and the second `LDR` which appears after the loop. Register `X6` (which is the same as `W6`) doesn't change the address loaded in the second `LDR` because the previous `AND` instruction zeros the offset. The point of the `AND` is to create a dependency between the first and second `LDR` instructions so that they execute in order. The net effect is that we have a barrier for the address `x` between the two `LDR` instructions. However, we do not have a barrier for the address `y`. In this way, it is a more relaxed barrier than using `LDAR`, because `LDAR` applies to all memory accesses that appear after it in program order.

Below is the `herd7` output of this test.
```
Test MP+Loop+Dep Allowed
States 2
1:X0=1; 1:X2=1; 1:X5=0;
1:X0=1; 1:X2=1; 1:X5=1;
```
The possible outcome of `(1,1,0)` makes sense because the dependency we've added doesn't cover the read of address `w`.

Below is the `litmus7` output of this test on a Neoverse platform.
```
Test MP+Loop+Dep Allowed
Histogram (2 states)
1     *>1:X0=1; 1:X2=1; 1:X5=0;
49999999:>1:X0=1; 1:X2=1; 1:X5=1;
```
We have the same result here too. However, notice that we had to execute the test 50 million times just to observe the reorder of the `LDR` of address `w` just one time. Again, if we don't do enough test iterations, we might miss the observation of a possible outcome.

## Experimentation Ideas

We encourage readers to modify and experiment with the example tests shared here. Readers can also create their own examples by using the assembly code generated from higher level languages. Last, there are also other litmus tests posted in the [herd7 online simulator](https://developer.arm.com/herd7)
