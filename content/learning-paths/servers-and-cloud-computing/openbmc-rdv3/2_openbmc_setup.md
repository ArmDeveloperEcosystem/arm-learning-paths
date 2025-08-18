---
title: Set Up OpenBMC Development Environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set Up Development Environment

This module guides you through installing dependencies, configuring repositories, and preparing your workspace to simulate the OpenBMC and UEFI firmware stack on the Arm Neoverse RD-V3 platform using Fixed Virtual Platforms (FVPs).

Before getting started, it’s strongly recommended to review the previous Learning Path: [CSS-V3 Pre-Silicon Software Development Using Neoverse Servers](https://learn.arm.com/learning-paths/servers-and-cloud-computing/neoverse-rdv3-swstack).
That guide walks you through how to use the CSSv3 reference design on FVP to perform early-stage development and validation.

Ensure your system meets the following requirements:
- Access to an Arm Neoverse-based Linux machine (either cloud-based or local) is required, with at least 80 GB of free disk space, 48 GB of RAM, and running Ubuntu 22.04 LTS.
- Working knowledge of Docker, Git, and Linux terminal tools
- Basic understanding of server firmware stack (UEFI, BMC, TF-A, etc.)
- Docker installed, or GitHub Codespaces-compatible development environment

### Install Required Packages

Install the base packages for building OpenBMC with the Yocto Project:

```bash
sudo apt update
sudo apt install git gcc g++ make file wget gawk diffstat bzip2 cpio chrpath zstd lz4 bzip2 unzip
```

### Set Up the repo Tool

```bash
mkdir -p ~/.bin
PATH="${HOME}/.bin:${PATH}"
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
chmod a+rx ~/.bin/repo
```

### Download the Arm FVP Model (RD-V3)

Download and extract the RD-V3 FVP binary from Arm:
```bash
mkdir ~/fvp
cd ~/fvp
wget https://developer.arm.com/-/cdn-downloads/permalink/FVPs-Neoverse-Infrastructure/RD-V3-r1/FVP_RD_V3_R1_11.29_35_Linux64_armv8l.tgz
tar -xvf FVP_RD_V3_R1_11.29_35_Linux64_armv8l.tgz
./FVP_RD_V3_R1.sh
```

The FVP installation may prompt you with a few questions—choosing the default options is sufficient for this learning path. By default, the FVP will be installed in /home/ubuntu/FVP_RD_V3_R1.


### Initialize the Host Build Environment

Set up a workspace for host firmware builds:

```bash
mkdir ~/host
cd host

~/.bin/repo init -u "https://git.gitlab.arm.com/infra-solutions/reference-design/infra-refdesign-manifests.git" \
 -m "pinned-rdv3r1-bmc.xml" \
 -b "refs/tags/RD-INFRA-2025.07.03" \
 --depth=1

repo sync -c -j $(nproc) --fetch-submodules --force-sync --no-clone-bundle
```



{{% notice Need Review %}}
We need descript how to / where can download the patch file?
{{% /notice %}}

Then, download the `patch.zip` from ... into root directory and unzip the file.

```bash
unzip ~/patch.zip
```

Create a file `~/apply_patch.sh` and copy following content into.

```patch
FVP_DIR="host"
SOURCE=${PWD}

GREEN='\033[0;32m'
NC='\033[0m'

pushd ${FVP_DIR} > /dev/null
echo -e "${GREEN}\n===== Apply patches to edk2 =====\n${NC}"
pushd uefi/edk2
git am --keep-cr ${SOURCE}/patch/edk2/*.patch
popd > /dev/null

echo -e "${GREEN}\n===== Apply patches to edk2-platforms =====\n${NC}"
pushd uefi/edk2/edk2-platforms > /dev/null
git am --keep-cr ${SOURCE}/patch/edk2-platforms/*.patch
popd > /dev/null

echo -e "${GREEN}\n===== Apply patches to edk2-redfish-client =====\n${NC}"
git clone https://github.com/tianocore/edk2-redfish-client.git
pushd edk2-redfish-client > /dev/null
git checkout 4f204b579b1d6b5e57a411f0d4053b0a516839c8
git am --keep-cr ${SOURCE}/patch/edk2-redfish-client/*.patch
popd > /dev/null

echo -e "${GREEN}\n===== Apply patches to buildroot =====\n${NC}"
pushd buildroot > /dev/null
git am ${SOURCE}/patch/buildroot/*.patch
popd > /dev/null

echo -e "${GREEN}\n===== Apply patches to build-scripts =====\n${NC}"
pushd build-scripts > /dev/null
git am ${SOURCE}/patch/build-scripts/*.patch
popd > /dev/null
popd > /dev/null
```

Next, apply patches to the `host`.

```bash
chmod +x ./apply_patch.sh
./apply_patch.sh
```

{{% notice Need Review %}}
We need descript more about what's the patch?
{{% /notice %}}


### Build RDv3 R1 Host Docker Image

Before building the host image, update the following line in `~/host/grub/bootstrap` to replace the `git://` protocol.
Some networks or corporate environments restrict `git://` access due to firewall or security policies. Switching to `https://` ensures reliable and secure access to external Git repositories.

```
diff --git a/bootstrap b/bootstrap
index 5b08e7e2d..031784582 100755
--- a/bootstrap
+++ b/bootstrap
@@ -47,7 +47,7 @@ PERL="${PERL-perl}"
    me=$0
-default_gnulib_url=git://git.sv.gnu.org/gnulib
+default_gnulib_url=https://git.savannah.gnu.org/git/gnulib.git
usage() {
    cat <<EOF
```

```bash
cd ~/host/container-scripts
./container.sh build
```

Within the `host` directory, run:

```bash
docker run --rm \
  -v $HOME/host:$HOME/host \
  -w $HOME/host \
  --env ARCADE_USER=$(id -un) \
  --env ARCADE_UID=$(id -u) \
  --env ARCADE_GID=$(id -g) \
  -t -i rdinfra-builder \
  bash -c "./build-scripts/rdinfra/build-test-busybox.sh -p rdv3r1 all"
```

Once complete, you can observe the build binary in `~/host/output/rdv3r1/rdv3r1/`

```
ls -la host/output/rdv3r1/rdv3r1/
total 4308
drwxr-xr-x 2 ubuntu ubuntu    4096 Aug 18 10:19 .
drwxr-xr-x 4 ubuntu ubuntu    4096 Aug 18 10:20 ..
lrwxrwxrwx 1 ubuntu ubuntu      25 Aug 18 10:19 Image -> ../components/linux/Image
lrwxrwxrwx 1 ubuntu ubuntu      35 Aug 18 10:19 Image.defconfig -> ../components/linux/Image.defconfig
-rw-r--r-- 1 ubuntu ubuntu 4402315 Aug 18 10:19 fip-uefi.bin
lrwxrwxrwx 1 ubuntu ubuntu      34 Aug 18 10:19 lcp_ramfw.bin -> ../components/rdv3r1/lcp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      33 Aug 18 10:19 lcp_ramfw_ns -> ../components/rdv3r1/lcp_ramfw_ns
lrwxrwxrwx 1 ubuntu ubuntu      26 Aug 18 10:19 lkvm -> ../components/kvmtool/lkvm
lrwxrwxrwx 1 ubuntu ubuntu      34 Aug 18 10:19 mcp_ramfw.bin -> ../components/rdv3r1/mcp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      33 Aug 18 10:19 mcp_ramfw_ns -> ../components/rdv3r1/mcp_ramfw_ns
lrwxrwxrwx 1 ubuntu ubuntu      28 Aug 18 10:19 rmm.img -> ../components/rdv3r1/rmm.img
lrwxrwxrwx 1 ubuntu ubuntu      34 Aug 18 10:19 scp_ramfw.bin -> ../components/rdv3r1/scp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      33 Aug 18 10:19 scp_ramfw_ns -> ../components/rdv3r1/scp_ramfw_ns
lrwxrwxrwx 1 ubuntu ubuntu      41 Aug 18 10:19 signed_lcp_ramfw.bin -> ../components/rdv3r1/signed_lcp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      41 Aug 18 10:19 signed_mcp_ramfw.bin -> ../components/rdv3r1/signed_mcp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      41 Aug 18 10:19 signed_scp_ramfw.bin -> ../components/rdv3r1/signed_scp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      31 Aug 18 10:19 tf-bl1.bin -> ../components/rdv3r1/tf-bl1.bin
lrwxrwxrwx 1 ubuntu ubuntu      30 Aug 18 10:19 tf-bl1_ns -> ../components/rdv3r1/tf-bl1_ns
lrwxrwxrwx 1 ubuntu ubuntu      31 Aug 18 10:19 tf-bl2.bin -> ../components/rdv3r1/tf-bl2.bin
lrwxrwxrwx 1 ubuntu ubuntu      32 Aug 18 10:19 tf-bl31.bin -> ../components/rdv3r1/tf-bl31.bin
lrwxrwxrwx 1 ubuntu ubuntu      55 Aug 18 10:19 tf_m_flash.bin -> ../components/arm/rse/neoverse_rd/rdv3r1/tf_m_flash.bin
lrwxrwxrwx 1 ubuntu ubuntu      48 Aug 18 10:19 tf_m_rom.bin -> ../components/arm/rse/neoverse_rd/rdv3r1/rom.bin
lrwxrwxrwx 1 ubuntu ubuntu      50 Aug 18 10:19 tf_m_vm0_0.bin -> ../components/arm/rse/neoverse_rd/rdv3r1/vm0_0.bin
lrwxrwxrwx 1 ubuntu ubuntu      50 Aug 18 10:19 tf_m_vm0_1.bin -> ../components/arm/rse/neoverse_rd/rdv3r1/vm0_1.bin
lrwxrwxrwx 1 ubuntu ubuntu      50 Aug 18 10:19 tf_m_vm1_0.bin -> ../components/arm/rse/neoverse_rd/rdv3r1/vm1_0.bin
lrwxrwxrwx 1 ubuntu ubuntu      50 Aug 18 10:19 tf_m_vm1_1.bin -> ../components/arm/rse/neoverse_rd/rdv3r1/vm1_1.bin
lrwxrwxrwx 1 ubuntu ubuntu      33 Aug 18 10:19 uefi.bin -> ../components/css-common/uefi.bin
```


{{% notice Note %}}
The other [Arm Learning Path](https://learn.arm.com/learning-paths/servers-and-cloud-computing/neoverse-rdv3-swstack/3_rdv3_sw_build/) provides a complete introduction to setting up the RDv3 development environment — feel free to refer to it for more details.
{{% /notice %}}


### Build OpenBMC Image

you need use [BitBake](https://docs.yoctoproject.org/bitbake/) to build OpenBMC.

{{% notice Need Review %}}


Should we need install bitbake?

```bash
git clone https://git.openembedded.org/bitbake
cd bitbake
```
How to install bitbake? Clone https://git.openembedded.org/bitbake or else?
{{% /notice %}}

Start by cloning and building the OpenBMC image using the bitbake build system:

```bash
cd ~
git clone https://github.com/openbmc/openbmc.git
cd openbmc
source setup fvp
bitbake obmc-phosphor-image
```

During the OpenBMC build process, you may encounter a native compilation error when building Node.js (especially version 22+) due to high memory usage during the V8 engine build phase depends on your build machine.

```
g++: fatal error: Killed signal terminated program cc1plus
compilation terminated.
ERROR: oe_runmake failed
```

This is a typical Out-of-Memory (OOM) failure, where the system forcibly terminates the compiler due to insufficient available memory.

To reduce memory pressure, explicitly limit parallel tasks in `conf/local.conf`:

```bash
BB_NUMBER_THREADS = "2"
PARALLEL_MAKE = "-j2"
```

This ensures that BitBake only runs two parallel tasks and that each Makefile invocation limits itself to two threads. It significantly reduces peak memory usage and avoids OOM terminations.

Once success build, you will observe the message like:

```
Loading cache: 100% |                                                                                                              | ETA:  --:--:--
Loaded 0 entries from dependency cache.
Parsing recipes: 100% |#############################################################################################################| Time: 0:00:09
Parsing of 3054 .bb files complete (0 cached, 3054 parsed). 5148 targets, 770 skipped, 0 masked, 0 errors.
NOTE: Resolving any missing task queue dependencies

Build Configuration:
BB_VERSION           = "2.12.0"
BUILD_SYS            = "aarch64-linux"
NATIVELSBSTRING      = "ubuntu-22.04"
TARGET_SYS           = "aarch64-openbmc-linux"
MACHINE              = "fvp"
DISTRO               = "openbmc-phosphor"
DISTRO_VERSION       = "nodistro.0"
TUNE_FEATURES        = "aarch64 armv8-4a"
TARGET_FPU           = ""
meta                 
meta-oe              
meta-networking      
meta-python          
meta-phosphor        
meta-arm             
meta-arm-toolchain   
meta-arm-bsp         
meta-evb             
meta-evb-fvp-base    = "master:1b6b75a7d22262ec1bf5ab8e2bfa434ac84d981b"

Sstate summary: Wanted 0 Local 0 Mirrors 0 Missed 0 Current 2890 (0% match, 100% complete)###############################           | ETA:  0:00:00
Initialising tasks: 100% |##########################################################################################################| Time: 0:00:03
NOTE: Executing Tasks

```

{{% notice Note %}}
The first build may take up to an hour depending on your system performance, as it downloads and compiles the entire firmware stack.
{{% /notice %}}


```text
├── FVP_RD_V3_R1
├── apply_patch.sh
├── fvp
│   ├── FVP_RD_V3_R1.sh
│   ├── FVP_RD_V3_R1_11.29_35_Linux64_armv8l.tgz
│   └── license_terms
├── host
│   ├── build-scripts
│   ├── buildroot
│   ├── ... 
├── openbmc
│   ├── ...
│   ├── build
│   ├── meta-arm
│   ├── ...
│   ├── poky
│   └── setup
├── patch
│   ├── build-scripts
│   ├── buildroot
│   ├── edk2
│   ├── edk2-platforms
│   └── edk2-redfish-client
├── patch.zip
└── run.sh

``
