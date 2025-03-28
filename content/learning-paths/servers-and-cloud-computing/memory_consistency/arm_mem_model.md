---
title: "Thread Synchronization, Arm Memory Model, and Tools"
weight: 2
layout: "learningpathall"
---

## The Memory Consistency Model

Most developers don't need deep knowledge of a CPU's memory consistency model. Programming languages and runtimes abstract the CPU’s model by providing their own memory ordering rules, synchronization constructs, and libraries. As long as the developer uses these correctly, compilers and runtime engines ensure that the code executes correctly on any CPU - whether its memory ordering is strong or weak.

That said, developers might want to dig deeper into this topic for various reasons including:

- Extracting additional performance from weakly-ordered CPUs, such as Arm CPUs:
  - Although compilers and runtimes typically do a good job of maximizing performance, manual tuning in well understood niche cases might provide further improvements. In most cases, all it takes to improve performance is using latest compilers, compiler switches, and runtimes.
- Gaining confidence in the correctness of synchronization constructs.
- Understanding how compilers and runtimes select machine instructions while still honoring the memory ordering rules.

In this Learning Path, you will use publicly available tools to explore thread synchronization on Arm CPUs. You will gain enough working knowledge of these tools to explore thread synchronization concepts. 

{{% notice Learning Tip%}}
At the end of this Learning Path, you can find details of further resources that you can consult to gain a deeper understanding of this subject.{{% /notice %}}

##  The Formal Definition of the Arm Memory Model

The formal definition of the Arm memory model is described in the [Arm Architecture Reference Manual for A-profile architecture](https://developer.arm.com/documentation/ddi0487/la) (often referred to as "the Arm ARM") under the section called `The AArch64 Application Level Memory Model`. The ordering requirements defined in the Arm ARM is a transliteration of the `aarch64.cat` file hosted on the Arm [herd7 simulator tool](https://developer.arm.com/herd7). In fact, the `aarch64.cat` file is the authoritative definition of the Arm memory model. As a formal definition, it is inherently complex.

##  Herd7 Simulator and Litmus7 Tool

The herd7 simulator tests snippets of Arm assembly against the formal definition of the Arm memory model (the `aarch64.cat` file mentioned above). The litmus7 tool runs the same snippets of assembly on actual Arm hardware, enabling a direct comparison between the formal model and the real-world behavior of an actual Arm CPU. These snippets of assembly are called litmus tests.

It's important to note that an Arm CPU implementation might exhibit stronger ordering than the formal memory model. This is not a violation; the CPU still executes code in a way that is compliant with the memory ordering rules.

## Install the Tools

Herd7 and Litmus7 are part of the [diy7](http://diy.inria.fr/) tool suite. You can install the diy7 tool suite by following the [installation instructions](http://diy.inria.fr/sources/index.html). Install the tools on an Arm Linux system so that both herd7 and litmus7 can be compared side by side.

Start an Arm-based cloud instance. This example uses a `t4g.xlarge` AWS instance running Ubuntu 22.04 LTS, but other instances types are possible. 

If you are new to cloud-based virtual machines, refer to [Get started with Servers and Cloud Computing](/learning-paths/servers-and-cloud-computing/intro/). 

First confirm you are using a Arm-based instance:

```bash
uname -m
```
You should see the following output:

```output
aarch64
```

Install OCaml Package Manager (opam). You need `opam` to install the `herdtools7` tool suite:
```bash
sudo apt update
sudo apt install opam -y
```

Set up `opam` to install the tools:
```bash
opam init
opam update
eval $(opam env)
```

Now install the `herdtool7` tool suite (which includes both `litmus7` and `herd7`):

```bash
opam install herdtools7
```


## Herd7 and Litmus7 Example Commands

You can run `--help` on both tools to review all available options:
```
herd7 --help
```
```
litmus7 --help
```

The input to both `herd7` and `litmus7` tools are snippets of assembly code, called litmus tests.

Shown below are some example of running the tools with a litmus test. In the next section, you will go through an actual litmus test example.

Run herd7 with a litmus test:
```
herd7 ./test.litmus
```

Run litmus7 with a litmus test:
```
litmus7 ./test.litmus
```

Run litmus7 with 5,000,000 test iterations (default is 1,000,000):
```
litmus7 ./test.litmus -s 5000000
```

Run a litmus7 test in parallel on 8 CPUs:
```
litmus7 ./test.litmus -a 8
```

Run litmus7 with GCC emitting atomic instructions as required by the litmus test (explained later):
```
litmus7 ./test.litmus -ccopts="-mcpu=native"
```
