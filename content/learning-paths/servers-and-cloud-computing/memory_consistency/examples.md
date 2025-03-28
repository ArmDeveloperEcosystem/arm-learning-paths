---
# User change
title: "Thread Synchronization Examples"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Arm Instructions that Support Acquire-Release Ordering

This section focuses on examples that use the instructions `LDAR` (load-acquire) and `STLR` (store-release). However, these are not the only instructions that support acquire-release ordering. 

Starting with Armv8.1 of the Armv8-A architecture profile, several atomic instructions became mandatory. Examples include Compare and Swap (`CAS`), Swap (`SWP`), Load-Add (`LDADD`), and Store-Add (`STADD`). 

{{% notice Learning Tip %}}
Though these other atomic instructions are outside the scope of this Learning Path, you can go on to investigate these further yourself. See the Additional Resources section at the end.
{{% /notice %}}

## Litmus7 Switches

As `litmus7` executes code on a machine, it first needs to build the assembly snippets into executable code. By default, `litmus7` compiles with GCC's standard options. When you run on an Arm Neoverse platform however, it is strongly recommended that you use the switch `-ccopts="-mcpu=native"`. This is the simplest way to avoid all possible runtime failures. 

For example, if you execute the Compare and Swap example below without this switch, it will fail to run because GCC by default, does not emit the Compare and Swap (`CAS`) instruction. Although `CAS` is supported in Armv8.1 of the Arm architecture, GCC still defaults to Armv8.0. In the future, if  GCC updates its default to target a newer version of the Arm architecture (for example, Armv9.0), the `-ccopts` switch will no longer be necessary for tests that use atomic instructions like `CAS`.

## Example 1: Message Passing without Barriers

The first example highlights one of the pitfalls that can occur under a relaxed memory model.

To try it out, create a litmus file named `test1.litmus` with the content shown below:

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
This example is similar to what you saw in the previous section, except now there is a loop to check for the "message ready" flag. If you think about this assembly in a Sequentially Consistent way, you might conclude that the only valid outcome of these two threads executing will be `(1,1)`. 

Run the following command to test this with `herd7`:

```bash
herd7 ./test1.litmus
```

The output should look like:

```output
Test MP+Loop Allowed
States 2
1:X0=1; 1:X2=0;
1:X0=1; 1:X2=1;
```
You should see the outcome of `(1,0)`. 

Now try to run this same test with `litmus7` on your Arm Neoverse instance to see if you get the same outcomes:

```bash
litmus7 ./test1.litmus
```

The output should look like this:

```output
Test MP+Loop Allowed
Histogram (2 states)
458   *>1:X0=1; 1:X2=0;
999542:>1:X0=1; 1:X2=1;
```
Here `(1,1)` is by far the most common result, but `(1,0)` still appears occasionally. This highlights the benefit of increasing the number of test iterations when using `litmus7`:doing so increases the probability of observing all outcomes, including those that happen rarely.

You will see the `(1,0)` outcome because `LDR` and `STR` are ordinary memory accesses. When there are no dependencies between them, as in this example, the CPU can reorder these operations. Both `herd7` and `litmus7` confirm that this reordering can, and will, happen. The `(1,0)` result is undesirable because it indicates the message payload is read before the ready flag is set. This is likely not what the programmer intended.

## Example 2: Message Passing With Two-Way Barriers

You can fix the message passing by adding two-way barriers through a data memory barrier (`DMB`).
Create a litmus file called `test2.litmus` with the following contents:

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
In this example you added the `DMB` instruction between the `STR` instructions in `P0`, and between the `LDR` instructions in `P1`. The `DMB` prevents memory accesses from reordering across it. Note that non-memory access instructions can still be reordered across the `DMB`. For example, it's possible for the second `MOV` in `P0` to be executed before the `DMB` because it's not a memory access instruction. Also, on Arm, `DMB` instructions are Sequentially Consistent with respect to other `DMB` instructions.

Run this test with `herd7`:
```bash
herd7 test2.litmus
```

The output will look like:

```output
Test MP+Loop+DMB Allowed
States 1
1:X0=1; 1:X2=1;
...
Warning: File "test.litmus": unrolling limit exceeded at L1, legal outcomes may be missing.
```
Now that you have the memory barriers in place, you only see the outcome `(1,1)` which is what you want for message passing between threads. When you run tests that contain loops with `herd7`, a warning will be shown. This warning appears because `herd7` is a simulator that interleaves instructions to figure out all possible outcomes. A consequence of it working this way means that it will unroll loops first, then test against the unrolled loops. By default, it unrolls loops twice. You can increase this with the `-unroll` switch. That said, it doesn't seem useful to increase the number of unrolls unless there is some very specific and unusual sequencing to explore. In general, it is strongly recommended to break down complex scenarios into smaller and more primitive tests.

