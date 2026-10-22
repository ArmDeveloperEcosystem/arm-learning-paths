---
title: "Connect PocketBeagle 2 to Greengrass Lite"
description: Understand how a PocketBeagle 2 Yocto image, Greengrass Lite identity, and AWS IoT thing group enable cloud application deployment.
weight: 2
layout: "learningpathall"
---

## Build an Arm edge device that receives cloud deployments

Build a Yocto Linux image for PocketBeagle 2, register its AWS IoT identity, and deploy a Hello World application from AWS IoT Greengrass. The final test prints a message repeatedly on the device, proving that a cloud deployment reached the Arm board and started your application.

PocketBeagle 2 uses a Texas Instruments AM6254 processor with Arm Cortex-A53 application cores. This tutorial targets 64-bit Linux on those cores. It does not target the original PocketBeagle or run the application on the board's microcontrollers.

Greengrass nucleus lite is a native runtime for constrained Linux devices. It implements a subset of the Java-based Greengrass nucleus. This tutorial uses a generic component with a shell lifecycle and no IPC dependencies, suitable for the Lite runtime.

## Follow the workflow

The tasks progress from preparing the image to validating a cloud deployment:

| Stage | Where you work | Result |
| --- | --- | --- |
| Build | x86_64 Linux host | Bootable microSD image with Nucleus Lite |
| Boot and connect | PocketBeagle 2 and attached computer | SSH and outbound Internet access |
| Provision | AWS workstation and board | Unique certificate, IoT thing, and connected core device |
| Publish | AWS workstation | Versioned Hello World component |
| Deploy | AWS and board | Thing group deployment and observed application output |

A *thing* is the AWS IoT identity of one board. A *thing group* is a deployment target containing one or more things. Here, “group deployment” means a Greengrass V2 deployment to an AWS IoT thing group. Each board retains its own identity and certificate.

## Use the supplied build bundle

Download the [PocketBeagle 2 Scarthgap build bundle](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/pocketbeagle2-scarthgap-build.zip). It includes `build-pocketbeagle2.sh`, the `meta-pocketbeagle2-dev` layer, a provisioning helper, and a README. Keep these together: the script locates its layer relative to itself.

The bundle pins Yocto Scarthgap layers and Greengrass nucleus lite 2.6.0. The generated `sources.lock` records the upstream revisions; see the bundled `AUDIT.txt` for verification limits.

Allow several additional hours for a first uncached build beyond the hands-on time shown for this Learning Path. AWS services can incur charges; use a dedicated development thing group.

This image also prepares the board for [Part 2: run Zephyr alongside Yocto Linux](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-zephyr-part2/). To follow both parts, use PocketBeagle 2 revision A1 and have a 3.3 V USB-to-UART adapter and jumper wires.

## What you have learned

You know how the Yocto image, unique device identity, component version, and thing group fit together. Next, build the image that provides the runtime and board connectivity.

