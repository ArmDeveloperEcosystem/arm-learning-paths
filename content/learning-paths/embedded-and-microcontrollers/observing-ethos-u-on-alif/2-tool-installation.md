---
title: Set up the Alif Ensemble E8 DevKit
description: Connect an Alif Ensemble E8 DevKit and install SETOOLS, J-Link, VS Code extensions, and CMSIS packs for ExecuTorch development.
weight: 3
layout: learningpathall
---

## Connect to the Alif Ensemble E8 DevKit

To connect to the Alif Ensemble E8 DevKit:

1. Unplug all USB cables from the DevKit before changing any jumpers.

2. Verify that the jumpers are in their factory default positions, as shown in the Alif Ensemble E8 DevKit (DK-E8) User Guide on [alifsemi.com](https://alifsemi.com/support/kits/ensemble-e8devkit/).

3. Connect a USB-C cable from your computer to the PRG USB port on the bottom edge of the DevKit.

![Close-up of the Alif Ensemble E8 DevKit showing a USB-C cable connected to the PRG USB port; the separate MCU USB port is visible below#center](prg-usb-port.png "USB-C cable connected to the PRG USB port")

4. Confirm that a green LED illuminates near the E1 device and the UART switch (SW4).

Leave SW4 in its default position. This routes the on-board USB UART to SEUART, which the Alif Security Toolkit (SETOOLS) uses for programming.

## Verify USB connection to the DevKit

Check that your computer recognizes the DevKit:

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
ls /dev/cu.*
  {{< /tab >}}

  {{< tab header="Linux" language="bash">}}
ls /dev/ttyACM* /dev/ttyUSB* 2>/dev/null
  {{< /tab >}}

  {{< tab header="Windows" language="powershell">}}
Get-CimInstance Win32_SerialPort | Select-Object DeviceID,Name,Description
  {{< /tab >}}
{{< /tabpane >}}

{{% notice Important %}}
Close any terminal application that’s connected to SEUART, such as PuTTY, minicom, or screen, before you use the Security Toolkit (SETOOLS). The DevKit exposes only one SEUART interface, so SETOOLS can’t access the port if another application is already using it.
{{% /notice %}}

You should see a SEGGER J-Link device. If you're unsure which entry belongs to the DevKit, run the command before and after connecting the board and compare the output. If no device appears, check that the USB cable is connected to the **PRG USB** port and that the cable supports data, not only charging.

## Create a project directory for the DevKit

Before installing all required tools for ExecuTorch development, create a project directory:

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
mkdir -p ~/mnist_alif
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
New-Item -ItemType Directory -Force -Path ~\mnist_alif
  {{< /tab >}}
{{< /tabpane >}}

## Install SETOOLS

Secure Enclave Tools (SETOOLS) is Alif's toolset for flashing firmware to MRAM through the Secure Enclave.

1. Download the SETOOLS package from the [Alif Ensemble E8 DevKit support page](https://alifsemi.com/support/kits/ensemble-e8devkit/) and extract it to `~/mnist_alif`.
  Make sure to edit the following command with the name of your `.tar` or `.zip` file.
  {{< tabpane code=true >}}
    {{< tab header="macOS / Linux" language="bash" >}}
  cd ~/Downloads
  tar xvf <replace_with_your_alif_security_toolkit_download.tar> -C ~/mnist_alif
    {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
  cd ~/Downloads
  Expand-Archive <.\replace_with_your_alif_security_toolkit_download.zip> -DestinationPath ~\mnist_alif
    {{< /tab >}}
  {{< /tabpane >}}

2. Verify the installation. The extracted folder name can vary by SETOOLS release. The following commands assume the package extracts to `app-release-exec-*`.
  Each command should print a `usage:` message. If either command fails, check that you're in the extracted SETOOLS directory for your operating system.
  {{< tabpane code=true >}}
    {{< tab header="macOS" language="bash" >}}
    cd ~/mnist_alif/app-release-exec-macos
    ./app-write-mram -h
    ./app-gen-toc -h
    {{< /tab >}}
  {{< tab header="Linux" language="bash" >}}
    cd ~/mnist_alif/app-release-exec-linux
    ./app-write-mram -h
    ./app-gen-toc -h
  {{< /tab >}}
  {{< tab header="Windows" language="powershell" >}}
    cd ~\mnist_alif\app-release-exec-windows
    .\app-write-mram.exe -h
    .\app-gen-toc.exe -h
  {{< /tab >}}
  {{< /tabpane >}}

{{% notice Important %}}
On macOS, the system might block the unsigned binary the first time you run it. If this happens, do the following:

  1. Open **System Settings** or **System Preferences**.
  2. Navigate to **Privacy & Security**.
  3. Select **Allow Anyway**. 

Then, run the command again. You might need to reapprove for both `./app-*` commands.
{{% /notice %}}


## Install J-Link

SEGGER J-Link provides the debug connection for Real-Time Transfer (RTT) output, which you'll use later to view inference results.

Install J-Link version 7.94 or later for Alif Ensemble E8 support:

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
brew install --cask segger-jlink
JLinkExe --version
  {{< /tab >}}
  {{< tab header="Linux" language="bash">}}
wget https://www.segger.com/downloads/jlink/JLink_Linux_x86_64.deb
sudo dpkg -i JLink_Linux_x86_64.deb
JLinkExe --version
  {{< /tab >}}
  {{< tab header="Windows" language="text">}}
1. Download installer from https://www.segger.com/downloads/jlink/
2. Run the installer and follow prompts
3. Verify in Command Prompt: JLink.exe --version
  {{< /tab >}}
{{< /tabpane >}}


## Set up the Alif Visual Studio Code template

Next, you'll need to set up the Alif Visual Studio Code (VS Code) template.

To start, clone the Alif VS Code template repository and check out a known-working commit: 

```bash
cd ~/mnist_alif
git clone https://github.com/alifsemi/alif_vscode-template.git
cd alif_vscode-template
git checkout 8b1aa0b09eacf68a28850af00c11f0b5af03c100
git submodule update --init
```

By checking out a known commit, you can avoid breakage if the template gets updated.

After cloning, open the project in VS Code:

```bash
code .
```
VS Code might prompt you to install the recommended extensions for this workspace. If it does, install the following:

  - Arm CMSIS Solution
  - Arm Tools Environment Manager
  - Cortex-Debug
  - Microsoft C/C++ Extension Pack

When prompted, select **Always Allow** or **Allow for Selected Workspace**.

{{% notice Note %}}
The recommended VS Code extensions are listed in `.vscode/extensions.json`. If you don’t get an automatic trigger to enable them, you can open the **Extensions** view and look for a **Workspace Recommendations** section to install or enable them manually.
{{% /notice %}}

Restart VS Code if prompted.

## Install CMSIS packs

Common Microcontroller Software Interface Standard (CMSIS) is a set of APIs, software components, and metadata that simplifies development on Arm Cortex-M processors. 
Installing the CMSIS pack will provide the device definitions, startup files, drivers, and middleware components you'll need for the Alif E8 target. 

To install CMSIS packs:

1. In VS Code, open the Command Palette using **Ctrl+Shift+P** on Windows and Linux, or **Command+Shift+P** on macOS.
2. Select **Tasks: Run Task**.
3. Select **First time pack installation**. 
4. When prompted, press the **A** key to accept all licenses.

{{% notice Note %}}
If the installation task doesn't appear, run **Developer: Reload Window** from the Command Palette and try again.
{{% /notice %}}

## Configure VS Code settings

VS Code needs to know where the external Alif SETOOLS and SEGGER J-Link tools are installed. 

To configure the settings on VS Code:

1. Open the Command Palette and run **Preferences: Open User Settings (JSON)**.
2. Add the following settings, updating the paths for your operating system:

  ```json
  {
    "alif.setools.root": "path/to/your/setools-folder",
    "cortex-debug.JLinkGDBServerPath": "/Applications/SEGGER/JLink/JLinkGDBServerCLExe"
  }
  ```
  If your settings file already contains entries, add only these two settings inside the existing braces.

## Verify your toolchain with Blinky

Build and flash the built-in Blinky example to verify your toolchain:

1. In VS Code, select the **CMSIS** icon in the left sidebar.
2. Select the **gear icon**.
3. Set **Active Target** to **E8-HE**.
4. Set **Active Project** to **blinky**.
5. Select the **Build** (hammer) icon.
6. Open the **Command Palette** and run **Tasks: Run Task**.
7. Select **Program with Security Toolkit (select COM port)**.
8. Choose the DevKit port when prompted.

If the RGB LED blinks, your VS Code setup, CMSIS packs, SETOOLS configuration, and board connection are working.

## What you've accomplished and what's next

You've now connected the Alif Ensemble E8 DevKit to your computer and installed required tools for the DevKit. The tools include SETOOLS for flashing firmware to MRAM, J-Link for programming and debugging, required VS Code extensions, and CMSIS packs.

Next, if you're using the provided `.pte` model, skip to [Prepare firmware artifacts](/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts/). If you want to train and export the model yourself, see [(Optional) Set up a Docker development environment](/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/).
