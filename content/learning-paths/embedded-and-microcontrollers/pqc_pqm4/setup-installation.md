---
title: Set up the pqm4 development environment

weight: 3

layout: learningpathall
---

## Download and install dependencies for pqm4

In this section, you'll install all dependencies needed to build and run pqm4. 

You'll need Python 3.8 or higher on your host machine. You'll also need one of the following to run pqm4:

- A physical Arm Cortex-M4 development board such as NUCLEO-L4R5ZI (the pqm4 default), NUCLEO-L476RG, or STM32F4 Discovery, plus stlink or OpenOCD for flashing
- QEMU, if you want to simulate a Cortex-M4 environment using the `mps2-an386` platform without physical hardware

After downloading and installing dependencies, follow the steps to configure either a physical board or QEMU. 

### Install the Arm GNU Toolchain

Follow the [Arm GNU Toolchain install guide](https://learn.arm.com/install-guides/gcc/arm-gnu/) to install `arm-none-eabi-gcc` on your host machine.

{{% notice Note %}}
Use toolchain version 12.x. Other versions may work but have not been tested.
{{% /notice %}}

Verify the installation by running:

```bash
arm-none-eabi-gcc --version
```

The output is similar to:

```output
arm-none-eabi-gcc (Arm GNU Toolchain 12.3.Rel1) 12.3.1 20230626
Copyright (C) 2022 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```
### Download pqm4 and submodules

Clone the pqm4 repository including all submodules:

```bash
git clone --recursive https://github.com/mupq/pqm4.git
cd pqm4
```

### Install Python dependencies

Create a virtual environment inside the pqm4 directory and install the required modules:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pyserial tqdm
```

Activate the virtual environment each time you open a new terminal before running pqm4 Python scripts:

```bash
source venv/bin/activate
```

## Configure a physical board

If you're using a physical development board, follow these steps to configure it.

### Install stlink 

Install stlink using your package manager.

On Linux:

```bash
sudo apt-get install stlink-tools
```

On macOS:

```bash
brew install stlink
```

If you need to build from source on Linux:

```bash
sudo apt-get install libusb-1.0-0-dev -y
git clone https://github.com/stlink-org/stlink.git
cd stlink
make release
```

Verify the connection to your board:

```bash
st-info --probe
```

The output is similar to:

```output
Found 1 stlink programmers
```

### (Optional) Install OpenOCD 

If you are using a physical board and stlink does not support it, install OpenOCD as an alternative.

On Linux:

```bash
sudo apt-get install openocd -y
```

On macOS:

```bash
brew install openocd
```

If your package manager provides an older version that doesn't support your board, you can build from source instead:

```bash
sudo apt install libjim-dev libtool-bin -y
git clone https://github.com/openocd-org/openocd.git
cd openocd
./bootstrap
./configure
make
sudo make install
```

### (Optional) Install ChipWhisperer 

ChipWhisperer is required only if you're using the `cw308t-stm32f3` platform. If you're using another board such as NUCLEO or STM32 Discovery, skip this section.

Install it using pip:

```bash
python3 -m pip install chipwhisperer
```


### Build for a target platform

Build pqm4 by specifying the platform identifier for your board using the `PLATFORM` variable.

For NUCLEO-L4R5ZI (the pqm4 default):

```bash
make -j4 PLATFORM=nucleo-l4r5zi
```

For NUCLEO-L476RG:

```bash
make -j4 PLATFORM=nucleo-l476rg
```

For STM32F4 Discovery:

```bash
make -j4 PLATFORM=stm32f4discovery
```
For a full list of supported platforms, see the [pqm4 README](https://github.com/mupq/pqm4).

### Configure the serial port 

The script `host_unidirectional.py` uses a default serial port (often `/dev/ttyUSB0`) which might not match your system. Update it to match your board's serial port.

On macOS:

```bash
ls /dev/tty.*
```

On Linux:

```bash
ls /dev/ttyACM* /dev/ttyUSB*
```

Open the script:

```bash
nano hostside/host_unidirectional.py
```

Update this line with your actual port:

```python
dev = serial.Serial("/dev/tty.usbmodemXXXX", 38400)
```

### Flash and verify communication

Connect the board to your host machine using the mini-USB port to provide power and enable flashing.

Flash a test binary:

```bash
st-flash write bin/boardtest.bin 0x8000000
```

Read the output from the board:

```bash
python3 hostside/host_unidirectional.py
```

Press the RESET button on the board. The output is similar to:

```output
Hello world
Stack Size
Random number
```

If you see this output, your board is flashed, communicating over serial, and ready to run pqm4. 

## Configure QEMU

If you're using QEMU instead of a physical board, follow these steps:

### Install QEMU

Install QEMU to simulate a Cortex-M4 environment using the `mps2-an386` machine type.

On macOS:

```bash
brew install qemu
```

On Linux:

```bash
sudo apt-get install qemu-system-arm -y
```

### Build for a target platform

Build pqm4 by specifying the platform identifier for QEMU simulation using the `PLATFORM` variable:

```bash
make -j4 PLATFORM=mps2-an386
```

For a full list of supported platforms, see the [pqm4 README](https://github.com/mupq/pqm4).

Communication with QEMU is covered in the next section.

## What you've accomplished and what's next

You've now installed the Arm GNU Toolchain, installed required Python dependencies, and cloned the pqm4 repository. You've also set up either a physical Arm Cortex-M4 development board or QEMU to build and run pqm4.

Next, you'll run the pqm4 test suite and benchmarks to measure the performance of post-quantum algorithms.