---
title: Use Topo to assess target compatibility
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run Topo health checks

### Prepare host environment

Confirm that the required dependencies are available on the host by running this command in your host terminal:

```bash
topo health
```

The output should appear similar to the following:

```bash
Host
----
SSH: ✅ (ssh)
Container Engine: ✅ (docker)

Target
------
ℹ️ provide --target or set TOPO_TARGET to check target health
```

If Docker is missing, please use [Install Docker](https://learn.arm.com/install-guides/docker/).

If SSH is missing, please use [Install SSH](https://learn.arm.com/install-guides/ssh/).

## Prepare target environment

Now that the host device is prepared, we will setup the target. On the host device, connect to your target with SSH.

```bash
ssh user@your-target
```

Once connected to the target, use the following commands to verify both Docker and `lscpu` are installed:

```bash
docker --version
lscpu
```

The output should apear similar to the following:

```output
Docker version xx.x.x
Architecture:             aarch64
CPU(s):                   ...
```

### Prepare Topo for target

We will now run a health check against your target. Run the following command from the terminal of your host device.

If you are using your host device simultaneously as your target, use `topo health --target localhost`.

```bash
topo health --target user@my-target
```

The output should appear similar to:

```output
Host
----
SSH: ✅ (ssh)
Container Engine: ✅ (docker)

Target
------
Connectivity: ✅
Container Engine: ✅ (docker)
Remoteproc Runtime: ✅ (remoteproc-runtime)
Remoteproc Shim: ✅ (containerd-shim-remoteproc-v1)
Hardware Info: ✅ (lscpu)
Subsystem Driver (remoteproc): ✅ (m33, m0)
```

A Topo health check confirms connectivity between the host and target, as well as the verifying the presence of dependencies such as docker.

You should resolve any `❌` errors before moving on. Warnings (`⚠️`) can indicate optional capabilities you can add later. `ℹ️` provides other information. A `✅` confirms the presence of dependencies and no warnings or errors.

If you are using password-based SSH, you will likely see the `❌` error below:

```output
Connectivity: ❌ (key-based SSH authentication is not setup)
  → run `topo setup-keys --target user@my-target` or manually setup SSH keys for the target
```

This is because Topo requires key-based SSH. You can use the command specified above, and Topo will setup the key-based SSH for you. Ensure that if prompted to set a passphrase, you leave it empty. Afterwards, run `topo health` again to confirm it has correctly setup the key-based authentication.

## Optional: install remoteproc-runtime on heterogeneous devices

If using a Cortex-A + Cortex-M device, such as the i.MX 93, you may see a `⚠️` warning if `remoteproc-runtime` is not installed on the target.

[`remoteproc`](https://docs.kernel.org/staging/remoteproc.html) is a Linux kernel framework for managing remote / auxiliary processors in a heterogeneous SoC. It allows the main CPU (e.g., Cortex-A) to load firmware on to the auxiliary processors (e.g., Cortex-M), start and stop them, and to communicate with them (e.g. using `rpmsg`).

[`remoteproc-runtime`](https://github.com/arm/remoteproc-runtime) builds on this by adding a container-style (OCI) interface. This lets you package and manage firmware like container images using standard tools (e.g. Docker or containerd), even though the code runs as firmware on the Cortex-M. OCI (Open Container Initiative) defines open standards for container image formats and runtimes, ensuring compatibility across container tools.

You can use Topo to install `remoteproc-runtime`. Run the following command from the host device:

```bash
topo install remoteproc-runtime --target user@my-target
```

Run the health command again to verify installation. Topo uses `remoteproc-runtime` under the hood when deploying to heterogeneous devices.

## Generate a target description

In this step, you ask Topo to probe your target and create a machine-readable YAML description of the hardware.

On your host device, run:

```bash
topo describe --target user@my-target
```

This writes a `target-description.yaml` file in your current directory.

The file captures details such as CPU architecture features, which Topo uses to select compatible templates.

Open the file and have a look. An example snippet from an AWS Graviton instance is shown below, showing the main processor and its features, an absence of any remote / auxiliary processors, and the total memory:

```output
host:
    - model: Neoverse-V1
      cores: 4
      features:
        - fp
        - asimd
        - evtstrm
        - aes
        ...
remoteprocs: []
totalmemory_kb: 16044280
```

## List templates compatible with your target

Now that Topo understand the capabilities of your target device, it can advise on the compatibility of templates.

Use the following command on your host device to to list templates according to the target description:

```bash
topo templates --target-description target-description.yaml
```

You can also query templates directly by specifying the target:

```bash
topo templates --target user@my-target
```

An example output for an AWS Graviton instance is shown below:

```output
✅ topo-welcome | https://github.com/Arm-Examples/topo-welcome.git | main
  A minimal "Hello, World" web app for validating a Topo setup and deployment.
  It runs a single service that exposes a web page on the target,
  with the greeting text customizable via the GREETING_NAME parameter.

❌ topo-lightbulb-moment | https://github.com/Arm-Examples/topo-lightbulb-moment.git | main
  Features: remoteproc-runtime
  Reads a switch over GPIO pins on an M class cpu, reports switch state over
  Remoteproc Message, then a web application on the A class reads this and
  displays a lightbulb in either the on or off state. The lightbulb state is
  described by an LLM in any user-specified style.

✅ topo-cpu-ai-chat | https://github.com/Arm-Examples/topo-cpu-ai-chat.git | main
  Features: SVE, NEON
  Complete LLM chat application optimized for Arm CPU inference.

  This project demonstrates running large language models on CPU
  using llama.cpp compiled with Arm baseline optimizations and
  accelerated using NEON SIMD and SVE (when supported and enabled).

  The stack includes:
  - llama.cpp server with Arm NEON optimizations (SVE optional)
  - Quantized Qwen2.5-1.5B-Instruct model bundled in the image (~1.12 GB)
  - Simple web-based chat interface
  - No GPU required - pure CPU inference

  Perfect for demos and testing! The bundled Qwen2.5-1.5B model allows the
  project to run immediately without downloading additional models.

  Ideal for testing LLM workloads on Arm hardware without GPU dependencies,
  showcasing how far you can push NEON acceleration. Rebuild with SVE enabled
  when wider vectors are available.

✅ topo-simd-visual-benchmark | https://github.com/Arm-Examples/topo-simd-visual-benchmark.git | main
  Features: NEON, SVE
  Visual demonstration of SIMD performance benefits on Arm processors.
  Compare scalar (no SIMD), NEON (128-bit), and SVE (scalable vector)
  implementations running identical image processing workloads side-by-side.

  This demo shows real hardware acceleration through three C++ services
  compiled with different architecture flags, processing the same box blur
  algorithm on images. Performance differences are measured in real-time
  and displayed in an interactive web dashboard.

  Perfect for demonstrating to non-technical audiences the concrete benefits
  of SIMD optimizations, with visual results and quantified speedups.
```

In the above example, `topo-lightbulb-moment` is marked as incompatible, since it requires an SoC with both a Cortex-A and a Cortex-M. The Graviton instance used contains Arm Neoverse cores only. All other templates are marked as compatible. You may see different results depending on the target hardware you use.

## What you've learned and what's next

You have performed a health check on your target device and generated a description of its hardware features. Topo has informed you which templates are compatible with your target. In the next step, you will choose and deploy a template containerized workload.

