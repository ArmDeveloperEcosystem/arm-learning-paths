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

- **full**: Run complete system diagnostics and summarize results
  ```bash
  sudo tinkerblox-cli diagnostics full
  ```
- **system**: Check CPU, memory, and OS-level health
  ```bash
  sudo tinkerblox-cli diagnostics system
  ```
- **network**: Verify network connectivity and endpoint reachability
  ```bash
  sudo tinkerblox-cli diagnostics network
  ```
- **filesystem**: Validate database and filesystem connectivity and integrity
  ```bash
  sudo tinkerblox-cli diagnostics filesystem
  ```
- **engine**: Check engine, microboost, and neuroboost
  ```bash
  sudo tinkerblox-cli diagnostics engine
  ```

## Troubleshoot common issues

If you encounter errors while running CLI commands or deploying microservices, use the following guidance to resolve them:

**Permission denied**
- Ensure you have `sudo` privileges.
- Check directory ownership and permissions.
- Verify overlay filesystem support is enabled.

**Directory creation failed**
- Check available disk space.
- Verify parent directory permissions.
- Ensure the path is valid.

**Cross-architecture build issues**
Cross-architecture issues usually occur when binaries are built for a different CPU architecture than your host system. These are not related to Yocto build issues.
- Verify QEMU installation:
        ```bash
        qemu-aarch64-static --version
        ```
- Check binfmt registration:
        ```bash
        ls /proc/sys/fs/binfmt_misc/
        ```
- Ensure the target architecture is enabled.
- If issues persist, try changing the host architecture.

## What you've accomplished and what's next

In this section, you:
- Used the Tinkerblox CLI to manage microservices and system diagnostics
- Practiced installing, starting, stopping, and monitoring microservices on UltraEdge

Next, explore more advanced CLI features, automate deployments, or integrate with additional monitoring and orchestration tools for your edge environment.