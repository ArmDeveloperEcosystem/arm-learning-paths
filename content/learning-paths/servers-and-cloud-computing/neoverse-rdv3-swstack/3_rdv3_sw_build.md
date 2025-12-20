---
title: Build the RD-V3 Reference Platform Software Stack
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Building the RD-V3 Reference Platform Software Stack

In this module, you’ll set up your development environment on any Arm-based server and build the firmware stack required to simulate the RD-V3 platform. This Learning Path was tested on an AWS `m7g.4xlarge` Arm-based instance running Ubuntu 22.04.

## Step 1: Set up your development environment

First, check that your system is current and install the required dependencies:

```bash
sudo apt update
sudo apt install -y curl git
```

Configure git(optional):

```bash
git config --global user.name "<your-name>"
git config --global user.email "<your-email@example.com>"
```

## Step 2: Fetch the source code

The RD‑V3 platform firmware stack consists of multiple components, most maintained in separate Git repositories, such as:

- TF‑A
- SCP/MCP
- RSE (TF-M)
- UEFI (EDK II)
- Linux kernel
- Buildroot
- kvmtool (lkvm)
- RMM (optional)

Use the repo tool with the RD-V3 manifest to sync these sources from multiple upstreams consistently (typically to a pinned release tag). It simplifies syncing the full platform software stack from multiple upstreams.

If `repo` is not installed, you can download it and add it to your `PATH`:

```bash
mkdir -p ~/.bin
PATH="${HOME}/.bin:${PATH}"
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
chmod a+rx ~/.bin/repo
```

Once ready, create a workspace and initialize the repo manifest. This Learning Path uses a pinned manifest to ensure reproducibility across different environments. This locks all component repositories to known-good commits that are validated and aligned with a specific FVP version.

For this session, use `pinned-rdv3.xml` and `RD-INFRA-2025.07.03`:

```bash
cd ~
mkdir rdv3
cd rdv3
```
Initialize and sync the source code tree:
```bash
repo init -u https://git.gitlab.arm.com/infra-solutions/reference-design/infra-refdesign-manifests.git -m pinned-rdv3.xml -b refs/tags/RD-INFRA-2025.07.03 --depth=1
repo sync -c -j $(nproc) --fetch-submodules --force-sync --no-clone-bundle --retry-fetches=5
```

Once synced, the output should look like:
```output
Syncing:  95% (19/20), done in 2m36.453s
Syncing: 100% (83/83) 2:52 | 1 job | 0:01 platsw/edk2-platforms @ uefi/edk2/edk2-platformsrepo sync has finished successfully.
```

{{% notice Note %}}
As of the time of writing, the latest release tag is `RD-INFRA-2025.07.03`. Newer tags might be available in future updates.
{{% /notice %}}

This manifest fetches the required sources, including:
* TF‑A
* SCP / RSE firmware
* EDK II (UEFI)
* Linux kernel
* Buildroot and platform scripts


## Step 3: Build the Docker Image

There are two supported methods for building the reference firmware stack: **host-based** and **container-based**.

- The **host-based** build installs all required dependencies directly on your local system and executes the build natively.
- The **container-based** build runs the compilation process inside a pre-configured Docker image, ensuring consistent results and isolation from host environment issues.

In this Learning Path, you will use the **container-based** approach.

The container image uses your host source directory (~/rdv3) and performs the build inside Docker. Ensure Docker is installed on your machine. You can follow this [installation guide](/install-guides/docker/).


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

The build procedure can take a few minutes, depending on network bandwidth and CPU performance. This Learning Path was tested on an AWS `m7g.4xlarge` instance, and the build took 250 seconds. 

Expected output:

