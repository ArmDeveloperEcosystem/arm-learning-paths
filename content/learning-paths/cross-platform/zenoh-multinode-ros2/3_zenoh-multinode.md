---
title: Setting Up a Multi-Node Environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploying Zenoh on Multiple Raspberry Pi Devices Using Docker

After building Zenoh and its core examples, your next step is to deploy them across multiple Arm-based devices. 

In this section, you’ll use Raspberry Pi boards to simulate a scalable, distributed environment, but the same workflow applies to any Arm Linux system, including Arm cloud instances.

You’ll learn how to use Docker to deploy the environment on physical devices.

This setup lets you simulate real-world, cross-node communication, making it ideal for validating Zenoh's performance in robotics and industrial IoT use cases.

### Install Docker 

To simplify this process and ensure consistency, you can use Docker to containerize your Zenoh and ROS 2 environment. 
This lets you quickly replicate the same runtime on any device without needing to rebuild from source.

This enables multi-node testing and real-world distributed communication scenarios.

First, install Docker on each of Raspberry Pi.

```bash
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER ; newgrp docker
```

### Create a ROS 2 + DDS Docker Image

In a working directory, create a `Dockerfile` with the following content to create the ROS 2 / DDS docker image.

```bash
FROM ros:galactic
RUN apt-get update 
RUN apt-get install -y ros-galactic-demo-nodes-cpp ros-galactic-rmw-cyclonedds-cpp ros-galactic-turtlesim
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
CMD bash
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
zenoh-node                           latest             b7a9c27cf8a8   About a minute ago   962MB
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
