---
title: TimescaleDB Environment Setup on Arm64
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## TimescaleDB Environment Setup

In this section, you prepare an Arm64-based SUSE Linux Enterprise Server (SLES) virtual machine and install TimescaleDB by building it from source. Building from source ensures the database extension is fully optimized for the Arm64 architecture, which is especially important for high-ingest and time-series workloads.

## Architecture Overview

```text
Linux ARM64 VM (SUSE)
        |
        v
PostgreSQL 15
        |
        v
TimescaleDB 2.25.0 Extension
```

TimescaleDB provides time-series optimizations on top of PostgreSQL, making it ideal for high-ingest sensor workloads.

## Install Build Dependencies (SUSE)

TimescaleDB must be compiled against PostgreSQL, so development headers and build tools are required.

```bash
sudo zypper refresh
```

```bash
sudo zypper install \
  cmake \
  gcc gcc-c++ make \
  git \
  libopenssl-devel \
  postgresql15 \
  postgresql15-server \
  postgresql15-devel
```

### Important (SUSE note)

If you are prompted about `readline-devel`, choose **Solution 1 (vendor change/downgrade)**.

**Why this matters:**

- This avoids dependency conflicts on SUSE.
- It ensures compatibility with PostgreSQL development libraries.

## Initialize PostgreSQL

Before using PostgreSQL, its data directory must be initialized.

```bash
sudo -u postgres initdb -D /var/lib/pgsql/data
```

**What this does:**

- Creates the PostgreSQL data directory.
- Initializes system tables and default configurations.
- Runs as the postgres system user for security.

**Enable and start PostgreSQL:**

```bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
```


**Verify PostgreSQL:**

```bash
psql --version
```

The output is similar to:
```output
psql (PostgreSQL) 15.10
```

## Build TimescaleDB from Source (ARM64)
Building TimescaleDB from source ensures native Arm64 compilation and optimal performance.

### Clone the repository

```bash
git clone https://github.com/timescale/timescaledb.git
cd timescaledb
git checkout 2.25.0
```

- Download the official TimescaleDB source code.
- Check out version 2.25.0 to ensure version consistency throughout the learning path

{{% notice Note %}}
According to the [release notes](https://github.com/timescale/timescaledb/releases/tag/2.16.0), TimescaleDB 2.16.0 introduces performance optimizations for DML on compressed chunks, improving upsert operations by **100×** and update/delete operations by **1000×** in some cases.  

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends **TimescaleDB 2.16.0** or higher for Arm platforms.
{{% /notice %}}

### Bootstrap and build:

```bash
./bootstrap
cd build
make -j$(nproc)
sudo make install
```
This compiles TimescaleDB natively for Arm64.

## Enable TimescaleDB in PostgreSQL
TimescaleDB must be preloaded when PostgreSQL starts.

### Edit PostgreSQL configuration

```bash
sudo vi /var/lib/pgsql/data/postgresql.conf
```

**Add:**

```text
shared_preload_libraries = 'timescaledb'
```
**What this does:**

- Ensures TimescaleDB is loaded when PostgreSQL starts.
-Required for advanced TimescaleDB features like background workers and compression.

### Restart PostgreSQL

```bash
sudo systemctl restart postgresql
```

## Create Database and Enable Extension
Now you enable TimescaleDB at the database level.

```bash
sudo -u postgres psql
```

```psql
CREATE DATABASE sensors;
\c sensors
CREATE EXTENSION IF NOT EXISTS timescaledb;
```
What this does:

- Creates a database named sensors.
- Switches to the sensors database.
- Enables TimescaleDB features within that database.

**Verify version:**

```psql
SELECT extversion FROM pg_extension WHERE extname='timescaledb';
```

The output is similar to:

```output
sensors=# SELECT extversion FROM pg_extension WHERE extname='timescaledb';
 extversion
------------
 2.25.0
(1 row)
```

**What this confirms:**

- TimescaleDB is installed correctly.
- The expected version is active in the database.

## What You Have Accomplished

- Installed PostgreSQL 15 on SUSE Arm64
- Built TimescaleDB 2.25.0 from source
- Enabled TimescaleDB at database level

## What’s Next

In the next section, you will create a real-time sensor ingestion pipeline using Python.
