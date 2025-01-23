---
title: Building the hybrid-runtime and container image (optional)
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---
This section shows how you can build the hello world example on your Arm Linux host using a Docker container. Before getting started, you need to install Git, buildx and Docker on your Linux host. Follow the [Docker Engine install guide](/install-guides/docker/docker-engine/).

Install Git by running the following:
```bash
sudo apt install git
```

## Building the hybrid-runtime

Pull the hybrid runtime GitHub repository:
```bash
git clone https://github.com/smarter-project/hybrid-runtime.git
```
Navigate to the `hybrid-runtime/docker` directory and build the hybrid-runtime components:
```bash
cd hybrid-runtime/docker
make all
```
This builds the `hybrid-runtime` CLI and `containerd` `hybrid-shim`.

Navigate to the `hybrid_runtime/cortexm_console`  directory and build the application:
```bash
cd ../cortexm_console
docker buildx build --platform linux/arm64 -o output -f Dockerfile .
```

{{% notice Note %}}
You may have to be root to run Docker. Try adding `sudo` to the beginning of the Docker commands.
{{% /notice %}}

This builds the helper application, `cortexm_console`, that can capture output from a Cortex-M application. The binary is created in the directory.

By default, `containerd` will look in `/usr/local/bin` to find the hybrid-runtime components. Therefore, copy the hybrid-runtime components and the `cortexm_console` application into `/usr/local/bin` on the AVH model.

Copy the `containerd-shim-containerd-hybrid` to the board under `/usr/local/bin` using *SCP* and the IP address from before.

If you are using a VPN configured setup then you can use SCP directly. For example:
```bash
scp runtime/hybrid-shim/target/aarch64-unknown-linux-musl/debug/containerd-shim-containerd-hybrid root@10.11.0.1:/usr/local/bin/
scp cortexm_console/output/cortexm_console  root@10.11.0.1:/usr/local/bin/
```
Otherwise you can use the information from the **Quick Connect** section (substituting your particular -J argument). For example:
```bash
scp -J 95757722-1eb3-4e69-8cad-54f0400aa3d2@proxy.app.avh.arm.com runtime/hybrid-shim/target/aarch64-unknown-linux-musl/debug/containerd-shim-containerd-hybrid root@10.11.0.1:/usr/local/bin/
scp  -J 95757722-1eb3-4e69-8cad-54f0400aa3d2@proxy.app.avh.arm.com cortexm_console/output/cortexm_console  root@10.11.0.1:/usr/local/bin/
```

{{% notice Note %}}
You will need to edit the above commands to fit your IP address and paths.
{{% /notice %}}

## Building the hello-world firmware container image

Pull the runtime GitHub repository:
```bash
git clone https://github.com/smarter-project/hybrid-runtime.git
```
Then run the following:
```bash
cd hybrid-runtime/docker
make image
```
This should build a docker image with the name `ghcr.io/smarter-project/hybrid-runtime/hello_world_imx8mp:latest`.

The `image.dockerfile` file pulls the NXP SDK and builds the hello world example present in the NXP SDK. Finally, the Dockerfile creates a new image, copies the hello world binary into it, sets the entrypoint and adds the correct labels. You can use this Dockerfile to run the example as shown in the section [Deploy firmware container using containerd](/learning-paths/embedded-and-microcontrollers/cloud-native-deployment-on-hybrid-edge-systems/containerd/).
