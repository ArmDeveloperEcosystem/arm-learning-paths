---
title: Setup and Install PostgreSQL on Cobalt 100
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Setup and Install PostgreSQL on Cobalt 100 (Arm64)

In this section, you install and configure PostgreSQL on an Azure Ubuntu 24.04 Pro Arm64 virtual machine running on Cobalt 100 processors.

At the end of this section, PostgreSQL is:

* Installed and running as a database service
* Configured for remote access
* Ready for application workloads
* Tuned for Arm64 performance

## Update system

Update the operating system to ensure all packages are current.

```bash
sudo apt update && sudo apt upgrade -y
```

## Install PostgreSQL

Install PostgreSQL and additional contributed modules.

```bash
sudo apt install -y postgresql postgresql-contrib
```

## Verify installation

Confirm PostgreSQL is installed correctly.

```bash
psql --version
```

The output is similar to:

```output
psql (PostgreSQL) 16.13 (Ubuntu 16.13-0ubuntu0.24.04.1)
```

## Start PostgreSQL

Enable and start the PostgreSQL service.

```bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
sudo systemctl status postgresql
```
The service should be active and running.

## Create database and user

Switch to the PostgreSQL superuser and create a database and application user.

```bash
sudo -u postgres psql
```

```sql
CREATE USER appuser WITH PASSWORD 'StrongPassword123';
CREATE DATABASE appdb OWNER appuser;
GRANT ALL PRIVILEGES ON DATABASE appdb TO appuser;
```

**Exit the PostgreSQL shell:**

```bash
\q
```

## Enable remote access

Edit the PostgreSQL configuration file.

```bash
sudo nano /etc/postgresql/16/main/postgresql.conf
```

**Search for listen_addresses and update it as follows:**

- listen_addresses = '*'

## Edit authentication:

Edit the host-based authentication file.

```bash
sudo nano /etc/postgresql/16/main/pg_hba.conf
```

**Add the following line:**

```text
host    all     all     0.0.0.0/0     md5
```

**Restart PostgreSQL to apply changes:**

```bash
sudo systemctl restart postgresql
```

## Performance tuning (ARM64)

Tune PostgreSQL settings to better utilize Cobalt 100 resources.

```bash
sudo nano /etc/postgresql/16/main/postgresql.conf
```

**Update or add the following parameters:**

```text
# Controls how much memory PostgreSQL uses for caching data pages.
# Set to 25-40% of total RAM. A 2GB shared buffer suits a VM with 8GB RAM.
shared_buffers = 2GB

# Memory allocated per sort or hash operation within a query.
# Higher values improve complex sort and hash join performance.
work_mem = 64MB

# Memory for maintenance operations such as VACUUM and CREATE INDEX.
# A larger value speeds up index builds and table maintenance.
maintenance_work_mem = 512MB

# Planner estimate of the total memory available for caching.
# Helps the planner choose index scans over sequential scans.
# Set to 75% of total RAM.
effective_cache_size = 6GB

# Maximum number of background parallel workers across all queries.
# Match this to the number of vCPUs on the Cobalt 100 instance.
max_parallel_workers = 8

# Maximum parallel workers a single query can use.
# Cobalt 100 dedicates one physical core per vCPU, so 4 workers
# lets queries use half the cores without contention.
max_parallel_workers_per_gather = 4
```

**Restart PostgreSQL:**

```bash
sudo systemctl restart postgresql
```

## What you've accomplished and what's next

You've successfully installed and configured PostgreSQL on an Azure Ubuntu Arm64 virtual machine. Your setup includes:

- PostgreSQL is installed and running as a system service
- Database and application user configured
- Remote connectivity enabled
- Performance tuning applied to Arm64 systems

Next, you'll create database schemas, load data, and run transactional and analytical queries.
