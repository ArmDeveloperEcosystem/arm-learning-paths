---
# User change
title: Run on FVP or MPS3

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
{{% notice  MPS3%}}
MPS3 users can jump to the [MPS3 section](#mps3).
{{% /notice %}}


## Run the software on Corstone-1000 FVP

When the build is complete, run the image on the FVP:

```console
kas shell meta-arm/kas/corstone1000-fvp.yml:meta-arm/ci/debug.yml -c "../meta-arm/scripts/runfvp --terminals=xterm"
```

When the boot sequence is complete, you will be presented with a login prompt.

```output
corstone1000-fvp login:
```

Login as `root`, and proceed as you wish. For example:
```console
uname -a
```
will return similar to:
```output
Linux corstone1000-fvp 6.1.20-yocto-standard #1 SMP PREEMPT Sat Mar 18 02:48:04 UTC 2023 aarch64 GNU/Linux
```


## Run software on MPS3 AN550 {#mps3}

When the MPS3 build is complete, the generated binaries can be found in this directory:
```console
/build/tmp/deploy/images/corstone1000-mps3
```
The files of interest are:
```console
bl1.bin
es_flashfw.bin
corstone1000-flash-firmware-image-corstone1000-mps3.wic
```
Because of the `8.3` naming convention of MPS3, you must rename latter files:
```console
mv es_flashfw.bin es0.bin
mv corstone1000-flash-firmware-image-corstone1000-mps3.wic cs1000.bin
```

### Set up MPS3

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

Navigate to `Boardfiles\MB\HBI0309C\AN550`. Delete (or rename) the existing `images.txt` file, and create a new one containing the following:
```console
;************************************************
;       Preload port mapping                    *
;************************************************
;  PORT 0 & ADDRESS: 0x00_0000_0000 QSPI Flash (XNVM) (32MB)
;  PORT 0 & ADDRESS: 0x00_8000_0000 OCVM (DDR4 2GB)
;  PORT 1        Secure Enclave (M0+) ROM (64KB)
;  PORT 2        External System 0 (M3) Code RAM (256KB)
;  PORT 3        Secure Enclave OTP memory (8KB)
;  PORT 4        CVM (4MB)
;************************************************

[IMAGES]
TOTALIMAGES: 3      ;Number of Images (Max: 32)

IMAGE0PORT: 1
IMAGE0ADDRESS: 0x00_0000_0000
IMAGE0UPDATE: RAM
IMAGE0FILE: \SOFTWARE\bl1.bin

IMAGE1PORT: 0
IMAGE1ADDRESS: 0x00_0000_0000
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

| Attribute | Setting     |
| --------- | ----------- |
| Baud      | 115200      |
| Data      | 8b          |
| Stop-bits | 1           |
| Parity    | None        |
| Flow      | None        |
| New line  | CR (COM0)   |
|           | LF (COM1-3) |

### Reprogram MPS3

When the board boots, it should be visible as a local drive named `V2M-MPS3`.

Delete all contents therein, and replace with new contents of the above `Boardfiles` directory.

If you have issues with this, you can also manually remove the micro-SD card from the board and reprogram directly with a suitable card reader.

Reboot the board, either by power-cycling, or using the `reboot` command on the terminal. The FPGA will be updated and the software stack will be executed.

Observe the steps of the secure boot process reported on the `Secure Enclave (SE)` UART (`COM1`), and Linux on the `SSE-710` UART (`COM2`). All components outside of the enclave are considered as less trustworthy. It is only after verification that the host is taken out of reset.

After a few minutes you will see login terminal on the `SSE-710` UART (`COM2`).
```output
corstone1000-mps3 login:
```
Login as `root`, and proceed as you wish. For example:
```console
uname -a
```
will return similar to:
```output
Linux corstone1000-mps3 6.1.20-yocto-standard #1 SMP PREEMPT Sat Mar 18 02:48:04 UTC 2023 aarch64 GNU/Linux
```

## Further reading

You have run Trusted Firmware on the Corstone-1000 FVP and/or MPS3.

Refer to the [Trusted Firmware-M User Guide](https://tf-m-user-guide.trustedfirmware.org/platform/arm/corstone1000/readme.html) for complete documentation.
