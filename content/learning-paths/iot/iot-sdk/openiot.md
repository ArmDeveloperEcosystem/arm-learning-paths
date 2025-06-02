---
# User change
title: Build and run Open-IoT-SDK examples

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Arm Total Solutions for IoT](https://www.arm.com/markets/iot/total-solutions-iot) provide reference software stacks, integrating various Arm technologies, such as [Arm Trusted Firmware-M](https://developer.arm.com/Tools%20and%20Software/Trusted%20Firmware-M) and the [Arm ML Evaluation Kit (MLEK)](https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ml-embedded-evaluation-kit).

The [Open-IoT-SDK](https://github.com/ARM-software/open-iot-sdk) is designed to be used with [Arm Virtual Hardware (AVH)](https://www.arm.com/products/development-tools/simulation/virtual-hardware), which provides [Corstone-300](https://developer.arm.com/Processors/Corstone-300) Virtual Hardware.


## Arm Virtual Hardware

Setup your AVH instance, following the instructions in the [Arm Virtual Hardware install guide](/install-guides/avh#corstone).

## Install the required software

In your AVH instance, install the required python software:

```console
sudo apt update
sudo apt install python3.8-venv -y
sudo cp /usr/local/bin/pip3.8 /usr/bin
```

Install Python packages:

```console
python3.8 -m pip install imgtool cbor2
python3.9 -m pip install imgtool cffi intelhex cbor2 cbor pytest click
```

Modify the `PATH` environment variable to make python user packages visible in the shell:

```console
export PATH=$PATH:/home/ubuntu/.local/bin
```

## Clone the example repository

Clone the example repository, and navigate to the `v8m` folder.

```console
git clone https://github.com/ARM-software/open-iot-sdk.git
cd open-iot-sdk/v8m
```

## Build an example

The projects are located in the `examples` folder. Review the list of available projects:

```console
ls examples
```

The output is:

```output
blinky  keyword  speech
```

Use the `ats.sh` script to build the examples. 

The `blinky` example demonstrates how to use Trusted Firmware-M to create secure and non-secure partitions, and blink the LED from the non-secure code.

Build `blinky` example by running:

```console
./ats.sh build blinky
```

Ignore any warnings from the build. The build takes a few minutes to complete.

## Run the example on Arm Virtual Hardware

To run the `blinky` example on `Arm Virtual Hardware for Corstone-300`:

```console
./ats.sh run blinky
```
Observe in the output that the system boots through Arm Trusted Firmware (default build uses dummy keys), before the main application.

The output will be similar to:

```output
[INF] Starting bootloader
[INF] Beginning BL2 provisioning
[WRN] TFM_DUMMY_PROVISIONING is not suitable for production! This device is NOT SECURE
[INF] Swap type: none
[INF] Swap type: none
[INF] Bootloader chainload address offset: 0x0
[INF] Jumping to the first image slot
[INF] Beginning TF-M provisioning
<NUL>[WRN] <NUL>TFM_DUMMY_PROVISIONING is not suitable for production! <NUL>This device is NOT SECURE<NUL>
<NUL>[Sec Thread] Secure image initializing!
<NUL>Booting TF-M v1.7.0+3ae2ac302
<NUL>Creating an empty ITS flash layout.
Creating an empty PS flash layout.
[INF][Crypto] Provisioning entropy seed... complete.
[DBG][Crypto] Initialising mbed TLS 3.2.1 as PSA Crypto backend library... complete.
Initialising kernel
Starting kernel and threads
The LED started blinking...
LED on
LED off
LED on
LED off
...
```

Use `Ctrl+C` to stop the simulation.
