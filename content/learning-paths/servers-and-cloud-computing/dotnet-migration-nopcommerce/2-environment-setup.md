---
title: Set up an Arm-based environment
description: Set up an Ubuntu Azure Cobalt VM with Docker, .NET 9, and PostgreSQL so you can build and validate nopCommerce on Arm.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up a Microsoft Azure virtual machine powered by Cobalt 100

Set up an Arm Azure environment first, then keep your toolchain and runtime configuration stable across all test runs. This creates a reliable Arm baseline for migration and tuning work.

Start with the [Azure Cobalt Learning Path](https://learn.arm.com/learning-paths/servers-and-cloud-computing/cobalt/) and complete VM provisioning.

The Learning Path was validated with Ubuntu 24.04 LTS on Azure Cobalt in `westus2` (example VM size: `Standard_D2ps_v6`, 2 vCPUs).

### Install tools on the Azure virtual machine

Install the toolchain on the Azure VM before building and testing. 

The following commands install the Linux packages used throughout this Learning Path: source control, HTTP validation, JSON inspection, Python for the endpoint tester, package archive inspection, Docker, and the .NET 9 SDK from the Ubuntu backports feed:

```bash
sudo apt-get update -y
sudo apt-get install -y git curl jq python3 ripgrep unzip ca-certificates gnupg software-properties-common docker.io
sudo usermod -aG docker "$USER"

sudo add-apt-repository ppa:dotnet/backports -y
sudo apt-get update -y
sudo apt-get install -y dotnet-sdk-9.0
```

The Docker group change applies to new login sessions. Sign out and sign back in before running Docker without `sudo`, or run `newgrp docker` in the current terminal before continuing.

Confirm architecture and tool versions before proceeding: 

```bash
uname -m
dotnet --version
docker --version
```
On Azure Cobalt, the Linux machine architecture should be `aarch64`, and the .NET SDK should be a `9.0.x` release.

The output is similar to:

```output
aarch64
9.0.x
Docker version ...
```

If you're upgrading from an older .NET version before migrating to Cobalt, use [GitHub Copilot modernization for .NET](https://learn.microsoft.com/dotnet/core/porting/github-copilot-app-modernization/overview) to assess the project and guide the upgrade. In Visual Studio Code, open Copilot Chat and use `@modernize-dotnet`. In Visual Studio, use the **Modernize** action from **Solution Explorer**.

### Enable citext to satisfy PostgreSQL prerequisite 

nopCommerce defaults to SQL Server, but you'll use PostgreSQL for Arm validation. For PostgreSQL installs, you need `citext` before migration and installation. Without it, installer migrations fail with `type "citext" does not exist` (captured in local test artifacts).

Create PostgreSQL and enable `citext` before running the installer. The database runs in Docker on the VM so the nopCommerce app can connect to `127.0.0.1:5432` during the local validation phase. 

Replace the password value before running the following commands:

```bash
export NOP_POSTGRES_PASSWORD='replace-with-a-strong-password'

# Start PostgreSQL for local validation.
docker run -d --name nop-postgres \
  -e POSTGRES_USER=nop \
  -e POSTGRES_PASSWORD="$NOP_POSTGRES_PASSWORD" \
  -e POSTGRES_DB=nopcommerce \
  -p 5432:5432 postgres:16

# Enable the extension required by nopCommerce migrations.
docker exec nop-postgres psql -U nop -d nopcommerce \
  -c "CREATE EXTENSION IF NOT EXISTS citext;"
```

The `docker exec` command should print `CREATE EXTENSION`. If it prints `NOTICE: extension "citext" already exists, skipping`, the database is already prepared and you can continue.

## What you've accomplished and what's next

You've set up an Arm-based environment by creating a Microsoft Azure VM powered by Cobalt 100 with Docker, .NET 9, and PostgreSQL ready for nopCommerce validation. 

Next, you'll create a reproducible baseline to use for benchmarking.
