---
title: Distrobox
description: Install Distrobox on Arm Linux or Linux on a ChromeOS or Googlebook OS device, and run an Ubuntu 26.04 container that integrates with your home directory.


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

You can use [Distrobox](https://distrobox.it/) to run any Linux distribution inside a container while sharing your home directory with the host. Distrobox uses Podman or Docker underneath, so that you can create a container and enter it similar to a normal shell. You can install packages with the package manager for the distribution, and remove the container when you're done. Your files stay on the host, which makes the containers safe to experiment with and quick to throw away.

Distrobox is useful on Arm systems when you want a different distribution than your host, or a clean build environment for testing.

You'll learn how to install Distrobox and run an Ubuntu container on a system running Arm Linux. You can use a physical Arm device, an Arm-based virtual machine, or the Linux development environment on a ChromeOS or Googlebook OS device. 

## Before you begin

Make sure that you're using a system running Arm Linux. 

Confirm the architecture:

```bash
uname -m
```

The expected output for 64-bit Arm systems is `aarch64`.

Distrobox needs a container engine. Podman is used in these steps because it runs containers without root privileges. This suits both Arm Linux and the ChromeOS and Googlebook OS Linux environment.

{{% notice Note %}}
On a ChromeOS or Googlebook OS device, set up the Linux development environment first. On ChromeOS, open **Settings**. Navigate to **About ChromeOS** and select **Developers**. Then, turn on **Linux development environment**. 

On Googlebook OS, open the **Terminal** app from the app drawer. Follow the prompts to initialize the Linux environment. This creates a managed Debian environment where you install and run Distrobox. The environment already provides the user namespace and `subuid` and `subgid` configuration that rootless Podman needs.
{{% /notice %}}

## Install Distrobox on Arm Linux

The following steps are for a Debian-based distribution. This can be Ubuntu, or the Debian environment on a ChromeOS or Googlebook OS device. 

Install Podman, Distrobox, and the `uidmap` package for rootless containers:

```bash
sudo apt update
sudo apt install -y podman distrobox uidmap curl
```

Confirm that the tools are installed:

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

A `true` result confirms that rootless mode is working. You can create and enter containers as your normal user.

## Verify Distrobox installation

You'll now verify Distrobox installation by creating a container and running commands in it. The container will run `arm64` software.

### Create an Ubuntu 26.04 container

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

### Enter the container

The first time you enter a container, Distrobox sets up your user, sudo access, and the shared home directory. This takes a moment. Later entries are faster.

Enter the container:

```bash
distrobox enter ubuntu26
```

When setup finishes, your shell prompt changes to show that you're inside the container. 

Confirm the distribution and architecture:

```bash
grep PRETTY_NAME /etc/os-release
uname -m
```

The output is similar to:

```output
PRETTY_NAME="Ubuntu 26.04.1 LTS"
aarch64
```

You're now in an Ubuntu 26.04 environment on Arm. Your home directory is shared with the host, so files that you create are visible in both places. Confirm this by listing your home directory:

```bash
ls $HOME
```

You'll see the same files and directories as on your host. 

Install packages with `apt` as you would on any Ubuntu system:

```bash
sudo apt update
sudo apt install -y htop
```

{{% notice Note %}}
Any software that you install inside the container needs to have an `arm64` build. Most packages in the Ubuntu repositories provide one, so `apt` installs work as expected on your Arm device.
{{% /notice %}}

### Exit the container

To leave the container and return to your host shell, press **Ctrl+D**.

The container keeps running in the background after you exit. You can enter it again without waiting for setup.

### Run a command in the container from the host

To run a single command inside the container from your host, pass it after `--`:

```bash
distrobox enter ubuntu26 -- uname -m
```

The output is similar to:

```output
aarch64
```

### View container status

See a list of containers that you've created, and their status:

```bash
distrobox list
```

The output is similar to:

```output
ID           | NAME                 | STATUS             | IMAGE
56452187200e | ubuntu26             | Up 23 minutes      | docker.io/library/ubuntu:26.04
```

## Stop the container

Stop the running container without deleting it:

```bash
distrobox stop ubuntu26
```

The container files and installed packages stay in place. Enter the container again at any time to resume work.

## Delete the container

When you no longer need a container, make sure that it's stopped first, then delete it.

Delete the test container:

```bash
distrobox rm ubuntu26
```

Deleting a container removes its installed packages. Your home directory stays on the host because it's shared rather than stored inside the container.

## Find other distributions for Distrobox

Distrobox doesn't have its own catalog of distributions. It creates containers from standard container images that are hosted on registries such as Docker Hub and quay.io. Any distribution with a suitable image works with Distrobox.

List the images tested for the Distrobox project:

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

{{% notice Note %}}
The compatibility list doesn't indicate which images support Arm. Before you use an image, check that its registry page lists an `arm64` variant. Most official images from Ubuntu, Debian, Fedora, and Alpine provide one.
{{% /notice %}}

## Next steps

You're now ready to use Distrobox to run Ubuntu 26.04 and other distributions on your Arm device.

To create a container from any image on the compatibility list or a registry, pass its name to the `--image` option.
