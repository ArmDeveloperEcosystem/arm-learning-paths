---
title: RUNNING Setup/Installation - UltraEdge HPC-I execution fabric for AI & mixed workloads

weight: 5

layout: "learningpathall"
---

{{% notice Note %}}
REMOVE ME:  We probably need to come up with an actual "exercise" here to exercise tinkerblox... below is only a reference to the CLI commands... what do we want the user to explore/experiment and see with tinkerblox? 
{{% /notice %}}

### Tinkerblox CLI Usage Guide

Tinkerblox Command Line Interface for managing the Edge Agent and
microservices.

**Usage:**

    tinkerblox-cli [OPTIONS] <COMMAND>

**Commands:**

-   `status` — Show connection status with the Edge Agent
-   `microboost` — Microservice management commands
-   `help` — Print this message or the help of the given subcommand(s)

**Options:**

-   `-h`, `--help` — Print help
-   `-V`, `--version` — Print version

### Usage

#### Check CLI Connection Status

    sudo tinkerblox-cli status

*Displays whether the CLI is connected to the Edge Agent.*

#### Microservice Management

Manage microservices running on the Edge platform.

**Syntax:**

    sudo tinkerblox-cli microboost <command> [options]

##### Available Commands

* **install**
    Installs a microservice. You must provide the path to the MPAC file as an argument.

        sudo tinkerblox-cli microboost install -f /path/to/your.mpac

* **list**
    Lists all installed microservices.

        sudo tinkerblox-cli microboost list

* **status <id>**
    Shows statistics (CPU, memory, status, etc.) for the specified microservice.

        sudo tinkerblox-cli microboost status <id>

* **stop <id>**
    Stops the microservice with the specified ID.

        sudo tinkerblox-cli microboost stop <id>

* **start <id>**
    Starts the microservice with the specified ID (must be stopped).

        sudo tinkerblox-cli microboost start <id>

* **uninstall <id>**
    Uninstalls the microservice with the specified ID.

        sudo tinkerblox-cli microboost uninstall <id>

#### Diagnostics Management

Run diagnostics on the Edge platform.

**Syntax:**

    sudo tinkerblox-cli diagnostics <command>

**full**  
Run complete system diagnostics and summarize results

    sudo tinkerblox-cli diagnostics full

**system**  
Check CPU, memory, and OS-level health

    sudo tinkerblox-cli diagnostics system

**network**  
Verify network connectivity and endpoint reachability

    sudo tinkerblox-cli diagnostics network

**filesystem**  
Validate database/filesystem connectivity and integrity

    sudo tinkerblox-cli diagnostics filesystem

**engine**  
Check engine microboost neuroboost

    sudo tinkerblox-cli diagnostics engine

## Troubleshooting

{{% notice Note %}}
REMOVE ME:  We probably need to outline more where the errors might be seen while running a specific task/exercise...  
{{% /notice %}}

**Permission Denied**

-   Ensure `sudo` privileges.
-   Check directory ownership and permissions.
-   Verify overlay filesystem support.

**Directory Creation Failed**

-   Check disk space.
-   Verify parent directory permissions.
-   Ensure the path is valid.

**Cross-Architecture Build Issues**

{{% notice Note %}}
REMOVE ME: are there any tel-tale signs that my issue is a cross-architecture build issue?  Is this a Yocto build issue?
{{% /notice %}}

-   Verify QEMU installation:

        qemu-aarch64-static --version

-   Check binfmt registration:

        ls /proc/sys/fs/binfmt_misc/

-   Ensure the target architecture is enabled.

-   If issues persist, change the host architecture.