```output
Building docker image: rdinfra-builder ...
[+] Building 239.7s (19/19) FINISHED                                                                                                docker:default
 => [internal] load build definition from rd-infra-arm64                                                                                      0.0s
 => => transferring dockerfile: 4.50kB                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/ubuntu:jammy-20240911.1                                                                    1.0s
 => [internal] load .dockerignore                                                                                                             0.0s
 => => transferring context: 2B                                                                                                               0.0s
 => [internal] load build context                                                                                                             0.0s
 => => transferring context: 10.80kB                                                                                                          0.0s
 => [ 1/14] FROM docker.io/library/ubuntu:jammy-20240911.1@sha256:0e5e4a57c2499249aafc3b40fcd541e9a456aab7296681a3994d631587203f97            1.7s
 => => resolve docker.io/library/ubuntu:jammy-20240911.1@sha256:0e5e4a57c2499249aafc3b40fcd541e9a456aab7296681a3994d631587203f97              0.0s
 => => sha256:0e5e4a57c2499249aafc3b40fcd541e9a456aab7296681a3994d631587203f97 6.69kB / 6.69kB                                                0.0s
 => => sha256:7c75ab2b0567edbb9d4834a2c51e462ebd709740d1f2c40bcd23c56e974fe2a8 424B / 424B                                                    0.0s
 => => sha256:981912c48e9a89e903c89b228be977e23eeba83d42e2c8e0593a781a2b251cba 2.31kB / 2.31kB                                                0.0s
 => => sha256:a186900671ab62e1dea364788f4e84c156e1825939914cfb5a6770be2b58b4da 27.36MB / 27.36MB                                              1.1s
 => => extracting sha256:a186900671ab62e1dea364788f4e84c156e1825939914cfb5a6770be2b58b4da                                                     0.5s
 => [ 2/14] RUN apt-get update -q=2     && apt-get install -q=2 --yes --no-install-recommends         ca-certificates         curl           12.5s
 => [ 3/14] RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null         | gpg --dearmor - | tee /etc/apt/trust  0.5s 
 => [ 4/14] RUN apt-get update -q=2     && apt-get install -q=2 --yes --no-install-recommends         acpica-tools         autoconf          40.0s 
 => [ 5/14] RUN pip3 install --no-cache-dir poetry                                                                                            7.4s 
 => [ 6/14] RUN curl https://storage.googleapis.com/git-repo-downloads/repo > /usr/bin/repo     && chmod a+x /usr/bin/repo                    0.3s 
 => [ 7/14] COPY common/install-openssl.sh /tmp/common/                                                                                       0.0s 
 => [ 8/14] RUN bash /tmp/common/install-openssl.sh /opt                                                                                     32.7s 
 => [ 9/14] COPY common/install-gcc.sh /tmp/common/                                                                                           0.0s 
 => [10/14] COPY common/install-clang.sh /tmp/common/                                                                                         0.0s 
 => [11/14] RUN  bash /tmp/common/install-gcc.sh /opt 13.2.rel1 "arm-none-eabi"                                                              19.8s 
 => [12/14] RUN  bash /tmp/common/install-gcc.sh /opt 13.2.rel1 "aarch64-none-elf"                                                           13.4s 
 => [13/14] RUN  bash /tmp/common/install-clang.sh /opt 15.0.6                                                                              101.2s 
 => [14/14] COPY common/entry.sh /root/entry.sh                                                                                               0.0s 
 => exporting to image                                                                                                                        9.2s 
 => => exporting layers                                                                                                                       9.2s 
 => => writing image sha256:3a395c5a0b60248881f9ad06048b97ae3ed4d937ffb0c288ea90097b2319f2b8                                                  0.0s 
 => => naming to docker.io/library/rdinfra-builder                                                                                            0.0s
```

Verify the image:
  
```bash
docker images
```

You should see a docker image called `rdinfra-builder`:

```output
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
rdinfra-builder   latest    3a395c5a0b60   4 minutes ago   8.12GB
```

Quick interactive test:

```bash
./container.sh -v ~/rdv3 run
```

This script mounts your source directory (~/rdv3) into the container and opens a shell session at that location. Inside the container, you should see a prompt like this:

```output
Running docker image: rdinfra-builder ...
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

your-username:hostname:/home/your-username/rdv3$
```

You can explore the container environment if you wish, then type `exit` to return to the host.


## Step 4: Build firmware 

Building the full firmware stack involves compiling several components and packaging them for simulation. The following command runs build and then package inside the Docker image:

- **build**compiles all individual components of the firmware stack, including TF‑A, SCP, RSE, UEFI, Linux kernel, and rootfs
- **package** consolidates outputs into simulation-ready artifacts for FVP

Ensure you’re back in the host OS, then run:

```bash
cd ~/rdv3
docker run --rm \
  -v "$PWD:$PWD" \
  -w "$PWD" \
  --mount type=volume,dst="$HOME" \
  --env ARCADE_USER="$(id -un)" \
  --env ARCADE_UID="$(id -u)" \
  --env ARCADE_GID="$(id -g)" \
  -t -i rdinfra-builder \
  bash -c "./build-scripts/rdinfra/build-test-buildroot.sh -p rdv3 build && \
           ./build-scripts/rdinfra/build-test-buildroot.sh -p rdv3 package"
```

