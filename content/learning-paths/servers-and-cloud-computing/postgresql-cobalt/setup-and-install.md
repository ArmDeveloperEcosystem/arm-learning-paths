---
title: Install and configure PostgreSQL on Cobalt 200
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare PostgreSQL for Arm deployment

In this section, you install and configure PostgreSQL on an Azure Ubuntu 24.04 LTS Arm64 virtual machine running on Cobalt 200 processors.

At the end of this section, PostgreSQL is:

* Installed and running as a database service
* Accessible locally using an application user
* Ready for application workloads
* Configured with resource settings for the selected VM

## Update system

Refresh the package lists.

```bash
sudo apt update
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
psql (PostgreSQL) 16.15 (Ubuntu 16.15-0ubuntu0.24.04.1)
```

## Start PostgreSQL

Enable and start the PostgreSQL service.

```bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
sudo systemctl status postgresql@16-main
```
The cluster service should show `active (running)`. The parent `postgresql` service can show `active (exited)`; use the cluster service above to check the database process.

## Create database and user

Switch to the PostgreSQL superuser and create a database and application user.

```bash
sudo -u postgres psql
```

```sql
CREATE USER appuser WITH PASSWORD 'StrongPassword123';
CREATE DATABASE appdb OWNER appuser;
```

**Exit the PostgreSQL shell:**

```text
\q
```

Replace `StrongPassword123` with a strong password of your choice and use it for subsequent `appuser` connections.

## Validate local access

Keep PostgreSQL’s default local-only listener and host authentication settings. From your SSH session, connect over the loopback interface:

```console
psql -h localhost -U appuser -d appdb
```

Enter your application user’s password when prompted. At the `appdb=>` prompt, run:

```sql
SELECT current_user, current_database();
\q
```

You do not need to modify `listen_addresses`, add a network-wide authentication rule, or open port 5432 for this Learning Path.

## Performance tuning (ARM64)

The following starting settings match the **4-vCPU, 16-GiB Standard_D4ps_v7** VM. They are workload settings rather than architecture-specific optimizations. Reduce memory allocations if other services share the VM.

```console
sudo nano /etc/postgresql/16/main/postgresql.conf
```

Update the existing parameters or add them if absent:

```text
# Shared cache: 25% of the selected VM's memory.
shared_buffers = 4GB

# Per sort/hash operation; concurrent operations can multiply memory use.
work_mem = 16MB

# Memory for maintenance operations such as index creation.
maintenance_work_mem = 512MB

# Planner estimate of memory available for caching, not an allocation.
effective_cache_size = 12GB

# Parallel worker limits for the selected four-vCPU VM.
max_parallel_workers = 4
max_parallel_workers_per_gather = 2
```

**Restart PostgreSQL:**

```bash
sudo systemctl restart postgresql
```

## What you've learned and what's next

You've successfully installed and configured PostgreSQL on an Azure Ubuntu Arm64 virtual machine. Your setup includes:

- PostgreSQL is installed and running as a system service
- Database and application user configured
- Local application connectivity validated
- Resource settings aligned with the selected VM

Next, you'll create database schemas, load data, and run transactional and analytical queries.
