---
title: Install Rust
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Rust Installation on GCP SUSE VM
This guide explains how to install and configure Rust on a GCP SUSE Arm64 VM, ensuring the environment is ready for building and benchmarking Rust applications.

### System Preparation
Updates the system and installs essential build tools for compiling Rust programs.

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y curl gcc make
```
### Install Rust Using rustup
Rust provides an official installer script via `rustup`, which handles the setup automatically:

```console
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
When prompted, you can choose **option 1** (default installation).

### Configure Rust Environment
Activates Rust’s environment variables for the current shell session.

```console
source $HOME/.cargo/env
```

### Verify Rust Installation
Confirms successful installation of Rust and Cargo by checking their versions.

```console
rustc --version
cargo --version
```

You should see an output similar to:
```output
rustc 1.91.0 (f8297e351 2025-10-28)
cargo 1.91.0 (ea2d97820 2025-10-10)
```
Rust installation is complete. You can now go ahead with the baseline testing of Rust in the next section.
