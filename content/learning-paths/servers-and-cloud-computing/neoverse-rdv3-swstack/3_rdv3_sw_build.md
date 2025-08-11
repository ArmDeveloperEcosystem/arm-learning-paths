---
title: Building the RD‑V3 Reference Platform
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Building the RD‑V3 Reference Platform

In this module, you’ll set up your development environment and build the firmware stack required to simulate the RD‑V3 platform.

### Step 1: Prepare the Development Environment

First, ensure your system is up-to-date and install the required tools and libraries:

```bash
sudo apt update
sudo apt install curl git
```

Configure git as follows.

```bash
git config --global user.name "<your-name>"
git config --global user.email "<your-email@example.com>"
```

### Step 2: Fetch the Source Code

The RD‑V3 platform firmware stack consists of many independent components—such as TF‑A, SCP, RSE, UEFI, Linux kernel, and Buildroot. Each component is maintained in a separate Git repository.

To manage and synchronize these repositories efficiently, we use the `repo` tool. It simplifies syncing the full platform software stack from multiple upstreams.

If repo is not installed, you can download it manually:

```bash
mkdir -p ~/.bin
PATH="${HOME}/.bin:${PATH}"
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
chmod a+rx ~/.bin/repo
```

Once ready, create a workspace and initialize the repo manifest by following instruction.

You will reference the designated `manifest.xml` file from the Arm GitLab repository and specify the corresponding `release tag`. For this session, we will use pinned-rdv3.xml and RD-INFRA-2025.07.03. 


```bash
cd ~
mkdir rdv3
cd rdv3
# Initialize the source tree
repo init -u https://git.gitlab.arm.com/infra-solutions/reference-design/infra-refdesign-manifests.git -m pinned-rdv3.xml -b RD-INFRA-2025.07.03 --depth=1

# Sync the full source code
repo sync -c -j $(nproc) --fetch-submodules --force-sync --no-clone-bundle
```

{{% notice Note %}}
As of the time of writing, the latest official release tag is RD-INFRA-2025.07.03.
Please note that newer tags may be available as future platform updates are published.
{{% /notice %}}

This manifest will fetch all required sources including:
* TF‑A
* SCP / RSE firmware
* EDK2 (UEFI)
* Linux kernel
* Buildroot and platform scripts


### Step 3: Build the Reference Stack

There are two supported methods for building the reference firmware stack: **host-based** and **container-based**.

- The **host-based** build installs all required dependencies directly on your local system and executes the build natively.
- The **container-based** build runs the compilation process inside a pre-configured Docker image, ensuring consistent results and isolation from host environment issues.

In this Learning Path, we will use the **container-based** approach.

The container image is designed to use the source directory from the host (`~/rdv3`) and perform the build process inside the container. Make sure Docker is installed on your Linux machine. You can follow this [installation guide](https://learn.arm.com/install-guides/docker/).


After Docker is installed, you’re ready to build the container image.

The `container.sh` script is a wrapper that builds the container using default settings for the Dockerfile and image name. You can customize these by using the `-f` (Dockerfile) and `-i` (image name) options, or by editing the script directly.

To view all available options:

```bash
cd ~/rdv3/container-scripts
./container.sh -h
```

To build the container image:

```bash
./container.sh build
```

After the build completes successfully, the following output artifacts will be generated in the `~/rdv3/fvp/output/` directory:

| Component            | Output Files                                |
|----------------------|----------------------------------------------|
| TF‑A                 | `bl1.bin`, `bl2.bin`, `bl31.bin`, `fip.bin`  |
| SCP and RSE firmware | `scp.bin`, `mcp_rom.bin`, etc.               |
| UEFI                 | `uefi.bin`, `flash0.img`                     |
| Linux kernel         | `Image`                                      |
| Initrd               | `rootfs.cpio.gz`                             |

