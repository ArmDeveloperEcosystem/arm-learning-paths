---
title: Run and manage UltraEdge HPC-I for AI and mixed workloads on Arm

weight: 6

layout: "learningpathall"
---

## Get started with the Tinkerblox CLI

In this section, you'll use the Tinkerblox CLI to deploy, manage, and monitor microservices on the UltraEdge platform. You'll practise inspecting system state, installing a sample microservice, and observing its runtime behavior.

To get started, download a sample MPAC file from the [Tinkerblox support repository](https://github.com/Tinkerbloxsupport/arm-learning-path-support/blob/main/static/Sample_ms/dte_nn.mpac) and install it on your device.

## Use the Tinkerblox CLI

The Tinkerblox Command Line Interface (CLI) lets you manage the Edge Agent and microservices on UltraEdge devices.

**Basic usage:**

```bash
tinkerblox-cli [OPTIONS] <COMMAND>
```

**Common commands:**

- `status`: Show connection status with the Edge Agent
- `microboost`: Microservice management commands
- `help`: Print this message or the help for a given subcommand

**Options:**

- `-h`, `--help`: Print help
- `-V`, `--version`: Print version

## Check CLI connection status

To verify that the CLI is connected to the Edge Agent, run:

```bash
sudo tinkerblox-cli status
```

The output shows whether the CLI is connected to the Edge Agent.

## Manage microservices

You can install, list, start, stop, and uninstall microservices using the `microboost` command. Replace `/path/to/your.mpac` with the path to your MPAC file and `<id>` with the microservice ID.

**Install a microservice:**
```bash
sudo tinkerblox-cli microboost install -f /path/to/your.mpac
```

**List installed microservices:**
```bash
sudo tinkerblox-cli microboost list
```

**Show microservice status:**
```bash
sudo tinkerblox-cli microboost status <id>
```

**Stop a microservice:**
```bash
sudo tinkerblox-cli microboost stop <id>
```

**Start a microservice:**
```bash
sudo tinkerblox-cli microboost start <id>
```

**Uninstall a microservice:**
```bash
sudo tinkerblox-cli microboost uninstall <id>
```

## Run diagnostics

Use the `diagnostics` command to check system health and connectivity on your UltraEdge device.

**Syntax:**
```bash
sudo tinkerblox-cli diagnostics <command>
```

**Available diagnostics:**

        sudo tinkerblox-cli diagnostics full

**system** : Check CPU, memory, and OS-level health

        sudo tinkerblox-cli diagnostics system

**network** : Verify network connectivity and endpoint reachability

        sudo tinkerblox-cli diagnostics network

**filesystem** : Validate database/filesystem connectivity and integrity

        sudo tinkerblox-cli diagnostics filesystem

**engine** : Check engine microboost neuroboost

        sudo tinkerblox-cli diagnostics engine

## Troubleshooting

 The following sections describe common errors you may encounter while running CLI commands or deploying microservices, along with guidance on how to resolve them. These are general errors and are not limited to any specific scenario; they may occur while executing commands or managing the system.

Permission denied

-   Ensure `sudo` privileges.
-   Check directory ownership and permissions.
-   Verify overlay filesystem support.

Directory creation failed

-   Check disk space.
-   Verify parent directory permissions.
-   Ensure the path is valid.

Cross-architecture build issues

Cross-architecture issues typically occur when binaries are built for a different CPU architecture than the host system. They are not related to yocto build issues. 

-   Verify QEMU installation:

```bash
        qemu-aarch64-static --version
```

-   Check binfmt registration:

```bash
        ls /proc/sys/fs/binfmt_misc/
```

-   Ensure the target architecture is enabled.

-   If issues persist, change the host architecture.

## What you've accomplished and what's next

In this section, you:
- Used the Tinkerblox CLI to manage microservices and system diagnostics
- Practiced installing, starting, stopping, and monitoring microservices on UltraEdge

Next, explore more advanced CLI features, automate deployments, or integrate with additional monitoring and orchestration tools for your edge environment.