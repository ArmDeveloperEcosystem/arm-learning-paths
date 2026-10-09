---
title: Rust for Linux Applications
description: Install Rust on Arm Linux and compile a sample project so you can build Linux applications with the Rust toolchain.
minutes_to_complete: 10
official_docs: https://www.rust-lang.org/tools/install
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=rust
author: Mathias Brossard
additional_search_terms:
- compiler
- linux
- rust

test_images:
- ubuntu:latest
test_maintenance: true

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Rust](https://www.rust-lang.org/) is an open source programming language.

This install guide is for Linux application developers who use Rust.

If you want to use Rust for embedded applications on Arm, see [Rust for Embedded Applications](/install-guides/rust_embedded/) instead.

## What are the prerequisites before installing Rust on Arm Linux?

Rust is available for a variety of operating systems and Linux distributions, and there are multiple ways to install it.

This install guide provides a quick solution to install Rust on an Arm Linux distribution.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## How do I install Rust on an Arm Linux system? {#install}

### How do I install dependencies on Debian-based distributions?

Use the `apt` command to install the required software packages on any Debian-based Linux distribution, including Ubuntu.

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install -y curl gcc
```

### How do I install dependencies on Red Hat, Fedora, or Amazon Linux?

These Linux distributions use `yum` as the package manager.

Use the `yum` command to install the required software packages. If the machine has `sudo` you can use it.

```console
sudo yum update -y
sudo yum install -y curl gcc
```

### How do I download and install Rust?

Run the following command to download and install Rust:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
```

The installer output is similar to:

```output
info: downloading installer
info: profile set to default
info: default host triple is aarch64-unknown-linux-gnu
info: syncing channel updates for stable-aarch64-unknown-linux-gnu
info: latest update on 2026-08-20 for version 1.98.0 (88d9e12ae 2026-08-18)
info: downloading 6 components
info: default toolchain set to stable-aarch64-unknown-linux-gnu

  stable-aarch64-unknown-linux-gnu installed - rustc 1.98.0 (88d9e12ae 2026-08-18)


Rust is installed now. Great!

To get started you may need to restart your current shell.
This would reload your PATH environment variable to include
Cargo's bin directory ($HOME/.cargo/bin).

To configure your current shell, you need to source
the corresponding env file under $HOME/.cargo.

This is usually done by running one of the following (note the leading DOT):
. "$HOME/.cargo/env"            # For sh/bash/zsh/ash/dash/pdksh
source "$HOME/.cargo/env.fish"  # For fish
```

The latest version of Rust is now installed.

The installer updates `$HOME/.bashrc` and `$HOME/.profile` to set up the environment. Start a new shell or run the following command to continue:

```bash
source "$HOME/.cargo/env"
```

To confirm the installation is complete, run `cargo version` (`cargo` is the Rust package manager):

```bash { env_source="~/.bashrc" }
cargo version
```

The output is similar to:

```output
cargo 1.98.0 (797e8a9bc 2026-08-05)
```

You are ready to use the Rust programming language on your Arm Linux machine.

## How do I get started using Rust? {#start}

To compile an example program, run the following commands:

```console
cargo new hello
cd hello
cargo run
```

The `cargo run` command outputs:

```output
   Compiling hello v0.1.0 (/home/user/hello)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.54s
     Running `target/debug/hello`
Hello, world!
```
