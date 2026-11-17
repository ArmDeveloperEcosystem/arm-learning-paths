---
title: Arm GNU Toolchain
description: Install the Arm GNU Toolchain on Windows, Linux, or macOS for bare-metal and embedded Arm targets such as Cortex-M and Cortex-R.

author: Jason Andrews
minutes_to_complete: 10
official_docs: https://gcc.gnu.org/onlinedocs/

test_maintenance: false
test_images:
- ubuntu:latest

layout: installtoolsall
multi_install: false
multitool_install_part: true
tool_install: false
weight: 2

additional_search_terms:
- compiler
- arm-none-eabi
- embedded
- Cortex-M
- Cortex-R
- microcontroller
- bare-metal
- firmware
---

The [Arm GNU Toolchain](https://gitlab.arm.com/tooling/gnu-toolchains-for-arm) is a community-supported, pre-built GNU compiler toolchain for Arm CPUs. Use it to build bare-metal software or software that uses a real-time operating system (RTOS) for supported Cortex-M, Cortex-R, and Cortex-A processors. To cross-compile Linux applications, see the [cross-compiler](../cross) install guide instead.

## Choose your target

| Compiler | Target |
|----------|--------|
| `arm-none-eabi-gcc` | Cortex-M software |
| `arm-none-eabi-gcc` | 32-bit software for supported Cortex-R and Cortex-A processors (AArch32) |
| `aarch64-none-elf-gcc` | 64-bit software for supported Cortex-R and Cortex-A processors (AArch64) |

For Cortex-A and Cortex-R, check your board or RTOS documentation to determine whether your project uses 32-bit or 64-bit software.

## Quick install

The commands use the `arm-none-eabi` toolchain, the right choice for most embedded developers.

For 64-bit software, choose an available `aarch64-none-elf` package for your host computer from the download tables. Replace `arm-none-eabi` with `aarch64-none-elf` in the filenames, installation paths, and compiler commands.

Select the tab for your host computer. The macOS commands assume you use Zsh, and the Linux commands assume you use Bash. For a graphical installer on Windows, see [Graphical install](#graphical-install).

On Windows, open Command Prompt as administrator and change to your download directory before running the commands.

{{% notice Note %}}
The examples use Arm GNU Toolchain version 15.3.rel1. To use another release, choose the package for your host computer and software target, then update the filenames and installation paths accordingly. See the [Arm GNU Toolchain releases](https://gitlab.arm.com/tooling/gnu-toolchains-for-arm) for available versions.
{{% /notice %}}

{{< tabpane code=true >}}
  {{< tab header="Windows (Command Prompt)" language="console" >}}
curl.exe -LO https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-mingw-w64-x86_64-arm-none-eabi.msi
start "" /wait msiexec.exe /i "arm-gnu-toolchain-15.3.rel1-mingw-w64-x86_64-arm-none-eabi.msi" EULA=1 /quiet /norestart
"%ProgramFiles%\Arm\GNU Toolchain mingw-w64-x86_64-arm-none-eabi\bin\gccvar.bat"
{{< /tab >}}
  {{< tab header="macOS (Apple Silicon)" language="bash" >}}
curl -LO https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-darwin-arm64-arm-none-eabi.pkg
sudo installer -pkg arm-gnu-toolchain-15.3.rel1-darwin-arm64-arm-none-eabi.pkg -target /
echo 'export PATH="/Applications/ArmGNUToolchain/15.3.rel1/arm-none-eabi/bin:$PATH"' >> ~/.zprofile
source ~/.zprofile
{{< /tab >}}
  {{< tab header="Linux (x86_64)" language="bash" >}}
curl -LO https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-x86_64-arm-none-eabi.tar.xz
tar xJf arm-gnu-toolchain-15.3.rel1-x86_64-arm-none-eabi.tar.xz -C $HOME
echo 'export PATH="$PATH:$HOME/arm-gnu-toolchain-15.3.rel1-x86_64-arm-none-eabi/bin"' >> ~/.bashrc
source ~/.bashrc
{{< /tab >}}
  {{< tab header="Linux (AArch64)" language="bash" >}}
curl -LO https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-aarch64-arm-none-eabi.tar.xz
tar xJf arm-gnu-toolchain-15.3.rel1-aarch64-arm-none-eabi.tar.xz -C $HOME
echo 'export PATH="$PATH:$HOME/arm-gnu-toolchain-15.3.rel1-aarch64-arm-none-eabi/bin"' >> ~/.bashrc
source ~/.bashrc
{{< /tab >}}
{{< /tabpane >}}

After running the commands for your host computer, [verify the installation](#verify-the-installation).

On Windows, `gccvar.bat` sets PATH for the current Command Prompt session. Run it again whenever you open a new Command Prompt.

## Install on Windows

{{% notice Note %}}
32-bit Windows (mingw-w64-i686) toolchains are deprecated and will be removed in a future release. Use the 64-bit (mingw-w64-x86_64) packages instead.
{{% /notice %}}

Download the `.msi` installer or `.zip` archive for your target from the table below.

| Target | MSI installer | ZIP archive |
|--------|--------------|-------------|
| 32-bit software (`arm-none-eabi`) | [arm-none-eabi MSI](https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-mingw-w64-x86_64-arm-none-eabi.msi) | [arm-none-eabi ZIP](https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-mingw-w64-x86_64-arm-none-eabi.zip) |
| 64-bit software (`aarch64-none-elf`) | [aarch64-none-elf MSI](https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-mingw-w64-x86_64-aarch64-none-elf.msi) | [aarch64-none-elf ZIP](https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-mingw-w64-x86_64-aarch64-none-elf.zip) |

### Graphical install

1. Double-click the `.msi` file and follow the on-screen prompts.
2. Open Command Prompt and run `gccvar.bat` from the installed `bin` directory. For the default installation location, use:

```console
"%ProgramFiles%\Arm\GNU Toolchain mingw-w64-x86_64-arm-none-eabi\bin\gccvar.bat"
```

If you chose a different installation directory or installed `aarch64-none-elf`, adjust the path accordingly. Keep this window open to verify the installation.

### Command line install

Open Command Prompt as administrator and change to the directory containing the downloaded `.msi` file. To install silently, use the filename for your target:

```console
start "" /wait msiexec.exe /i "arm-gnu-toolchain-15.3.rel1-mingw-w64-x86_64-arm-none-eabi.msi" EULA=1 /quiet /norestart
```

The command waits for the silent installation to finish.

| Property | Effect |
|----------|--------|
| `EULA=1` | Accept the license agreement |
| `/quiet` | Silent mode, no GUI |
| `/norestart` | Prevent an automatic restart |

After a successful installation, run `gccvar.bat` to set PATH for your current Command Prompt session:

```console
"%ProgramFiles%\Arm\GNU Toolchain mingw-w64-x86_64-arm-none-eabi\bin\gccvar.bat"
```

Adjust the path if you installed `aarch64-none-elf`. Keep this window open to verify the installation. Run `gccvar.bat` again whenever you open a new Command Prompt.

### ZIP package install

If you can't run the MSI installer, download the `.zip` file for your target from the table above, then use PowerShell to extract it.

The commands use the default `arm-none-eabi` package. For `aarch64-none-elf`, replace `arm-none-eabi` in both the archive filename and the extracted directory path.

Extract the archive:

```console
Expand-Archive -Path arm-gnu-toolchain-15.3.rel1-mingw-w64-x86_64-arm-none-eabi.zip -DestinationPath C:\
```

Open Command Prompt and run `gccvar.bat` from the extracted `bin` directory. Keep this window open to verify the installation.

```console
C:\arm-gnu-toolchain-15.3.rel1-mingw-w64-x86_64-arm-none-eabi\bin\gccvar.bat
```

## Install on macOS

Arm GNU Toolchain 15.3.rel1 provides Apple Silicon builds only.

### Download

| Target | Download |
|--------|----------|
| 32-bit software (`arm-none-eabi`) | [arm-none-eabi PKG](https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-darwin-arm64-arm-none-eabi.pkg) |
| 64-bit software (`aarch64-none-elf`) | [aarch64-none-elf PKG](https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-darwin-arm64-aarch64-none-elf.pkg) |

### Install using the .pkg file

Download and run the installer:

```bash
curl -LO https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-darwin-arm64-arm-none-eabi.pkg
sudo installer -pkg arm-gnu-toolchain-15.3.rel1-darwin-arm64-arm-none-eabi.pkg -target /
```

For Zsh, the default macOS shell, add the toolchain to your user PATH:

```bash
echo 'export PATH="/Applications/ArmGNUToolchain/15.3.rel1/arm-none-eabi/bin:$PATH"' >> ~/.zprofile
source ~/.zprofile
```

The `source` command applies the PATH change to your current session. New Zsh login sessions load it automatically.

If you use Bash, add the same `export PATH=` line to `~/.bash_profile` instead. For other shells, use the appropriate PATH syntax and configuration file.

## Install on Linux

Linux packages are distributed as tar archives for x86_64 and AArch64 hosts.

### Download

| Host | Target | Download |
|------|--------|----------|
| x86_64 | 32-bit software (`arm-none-eabi`) | [arm-none-eabi tar.xz](https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-x86_64-arm-none-eabi.tar.xz) |
| x86_64 | 64-bit software (`aarch64-none-elf`) | [aarch64-none-elf tar.xz](https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-x86_64-aarch64-none-elf.tar.xz) |
| AArch64 | 32-bit software (`arm-none-eabi`) | [arm-none-eabi tar.xz](https://gitlab.arm.com/api/v4/projects/10698/packages/generic/gnu-toolchain/15.3.rel1/arm-gnu-toolchain-15.3.rel1-aarch64-arm-none-eabi.tar.xz) |

Download your chosen file from the table, then extract it to your preferred install directory.

The commands use the default `arm-none-eabi` package on an x86_64 host. Use the filename and extracted directory name for the package you downloaded in both the extraction and PATH commands.

On Ubuntu or Debian, install `xz-utils` if it's not already available:

```bash
sudo apt install xz-utils -y
```

On other Linux distributions, install the `xz` utility using your distribution's package manager.

Extract the archive:

```bash
tar xJf arm-gnu-toolchain-15.3.rel1-x86_64-arm-none-eabi.tar.xz -C $HOME
```

If you use Bash, add the `bin` directory to your PATH:

```bash
echo 'export PATH="$PATH:$HOME/arm-gnu-toolchain-15.3.rel1-x86_64-arm-none-eabi/bin"' >> ~/.bashrc
source ~/.bashrc
```

If you use another shell, add the same `bin` directory to your PATH in that shell's configuration file.

## Verify the installation

These steps apply to all operating systems.

On macOS or Linux, open a new terminal. On Windows, use the Command Prompt window where you ran `gccvar.bat`.

Check the default `arm-none-eabi` toolchain:

```bash
arm-none-eabi-gcc --version
```

If you installed the 64-bit toolchain, use `aarch64-none-elf-gcc --version` instead.

The output is similar to:

```output
arm-none-eabi-gcc (Arm GNU Toolchain 15.3.Rel1 (Build arm-15.149)) 15.3.1 20260627
Copyright (C) 2025 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## Arm Development Studio

To use the Arm GNU Toolchain with Arm Development Studio, you may need to follow the instructions to [register a compiler toolchain](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Register-a-compiler-toolchain).

## Older versions

All releases, including older versions, are available from the [Arm GNU Toolchain GitLab repository](https://gitlab.arm.com/tooling/gnu-toolchains-for-arm).
