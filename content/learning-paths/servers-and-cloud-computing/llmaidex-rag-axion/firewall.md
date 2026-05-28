---
title: Configure Google Cloud firewall rules for LlamaIndex
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Allow inbound access to the LlamaIndex browser application

Create a firewall rule in Google Cloud Console to expose the required port for the browser-based LlamaIndex RAG application.

{{% notice Note %}}For help with GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).{{% /notice %}}

## Configure the firewall rule in Google Cloud Console

To configure a firewall rule for the LlamaIndex browser-based RAG application:

1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Google Cloud Console VPC Network Firewall page showing the Create firewall rule button in the top menu bar#center](images/firewall-rule.png "Create a firewall rule in Google Cloud Console")

2. Create a firewall rule that exposes the port required for the LlamaIndex browser application.

3. Set **Name** to `allow-llamaindex-port`, then select the network you want to bind to your virtual machine.

4. Set **Direction of traffic** to **Ingress**, set **Action on match** to **Allow**, set **Targets** to **All instances in the network**, and set **Source IPv4 ranges** to **0.0.0.0/0**.

![Google Cloud Console Create firewall rule form with Name set to allow-llamaindex-port and Direction of traffic set to Ingress#center](images/network-rule.png "Configuring the allow-llamaindex-port firewall rule")

5. Under **Protocols and ports**, select **Specified protocols and ports**.

6. Select the **TCP** checkbox and enter:

```text
8000
````

Use port mapping **8000** for the browser-based LlamaIndex RAG application running with FastAPI.

![Google Cloud Console Protocols and ports section with TCP selected and port 8000 entered#center](images/network-port.png "Setting the LlamaIndex browser application port in the firewall rule")

7. Select **Create**.

## What you've accomplished and what's next

You've created a firewall rule to expose the browser-based LlamaIndex RAG application. You also enabled external access to query documents and interact with the application directly from a web browser.

Next, you'll access the browser-based RAG application using the external IP address of your Google Cloud Axion virtual machine.
