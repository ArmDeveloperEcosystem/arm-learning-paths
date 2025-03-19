---
# User change
title: "Herd7 & Litmus7 Test Primer"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Herd7 & Litmus7 Test Primer

In this section we will give just enough information to understand the syntax of litmus tests and how to run them. More comprehensive information on developing and runing litmus tests can be found in the [diy7 documentation](https://diy.inria.fr/doc/index.html)

We will use an abbreviated version of the `MP.litmus` test included in the [herd7 online simulator](https://developer.arm.com/herd7).
```
AArch64 MP
{
0:X1=x; 0:X3=y;
1:X1=y; 1:X3=x;
}
  P0               |  P1               ;
  MOV    W0,  #1   |  LDR    W0,  [X1] ;
  STR    W0,  [X1] |  LDR    W2,  [X3] ;
  MOV    W2,  #1   |                   ;
  STR    W2,  [X3] |                   ;
exists
(1:X0=1 /\ 1:X2=0)
```

- The first line sets the target architecture of this test which is `AArch64`. This is required because the diy7 tool supports other architectures that are not Arm. After the architecture label we have `MP` which is a label that gives this test its name. `MP` stands for "Message Passing".
  - In short, the first line say's "This is a test for AAarch64 called `MP`"
- This test defines two threads `P0` and `P1`. It is possible to define more threads than just two, but in this Learning Path we will only work with two threads to keep things manageable.
- The lines between the brackets ( `{..}` ) determines the initial state of the CPU registers for this test.
  - `0:X1=x; 0:X3=y;` defines the initial state for `P0`.
    - Register X1 holds memory address `x`.
    - Register X3 holds memory address `y`.
  - `1:X1=y; 1:X3=x;` defines the initial state for `P1`.
    - Register X1 holds memory address `y`.
    - Register X3 holds memory address `x`.
  - Any registers and memory addresses not listed in between these brackets are initialized to 0.
  - The memory address `x` contains the message to pass, while the memory address `y` is the message ready flag.
- Below the brackets we see the assembly snippets for `P0` and `P1`.
  - `P0`.
    - The first `MOV` and `STR` writes a `1` into memory address `x` (the payload).
    - The second `MOV` and `STR` writes a `1` into memory address `y` (the flag).
  - `P1`.
    - The first `LDR` reads the address `y` (the flag). The value of the flag is stored in register `W0`.
    - The second `LDR` reads the address `x` (the payload). The value of the payload is stored in register `W2`.
    - Notice that we are not looping on the flag like what would normally be done in a message passing scenario. We explore loops in the next section.
- The last two lines shows a test condition. This test condition asks the question:
  - "On `P1`, is it possible for us to observe register `W0` (the flag) set to 1 **AND** register `W2` (the payload) set to 0?"
    - Wait...but the condition uses register names `X0` and `X2`, not `W0` and `W2`. See the note below for more.
  - In this condition check syntax, `/\` is a logical **AND**, while `\/` is a logical **OR**
- A note on `X` and `W` registers.
  - Notice we are using `X` registers for storing addresses and for doing the condition check, but `W` registers for everything else.
    - Addresses need to be stored as 64-bit values, hence the need to use `X` registers for the addresses because they are 64-bit. `W` registers are 32-bit. In fact, register `Wn` is the lower 32-bits of register `Xn`.
    - Writing the litmus tests this way is cleaner than if we use all `X` registers. If all `X` registers are used, the data type of each register needs to be declared on additional lines. For this reason, most tests are written as shown above. The way this is done may be changed in the future to reduce potential confusion around the mixed use of `W` and `X` registers, but all of this is functionally correct.

Before we run this test with `herd7` and `litmus7`, let's hypothesize on what might be observed in registers `X0` (flag) and `X2` (payload) on thread `P1`. Even though we know Arm machines are not Sequentially Consistent (modern machines usually aren't), let's start by assuming this to be the case anyway. To reason on the execution of these threads in a Sequentially Consistent way, means to imagine the instructions on `P0` and `P1` are executed in some interleaved order. Further, if we interleave these instructions in all possible permutations, we can figure out all of the possible valid outcomes of registers `X0` (flag) and `X2` (payload) on `P1`. For the example test above, the possible valid outcomes of `(X0,X2)` (or `(flag,data)`) are `(0,0)`, `(0,1)`, & `(1,1)`. Below we show some permutations that result in these valid outcomes. These are not all the possible instruction permutations for this test. Listing them all would make this section needlessly long.

A permutation that results in `(0,0)`:
```
(P1)  LDR  W0,  [X1]  # P1 reads flag, gets 0
(P1)  LDR  W2,  [X3]  # P1 reads payload, gets 0
(P0)  MOV  W0,  #1
(P0)  STR  W0,  [X1]  # P2 writes payload, sets 1
(P0)  MOV  W2,  #1
(P0)  STR  W2,  [X3]  # P2 writes flag, sets 1
```
In this permutation of the test execution, `P1` runs to completion before `P0` even starts its execution. For this reason, `P1` observes the initial values of 0 for both the flag and payload.

A permutation that results in `(0,1)`:
```
(P1)  LDR  W0,  [X1]  # P1 reads flag, gets 0
(P0)  MOV  W0,  #1
(P0)  STR  W0,  [X1]  # P2 writes payload, sets 1
(P1)  LDR  W2,  [X3]  # P1 reads payload, gets 1
(P0)  MOV  W2,  #1
(P0)  STR  W2,  [X3]  # P2 writes flag, sets 1
```
In this permutation of the test execution, `P1` reads the initial value of the flag (the first line) because this instruction is executed before `P0` writes the flag (the last list). However `P1` reads the payload value of 1 because it executes after `P0` writes the payload to 1 (third and forth lines).

A permutation that results in `(1,1)`:
```
(P0)  MOV  W0,  #1
(P0)  STR  W0,  [X1]  # P2 writes payload, sets 1
(P0)  MOV  W2,  #1
(P0)  STR  W2,  [X3]  # P2 writes flag, sets 1
(P1)  LDR  W0,  [X1]  # P1 reads flag, gets 1
(P1)  LDR  W2,  [X3]  # P1 reads payload, gets 1
```
In this permutation of the test execution, `P2` runs to completion before `P1` starts. Thus `P1` observes both the flag and payload set to 1.

Result `(1,0)` is not possible in a Sequentially Consistent execution of this test. This is because the instructions in `P0` and `P1` must execute in program order (a requirement for Sequential Consistency). It is only possible to get the result `(1,0)` if the machine is not Sequentially Consistent. Not being Sequentially Consistent means that the memory access instructions (`STR` and `LDR`) can be executed out of program order if there are no dependencies between them.

Now that we've developed a hypothesis on what we should see assuming a Sequentially Consistent machine, let's try running the test with `herd7`. `herd7` will simulate all the possible instruction permutations to see which outcomes are possible. Below is the output of the test on `herd7`.

```
Test MP Allowed
States 4
1:X0=0; 1:X2=0;
1:X0=0; 1:X2=1;
1:X0=1; 1:X2=0;
1:X0=1; 1:X2=1;
Ok
Witnesses
Positive: 1 Negative: 3
```

It turns out that we do see outcome `(1,0)` when testing against the Arm memory model. This point is also signaled by the positive witness on our test condition. This tells us that the Arm memory model violates Sequential Consistency. As mentioned earlier, we know this already. The Arm memory model tends to be a Relaxed Consistency model. We are saying Arm "tends to" be a Relaxed Consistency model because it is possible for an Arm CPU in the real world to use ordering rules that are stronger than Relaxed Consistency. Going stronger on the memory model will not violate the Arm ordering rules. A stronger memory model means that there might be less opportunity for HW based optimizations, it will not affect the correctness of code execution (assuming no bugs in the code). That said, all Arm Neoverse CPUs in the market can be thought of as following a Relaxed Consistency model (i.e. acquire-release ordering is supported).

In a Release Consistency model, ordinary memory accesses like `STR` and `LDR` do not need to follow program order. This relaxation in the ordering rules expands the list of instruction permutations in the litmus test above. It is in these additional instruction permutations allowed by the Relaxed Consistency model that yields at least one permutation that results in `(1,0)`. Below is one such example of a permutation. For this permutation, we reordered the `LDR` instructions in `P1`.

One possible permutation resulting in `(1,0)`:
```
(P1)  LDR  W2,  [X3]  # P1 reads payload, gets 0
(P0)  MOV  W0,  #1
(P0)  STR  W0,  [X1]  # P2 writes payload, sets 1
(P0)  MOV  W2,  #1
(P0)  STR  W2,  [X3]  # P2 writes flag, sets 1
(P1)  LDR  W0,  [X1]  # P1 reads flag, gets 1
```
There are more possible permutations of instructions, including some that reorder the `STR` instructions in `P0`. We will not explore those here, this is what `herd7` tests for us anyway.

Now that we see the results against the formal Arm memory model, we can try testing on actual hardware with `litmus7`. Since `litmus7` runs the test against actual HW, it can't guarantee that all instruction permutations are tested. This is because there isn't a way to manipulate the CPUs dynamic instruction scheduler (this is "hardwired" in the CPU design). Instead, we have to run numerous iterations of the test to increase the probability that we see all possible outcomes. Thus, `litmus7` can't formally verify/confirm the memory model of the CPU, it can only provide empirical evidence to support a claim on the CPU's memory model. That said, it can be used to disprove that the CPU does not follow a specific memory model. For example, we can prove that Arm is **not** Sequentially Consistent by finding at least one outcome that would not be allowed by Sequential Consistency.

Below we run the test 1,000,000 times with `litmus7`. 1,000,000 is the default number of iterations, this can be adjusted with the `-s` switch. It is also possible to run the test on more than one CPU in parallel with the `-a` switch. The more test iterations we run, the more confidence there can be that we've capture all possible outcomes. Below is the result of running the test on an Arm Neoverse system.

```
Test MP Allowed
Histogram (4 states)
553396:>1:X0=0; 1:X2=0;
53040 *>1:X0=1; 1:X2=0;
96641 :>1:X0=0; 1:X2=1;
296923:>1:X0=1; 1:X2=1;
```
`litmus7` reports the same 4 outcomes we saw in the `herd7` simulation. The outcome with the asterisk signals the positive witness of the condition check. It also reports the number of times each outcome was observed. This result suggests that this CPU is in agreement with the formal memory model (tested with `herd7`), at least for this test. To build more confidence, more tests and more test iterations with `litmus7` would be needed. The [herd7 online simulator](https://developer.arm.com/herd7) contains additional tests that can be executed. Additional tests can also be created by the reader.

Let's move on to exploring thread synchronization.
