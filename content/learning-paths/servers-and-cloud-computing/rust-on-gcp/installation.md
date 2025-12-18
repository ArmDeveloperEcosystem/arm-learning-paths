---
title: Install Rust
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This section explains how to install and configure Rust on your GCP SUSE Arm64 VM, preparing your environment for building and benchmarking Rust applications.

## Update your system

Update the system and install essential build tools required for compiling Rust programs:

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y curl gcc make
```

This ensures your system has the latest packages and the necessary compilation tools.

## Install Rust using rustup

Rust provides an official installer script via `rustup` that handles the setup automatically:

```console
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

When prompted, select option 1 for the default installation. This installs the latest stable version of Rust along with Cargo, Rust's package manager and build system.

## Configure your environment

Activate Rust's environment variables for your current shell session:

```console
source $HOME/.cargo/env
```

This command adds the Rust toolchain to your PATH, making the `rustc` compiler and `cargo` commands available.

## Verify the installation

Confirm that Rust and Cargo installed successfully by checking their versions:

```console
rustc --version
cargo --version
```

The output is similar to:

```output
rustc 1.91.0 (f8297e351 2025-10-28)
cargo 1.91.0 (ea2d97820 2025-10-10)
```

Your Rust installation is now complete and ready for development on your Arm64 instance.