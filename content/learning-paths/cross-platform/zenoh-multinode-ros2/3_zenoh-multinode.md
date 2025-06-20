---
title: Setting Up a Multi-Node Environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploying Zenoh on Multiple Raspberry Pi Devices Using Docker

After building Zenoh and its core examples, your next step is to deploy them across multiple Arm-based devices. 

In this session, you’ll use Raspberry Pi boards to simulate a scalable, distributed environment—but the same workflow applies to any Arm Linux system, including Arm cloud instances and Arm Virtual Hardware.

You’ll learn how to use Docker to deploy the environment on physical devices, and how to duplicate virtual instances using snapshot cloning on Arm Virtual Hardware.

This setup lets you simulate `real-world`, `cross-node communication`, making it ideal for validating Zenoh’s performance in robotics and industrial IoT use cases.

### Install Docker on Raspberry Pi

To simplify this process and ensure consistency, you’ll use Docker to containerize your Zenoh and ROS 2 environment. 
This lets you quickly replicate the same runtime on any device without needing to rebuild from source.

This enables multi-node testing and real-world distributed communication scenarios.

First, install the docker environment on each of Raspberry Pi if you don't have that.

```bash
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi
```

Log out and back in, or run newgrp docker to activate Docker group permissions.

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
$ docker build -t zenoh-node .
```

After this has been done, the created ROS 2 docker image can be seen by the following command.

```bash
$ docker images | grep zenoh-node
```

```output
zenoh-node                           latest             b7a9c27cf8a8   About a minute ago   962MB
```

### Transfer the Docker Image on Another RPi

You now need to transfer the Docker image to your second device. Choose one of the following methods:

You have two options:

Option 1: Save and copy via file 

```bash
docker save zenoh-node > zenoh-node.tar
scp zenoh-node.tar pi@<target_ip>:/home/pi/
```

On the target device:
```bash
docker load < zenoh-node.tar
```

Option 2: Push to a container registry (e.g., DockerHub or GHCR).

You can also push the image to Docker Hub or GitHub Container Registry and pull it on the second device.

### Run the Docker Image

Once the image is successfully loaded into second device, you can run the container by

```bash
docker run -it --network=host zenoh-node
```

Now, all the Zenoh example binaries are now available within this container, allowing you to test pub/sub and query flows across devices.

### Another Duplicate Setting Option on Arm Virtual Hardware

If you have [Corellium](https://www.corellium.com/) account, you can 

1. Set up and install Zenoh on a single AVH instance.
2. Use the [Clone](https://support.corellium.com/features/snapshots) function to duplicate the environment.
3. Optionally, you may optionally rename the device to avh* for easy device recognition by changing the setting in the `/etc/hostname` file. 


With your multi-node environment in place, you’re now ready to run and test Zenoh communication flows across distributed edge devices.