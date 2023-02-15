---
# User change
title: "Create a peripheral using Virtual Input/Output (VIO)"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Arm Virtual Hardware (AVH) supports [Virtual Interfaces](https://arm-software.github.io/AVH/main/simulation/html/group__arm__cmvp.html) which can be used to simulate real world peripherals and stimuli.

## Prerequisites

A valid [AWS](https://aws.amazon.com/) account is required.

Launch the Arm Virtual Hardware AMI. For full instructions see [here](/install-tools/avh#corstone).

The example used here makes use of the [Tkinter](https://docs.python.org/3/library/tkinter.html) Python interface to Tcl/Tk, and can be installed in the AVH terminal with:
```console
sudo apt install -y python3-tk
```
## Clone the repository:

In your AVH terminal, clone the example project repository, and navigate into the `leds_example` directory.
```console
git clone https://github.com/Arm-Examples/AVH-Virtual-Peripherals
cd AVH-Virtual-Peripherals/leds_example
```
## Build and run the example

A makefile is provided to build the example project. A `run.sh` script is provided to run the example.
```console
make
./run.sh
```
You can interact with the Virtual LEDs. If they are not displayed you may need to implement a [VNC connection](/install-tools/avh#vnc) to the AVH instance.

## Understand the example

The Virtual Hardware is launched with the `-V` option which specifies the python implementation of the peripheral.

The python script(s) implement the [VIO Python interface](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vio__py.html) to communicate with the Virtual Hardware application.

In the application, signals are passed via the [VIO API](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vio__api.html) to/from the virtual peripheral.
