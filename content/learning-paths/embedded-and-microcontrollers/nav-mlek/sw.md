---
title: Software development considerations
description: Review software development tools, model formats, and example applications used with the ML Evaluation Kit.

weight: 4

# Do not modify these elements
layout: "learningpathall"
---

## Development environment

You should use an `x86_64` development machine running Windows or Linux for the best experience. 

The [Arm ML Evaluation Kit (MLEK)](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit) is not fully supported on Windows. Some of the required tools work only on Linux. Linux is recommended if you plan to use MLEK extensively. 

There are some ML examples which can be developed using Windows tools. 

The same development tools for general embedded projects are needed for ML applications, but there are additional tools and software which are also common in ML applications. 

### C/C++ Compilers 

You can build ML applications with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded/) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain/). 

Use the install guides to install the compilers on your computer:
- [Arm Compiler for Embedded](/install-guides/armclang/)
- [Arm GNU Toolchain](/install-guides/gcc/arm-gnu/)

## Integrated Development Environments (IDE)

Use the [Arm Development Studio install guide](/install-guides/armds/) to set up Arm DS on Linux or Windows. 

[Keil MDK](/install-guides/mdk/) is a popular microcontroller development toolkit on Windows.

Both IDEs contain `Arm Compiler for Embedded` to build applications, and can connect to the Ecosystem FVPs for software debug and test.

## Other tools

A number of other tools are common in ML applications.
- Python
- pip
- [CMake](/install-guides/cmake/)
- [CMSIS-Toolbox](/install-guides/cmsis-toolbox/)

## Using Docker

You may want to use [Docker](/install-guides/docker/) to simplify ML development environment creation. 

As an example, clone the MLEK repository and look at the `Dockerfile` at the top of the repository to see one way to use Docker in ML application development:

```console
git clone "https://git.gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit.git"
cd ml-embedded-evaluation-kit
git submodule update --init
```

Use an editor or program such as `more` or `cat` to view the Dockerfile.

## Machine learning Frameworks

[LiteRT for Microcontrollers](https://ai.google.dev/edge/litert/microcontrollers/overview), formerly known as TensorFlow Lite for Microcontrollers is one of the more common framework for microcontroller ML applications.

TensorFlow uses [`xxd`](https://linux.die.net/man/1/xxd/) to convert TensorFlow Lite models into C data structures. 

[PyTorch](https://pytorch.org/) is also commonly used on microcontrollers. 

[Apache TVM](https://tvm.apache.org/) is an open-source compiler framework for ML and can be used on microcontrollers.

The ML ecosystem is changing rapidly with many new companies and software. You can refer to the [AI Ecosystem Catalog](https://www.arm.com/partners/ai-ecosystem-catalog/) to find ML solutions for Cortex-M microcontrollers.

### Ethos optimized model

[Vela](https://pypi.org/project/ethos-u-vela/) is used to compile a TFLM neural network model into an optimized version that can run on hardware containing an Arm Ethos-U NPU.

Install it using `pip3`:

```console
pip install ethos-u-vela
```

### CMSIS-NN

The [CMSIS-NN](https://www.keil.com/pack/doc/CMSIS/NN/html/index.html) software library is a collection of efficient neural network kernels developed to maximize the performance and minimize the memory footprint of neural networks on Arm Cortex-M processors.

The library is used by frameworks for operations that cannot be executed on the Ethos processor.

[Accelerated inference on Arm microcontrollers with TensorFlow Lite for Microcontrollers and CMSIS-NN](https://blog.tensorflow.org/2021/02/accelerated-inference-on-arm-microcontrollers-with-tensorflow-lite.html) provides an excellent overview.


## Example applications

Resources for learning about ML applications are listed below for you to investigate and learn from.

### Arm ML Evaluation Kit (MLEK)

The [MLEK](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit) provides a number of example ML applications.

[The Quick Start Guide](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/main/docs/quick_start.md) guides you through running an example application.

### Open-IoT-SDK

The Open-IoT-SDK includes a number of ML applications and demonstrates concepts such as how to integrate Arm Trusted Firmware for Cortex-M with an ML application. 

Refer to the [Open-IoT-SDK repository](https://github.com/ARM-software/open-iot-sdk) to learn how to use the SDK.


### TVM example

To learn about TVM, refer to [Running TVM on bare metal Cortex-M55 and Ethos-U55 NPU with CMSIS-NN](https://tvm.apache.org/docs/how_to/work_with_microtvm/micro_ethosu.html).

You will learn the basics of TVM and more about [CMSIS-NN](https://github.com/ARM-software/CMSIS-NN/), the software library of efficient neural network kernels for Cortex-M.

### Arm ML example repository

Additional examples are in an Arm GitHub repository called [ML-examples](https://github.com/ARM-software/ML-examples/)

## Example use cases

The potential use cases of machine learning are very broad. Please propose your favorite applications for Cortex-M and Ethos-U ML in [GitHub discussions](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/discussions/categories/ideas/).
