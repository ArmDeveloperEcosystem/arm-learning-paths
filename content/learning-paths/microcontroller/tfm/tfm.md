---
# User change
title: "Build and run TF-M test cases"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Trusted Firmware-M](https://www.trustedfirmware.org/projects/tf-m/) (TF-M) implements the Secure Processing Environment (SPE) for Armv8-M, Armv8.1-M architectures. It is the platform security architecture reference implementation aligning with [PSA Certified](https://www.psacertified.org/) guidelines.

You will build the supplied reference examples, and run them on the [Corstone-300](https://developer.arm.com/Processors/Corstone-300) Fixed Virtual Platform (FVP).

These instructions assume an Ubuntu Linux host machine, or use of [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware).

## Corstone-300 FVP {#fvp}

The Corstone-300 FVP is available from the [Arm Ecosystem FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) page. For installation instructions see [this article](/install-tools/ecosystem_fvp/).

Alternatively, you can access the FVP with [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware). For setup instructions see [here](/install-tools/avh#corstone).

## Install appropriate compiler

The examples can be built with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain). Both toolchains are installed within Arm Virtual Hardware.

To install locally see:
- [Arm Compiler for Embedded](/install-tools/armclang/) or
- [Arm GNU Toolchain](/install-tools/gcc/#Arm-GNU)

## Prerequisites

Install `python 3` prerequisites for TF-M:
```console
sudo apt update
sudo apt install -y python3.8-venv
sudo ln -s /usr/local/bin/pip3 /usr/bin/pip3.8
python3.8 -m pip install imgtool cbor2
python3.9 -m pip install imgtool cffi intelhex cbor2 cbor pytest click
```

## Clone the TF-M repository
```console
git clone https://git.trustedfirmware.org/TF-M/trusted-firmware-m.git
cd trusted-firmware-m
```
TF-M uses `cmake` as the build system. Install if necessary, then create and navigate into a build directory.
```console
sudo apt install -y cmake
mkdir cmake_build
cd cmake_build
```
Set the relevant `cmake` variables to build the TF-M suite of tests. The `TFM_TOOLCHAIN_FILE` parameter is used to select a toolchain. For example:

```console
cmake .. -DTFM_PLATFORM=arm/mps3/an552 -DTEST_NS=ON -DTEST_S=ON -DTFM_TOOLCHAIN_FILE=toolchain_ARMCLANG.cmake
```
All the parameters are defined in the Trusted Firmware-M [documentation](https://tf-m-user-guide.trustedfirmware.org/docs/getting_started/tfm_build_instruction.html).

## Build using make
```console
make install
```
On a successful build, the TF-M test binaries are created in the `bin` directory. This includes binaries files for the `MCUBoot bootloader`, `TF-M secure firmware` and `TF-M non-secure` app. Signed variants of both the TF-M secure and non-secure images are created along with a combined signed image of both the secure and non-secure image.

## Run the TF-M tests on the Corstone-300 FVP

To run the tests on the FVP use:

### Standalone
```console
FVP_Corstone_SSE-300_Ethos-U55 -a cpu0*="bin/bl2.axf" --data "bin/tfm_s_ns_signed.bin"@0x01000000
```
### Within Arm Virtual Hardware
```console
VHT_Corstone_SSE-300_Ethos-U55 -a cpu0*="bin/bl2.axf" --data "bin/tfm_s_ns_signed.bin"@0x01000000
```
where:
- `bl2.axf` is the MCUBoot bootloader image.
- `tfm_s_ns_signed.bin` is the combined signed image for the TF-M secure and non-secure image
  - `@<addr>` indicates where in the Corstone-300 FVP memory the image is loaded. 

The memory map for the FVP is documented [here](https://developer.arm.com/documentation/100966/1118/Arm--Corstone-SSE-300-FVP/Memory-map-overview-for-Corstone-SSE-300).

The test results will be output in a `telnet` window.

```
*** Non-secure test suites summary ***
Test suite 'SFN Backend NS test (TFM_NS_SFN_TEST_1XXX)' has PASSED
Test suite 'PSA protected storage NS interface tests (TFM_NS_PS_TEST_1XXX)' has PASSED
...
```
