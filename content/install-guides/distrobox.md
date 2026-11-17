---
title: Distrobox
description: Install Distrobox on Arm Linux or a ChromeOS or Googlebook OS device and run an Ubuntu 26.04 container that integrates with your home directory.

draft: true

additional_search_terms:
- distrobox
- container
- Podman
- Ubuntu
- Chromebook
- Googlebook
- Crostini
- Linux

minutes_to_complete: 15

author: Jason Andrews

official_docs: https://distrobox.it/

test_images:
- ubuntu:latest
test_maintenance: false

weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Distrobox](https://distrobox.it/) lets you run any Linux distribution inside a container while sharing your home directory with the host. It uses Podman or Docker underneath, so you can create a container, enter it like a normal shell, install packages with the native package manager, and remove it when you're done. Your files stay on the host, which makes containers safe to experiment with and quick to throw away.

Distrobox is useful on Arm systems when you want a different distribution than your host or a clean build environment for testing.

You'll learn how to install Distrobox and run an Ubuntu container on Arm Linux or a ChromeOS or Googlebook OS device.

Everything in this guide targets the `aarch64` (64-bit Arm) architecture. Your device needs an Arm CPU, and the containers you create run `arm64` software.

## Before you begin

Make sure you're using a system running Arm Linux. You can use a physical Arm device, an Arm-based virtual machine, or the Linux development environment on a ChromeOS or Googlebook OS device.

To confirm the architecture, run:

```bash
uname -m
```

The output should be `aarch64` for 64-bit Arm systems.

Distrobox needs a container engine. This guide uses Podman because it runs containers without root privileges, which suits both Arm Linux and the ChromeOS and Googlebook OS Linux environment.

{{% notice Note %}}
On a ChromeOS or Googlebook OS device, set up the Linux development environment first. On ChromeOS, open **Settings**, go to **About ChromeOS**, select **Developers**, and turn on **Linux development environment**. On Googlebook OS, open the **Terminal** app from the app drawer and follow the prompts to initialize the Linux environment. This creates a managed Debian environment where you install and run Distrobox, and it already provides the user namespace and `subuid` and `subgid` configuration that rootless Podman needs.
{{% /notice %}}

## Install Distrobox on Arm Linux

The following steps use a Debian-based distribution, such as Ubuntu or the Debian environment on a ChromeOS or Googlebook OS device. Install Podman, Distrobox, and the `uidmap` package for rootless containers:

```bash
sudo apt update
sudo apt install -y podman distrobox uidmap curl
```

Confirm the tools are installed:

```bash
distrobox version
podman --version
```

The output is similar to:

```output
distrobox: 1.8.1.2
podman version 5.4.2
```

Check that Podman can run containers without root privileges:

```bash
podman info --format '{{.Host.Security.Rootless}}'
```

The expected output is:

```output
true
```

A `true` result confirms rootless mode is working, so you can create and enter containers as your normal user.

## Create an Ubuntu 26.04 container

Create a container named `ubuntu26` from the official Ubuntu 26.04 image. Podman automatically pulls the `arm64` variant of the image for your Arm CPU:

```bash
distrobox create --name ubuntu26 --image docker.io/library/ubuntu:26.04 --yes
```

The output is similar to:

```output
Trying to pull docker.io/library/ubuntu:26.04...
Creating 'ubuntu26' using image docker.io/library/ubuntu:26.04	 [ OK ]
Distrobox 'ubuntu26' successfully created.
To enter, run:

distrobox enter ubuntu26
```

## Enter the container

The first time you enter a container, Distrobox sets up your user, sudo access, and the shared home directory. This takes a moment. Later entries are fast.

Enter the container:

```bash
distrobox enter ubuntu26
```

When setup finishes, your shell prompt changes to show you're inside the container. Confirm the distribution and architecture:

```bash
grep PRETTY_NAME /etc/os-release
uname -m
```

The output is similar to:

```output
PRETTY_NAME="Ubuntu 26.04.1 LTS"
aarch64
```

You're now in an Ubuntu 26.04 environment on Arm. Your home directory is shared with the host, so files you create are visible in both places. Confirm this by listing your home directory:

```bash
ls $HOME
```

You'll see the same files and directories as on your host. Install packages with `apt` as you would on any Ubuntu system:

```bash
sudo apt update
sudo apt install -y htop
```

{{% notice Note %}}
Any software you install inside the container must have an `arm64` build. Most packages in the Ubuntu repositories provide one, so `apt` installs work as expected on your Arm device.
{{% /notice %}}

## Exit the container

To leave the container and return to your host shell, type `exit` or press `Ctrl+D`:

```bash
exit
```

The container keeps running in the background after you exit, so you can enter it again without waiting for setup.

## Run a command without entering the container

To run a single command inside the container from your host, pass it after `--`:

```bash
distrobox enter ubuntu26 -- uname -m
```

The output is similar to:

```output
aarch64
```

## List your containers

To see the containers you've created and their status, run:

```bash
distrobox list
```

The output is similar to:

```output
ID           | NAME                 | STATUS             | IMAGE
56452187200e | ubuntu26             | Up 23 minutes      | docker.io/library/ubuntu:26.04
```

## Stop a container

To stop a running container without deleting it, run:

```bash
distrobox stop ubuntu26
```

The container's files and installed packages stay in place. Enter it again at any time to resume work.

## Delete a container

When you no longer need a container, make sure it's stopped first (with `distrobox stop ubuntu26`), and then delete it:

```bash
distrobox rm ubuntu26
```

Deleting a container removes its installed packages, but your home directory stays on the host because it's shared rather than stored inside the container.

## Find other distributions

Distrobox doesn't have its own catalog of distributions. It creates containers from standard container images hosted on registries such as Docker Hub and quay.io, so any distribution with a suitable image works.

To list the images the Distrobox project has tested, run:

```bash
distrobox create --compatibility
```

The output is a list of image names, and includes entries similar to:

```output
docker.io/library/debian:stable-backports
docker.io/library/debian:unstable
quay.io/fedora/fedora:44
quay.io/toolbx-images/almalinux-toolbox:9
quay.io/toolbx-images/alpine-toolbox:edge
```

The list changes as new releases are tested. The [Distrobox compatibility page](https://distrobox.it/compatibility/#containers-distros) shows the same information in a table, grouped by distribution.

To create a container from any image in the list, or from an image you find on a registry, pass its name to the `--image` option as you did for Ubuntu.

{{% notice Note %}}
The compatibility list doesn't say which images support Arm. Before you use an image, check that its registry page lists an `arm64` variant. Most official images from Ubuntu, Debian, Fedora, and Alpine provide one.
{{% /notice %}}

You're now ready to use Distrobox to run Ubuntu 26.04 and other distributions on your Arm device.
