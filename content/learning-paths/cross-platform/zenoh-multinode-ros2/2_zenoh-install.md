---
title: Setting Up Zenoh on Arm Devices
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Installation: Setting Up Zenoh on Arm Devices

The following instructions are verified on both Raspberry Pi 4/5 and Arm Virtual Hardware, but you can implement them on any Cortex-A Linux device.

Before building Zenoh, make sure your system has the necessary development tools and runtime libraries.

#### Install the Rust build environment

First, we need to install the [Rust](https://www.rust-lang.org/) build environment, since the core of Zenoh is totally developed using Rust to keep it safe and efficient. 

Follow this [installation guide](https://learn.arm.com/install-guides/rust/) to install Rust and Cargo on Arm Linux, a build system for Rust. Or, simply use the following commands.

```bash
curl https://sh.rustup.rs -sSf | sh
```

Follow the prompts to complete the installation. If successful, you’ll see:

```output
Rust is installed now. Great!
```

For more details, refer to [Rust’s official install guide.](https://doc.rust-lang.org/cargo/getting-started/installation.html#install-rust-and-cargo)

#### Install ROS 2

[Robot Operating System](https://www.ros.org/) is a set of software libraries and tools that help you build robot applications. From drivers to state-of-the-art algorithms, and with powerful developer tools, ROS has what you need for your next robotics project. And it's all open source.

Since ROS was started in 2007, a lot has changed in the robotics and ROS community. The goal of the [ROS 2](https://docs.ros.org/en/rolling/index.html) project is to adapt to these changes, leveraging what is great about ROS 1 and improving what isn’t.

Here is the quick [installation guide](https://learn.arm.com/install-guides/ros2/) about how to install ROS 2 in Arm platform.


## Download and build the Zenoh source

Now, we can clone the Zenoh.

```bash
cd ~
git clone https://github.com/eclipse-zenoh/zenoh.git
```

After that, simply use cargo to build the source.

```bash
cd zenoh
cargo build --release --all-targets -j $(nproc)
```

This will take several minutes depending on your device. Once the installation is complete, you should see:

```output
cargo build --release --all-targets -j $(nproc)
warning: output filename collision.
The lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-plugin-storage-manager)` has the same output filename as the lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-plugin-storage-manager)`.
Colliding filename is: /home/ubuntu/zenoh/zenoh/target/release/deps/libzenoh_plugin_storage_manager.so
The targets should have unique names.
Consider changing their names to be unique or compiling them separately.
This may become a hard error in the future; see <https://github.com/rust-lang/cargo/issues/6313>.
warning: output filename collision.
The lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-plugin-storage-manager)` has the same output filename as the lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-plugin-storage-manager)`.
Colliding filename is: /home/ubuntu/zenoh/zenoh/target/release/deps/libzenoh_plugin_storage_manager.so.dwp
The targets should have unique names.
Consider changing their names to be unique or compiling them separately.
This may become a hard error in the future; see <https://github.com/rust-lang/cargo/issues/6313>.
warning: output filename collision.
The lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-plugin-storage-manager)` has the same output filename as the lib target `zenoh_plugin_storage_manager` in package `zenoh-plugin-storage-manager v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-plugin-storage-manager)`.
Colliding filename is: /home/ubuntu/zenoh/zenoh/target/release/deps/libzenoh_plugin_storage_manager.rlib
The targets should have unique names.
Consider changing their names to be unique or compiling them separately.
This may become a hard error in the future; see <https://github.com/rust-lang/cargo/issues/6313>.
   Compiling zenoh-plugin-storage-manager v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-plugin-storage-manager)
   Compiling zenoh-ext-examples v1.3.0 (/home/ubuntu/zenoh/zenoh/zenoh-ext/examples)
   Compiling zenoh-plugin-rest v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-plugin-rest)
   Compiling zenohd v1.3.0 (/home/ubuntu/zenoh/zenoh/zenohd)
   Compiling zenoh-backend-example v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-backend-example)
   Compiling zenoh-examples v1.3.0 (/home/ubuntu/zenoh/zenoh/examples)
   Compiling zenoh-ext v1.3.0 (/home/ubuntu/zenoh/zenoh/zenoh-ext)
   Compiling zenoh_backend_traits v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-backend-traits)
   Compiling zenoh-plugin-example v1.3.0 (/home/ubuntu/zenoh/zenoh/plugins/zenoh-plugin-example)
   Compiling zenoh v1.3.0 (/home/ubuntu/zenoh/zenoh/zenoh)
    Finished `release` profile [optimized] target(s) in 8m 12/home/ubuntu/zenoh/zenoh/plugins/zenoh-backend-examples
```

After the build process, the binary executables will be stored under the directory of `~/zenoh/target/release/examples/`.

{{% notice Note %}}
Installation time may vary depending on your device’s processing power.
{{% /notice %}}

