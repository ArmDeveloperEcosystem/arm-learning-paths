---
title: Development platforms

weight: 3

# Do not modify these elements
layout: "learningpathall"
---
You must select an appropriate platform on which to develop your ML application. There are a number of physical and virtual solutions available.

## Physical Hardware
There are very many Cortex-M microcontrollers with available [development boards](/learning-paths/embedded-and-microcontrollers/intro/). However there are currently a limited number of readily available development boards available with Ethos-U processors. Board choices are likely to increase, but today developers have limited options for software development.

### MPS3 FPGA prototyping board

The [Arm MPS3 FPGA Prototyping Board](https://www.arm.com/products/development-tools/development-boards/mps3/) can be programmed with [FPGA images](https://developer.arm.com/downloads/-/download-fpga-images/) for the for the Corstone-300, Corstone-310 and Corstone-1000 reference packages. The FPGA images are good for early software development.

MPS3 is the recommended solution for evaluating performance, but boards are in short supply and may be difficult to obtain.

## Virtual Hardware

Virtual implementations of the Corstone reference systems are also available for software development. These can be accessed locally or in the cloud.

### Ecosystem FVPs

Ecosystem FVPs are free-of-charge and target a variety of applications. They run on Linux and Windows.

The Corstone reference systems are available on the [Arm Ecosystem FVP page](https://developer.arm.com/downloads/-/arm-ecosystem-fvps/). General ecosystem FVP setup instructions are provided in the [install guide](/install-guides/fm_fvp/eco_fvp/).

The Ecosystem FVP can be used in conjunction with [Keil MDK](https://developer.arm.com/Tools%20and%20Software/Keil%20MDK) or [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio).

Keil MDK Professional Edition also provides these virtual platforms.

### Arm Virtual Hardware

[Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware/) provides two cloud-based solutions to access Corstone reference systems. These are intended for use as software test and validation environments suitable for CI/CD integration.

Both versions of AVH offer FVPs. Choose the one which best matches your preferences. You can use your AWS account and pay for the compute you use or pay for the hardware-as-a-service directly using your Arm account. Both methods offer free trials.

The marketing information provides more details about the similarities and differences.

- [Arm Virtual Hardware Corstone and CPUs](#aws) AWS AMI (Amazon Machine Image) provides Virtual Hardware Targets (`VHT`) in a cloud instance (virtual machine). The AMI is available in the [AWS marketplace](https://aws.amazon.com/marketplace/pp/prodview-urbpq7yo5va7g/).

- [Arm Virtual Hardware Third-Party Hardware](#3rdparty) uses hypervisor technology to model real hardware provided by Arm’s partners. It also offers FVPs as part of the cloud service.

#### Arm Virtual Hardware Corstone and CPUs (AWS AMI) {#aws}

Follow the [Arm Virtual Hardware Corstone install guide](/install-guides/avh/#corstone) to get started with AVH on AWS.

The following executables are provided:
* `VHT_Corstone_SSE-300_Ethos-U55`
* `VHT_Corstone_SSE-300_Ethos-U65`
* `VHT_Corstone_SSE-310_Ethos-U65`

When you launch a model:
```console
VHT_Corstone_SSE-300_Ethos-U55
```
It will display output similar to:
```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003

    Ethos-U rev 136b7d75 --- Feb 16 2022 15:47:15
    (C) COPYRIGHT 2019-2022
```
{{% notice Visualization %}}

A visualization of the FVP will also be displayed on the Linux desktop.

To disable this, which should allow the FVP to startup more quickly, add:

`-C mps3_board.visualisation.disable-visualisation=1`

to the command line.
{{% /notice %}}

Terminate the FVP with `Ctrl+C`.

If you can start the FVPs you are ready for ML application development.

#### Arm Virtual Hardware Third-Party Hardware {#3rdparty}

Arm Virtual Hardware Third-Party Hardware is currently in public beta.

[Log in to AVH](https://app.avh.arm.com/login/) using your Arm account or create a new one using the `Create an Arm account` link.

After log in, you can use the AVH console to create a new device and select `Corstone-300fvp` or `Corstone-310fvp`.

You can use the AVH console to upload software and control FVP execution.

There is also documentation available in the console you can read to continue learning about AVH.

If you are in the console and can see the FVPs, you are ready for ML application development.


## FVP configuration options

These virtual platforms have some options to help you evaluate different configurations.

The [AVH simulation model documentation](https://arm-software.github.io/AVH/main/simulation/html/Using.html) has many good tips.

### Number of MACs

Ethos-U55 and Ethos-U65 offer a configurable number of MACs (multiply-accumulate units). During IP evaluation and performance analysis you need to understand the numbers of MACs available in the hardware and create your software to use the same configuration.

| Ethos-U NPU | Number of MACs supported    |
| ----------- | -----------                 |
| Ethos-U55   | 32, 64, 128, 256            |
| Ethos-U65   | 256, 512                    |

FVP and VHT platforms can be configured with:
```console
-C ethosu.num_macs=128
```
### Fast mode

The Ethos-U model used in FVPs can run at a faster speed with less simulation detail.

Use this configuration parameter to enable fast mode:

```console
-C ethosu.extra_args="--fast"
```

### Hardware memory maps

A memory map is available for each configuration of the Corstone kits. For example, the Corstone-300 with Cortex-M55 and Ethos-U55 [memory map](https://developer.arm.com/documentation/100966/1118/Arm--Corstone-SSE-300-FVP/Memory-map-overview-for-Corstone-SSE-300/) describes the address ranges for memory and peripherals.

Refer to the reference guides for details about the hardware models:
- [Corstone-300 Reference Guide](https://developer.arm.com/documentation/100966/latest/Arm--Corstone-SSE-300-FVP/)
- [Corstone-310 Reference Guide](https://developer.arm.com/documentation/100966/latest/Arm--Corstone-SSE-310-FVP/)
- [Corstone-315 Reference Guide](https://developer.arm.com/documentation/109395/latest)
- [Corstone-320 Reference Guide](https://developer.arm.com/documentation/109760/latest)

The memory map of FVPs is NOT configurable.

## Arm IP Explorer

Arm IP Explorer is used by SoC architects to select IP for new designs. It includes simulation features which provide cycle accurate simulation of Arm processors for the purpose of processor selection. It covers Cortex-M and Ethos-U and can help you determine the best processor configurations for a project.

Refer to the [Arm IP Explorer install guide](/install-guides/ipexplorer/) for links to more information.

## Summary

You should have a general understanding of the hardware options for Corstone-300 and Corstone-310 for application development. You can use an MPS3 board or an FVP on your local machine or using one of the cloud solutions.

The next section covers similar information for software, tools, and example applications.
