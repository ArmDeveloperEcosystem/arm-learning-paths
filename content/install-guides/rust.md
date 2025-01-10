---
title: Rust for Linux Applications
minutes_to_complete: 10
official_docs: https://www.rust-lang.org/tools/install
author_primary: Mathias Brossard
additional_search_terms:
- compiler
- linux
- rust

test_images:
- ubuntu:latest

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: FALSE            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Rust](https://www.rust-lang.org/) is an open source programming language. 

This install guide is for Linux application developers wishing to use Rust. 

If you wish to use Rust to build embedded applications for Arm, refer to [Rust for Embedded Applications](/install-guides/rust_embedded/) instead.

## Before you begin

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

## Installation {#install}

### Installing dependencies on Debian based distributions such as Ubuntu

Use the `apt` command to install the required software packages on any Debian-based Linux distribution, including Ubuntu.

```bash { target="ubuntu:latest" }
sudo apt update 
sudo apt install -y curl gcc
```

### Installing dependencies on Red Hat / Fedora / Amazon Linux

These Linux distributions use `yum` as the package manager.

Use the `yum` command to install the required software packages. If the machine has `sudo` you can use it.

```bash { target="fedora:latest" }
sudo yum update -y
sudo yum install -y curl gcc
```

### Download and install Rust

Run the following command to download and install Rust:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
```

The installer output will be similar to:

```output
info: downloading installer
info: profile set to 'default'
info: default host triple is aarch64-unknown-linux-gnu
info: syncing channel updates for 'stable-aarch64-unknown-linux-gnu'
info: latest update on 2023-12-07, rust version 1.74.1 (a28077b28 2023-12-04)
info: downloading component 'cargo'
info: downloading component 'clippy'
info: downloading component 'rust-docs'
info: downloading component 'rust-std'
info: downloading component 'rustc'
info: downloading component 'rustfmt'
info: installing component 'cargo'
info: installing component 'clippy'
info: installing component 'rust-docs'
 13.6 MiB /  13.6 MiB (100 %)   8.2 MiB/s in  1s ETA:  0s
info: installing component 'rust-std'
 32.8 MiB /  32.8 MiB (100 %)  12.6 MiB/s in  2s ETA:  0s
info: installing component 'rustc'
 75.5 MiB /  75.5 MiB (100 %)  17.7 MiB/s in  4s ETA:  0s
info: installing component 'rustfmt'
info: default toolchain set to 'stable-aarch64-unknown-linux-gnu'

  stable-aarch64-unknown-linux-gnu installed - rustc 1.70.0 (90c541806 2023-05-31)


Rust is installed now. Great!

To get started, you may need to restart your current shell.
This reloads your PATH environment variable to include
Cargo's bin directory ($HOME/.cargo/bin).

To configure your current shell, run:
source "$HOME/.cargo/env"
```

The latest version of Rust is now installed. 

The installer updates `$HOME/.bashrc` and `SHOME/.profile` to set up the environment. Start a new shell or run the following command to continue:

```bash
source "$HOME/.cargo/env"
```

To confirm the installation is complete run `cargo version` (`cargo` is the Rust package manager):

```bash { env_source="~/.bashrc" }
cargo version
```

This command will print the version:

```output
cargo 1.74.1 (ecb9851af 2023-10-18)
```

You are ready to use the Rust programming language on your Arm Linux machine.

## Get started {#start}

To compile an example program, run the following commands:

```bash { env_source="~/.bashrc" }
cargo new hello
cd hello
cargo run
```

The `cargo run` command outputs:

```output
   Compiling hello v0.1.0 (/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.44s
     Running `target/debug/hello`
Hello, world!
```
