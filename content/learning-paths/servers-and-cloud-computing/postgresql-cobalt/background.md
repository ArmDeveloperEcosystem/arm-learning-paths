---
title: Understand PostgreSQL on Azure Cobalt 200

weight: 2

layout: "learningpathall"
---

## Why run PostgreSQL on Azure Cobalt 200

PostgreSQL provides Arm64 packages for Linux, allowing you to run transactional and analytical queries on Azure Cobalt 200 virtual machines. In this Learning Path, you deploy PostgreSQL on a general-purpose **Standard_D4ps_v7** VM and validate it with sample data and a local benchmark.

## Azure Cobalt 200 Arm-based processor

Azure Cobalt 200 is Microsoft’s second-generation Arm-based processor, built on Arm Neoverse Compute Subsystems V3 (CSS V3). It supports cloud-native Linux workloads, including relational databases such as PostgreSQL.

To learn more, see Microsoft’s [introduction to Azure Cobalt 200 virtual machines](https://azure.microsoft.com/en-us/blog/new-azure-cobalt-200-vms-deliver-50-performance-improvement-fully-optimized-for-modern-agentic-ai-workloads/).

## PostgreSQL

PostgreSQL is a powerful, open-source relational database management system (RDBMS) known for its reliability, extensibility, and performance. It is widely used for transactional (OLTP) and analytical (OLAP) workloads across modern applications.

Learn more in the [PostgreSQL documentation](https://www.postgresql.org/docs/).

PostgreSQL supports advanced features such as:

- ACID-compliant transactions for data consistency
- Complex queries, joins, and aggregations
- Indexing and query optimization
- Extensibility with custom functions and extensions
- Support for JSON and semi-structured data

These capabilities make PostgreSQL suitable for a wide range of use cases, including:

- Web and mobile application backends
- Financial and transactional systems
- Analytics and reporting workloads
- Data warehousing and hybrid workloads

## Key PostgreSQL components

PostgreSQL consists of several core components that work together to manage data efficiently:

- **PostgreSQL Server:**
  The main database engine is responsible for processing queries, managing data storage, and handling client connections.

- **Client Tools (psql):**
  Command-line interface used to interact with the database, execute queries, and manage database objects.

- **Storage Engine:**
  Handles how data is stored on disk, including tables, indexes, and write-ahead logging (WAL) for durability and crash recovery.

- **Query Planner and Executor:**
  Optimizes SQL queries and determines the most efficient way to execute them.

- **Extensions (for example, pg_stat_statements) and tools (for example, pgbench):**
  Provide additional functionality such as performance monitoring and benchmarking.


## PostgreSQL on Arm (Cobalt 200)

You use the same SQL syntax and PostgreSQL tools on Arm64 as on other supported architectures. This Learning Path establishes a functional baseline on Cobalt 200; performance depends on the VM size, storage, configuration, and workload.

## What this learning path covers

In this learning path, you will:

- Install and configure PostgreSQL on Azure Cobalt 200 Arm64 virtual machines
- Deploy a relational schema for transactional workloads
- Run analytical queries on operational data
- Benchmark PostgreSQL performance using pgbench
- Monitor and optimize query execution

By the end, you will have a fully functional PostgreSQL deployment configured and benchmarked on Arm-based cloud infrastructure.
