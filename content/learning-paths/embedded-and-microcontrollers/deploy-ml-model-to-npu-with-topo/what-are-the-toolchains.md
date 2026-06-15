---
title: Understand the toolchains
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the build and runtime pieces

The `topo-imx93-npu-deployment` Template combines several toolchains. Topo hides much of the deployment plumbing, but it is useful to understand what is being built and where each component runs.

## ExecuTorch

[ExecuTorch](https://docs.pytorch.org/executorch/stable/index.html) is PyTorch's runtime for deploying PyTorch models to edge devices. By using different backends within ExecuTorch, you can target specific hardware. For example, you can target Ethos-U65 by using the Ethos-U backend. To learn more about how the MobileNetV2 model was exported from PyTorch to ExecuTorch, and delegated to the Ethos-U, look at [Build ExecuTorch models for Ethos-U65](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/7-build-executorch-pte/).

In this Template, ExecuTorch is used in two places:

- At build time, the Template exports a MobileNetV2 model to an ExecuTorch `.pte` program.
- At run time, the Cortex-M33 firmware loads and executes that `.pte` program.

The export pipeline targets `ethos-u65-256`, which means the Ethos-U65 has 256 multiply-accumulate (MAC) units. The model is quantized and lowered so supported neural network operators can be delegated to the Ethos-U65 NPU. The generated file is:

```output
mv2_ethosu65_256.pte
```

The web application includes this `.pte` file in its container image. During inference, it writes the file into the reserved physical memory range starting at `0xC0000000`, where the Cortex-M33 runner can read it.

## Cortex-M33 firmware runner

The firmware runner is built as:

```output
executorch_runner_cm33.elf
```

This firmware runs on the Cortex-M33 core. It waits for commands coming from the Linux web application over `RPMsg`, reads the input image tensors from reserved memory, executes inference through ExecuTorch, and writes classification output back over `RPMsg`.

The Template packages the firmware as the entrypoint of the `cm33-runner` image:

```yaml
cm33-runner:
  runtime: io.containerd.remoteproc.v1
  annotations:
    remoteproc.name: imx-rproc
```

The `runtime: io.containerd.remoteproc.v1` setting tells containerd to use the remote processor runtime instead of the normal Linux container runtime. The `remoteproc.name` annotation identifies the target remote processor driver, `imx-rproc`.

## remoteproc-runtime

Linux includes a `remoteproc` framework for loading and controlling auxiliary processors such as the Cortex-M33 on the i.MX 93. `remoteproc-runtime` adds an Open Container Initiative interface on top of this framework, allowing firmware to be packaged and launched using container tooling.

Topo uses `remoteproc-runtime` when deploying the `cm33-runner` service. The deployment flow is:

1. Topo builds the `runner-runtime` image containing `executorch_runner_cm33.elf`.
2. Topo starts the image on the target.
3. containerd uses `io.containerd.remoteproc.v1`.
4. `remoteproc-runtime` passes the ELF file to the Linux `remoteproc` driver.
5. The kernel loads the ELF segments and releases the Cortex-M33.

This is why the target must pass the `Remoteproc Runtime`, `Remoteproc Shim`, and `Subsystem Driver (remoteproc)` checks in `topo health`.

## RPMsg

`RPMsg` is the communication channel between the Cortex-A Linux application and the Cortex-M33 firmware. The web application sends a `RUN` command over a `/dev/ttyRPMSG*` device. The firmware replies with status and classification output.

If the deployment succeeds but classification times out, inspect the web app's board checks and the target's `RPMsg` devices. The application expects an `RPMsg` TTY to appear after the Cortex-M33 firmware starts.

## Shared reserved memory

The web application and firmware exchange model and input data through reserved physical memory. The Template expects the target device tree to reserve:

- `model@c0000000`: 4 MiB for the ExecuTorch `.pte` file and input tensor.
- `ethosu_region@A8000000`: 128 MiB for Ethos-U65 use.

The web application checks these ranges at startup through `/proc/device-tree`. It also checks for `/dev/mem`, `/dev/ethosu0`, the `imx-rproc` remote processor, the `.pte` file, and ImageNet labels.

## Web application

The `webapp` service is a Python Flask application. It serves the browser UI, preprocesses selected images, stages the .pte program and input tensor in reserved memory, sends inference commands over `RPMsg`, and renders the ImageNet top-1 and top-5 results.

By default, the service maps target port `3001` to container port `3000`.

## What you've accomplished and what's next

You now understand the major toolchains and runtime interfaces used by the Template: ExecuTorch, the Cortex-M33 firmware runner, remoteproc-runtime, RPMsg, reserved memory, and the Flask web application. You have also seen how the web application stages the `.pte` program and input data in reserved memory before sending inference commands to the Cortex-M33 firmware.

Next, you will review how the project is structured as a Topo Template, including the Compose services, build artifacts, Remoteproc Runtime metadata, and Topo arguments.
