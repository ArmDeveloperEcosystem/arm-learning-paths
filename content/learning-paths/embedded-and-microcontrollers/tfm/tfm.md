---
# User change
title: "Build and run TF-M tests and example application"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Trusted Firmware-M](https://www.trustedfirmware.org/projects/tf-m/) (TF-M) implements the Secure Processing Environment (SPE) for Armv8-M, Armv8.1-M architectures. It is the platform security architecture reference implementation aligning with [PSA Certified](https://www.psacertified.org/) guidelines.

You will build the supplied tests and reference example, and run them on the [Corstone-300](https://developer.arm.com/Processors/Corstone-300) Fixed Virtual Platform (FVP).

These instructions assume an Ubuntu 22.04-LTS-jammy Linux machine.

## Prerequisites

Ensure the system is up to date:

```bash
sudo apt update
```

### Corstone-300 FVP {#fvp}

The Corstone-300 FVP is available from the [Arm Ecosystem FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) page and can be installed following the instructions from the [install guide](/install-guides/fm_fvp).

### Compiler

TF-M can be built with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain).

To install locally follow the instructions from:
- [Arm Compiler for Embedded](/install-guides/armclang/) or
- [Arm GNU Toolchain](/install-guides/gcc/arm-gnu/)

### Build system

TF-M uses `cmake` as the build system, and TF-M tests require `cmake` > 3.21 or higher.

On Ubuntu 22.04-LTS, `cmake` can be installed if necessary with:

```bash
sudo apt install -y cmake
```

### Clone the TF-M repositories

Clone the TF-M repositories that need and pin them to version `2.0.0` :

```bash
git clone -b TF-Mv2.0.0 https://git.trustedfirmware.org/TF-M/trusted-firmware-m.git
git clone -b TF-Mv2.0.0 https://git.trustedfirmware.org/TF-M/tf-m-tests.git
git clone -b TF-Mv2.0.0 https://git.trustedfirmware.org/TF-M/tf-m-extras.git
```

### Python packages

Install `python 3` prerequisites for TF-M in a virtual environment in order not to clutter your system:

```bash
sudo apt install -y python3-venv python3-pip
python3 -m venv myvenv
myvenv/bin/pip3 install -r trusted-firmware-m/tools/requirements.txt
```

## Configure and build the TF-M tests

Activate the python environment, navigate to the test suite we want to build and run and set the relevant `cmake` variables to build TF-M and its suite of tests. The `TFM_TOOLCHAIN_FILE` parameter is used to select a toolchain. The build is done in `Debug` mode in order to get progresses and results displayed when they will be executed. All the parameters are defined in the [Trusted Firmware-M documentation](https://tf-m-user-guide.trustedfirmware.org/getting_started/index.html#build-and-run-instructions). For example, to build with Arm GNU Compiler:

```bash
. myvenv/bin/activate

mkdir build
cmake -S tf-m-tests/tests_reg/spe -B build/tests-spe \
      -DCMAKE_BUILD_TYPE=Debug \
      -DTFM_PLATFORM=arm/mps3/corstone300/fvp \
      -DTFM_PROFILE=profile_small \
      -DTFM_TOOLCHAIN_FILE=$PWD/trusted-firmware-m/toolchain_GNUARM.cmake \
      -DCONFIG_TFM_SOURCE_PATH=$PWD/trusted-firmware-m \
      -DTEST_S=ON -DTEST_NS=ON
cmake --build build/tests-spe -- install

cmake -S tf-m-tests/tests_reg -B build/tests \
      -DCMAKE_BUILD_TYPE=Debug \
      -DCONFIG_SPE_PATH=$PWD/build/tests-spe/api_ns
cmake --build build/tests
```

Or, alternatively, for building with `armclang`, use `$PWD/../../trusted-firmware-m/toolchain_ARMCLANG.cmake` for `TFM_TOOLCHAIN_FILE`.

On a successful build, the TF-M test executables are created in the `build/tests-spe` and `build/tests` directories. This includes binary files for the `MCUBoot bootloader`, `TF-M secure firmware` and `TF-M non-secure` app. Signed variants of both the TF-M secure and non-secure images are created along with a combined signed image of both the secure and non-secure image.

## Run the TF-M tests on the Corstone-300 FVP

The tests we have just built can now be run on the Corstone-300 FVP. This is done by providing the following arguments to the FVP:
- `build/tests-spe/bin/bl2.axf` is the MCUBoot bootloader image.
- `build/tests/tfm_s_ns_signed.bin` is the combined signed image for the TF-M secure and non-secure image.
- `@<addr>` indicates where in the Corstone-300 FVP memory the image is loaded. The memory map for the FVP is documented in the [FVP Reference Guide](https://developer.arm.com/documentation/100966/1118/Arm--Corstone-SSE-300-FVP/Memory-map-overview-for-Corstone-SSE-300).
- the GUI is disabled with parameter `mps3_board.visualisation.disable-visualisation`
- the tests' outputs is redirected to the standard output with parameters `mps3_board.telnetterminal0.start_telnet` and `mps3_board.uart0.out_file`. Otherwise, the FVP will launch an `xterm` and use a `telnet` connection to display the log, which may not work if your environment does not have an X display.

```console
FVP_Corstone_SSE-300_Ethos-U55 \
  -a cpu0*=build/tests-spe/bin/bl2.axf \
  --data build/tests/tfm_s_ns_signed.bin@0x38000000 \
  -C mps3_board.visualisation.disable-visualisation=1 \
  -C mps3_board.telnetterminal0.start_telnet=0 \
  -C mps3_board.uart0.out_file=/dev/stdout
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003

    Ethos-U rev 136b7d75 --- Apr 12 2023 13:44:01
    (C) COPYRIGHT 2019-2023 Arm Limited
    ALL RIGHTS RESERVED

[INF] Starting bootloader
[INF] Beginning BL2 provisioning
[WRN] TFM_DUMMY_PROVISIONING is not suitable for production! This device is NOT SECURE
[INF] Image index: 0, Swap type: none
[INF] Bootloader chainload address offset: 0x0
[INF] Jumping to the first image slot
[INF] Beginning TF-M provisioning
<NUL>[WRN] <NUL>TFM_DUMMY_PROVISIONING is not suitable for production! <NUL>This device is NOT SECURE<NUL>
<NUL>[WRN] <NUL>This device was provisioned with dummy keys. <NUL>This device is NOT SECURE<NUL>
<NUL>[Sec Thread] Secure image initializing!
<NUL>TF-M isolation level is: <NUL>0x00000001
Booting TF-M v2.0.0
<NUL>[SFN Test partition] SFN Test Partition initialized.
Creating an empty ITS flash layout.
[INF][Crypto] Provisioning entropy seed... complete.
[DBG][Crypto] Initialising Mbed TLS 3.5.0 as PSA Crypto backend library... complete.

#### Execute test suites for the Secure area ####
Running Test Suite PSA internal trusted storage S interface tests (TFM_S_ITS_TEST_1XXX)...
> Executing 'TFM_S_ITS_TEST_1001'
  Description: 'Set interface'
  TEST: TFM_S_ITS_TEST_1001 - PASSED!
...
TESTSUITE PASSED!
Running Test Suite Symmetric key algorithm based Initial Attestation Service non-secure interface tests (TFM_NS_ATTEST_TEST_2XXX)...
> Executing 'TFM_NS_ATTEST_TEST_2001'
  Description: 'Symmetric key algorithm based Initial Attestation test'
  TEST: TFM_NS_ATTEST_TEST_2001 - PASSED!
TESTSUITE PASSED!

*** Non-secure test suites summary ***
Test suite 'SFN Backend NS test (TFM_NS_SFN_TEST_1XXX)' has PASSED
Test suite 'PSA internal trusted storage NS interface tests (TFM_NS_ITS_TEST_1XXX)' has PASSED
Test suite 'Crypto non-secure interface test (TFM_NS_CRYPTO_TEST_1XXX)' has PASSED
Test suite 'Symmetric key algorithm based Initial Attestation Service non-secure interface tests (TFM_NS_ATTEST_TEST_2XXX)' has PASSED

*** End of Non-secure test suites ***
^C
Stopping simulation...


Info: /OSCI/SystemC: Simulation stopped by user.
```

Congratulations, you have successfully ran some of the TF-M tests (some other test suite, like the PSA tests, are also available in the `tf-m-tests` repository).

# Configure, build and run the TF-M example application

Now that the tests are passing, let's build and run the TF-M example application !

```bash
cmake -S trusted-firmware-m -B build/spe \
      -DCMAKE_BUILD_TYPE=Debug \
      -DTFM_PLATFORM=arm/mps3/corstone300/fvp \
      -DTFM_PROFILE=profile_small \
      -DTFM_TOOLCHAIN_FILE=$PWD/trusted-firmware-m/toolchain_GNUARM.cmake
cmake --build build/spe -- install
```

The `CMakeLists.txt` for the TF-M example application requires a minor fix for the build to go smoothly. In `tf-m-extras/examples/tf-m-example-ns-app/CMakeLists.txt`, move command `add_subdirectory(${CONFIG_SPE_PATH} ${CMAKE_BINARY_DIR}/spe)` (at line 36) *after* the next statement (`add_executable(tfm_ns ...)` ). We can now build the application with:

```bash
cmake -S tf-m-extras/examples/tf-m-example-ns-app -B build/example \
      -DCMAKE_BUILD_TYPE=Debug \
      -DCONFIG_SPE_PATH=$PWD/build/spe/api_ns
cmake --build build/example
```

To run the image on the FVP, the command line is very similar to the one we used with the tests, we only have to change the paths to the example application images:

```console
FVP_Corstone_SSE-300_Ethos-U55 \
  -a cpu0*=build/spe/bin/bl2.axf \
  --data build/example/tfm_s_ns_signed.bin@0x38000000 \
  -C mps3_board.visualisation.disable-visualisation=1 \
  -C mps3_board.telnetterminal0.start_telnet=0 \
  -C mps3_board.uart0.out_file=/dev/stdout
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003

    Ethos-U rev 136b7d75 --- Apr 12 2023 13:44:01
    (C) COPYRIGHT 2019-2023 Arm Limited
    ALL RIGHTS RESERVED

[INF] Starting bootloader
[INF] Beginning BL2 provisioning
[WRN] TFM_DUMMY_PROVISIONING is not suitable for production! This device is NOT SECURE
[INF] Image index: 0, Swap type: none
[INF] Bootloader chainload address offset: 0x0
[INF] Jumping to the first image slot
[INF] Beginning TF-M provisioning
<NUL>[WRN] <NUL>TFM_DUMMY_PROVISIONING is not suitable for production! <NUL>This device is NOT SECURE<NUL>
<NUL>[WRN] <NUL>This device was provisioned with dummy keys. <NUL>This device is NOT SECURE<NUL>
<NUL>[Sec Thread] Secure image initializing!
<NUL>TF-M isolation level is: <NUL>0x00000001
Booting TF-M v2.0.0
<NUL>Creating an empty ITS flash layout.
[INF][Crypto] Provisioning entropy seed... complete.
[DBG][Crypto] Initialising Mbed TLS 3.5.0 as PSA Crypto backend library... complete.
Non-Secure system starting...
Hello TF-M world
FW  version = 257
Testing psa get random number...
1: psa_generate_random() = 254
2: psa_generate_random() = 214
3: psa_generate_random() = 129
4: psa_generate_random() = 226
5: psa_generate_random() = 102
End of TF-M example App
^C
Stopping simulation...


Info: /OSCI/SystemC: Simulation stopped by user.
[warning ][main@0][1298 ns] Simulation stopped by user
```

Congratulations, you have built and run your first TF-M application !
