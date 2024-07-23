---
# User change
title: "How do I install the Raspberry Pi Pico SDK?"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

The [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) is a low cost microcontroller board with a dual-core Cortex-M0+ processor, RAM, flash, and a variety of I/O options.

The Pico is a low cost board and a good way to get started learning programming for Arm Cortex-M.

The [Pico SDK](https://github.com/raspberrypi/pico-sdk) uses the GCC compiler and Cmake to build applications. 

[Getting started with Raspberry Pi Pico C/C++ development](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf) contains more details of C/C++ programming on the Pico.

## How do I use the Pico SDK installation script?

The Pico SDK installation script is managed in GitHub and is named pico_setup.sh 

The installation script is designed to run on a Debian-based Linux distribution. 

The script checks if you are running on a Raspberry Pi 3, 4, 400, or 5. There will be a warning if not, but the script will continue. 

Installation has been tested on a Raspberry Pi 4, Ubuntu 22.04 and Ubuntu 20.04.

The script installs additional software using `apt install`, clones the Pico SDK repositories from GitHub, builds examples, and installs additional tools including VS Code and openocd for debugging. 

Download the install script. 

```bash
wget https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico_setup.sh
```

On Ubuntu some additional packages are needed. Use the tabs to install extra packages. 

{{< tabpane code=true >}}
  {{< tab header="Ubuntu 22.04 or 24.04" >}}
sudo apt-get install jq minicom make cmake gdb-multiarch automake autoconf libtool libftdi-dev libusb-1.0-0-dev pkg-config clang-format -y
  {{< /tab >}}
  {{< tab header="Ubuntu 20.04" >}}
sudo apt-get install jq minicom make gdb-multiarch automake autoconf libtool libftdi-dev libusb-1.0-0-dev pkg-config clang-format -y
sudo snap install cmake --classic
  {{< /tab >}}
  {{< tab header="Raspberry Pi OS" >}}
Nothing more to install!
  {{< /tab >}}
{{< /tabpane >}}


Use variables to skip the VS Code and UART software installation on Ubuntu. 

If desired, VS Code can be installed from the [download area](https://code.visualstudio.com/download) instead. 

The UART is not needed because a non-Raspberry Pi computer doesn't have the I/O pins to the connect to the Pico UART.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu 20.04, 22.04 or 24.04" >}}
SKIP_VSCODE=1 SKIP_UART=1 bash ./pico_setup.sh
  {{< /tab >}}
  {{< tab header="Raspberry Pi OS" >}}
bash ./pico_setup.sh
  {{< /tab >}}
{{< /tabpane >}}


## How do I verify that the Pico SDK development tools work?

Before continuing, confirm the required tools are operational. 

Source the new .bashrc file as new variables are added by the Pico SDK.

```bash
source ~/.bashrc
```

There are four added variables. Display them with the `env` command.

```bash
env | grep PICO
```

Here is the output.

```output
PICO_EXTRAS_PATH=/home/pi/pico/pico-extras
PICO_SDK_PATH=/home/pi/pico/pico-sdk
PICO_PLAYGROUND_PATH=/home/pi/pico/pico-playground
PICO_EXAMPLES_PATH=/home/pi/pico/pico-examples
```

Each tool should run and return a message about the version installed. 

```bash
arm-none-eabi-gcc --version
```

```bash
gdb-multiarch --version
```

```bash
cmake --version
```

```bash
openocd --version
```

## How do I install the Pico SDK on other operating systems? 

If you are not using Linux there are instructions included in the Getting Started guide referenced above. Instructions are available for Microsoft Windows and Apple macOS.

