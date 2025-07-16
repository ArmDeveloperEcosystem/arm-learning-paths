---
title: Setting Up a Multi-Node Environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploying Zenoh on Multiple Raspberry Pi Devices

After building Zenoh and its core examples, your next step is to deploy them across multiple Arm-based devices. 

Once you’ve successfully installed Zenoh on an Arm Cortex-A or Neoverse platform in the previous session, you can either transfer the compiled binaries from `~/zenoh/target/release/` to your Raspberry Pi devices, or use Docker to quickly deploy them across multiple RPi nodes.

In this session, you’ll use Raspberry Pi boards to simulate a scalable, distributed environment—but the same workflow applies to any Arm Linux system, including Arm cloud instances and Arm Virtual Hardware.

This setup lets you simulate real-world, cross-node communication, making it ideal for validating Zenoh's performance in robotics and industrial IoT use cases.

### Install Docker on Raspberry Pi
To simplify this process and ensure consistency, you can use Docker to containerize your Zenoh and ROS 2 environment. 
This lets you quickly replicate the same runtime on any device without needing to rebuild from source.

This enables multi-node testing and real-world distributed communication scenarios.

First, install Docker on each of Raspberry Pi.

```bash
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER ; newgrp docker
```

### Create a ROS2 + Zenoh Docker Image

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

Under the directory where the above Dockerfile exists, run the following command to generate the docker image.

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

### Run the Docker Image

Once the image is successfully loaded on second device, you can run the container.

```bash
docker run -it --network=host zenoh-node
```

The Zenoh example binaries are now available within this container, allowing you to test pub/sub and query flows across devices.

## Run Zenoh in Multi-Node Environment

You’re now ready to run and test Zenoh communication flows across distributed edge devices.

The source of the examples written in Rust will be provided, and both are interoperable.  The 
Rust binaries are already available under: `$ZENOH_LOC/target/release/examples/` directory. 

The following sections illustrate the procedures to run the Zenoh examples so as to demonstrate the primary capabilities of Zenoh
1. Basic Pub/Sub – for real-time message distribution
2. Query and Storage – to persist and retrieving historical data
3. Queryable – to enable on-demand remote computation
4. Dynamic Queryable with Computation
