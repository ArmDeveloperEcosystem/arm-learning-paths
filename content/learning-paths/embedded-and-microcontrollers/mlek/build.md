---
# User change
title: "Build the ML Evaluation Kit examples"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The [Arm ML Evaluation Kit (MLEK)](https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ml-embedded-evaluation-kit) provides a number of ready-to-use ML applications. These allow you to investigate the embedded software stack and evaluate performance on the Cortex-M55 and Ethos-U85 processors.

You can use the MLEK source code to build sample applications and run them on the [Corstone reference systems](https://www.arm.com/products/silicon-ip-subsystems/), for example the [Corstone-320](https://developer.arm.com/Processors/Corstone-320) Fixed Virtual Platform (FVP).

## Before you begin

It is recommended to use an Ubuntu Linux host machine. The Ubuntu version should be 20.04 or 22.04. These instructions have been tested on the `x86_64` architecture.

## Build the example application

### Install the dependencies

Run the following commands to install some necessary tools.

```bash
sudo apt update
sudo apt install unzip python3-venv python3-pip -y
```
### Install the compiler

The examples can be built with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain).

Install the GNU toolchain (`gcc`).

```bash
wget https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz

tar -xf arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz

export PATH=~/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi/bin/:$PATH

```

{{% notice Tip %}}
You can review the installation guides for further details.

- [Arm Compiler for Embedded](/install-guides/armclang/)
- [Arm GNU Toolchain](/install-guides/gcc/arm-gnu)

{{% /notice %}}

### Clone the repository

Clone the ML Evaluation Kit repository, and navigate into the new directory:

```bash
git clone "https://review.mlplatform.org/ml/ethos-u/ml-embedded-evaluation-kit"
cd ml-embedded-evaluation-kit
git submodule update --init
```

### Run the build sscript

The default build is Ethos-U55  and Corstone-300. The default build for Ethos-U85 is Corstone-320. Use the `npu-config-name` flag to set Ethos-U85.

The default compiler is `gcc`, but `armclang` can also be used. Number after `ethos-u85-*` is the number of MACs, 128-2048 (2^n).

Use `--make-jobs` to specify `make -j` value.

You can select either compiler to build applications. You can also try them both and compare the results.

- Build with Arm GNU Toolchain (`gcc`):

```
./build_default.py --npu-config-name ethos-u85-256 --toolchain gnu --make-jobs 8
```

- Build with Arm Compiler for Embedded (`armclang`):

```console
./build_default.py --npu-config-name ethos-u85-256 --toolchain arm --make-jobs 8
```

{{% notice Tip %}}
Use `./build_default.py --help` for additional information.

{{% /notice %}}

The build will take a few minutes.

When the build is complete, you will find the examples (`.axf` files) in the `cmake-build-*/bin` directory. The `cmake-build` directory names are specific to the compiler used and Ethos-U85 configuration. Verify that the files have been created by observing the output of the `ls` command

```bash
ls cmake-build-mps4-sse-320-ethos-u85-256-gnu/bin/
```

The next step is to install the FVP and run the built example applications.

