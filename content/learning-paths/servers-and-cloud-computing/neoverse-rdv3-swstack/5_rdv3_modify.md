---
title: Build and Run RDV3-R1 Dual Chip Platform
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build and Run RDV3-R1 Dual Chip Platform

### Why Use RD‑V3‑R1?

The RD‑V3‑R1 platform is a dual-chip simulation environment built to model multi-die Arm server SoCs. It expands on the single-die RD‑V3 design by introducing a second application processor and a Management Control Processor (MCP).

***Key Use Cases***

- Simulate chiplet-style boot flow with two APs
- Observe coordination between SCP and MCP across dies
- Test secure boot in a distributed firmware environment

***Differences from RD‑V3***
- Dual AP boot flow instead of single AP
- Adds MCP (Cortex‑M7) to support cross-die management
- More complex power/reset coordination

### Build the RD‑V3‑R1 Firmware Stack

Initialize and sync the codebase for RD‑V3‑R1:

```bash
cd ~
mkdir rdv3r1
cd rdv3r1
# Initialize the source tree
repo init -u https://git.gitlab.arm.com/infra-solutions/reference-design/infra-refdesign-manifests.git -m pinned-rdv3r1.xml -b refs/tags/RD-INFRA-2025.07.03 --depth=1

# Sync the full source code
repo sync -c -j $(nproc) --fetch-submodules --force-sync --no-clone-bundle
```


```bash
cd ~/rdv3r1/container-scripts
./container.sh build
```

Download and Install the FVP Model.

```bash
mkdir -p ~/fvp
cd ~/fvp
wget https://developer.arm.com/-/cdn-downloads/permalink/FVPs-Neoverse-Infrastructure/RD-V3-r1/FVP_RD_V3_R1_11.29_35_Linux64_armv8l.tgz
tar -xvf FVP_RD_V3_R1_11.29_35_Linux64_armv8l.tgz
./FVP_RD_V3_R1.sh
```


Once connected via Remote Desktop, open a terminal and launch the RD‑V3 FVP simulation:

```bash
cd ~/rdv3r1/model-scripts/rdinfra
export MODEL=/home/ubuntu/FVP_RD_V3/models/Linux64_armv8l_GCC-9.3/FVP_RD_V3_R1
./boot-buildroot.sh -p rdv3r1 &
```