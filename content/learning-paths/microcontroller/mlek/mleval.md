---
# User change
title: "Using the ML Evaluation Kit"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The [Arm ML Evaluation Kit (MLEK)](https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ml-embedded-evaluation-kit) provides a number of ready-to-use ML applications. These allow you to investigate the embedded software stack and evaluate performance of the networks running on the Cortex-M55 and Ethos-U55 processors.

We will get the MLEK source, build sample applications, and run them on the [Corstone-300](https://developer.arm.com/Processors/Corstone-300) Fixed Virtual Platform (FVP).

These instructions assume an Ubuntu Linux host machine, or use of [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware).

Full instructions are provided in the evaluation kit [documentation](https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ml-embedded-evaluation-kit/+/HEAD/docs/quick_start.md).

## Corstone-300 FVP {#fvp}

The Corstone-300 FVP is available from the [Arm Ecosystem FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) page. For installation instructions see [this article](/install-tools/ecosystem_fvp/).

Alternatively, you can access the FVP with [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware). For setup instructions see [here](/install-tools/avh#corstone).

## Clone the Evaluation kit repository:

Clone the ML Evaluation Kit repository, and navigate into its directory.
```console
git clone "https://review.mlplatform.org/ml/ethos-u/ml-embedded-evaluation-kit"
cd ml-embedded-evaluation-kit
```

## Resolve external dependencies and prepare build environment:
```console
git submodule update --init
sudo apt install python3.8-venv
```

## Build the example applications

The examples can be built with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain). Both toolchains are installed within Arm Virtual Hardware. To install locally see:
- [Arm Compiler for Embedded](/install-tools/armclang/) or
- [Arm GNU Toolchain](/install-tools/gcc/#Arm-GNU)


### Build with Arm Compiler for Embedded
```console
./build_default.py --toolchain arm
```
### Build with Arm GNU Toolchain
```
./build_default.py
```
The build will take a few minutes. When complete, you will find the example images (`.axf` files) in the `cmake-build-*/bin` directory. Navigate to that directory.
```console
cd cmake-build-mps3-sse-300-ethos-u55-128-arm/bin
```

## Run an example
To run an example on the Corstone-300 FVP target, run a command such as:

### Standalone
```console
FVP_Corstone_SSE-300_Ethos-U55 -a ethos-u-kws.axf
```
### Within Arm Virtual Hardware
```console
VHT_Corstone_SSE-300_Ethos-U55 -a ethos-u-kws.axf
```
Note that it takes some time (approx 1 minute) to initialize the NPU. Be patient. If you see warnings regarding loading the image, these can likely be ignored.

When the example is running, a telnet instance will open allowing you to interact with the example.

## Setting model parameters (Optional)

Some additonal parameters can be specified to Arm Virtual Hardware to configure certain aspects of how it executes.

### List parameters

For a full list of the available parameters, launch the executable with the `--list-params` option, for example:
```console
VHT_Corstone_SSE-300_Ethos-U55 --list-params > parameters.txt
```
### Set parameters
Individual parameters can be set with the `-C` command option. For example, to put the Ethos-U component into fast execution mode:
```console
VHT_Corstone_SSE-300_Ethos-U55 -a ethos-u-kws.axf -C ethosu.extra_args="--fast"
```
If you wish to set many parameters, you may find it easier to list them in a text file (without `-C`) and use `-f` to specify that file.

For example, create an `options.txt` containing:
```console
mps3_board.visualisation.disable-visualisation=1
ethosu.extra_args="--fast"
```
and specify with:
```console
VHT_Corstone_SSE-300_Ethos-U55 -a ethos-u-kws.axf -f options.txt
```
## Next steps
The ML Evaluation Kit provides some stand alone examples. These building blocks have been integrated into complete software stacks in the [Open-IoT-SDK](https://github.com/ARM-software/open-iot-sdk).
