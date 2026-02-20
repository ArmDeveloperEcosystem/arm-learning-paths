---
title: Create firewall rules on GCP for Flask and observability components
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure GCP firewall for OpenTelemetry

To allow inbound traffic for the Flask application and observability components, you must create a firewall rule in the Google Cloud Console.

{{% notice Note %}} For more information about GCP setup, see [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).{{% /notice %}}

## Required ports

| Service | Port | Purpose |
| ------- | ---- | ------- |
| Flask Application | 8080 | Application traffic |
| Jaeger UI | 16686 | Trace visualization |
| Prometheus UI | 9090 | Metrics dashboard |
| OTLP gRPC | 4317 | Telemetry ingestion |
| OTLP HTTP | 4318 | Telemetry ingestion |
| Collector Metrics | 8889 | Prometheus scrape endpoint |

## Create a firewall rule in GCP

To expose the TCP ports listed above, create a firewall rule.

Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Google Cloud Console VPC Network Firewall page showing existing firewall rules and Create Firewall Rule button alt-txt#center](images/firewall-rule1.png "Create a firewall rule")

Next, create the firewall rule that exposes the TCP ports.
Set the **Name** of the new rule to `allow-all-opentelemetry`. Select the network you intend to bind to your VM (the default is `default`, but your organization may use a different one).

Set **Direction of traffic** to "Ingress". Set **Allow on match** to "Allow" and **Targets** to "Specified target tags".

![Google Cloud Console firewall rule creation form showing name field, network selection, direction set to Ingress, and targets set to Specified target tags alt-txt#center](images/network-rule2.png "Creating opentelemetry firewall rule")

Next, enter `allow-all-opentelemetry` in the **Target tags** field. Set **Source IPv4 ranges** to `0.0.0.0/0`.

![Google Cloud Console firewall rule form showing target tags field with allow-all-opentelemetry entered and source IPv4 ranges set to 0.0.0.0/0 alt-txt#center](images/network-rule3.png "Creating the Opentelemetry firewall rule")

Finally, select **Specified protocols and ports** under the **Protocols and ports** section. Select the **TCP** checkbox, enter `8080,16686,9090,4317,4318,8889` in the **Ports** field, and select **Create**.

![Google Cloud Console firewall rule form showing protocols and ports section with TCP selected and ports 8080,16686,9090,4317,4318,8889 specified alt-txt#center](images/network-port.png "Specifying TCP ports for OpenTelemetry")

## What you've accomplished and what's next

You've successfully:

- Created firewall rules in Google Cloud to expose ports for the Flask application and observability components
- Configured network access for Jaeger, Prometheus, and OpenTelemetry Collector endpoints
- Set up secure ingress rules for telemetry data collection

Next, you'll provision a Google Axion C4A Arm virtual machine and apply these firewall rules to enable external access to your observability stack.
