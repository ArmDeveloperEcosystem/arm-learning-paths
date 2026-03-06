---
title: Set up the Alif Ensemble E8 DevKit
weight: 2

layout: "learningpathall"
---

## Overview

The Alif Ensemble E8 DevKit features a dual-core Arm Cortex-M55 processor and three neural processing units (NPUs): two Ethos-U55 and one Ethos-U85. In this Learning Path, you use the Cortex-M55 High-Performance (HP) core running at 400 MHz to orchestrate inference on the Ethos-U85 NPU.

Before writing any ML code, you need to verify that your toolchain, debug probe, and flashing workflow all function correctly. This section walks you through hardware setup, software installation, and a sanity check build.

## Connect the board

1. Unplug all USB cables from the board before changing any jumpers.
2. Verify the jumpers are in their factory default positions, as shown in the Alif Ensemble E8 DevKit (DK-E8) User Guide, available on [alifsemi.com](https://alifsemi.com/support/kits/ensemble-e8devkit/).
3. Connect a USB-C cable from your computer to the **PRG USB** port on the bottom edge of the board.
4. Confirm that a green LED illuminates near the E1 device and the UART switch (SW4).

Leave **SW4** in its default position. This routes the on-board USB UART to **SEUART**, which the Alif Security Toolkit uses for programming.

{{% notice Note %}}
Don't have a terminal application (PuTTY, minicom, screen) attached to SEUART while using the Security Toolkit. There is only one SEUART on the device, and two applications can't share the port.
{{% /notice %}}

## Install the Alif Security Toolkit

The Security Toolkit (SETOOLS) programs firmware images onto the board.

1. Download SETOOLS v1.107.000 from the [Alif Ensemble E8 DevKit support page](https://alifsemi.com/support/kits/ensemble-e8devkit/).
2. Extract it to a stable location, for example `~/alif/app-release-exec-macos/`.
3. Open a terminal in the SETOOLS directory and run:

```bash
./updateSystemPackage -d
```

On macOS, the system blocks this unsigned binary the first time. Open **System Settings > Privacy & Security**, scroll to the **Security** section, and select **Allow Anyway**. Then re-run the command.

When prompted for a serial port, enter the DevKit's USB modem port. It usually appears as `/dev/cu.usbmodemXXXXXXX`. If SETOOLS detects the Ensemble E8 and asks to set it as default, answer `y`.

## Install SEGGER J-Link

SEGGER J-Link provides the debug connection for RTT (Real-Time Transfer) output, which you use later to view inference results.

On macOS, install it with Homebrew:

```bash
brew install --cask segger-jlink
```

Alternatively, download it from the [SEGGER website](https://www.segger.com/downloads/jlink/). Run J-Link Commander once after installation to update the on-board probe firmware if needed.

## Set up VS Code and the Alif template

1. Clone the Alif VS Code template repository:

```bash
cd ~/repo/alif
git clone https://github.com/alifsemi/alif_vscode-template.git
cd alif_vscode-template
git checkout 8b1aa0b09eacf68a28850af00c11f0b5af03c100
git submodule update --init
```

{{% notice Note %}}
The `git checkout` command pins the template to a known-working commit. This avoids breakage if the upstream template is updated.
{{% /notice %}}

2. Open the `alif_vscode-template/` folder in VS Code.
3. Install the recommended extensions when prompted:
   - Arm CMSIS Solution
   - Arm Tools Environment Manager
   - Cortex-Debug
   - Microsoft C/C++ Extension Pack
4. When prompted, select **Always Allow** or **Allow for Selected Workspace**.
5. Restart VS Code if prompted.

## Install CMSIS packs

Press **F1** in VS Code, type `Tasks: Run Task`, and select **First time pack installation**. Press **A** to accept all licenses when prompted.

## Configure VS Code settings

Press **F1**, select **Preferences: Open User Settings (JSON)**, and add the following entries (update the paths for your system):

```json
{
  "alif.setools.root": "/path/to/your/app-release-exec-macos",
  "cortex-debug.JLinkGDBServerPath": "/Applications/SEGGER/JLink/JLinkGDBServerCLExe"
}
```

## Sanity check: build and flash Blinky

Before moving on to ML code, verify your entire toolchain works end to end with the built-in Blinky example.

1. In VS Code, select the **CMSIS** icon in the left sidebar.
2. Select the gear icon, then set **Active Target** to **E8-HP** and **Active Project** to **blinky**.
3. Select the **Build** (hammer) icon.
4. Press **F1**, select **Tasks: Run Task**, then select **Program with Security Toolkit (select COM port)**.
5. Choose the DevKit's port when prompted.

If the board's red LED blinks, your toolchain, SETOOLS, and board connection are all working correctly. You're ready to move on to model compilation.
