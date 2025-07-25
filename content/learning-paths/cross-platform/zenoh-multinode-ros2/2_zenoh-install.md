---
title: Install and build Zenoh on Arm devices

weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up Zenoh on Arm devices


The following instructions have been verified on both Raspberry Pi 4 and 5 devices, but you can implement them on any Arm Linux device. These steps show how to install Zenoh on Raspberry Pi and other Arm-based Linux platforms.

Before building Zenoh, make sure your system has the necessary development tools and runtime libraries.

### Install the Rust development environment

First, install the [Rust](https://www.rust-lang.org/) environment, since the core of Zenoh is developed using Rust to keep it safe and efficient.

```bash
sudo apt update
sudo apt install -y curl gcc
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
```

Near the end of the installation you will see the success message:

```output
Rust is installed now. Great!
```

Make sure to source the environment to add Rust to your shell environment:

```bash
source "$HOME/.cargo/env"
```

You can learn more using the [Rust install guide](/install-guides/rust/) for Arm Linux.

### Install ROS 2

[Robot Operating System](https://www.ros.org/) is a set of software libraries and tools that help you build robot applications. ROS provides everything from drivers to state-of-the-art algorithms, as well as developer tools. It is completely open-source.

If your use case involves ROS 2 integration, you should install ROS 2 before proceeding with Zenoh-related development. Follow the [ROS2 installation guide](/install-guides/ros2/) to install ROS 2 on your Arm platforms.

### Download and build the Zenoh source

Clone the Zenoh repository:

```bash
cd $HOME
git clone https://github.com/eclipse-zenoh/zenoh.git
```

After cloning, use cargo to build the source:

```bash
cd zenoh
cargo build --release --all-targets -j $(nproc)
```

This process will take several minutes depending on your device. Once the installation is complete, you should see:

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

After the build process, the binary executables will be stored under the directory of `~/zenoh/target/release/examples/`.

{{% notice Note %}}
Installation time can vary depending on your device’s performance.
{{% /notice %}}

If you get a build error:
```output
error[E0599]: no function or associated item named `start` found for struct `StoragesPlugin` in the current scope
   --> plugins/zenoh-plugin-storage-manager/tests/operations.rs:91:55
```

Edit the file `./plugins/zenoh-plugin-storage-manager/tests/operations.rs` and comment the line shown below and add the second line to the file:

```rust
//use zenoh_plugin_trait::Plugin;
use crate::path::to::Plugin;
```

Run the build again:

```bash
cargo clean && cargo build
```

With Zenoh successfully compiled, you’re ready to explore how nodes communicate using the Zenoh runtime.
