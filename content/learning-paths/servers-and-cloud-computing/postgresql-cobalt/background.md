---
title: "Overview of Azure Cobalt 100 and PostgreSQL"

weight: 2

layout: "learningpathall"
---

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads such as web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, which helps ensure consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

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

- **Extensions (for example, pg_stat_statements, pgbench):**  
  Provide additional functionality such as performance monitoring and benchmarking.


## PostgreSQL on Arm (Cobalt 100)

Running PostgreSQL on Arm-based processors like Cobalt 100 provides several advantages:

- Efficient CPU utilization with dedicated cores per vCPU  
- Improved performance per watt for database workloads  
- Strong performance for parallel query execution  
- Cost-effective scaling for cloud-native applications  

PostgreSQL’s multi-process architecture and parallel execution capabilities align well with Arm-based infrastructure, making it a strong choice for modern cloud deployments.

## What this learning path covers

In this learning path, you will:

- Install and configure PostgreSQL on Azure Cobalt 100 Arm64 virtual machines  
- Deploy a relational schema for transactional workloads  
- Run analytical queries on operational data  
- Benchmark PostgreSQL performance using pgbench  
- Monitor and optimize query execution  

By the end, you will have a fully functional PostgreSQL deployment optimized for Arm-based cloud environments.
