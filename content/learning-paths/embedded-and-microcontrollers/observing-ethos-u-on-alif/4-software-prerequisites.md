---
# User change
title: "Install Software Prerequisites"

weight: 5

# Do not modify these elements
layout: "learningpathall"
---

To build and flash ML applications for the Alif E8 board, you need to install several software tools on your development machine.

## Install ARM GCC Toolchain

The ARM GCC toolchain compiles C/C++ code for ARM Cortex-M processors.

{{< tabpane code=false >}}
{{< tab header="macOS" >}}
Install using Homebrew:
```bash
brew install arm-none-eabi-gcc
```

Verify the installation:
```bash
arm-none-eabi-gcc --version
```

Expected output:
```output
arm-none-eabi-gcc (Homebrew GCC ARM Embedded Toolchain 13.x.x) 13.x.x
```
{{< /tab >}}

{{< tab header="Linux" >}}
Install using your package manager:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install gcc-arm-none-eabi

# Or download from ARM
wget https://developer.arm.com/-/media/Files/downloads/gnu/13.2.rel1/binrel/arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz
tar xf arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz
export PATH=$PATH:$PWD/arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi/bin
```

Verify:
```bash
arm-none-eabi-gcc --version
```
{{< /tab >}}

{{< tab header="Windows" >}}
Download and install from [ARM GNU Toolchain Downloads](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads)

After installation, add to PATH and verify:
```cmd
arm-none-eabi-gcc --version
```
{{< /tab >}}
{{< /tabpane >}}

## Install CMSIS Toolbox

The CMSIS Toolbox provides build tools for embedded projects using the CMSIS framework.

1. Download the latest release from [CMSIS-Toolbox Releases](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/releases)

2. Extract to a location on your system:

{{< tabpane code=false >}}
{{< tab header="macOS/Linux" >}}
```bash
# Extract to home directory
cd ~
tar xf cmsis-toolbox-<version>.tar.gz
```

Add to your PATH:
```bash
export PATH=$HOME/cmsis-toolbox/bin:$PATH
```

To make this permanent, add the export line to your `~/.bashrc` or `~/.zshrc`.
{{< /tab >}}

{{< tab header="Windows" >}}
Extract the zip file to `C:\cmsis-toolbox`

Add `C:\cmsis-toolbox\bin` to your system PATH.
{{< /tab >}}
{{< /tabpane >}}

3. Verify the installation:
   ```bash
   cbuild --version
   ```

   Expected output:
   ```output
   cbuild version x.x.x (C) 2024 ARM
   ```

## Install SEGGER JLink

JLink provides debugging and flashing capabilities for the Alif E8 board.

1. Download JLink from [SEGGER Downloads](https://www.segger.com/downloads/jlink/)

2. Install the package for your operating system

3. Verify the installation:
   ```bash
   JLinkExe --version
   ```

   Expected output:
   ```output
   SEGGER J-Link Commander Vx.xx (Compiled ...)
   ```

## Install Required CMSIS Packs

The Alif E8 requires specific device family packs (DFPs) for building projects.

1. Install the Alif Ensemble device pack:
   ```bash
   cpackget add AlifSemiconductor::Ensemble@2.0.4
   ```

2. Verify the pack installation:
   ```bash
   cpackget list | grep Alif
   ```

   You should see:
   ```output
   AlifSemiconductor.Ensemble 2.0.4
   ```

## Verify All Tools

Run this verification script to confirm all tools are installed:

```bash
#!/bin/bash
echo "Checking ARM GCC..."
arm-none-eabi-gcc --version | head -1

echo -e "\nChecking CMSIS Toolbox..."
cbuild --version | head -1

echo -e "\nChecking JLink..."
JLinkExe --version | head -1

echo -e "\nChecking CMSIS Packs..."
cpackget list | grep Alif
```

If all commands succeed, you're ready to proceed to building your first project.

## Troubleshooting

**Command not found errors:**
- Ensure the tool is in your system PATH
- Restart your terminal after installation
- On macOS/Linux, source your shell configuration: `source ~/.bashrc` or `source ~/.zshrc`

**CMSIS pack installation fails:**
- Check internet connection
- Try with sudo: `sudo cpackget add AlifSemiconductor::Ensemble@2.0.4`
- Clear pack cache: `cpackget clean`

**JLink connection issues:**
- Install JLink drivers separately if needed
- On Linux, add udev rules for JLink USB devices
- Check USB cable is properly connected to PRG port
