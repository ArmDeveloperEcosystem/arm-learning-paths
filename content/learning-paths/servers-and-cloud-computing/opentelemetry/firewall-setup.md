---
title: Create firewall rules on GCP for flask and observability components
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure GCP firewall for OpenTelemetry

To allow inbound traffic for the Flask application and observability components, you must create a firewall rule in the Google Cloud Console.

{{% notice Note %}} For more information about GCP setup, see [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).{{% /notice %}}

## Required Ports

| Service | Port | Purpose |
| ------- | ---- | ------- |
| Flask Application | 8080 | Application traffic |
| Jaeger UI | 16686 | Trace visualization |
| Prometheus UI | 9090 | Metrics dashboard |
| OTLP gRPC | 4317 | Telemetry ingestion |
| OTLP HTTP | 4318 | Telemetry ingestion |
| Collector Metrics | 8889 | Prometheus scrape endpoint |

## Create a Firewall Rule in GCP

To expose the above TCP ports, let's create a firewall rule.

Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Google Cloud Console VPC Network Firewall page showing existing firewall rules and Create Firewall Rule button#center](images/firewall-rule1.png "Create a firewall rule")

Next, create the firewall rule that will expose the above TCP ports.
Set the **Name** of the new rule to "allow-all-opentelemetry". Select your network that you intend to bind to your VM (default is "default" but your organization may vary)

Set **Direction of traffic** to "Ingress". Set **Allow on match** to "Allow" and **Targets** to "Specified target tags".

![Google Cloud Console firewall rule creation form showing name field, network selection, direction set to Ingress, and targets set to Specified target tags#center](images/network-rule2.png "Creating opentelemetry firewall rule")

Next, enter "allow-all-opentelemetry" in the **Target tags** text field. Set **Source IPv4 ranges** to "0.0.0.0/0".

![Google Cloud Console firewall rule form showing target tags field with allow-all-opentelemetry entered and source IPv4 ranges set to 0.0.0.0/0#center](images/network-rule3.png "Creating the Opentelemetry firewall rule")

Finally, select **Specified protocols and ports** under the **Protocols and ports** section. Select the **TCP** checkbox, enter "8080,16686,9090,4317,4318,8889" in the **Ports" text field, and select **Create**.

![Google Cloud Console firewall rule form showing protocols and ports section with TCP selected and ports 8080,16686,9090,4317,4318,8889 specified#center](images/network-port.png "Specifying the TCP ports to expose for Opentelemetry")

## What you've accomplished and what's next

You've successfully:

- Created firewall rules in Google Cloud to expose ports for the Flask application and observability components
- Configured network access for Jaeger, Prometheus, and OpenTelemetry Collector endpoints
- Set up secure ingress rules for telemetry data collection

Next, you'll provision a Google Axion C4A Arm virtual machine and apply these firewall rules to enable external access to your observability stack.
