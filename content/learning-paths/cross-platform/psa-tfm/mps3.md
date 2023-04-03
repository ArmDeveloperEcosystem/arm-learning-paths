---
# User change
title: Build and run Trusted Firmware on the MPS3

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The default build for MPS3 will run as per the FVP. If you just wish to build that, jump to [here](#build).

However the MPS3 FPGA image implements CoreSight [SDC-600](https://www.arm.com/en/products/silicon-ip-system/coresight-debug-trace/sdc-600) Secure Debug Channel.

Used in conjunction with [Arm Development Studio](https://www.arm.com/products/development-tools/embedded-and-software/arm-development-studio), it can be used to demonstrate the use of [PSA-ADAC Authenticated Debug](https://developer.arm.com/documentation/107745/latest/Platform-Security-Architecture-Authenticated-Debug-Access-Control).

## Configure build to enable SDC-600

Navigate into the build recipes, and locate `trusted-firmware-m.inc`:
```console
cd /meta-arm/meta-arm/recipes-bsp/trusted-firmware-m
ls
```
Modify `trusted-firmware-m.inc` to add this macro to the build recipe:
```console
# Enable Authenticated Debug
EXTRA_OEMAKE += "-DPLATFORM_PSA_ADAC_SECURE_DEBUG=TRUE"
```

## Build software stack {#build}

{{% notice Note%}}
The build step can take over one hour to complete!
{{% /notice %}}

### Build for MPS3
```console
kas build meta-arm/kas/corstone1000-mps3.yml
```
 When complete, the binaries are generated, and can be found in this directory:
```console
/build/tmp/deploy/images/corstone1000-mps3
```
The files of interest are:
```console
bl1.bin
es_flashfw.bin
corstone1000-image-corstone1000-<timestamp>-mps3.wic.nopt
```
Because of the `8.3` naming convention of MPS3, you must rename latter files:
```console
mv es_flashfw.bin es0.bin
mv corstone1000-image-corstone1000-<timestamp>-mps3.wic.nopt cs1000.bin
```

## Set up MPS3

It is recommended to prepare files to be uploaded to MPS3 on local machine, rather than directly on MPS3.

Download [AN550](https://developer.arm.com/downloads/view/AN550) and unzip locally. If you wish to preserve the original, copy the contents of `Boardfiles` to a new directory.

### Copy binaries

Navigate to `Boardfiles\SOFTWARE`. Delete any files therein, and copy the above three binaries there.
```output
bl1.bin
es0.bin
cs1000.bin
```
### Create new image.txt

Navigate to `Boardfiles\MB\HBI0309C`. Delete (or rename) the existing `image.txt` file, and create a new one containing the following.
```console
[IMAGES]
TOTALIMAGES: 3      ;Number of Images (Max: 32)

IMAGE0PORT: 1
IMAGE0ADDRESS: 0x00_0000_0000
IMAGE0UPDATE: RAM
IMAGE0FILE: \SOFTWARE\bl1.bin

IMAGE1PORT: 0
IMAGE1ADDRESS: 0x00_0010_0000
IMAGE1UPDATE: AUTOQSPI
IMAGE1FILE: \SOFTWARE\cs1000.bin

IMAGE2PORT: 2
IMAGE2ADDRESS: 0x00_0000_0000
IMAGE2UPDATE: RAM
IMAGE2FILE: \SOFTWARE\es0.bin
```
Leave all other files as before.

### Connect MPS3 to local machine

Power-on MPS3, and connect to local machine via USB.

Four COM ports will be created, and enumerated, for example `COM0-COM3`. The exact numbers will depend on the host machine, but will always be in this order (`COM(n+0)-COM(n+3)`).

Connect to the lowest numbered port (`COM0`) with a serial terminal, such as `PuTTY`, and observe the boot sequence from whatever was previously programmed on the board.

Recommend to also connect to `COM1` and `COM2`.

| Attribute   | Setting     |
|-------------|-------------|
| Baud        | 115200      |
| Data        | 8b          |
| Stop-bits   | 1           |
| Parity      | None        |
| Flow        | None        |
| New line    | CR (COM0)   |
|             | LF (COM1-3) |

### Reprogram MPS3

When the board boots, it should be visible as a local drive named `V2M-MPS3`.

Delete all contents therein, and replace with new contents of the above `Boardfiles` directory.

If you have issues with this, you can also manually remove the micro-SD card from the board and reprogram directly with a suitable card reader.

Reboot the board, either by power-cycling, or using the `reboot` command on the terminal. The FPGA will be updated and the software stack will be executed.

Observe the steps of the secure boot process reported on the `Secure Enclave (SE)` UART (`COM1`), and Linux on the `SSE-710` UART (`COM2`).

After a few minutes you will see login terminal on the `SSE-710` UART (`COM2`).
```output
corstone1000-mps3 login:
```
Login as `root`, and proceed as you wish. For example:
```console
uname -a
```
will return:
```output
Linux corstone1000-mps3 6.1.20-yocto-standard #1 SMP PREEMPT Sat Mar 18 02:48:04 UTC 2023 aarch64 GNU/Linux
```
