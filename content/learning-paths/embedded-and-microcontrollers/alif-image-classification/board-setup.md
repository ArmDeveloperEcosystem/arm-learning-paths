---
title: Set up the Alif Ensemble E8 DevKit
weight: 2

layout: "learningpathall"
---

## Understand the Alif Ensemble E8 hardware

The Alif Ensemble E8 DevKit features a dual-core Arm Cortex-M55 processor and three neural processing units (NPUs): two Ethos-U55 and one Ethos-U85. In this Learning Path, you use the Cortex-M55 High-Performance (HP) core running at 400 MHz to orchestrate inference on the Ethos-U85 NPU.

Before writing any ML code, you need to verify that your toolchain, debug probe, and flashing workflow all function correctly. This section covers DevKit hardware setup, software installation, and a short validation build.

The instructions assume macOS on Apple Silicon. If you use Arm Linux, links are provided for the equivalent Linux packages.

## Connect the DevKit

1. Unplug all USB cables from the DevKit before changing any jumpers.

2. Verify that the jumpers are in their factory default positions, as shown in the Alif Ensemble E8 DevKit (DK-E8) User Guide on [alifsemi.com](https://alifsemi.com/support/kits/ensemble-e8devkit/).

3. Connect a USB-C cable from your computer to the **PRG USB** port on the bottom edge of the DevKit.

4. Confirm that a green LED illuminates near the E1 device and the UART switch (SW4).

Leave **SW4** in its default position. This routes the on-board USB UART to **SEUART**, which the Alif Security Toolkit (SETOOLS) uses for programming.

{{% notice Note %}}
Close any terminal application that's connected to SEUART, such as PuTTY, minicom, or screen, before you use the Security Toolkit (SETOOLS). The DevKit exposes only one SEUART interface, so SETOOLS can't access the port if another application is already using it.
{{% /notice %}}

5. Create a project directory:

```bash
mkdir ~/alif
```

## Install the Alif Security Toolkit

The Security Toolkit (SETOOLS) programs firmware images onto the DevKit.

1. Download the macOS version of SETOOLS from the [Alif Ensemble E8 DevKit support page](https://alifsemi.com/support/kits/ensemble-e8devkit/).

2. Extract it into `~/alif`. This creates the toolkit directory under a stable location, for example `~/alif/app-release-exec-macos/`.

```bash
cd ~/Downloads
tar xvf APFW0003-app-release-exec-macos-SW_FW_1.107.00_DEV-4.tar -C ~/alif
```

3. Open a terminal in the SETOOLS directory and run:

```bash
cd ~/alif/app-release-exec-macos
./updateSystemPackage -d
```

On macOS, the system blocks this unsigned binary the first time. After that happens, open **System Settings > Privacy & Security**, scroll to the **Security** section, and select **Allow Anyway**. Run the command again.

When prompted for a serial port, enter the DevKit's USB modem port. On macOS, it usually appears as `/dev/cu.usbmodemXXXXXXX`. If SETOOLS detects the Ensemble E8 and asks to set it as the default, answer `y`.

## Install SEGGER J-Link

SEGGER J-Link provides the debug connection for RTT (Real-Time Transfer) output, which you use later to view inference results.

Install it with Homebrew:

```bash
brew install --cask segger-jlink
```

Alternatively, download it from the [SEGGER website](https://www.segger.com/downloads/jlink/). Run J-Link Commander once after installation to update the on-board probe firmware if needed.

## Set up VS Code and the Alif template

### Clone the Alif VS Code template repository

```bash
cd ~/alif
git clone https://github.com/alifsemi/alif_vscode-template.git
cd alif_vscode-template
git checkout 8b1aa0b09eacf68a28850af00c11f0b5af03c100
git submodule update --init
```

{{% notice Note %}}
The `git checkout` command pins the template to a known-working commit. This avoids breakage if the upstream template is updated.
{{% /notice %}}

### Open the project in VS Code

Open the project in VS Code from the `alif_vscode-template/` directory:

```bash
code . &
```

### Install the recommended extensions when prompted

VS Code might prompt you to install the recommended extensions for this workspace. If it does, install the following:

   - Arm CMSIS Solution
   - Arm Tools Environment Manager
   - Cortex-Debug
   - Microsoft C/C++ Extension Pack

When prompted, select **Always Allow** or **Allow for Selected Workspace**.

The recommended VS Code extensions are listed in `.vscode/extensions.json`.

If you don't get an automatic trigger to enable them, you can open the Extensions view and look for a "Workspace Recommendations" section to install or enable them manually.

Restart VS Code if prompted.

## Install CMSIS packs

Open the Command Palette by pressing **Command+Shift+P** (or **Fn+F1**) in VS Code, type `Tasks: Run Task`, and select **First time pack installation**. Press **A** to accept all licenses when prompted.

If you don't see the task in the list, open the Command Palette (**Command+Shift+P** or **Fn+F1**) and run the **Reload Window** command.

## Configure VS Code settings

Press Fn+F1, select **Preferences: Open User Settings (JSON)**, and add the following entries.

Update both paths for your system, including using your username:

```json
{
  "alif.setools.root": "/Users/username/alif/app-release-exec-macos",
  "cortex-debug.JLinkGDBServerPath": "/Applications/SEGGER/JLink/JLinkGDBServerCLExe"
}
```

If you have existing settings, add only the two lines of text inside the existing braces.

## Verify your toolchain: build and flash Blinky

Before moving on to ML code, verify your entire toolchain works end to end with the built-in Blinky example.

1. In VS Code, select the **CMSIS** icon in the left sidebar.
2. Select the gear icon, then set **Active Target** to **E8-HP** and **Active Project** to **blinky**.
3. Select the **Build** (hammer) icon.
4. Press **Fn+F1**, select **Tasks: Run Task**, then select **Program with Security Toolkit (select COM port)**.
5. Choose the DevKit's port when prompted.

If the DevKit's red LED blinks, your toolchain, SETOOLS, and DevKit connection are all working correctly. You are ready to move on to model compilation.

## What you've learned and what's next

You've set up the Alif Ensemble E8 DevKit hardware, installed the Security Toolkit and J-Link tools, and verified the toolchain by building the Blinky example project.

Next, you'll compile the MobileNetV2 model on an Arm cloud instance using ExecuTorch and the Vela compiler.
