---
title: Get started with OpenTelemetry on Google Axion C4A 

weight: 2

layout: "learningpathall"
---

## Explore Axion C4A Arm instances in Google Cloud

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability and performance benefits of the Arm architecture in Google Cloud.

To learn more, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).


## Explore OpenTelemetry on Google Axion C4A (Arm Neoverse V2)

OpenTelemetry is an open-source observability framework that provides standardized APIs, SDKs, and tools for collecting telemetry data such as traces, metrics, and logs from cloud-native applications. It is a CNCF (Cloud Native Computing Foundation) project and is widely adopted for building vendor-neutral observability solutions.

OpenTelemetry enables developers to instrument applications once and export telemetry data to multiple backend systems including Prometheus, Grafana, Jaeger, Zipkin, and cloud monitoring platforms.

Running OpenTelemetry on Google Axion C4A Arm-based infrastructure allows you to achieve high-throughput telemetry processing with improved performance per watt and reduced infrastructure costs, making it ideal for modern distributed systems.

Common use cases include application performance monitoring (APM), distributed tracing, infrastructure metrics collection, log aggregation, and monitoring microservices architectures.

To learn more, visit the [OpenTelemetry website](https://opentelemetry.io/) and explore the [OpenTelemetry documentation](https://opentelemetry.io/docs/).

## What you've accomplished and what's next

In this section, you learned about:

* Google Axion C4A Arm-based VMs and their performance characteristics
* OpenTelemetry observability framework and its role in modern cloud-native monitoring
* How Arm architecture enables cost-effective, high-performance telemetry processing  

Next, you'll configure firewall rules and network access to allow external communication between your OpenTelemetry components and monitored services.
