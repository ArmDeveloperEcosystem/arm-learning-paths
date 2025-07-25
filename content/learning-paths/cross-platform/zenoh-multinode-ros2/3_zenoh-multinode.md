---
title: Containerize and deploy Zenoh across multiple Raspberry Pi devices

weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy Zenoh on multiple Raspberry Pi devices

After building Zenoh and its core examples, the next step is to deploy them across multiple Arm-based devices.

If you’ve already installed Zenoh on an Arm Cortex-A or Neoverse platform as shown in the previous section, you can copy the compiled binaries from `~/zenoh/target/release/` to each of your Raspberry Pi devices. 

To simplify and scale deployment across multiple devices, this section shows how to containerize Zenoh with Docker for streamlined distribution and consistent multi-node testing. This containerized approach enables repeatable rollouts and makes it easier to test distributed communication across Raspberry Pi, Arm cloud instances (like AWS Graviton), and Arm Virtual Hardware.

In this session, you’ll use Raspberry Pi boards to simulate a scalable distributed environment. The same workflow applies to any Arm Linux system, including cloud instances and virtual hardware. This setup allows you to simulate real-world, cross-node communication scenarios, making it ideal for evaluating Zenoh’s performance in robotics and industrial IoT applications. Zenoh is ideal for robotics and industrial IoT systems that require fast, decentralized communication. It supports scalable data exchange across devices using pub/sub, storage, and query models.

### Install Docker on Raspberry Pi
To simplify this process and ensure consistency, you can use Docker to containerize your Zenoh and ROS 2 environment. This lets you quickly replicate the same runtime on any device without needing to rebuild from source.

This enables scalable, multi-node testing in realistic distributed environments.

First, install Docker on each Raspberry Pi device:

```bash
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER ; newgrp docker
```

### Create a ROS 2 + Zenoh Docker image

To ensure compatibility with ROS-related tools, create a `Dockerfile` based on  `ros:galactic `, and use the official Rust installation method to build Zenoh, as shown below.

This Dockerfile uses a multi-stage build process based on the ros:galactic environment.
In the first stage, it installs Rust and compiles the Zenoh binaries directly from source. 
In the second stage, it installs essential ROS 2 demo tools and copies the Zenoh executables into the final runtime image.

```bash
# Stage 1: Build Zenoh using ROS base with Rust toolchain
FROM ros:galactic AS builder

RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    pkg-config \
    clang \
    libssl-dev \
    cmake

RUN curl -sSf https://sh.rustup.rs -o rustup-init.sh && \
    chmod +x rustup-init.sh && \
    ./rustup-init.sh -y --no-modify-path && \
    rm rustup-init.sh

ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /root
RUN git clone https://github.com/eclipse-zenoh/zenoh.git
WORKDIR /root/zenoh
RUN cargo build --release --all-targets -j $(nproc)

# Stage 2: Runtime with ROS + Zenoh binary only
FROM ros:galactic AS runtime

RUN apt-get update && apt-get install -y \
    ros-galactic-demo-nodes-cpp \
    ros-galactic-rmw-cyclonedds-cpp \
    ros-galactic-turtlesim

COPY --from=builder /root/zenoh/target/release /root/zenoh/target/release

ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

WORKDIR /root/zenoh/target/release

CMD ["/bin/bash"]
```

From the directory containing the above Dockerfile, run the following command to generate the docker image:


```bash
docker build -t zenoh-node .
```

After this has been done, the created ROS 2 Docker image can be seen by the following command.

```bash
docker images | grep zenoh-node
```

```output
REPOSITORY              TAG       IMAGE ID       CREATED          SIZE
zenoh-node              latest    2300ea78d043   30 minutes ago   3.73GB
```

Alternatively, if you’d like to skip the build process, a pre-built Docker image is available on Docker Hub.
You can pull it directly using:

```bash
docker pull odinlmshen/zenoh-node
```
{{% notice Tip %}}
Once built, you can reuse this Docker image across multiple Arm-based nodes, including Raspberry Pi, AWS Graviton, and Arm Virtual Hardware.
{{% /notice %}}

### Transfer the Docker image to the other Raspberry Pi

There are two options to transfer the Docker image to your second device. Choose one of the following methods.

Option 1: Save and copy via file 

```bash
docker save zenoh-node > zenoh-node.tar
scp zenoh-node.tar pi@<target_ip>:/home/pi/
```

On the target device:

```bash
docker load < zenoh-node.tar
```

Option 2: Push the image to a container registry such as Docker Hub

You can also push the image to Docker Hub or GitHub Container Registry and pull it on the second device.




### Run the Docker image

Once the image is successfully loaded on the second device, you can run the container to start the Zenoh environment.

```bash
docker run -it --network=host zenoh-node
```

The Zenoh example binaries are now available within this container, allowing you to test pub/sub and query flows across devices.

## Run Zenoh examples in a multi-node environment

With Zenoh running inside containers across devices, you’re now ready to explore real-time communication using prebuilt examples.

The following examples are written in Rust and precompiled in your container image. They're fully interoperable and can be used to demonstrate Zenoh's key capabilities across devices. The Rust binaries are available in the `$ZENOH_LOC/target/release/examples/` directory. If you haven't set `ZENOH_LOC`, they can be found under `~/zenoh/target/release/examples/`.
 

The following sections illustrate the procedures to run the Zenoh examples so as to demonstrate the primary capabilities of Zenoh:
- Basic pub/sub – for real-time message distribution  
- Query and storage – for persisting and retrieving historical data  
- Queryable – for enabling on-demand remote computation  
- Dynamic queryable with computation – for executing dynamic logic across nodes

