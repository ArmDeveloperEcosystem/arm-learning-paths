UltraEdge Middleware

<span class="pill">Updated: 2025-11-01</span> <span class="pill">Skill:
Intermediate → Advanced</span> <span class="spacer"></span>

Contents

1.  [About](#1-about-this-learning-path--project)
2.  [Who is this for?](#2-who-is-this-for)
3.  [What will you learn?](#3-what-will-you-learn)
4.  [Prerequisites](#4-prerequisites)
5.  [Overview & Architecture](#5-overview--architecture)
6.  [Installation & Setup](#6-installation--setup)
7.  [MicroPac](#7-micropac)
8.  [Tinkerblox CLI](#8-tinkerblox-cli-usage-guide)
9.  [Troubleshooting](#9-troubleshooting)

# UltraEdge High-Performance Compute Infrastructure

Learning Path / User Guide • Reading time: ~20 min

## 1. About this Learning Path / Project

UltraEdge HPC-I is the execution fabric for AI & mixed workloads for
new-age compute infrastructure – automotive, smart products & technology
infrastructure industries.

UltraEdge forms the recommended edge architecture orchestration for
SOAFEE standard for software defined vehicles \[SDVs\]. UltraEdge
transforms HPC workload management with reduced workload package size,
lower resource utilization footprint and architecture-redefining
workload startup.

Smart product OEMs leverage UltraEdge to shorten time-to-market for new
products and to ‘AIoT-ize’ its existing install base of legacy products
with Plug-n-Play additions.

For technology infrastructure industry \[especially data centers\],
UltraEdge is pathbreaking in its ability to unlock under-utilized
compute power with the double whammy of higher performance at lower TCO.

## 2. Who is this for?

-   Business teams targeting lower TCO of computing infrastructure
    through higher utilization of CPU and/or CPU-GPU install bases .
-   R&D and Engineering teams looking for most efficient use of
    CPU/CPU-GPU infrastructure .
-   Innovation teams looking to maximize edge resources to host new-age
    AI on constrained environments.
-   Development teams looking at alternative packaging tech – run-time
    environments to build next generation workloads.

## 3. What will you learn?

By the end of this guide, you will be able to:

-   Understand the layered architecture of UltraEdge: **core**,
    **boost**, and **prime**.
-   Build applications using the **UltraEdge MicroStack**
-   Deploy the MicroPacs on **Linux-based compute systems** and scale to
    cloud or data-centre environments.
-   Optimize performance for **edge-cloud scenarios**, enabling near
    real-time data flows.

## 4. Prerequisites

Before starting, ensure you have:

-   Experience using **Linux** on embedded or SBC platforms.
-   Understanding of **container runtimes** (containerd) and **CNI
    networking**.
-   Basic knowledge of **communication protocols** (MQTT, HTTP, etc.).
-   *(Optional but helpful)* Familiarity with **edge-cloud
    architectures** and **data-flow orchestration**.

## 5. Overview & Architecture

## 5.1 Overview

UltraEdge was built with the vision of orchestrating the edge-native
execution fabric for high-performance compute infrastructure

-   UltraEdge is a ‘built-for-edge’ adaptive **AI & Mixed Workloads**
    execution stack built on the ethos of high performance, high
    fungibility & ultra-low footprint
-   Developed through strategic alliances with world-renowned technology
    powerhouses
-   Clear dual focus on Mixed workloads and new-age AI workloads
-   Full stack enablement through MicroStack & NeuroStack systems
-   Curated for AI@Edge with preferred edge deployment approach by Edge
    AI Foundation
-   Managed cluster” orchestration through integration with Kube-stack
    and/or Slurm
-   Observability for control plane, diagnostics & telemetry
-   Demonstrable value to customer through lower TCO of CPU-GPU clusters

### 5.2 High-Level Architecture

**UltraEdge ‘Core’ Layer **  
Handles compute infrastructure management including service
orchestration, lifecycle management, rule engine orchestration, and
data-flow management .

**UltraEdge ‘Boost’ Layer **  
Implements performance-critical routines and FFI (Foreign Function
Interface) calls; Contains dynamic connectors, and southbound protocol
adapters

**UltraEdge ‘Prime’ Layer **  
Contains business logic, trigger & activation sequences, and AI & mixed
workload orchestration .

**UltraEdge Edge-Cloud ‘Connect’ Layer **  
Supports data streaming to databases (InfluxDB, SQLite) and provides
diagnostic/logging outputs .

**UltraEdge Dock**  
Supports workload orchestration management through kube-stack or slurm.
.

## 6. Installation & Setup

### 6.1 System Requirements

-   Linux host (Aarch64 (arm64),armv7)

------------------------------------------------------------------------

### 6.2 Yocto

#### 6.2.1 Build Instructions

1.  Copy the `meta-tinkerblox` folder to your Yocto build environment.

2.  Add the layer:

        bitbake-layers add-layer <path-to-meta-tinkerblox>

3.  Build and flash the firmware to the target hardware.

#### 6.2.2 Activation of Agent

On the first boot, the agent will automatically generate a file named
`activation_key.json` at the path:

    /opt/tinkerblox/activation_key.json

Share this `activation_key.json` file with the TinkerBlox team to
receive license key (which includes license metadata).

1.  Stop the agent using the following command:

        sudo systemctl stop ultraedge.service

2.  Replace the existing `activation_key.json` file in
    `/opt/tinkerblox/` with the licensed one provided by TinkerBlox.

3.  Start the agent:

        sudo systemctl start ultraedge.service

#### 6.2.3 Manual Running

-   Binary path: `/opt/tinkerblox/Ultraedge/EdgeBloXagent`

-   To start:

        cd /opt/tinkerblox/Ultraedge
        ./EdgeBloXagent

-   To stop, press <span class="kbd">Ctrl</span> +
    <span class="kbd">C</span> once.

------------------------------------------------------------------------

### 6.3 Other Distributions

#### 6.3.1 Installation Process

-   Copy device installation details from **Uncloud**.
-   Device Initialization

    1.  Copy the command below into the clipboard.
    2.  Open terminal on your device.
    3.  Paste the copied command into terminal to initialize the device.
       
    Just an example code. You will find the exact to execute for your device in unclound
    ```bash
    sudo apt update && sudo apt install curl && sudo apt install jq -y && sudo DEVICE_ID="5b3ff290-0c88-4cd9-8ef7-08de0bded9df" KEY="TB.ApiKey-mlBZgDFc7qyM6ztPjILBCbFEqnVlbvjUpM1Q1IqNP6tA7wNdi97AQ==" sh -c "$(curl "https://tinkerbloxdev.blob.core.windows.net:443/tinkerbloxdev/binaries/installer.sh?sv=2025-01-05&st=2025-11-03T06%3A31%3A55Z&se=2025-11-03T06%3A56%3A55Z&sr=b&sp=r&sig=HNS70HgJyHlhCVQrqvpGdCcaf8%2FtVjdW4RNiiiIPCSUA%3D")"
    ```

-   Paste the copied content in the target terminal and execute.

#### 6.3.2 Activation of Agent

On the first boot, the agent will automatically generate a file named
`activation_key.json` at the path:

    /opt/tinkerblox/activation_key.json

Share this `activation_key.json` file with the TinkerBlox team to
receive license key (which includes license metadata).

1.  Stop the agent using the following command:

        sudo systemctl stop ultraedge.service

2.  Replace the existing `activation_key.json` file in
    `/opt/tinkerblox/` with the licensed one provided by TinkerBlox.

3.  Start the agent:

        sudo systemctl start ultraedge.service

#### 6.3.3 Manual Running

-   Binary path: `/usr/bin/EdgeBloXagent`

-   To start:

        EdgeBloXagent

-   To stop, press <span class="kbd">Ctrl</span> +
    <span class="kbd">C</span> once.

## 7. MicroPac

### 7.1 Prerequisites

#### 7.1.1 System Requirements

-   Linux host (aarch64)
-   Sudo permissions
-   Overlay filesystem support
-   Internet connection

#### 7.1.2 Required Packages

    sudo apt-get update
    sudo apt-get install -y tar curl qemu-user-static binfmt-support

------------------------------------------------------------------------

### Cross-Architecture Support

To build MicroPac for different architectures:

    
    # Enable binfmt for armv7
    sudo update-binfmts --enable qemu-armv7

------------------------------------------------------------------------

### 7.2 Installation

-   The package is provided as a `.deb` file.

-   Install it on your host machine:

        sudo apt install ./<package_name>.deb

### 7.3 MicroPac File Schema

Place a `MicroPacFile` in your project directory.

**Example Schema:**

    name: nginx
    version: 1.0.0.0
    target: aarch64
    applicationType: custom
    image: Alpine:3.21
    createdBy: developer@tinkerblox.io
    description: Nginx web server microservice

    buildSteps:
      # Install nginx and create necessary directories
      - run: apk add --no-cache nginx
      - run: mkdir -p /var/www/html /var/log/nginx /var/lib/nginx /var/tmp/nginx

      # Copy configuration files
      - copy: [nginx.conf, /etc/nginx/nginx.conf]
      - copy: [index.html, /var/www/html/index.html]
      - copy: [404.html, /var/www/html/404.html]

      # Copy startup script
      - workdir: /app
      - copy: [nginx_start.sh, .]
      - run: chmod +x ./nginx_start.sh

      # Set proper permissions
      #- run: chown -R nginx:nginx /var/www/html /var/log/nginx /var/lib/nginx /var/tmp/nginx

    entry: /app/nginx_start.sh
    mode: continuous-run

    env:
      NGINX_PORT: 8080
      APP_ENV: production

    network:
      mode: host
      name: nginx-net

### 7.3 Configuration Fields

#### Required Fields

-   **name**: Application name (≤ 10 characters)
-   **version**: Application version
-   **target**: Target architecture
-   **applicationType**: Application type (python, others)
-   **image**: Base image
-   **entry**: Entry point command
-   **mode**: single-run

#### Optional Fields

-   **env**: Environment variable
-   **buildSteps**: Array of build instructions
-   **limits**: Resource limits (memory, cpu)
-   **mount**: Volume mount points
-   **network**: Network configuration
-   **createdBy**: maintanier of the application
-   **description**: description of the application

### 7.4 Building the MicroPac

Navigate to your project directory and execute:

    sudo micropac-builder build

This generates a file named `<project_name>.mpac`.

## 8. Tinkerblox CLI Usage Guide

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

#### 1. Check CLI Connection Status

    sudo tinkerblox-cli status

*Displays whether the CLI is connected to the Edge Agent.*

#### 2. Microservice Management

Manage microservices running on the Edge platform.

**Syntax:**

    sudo tinkerblox-cli microboost <command> [options]

##### Available Commands

**install**  
Installs a microservice. You must provide the path to the MPAC file as
an argument.

    sudo tinkerblox-cli microboost install /path/to/your.mpac

**list**  
Lists all installed microservices.

    sudo tinkerblox-cli microboost list

**status \<id\>**  
Shows statistics (CPU, memory, status, etc.) for the specified
microservice.

    sudo tinkerblox-cli microboost status <id>

**stop \<id\>**  
Stops the microservice with the specified ID.

    sudo tinkerblox-cli microboost stop <id>

**start \<id\>**  
Starts the microservice with the specified ID (must be stopped).

    sudo tinkerblox-cli microboost start <id>

**uninstall \<id\>**  
Uninstalls the microservice with the specified ID.

    sudo tinkerblox-cli microboost uninstall <id>

#### 3. Diagnostics Management

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

## 9. Troubleshooting

**Permission Denied**

-   Ensure `sudo` privileges.
-   Check directory ownership and permissions.
-   Verify overlay filesystem support.

**Directory Creation Failed**

-   Check disk space.
-   Verify parent directory permissions.
-   Ensure the path is valid.

**Cross-Architecture Build Issues**

-   Verify QEMU installation:

        qemu-aarch64-static --version

-   Check binfmt registration:

        ls /proc/sys/fs/binfmt_misc/

-   Ensure the target architecture is enabled.

-   If issues persist, change the host architecture.
