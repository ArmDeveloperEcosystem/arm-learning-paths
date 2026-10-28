---
title: Pethost CLI

description: Install the Pethost CLI on Arm Linux, macOS on Apple silicon, or Windows on Arm, and verify it so you can deploy and manage Pethost projects from the terminal.

additional_search_terms:
- cloud
- deploy
- hosting
- docker compose

minutes_to_complete: 5

author: Stephan Gomer

official_docs: https://pethost.dev/docs/cli/

test_images:
- ubuntu:latest
test_maintenance: true

### FIXED, DO NOT MODIFY
weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

[Pethost](https://pethost.dev/) is a hosting service that runs your Docker Compose projects on a Linux machine whose size your plan sets. Its command-line tool, `pethost`, puts a folder online with one command, then shows and changes what runs there: logs, requests, a shell, secrets, and domains.

The CLI is open source under the MIT license. Each release includes arm64 builds for Linux and macOS, and an ARM64 build for Windows on Arm. A build is one file with nothing else to install, so you download the file for your platform, check it against the release's checksums, and put it on your `PATH`.

## Before you begin

Confirm you're using a 64-bit Arm computer. On Linux, run:

```bash { target="ubuntu:latest" }
uname -m
```

The output is:

```output
aarch64
```

On macOS, the same command prints `arm64`.

On Windows, run the following command in PowerShell:

```console
$env:PROCESSOR_ARCHITECTURE
```

The output is:

```output
ARM64
```

If you see `x86_64` on a Mac with Apple silicon, or `AMD64` on Windows on Arm, your terminal runs under x86-64 emulation. See [Troubleshooting](#troubleshooting).

## How do I install the Pethost CLI?

{{% notice Note %}}
The following commands use pethost version 0.2.5. The same commands work with other versions: replace `0.2.5` in the download URLs with the version of your choice. To find the latest version, see the [pethost releases](https://github.com/pethost-dev/cli/releases).
{{% /notice %}}

### Install on Arm Linux

Download the arm64 binary and the release's checksums:

```bash { target="ubuntu:latest" }
curl -fsSLO https://github.com/pethost-dev/cli/releases/download/v0.2.5/pethost-linux-arm64
curl -fsSLO https://github.com/pethost-dev/cli/releases/download/v0.2.5/checksums.txt
```

Check the binary against its checksum:

```bash { target="ubuntu:latest" }
grep ' pethost-linux-arm64$' checksums.txt | sha256sum -c
```

The output is:

```output
pethost-linux-arm64: OK
```

Install it as `pethost` in `~/.local/bin`, which doesn't need `sudo`:

```bash { target="ubuntu:latest" }
mkdir -p ~/.local/bin
install -m 755 pethost-linux-arm64 ~/.local/bin/pethost
```

If `~/.local/bin` isn't on your `PATH` yet, add it:

```bash { target="ubuntu:latest" }
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Install on macOS

Download the arm64 binary for macOS and the release's checksums, then check the binary:

```console
curl -fsSLO https://github.com/pethost-dev/cli/releases/download/v0.2.5/pethost-darwin-arm64
curl -fsSLO https://github.com/pethost-dev/cli/releases/download/v0.2.5/checksums.txt
grep ' pethost-darwin-arm64$' checksums.txt | shasum -a 256 -c
```

The output is:

```output
pethost-darwin-arm64: OK
```

Install it in `~/.local/bin`, and add that directory to your `PATH` in zsh, the default shell on macOS:

```console
mkdir -p ~/.local/bin
install -m 755 pethost-darwin-arm64 ~/.local/bin/pethost
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Install on Windows on Arm

In PowerShell, download the ARM64 binary and the release's checksums:

```console
Invoke-WebRequest -UseBasicParsing -Uri https://github.com/pethost-dev/cli/releases/download/v0.2.5/pethost-windows-arm64.exe -OutFile pethost-windows-arm64.exe
Invoke-WebRequest -UseBasicParsing -Uri https://github.com/pethost-dev/cli/releases/download/v0.2.5/checksums.txt -OutFile checksums.txt
```

Compare the binary's SHA-256 hash with its line in the checksums:

```console
$expected = (Select-String -Path checksums.txt -Pattern ' pethost-windows-arm64.exe$').Line.Split(' ')[0]
(Get-FileHash -Algorithm SHA256 pethost-windows-arm64.exe).Hash -eq $expected
```

The output is:

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

The last line updates the window you're in. New windows read the user `Path`.

### Use the install script

The install scripts do the same steps for the newest release. They pick the binary for your CPU, check it against the release's checksums, and put it in `~/.local/bin`, without `sudo` or an administrator.

On Linux or macOS, run:

```console
curl -fsSL https://pethost.dev/install.sh | sh
```

On Windows, run the following command in PowerShell:

```console
irm https://pethost.dev/install.ps1 | iex
```

The scripts change no settings. When `~/.local/bin` isn't on your `PATH`, they print the command that adds it.

## How do I verify the installation?

Print the version:

```bash { target="ubuntu:latest" env_source="~/.bashrc" }
pethost --version
```

The output is:

```output
pethost 0.2.5
```

The same command works on macOS and in PowerShell.

On Linux and macOS, confirm that the installed file is the arm64 build:

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

On Windows, the hash you compared confirms that you installed the ARM64 build.

## Troubleshooting

- **The x86-64 build is installed on a Mac with Apple silicon.** The install script reads `uname -m`, which prints `x86_64` in a terminal that runs under Rosetta 2. The x86-64 build then runs under emulation too. Use a terminal that doesn't open with Rosetta, confirm that `uname -m` prints `arm64`, and run the script again.
- **The x64 build is installed on Windows on Arm.** The install script reads `$env:PROCESSOR_ARCHITECTURE`, which is `AMD64` in an x64 build of PowerShell, because Windows runs that build under emulation. Use the ARM64 build of PowerShell 7 or Windows PowerShell, confirm that `$env:PROCESSOR_ARCHITECTURE` prints `ARM64`, and run the script again.
- **`pethost` isn't found.** The shell prints `pethost: command not found`, or PowerShell says the term `pethost` isn't recognized, when `~/.local/bin` isn't on your `PATH`. Add it as the install steps for your platform show, then open a new terminal.

## Next steps

To deploy, you need a Pethost account with a plan. In a folder with a `Dockerfile` or a compose file, run:

```console
pethost deploy
```

The first time, your browser opens the Pethost panel to sign you in, and the command asks for the project's name, which becomes its address. It then sends the folder to your machine, which builds and starts it, and prints the address.

To move to a newer release later, run `pethost update`. It replaces the program with the newest release, checked against the release's checksums.

For every command and its flags, see the [Pethost CLI reference](https://pethost.dev/docs/cli/).
