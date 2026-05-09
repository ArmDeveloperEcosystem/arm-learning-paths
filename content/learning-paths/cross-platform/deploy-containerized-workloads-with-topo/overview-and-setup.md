---
title: Install Topo on your host machine
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## What is Topo?

[Topo](https://github.com/arm/topo) is an open-source command-line tool developed by Arm. It uses a host/target model. The host — your development machine, which can be x86 or Arm, running Linux, macOS, or Windows — runs the Topo CLI and connects to an Arm-based Linux target over SSH. Topo builds container images on the host, transfers them to the target, and starts the services on the target. Topo can also build and deploy directly on the target.

Topo detects the hardware capabilities of the target — such as Arm CPU features including Neon and SVE — and uses this information to identify which containerized workload templates are compatible. Topo also provides sample templates for common use cases, including a "Hello World" webpage, an LLM chatbot, and a SIMD benchmark comparing scalar, Neon (128-bit fixed-width), and SVE (scalable-width vector) implementations.

[Topo templates](https://github.com/arm/topo-template-format) are based on the [Compose Specification](https://github.com/compose-spec/compose-spec), extended with `x-topo` metadata that describes requirements such as CPU features and build arguments. The Compose Specification is a standard, YAML-based format for describing multi-container applications. Instead of starting containers individually, you define all services, images, connections, and configuration in a single `compose.yaml` file.

You can use any compatible target device in this Learning Path, for example a Raspberry Pi, an AWS Graviton-based EC2 instance, a DGX Spark, or an NXP i.MX 93. The target must be Arm-based, running Linux, and accessible over SSH. Your host can also function as the target simultaneously, provided it is an Arm-based Linux device.

The optional heterogeneous deployment section requires a Cortex-A + Cortex-M SoC, such as the i.MX 93.

## Why use Topo?

Topo removes the need to handle low-level setup and compatibility checks manually. It queries the target to identify processor features such as SVE or Neon, advises which templates are appropriate for the device, and automates the end-to-end deployment.

If you have a heterogeneous SoC (for example, a Cortex-A + Cortex-M device such as the i.MX 93), you can use Topo to deploy both firmware and application as containerized workloads through standard container tooling. This lets you make full use of all processors on the device.

You can also use Topo with CLI agents to streamline deployment workflows.


## Install Topo

Install Topo on your host using the following install script, or download the binary manually.

On your host device, run the following command:

{{< tabpane code=true >}}
  {{< tab header="Linux / MacOS">}}
curl -fsSL https://raw.githubusercontent.com/arm/topo/refs/heads/main/scripts/install.sh | sh
  {{< /tab >}}
  {{< tab header="Windows" >}}
irm https://raw.githubusercontent.com/arm/topo/refs/heads/main/scripts/install.ps1 | iex
  {{< /tab >}}
{{< /tabpane >}}

Alternatively, find the [latest release of Topo](https://github.com/arm/topo/releases), download the binary for your platform (x86/Arm, Linux/macOS/Windows), and extract it. Topo is a single executable file. Move it to a directory on your `PATH`, for example `/usr/local/bin/` on Linux and macOS.

Run the following command in the terminal on your host device to confirm the installation:

```bash
topo --help
```

The output confirms that Topo is present and describes the available commands:

```output
Topo CLI

Usage:
  topo [command]

Available Commands:
  clone       Clone an example project
  completion  Generate the autocompletion script for the specified shell
  deploy      Deploy services using the compose file
  extend      Add services from a template to the compose file
  health      Check the target host environment
  help        Help about any command
  init        Initialise a new project in the current directory
  install     Install components to the target
  service     Manage services in compose files
  setup-keys  Generate SSH keys for the target and install the public key on the target host
  stop        Stop a currently running deployment
  templates   List available service templates
  upgrade     Upgrade topo to the latest version

Flags:
  -h, --help            help for topo
  -o, --output string   output format: plain or json (default "plain")
  -v, --version         version for topo

Use "topo [command] --help" for more information about a command.
```

## What you've accomplished and what's next

You have now installed Topo on your host and confirmed it is available. Next, you'll use Topo to prepare your host and probe your target device for features, assessing its compatibility with template containerized workloads.
