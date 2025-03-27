---
title: "Thread Synchronization, Arm Memory Model, and Tools"
weight: 2
layout: "learningpathall"
---

## CPU Memory Model vs Language/Runtime Memory Models

The majority of developers do not need deep familiarity with the memory consistency model of the CPU. This is because programming languages and runtime engines abstract away the CPU's memory model by providing the programmer with a language/runtime memory model. This abstraction is achieved by providing developers with a set of language/runtime specific memory ordering rules, synchronization constructs, and supporting libraries. As long as the developer uses these correctly, language compilers and runtime engines will make sure the code executes correctly on any CPU regardless of how strong or weakly ordered it is.

That said, developers may want to dig deeper into this topic for various reasons including:

- Extract more performance from weakly ordered CPUs (like Arm CPUs).
  - Compilers and runtimes will do a good job of maximizing performance. Only in well understood niche cases will there be a potential for performance gain by going beyond what the compiler/runtime would do to higher level code. For most cases, all it takes to get more performance is to use the latest compilers, compiler switches, and runtimes.
- Develop confidence in the correctness of synchronization constructs.
- Develop an understanding of how compilers and runtimes select different machine instructions while still honoring the memory ordering rules of the language/runtime and CPU.

In this Learning Path, you will use publicly available tools to explore thread synchronization on Arm CPUs. You will gain enough working knowledge of the tools to be able to explore thread synchronization concepts. At the end of this Learning Path, you will be able access more information to get a deeper understanding of this subject.

##  The Formal Definition of the Arm Memory Model

The formal definition of the Arm memory model is in the [Arm Architecture Reference Manual for A-profile architecture](https://developer.arm.com/documentation/ddi0487/la) (Arm ARM) under the section called `The AArch64 Application Level Memory Model`. The ordering requirements defined in the Arm ARM is a transliteration of the `aarch64.cat` file hosted on the Arm [herd7 simulator tool](https://developer.arm.com/herd7). In fact, this `aarch64.cat` file is the authoritative definition of the Arm memory model. As it is a formal definition, it is complex.

##  Herd7 Simulator & Litmus7 Tool

The herd7 simulator provides a way to test snippets of Arm assembly against the formal definition of the Arm memory model (the `aarch64.cat` file mentioned above). The litmus7 tool can take the same snippets of assembly that run on herd7 and run them on actual Arm hardware. This allows for comparing the formal memory model to the memory model of an actual Arm CPU. These snippets of assembly are called litmus tests.

It's important to understand that it is possible for an implementation of an Arm CPU to be more strongly ordered than the formally defined Arm memory model. This case is not a violation of the memory model because it will still execute code in a way that is compliant with the memory ordering rules.

## Install the Tools

Herd7 and Litmus7 are part of the [diy7](http://diy.inria.fr/) tool suite. The diy7 tool suite can be installed by following the [installation instructions](http://diy.inria.fr/sources/index.html). You will install the tools on an Arm Linux system so that both herd7 and litmus7 can be compared side by side on the same system.

Start an Arm-based cloud instance. This example uses a `t4g.xlarge` AWS instance running Ubuntu 22.04 LTS, but other instances types are possible. 

If you are new to cloud-based virtual machines, refer to [Get started with Servers and Cloud Computing](/learning-paths/servers-and-cloud-computing/intro/). 

First confirm you are using a Arm-based instance with the following command.

```bash
uname -m
```
You should see the following output.

```output
aarch64
```

Next, install OCaml Package Manager (opam). You will need `opam` to install the `herdtools7` tool suite:
```bash
sudo apt update
sudo apt install opam -y
```

Setup `opam` to install the tools:
```bash
opam init
opam update
eval $(opam env)
```

Now install the `herdtool7` tool suite which include both `litmus7` and `herd7`:

```bash
opam install herdtools7
```


## Herd7 and Litmus7 Example Commands

You can run `--help` on both the tools to review all the options available.
```
herd7 --help
```
```
litmus7 --help
```

The input to both `herd7` and `litmus7` tools are snippets of assembly code, called litmus tests.

Shown below are some example of running the tools with a litmus test. In the next section, you will go through an actual litmus test example.

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
