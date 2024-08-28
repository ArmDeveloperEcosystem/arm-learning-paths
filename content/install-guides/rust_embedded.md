---
title: Rust for Embedded Applications
minutes_to_complete: 10
official_docs: https://docs.rust-embedded.org/
author_primary: Ronan Synnott
additional_search_terms:
- compiler
- rust

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: FALSE            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Rust](https://www.rust-lang.org/) is an open source programming language. 

This install guide is for developers using Rust for their embedded applications. 

If you are using Rust to build Linux applications on an Arm Linux platform, refer to [Rust for Linux Applications](/install-guides/rust/) instead.

This install guide describes a setup using an Ubuntu Linux host.

For a thorough review of all options, refer to the official documentation. See [The Embedded Rust Book](https://docs.rust-embedded.org/book/).

## Installation {#install}

### Download and install Rust

Run the following command to download and install Rust:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Start a new shell or run the following command to continue:

```bash
source "$HOME/.cargo/env"
```
To confirm the installation is complete, run the following (`cargo` is the Rust package manager):

```bash { env_source="~/.bashrc" }
rustc --version
cargo version
```

The output is similar to:
```output
rustc 1.78.0 (9b00956e5 2024-04-29)
cargo 1.78.0 (54d8815d0 2024-03-26)
```
### Add Arm cross-compilation support

Add cross compilation support for the required Arm Architectures. For example, to add support for Armv7-M architecture, you can use:
```command
rustup target add thumbv7m-none-eabi
```
For a full list of supported architectures, use:
```command
rustup target list
```

### Install cargo-generate

To generate a project from a template, you need `cargo-generate`. To install and rebuild use:

```command
sudo apt install -y libssl-dev pkg-config
sudo apt install -y build-essential
cargo install cargo-generate
```

### Install cargo-binutils (optional)

Other utilities are also available. For completeness, they can be installed with:
```command
cargo install cargo-binutils
rustup component add llvm-tools-preview
```

You are now ready to build an embedded application in Rust.
