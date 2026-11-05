---
title: Prepare wasmCloud on your Graviton server
description: Install wash and the Rust toolchain on an AWS Graviton server to prepare for building and running a WebAssembly component.
weight: 2
layout: learningpathall
---

## What you will build

Build a small HTTP application from Rust source, run it on AWS Graviton with
wasmCloud, and measure how it responds to individual and concurrent requests.
The application returns a greeting. Keeping its behavior simple makes it easier
to understand the boundary between application code and the runtime hosting it.

A WebAssembly component is a compiled application artifact, typically a `.wasm`
file. A compatible host executes it in a sandbox and provides the interfaces it
needs. The component provides an HTTP request handler, and
wasmCloud provides the network listener and invokes that handler.

```text
HTTP client → wasmCloud HTTP listener → WebAssembly handler → HTTP response
```

wasmCloud is useful when you want to host small, independently packaged
applications within a shared runtime. The host can provide capabilities such as
HTTP, configuration, and access to external services. WebAssembly also separates
the component's application packaging from the native host executable installed
for a particular processor architecture. The native Linux
Arm64 host on Graviton runs the component.

First you'll run one application, then collect response time and throughput
measurements to see how it responds under individual and concurrent load.

## Check the server

Connect to your Ubuntu 24.04 Graviton instance using SSH. Run the remaining Linux
commands on that server. A `c7g.2xlarge` instance with 8 vCPUs and 16 GiB of RAM
was used, with at least 16 GiB of free disk space. Other Graviton instance sizes
work; your measurements will be slightly different if you use a different size.

Check the architecture, available processors, and memory:

```bash
uname -m
nproc
free -h
```

The architecture must be `aarch64`. Record the processor information for your
later measurements:

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

Follow the [wasmCloud install guide](/install-guides/wasmcloud/) to install and
verify `wash`. The guide adds `wash` to your PATH automatically. Return here after
the verification step.

## Prepare the Rust application toolchain

Install Rust using the [Rust installation guide](/install-guides/rust/) if it is
not already available. Then load its environment and install the pinned toolchain
and WebAssembly target:

```bash
source "$HOME/.cargo/env"
rustup target add wasm32-wasip2
```

The application targets WASI Preview 2, also called WASI 0.2 or P2. WASI defines
interfaces a component can use to interact with its host, including HTTP.

## What you've accomplished

You have installed the `wash` CLI and the Rust toolchain with the WebAssembly
target. Next, inspect the HTTP handler and build its component.
