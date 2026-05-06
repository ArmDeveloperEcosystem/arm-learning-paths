---
title: Use Topo to assess target compatibility
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run Topo health checks

Start by running a Topo health check to confirm that all required dependencies are available on the host and the target.

### Prepare host environment

Confirm that the required dependencies are available on the host by running this command in your host terminal:

```bash
topo health
```

The output is similar to:

```output
Host
----
Topo: ✅ (topo)
SSH: ✅ (ssh)
Container Engine: ✅ (docker)

Target
------
ℹ️ provide --target or set TOPO_TARGET to check target health

```

If Docker is missing, follow the steps in [Install Docker](https://learn.arm.com/install-guides/docker/) to install Docker.

If SSH is missing, follow the steps in [Install SSH](https://learn.arm.com/install-guides/ssh/) to install SSH.

### Prepare target environment

Now that the host is prepared, connect to your target over SSH to verify its dependencies:

```bash
ssh user@my-target
```

After connecting to the target, use the following commands to verify both Docker and `lscpu` are installed:

```bash
docker --version
lscpu
```

The output is similar to:

```output
Docker version xx.x.x
Architecture:             aarch64
CPU(s):                   ...
```


### Run a health check against the target

Run the following command from the terminal of your host device.

If you are using your host device simultaneously as your target, use `topo health --target localhost`.

```bash
topo health --target user@my-target
``` 

The output is similar to the following example from a heterogeneous SoC, with differences depending on your hardware:

```output
Host
----
Topo: ✅ (topo)
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

A Topo health check confirms connectivity between the host and target, and verifies the presence of dependencies such as Docker.

Resolve any `❌` errors before moving on. Warnings (⚠️) can indicate optional capabilities that might be needed in certain projects. `ℹ️` provides other information. A `✅` confirms the presence of dependencies without warnings or errors.


#### Troubleshoot SSH authentication

If you are using password-based SSH, you might see the following `❌` error:

```output
Connectivity: ❌ (key-based SSH authentication is not setup)
  → run `topo setup-keys --target user@my-target` or manually setup SSH keys for the target
```

This is because Topo requires key-based SSH for secure, automated access. You can use the command specified in the output, and Topo will set up the key-based SSH for you. When prompted to set a passphrase, leave it empty for automation, or use a passphrase and an SSH agent for added security. Afterwards, run `topo health` again to confirm it has correctly set up key-based authentication.

If you encounter SSH errors, check that:
- The target device is powered on and accessible from the host
- The correct username and IP address are used
- Your firewall allows SSH traffic


## (Optional) Install remoteproc-runtime on heterogeneous devices

If you're using a Cortex-A + Cortex-M device such as the i.MX 93, you might see a `⚠️` warning if `remoteproc-runtime` is not installed on the target.

[`remoteproc`](https://docs.kernel.org/staging/remoteproc.html) is a Linux kernel framework for managing remote or auxiliary processors in a heterogeneous SoC. It allows the main CPU (for example, Cortex-A) to load firmware onto the auxiliary processors (for example, Cortex-M), start and stop them, and communicate with them using [`rpmsg`](https://docs.kernel.org/staging/rpmsg.html).

[`remoteproc-runtime`](https://github.com/arm/remoteproc-runtime) builds on this by adding an Open Container Initiative (OCI) interface. This lets you package and manage firmware such as container images using standard tools such as Docker or containerd, even though the code runs as firmware on the Cortex-M. [OCI](https://opencontainers.org/) defines open standards for container image formats and runtimes, ensuring compatibility across container tools.


You need remoteproc-runtime only if your target is a heterogeneous SoC (for example, Cortex-A + Cortex-M, such as i.MX 93). For most single-CPU Arm Linux targets, you can skip this step.

You can use Topo to install `remoteproc-runtime`. Run the following command from the host device:

```bash
topo install remoteproc-runtime --target user@my-target
```

Run the health command again to verify installation. Topo uses `remoteproc-runtime` internally when deploying to heterogeneous devices.


## Generate a target description

Ask Topo to probe your target and output a description of the hardware in your terminal. 

On your host device, run:

```bash
topo describe --target user@my-target
```

The output captures details such as CPU architecture features, which Topo uses to select compatible templates.

The following is an example snippet from an AWS Graviton-based instance, showing the main processor and its features, an absence of any remote or auxiliary processors, and the total memory:

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

The `features` list mirrors the CPU feature flags reported by the Linux kernel. Key flags include `fp` (hardware floating-point), `asimd` (Neon Advanced SIMD — 128-bit vector acceleration), and `aes` (hardware AES encryption). Topo uses this feature list to determine which templates are compatible with your target.

## List templates compatible with your target

Because Topo can identify the capabilities of your target device, it can also advise on the compatibility of templates.

Use the following command on your host device to list compatible templates:

```bash
topo templates --target user@my-target
```

The following is an example output for an AWS Graviton-based instance:

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

In this example, `topo-lightbulb-moment` is marked as incompatible, because it requires an SoC with both a Cortex-A and a Cortex-M. The instance contains Arm Neoverse cores only. All other templates are marked as compatible. You might see different results depending on the target hardware you use.

## What you've accomplished and what's next

You have now verified your host and target environments, resolved any missing dependencies, and optionally enabled heterogeneous deployment. You also generated a description of your target's hardware features and identified compatible templates. Next, you'll choose a template containerized workload and deploy it to your target.