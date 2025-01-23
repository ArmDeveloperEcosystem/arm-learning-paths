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

You can use your own Ubuntu Linux host machine or use [Arm Virtual Hardware (AVH)](https://www.arm.com/products/development-tools/simulation/virtual-hardware) for this Learning Path.

The Ubuntu version should be 20.04 or 22.04. These instructions have been tested on the `x86_64` architecture. You will need a way to interact visually with your machine to run the FVP, because it opens graphical windows for input and output from the software applications.

If you want to use Arm Virtual Hardware the [Arm Virtual Hardware install guide](/install-guides/avh#corstone) provides setup instructions.

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


Both compilers are pre-installed in Arm Virtual Hardware.

### Clone the repository

Clone the ML Evaluation Kit repository, and navigate into the new directory:

```bash
git clone "https://review.mlplatform.org/ml/ethos-u/ml-embedded-evaluation-kit"
cd ml-embedded-evaluation-kit
git submodule update --init
```

### Run the build sscript

The default build is Ethos-U55  and Corstone-300. The default build for Ethos-U85 is Corstone-320. Use the `npu-config-name` flag to set Ethos-U85.

The default compiler is `gcc`, but `armclang` can also be used. Number after `ethos-u85-*` is number of MACs, 128-2048 (2^n).

You can select either compiler to build applications. You can also try them both and compare the results.

- Build with Arm GNU Toolchain (`gcc`)

```
./build_default.py --npu-config-name ethos-u85-256 --toolchain gnu
```

- Build with Arm Compiler for Embedded (`armclang`)

```console
./build_default.py --npu-config-name ethos-u85-256 --toolchain arm
```

The build will take a few minutes.

When the build is complete, you will find the examples (`.axf` files) in the `cmake-build-*/bin` directory. The `cmake-build` directory names are specific to the compiler used and Ethos-U85 configuration. Verify that the files have been created by observing the output of the `ls` command

```bash
ls cmake-build-mps4-sse-320-ethos-u85-256-gnu/bin/
```

The next step is to install the FVP and run it with these example audio clips.


## Corstone-320 FVP {#fvp}

This section describes installation of the Corstone-320 to run on your local machine. If you are using Arm Virtual Hardware, that comes with the Corstone-300 FVP pre-installed, and you can move on to the next section. You can review Arm's full FVP offer and general installation steps in the [Fast Model and Fixed Virtual Platform](/install-guides/fm_fvp) install guides.

{{% notice Note %}}
The rest of the steps for the Corstone-320 need to be run in a new terminal window.
{{% /notice %}}

Open a **new terminal window** and download the Corstone-320 archive.

```bash
cd $HOME
wget https://developer.arm.com/-/cdn-downloads/permalink/FVPs-Corstone-IoT/Corstone-320/FVP_Corstone_SSE-320_11.27_25_Linux64.tgz
```

Unpack it with `tar`, run the setup script and export the binary paths to the `PATH` environment variable.

```bash
tar -xf FVP_Corstone_SSE-320_11.27_25_Linux64.tgz
./FVP_Corstone_SSE-320.sh --i-agree-to-the-contained-eula --no-interactive -q
export PATH=$HOME/FVP_Corstone_SSE-320/models/Linux64_GCC-9.3:$PATH
```

The FVP requires an additional dependency, `libpython3.9.so.1.0`, which can be installed using a script. Note that this will tinkle with the python installation for the current terminal window, so make sure to open a new one for the next step.

```bash
source $HOME/FVP_Corstone_SSE-320/scripts/runtime.sh
```

Verify that the FVP was successfully installed by comparing your output from below command.

```bash
FVP_Corstone_SSE-320
```

```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003

```


Now you are ready to test the application with the FVP.

