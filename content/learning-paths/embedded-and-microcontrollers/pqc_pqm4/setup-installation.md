---
title: Setting Up the Development Environment

weight: 3

layout: learningpathall
---

## Required Hardware and Software

Before you begin, ensure you have the following hardware and software:

- **Development Board**: ARM Cortex-M4 based board such as:
  - NUCLEO-L476RG  
  - NUCLEO-L4R5ZI (default in pqm4)  
  - STM32F4 Discovery  
- **ARM Toolchain**: arm-none-eabi toolchain  
- **Flashing Tools**: stlink or OpenOCD  
- **Python 3.8+**
- **Python Modules**: pyserial, tqdm  

## Installing the ARM Toolchain


Download the ARM GNU toolchain from the official website:

https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads

Download and install **gcc-arm-none-eabi** for your system.

Recommended version: **12.x**  
Avoid newer versions (e.g., 15.x) as they may cause build/linker issues with pqm4.

## Installing stlink

For flashing binaries, install stlink using your package manager or compile it from source:

```bash
git clone https://github.com/texane/stlink.git
cd stlink
make release
```

Verify connection

```bash
st-info --probe
```
Expected output:
Found 1 stlink programmers

## Installing OpenOCD

For the NUCLEO-L4R5ZI board, OpenOCD is used. Install it via your package manager or compile from source:

```bash
git clone http://openocd.org
cd openocd
./configure
make
```
## Installing ChipWhisperer (Optional)
The ChipWhisperer module is only required if you are using the `cw308t-stm32f3` platform.  
If you are using other boards (e.g., NUCLEO or STM32 Discovery), you can skip this step.

```bash
python3 -m pip install chipwhisperer
```

## Installing QEMU (Optional)
QEMU is required only if you are using the mps2-an386 platform (simulated ARM Cortex-M4 environment).
If you are using a physical board, you can skip this step.

For macOS: 
```bash
brew install qemu
```
For Linux:
```bash
sudo apt-get install qemu-system-arm
```
Note : Ensure the version is 5.2 or higher.

## Installing Python Dependencies

Install the required Python modules using pip:

```bash
python3 -m pip install pyserial tqdm
```

## Downloading pqm4 and Submodules

```bash
git clone --recursive https://github.com/mupq/pqm4.git  
cd pqm4

```

## Building for a Target Platform 

```bash
make -j4 PLATFORM=<platform>
```

Example for NUCLEO-L476RG board:
make -j4 PLATFORM=nucleo-l476rg


## Configuring Serial Port in host_unidirectional.py

The script `host_unidirectional.py` uses a default serial port (often `/dev/ttyUSB0`) which may not match your system.

You must update it to match your board’s serial port.

Open the file:
```bash
nano hostside/host_unidirectional.py
```
replace the port shown in below line with your actual port  
```python
dev = serial.Serial("/dev/tty.usbmodemXXXX", 38400)
```
to find your port 
```bash
ls /dev/tty.*
```


## Flashing and Testing Communication

Connect the board to your host machine using the mini-USB port. This provides it with power, and allows you to flash binaries onto the board


Flash a basic test:

```bash
st-flash write bin/boardtest.bin 0x8000000
```

Read output:

```bash
python3 hostside/host_unidirectional.py
```

Press RESET button on board 

Expected output :
```python
Hello world  
Stack Size  
Random number
```
  

