---
title: Pethost CLI

description: Install the Pethost CLI on Arm Linux, macOS on Apple silicon, or Windows on Arm, and verify it so you can deploy and manage Pethost projects from the terminal.

additional_search_terms:

- docker compose
- pethost

minutes_to_complete: 5

author: Stephan Gomer

official_docs: https://pethost.dev/docs/cli/

test_images:
- ubuntu:latest
test_maintenance: false

### FIXED, DO NOT MODIFY
weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

[Pethost](https://pethost.dev/) hosts your Docker Compose projects on a Linux machine sized according to your plan. Its command-line interface (CLI), `pethost`, deploys a folder with one command. You can also use the CLI to inspect logs and requests, open a shell, and manage secrets and domains.

The CLI is open source under the MIT license. Each release includes `arm64` builds for Linux and macOS, and an ARM64 build for Windows on Arm. 

## Before you begin

Confirm that you're using a 64-bit Arm computer. 

On Linux, run:

```bash { target="ubuntu:latest" }
uname -m
```

The expected output is:

```output
aarch64
```

On macOS, the same command prints `arm64`.

On Windows, run the following command in PowerShell:

```console
$env:PROCESSOR_ARCHITECTURE
```

The expected output is:

```output
ARM64
```

If you see `x86_64` on a Mac with Apple silicon, or `AMD64` on Windows on Arm, your terminal runs under x86-64 emulation. For a resolution, see [Troubleshoot installation issues](#troubleshoot-installation-issues).

## Install the Pethost CLI

The CLI is a single executable. To install it manually, download the file for your platform, verify its checksum, and put it in a directory on your `PATH`.

{{% notice Note %}}
The manual installation commands use Pethost CLI version `0.2.5`. To install another version, replace `0.2.5` in the download URLs. To find the latest version, see the [Pethost CLI releases](https://github.com/pethost-dev/cli/releases).
{{% /notice %}}

### Install manually on Arm Linux

Download the `arm64` binary and the release checksums:

```bash { target="ubuntu:latest" }
curl -fsSLO https://github.com/pethost-dev/cli/releases/download/v0.2.5/pethost-linux-arm64
curl -fsSLO https://github.com/pethost-dev/cli/releases/download/v0.2.5/checksums.txt
```

Check the binary against its checksum:

```bash { target="ubuntu:latest" }
grep ' pethost-linux-arm64$' checksums.txt | sha256sum -c
```

The expected output is:

```output
pethost-linux-arm64: OK
```

Install it as `pethost` in `~/.local/bin`, which doesn't need `sudo`:

```bash { target="ubuntu:latest" }
mkdir -p ~/.local/bin
install -m 755 pethost-linux-arm64 ~/.local/bin/pethost
```

If `~/.local/bin` isn't on your `PATH`, add it using the following commands for Bash:

```bash { target="ubuntu:latest" }
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Install manually on macOS

Download the `arm64` binary for macOS and the release checksums, then check the binary:

```console
curl -fsSLO https://github.com/pethost-dev/cli/releases/download/v0.2.5/pethost-darwin-arm64
curl -fsSLO https://github.com/pethost-dev/cli/releases/download/v0.2.5/checksums.txt
grep ' pethost-darwin-arm64$' checksums.txt | shasum -a 256 -c
```

The expected output is:

```output
pethost-darwin-arm64: OK
```

Install it in `~/.local/bin`, and add the directory to your `PATH` in `zsh`, the default shell on macOS:

```console
mkdir -p ~/.local/bin
install -m 755 pethost-darwin-arm64 ~/.local/bin/pethost
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Install manually on Windows on Arm

In PowerShell, download the ARM64 binary and the release checksums:

```console
Invoke-WebRequest -UseBasicParsing -Uri https://github.com/pethost-dev/cli/releases/download/v0.2.5/pethost-windows-arm64.exe -OutFile pethost-windows-arm64.exe
Invoke-WebRequest -UseBasicParsing -Uri https://github.com/pethost-dev/cli/releases/download/v0.2.5/checksums.txt -OutFile checksums.txt
```

Compare the SHA-256 hash of the binary with the matching entry in `checksums.txt`:

```console
$expected = (Select-String -Path checksums.txt -Pattern ' pethost-windows-arm64.exe$').Line.Split(' ')[0]
(Get-FileHash -Algorithm SHA256 pethost-windows-arm64.exe).Hash -eq $expected
```

The expected output is:

```output
True
```

Install it as `pethost.exe` in `~\.local\bin`, and add that folder to your user `Path`:

```console
New-Item -ItemType Directory -Force -Path "$HOME\.local\bin" | Out-Null
Move-Item -Force pethost-windows-arm64.exe "$HOME\.local\bin\pethost.exe"
[Environment]::SetEnvironmentVariable("Path", "$HOME\.local\bin;" + [Environment]::GetEnvironmentVariable("Path", "User"), "User")
$env:Path = "$HOME\.local\bin;$env:Path"
```

The last line updates `Path` for your current PowerShell session. New sessions use the saved user `Path`.

### Use the install script

As an alternative to manual installation, use an install script to install the latest release. The scripts select the binary for your CPU, verify its checksum, and install it in `~/.local/bin` (`~\.local\bin` on Windows). You don't need `sudo` or administrator privileges.

On Linux or macOS, run:

```console
curl -fsSL https://pethost.dev/install.sh | sh
```

The output is similar to:

```output
pethost 0.2.6 is in ~/.local/bin (checksum verified).
Next: cd into your app, and run   pethost deploy
```
The version and next steps depend on the release installed and your `PATH`.

On Windows, run the following command in PowerShell:

```console
irm https://pethost.dev/install.ps1 | iex
```

The scripts don't change your shell configuration or `PATH`. If the installation directory isn't on your `PATH`, run the command printed by the script, then open a new terminal.

## Verify the installation

Print the installed version. This command works on Linux, macOS, and in PowerShell:

```bash { target="ubuntu:latest" env_source="~/.bashrc" }
pethost --version
```

For the manual installation of version `0.2.5`, the expected output is:

```output
pethost 0.2.5
```

If you used an install script, the output shows the latest release available when you ran it. The version can differ from the example.

On Linux and macOS, confirm that the installed file is the `arm64` build:

```console
file ~/.local/bin/pethost
```

On Linux, the output is similar to:

```output
/home/user/.local/bin/pethost: ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV), statically linked, Go BuildID=nz0tP2R60YBR9Z7axS98/X6WT5iMG6VRsYMJfno1L/Y9z5cPPXsx8akoaCeuui/88htszulU7mndNGVCfQD, BuildID[sha1]=a519661c7e9469bb40a861474eba3a25138e55d0, stripped
```

On macOS, the output is similar to:

```output
/Users/user/.local/bin/pethost: Mach-O 64-bit executable arm64
```

On Windows, the hash that you compared confirms that you installed the ARM64 build.

## Troubleshoot installation issues

Use the following guidance to troubleshoot issues with installing `pethost`.

### The x86-64 build is installed on Apple silicon

The install script reads `uname -m`. In a terminal running under Rosetta 2, this command prints `x86_64`, so the script installs the x86-64 build.

Open a terminal without Rosetta, confirm that `uname -m` prints `arm64`, and run the script again.

### The x64 build is installed on Windows on Arm

In an x64 PowerShell session running under emulation, `$env:PROCESSOR_ARCHITECTURE` reports `AMD64`.

Use an ARM64 build of PowerShell 7 or Windows PowerShell. Confirm that `$env:PROCESSOR_ARCHITECTURE` prints `ARM64`, then run the script again.

### The pethost command isn't found

If the installation directory isn't on your `PATH`, your shell reports `pethost: command not found`. PowerShell reports that `pethost` isn't recognized.

Add the installation directory to your `PATH` using the instructions for your platform, then open a new terminal.

## Next steps

You can now host Docker compose projects on Pethost on Arm.

To deploy a project using `pethost`, you need a Pethost account with a plan. In a folder with a `Dockerfile` or a compose file, run:

```console
pethost deploy
```

On your first deployment, your browser opens the Pethost panel so that you can sign in. The command asks for a project name, which becomes its address. It then sends the folder to your Pethost machine to build and start the project, and prints the address.

To update the CLI later, run `pethost update`. It verifies the checksum of the latest release before replacing the installed executable.

For every command and its flags, see the [Pethost CLI reference](https://pethost.dev/docs/cli/).
