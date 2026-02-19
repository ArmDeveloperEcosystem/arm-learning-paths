---
title: Install development tools
weight: 2
layout: learningpathall
---

## Overview

This section covers installing all required tools for ExecuTorch development on the Alif Ensemble E8 DevKit.

You need:
- Docker for the build environment
- CMSIS-Toolbox for Alif E8 projects
- J-Link for programming and debugging
- SETOOLS for Alif-specific flashing
- ARM GCC Toolchain (installed within Docker)

## Install Docker

Docker provides an isolated environment with all build dependencies.

### Install Docker Desktop

Select your operating system:

{{< tabpane>}}
{{< tab header="macOS" >}}

```bash
# Download and install Docker Desktop from:
# https://www.docker.com/products/docker-desktop

# Or install via Homebrew
brew install --cask docker

# Start Docker Desktop from Applications
# Verify installation
docker --version
```

Expected output:
```output
Docker version 24.0.7, build afdd53b
```

{{</tab >}}
{{<tab header="Linux" >}}

```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER

# Log out and back in, then verify
docker --version
```

Expected output:
```output
Docker version 24.0.7, build afdd53b
```

{{< /tab >}}
{{< tab header="Windows" >}}

1. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop)
2. Run the installer
3. Restart your computer when prompted
4. Open PowerShell and verify:

```powershell
docker --version
```

Expected output:
```output
Docker version 24.0.7, build afdd53b
```

{{</tab >}}
{{</tabpane >}}

### Verify Docker Installation

Test Docker is working:

```bash
docker run hello-world
```

