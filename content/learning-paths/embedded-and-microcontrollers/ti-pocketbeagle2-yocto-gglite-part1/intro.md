---
title: "Connect PocketBeagle 2 to Greengrass nucleus lite"
description: Understand how a PocketBeagle 2 Yocto image, Greengrass nucleus lite identity, and AWS IoT thing group enable cloud application deployment.
weight: 2
layout: "learningpathall"
---

## Build an Arm edge device that receives cloud deployments

A PocketBeagle 2 can receive applications pushed from the cloud, but it requires a Linux image that includes the AWS IoT Greengrass runtime and an identity that AWS recognizes. You can set up both, then send a Hello World application from AWS to the board and watch it run.

The host computer is an Ubuntu 24.04 Linux computer that builds the image, connects to the board over USB, and runs the AWS commands.

The project has four parts:

- Build a Yocto Linux image that includes Greengrass nucleus lite, and write it to a microSD card
- Boot the board and connect it to the host computer over USB, with outbound Internet access
- Create the board's AWS IoT identity and connect it to AWS as a Greengrass core device
- Publish a Hello World component, deploy it to a thing group, and confirm in the board's journal that it runs

At the end, the board takes deployments from AWS, and you have a repeatable process for sending it your own applications.

PocketBeagle 2 uses a Texas Instruments AM6254 processor with Arm Cortex-A53 application cores. The image targets 64-bit Linux on those cores. It doesn't target the original PocketBeagle, and the application doesn't run on the board's microcontrollers.

Greengrass nucleus lite is a native runtime for constrained Linux devices. It implements a subset of the Java-based Greengrass nucleus. The Hello World component is a generic component with a shell lifecycle and no IPC dependencies, which suits the nucleus lite runtime.

## Follow the workflow

The tasks progress from preparing the image to validating a cloud deployment:

| Stage | Where you work | Result |
| --- | --- | --- |
| Build | Host computer | Bootable microSD image with Greengrass nucleus lite |
| Boot and connect | PocketBeagle 2 and host computer | SSH and outbound Internet access |
| Provision | Host computer, AWS, and board | Unique certificate, IoT thing, and connected core device |
| Publish | Host computer and AWS | Versioned Hello World component |
| Deploy | Host computer, AWS, and board | Thing group deployment and observed application output |

A *thing* is the AWS IoT identity of one board. A *thing group* is a deployment target containing one or more things. Here, “group deployment” means a Greengrass V2 deployment to an AWS IoT thing group. Each board retains its own identity and certificate.

## Download the build scripts

The build uses scripts and Yocto configuration files. Download them on the host computer:

```bash
wget https://learn.arm.com/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/pocketbeagle2-scarthgap-build.zip
```

The zip file contains the build script, the Yocto layer for the board, a provisioning helper, and a README. The next page unzips it and starts the build.

## What you have accomplished

You have an overview of the project and the build scripts on the host computer. Next, use the scripts to build the Yocto image that provides the Greengrass runtime and board connectivity.