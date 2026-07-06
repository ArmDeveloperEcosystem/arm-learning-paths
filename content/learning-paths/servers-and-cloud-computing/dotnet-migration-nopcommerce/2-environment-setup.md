---
title: Environment setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Environment setup

Set up an Arm Cobalt environment first, then keep your toolchain and runtime configuration stable across all test runs. This creates a reliable Arm baseline for migration and tuning work.

Start with the official [Azure Cobalt setup guide](https://learn.arm.com/learning-paths/servers-and-cloud-computing/cobalt/) and complete VM provisioning there first.

This path was validated with Ubuntu 24.04 LTS on Azure Cobalt in `westus2` (example VM size: `Standard_D2ps_v6`, 2 vCPUs).

## Install tools on Cobalt VM

Install the toolchain on the Cobalt VM before building and testing. The commands install the Linux packages used throughout this Learning Path: source control, HTTP validation, JSON inspection, Python for the endpoint tester, package archive inspection, Docker, and the .NET 9 SDK from the Ubuntu backports feed.

```bash
sudo apt-get update -y
sudo apt-get install -y git curl jq python3 ripgrep unzip ca-certificates gnupg software-properties-common docker.io
sudo usermod -aG docker "$USER"

sudo add-apt-repository ppa:dotnet/backports -y
sudo apt-get update -y
sudo apt-get install -y dotnet-sdk-9.0
```

The Docker group change applies to new login sessions. Sign out and sign back in before running Docker without `sudo`, or run `newgrp docker` in the current terminal before continuing.

Confirm architecture and tool versions before proceeding. On Azure Cobalt, the Linux machine architecture should be `aarch64`, and the .NET SDK should be a 9.0.x release.

```bash
uname -m
dotnet --version
docker --version
```

The output is similar to:

```output
aarch64
9.0.x
Docker version ...
```

If you are upgrading from an older .NET version before migrating to Cobalt, you can use [GitHub Copilot modernization for .NET](https://learn.microsoft.com/dotnet/core/porting/github-copilot-app-modernization/overview) to assess the project and guide the upgrade. In Visual Studio Code, open Copilot Chat and use `@modernize-dotnet`; in Visual Studio, use the Modernize action from Solution Explorer.

## PostgreSQL prerequisite for nopCommerce install

nopCommerce defaults to SQL Server, but this learning path uses PostgreSQL for Arm validation. For PostgreSQL installs, `citext` is required before migration/installation. Without it, installer migrations fail with `type "citext" does not exist` (captured in local test artifacts).

Create PostgreSQL and enable `citext` before running the installer. The database runs in Docker on the Cobalt VM so the nopCommerce app can connect to `127.0.0.1:5432` during the local validation phase. Replace the password value before running the command.

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
