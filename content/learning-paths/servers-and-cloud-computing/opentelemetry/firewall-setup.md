---
title: Create a firewall rule on GCP
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure GCP firewall for OpenTelemetry

To allow inbound traffic for the Flask application and observability components, you must create firewall rules in the Google Cloud Console.

{{% notice Note %}} For more information about GCP setup, see [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).{{% /notice %}}

## Required Ports

| Service | Port | Purpose |
|--------|------|---------|
| Flask Application | 8080 | Application traffic |
| Jaeger UI | 16686 | Trace visualization |
| Prometheus UI | 9090 | Metrics dashboard |
| OTLP gRPC | 4317 | Telemetry ingestion |
| OTLP HTTP | 4318 | Telemetry ingestion |
| Collector Metrics | 8889 | Prometheus scrape endpoint |

## Create a Firewall Rule in GCP

To expose the Flask application (port 8080), create a firewall rule.

Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Google Cloud Console VPC Network Firewall page showing existing firewall rules and Create Firewall Rule button alt-txt#center](images/firewall-rule1.png "Create a firewall rule")

Next, create the firewall rule that exposes the TCP port 8080.
Set the **Name** of the new rule to "allow-tcp-8080". Select your network that you intend to bind to your VM (default is "autoscaling-net", but your organization might have others).

Set **Direction of traffic** to "Ingress". Set **Allow on match** to "Allow" and **Targets** to "Specified target tags".

![Google Cloud Console firewall rule creation form showing name field, network selection, direction set to Ingress, and targets set to Specified target tags alt-txt#center](images/network-rule2.png "Creating the TCP/8080 firewall rule")

Next, enter "allow-tcp-8080" in the **Target tags** text field. Set **Source IPv4 ranges** to "0.0.0.0/0".

![Google Cloud Console firewall rule form showing target tags field with allow-tcp-8080 entered and source IPv4 ranges set to 0.0.0.0/0 alt-txt#center](images/network-rule3.png "Creating the TCP/8080 firewall rule")

Finally, select **Specified protocols and ports** under the **Protocols and ports** section. Select the **TCP** checkbox, enter "8080" in the **Ports" text field, and select **Create**.

![Google Cloud Console firewall rule form showing protocols and ports section with TCP selected and port 8080 specified alt-txt#center](images/network-port.png "Specifying the TCP port to expose")

{{% notice Note %}}
The above steps demonstrate how to open port **8080** for the Flask application.

You can repeat the same workflow to create firewall rules for the following OpenTelemetry services:

- **16686** → Jaeger UI  
- **9090** → Prometheus UI  
- **4317** → OTLP gRPC endpoint  
- **4318** → OTLP HTTP endpoint  
- **8889** → Collector metrics endpoint  

Change the rule name and port number accordingly (for example: `allow-tcp-16686`, `allow-tcp-9090`, etc.).
{{% /notice %}}

You can now proceed to deploy and validate the OpenTelemetry stack.
