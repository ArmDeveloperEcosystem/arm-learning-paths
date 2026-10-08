---
title: Prepare the DevKit for debugging
description: Use Alif SETOOLS to install the table of contents and Cortex-M55 high-performance core debug stub needed by the example.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the one-time provisioning step

The Alif Secure Enclave boots processor images from a table of contents in magnetoresistive random-access memory (MRAM). Before the first debug session, install the configuration that points the high-performance Cortex-M55 core to the project's debug stub.

You normally perform this step once. Repeat it if another project replaces the table of contents.

## Install the debug stub

Confirm that the board is connected through **PRG USB** and that **SW4** is set to **SEUART**. Close any serial monitor that has the DevKit port open.

In VS Code, select:

**Terminal > Run Task > Alif: Install M55_HP debug stubs (DevKit-E8, single core configuration)**

Choose automatic COM port discovery with `-d` the first time. SETOOLS remembers the selected port for later runs.

The task performs these operations:

1. Selects the DevKit-E8 part `AE822FA0E5597LS0` with revision `A0`.
2. Copies the supplied device configuration and debug stub into the SETOOLS workspace.
3. Generates the application table of contents.
4. Writes the table and debug stub to MRAM.

If `app-write-mram` reports a different board revision and asks whether to continue, answer `y`. The part number determines whether the table can boot.

## Switch the UART to the application

After the task completes, set **SW4** to **UART4**. This routes the DevKit's application console to the USB-to-UART bridge.

{{% notice Important %}}
Keep the debug interface set to SWD. A JTAG configuration can leave the generated load task waiting for a J-Link chain response while the device remains in SWD mode.
{{% /notice %}}

## What you've accomplished and what's next

You've installed the boot table and debug stub for the Cortex-M55 high-performance core, then routed the console to UART4. Next, you'll build the application, generate a face, and validate that both ExecuTorch methods ran on the Ethos-U85 NPU.
