---
title: Get started with Zenoh on Raspberry Pi and Arm Linux

weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up Zenoh on Arm devices

This section shows you how to install and build the open-source Eclipse Zenoh protocol on Arm-based devices like Raspberry Pi.

The following instructions have been verified on Raspberry Pi 4 and 5, but you can use any Arm Linux device. These steps apply to Raspberry Pi and other Arm-based Linux platforms. Before building Zenoh, make sure your system has the necessary development tools and runtime libraries.

## Install the Rust development environment

First, install the [Rust](https://www.rust-lang.org/) environment. The core of Zenoh is developed in Rust for performance and safety. 

```bash
sudo apt update
sudo apt install -y curl gcc
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
```

Near the end of the installation, you should see the message:

```output
Rust is installed now. Great!
```
Source your shell environment to activate Rust:

```bash
source "$HOME/.cargo/env"
```

For more information, see the [Rust Install Guide](/install-guides/rust/) for Arm Linux.

## Install ROS 2

[Robot Operating System](https://www.ros.org/) is a set of software libraries and tools that help you build robot applications. ROS provides everything from drivers to state-of-the-art algorithms, as well as developer tools. It is completely open-source.

If you plan to use Zenoh alongside ROS 2, for example, to bridge DDS-based nodes, you should install ROS 2 before proceeding. See the [ROS2 Installation Guide](/install-guides/ros2/) to install ROS 2 on your Arm platforms.

## Download and build the Zenoh source

Clone the Zenoh repository:

```bash
cd $HOME
git clone https://github.com/eclipse-zenoh/zenoh.git
```
Build the source using Cargo:

```bash
cd zenoh
cargo build --release --all-targets -j $(nproc)
```
This process will take several minutes depending on your device. When complete, you should see output like:

```output
    Updating crates.io index
  Downloaded humantime v2.2.0
  Downloaded spin v0.10.0
  Downloaded crossbeam-channel v0.5.14
  Downloaded uhlc v0.8.1
  Downloaded 4 crates (182.5 KB) in 2.19s
warning: output filename collision.
The lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.4.0 (/home/ubuntu/zenoh/plugins/zenoh-plugin-storage-manager)` has the same output filename as the lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.4.0 (/home/ubuntu/zenoh/plugins/zenoh-plugin-storage-manager)`.
Colliding filename is: /home/ubuntu/zenoh/target/release/deps/libzenoh_plugin_storage_manager.so
The targets should have unique names.
Consider changing their names to be unique or compiling them separately.
This may become a hard error in the future; see <https://github.com/rust-lang/cargo/issues/6313>.
warning: output filename collision.
The lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.4.0 (/home/ubuntu/zenoh/plugins/zenoh-plugin-storage-manager)` has the same output filename as the lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.4.0 (/home/ubuntu/zenoh/plugins/zenoh-plugin-storage-manager)`.
Colliding filename is: /home/ubuntu/zenoh/target/release/deps/libzenoh_plugin_storage_manager.so.dwp
The targets should have unique names.
Consider changing their names to be unique or compiling them separately.
This may become a hard error in the future; see <https://github.com/rust-lang/cargo/issues/6313>.
warning: output filename collision.
The lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.4.0 (/home/ubuntu/zenoh/plugins/zenoh-plugin-storage-manager)` has the same output filename as the lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.4.0 (/home/ubuntu/zenoh/plugins/zenoh-plugin-storage-manager)`.
Colliding filename is: /home/ubuntu/zenoh/target/release/deps/libzenoh_plugin_storage_manager.rlib
The targets should have unique names.
Consider changing their names to be unique or compiling them separately.
This may become a hard error in the future; see <https://github.com/rust-lang/cargo/issues/6313>.
   Compiling proc-macro2 v1.0.86
   Compiling unicode-ident v1.0.13
   Compiling libc v0.2.158
   Compiling version_check v0.9.5
   Compiling autocfg v1.3.0
...
   Compiling zenoh-link-quic v1.4.0 (/home/ubuntu/zenoh/io/zenoh-links/zenoh-link-quic)
   Compiling zenoh_backend_traits v1.4.0 (/home/ubuntu/zenoh/plugins/zenoh-backend-traits)
   Compiling zenoh-plugin-storage-manager v1.4.0 (/home/ubuntu/zenoh/plugins/zenoh-plugin-storage-manager)
   Compiling zenoh-ext v1.4.0 (/home/ubuntu/zenoh/zenoh-ext)
   Compiling zenoh-ext-examples v1.4.0 (/home/ubuntu/zenoh/zenoh-ext/examples)
   Compiling zenoh-plugin-example v1.4.0 (/home/ubuntu/zenoh/plugins/zenoh-plugin-example)
   Compiling zenoh-backend-example v1.4.0 (/home/ubuntu/zenoh/plugins/zenoh-backend-example)
    Finished `release` profile [optimized] target(s) in 6m 28s
```

After the build process, the binary executables will be located at `~/zenoh/target/release/examples/`.

{{% notice Note %}}
Installation time can vary depending on your device’s performance.
{{% /notice %}}


## Troubleshooting build errors

If you get a build error like this:
```output
error[E0599]: no function or associated item named `start` found for struct `StoragesPlugin` in the current scope
   --> plugins/zenoh-plugin-storage-manager/tests/operations.rs:91:55
```

Edit the file `./plugins/zenoh-plugin-storage-manager/tests/operations.rs` and comment the line shown below and add the second line to the file:

```rust
//use zenoh_plugin_trait::Plugin;
use crate::path::to::Plugin;
```

Then rebuild:

```bash
cargo clean && cargo build
```

With Zenoh successfully compiled, you’re ready to explore how nodes communicate using the Zenoh runtime.
