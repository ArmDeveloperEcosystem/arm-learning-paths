---
title: Building the hybrid-runtime and container image
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Building the hybrid-runtime

On your Linux host, pull the hybrid runtime GitHub repository:
```console
git clone git@github.com:smarter-project/hybrid-runtime.git
```
Navigate to the `hybrid-runtime/docker` directory and build the hybrid-runtime components:
```console
make all
```
This builds the hybrid-runtime CLI and containerd hybrid-shim. 

Navigate to the `hybrid_runtime/cortexm_console`  directory and build the application:
```console
docker buildx build --platform linux/arm64 -o output -f Dockerfile .
```
This builds the helper application, cortexm_console, that can capture output from a cortex-m application. The binary is created in the directory.

By default containerd will look in `/usr/local/bin` to find the hybrid runtime components and so we copy the hybrid runtime components and the cortexm_console application into `/usr/local/bin` on the AVH model.

Copy the `containerd-shim-containerd-hybrid` to the board under `/usr/local/bin` using *scp*.

If you are using a VPN configured setup then you can use scp directly. For example: 
```console
scp runtime/hybrid-shim/target/aarch64-unknown-linux-musl/debug/containerd-shim-containerd-hybrid root@10.11.0.1:/usr/local/bin/
scp cortexm_console/output/cortexm_console  root@10.11.0.1:/usr/local/bin/
```
Otherwise you can use the information from the “Quick connect” section (substituting your particular -J argument). For example:
```console
scp -J 95757722-1eb3-4e69-8cad-54f0400aa3d2@proxy.app.avh.arm.com runtime/hybrid-shim/target/aarch64-unknown-linux-musl/debug/containerd-shim-containerd-hybrid root@10.11.0.1:/usr/local/bin/
scp  -J 95757722-1eb3-4e69-8cad-54f0400aa3d2@proxy.app.avh.arm.com cortexm_console/output/cortexm_console  root@10.11.0.1:/usr/local/bin/
```

## Building the hello-world firmware container image

Pull the runtime GitHub repository.
```console
git clone https://github.com/smarter-project/hybrid-runtime.git
```
In the `hybrid-runtime/docker` directory run:
```console
make image
```
This should build a docker image with the name: `ghcr.io/smarter-project/hybrid-runtime/hello_world_imx8mp:latest`

The `image.dockerfile` file pulls the NXP SDK and builds the hello world example present in the NXP SDK.  The final step is to create a new image, copy the hello world binary into it, set the entrypoint and finally add the correct labels.

## Summary

The hybrid-runtime allows deploying and running workloads on hybrid systems, boards with an SoC containing a Cortex-A plus a Cortex-M/R using cloud tools such as k3s and containerd.

For more information on the hybrid runtime https://github.com/smarter-project/hybrid-runtime.