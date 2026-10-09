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


## Understand target compatibility

Topo probes the target during health checks and project listing. It uses target details such as the CPU architecture, Arm CPU features, memory, and remote processor support to determine which Topo Projects are compatible.

The hardware feature list mirrors CPU feature flags reported by the Linux kernel. Key flags include `fp` (hardware floating-point), `asimd` (Neon Advanced SIMD — 128-bit vector acceleration), and `aes` (hardware AES encryption). Topo uses this information to determine which projects are compatible with your target.

## List projects compatible with your target

Because Topo can identify the capabilities of your target device, it can also advise on the compatibility of projects.

Use the following command on your host device to list compatible projects:

```bash
topo projects --target user@my-target
```

The following is an example output for an AWS Graviton-based instance:

```output
Hello World
  Clone:
    topo clone https://github.com/Arm-Examples/topo-welcome.git#main

  A minimal "Hello, World" web app for validating a Topo setup and deployment.
  It runs a single service that exposes a web page on the target,
  with the greeting text customizable via the GREETING_NAME parameter.

Lightbulb Moment
  Clone:
    topo clone https://github.com/Arm-Examples/topo-lightbulb-moment.git#main
  Features:
    remoteproc-runtime

  Reads a switch over GPIO pins on an M class cpu, reports switch state over
  Remoteproc Message, then a web application on the A class reads this and
  displays a lightbulb in either the on or off state. The lightbulb state is
  described by an LLM in any user-specified style.

Topo llama.cpp WebUI Chat
  Clone:
    topo clone https://github.com/Arm-Examples/topo-llama-web-ui.git#main

  LLM chat application with Arm CPU inference provided by llama.cpp.

  This project demonstrates running large language models on CPU
  with inference provided by the llama.cpp server.

  The upstream Linux Arm64 image includes architecture-specific CPU
  backend variants for Armv8.0 baseline, Armv8.2 dot product/FP16/SVE,
  Armv8.6 int8 matrix multiply/SVE2, and Armv9.2 SME-capable CPUs.

SIMD Visual Benchmark
  Clone:
    topo clone https://github.com/Arm-Examples/topo-simd-visual-benchmark.git#main
  Features:
    SVE

  Visual demonstration of SIMD performance benefits on Arm processors.
  Compare scalar (no SIMD), NEON (128-bit), and SVE (scalable vector)
  implementations running identical image processing workloads side-by-side.
```

When you provide `--target`, Topo marks each project according to compatibility with your target. For example, `topo-lightbulb-moment` requires `remoteproc-runtime`, so it is incompatible with targets that don't provide a supported remote processor environment. You might see different results depending on the target hardware you use.

## What you've accomplished and what's next

You have now verified your host and target environments, resolved any missing dependencies, and optionally enabled heterogeneous deployment. You also identified compatible projects for your target. Next, you'll choose a containerized workload project and deploy it to your target.
