---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Sysbox

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- cloud
- vm
- virtual machine
- linux
- containers
- container
- docker

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

author: Jason Andrews

### Link to official documentation
official_docs: https://github.com/nestybox/sysbox/blob/master/docs/user-guide/README.md

test_images:
- ubuntu:latest
test_maintenance: true

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Sysbox](https://github.com/nestybox/sysbox/blob/master/README.md) allows you to use Docker containers for workloads that typically require virtual machines (VMs). Containers run with Sysbox are able to run software that relies on the [systemd System and Service Manager](https://systemd.io/) that is not usually present in containers, and it does this without the need for a full virtual machine and hardware emulation.

Running Docker inside Docker, and Kubernetes inside Docker, are also Sysbox use cases. Without Sysbox, these are difficult because the Docker daemon requires systemd.

In summary, Sysbox is a powerful container runtime that provides many of the benefits of virtual machines without the overhead of running a full VM. It is good for workloads that require the ability to run system-level software.

Sysbox runs on Linux and supports Arm.

## Before you begin

Sysbox has limited support for older versions of Linux, but recent Linux versions are easily compatible. To check whether your Linux distribution and Linux kernel version are supported, see [Sysbox Distro Compatibility](https://github.com/nestybox/sysbox/blob/master/docs/distro-compat.md).

Sysbox is a container runtime, so Docker is required before installing Sysbox.

In most cases, you can install Docker on Arm Linux with the commands:

```bash
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER ; newgrp docker
```

For more information, see the [Docker install guide](/install-guides/docker/docker-engine/).

You can use Sysbox on a virtual machine from a [cloud service provider](/learning-paths/servers-and-cloud-computing/intro/find-hardware/), a Raspberry Pi 5, or any other Arm Linux-based computer.

## Install Sysbox

Download the Sysbox official package from [Sysbox Releases](https://github.com/nestybox/sysbox/releases/).

You can download the Debian package for Arm from the command line:

{{% notice Note %}}
The following commands use Sysbox version 0.6.7. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Sysbox releases](https://github.com/nestybox/sysbox/releases/).
{{% /notice %}}

```bash
wget https://github.com/nestybox/sysbox/releases/download/v0.6.7/sysbox-ce_0.6.7.linux_arm64.deb
```

Install the package using the `apt` command:

```bash
sudo apt-get install ./sysbox-ce_0.6.7.linux_arm64.deb -y
```

If you are not using a Debian-based Linux distribution, you can use instructions to build Sysbox from the source code. For more information, see [Sysbox Developer's Guide: Building & Installing](https://github.com/nestybox/sysbox/blob/master/docs/developers-guide/build.md).

Run `systemctl` to confirm if Sysbox is running:

```bash
systemctl list-units -t service --all | grep sysbox
```

If Sysbox is running, you see the output:

```output
  sysbox-fs.service                              loaded    active   running sysbox-fs (part of the Sysbox container runtime)
  sysbox-mgr.service                             loaded    active   running sysbox-mgr (part of the Sysbox container runtime)
  sysbox.service                                 loaded    active   running Sysbox container runtime
```

## Verify Sysbox installation

You can test Sysbox by creating a container image that includes systemd and Docker.

Use a text editor to copy the following text to a file named `Dockerfile`:

```console {file_name="Dockerfile"}
FROM ubuntu:24.04

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update && \
      apt-get -y install sudo curl net-tools openssh-server

ENV USER=ubuntu

RUN echo "$USER:ubuntu" | chpasswd && adduser $USER sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Install Docker
RUN curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
RUN sudo usermod -aG docker $USER

EXPOSE 22

ENTRYPOINT [ "/sbin/init", "--log-level=err" ]
```

Notice that Docker and the SSH server are installed, and port 22 is open for SSH connections.

Build a container image using `docker`:

```bash
docker build -t sysbox-test -f Dockerfile .
```

Use Sysbox as the container runtime to create a new container:

```console
docker run --runtime=sysbox-runc -P --hostname=sbox -it sysbox-test
```

The following animated output shows the Linux init process running. You can log in with the password `ubuntu`, or change it in the Dockerfile.

You can use Docker inside the container. The SSH server operates as expected. Both are possible because systemd is running in the container.

![Animated terminal showing systemd init process starting in the Sysbox container, followed by a login prompt where you can enter the ubuntu user credentials to verify the container is running with full system services.#center](/install-guides/_images/sysbox.gif)

## Use SSH to connect to a Sysbox container

To connect using SSH, you can identify the IP address of your Sysbox container in two ways: from inside the container, or from outside the container.

To find the IP address from inside the container, use the `ifconfig` command:

```console
ifconfig
```

The output is similar to:

```output
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.20.0.2  netmask 255.255.0.0  broadcast 172.20.255.255
        ether 02:42:ac:14:00:02  txqueuelen 0  (Ethernet)
        RX packets 126  bytes 215723 (215.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 115  bytes 7751 (7.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

The `inet` IP address for `eth0` is the one you can use to SSH from outside the Sysbox container.

For this example, the SSH command is the following. Replace the IP address with that of your container.

```console
ssh ubuntu@172.20.0.2
```

Log in using the same `ubuntu` username and password.

You can also use the `docker` command to identify the IP address and port from outside the container.

Run the following command from another shell outside of the Sysbox container:

```bash
docker ps
```

The output is similar to:

```output
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS                                       NAMES
3a42487cddc0   sysbox-test   "/sbin/init --log-le…"   10 minutes ago   Up 10 minutes   0.0.0.0:32768->22/tcp, [::]:32768->22/tcp   determined_hopper
```

Look in the `PORTS` column for the port number that is connected to port 22 of the container. In this example, it is 32768. You can use `localhost`, `0.0.0.0` or the actual IP of your machine with the identified port.

SSH to the container using the connected port:

```console
ssh ubuntu@localhost -p 32768
```

Log in using the same `ubuntu` username and password.

You can exit the Sysbox container using:

```console
sudo halt
```

Sysbox behaves like a virtual machine that you can use to run applications that require system services normally not available in containers. It is useful for testing and development tasks because the container changes are not saved, meaning that you can create a clean testing environment simply by restarting the Sysbox container.

You're now ready to use Sysbox.