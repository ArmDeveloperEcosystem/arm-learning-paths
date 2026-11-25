---
title: "Prepare to connect PocketBeagle 2 to AWS IoT Greengrass"
description: Understand how a PocketBeagle 2 Yocto image, Greengrass nucleus lite identity, and AWS IoT thing group enable cloud application deployment.
weight: 2
layout: "learningpathall"
---

## Build an Arm edge device that receives cloud deployments

A PocketBeagle 2 can receive applications pushed from the cloud. However, it requires a Linux image that includes the AWS IoT Greengrass runtime and an identity that AWS recognizes. You can set up both, then send a Hello World application from AWS to the board and watch it run.

The host computer is an Ubuntu 24.04 Linux computer that builds the image and connects to the board over USB. You'll run AWS commands on the host.

The project has four parts:

- Build a Yocto Linux image that includes Greengrass nucleus lite, and write it to a microSD card.
- Boot the board and connect it to the host computer over USB, with outbound Internet access.
- Create the AWS IoT identity for the board and connect it to AWS as a Greengrass core device.
- Publish a Hello World component, deploy it to a thing group, and confirm in the board journal that it runs.

At the end, the board takes deployments from AWS. You'll have a repeatable process for sending the board your own applications.

PocketBeagle 2 uses a Texas Instruments AM6254 processor with Arm Cortex-A53 application cores. The image targets 64-bit Linux on those cores. It doesn't target the original PocketBeagle, and the application doesn't run on the microcontrollers of the board.

Greengrass nucleus lite is a device runtime for constrained Linux devices. It implements a subset of the Java-based Greengrass nucleus. The Hello World component is a generic component with a shell lifecycle and no IPC dependencies. This suits the nucleus lite runtime.

## Understand the workflow

The tasks progress from preparing the image to validating a cloud deployment:

| Stage | Where you work | Result |
| --- | --- | --- |
| Build | Host computer | Bootable microSD image with Greengrass nucleus lite |
| Boot and connect | PocketBeagle 2 and host computer | SSH and outbound Internet access |
| Provision | Host computer, AWS, and board | Unique certificate, IoT thing, and connected core device |
| Publish | Host computer and AWS | Versioned Hello World component |
| Deploy | Host computer, AWS, and board | Thing group deployment and observed application output |

A thing is the AWS IoT identity of one board. A thing group is a deployment target containing one or more things. Group deployment refers to a Greengrass V2 deployment to an AWS IoT thing group. Each board retains its own identity and certificate.

## Download the build scripts

The build uses scripts and Yocto configuration files. Download the files on the host computer:

```bash
wget https://learn.arm.com/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/pocketbeagle2-scarthgap-build.zip
```

The zip file contains the build script, the Yocto layer for the board, a provisioning helper, and a README. You'll unzip the file and start the build later.

## What you've accomplished and what's next

You've learned about the deployment workflow and downloaded build scripts on the host computer.

Next, you'll use the scripts to build the Yocto image that provides the Greengrass runtime and board connectivity.
