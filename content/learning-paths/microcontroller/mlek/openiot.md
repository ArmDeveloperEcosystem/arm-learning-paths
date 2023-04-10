---
# User change
title: "Building Open-IoT-SDK examples"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

The [Arm Open-IoT-SDK](https://github.com/ARM-software/open-iot-sdk) provides a growing number of complete software stack examples for you to use as the basis of your own IoT applications. 

## Before you begin 

The Arm Open-IoT-SDK is designed for use with Arm Virtual Hardware. 

Refer the previous topic, [Using the ML Evaluation Kit](/learning-paths/microcontroller/mlek/mleval/), for the links to setup Arm Virtual Hardware.

## Install the required software

Install the required python software:

```console
sudo apt update
sudo apt install python3.8-venv -y
python3.8 -m pip install imgtool cbor2
python3.9 -m pip install imgtool cffi intelhex cbor2 cbor pytest click
```

Modify the `PATH` environment variable to make python user packages visible in the shell:

```console
export PATH=$PATH:/home/ubuntu/.local/bin
```

## Clone the example repository

Clone the example repository, and navigate to the examples folder.

```console
git clone https://github.com/ARM-software/open-iot-sdk
cd open-iot-sdk/examples
```

Navigate to the desired example (`ats-keyword` in used here):

```console
cd ats-keyword
```

## Prepare build

For convenience a script `ats.sh` is provided to configure, build, and run all examples.

You must first synchronize git submodules, and apply required patches, which you can do with:

```console
./ats.sh bootstrap
```

You are now ready to build the examples.

## Build an example

Use the `ats.sh` script to build the `Keyword Spotting` (`kws`) example. This will take a few minutes to complete.

```console
./ats.sh build kws
```

## Run the example on Arm Virtual Hardware

To run the `kws` example on `Arm Virtual Hardware for Corstone-300`:

```console
./ats.sh run kws
```

The output will be similar to:

```output
...
*** ML interface initialised
ML_HEARD_ON
INFO - For timestamp: 0.000000 (inference #: 0); label: on, score: 0.996094; threshold: 0.900000
INFO - For timestamp: 0.500000 (inference #: 1); label: on, score: 0.996094; threshold: 0.900000
INFO - For timestamp: 1.000000 (inference #: 2); label: on, score: 0.917969; threshold: 0.900000
ML_HEARD_OFF
INFO - For timestamp: 1.500000 (inference #: 3); label: off, score: 0.996094; threshold: 0.900000
...
```

Full details of the operation of the example are given in the supplied `README.md`.
