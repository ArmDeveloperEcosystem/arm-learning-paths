---
title: C2PA Tool
description: Install C2PA Tool on Arm Linux, macOS, or Windows on Arm to work with Content Credentials from the command line.
minutes_to_complete: 20
official_docs: https://github.com/contentauth/c2patool
author: Kostiantyn Perehuda

test_maintenance: false

### FIXED, DO NOT MODIFY
weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

Content Credentials use the Coalition for Content Provenance and Authenticity (C2PA) standard to record media provenance. [C2PA Tool](https://github.com/contentauth/c2patool), invoked as `c2patool`, reads, creates, and validates Content Credentials in supported media files. 

You can install C2PA Tool on 64-bit Arm Linux, macOS on Apple silicon, or Windows on Arm. The Linux instructions in this guide cover Ubuntu and Debian.

On macOS, you'll install C2PA Tool with Homebrew. 

On Arm Linux and Windows on Arm, use Cargo, the Rust package manager, to install C2PA Tool. With Cargo, you'll download the source code and compile it for Arm. This produces an executable for your Arm platform.

Homebrew and Cargo install the version available from their package source. For release
information, see [C2PA Tool releases](https://github.com/contentauth/c2patool/releases).

## Install on macOS

Install [Homebrew](https://brew.sh/) if it isn't already available, then install C2PA Tool:

```console
brew install c2patool
```

## Install on Arm Linux

Build C2PA Tool from source on your Arm Linux system to install a native `aarch64` executable.

Install the build dependencies on Ubuntu or Debian:

```console
sudo apt update
sudo apt install -y build-essential pkg-config libssl-dev
```

Install [Rust](/install-guides/rust/) to obtain Cargo, then build and install C2PA Tool from source:

```console
cargo install c2patool --locked
```

Cargo installs `c2patool` in `$HOME/.cargo/bin`.

## Install on Windows on Arm

Build C2PA Tool from source with the ARM64 Rust toolchain to install a native ARM64 executable
on Windows on Arm.

Install the Microsoft C++ Build Tools and [Rust](https://www.rust-lang.org/tools/install) with the
MSVC toolchain for ARM64. Install [7-Zip](https://www.7-zip.org/) and add its installation
directory (typically `C:\Program Files\7-Zip`) to your `PATH`.

Open a new PowerShell window and confirm that 7-Zip is available:

```console
7z -h
```

The output displays the 7-Zip version and command usage. 

Then, build and install C2PA Tool from source:

```console
cargo install c2patool --locked
```

Cargo installs `c2patool.exe` in `%USERPROFILE%\.cargo\bin`.

## Verify the installation

Print the installed version:

```console
c2patool --version
```

The output reports `c2patool` followed by the installed version number.

Display the command summary:

```console
c2patool --help
```

The expected output starts with:

```output
Tool for displaying and creating C2PA manifests.
```

## Troubleshoot installation issues

If your shell can't find `c2patool`, open a new terminal. For a Cargo installation, confirm that
`$HOME/.cargo/bin` on Linux or `%USERPROFILE%\.cargo\bin` on Windows is in your `PATH`.

## Update C2PA Tool

On macOS, run:

```console
brew update
brew upgrade c2patool
```

For a Cargo installation, run:

```console
cargo install c2patool --locked --force
```

## Uninstall C2PA Tool

For a Homebrew installation, run:

```console
brew uninstall c2patool
```

For a Cargo installation, run:

```console
cargo uninstall c2patool
```

## Next steps

You can now use the C2PA Tool to work with Content Credentials on Arm. 