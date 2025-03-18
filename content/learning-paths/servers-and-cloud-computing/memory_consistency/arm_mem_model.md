---
title: "Thread Synchronization, Arm Memory Model, and Tools"
weight: 2
layout: "learningpathall"
---

## CPU Memory Model vs Language/Runtime Memory Models

It's important to understand that the majority of developers will not need to concern themselves with the memory consistency model of the CPU their code will execute on. This is because programming languages and runtime engines abstract away the CPUs memory model by presenting the programmer with a language/runtime memory model. This abstraction is achieved by providing developers with a set of language/runtime specific memory ordering rules, synchronization constructs, and supporting libraries. So long as the developer uses these correctly, language compilers and runtime engines will make sure the code executes correctly on any CPU regardless of how strong or weakly ordered it is.

That said, developers may want to dig deeper into this topic for various reasons including:

- Extract more performance from weakly ordered CPUs (like Arm).
  - Keep in mind that compilers and runtimes will do a good job of maximizing performance. Only in well understood niche cases will there be a potential for performance gain by going beyond what the compiler/runtime would do to higher level code. For most cases, all it takes to get more performance is to use the latest compilers, compiler switches, and runtimes.
- Develop confidence in the correctness of synchronization constructs.
- Develop an understanding of how compilers and runtimes select different machine instructions while still honoring the memory ordering rules of the language/runtime and CPU.
- General learning.

## What We Will Do

In this Learning Path, we will use publicly available tools to explore thread synchronization on Arm CPUs. This will provide the reader with enough working knowledge of the tools to be able to explore on their own. At the end of this Learning Path, we will provide more information on where readers can find a more formal (and complex) treatment of this subject.

##  The Formal Definition of the Arm Memory Model

The formal definition of the Arm memory model is in the [Arm Architecture Reference Manual for A-profile architecture](https://developer.arm.com/documentation/ddi0487/la) (Arm ARM) under the section called `The AArch64 Application Level Memory Model`. The ordering requirements defined in the Arm ARM is a transliteration of the `aarch64.cat` file hosted on the Arm [herd7 simulator tool](https://developer.arm.com/herd7). In fact, this `aarch64.cat` file is the authoritative definition of the Arm memory model. Since it is a formal definition, it is complex.

##  Herd7 Simulator & Litmus7 Tool

The herd7 simulator provides a way to test snippets of Arm assembly against the formal definition of the Arm memory model (the `aarch64.cat` file mentioned above). The litmus7 tool can take the same snippets of assembly that run on herd7 and run them on actual Arm HW. This allows for comparing the formal memory model to the memory model of an actual Arm CPU. These snippets of assembly are called litmus tests.

It's important to understand that it is possible for an implementation of an Arm CPU to be more strongly ordered than the formally defined Arm memory model. This case is not a violation of the memory model because it will still execute code in a way that is compliant with the memory ordering rules.

## Installing the Tools

Herd7 and Litmus7 are part of the [diy7](http://diy.inria.fr/) tool suite. The diy7 tool suite can be installed by following the [installation instructions](http://diy.inria.fr/sources/index.html). We suggest installing this on an Arm system so that both herd7 and litmus7 can be compared side by side on the same system.


## Running Herd7 and Litmus7 Example Commands

The test file is assumed to be called `test.litmus` and is in the current directory.

The help menu shows all options.
```
herd7 --help
```
```
litmus7 --help
```

Example of running herd7.
```
herd7 ./test.litmus
```

Example of running litmus7.
```
litmus7 ./test.litmus
```

Example of running litmus7 with 5,000,000 test iterations (default is 1,000,000).
```
litmus7 ./test.litmus -s 5000000
```

Example of running a litmus7 tests in parallel on 8 CPUs.
```
litmus7 ./test.litmus -a 8
```

Example of running litmus7 and asking GCC to emit atomic instructions as required by the litmus test (the possible need for this is explained later).
```
litmus7 ./test.litmus -ccopts="-mcpu=native"
```
