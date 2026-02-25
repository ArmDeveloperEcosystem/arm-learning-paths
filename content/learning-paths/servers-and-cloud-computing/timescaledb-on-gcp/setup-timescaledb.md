---
title: Set up TimescaleDB on Arm64
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the TimescaleDB environment

In this section, you prepare an Arm64-based SUSE Linux Enterprise Server (SLES) virtual machine and install TimescaleDB by building it from source. Building from source ensures the database extension is fully optimized for Arm64, which is especially important for high-ingest and time-series workloads.

## Architecture overview

```text
Linux Arm64 VM (SUSE)
        |
        v
PostgreSQL 15
        |
        v
TimescaleDB 2.25.0 Extension
```

TimescaleDB provides time-series optimizations on top of PostgreSQL, making it ideal for high-ingest sensor workloads.

## Install build dependencies

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
  postgresql15-server-devel \
  postgresql15-devel
```

{{% notice Note %}}If you are prompted about `readline-devel`, choose **Solution 1 (vendor change/downgrade)**. This avoids dependency conflicts on SUSE and ensures compatibility with PostgreSQL development libraries.{{% /notice %}}

## Initialize PostgreSQL

Before using PostgreSQL, its data directory must be initialized. The following command runs as the `postgres` system user to create the data directory, initialize system tables, and set default configurations:

```bash
sudo -u postgres initdb -D /var/lib/pgsql/data
```

Enable and start PostgreSQL:

```bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
```


Verify PostgreSQL is running:

```bash
psql --version
```

The output is similar to:

```output
psql (PostgreSQL) 15.10
```

## Build TimescaleDB from source

Building TimescaleDB from source ensures native Arm64 compilation and optimal performance.

### Clone the repository

Download the official TimescaleDB source code and check out version 2.25.0 to ensure version consistency throughout this Learning Path:

```bash
git clone https://github.com/timescale/timescaledb.git
cd timescaledb
git checkout 2.25.0
```

{{% notice Note %}}
According to the [release notes](https://github.com/timescale/timescaledb/releases/tag/2.16.0), TimescaleDB 2.16.0 introduces performance optimizations for DML on compressed chunks, improving upsert operations by **100×** and update/delete operations by **1000×** in some cases.  

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends **TimescaleDB 2.16.0** or higher for Arm platforms.
{{% /notice %}}

### Bootstrap the configuration

```bash
./bootstrap
```

### Invoke the build

```bash
cd build
make -j$(nproc)
sudo make install
```

This compiles TimescaleDB natively for Arm64.

## Enable TimescaleDB in PostgreSQL

TimescaleDB must be preloaded when PostgreSQL starts.

### Edit PostgreSQL configuration and add the timescaledb library

Using a suitable editor and "sudo", edit **/var/lib/pgsql/data/postgresql.conf** and add the following line:

```text
shared_preload_libraries = 'timescaledb'
```

This update:

- Ensures TimescaleDB is loaded when PostgreSQL starts.
- Required for advanced TimescaleDB features like background workers and compression.

### Restart PostgreSQL

```bash
sudo systemctl restart postgresql
```

## Create a database and enable the extension

Enable TimescaleDB at the database level by creating the `sensors` database and loading the extension:

```bash
sudo -u postgres psql
```

```psql
CREATE DATABASE sensors;
\c sensors
CREATE EXTENSION IF NOT EXISTS timescaledb;
```

Verify the installed version:

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

Press Ctrl+D to exit.

This confirms that TimescaleDB is installed correctly and the expected version is active.

## What you've accomplished and what's next

You've successfully:

- Installed PostgreSQL 15 on SUSE Arm64
- Built TimescaleDB 2.25.0 from source for optimal Arm64 performance
- Enabled TimescaleDB at the database level and verified the installation

Next, you'll create a real-time sensor data ingestion pipeline using Python to continuously insert time-series data into TimescaleDB.
