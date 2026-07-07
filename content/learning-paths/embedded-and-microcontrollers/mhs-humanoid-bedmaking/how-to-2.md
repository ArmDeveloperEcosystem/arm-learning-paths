---
title: Set up Isaac Sim, Isaac Lab, and the MHS SDK on a DGX Spark
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

The NVIDIA DGX Spark is an Arm (GB10) machine, so you build **NVIDIA Isaac Sim 5.1** from source for `aarch64`, then install **Isaac Lab 2.3.2** against it, and finally install the **MHS Python SDK** into the Isaac Lab Python environment. Everything below runs on the Spark itself.

Set a working directory used throughout this Learning Path:

```bash
export WORK=$HOME/mhs-humanoid
mkdir -p "$WORK" && cd "$WORK"
```

## Build Isaac Sim 5.1 from source

Clone Isaac Sim and build it. On the GB10 the parallel build can race on one plugin the first time; if `build.sh` fails, simply run it again — the incremental build resolves it.

```bash
cd "$WORK"
git clone https://github.com/isaac-sim/IsaacSim.git
cd IsaacSim
./build.sh   # if the first run fails on a debug_draw / primitive_drawing link error, run ./build.sh again
```

{{% notice Note %}}
**GB10 build fix (Isaac Sim).** The first `build.sh` can fail with a missing `*debug_draw*primitive_drawing*.so` because the premake link step races the plugin build. Re-running `./build.sh` (incremental) links against the now-present plugin and completes. Two or three attempts is normal on a cold build.
{{% /notice %}}

When the build finishes, the runnable Sim is at `IsaacSim/_build/linux-aarch64/release`. Record it:

```bash
export ISAACSIM_PATH="$WORK/IsaacSim/_build/linux-aarch64/release"
ls "$ISAACSIM_PATH/python.sh"   # should exist
```

## Install Isaac Lab 2.3.2

Clone Isaac Lab at the pinned version, point it at your Isaac Sim build, and install it.

```bash
cd "$WORK"
git clone --branch v2.3.2 --recursive https://github.com/isaac-sim/IsaacLab.git
cd IsaacLab
ln -sfn "$ISAACSIM_PATH" "$PWD/_isaac_sim"
./isaaclab.sh --install
```

{{% notice Note %}}
**GB10 build fix (Isaac Lab).** On Python ≥ 3.12 the install can trip over a newer `setuptools`. If `./isaaclab.sh --install` fails while building a dependency, pin setuptools below 81 in the Isaac Lab Python and re-run:

```bash
./isaaclab.sh -p -m pip install "setuptools<81"
./isaaclab.sh --install
```
{{% /notice %}}

`./isaaclab.sh -p` runs the bundled Python; you will use it for every script in this Learning Path. On `aarch64`, preload libgomp so native extensions load cleanly:

```bash
export LD_PRELOAD="${LD_PRELOAD:+$LD_PRELOAD:}/lib/aarch64-linux-gnu/libgomp.so.1"
```

## Install the MHS Python SDK

The MHS SDK's distribution name is `mhs-python-sdk` and its import root is `mhs`. Until the first public release it installs from source; clone it and install it **editable into the Isaac Lab Python** so the demo can import it:

```bash
cd "$WORK"
git clone https://github.com/modelhardwarestandard/python-sdk.git mhs-python-sdk
cd "$WORK/IsaacLab"
./isaaclab.sh -p -m pip install -e "$WORK/mhs-python-sdk[wire,nats]"
```

The `[wire,nats]` extras select the pure-Python procedures/events/discovery tier plus the NATS transport client — everything the multi-robot coordination needs.

## Clone the demo and the humanoid connector

```bash
cd "$WORK"
git clone https://github.com/armwaheed/robots.git
git clone https://github.com/armwaheed/robotics-connect.git
```

- `robots/examples/isaac_bed_making` is the Isaac Sim demo you run in this Learning Path.
- `robotics-connect` is Arm's humanoid MHS connector and skills; the demo reuses its sensor-calibration and the whole-body policy tooling.

## Verify the environment

Run a single import check through the Isaac Lab Python:

```bash
cd "$WORK/IsaacLab"
./isaaclab.sh -p -c "import isaacsim, isaaclab, torch, mhs; print('OK', 'torch', torch.__version__, 'cuda', torch.cuda.is_available())"
```

You should see `OK`, a Torch version, and `cuda True`. If `import mhs` fails, re-check the editable install command above. With the environment verified, continue to run the demo.
