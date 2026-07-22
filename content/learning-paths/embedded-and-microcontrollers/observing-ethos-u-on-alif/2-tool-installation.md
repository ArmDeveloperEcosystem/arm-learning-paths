---
title: Install development tools
weight: 3
layout: learningpathall
---

## Overview

This section covers installing all required tools for ExecuTorch development on the Alif Ensemble E8 DevKit.


Start by creating a project directory:
{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash" >}}
mkdir -p ~/mnist_alif
  {{< /tab >}}

  {{< tab header="Windows (PowerShell)" language="powershell" >}}
New-Item -ItemType Directory -Force -Path ~\mnist_alif
  {{< /tab >}}
{{< /tabpane >}}

## Install SETOOLS

SETOOLS (Secure Enclave Tools) is Alif's toolset for flashing firmware to MRAM via the Secure Enclave.

- Download the SETOOLS package from the [Alif Ensemble E8 DevKit support page](https://alifsemi.com/support/kits/ensemble-e8devkit/) and extract it to `~/mnist_alif`.
Make sure to edit the command below with the name of your `.tar` or `.zip` file.
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

- Verify the installation. The extracted folder name can vary by SETOOLS release. The commands below assume the package extracts to `app-release-exec-*`.
Each command should print a `usage:` message. If either command fails, check that you are in the extracted SETOOLS directory for your operating system.
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
On macOS, the system may block the unsigned binary the first time you run it. If this happens, open **System Settings** or **System Preferences**, go to **Privacy & Security**, and select **Allow Anyway**. Then run the command again. (You may need to reapprove for both ./app-* commands)
{{% /notice %}}


## Install J-Link

SEGGER J-Link provides the debug connection for RTT (Real-Time Transfer) output, which you use later to view inference results.
Version 7.94 or later is required for Alif Ensemble E8 support.

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


## Set up the Alif VS Code template
- Clone the Alif VS Code template repository and checkout to a known-working commit. This is to avoid breakage if the template has been updated.
```bash
cd ~/mnist_alif
git clone https://github.com/alifsemi/alif_vscode-template.git
cd alif_vscode-template
git checkout 8b1aa0b09eacf68a28850af00c11f0b5af03c100
git submodule update --init
```

- Open the project in VS Code:
```bash
code .
```
VS Code might prompt you to install the recommended extensions for this workspace. If it does, install the following:

- Arm CMSIS Solution
- Arm Tools Environment Manager
- Cortex-Debug
- Microsoft C/C++ Extension Pack

When prompted, select **Always Allow** or **Allow for Selected Workspace**.

The recommended VS Code extensions are listed in .vscode/extensions.json. If you don’t get an automatic trigger to enable them, you can open the Extensions view and look for a “Workspace Recommendations” section to install or enable them manually.

Restart VS Code if prompted.

## Install CMSIS packs
CMSIS (Common Microcontroller Software Interface Standard) is a set of APIs, software components, and metadata that simplifies development on Arm Cortex-M processors. 
Installing the CMSIS pack will provide the device definitions, startup files, drivers, and middleware components we need for our Alif E8 target. To install, follow these steps:

In VS Code, open the Command Palette using **Ctrl+Shift+P** on Windows/Linux or **Command+Shift+P** on macOS.

Click **Tasks: Run Task**, then select **First time pack installation**. When prompted, press **A** to accept all licenses.

If the task does not appear, run **Developer: Reload Window** from the Command Palette and try again.

## Configure VS Code settings

VS Code need to know where the external Alif SETOOLS and SEGGER J-Link tools are installed.

Open the Command Palette and run **Preferences: Open User Settings (JSON)**.

Add the following settings, updating the paths for your operating system:

```json
{
  "alif.setools.root": "path/to/your/setools-folder",
  "cortex-debug.JLinkGDBServerPath": "/Applications/SEGGER/JLink/JLinkGDBServerCLExe"
}
```
If your settings file already contains entries, add only these two settings inside the existing braces.

### Verify your toolchain with Blinky
Before moving on to the ML application, build and flash the built-in Blinky example.
- In VS Code, select the **CMSIS** icon in the left sidebar.
- Select the **gear icon**.
- Set **Active Target** to **E8-HE**.
- Set **Active Project** to **blinky**.
- Select the **Build** (hammer) icon.
- Open the **Command Palette** and run **Tasks: Run Task**.
- Select **Program with Security Toolkit (select COM port)**.
- Choose the DevKit port when prompted.

If the RGB LED blinks, your VS Code setup, CMSIS packs, SETOOLS configuration, and board connection are working.

## Summary

You have installed:
- ✅ SETOOLS for flashing firmware to MRAM
- ✅ J-Link (7.94+) for programming and debugging
- ✅ Required VS Code extensions & CMSIS packs

