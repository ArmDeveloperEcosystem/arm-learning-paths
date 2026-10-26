---
title: Development platforms
description: Compare physical boards and virtual platforms for developing Cortex-M and Ethos-U machine learning applications.

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

Virtual implementations of the Corstone reference systems are also available for local software development.

### Ecosystem FVPs

Ecosystem FVPs are free-of-charge and target a variety of applications. They run on Linux and Windows.

The Corstone reference systems are available on the [Arm Ecosystem FVP page](https://developer.arm.com/downloads/-/arm-ecosystem-fvps/). General ecosystem FVP setup instructions are provided in the [install guide](/install-guides/fm_fvp/eco_fvp/).

The Ecosystem FVP can be used in conjunction with [Keil MDK](https://developer.arm.com/Tools%20and%20Software/Keil%20MDK) or [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio).

Keil MDK Professional Edition also provides these virtual platforms.

## FVP configuration options

These virtual platforms have some options to help you evaluate different configurations.

### Number of MACs

Ethos-U55 and Ethos-U65 offer a configurable number of MACs (multiply-accumulate units). During IP evaluation and performance analysis you need to understand the numbers of MACs available in the hardware and create your software to use the same configuration.

| Ethos-U NPU | Number of MACs supported    |
| ----------- | -----------                 |
| Ethos-U55   | 32, 64, 128, 256            |
| Ethos-U65   | 256, 512                    |

FVPs can be configured with:
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

You should have a general understanding of the hardware options for Corstone-300 and Corstone-310 application development. You can use an MPS3 board or an FVP on your local machine.

The next section covers similar information for software, tools, and example applications.