Now run the same litmus file with `litmus7` on an Arm Neoverse-based machine:

```bash
litmus7 test2.litmus
```

The output will look like:

```output
Test MP+Loop+DMB Allowed
Histogram (1 states)
1000000:>1:X0=1; 1:X2=1;
```
Here, 100% of the runs observed `(1,1)`, which builds confidence that the barriers are working.

A final point is that the `DMB` in `P1` can be relaxed by changing it to `DMB ISHLD`. This relaxation might potentially yield performance improvements in real applications. However, if you do the same relaxation to the `DMB` in `P0`, it breaks the message passing. You can try this experiment and also read the Arm documentation on the differences between `DMB ISH`, `DMB ISHLD`, and `DMB ISHST`.

## Example 3: Message Passing With One-Way Barriers

Now you can move on to test message passing with one-way barriers. This is done by using instructions that support acquire-release ordering.

Create a litmus file called `test3.litmus` with the contents shown below:

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

In this example, you have removed the `DMB` instructions and instead use a properly placed `STLR` in `P0` and `LDAR` in `P1`. `STLR` is a store-release instruction and `LDAR` is a load-acquire instruction. These are synchronizing memory accesses (as opposed to ordinary memory accesses). The `STLR` prevents earlier memory accesses from reordering after it, while the `LDAR` prevents later memory accesses from reordering before it. This is why these are also called one-way barriers; they block reordering only in one direction. `LDAR` and `STLR` instructions are Sequentially Consistent with respect to other `LDAR` and `STLR` instructions, while ordinary `LDR` and `STR` are not. There is also a more relaxed version of `LDAR` called `LDAPR`, this is a Load-Acquire with Processor Consistency. The Arm documentation on [Load-Acquire and Store-Release instructions](https://developer.arm.com/documentation/102336/0100/Load-Acquire-and-Store-Release-instructions) has more information on this.

Run this test with `herd7`:

```bash
herd7 test3.litmus
```
The output should look like:

```output
Test MP+Loop+ACQ_REL Allowed
States 1
1:X0=1; 1:X2=1;
```
Only an outcome of `(1,1)` is possible. This is the result you want.

Run the same test with `litmus` on your Arm Neoverse CPU based machine:

```bash
litmus7 test3.litmus
```

The output from this will look like:
```output
Test MP+Loop+ACQ_REL Allowed
Histogram (1 states)
1000000:>1:X0=1; 1:X2=1;
```

`litmus7` shows the same result as `herd7`.

## Example 4: Compare and Swap With One-Way Barriers

Atomic instructions support acquire-release semantics. In this example, you will examine a Compare and Swap instruction with acquire ordering (`CASA`).

Create a litmus file named `test4.litmus` with the content shown below:

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

This test represents a basic spin lock. The lock variable resides at address `y`. When `y` is set to 1, it's locked, when it's set to 0, it's available. 

The test starts with the lock variable at address `y` set to 1, which means it's locked. `P0` is assumed to be the owner of the lock at the start of the test. `P0` writes to address `x` (the payload), then releases the lock by writing a 0 to address `y`. The store to address `y` is a `STLR` (store-release), this ensures that the write to the payload is visible before the release of the lock at address `y`. On `P1`, you spin on address `y` (the lock) with a `CASA`. At each loop iteration, `CASA` checks the value at address `y`. If it's 0 (available), then it will write a 1 to take ownership. If it's 1, the `CASA` fails and loops back to try the `CASA` again. It will continue to loop until it successfully takes the lock. The `CASA` instruction does this operation atomically, and with acquire ordering to ensure that the later `LDR` of address `x` (the payload) is not ordered before the `CASA`.

Run this test with `herd7`:

```bash
herd7 test4.litmus
```

The output will look like:

```
Test Lock+Loop+CAS+ACQ_REL Allowed
States 1
1:X0=1; 1:X2=1;
```
Only an outcome of `(1,1)` is possible. This is the result you want.

Now run the same test with `litmus7` on your Arm Neoverse CPU based machine:

```bash
litmus7 ./test4.litmus -ccopts="-mcpu=native"
```
The output should look like:
```output
Test Lock+Loop+CAS+ACQ_REL Allowed
Histogram (1 states)
1000000:>1:X0=1; 1:X2=1;
```
Only an outcome of `(1,1)` has been observed. More test iterations can be executed to build confidence that this is the only possible result.

 Note that when you ran `litmus7`, you used the switch `-ccopts="-mcpu=native"`. If you didn't, `litmus7` would fail with a message saying that the `CASA` instruction cannot be emitted by the compiler.

Try changing the `CASA` to a `CAS` (Compare and Swap with no ordering) to see what happens.

## Example 5: Dependency as a Barrier

It is possible to create barriers that are more relaxed than acquire-releases. This is done by creating dependencies between instructions that block the CPU's scheduler from reordering them. This is what the C/C++ ordering of `memory_order::consume` aims to achieve. However, over the years, it has been challenging for compilers to support this dependency based barrier concept. Thus,`memory_order::consume` gets upgraded to `memory_order::acquire` in practice. In fact, this ordering is in discussion to be dropped from the C/C++ standard. Still, it makes for an interesting example to show here.

To be able to show the difference, you first need to look at the one-way barrier example from earlier but with a modification. That modification is that you will add a second payload memory address, call it `w`. 

Copy the content shown below with these modifications into a new litmus test file called `test5.litmus`:

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
On `P0`, you are writing to both `w` and `x` before the store-release on address `y`. This ensures that the writes to both `x` and `w` (the payloads) will be ordered before the write to address `y` (the flag). On `P1`, you loop with a load-acquire on address `y` (the flag). Once it is observed to be set, you load the two payload addresses. The load-acquire ensures that you do not read the payload addresses `w` and `x` until the flag is observe to be set. The condition at the bottom has been updated to check for any cases where either `w` or `x` are 0. Either of these being observed as 0 will be an indication of reading the payload before the ready flag is observed to be set (not what you want). Overall, this code should result in only the outcome `(1,1,1)`.

Run this test with `herd7`:

```bash
herd7 test5.litmus
```

The output should look like: 

```output
Test MP+Loop+ACQ_REL2 Allowed
States 1
1:X0=1; 1:X2=1; 1:X5=1;
```
Now run it with `litmus7` on your Arm Neoverse CPU based machine:

```bash
litmus7 test5.litmus
```
The output will look like:

```output
Test MP+Loop+ACQ_REL2 Allowed
Histogram (1 states)
1000000:>1:X0=1; 1:X2=1; 1:X5=1;
```

Both `herd7` and `litmus7` show the expected result. It might be worth increasing the number of iterations on `litmus7` to build more confidence in the result.

Now remove the load-acquire in `P1` and use a dependency as a barrier. Create a new litmus file `test6.litmus` with the contents shown below:

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
What you have done to `P1` is create a dependency between the first `LDR` which is in the loop, and the second `LDR` which appears after the loop. Register `X6` (which is the same as `W6`) doesn't change the address loaded in the second `LDR` because the previous `AND` instruction zeros the offset. The point of the `AND` is to create a dependency between the first and second `LDR` instructions so that they execute in order. The net effect is that you have a barrier for the address `x` between the two `LDR` instructions. However, you do not have a barrier for the address `y`. In this way, it is a more relaxed barrier than using `LDAR`, because `LDAR` applies to all memory accesses that appear after it in program order.

Run this test with `herd7`:

```bash
herd7 test6.litmus
```

The output of this test should look like:
```output
Test MP+Loop+Dep Allowed
States 2
1:X0=1; 1:X2=1; 1:X5=0;
1:X0=1; 1:X2=1; 1:X5=1;
```
The possible outcome of `(1,1,0)` makes sense because the dependency you have added doesn't cover the read of address `w`.

Now run the same test with `litmus7` on your Arm Neoverse CPU based machine:

```bash
litmus7 test6.litmus 
```
The output should look like:

```output
Test MP+Loop+Dep Allowed
Histogram (2 states)
14    *>1:X0=1; 1:X2=1; 1:X5=0;
999986:>1:X0=1; 1:X2=1; 1:X5=1;
```
You have the same result here too. However, notice that you had to execute the test 10 million times just to observe the reorder of the `LDR` of address `w` just fourteen times. Again, if you don't run enough test iterations, you might miss the observation of a possible outcome.

## Experimentation Ideas

You should now be able to modify and experiment with the example tests shared in this Learning Path. You can also create your own examples by using the assembly code generated from higher level languages. Another great resource to experiment with are the litmus tests posted in the [herd7 online simulator](https://developer.arm.com/herd7)
