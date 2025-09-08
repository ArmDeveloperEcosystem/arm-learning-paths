---
# User change
title: "Build and run CMSIS-DSP tests on Corstone-300 FVP"
draft: true
weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The [CMSIS-DSP tests](https://github.com/ARM-software/CMSIS-DSP/blob/main/Testing) are publicly available, and are used for validation of the library. They can be run on the [Corstone reference systems](https://www.arm.com/products/silicon-ip-subsystems/), for example [Corstone-300](https://developer.arm.com/Processors/Corstone-300) Fixed Virtual Platform (FVP).

These tests are primarily for Arm internal use, but users can replicate if they wish. Else proceed to the [next step](/learning-paths/embedded-and-microcontrollers/cmsis-dsp/_review/).

These instructions assume an Ubuntu Linux host machine, or use of [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware).

## Corstone-300 FVP {#fvp}

The Corstone-300 FVP is available from the [Arm Ecosystem FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) page. Setup instructions are given in the [install guide](/install-guides/fm_fvp).

Alternatively, you can access the FVP with [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware). Setup instructions are given in the [Arm Virtual Hardware install guide](/install-guides/avh#corstone).

## Select toolchain

The examples can be built with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded)(default) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain).

Both toolchains are installed within Arm Virtual Hardware.

To install locally see:
- [Arm Compiler for Embedded](/install-guides/armclang/) or
- [Arm GNU Toolchain](/install-guides/gcc/arm-gnu/)

## Setup the CMSIS-DSP test suite

Install python 3 prerequisites for the CMSIS-DSP test suite:
```console
sudo apt update
sudo ln -s /usr/local/bin/pip3 /usr/bin/pip3.8
pip install --upgrade pip
pip install pyparsing
pip install Colorama
```

Next, clone the CMSIS-DSP git repository:
```console
git clone https://github.com/ARM-software/CMSIS-DSP/
```

Now, build the test framework and generate all the C files needed using the steps below:
```console
cd CMSIS-DSP/Testing
./createDefaultFolder.sh
python preprocess.py -f desc.txt
python preprocess.py -f desc_f16.txt -o Output_f16.pickle
python processTests.py -e
python processTests.py -e -f Output_f16.pickle
```

## Select and build a test suite

Select the test suite you would like to build the tests for.

For example, run the command below to build all the BasicTests for F32 data type
```console
python processTests.py -e BasicTestsF32
```

CMSIS-DSP repository has a cmsis_build directory with all the files to build the tests for different AVH simulation targets. Run the commands below to first install the CMSIS-DSP pack and then build the selected tests for Corstone-300 AVH FVP.

Check the [CMSIS-DSP GitHub project](https://github.com/ARM-software/CMSIS-DSP/releases) for the latest released version.

```console
cd cmsis_build
cpackget pack add https://github.com/ARM-software/CMSIS-DSP/releases/download/v1.14.4/ARM.CMSIS-DSP.1.14.4.pack
cbuild.sh "test.Release+VHT-Corstone-300.cprj"  --outdir=Objects --intdir=Tmp --packs
```
The output executables from the build are created in the `Objects` directory as specified by the command.

## Run the CMSIS-DSP tests on the Corstone-300 FVP

The CMSIS-DSP suite of tests are ready to be run on the Corstone-300 FVP that is already installed on the AMI.

Use a command such as the below to run:

```console
VHT_Corstone_SSE-300_Ethos-U55 -a Objects/test.axf -f configs/ARM_VHT_Corstone_300_config.txt > results.txt
````

You will see raw output similar to the below in the `results.txt` file. This output needs be post-processed to understand the results.

```
S: g 1
S: g 1
S: g 6
S: s 2
S: t
S: 1 0 0 362 Y
E:
b
S: t
S: 2 0 0 494 Y
E:
...
```

To post-process the raw output and view the results, run the command below:

```console
python ../processResult.py -f ../Output.pickle -e -r results.txt
```

Now, you will see the test pass/fail status for each of the CMSIS-DSPs tests that you run.

```
Group : Root  (1)
  Group : DSP Tests  (1)
    Group : Basic Tests  (6)
      Suite : Basic Tests F32 (2)
        Test nb=3    arm_add_f32 (test_add_f32 - 1) : PASSED (cycles = 362)
        Test nb=4n   arm_add_f32 (test_add_f32 - 2) : PASSED (cycles = 494)
        Test nb=4n+1 arm_add_f32 (test_add_f32 - 3) : PASSED (cycles = 580)
        Test nb=3    arm_sub_f32 (test_sub_f32 - 4) : PASSED (cycles = 361)
        Test nb=4n   arm_sub_f32 (test_sub_f32 - 5) : PASSED (cycles = 496)
        Test nb=4n+1 arm_sub_f32 (test_sub_f32 - 6) : PASSED (cycles = 582)
        Test nb=3    arm_mult_f32 (test_mult_f32 - 7) : PASSED (cycles = 325)
...
```
{{% notice  Note%}}
A warning will be generated to say that the cycle information is not accurate on the FVP. This can be ignored for the purposes of pass/fail.

`The cycles displayed by this script must not be trusted.`

`They are just an indication. The timing code has not yet been validated.`
{{% /notice %}}
