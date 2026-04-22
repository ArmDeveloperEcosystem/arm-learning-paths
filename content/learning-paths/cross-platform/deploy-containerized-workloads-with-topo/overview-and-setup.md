---
title: Overview - What is the Topo tool?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Topo?

[Topo](https://github.com/arm/topo) is an open-source command-line tool, developed by Arm. Topo connects from a host device (e.g., your development laptop) to an Arm-based Linux target (e.g., a Raspberry Pi) over SSH, detects hardware capabilities, and allows the user to deploy compatible containerized workloads with ease. Topo builds container images on the host, transfers them to the target, and starts the services on the target. Building and deploying on target is also possible. Topo also showcases several sample templates defining workloads you can deploy, including a "Hello World" webpage, an LLM Chatbot, and a SIMD Benchmark comparing Scalar, Neon, and the Scalable Vector Extension (SVE).

[Topo templates](https://github.com/arm/topo-template-format) are based on the [Compose Specification](https://github.com/compose-spec/compose-spec), extended with `x-topo` metadata that describes requirements such as CPU features and build arguments. The Compose Specification is a standard, YAML-based format for describing how to run multi-container applications. Instead of manually starting containers one-by-one, you define everything in a single file that includes which services to run, what images to use, how they connect, and what configuration they need.

In this learning path, you can use a target device of your choice, whether that be Raspberry Pi, AWS Graviton instance, DGX Spark, NXP i.MX 93, or similar. The only stipulation is that the device must be Arm-based, running Linux, and accessible over SSH. Your host can also function as your target simultaneously, but only if your host is an Arm-based Linux device.

The optional heterogeneous deployment with `remoteproc-runtime` requires a heterogeneous Cortex-A + Cortex-M SoC, such as the i.MX 93.

## Why use Topo?

Topo streamlines deploying containerized workloads to Arm-based Linux devices.
If you have an heterogeneous device (e.g. Cortex-A + Cortex-M SoC such as the i.MX 93), Topo enables you to use it fully, deploying both firmware and application as containerized workloads through standard container tooling.

Once a template is defined, use of Topo removes the need to deal with low-level setup and compatibility issues manually. Topo first assesses the system to identify processor features such as SVE or Neon on CPU, then advises which templates are appropriate for the device, before automating the end to end deployment, for which Topo deals with all the low-level instructions.

Topo can also be leveraged by AI Agents to further streamline and automate.

## Install Topo

In this step, you install Topo on the host, along with other dependencies.

On your host device, run the following commands to install Topo:

{{< tabpane code=true >}}
  {{< tab header="Linux / MacOS">}}
curl -fsSL https://raw.githubusercontent.com/arm/topo/refs/heads/main/scripts/install.sh | sh
  {{< /tab >}}
  {{< tab header="Windows" >}}
irm https://raw.githubusercontent.com/arm/topo/refs/heads/main/scripts/install.ps1 | iex
  {{< /tab >}}
{{< /tabpane >}}

Alternatively, find the [latest release of Topo](https://github.com/arm/topo/releases), download the binary for your specific platform (x86/Arm, Linux/MacOS/Windows), and extract it. Topo is provided as a single executable file and `README.md`. Place Topo on your `PATH`:

Run the following command in the terminal on your host device to confirm the installation:

```bash
topo --help
```

You should see an output confirming Topo is present, and describing the available commands.

## What you've completed and what's next

You have now installed Topo on your host. In the next step, you will utilize Topo to prepare your host machine and to probe your target device for features, assessing its compability with template containerized workloads.
