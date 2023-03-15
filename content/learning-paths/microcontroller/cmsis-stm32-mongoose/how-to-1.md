---
title: "Setup tools"
weight: 2

# FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Setup required tools

In order to complete this learning path, we need to have Git, GNU Make, ARM GCC
and STLINK installed. Below are the installation instructions for Mac, Windows
and Linux:

### MacOS setup instructions

Start a terminal, and execute:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install gcc make git gcc-arm-embedded stlink
```

### Linux setup instructions

Assuming Ubuntu Linux. Start a terminal, and execute:

```sh
sudo apt -y update
sudo apt -y install build-essential make gcc-arm-none-eabi stlink-tools git
```

## Windows setup instructions

- Enable "Developer Mode" in Windows 10/11, for symbolic link support.
- Install Git from https://git-scm.com/download/win. Check "Enable symlink" during installation
- Download and run [mingwInstaller.exe](https://github.com/Vuniverse0/mingwInstaller/releases/download/1.2.0/mingwInstaller.exe)
  - Set install destination to `c:\`
  - Accept suggested default settings
  - Go to `c:\mingw32\bin` folder and rename `mingw32-make.exe` to `make.exe`
  - Add `c:\mingw32\bin` to the `Path` environment variable
- Download and install [gcc-arm-none-eabi-10.3-2021.10-win32.exe](https://developer.arm.com/-/media/Files/downloads/gnu-rm/10.3-2021.10/gcc-arm-none-eabi-10.3-2021.10-win32.exe?rev=29bb46cfa0434fbda93abb33c1d480e6&hash=3C58D05EA5D32EF127B9E4D13B3244D26188713C).
  - Enable "Add path to environment variable" during the installation
- Create `c:\tools` folder.
  - Download [stlink-1.7.0.zip](https://github.com/stlink-org/stlink/releases/download/v1.7.0/stlink-1.7.0-x86_64-w64-mingw32.zip)
  and unpack `bin/st-flash.exe` into the `c:\tools` folder
  - Add `c:\tools` to the `Path` environment variable
  - If st-link does not work, that may be because of the driver issues. To
  resolve, install [Zadig](https://zadig.akeo.ie/). It
  will detect the device missing a driver and let you install a proper one.
  Try WinUSB first


## Create project folder

Create a new folder for your project - for example, "stm32-baremetal".
Inside that folder, we are going to create project files, described below.

We are going to use a
[Nucleo-H743ZI](https://www.st.com/en/evaluation-tools/nucleo-h743zi.html)
development board for this example, but you can follow it using any other
Nucleo development board with an Ethernet interface.

NOTE: all source code in this learning path is (c) Cesanta Software Limited,
under the MIT License. The Mongoose Library used to create a web server is
licensed under the [dual GPLv2/commercial license](https://mongoose.ws/licensing/)
