---
title: Get started with TimescaleDB on Google Axion C4A 

weight: 2

layout: "learningpathall"
---

## Explore Axion C4A Arm instances in Google Cloud

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability and performance benefits of the Arm architecture in Google Cloud.

To learn more, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).


## Explore TimescaleDB on Google Axion C4A (Arm Neoverse V2)

TimescaleDB is a high-performance, open-source time-series database built on PostgreSQL. It provides powerful features for storing, querying, and analyzing time-series data efficiently, making it ideal for IoT, telemetry, financial, and observability workloads.

TimescaleDB enables developers to handle large volumes of time-stamped data with features like hypertables, continuous aggregates, retention policies, and automated data partitioning, while maintaining full SQL compatibility.

Running TimescaleDB on Google Axion C4A Arm-based infrastructure allows you to achieve high-throughput time-series ingestion and query processing with optimized performance per watt, lower infrastructure costs, and better scalability for distributed workloads.

Common use cases include real-time monitoring of IoT sensors, event-driven analytics, DevOps metrics collection, financial time-series analysis, and building dashboards with tools like Grafana for live visualization.

To learn more, visit the [TimescaleDB website](https://www.timescale.com/) and explore the [TimescaleDB documentation](https://docs.timescale.com/).


## What You've Accomplished and What's Next

In this section, you learned about:
- Google Axion C4A Arm-based VMs and their performance advantages for time-series workloads  
- TimescaleDB and its key features, including hypertables, continuous aggregates, and retention policies  
- How Arm architecture enables cost-efficient, high-throughput ingestion and query processing for time-series data  

Next, you'll install Grafana, connect TimescaleDB as a data source, and create a live sensor temperature dashboard to visualize real-time time-series data.