The output is similar to:
```output
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

## Install CMSIS-Toolbox

CMSIS-Toolbox provides the `cbuild` command used to build CMSIS projects for the Alif E8.

### Prerequisites

Install CMake and Ninja before proceeding. These are required by CMSIS-Toolbox for project builds.

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
brew install cmake ninja

cmake --version
ninja --version
  {{< /tab >}}
  {{< tab header="Linux" language="bash">}}
sudo apt update
sudo apt install cmake ninja-build -y

cmake --version
ninja --version
  {{< /tab >}}
  {{< tab header="Windows" language="bash">}}
winget install Kitware.CMake
winget install Ninja-build.Ninja

cmake --version
ninja --version
  {{< /tab >}}
{{< /tabpane >}}

Confirm CMake is version 3.25.2 or later and Ninja is version 1.10.2 or later.

### Download and install CMSIS-Toolbox

Download the CMSIS-Toolbox archive for your host platform from the [Arm Tools Artifactory](https://artifacts.tools.arm.com/cmsis-toolbox/).

The examples below use version 2.6.0. Replace the version number if a newer release is available.

{{< tabpane code=true >}}
  {{< tab header="macOS (Apple Silicon)" language="bash">}}
curl -L -o cmsis-toolbox.tar.gz \
  https://artifacts.tools.arm.com/cmsis-toolbox/2.6.0/cmsis-toolbox-darwin-arm64.tar.gz

tar -xzf cmsis-toolbox.tar.gz
sudo mv cmsis-toolbox /opt/cmsis-toolbox
  {{< /tab >}}
  {{< tab header="macOS (Intel)" language="bash">}}
curl -L -o cmsis-toolbox.tar.gz \
  https://artifacts.tools.arm.com/cmsis-toolbox/2.6.0/cmsis-toolbox-darwin-amd64.tar.gz

tar -xzf cmsis-toolbox.tar.gz
sudo mv cmsis-toolbox /opt/cmsis-toolbox
  {{< /tab >}}
  {{< tab header="Linux (x86_64)" language="bash">}}
wget https://artifacts.tools.arm.com/cmsis-toolbox/2.6.0/cmsis-toolbox-linux-amd64.tar.gz

tar -xzf cmsis-toolbox-linux-amd64.tar.gz
sudo mv cmsis-toolbox /opt/cmsis-toolbox
  {{< /tab >}}
  {{< tab header="Linux (Arm64)" language="bash">}}
wget https://artifacts.tools.arm.com/cmsis-toolbox/2.6.0/cmsis-toolbox-linux-arm64.tar.gz

tar -xzf cmsis-toolbox-linux-arm64.tar.gz
sudo mv cmsis-toolbox /opt/cmsis-toolbox
  {{< /tab >}}
{{< /tabpane >}}

For Windows, download the appropriate `.zip` archive from the [Arm Tools Artifactory](https://artifacts.tools.arm.com/cmsis-toolbox/) and extract it to a directory such as `C:\cmsis-toolbox`.

### Set environment variables

Configure the required environment variables so that CMSIS-Toolbox can locate your toolchain and pack directory.

{{< tabpane code=true >}}
  {{< tab header="macOS / Linux" language="bash">}}
export CMSIS_PACK_ROOT=$HOME/.arm/Packs
export CMSIS_COMPILER_ROOT=/opt/cmsis-toolbox/etc
export PATH=/opt/cmsis-toolbox/bin:$PATH
  {{< /tab >}}
  {{< tab header="Windows (PowerShell)" language="powershell">}}
$env:CMSIS_PACK_ROOT = "$env:LOCALAPPDATA\Arm\Packs"
$env:CMSIS_COMPILER_ROOT = "C:\cmsis-toolbox\etc"
$env:PATH = "C:\cmsis-toolbox\bin;$env:PATH"
  {{< /tab >}}
{{< /tabpane >}}

{{% notice Tip %}}
Add these exports to your shell profile (`~/.bashrc`, `~/.zshrc`, or equivalent) so they persist across sessions.
{{% /notice %}}

The table below summarizes the key environment variables:

| Variable | Description |
|----------|-------------|
| `CMSIS_PACK_ROOT` | Root directory for installed CMSIS-Packs |
| `CMSIS_COMPILER_ROOT` | Path to the CMSIS-Toolbox `etc` directory containing compiler configuration files |
| `PATH` | Must include the CMSIS-Toolbox `bin` directory, CMake, and Ninja |

### Initialize the pack directory

Run the following command to initialize the CMSIS-Pack index:

```bash
cpackget init https://www.keil.com/pack/index.pidx
```

### Install Alif Ensemble Pack

Add the Alif Ensemble device pack:

```bash
cpackget add AlifSemiconductor::Ensemble@2.0.4
```

Verify the pack is installed:

```bash
cpackget list
```

The output includes:
```output
AlifSemiconductor::Ensemble@2.0.4
```

### Verify CMSIS-Toolbox installation

Confirm that `cbuild` is available and reports version 2.6.0 or later:

```bash
cbuild --version
```

Expected output:
```output
cbuild 2.6.0
```

## Install J-Link

J-Link is used for programming and debugging the Alif E8 hardware.

{{% notice Note %}}
J-Link version 7.94 or later is required for Alif Ensemble E8 support.
{{% /notice %}}

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
# Download from SEGGER website or use Homebrew
brew install --cask segger-jlink

# Verify installation
JLinkExe --version
# Expected output: SEGGER J-Link Commander V7.94 or later
  {{< /tab >}}
  {{< tab header="Linux" language="bash">}}
# Download from SEGGER website
wget https://www.segger.com/downloads/jlink/JLink_Linux_x86_64.deb
sudo dpkg -i JLink_Linux_x86_64.deb

# Verify installation
JLinkExe --version
  {{< /tab >}}
  {{< tab header="Windows" language="text">}}
1. Download installer from https://www.segger.com/downloads/jlink/
2. Run the installer and follow prompts
3. Verify in Command Prompt: JLink.exe --version
  {{< /tab >}}
{{< /tabpane >}}

## Install SETOOLS

SETOOLS (Secure Enclave Tools) is Alif's proprietary toolset for flashing firmware to MRAM via the Secure Enclave.

{{% notice Important %}}
SETOOLS is provided by Alif Semiconductor. Contact Alif support to obtain the latest release for your platform.
{{% /notice %}}

### Install SETOOLS

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
# Extract the release package (provided by Alif)
cd ~/Downloads
unzip app-release-exec-macos.zip
cd app-release-exec-macos

# Make tools executable
chmod +x app-gen-toc app-write-mram

# Add to PATH (add to ~/.zshrc or ~/.bashrc)
export PATH="$PATH:$HOME/Downloads/app-release-exec-macos"
echo 'export PATH="$PATH:$HOME/Downloads/app-release-exec-macos"' >> ~/.zshrc
  {{< /tab >}}
  {{< tab header="Linux" language="bash">}}
# Extract the release package
cd ~/Downloads
unzip app-release-exec-linux.zip
cd app-release-exec-linux

# Make tools executable
chmod +x app-gen-toc app-write-mram

# Add to PATH
export PATH="$PATH:$HOME/Downloads/app-release-exec-linux"
echo 'export PATH="$PATH:$HOME/Downloads/app-release-exec-linux"' >> ~/.bashrc
  {{< /tab >}}
  {{< tab header="Windows" language="text">}}
1. Extract app-release-exec-windows.zip to a folder (for example, C:\setools)
2. Add the folder to your system PATH:
   - Right-click "This PC" → Properties → Advanced System Settings
   - Click "Environment Variables"
   - Under System Variables, select PATH and click Edit
   - Add the SETOOLS folder path
   - Click OK on all dialogs
  {{< /tab >}}
{{< /tabpane >}}

### macOS Gatekeeper Warning

On macOS, when you first run SETOOLS commands, you may see a security warning:

![macOS cannot verify developer warning alt-text#center](macos-not-opened-warning.jpg "macOS Gatekeeper warning for SETOOLS")

To allow SETOOLS to run:

1. Open **System Preferences** → **Security & Privacy** → **General**
2. Click **Allow Anyway** for the blocked app

![macOS Security allow SETOOLS alt-text#center](macos-allow-setools.jpg "Allow SETOOLS in macOS Security settings")

### Verify SETOOLS Installation

Test that SETOOLS is accessible:

```bash
app-write-mram -d
```

If your Alif E8 DevKit is connected, the output shows device information:

```output
Device Part# AE722F80F55D5AS Rev A1
MRAM Size (KB)  = 5632  (5.5 MB)
SRAM Size (KB)  = 13824 (13.5 MB)
```

{{% notice Note %}}
The DK-E8-Alpha DevKit may contain E7 silicon (AE722F80F55D5AS) rather than E8 silicon. SETOOLS auto-detects your actual chip. You'll use the detected silicon type when building projects.
{{% /notice %}}

## Install Serial Terminal Software

For viewing UART debug output, you need a serial terminal program.

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
# Install picocom
brew install picocom

# Verify installation
picocom --help
  {{< /tab >}}
  {{< tab header="Linux" language="bash">}}
# Install picocom or minicom
sudo apt-get install picocom minicom

# Verify installation
picocom --help
  {{< /tab >}}
  {{< tab header="Windows" language="text">}}
Download and install PuTTY from https://www.putty.org/
  {{< /tab >}}
{{< /tabpane >}}

## Summary

You have installed:
- ✅ Docker for the build environment
- ✅ CMSIS-Toolbox (cbuild 2.6.0+) for Alif E8 projects
- ✅ J-Link (7.94+) for programming and debugging
- ✅ SETOOLS for Alif-specific flashing
- ✅ Serial terminal for UART debugging

In the next section, you'll set up the hardware connections.
