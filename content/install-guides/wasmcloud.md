---
title: wasmCloud
description: Install and verify the wash CLI for wasmCloud on Arm Linux so you can develop and run WebAssembly components on Arm servers and cloud instances.
minutes_to_complete: 10
official_docs: https://wasmcloud.com/docs/installation/
author: Jason Andrews
draft: true
additional_search_terms:
  - wash
  - WebAssembly
  - WASI
  - Graviton
  - aarch64

### FIXED, DO NOT MODIFY
weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

[wasmCloud](https://wasmcloud.com/) hosts applications packaged as WebAssembly components. Its Wasm Shell, `wash`, provides commands for developing, building, and running components, including a local development server through `wash dev`.

You can install `wash` on Arm Linux without compiling wasmCloud or installing Rust. To build an application, you'll need the appropriate language toolchain.

## Before you begin

You need an Arm Linux system and internet access. 

Confirm your processor architecture:

```bash
uname -m
```

The expected output is:

```output
aarch64
```

## Install `wash`

There are two ways to install `wash`. The install script is a single command that always installs the latest version. The GitHub release download lets you pin a specific version and verify the checksum before installing.

### Install using the install script

Run the install script to download and install `wash`:

```bash
curl -fsSL https://wasmcloud.com/sh | bash
```

The script detects your platform automatically and installs `wash` to `~/.wash/bin`. 

The output is similar to:

```output
[INFO] Installing wash - The Wasm Shell
[INFO] Install directory: ~/.wash/bin
[INFO] Detecting platform...
[INFO] Platform detected: aarch64-unknown-linux-gnu
[INFO] Fetching latest release information...
[INFO] Version: v2.12.0
[INFO] Downloading wash binary...
[SUCCESS] wash v2.12.0 installed successfully to ~/.wash/bin/wash
[SUCCESS] Verified installation
```

The script updates your shell profile automatically.

 Open a new terminal, or run the following command to use `wash` in your current session:

```bash
source ~/.bashrc
```

### Install a specific version from GitHub

Use this method when you need a pinned, verifiable install. 

Install `curl` and `ca-certificates`:

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl
```

{{% notice Note %}}
The following commands use `wash` version `2.11.0`. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [wasmCloud releases](https://github.com/wasmCloud/wasmCloud/releases).
{{% /notice %}}

Download the prebuilt Arm64 binary:

```bash
mkdir -p "$HOME/.cache/wasmcloud-install/2.11.0"
curl -fL --retry 3 \
  https://github.com/wasmCloud/wasmCloud/releases/download/v2.11.0/wash-aarch64-unknown-linux-gnu \
  -o "$HOME/.cache/wasmcloud-install/2.11.0/wash"
```

Verify the SHA-256 checksum against the value published for the [v2.11.0 release](https://github.com/wasmCloud/wasmCloud/releases/tag/v2.11.0):

```bash
printf '%s  %s\n' \
  'c3b2204dd99ae2bc46c1236967f4a328cebe3b57d3d5a1605091618eff66bcad' \
  "$HOME/.cache/wasmcloud-install/2.11.0/wash" \
  | sha256sum --check
```

The output is similar to:

```output
/home/ubuntu/.cache/wasmcloud-install/2.11.0/wash: OK
```

If your username isn't `ubuntu`, the path will reflect your actual username. If the checksum fails, download the file again and confirm that the version and asset name match before continuing.

Install `wash` to your user executable directory:

```bash
mkdir -p "$HOME/.local/bin"
install -m 0755 "$HOME/.cache/wasmcloud-install/2.11.0/wash" "$HOME/.local/bin/wash"
```

Add `$HOME/.local/bin` to your PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

## Verify the installation

Check the installed version:

```bash
wash --version
```

The output is similar to:

```output
wash 2.12.0
```

Confirm that the development host command is available:

```bash
wash dev --help
```

The output is similar to:

```output
Start a development server for a Wasm component

Usage: wash dev [OPTIONS]

Options:
  -o, --output <OUTPUT>
          Specify output format (text or json)

          [default: text]

  -l, --log-level <LOG_LEVEL>
          Set the opentelemetry log level (trace, debug, info, warn, error)

          [default: INFO]

      --verbose
          Enable verbose output

      --non-interactive
          Run in non-interactive mode: skip terminal checks for host exec and accept the default
          answer for any confirmation prompts. Automatically enabled when stdin is not a TTY

      --user-config <USER_CONFIG>
          Path to user configuration file

      --meters <METERS>
          What to measure about guests: `off`, `duration`, or `fuel` [default: duration]

  -h, --help
          Print help (see a summary with '-h')
```

Displaying help doesn't start a listener or load an application.

## Next steps

You can now use `wash` to build and run a WebAssembly application on Arm. 

To learn more, see [Run and benchmark a WebAssembly application on AWS Graviton with wasmCloud](/learning-paths/servers-and-cloud-computing/wasmcloud/).
