---
title: Arm Linux Migration Tools

additional_search_terms:
- migration
- porting
- analysis
- containers
- arm64
- aarch64
- sysreport
- skopeo
- llvm-mca
- topdown-tool
- kubearchinspect
- migrate-ease
- aperf
- bolt
- papi
- perf
- processwatch
- check-image
- porting-advisor

minutes_to_complete: 20

author: Jason Andrews

official_docs: https://github.com/arm/arm-linux-migration-tools

test_images:
- ubuntu:latest
test_maintenance: true
test_link: null

layout: installtoolsall
tool_install: true
multi_install: false
multitool_install_part: false
weight: 1
---

[Arm Linux Migration Tools](https://github.com/arm/arm-linux-migration-tools) provides a comprehensive collection of 13 essential utilities to help you migrate applications from x86 to Arm Linux systems. Instead of installing and managing each tool individually, get everything you need in a single, streamlined installation.

This package includes code analysis, performance, and migration tools such as Sysreport, Skopeo, LLVM Machine Code Analyzer, Telemetry Solution, KubeArchInspect, Migrate Ease, Aperf, BOLT, PAPI, Perf, Process Watch, Check Image, and Porting Advisor for Graviton. These tools assess application compatibility, analyze performance characteristics, optimize code layout, and identify potential issues before and after migration.

Whether you're migrating containerized applications, analyzing system performance, or optimizing binaries for Arm processors, this package simplifies your migration workflow by providing all necessary tools through a unified installation process. 

## What are the tools included in Arm Linux Migration Tools? 

The Arm Linux Migration Tools package includes the following utilities:

| Tool | Purpose | Test Command | Documentation |
|------|---------|--------------|---------------|
| Sysreport | System analysis and reporting tool for performance and configuration checks | `sysreport --help` | [Get ready for performance analysis with Sysreport](/learning-paths/servers-and-cloud-computing/sysreport/) |
| Skopeo | Container image inspection and manipulation tool | `skopeo --help` | [Skopeo install guide](/install-guides/skopeo/) |
| LLVM Machine Code Analyzer | Machine Code Analyzer for performance analysis of compiled code | `llvm-mca --help` | [Learn about LLVM Machine Code Analyzer](/learning-paths/cross-platform/mca-godbolt/) |
| Telemetry Solution | Performance analysis methodology tool for Linux systems | `topdown-tool --help` | [Telemetry Solution](/install-guides/topdown-tool/) |
| KubeArchInspect | Kubernetes architecture inspection and reporting tool | `kubearchinspect --help` | [Migrate containers to Arm using KubeArchInspect](/learning-paths/servers-and-cloud-computing/kubearchinspect/) |
| Migrate Ease | Migration assistance tool for analyzing and porting workloads | `migrate-ease-cpp --help` | [Migrate applications to Arm servers using migrate-ease](/learning-paths/servers-and-cloud-computing/migrate-ease/) |
| Aperf | Performance monitoring tool for Linux systems | `aperf --help` | [Aperf install guide](/install-guides/aperf/) |
| BOLT | Binary optimization and layout tool (part of LLVM) | `llvm-bolt --help` | [BOLT install guide](/install-guides/bolt/) |
| PAPI | Performance API for accessing hardware performance counters | `papi_avail -h` | [PAPI install guide](/install-guides/papi/) |
| Perf | Linux performance analysis tool for profiling and tracing | `perf --help` | [Perf install guide](/install-guides/perf/) |
| Process Watch | Process monitoring tool for Linux systems | `processwatch -h` | [Run Process watch on your Arm machine](/learning-paths/servers-and-cloud-computing/processwatch/) |
| Check Image | Checks a container image for Arm architecture support | `check-image -h` | [Check Image on learn.arm.com](/learning-paths/cross-platform/docker/check-images/) |
| Porting Advisor for Graviton | Tool to assess portability of software to Arm architecture | `porting-advisor --help` | [Porting Advisor install guide](/install-guides/porting-advisor/) |

Each tool serves a specific purpose in the migration process, from analyzing system configurations and performance characteristics to optimizing binaries and checking container compatibility. 

## Prerequisites

Before installing the Arm Linux Migration Tools, verify that your system meets the following requirements:

### Architecture verification

This package is designed for Arm Linux systems. Verify that you're running on the Arm architecture:

```bash
uname -m
```

The output should be `aarch64`. If you see `x86_64` or another architecture, this package isn't compatible with your system.

### Operating system support

The Arm Linux Migration Tools package supports Ubuntu 22.04 and Ubuntu 24.04. 

### Required dependencies

Some tools in the package require additional software to function properly:

Docker or Podman is required for Migrate Ease. You can install Docker with the [Docker install guide](/install-guides/docker/docker-engine).

Alternatively, if you prefer Podman over Docker, install it with the Ubuntu package manager:

```bash
sudo apt install -y podman
```

## Installation

The Arm Linux Migration Tools package provides multiple installation methods to suit different preferences and environments. Choose the method that works best for your setup.

### Option 1: Single-line installation

The fastest way to install the Arm Linux Migration Tools is with the automated installation script. This method downloads and installs the latest release automatically:

```bash
curl -sSL https://github.com/arm/arm-linux-migration-tools/releases/download/v3/install.sh | sudo bash
```

The command above performs the following actions:
- Downloads the installation script `install.sh` from the GitHub repository
- Automatically detects your system architecture 
- Installs required dependencies using the package manager
- Downloads the appropriate release package for your system
- Installs the included tools in `/opt/arm-migration-tools/`
- Creates wrapper scripts in `/usr/local/bin` for easy access
- Configures a Python virtual environment with the required dependencies

The installation script prompts for your password when `sudo` access is required for copying files to system directories. 

If this is your first install, review the script before running it with `curl | bash`.

```console
curl -fsSL https://github.com/arm/arm-linux-migration-tools/releases/download/v3/install.sh | more
```

This command displays the script so you can verify what it does before executing it.

### Option 2: Download and install 

For manual installation, download the release tar file for a specific version from GitHub and install it.

Download the latest release file with `wget`:

```bash
wget https://github.com/arm/arm-linux-migration-tools/releases/download/v3/arm-migration-tools-v3-arm64.tar.gz
```

Extract the downloaded tar file to a temporary directory:

```bash
tar xvfz arm-migration-tools-v3-arm64.tar.gz
```

Navigate to the extracted directory and run the installation script:

```bash
cd arm-linux-migration-tools
sudo ./scripts/install.sh
```

After successful installation, remove the downloaded files:

```bash
cd ..
rm -rf arm-linux-migration-tools arm-migration-tools-v3-arm64.tar.gz
```

### Option 3: Build from source

To build the Arm Linux Migration Tools from source code, clone the repository and build it locally. This method is useful for developers who want to modify the tools or contribute to the project.

First, clone the GitHub repository to your local system:

```bash
git clone https://github.com/arm/arm-linux-migration-tools.git
```

Change to the cloned repository directory:

```bash
cd arm-linux-migration-tools
```

Run the build script to compile and prepare all tools:

```console
./scripts/build.sh
```

The build script performs the following tasks:
- Downloads and compiles source code for the tools that have source
- Resolves dependencies and builds binaries
- Creates the directory structure for installation
- Prepares a Python virtual environment and installs required packages
- Validates that all tools build successfully

After a successful build, install the tools to your system:

```console
sudo ./scripts/install.sh
```

The install script:
- Installs the locally built tools to `/opt/arm-migration-tools/`
- Creates wrapper scripts in `/usr/local/bin` for easy access
- Sets up the Python virtual environment with the built dependencies
- Configures permissions for all installed components

After successful installation, clean up the build directory:

```bash
cd ..
rm -rf arm-linux-migration-tools
```

## Installation locations

After successful installation, the Arm Linux Migration Tools are organized in a structured directory layout that separates the core tools, dependencies, and user-accessible commands. Understanding this structure helps you troubleshoot issues and manage the installation effectively.

All tools and their dependencies are installed in the `/opt/arm-migration-tools/` directory:

```bash
ls /opt/arm-migration-tools/
```

For easy access from anywhere in your system, wrapper scripts are installed in `/usr/local/bin/`:

```bash
ls /usr/local/bin/ | grep -E "(sysreport|skopeo|llvm-mca|topdown-tool|kubearchinspect|migrate-ease|aperf|llvm-bolt|papi|perf|processwatch|check-image|porting-advisor)"
```

### Python virtual environment

A Python virtual environment is located at `/opt/arm-migration-tools/venv/` and contains all Python packages required by the migration tools.

The wrapper scripts in `/usr/local/bin` use this environment automatically. To activate it manually:

```bash
source /opt/arm-migration-tools/venv/bin/activate
```

View the installed Python packages in the virtual environment:

```bash
/opt/arm-migration-tools/venv/bin/pip list
```

The output is similar to:

```output
Package                   Version    Editable project location
------------------------- ---------- --------------------------------------------------------------
altgraph                  0.17.3
annotated-types           0.7.0
attrs                     25.4.0
blinker                   1.9.0
certifi                   2025.11.12
charset-normalizer        3.4.4
click                     8.3.1
Flask                     3.1.2
gitdb                     4.0.12
GitPython                 3.1.45
idna                      3.11
itsdangerous              2.2.0
Jinja2                    3.1.4
jsonschema                4.25.1
jsonschema-specifications 2025.9.1
lxml                      5.3.2
markdown-it-py            4.0.0
MarkupSafe                2.1.3
mdurl                     0.1.2
packaging                 23.1
pip                       25.3
progressbar33             2.4
pycryptodome              3.19.1
pydantic                  2.11.7
pydantic_core             2.33.2
Pygments                  2.19.2
pyparsing                 3.1.1
python-magic              0.4.27
referencing               0.37.0
requests                  2.32.5
rich                      14.1.0
rpds-py                   0.30.0
ruamel.yaml               0.18.16
ruamel.yaml.clib          0.2.15
smmap                     5.0.2
topdown-tool              1.0.0      /opt/arm-migration-tools/telemetry-solution/tools/topdown_tool
typing_extensions         4.15.0
typing-inspection         0.4.2
urllib3                   2.6.2
uuid                      1.30
Werkzeug                  3.1.4
XlsxWriter                3.1.2
```

## Verify installation

After installing the Arm Linux Migration Tools, verify that all tools are working correctly. The package includes a comprehensive test script to validate your installation.

Execute the included test script to verify all 13 tools are properly installed and functional:

```bash
/opt/arm-migration-tools/scripts/arm-migration-tools-test.sh 
```

The script performs a basic invocation of each tool to confirm it runs.

{{% notice Note %}}
If you get an error when running Topdown Tool, run these commands:
```console
sudo sh -c "echo -1 > /proc/sys/kernel/perf_event_paranoid"
sudo sh -c "echo 0 > /proc/sys/kernel/kptr_restrict"
```
For more information about these options, see the [Linux Perf install guide](/install-guides/perf/).
{{% /notice %}}

## Next steps

Now that you have successfully installed and verified the Arm Linux Migration Tools, you're ready to begin.

You can review the [Arm Migration overview](/migration/) for additional guidance.

## Uninstall

If you need to remove the Arm Linux Migration Tools from your system, use the included uninstall script. This process completely removes all installed components and restores your system to its previous state.

To uninstall the Arm Linux Migration Tools package, run the uninstall script:

```bash
sudo /opt/arm-migration-tools/scripts/uninstall.sh
```

The uninstall script performs the following tasks:
- Removes all tools from `/opt/arm-migration-tools/` directory
- Deletes all wrapper scripts from `/usr/local/bin/`
- Removes the Python virtual environment and all installed dependencies