The build artifacts will be placed under `~/rdv3/output/rdv3/rdv3/`, where the last `rdv3` in the directory path corresponds to the selected platform name.

Inspect the artifacts:

```bash
ls ~/rdv3/output/rdv3/rdv3 -al
```

Expected output:
```output
total 7092
drwxr-xr-x 2 ubuntu ubuntu    4096 Aug 12 13:15 .
drwxr-xr-x 4 ubuntu ubuntu    4096 Aug 12 13:15 ..
lrwxrwxrwx 1 ubuntu ubuntu      25 Aug 12 13:15 Image -> ../components/linux/Image
lrwxrwxrwx 1 ubuntu ubuntu      35 Aug 12 13:15 Image.defconfig -> ../components/linux/Image.defconfig
-rw-r--r-- 1 ubuntu ubuntu 7250838 Aug 12 13:15 fip-uefi.bin
lrwxrwxrwx 1 ubuntu ubuntu      32 Aug 12 13:15 lcp_ramfw.bin -> ../components/rdv3/lcp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      26 Aug 12 13:15 lkvm -> ../components/kvmtool/lkvm
lrwxrwxrwx 1 ubuntu ubuntu      32 Aug 12 13:15 mcp_ramfw.bin -> ../components/rdv3/mcp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      26 Aug 12 13:15 rmm.img -> ../components/rdv3/rmm.img
lrwxrwxrwx 1 ubuntu ubuntu      32 Aug 12 13:15 scp_ramfw.bin -> ../components/rdv3/scp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      29 Aug 12 13:15 tf-bl1.bin -> ../components/rdv3/tf-bl1.bin
lrwxrwxrwx 1 ubuntu ubuntu      29 Aug 12 13:15 tf-bl2.bin -> ../components/rdv3/tf-bl2.bin
lrwxrwxrwx 1 ubuntu ubuntu      30 Aug 12 13:15 tf-bl31.bin -> ../components/rdv3/tf-bl31.bin
lrwxrwxrwx 1 ubuntu ubuntu      53 Aug 12 13:15 tf_m_flash.bin -> ../components/arm/rse/neoverse_rd/rdv3/tf_m_flash.bin
lrwxrwxrwx 1 ubuntu ubuntu      46 Aug 12 13:15 tf_m_rom.bin -> ../components/arm/rse/neoverse_rd/rdv3/rom.bin
lrwxrwxrwx 1 ubuntu ubuntu      48 Aug 12 13:15 tf_m_vm0_0.bin -> ../components/arm/rse/neoverse_rd/rdv3/vm0_0.bin
lrwxrwxrwx 1 ubuntu ubuntu      48 Aug 12 13:15 tf_m_vm1_0.bin -> ../components/arm/rse/neoverse_rd/rdv3/vm1_0.bin
lrwxrwxrwx 1 ubuntu ubuntu      33 Aug 12 13:15 uefi.bin -> ../components/css-common/uefi.bin
```
Reference mapping:

| Component            | Output Files                                 | Description                 |
|----------------------|----------------------------------------------|-----------------------------|
| TF‑A                 | `bl1.bin`, `bl2.bin`, `bl31.bin`, `fip.bin`  | Entry-level boot firmware   |
| SCP and RSE firmware | `scp.bin`, `mcp_rom.bin`, etc.               | Platform power/control      |
| UEFI                 | `uefi.bin`, `flash0.img`                     | Boot device enumeration     |
| Linux kernel         | `Image`                                      | OS payload                  |
| Initrd               | `rootfs.cpio.gz`                             | Minimal filesystem          |


## Optional: run the build manually from inside the container

You can also build from within an interactive container session (useful for debugging or partial builds):

Start your docker container. In your running container shell:
```bash
cd ~/rdv3
./build-scripts/rdinfra/build-test-buildroot.sh -p rdv3 build
./build-scripts/rdinfra/build-test-buildroot.sh -p rdv3 package
```

You’ve now prepared and built the full RD-V3 firmware stack. In the next section, you’ll install the appropriate FVP and simulate the full boot sequence, bringing the firmware to life on a virtual platform.
