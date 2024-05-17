---
# User change
title: Install tools and build an example

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Install Arm Development Studio

Follow the instructions from the [Arm Development Studio Install Guide](/install-guides/armds).

Arm Development Studio provides Fixed Virtual Platform (`FVP`) to execute example code on, as well as the Arm Debugger.

Note that Arm Development Studio is license managed.

## Install Rust compiler

Follow the instructions from the [Rust for Embedded Applications Install Guide](/install-guides/rust_embedded) to install the Rust compiler `rustc` and cross compilation support for the Arm architecture of choice.

In this example we will use `Armv7-M` (such as for `Cortex-M3`).

```command
rustup target add thumbv7m-none-eabi
```

## Create example project

Rust projects (known as `crates`) need to be created before you can begin.

An example template is available (courtesy of [The Embedded Rust Book](https://docs.rust-embedded.org/book/start/qemu.html)) that can be used to generate a crate:
```command
cargo generate --git https://github.com/rust-embedded/cortex-m-quickstart
```
You will be prompted to provide a `Project Name`, which will create a directory of that name with the crate content therein.
``` output
Project Name: rust-example
```
Navigate into that folder.
```command
cd rust-example
```

It is possible to create a simple single-file Rust application, within the `Examples` folder of the crate.

Using your preferred text editor, create the below `armds.rs`.
```command
nano examples/armds.rs
```
#### armds.rs
```rust
#![no_main]
#![no_std]

use panic_halt as _;
use cortex_m_rt::entry;
use cortex_m_semihosting::{debug, hprintln};

#[entry]
fn main() -> ! {

   let mut sum = 0;

   for n in 1..101 {
      sum += n;
      hprintln!("Total sum to {} is {}", n, sum).unwrap();

      let calc = (n*(n+1))/2;
      hprintln!("Calculated sum is {}\n", calc).unwrap();
   }

   // Semihosting exit
   debug::exit(debug::EXIT_SUCCESS);
   // Function never returns
   loop{};
}
```
The crate includes a default `memory.x` file that matches the memory map of the FVP, so no additional changes are needed.

## Build the example
Use `cargo` to build the example application.

{{% notice Build application %}}
The application name is the same as the source file, ignoring the `.rs` file type.
{{% /notice %}}

```command
cargo build --example armds
```
The project will build, and include appropriate libraries. You will see output similar to:
```output
...
   Compiling cortex-m v0.6.7
   Compiling cortex-m-semihosting v0.3.7
   Compiling rust-example v0.1.0 (/home/ubuntu/rust-example)
   Compiling panic-halt v0.2.0
   Compiling cortex-m-rt-macros v0.6.15
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 9.86s
```
The executable will be located in the `target/thumbv7m-none-eabi/debug/examples` folder.
