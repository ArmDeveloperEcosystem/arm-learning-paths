---
title: Prepare wasmCloud on your Graviton server
description: Install wash and the Rust toolchain on an AWS Graviton server to prepare for building and running a WebAssembly component.
weight: 2
layout: learningpathall
---

## What wasmCloud is

wasmCloud is a cloud platform that you can use to host small, independently packaged
applications within a shared runtime. 

The applications are comprised of WebAssembly components. A WebAssembly component is a compiled application artifact, typically a `.wasm` file. A compatible host runs a component in a sandbox and provides the interfaces that it
needs. The component provides an HTTP request handler. wasmCloud provides the network listener and invokes the handler.

## What you'll build with wasmCloud

You'll build a small HTTP application from Rust source and run it on AWS Graviton with
wasmCloud. Then, you'll collect response time and throughput to measure how it responds to individual and concurrent requests.
The application returns a greeting. 

WebAssembly separates the component package from the host executable built
for a particular processor architecture. On Graviton, a Linux `aarch64` host
runs the component.


The flow of the application is as follows:

```text
HTTP client → wasmCloud HTTP listener → WebAssembly handler → HTTP response
```

## Check the server

Connect to your Ubuntu 24.04 Graviton-based instance using SSH. Run all Linux
commands on that server. The Learning Path was tested on a `c7g.2xlarge` instance with 8 vCPUs and 16 GiB of RAM, with at least 16 GiB of free disk space. Other Graviton-based instance sizes
work, and your measurements will be slightly different if you use a different size.

Check the architecture, available processors, and memory:

```bash
uname -m
nproc
free -h
```

Ensure that the architecture is `aarch64`. 

Record the processor information for your later measurements:

```bash
mkdir -p ~/wasmcloud-learning-path/results
lscpu > ~/wasmcloud-learning-path/results/cpu.txt
uname -a > ~/wasmcloud-learning-path/results/kernel.txt
```

Install the application build tools and HTTP test utilities:

```bash
sudo apt-get update
sudo apt-get install build-essential ca-certificates curl pkg-config wrk -y
```

## Install `wash`

Install and verify `wash`, and add `wash` to your PATH. For installation instructions, see the [wasmCloud install guide](/install-guides/wasmcloud/).

## Prepare the Rust application toolchain

Install Rust if it's
not already available. For installation instructions, see the [Rust install guide](/install-guides/rust/).

Then, load the Rust environment and install the pinned toolchain
and WebAssembly target:

```bash
source "$HOME/.cargo/env"
rustup target add wasm32-wasip2
```

The application targets WASI Preview 2, also called WASI 0.2 or P2. WASI defines
interfaces that a component can use to interact with its host, including HTTP.

## What you've accomplished and what's next

You've installed the `wash` CLI and the Rust toolchain with the WebAssembly
target. 

Next, you'll inspect the HTTP handler and build its component.
