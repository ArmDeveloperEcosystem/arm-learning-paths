---
# User change
title: "Build the ML Evaluation Kit examples"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The [Arm ML Evaluation Kit (MLEK)](https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ml-embedded-evaluation-kit) provides a number of ready-to-use ML applications. These allow you to investigate the embedded software stack and evaluate performance on the Cortex-M55 and Ethos-U55 processors.

You can use the MLEK source code to build sample applications and run them on the [Corstone platform](https://www.arm.com/products/silicon-ip-subsystems/), for example the [Corstone-300](https://developer.arm.com/Processors/Corstone-300) Fixed Virtual Platform (FVP).

## Before you begin

You can use your own Ubuntu Linux host machine or use [Arm Virtual Hardware (AVH)](https://www.arm.com/products/development-tools/simulation/virtual-hardware) for this Learning Path.

The Ubuntu version should be 20.04 or 22.04. The `x86_64` architecture must be used because the Corstone-300 FVP is not currently available for the Arm architecture. You will need a Linux desktop to run the FVP because it opens graphical windows for input and output from the software applications.

If you want to use Arm Virtual Hardware the [Arm Virtual Hardware install guide](/install-guides/avh#corstone) provides setup instructions.

### Compilers

The examples can be built with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain).

Use the install guides to install the compilers on your computer:
- [Arm Compiler for Embedded](/install-guides/armclang/)
- [Arm GNU Toolchain](/install-guides/gcc/arm-gnu)

Both compilers are pre-installed in Arm Virtual Hardware.

### Corstone-300 FVP {#fvp}

To install the Corstone-300 FVP on your computer refer to the [install guide for Arm Ecosystem FVPs](/install-guides/fm_fvp).

The Corstone-300 FVP is pre-installed in Arm Virtual Hardware.

## Clone the repository

1. Install `virtualenv` to create Python virtual environments:

```console
sudo apt update
sudo apt install python3-venv -y
```

2. Clone the ML Evaluation Kit repository, and navigate into the new directory:

```console
git clone "https://review.mlplatform.org/ml/ethos-u/ml-embedded-evaluation-kit"
cd ml-embedded-evaluation-kit
git submodule update --init
```

## Build the example applications

The default compiler is `gcc`, but `armclang` can also be used.

You can select either compiler to build applications. You can also try them both and compare the results.

- Build with Arm GNU Toolchain (`gcc`)

```
./build_default.py
```

- Build with Arm Compiler for Embedded (`armclang`)

```console
./build_default.py --toolchain arm
```

The build will take a few minutes.

When the build is complete, you will find the example images (`.axf` files) in the `cmake-build-*/bin` directory. The `cmake-build` directory names are specific to the compiler used and Ethos-U55 configuration.
