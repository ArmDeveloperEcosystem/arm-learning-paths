---
title: "Overview of Azure Cobalt 100 and Dynatrace"

weight: 2

layout: "learningpathall"
---

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads such as web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, which helps ensure consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## Dynatrace

Dynatrace is an AI-powered observability and application performance monitoring (APM) platform used to monitor applications, infrastructure, logs, and user experience across cloud and on-premises environments. Dynatrace provides automatic discovery, full-stack monitoring, and real-time analytics to help teams understand system behavior and quickly identify performance issues.

Dynatrace automatically maps dependencies between services, hosts, containers, and applications using intelligent automation and topology mapping. The platform uses AI-driven analysis to detect anomalies and identify root causes across complex distributed systems.

There are three main components of Dynatrace:

- **Dynatrace OneAgent:** a lightweight monitoring agent installed on hosts that automatically collects metrics, logs, and traces from applications and infrastructure. Learn more in the [Dynatrace OneAgent documentation](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent). 

- **Dynatrace ActiveGate:** a secure gateway component that routes monitoring traffic, enables cloud integrations, and provides additional monitoring capabilities such as Kubernetes monitoring and synthetic monitoring. Learn more in the [Dynatrace ActiveGate documentation](https://docs.dynatrace.com/docs/ingest-from/dynatrace-activegate).

- **Dynatrace Platform (SaaS or Managed):** the central observability platform that processes monitoring data, provides dashboards, AI-driven root cause analysis, and system-wide visibility across applications and infrastructure. See the [Dynatrace documentation portal](https://docs.dynatrace.com/docs) for more details.
