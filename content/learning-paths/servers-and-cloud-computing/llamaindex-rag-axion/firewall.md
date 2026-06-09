---
title: Configure Google Cloud firewall rules for LlamaIndex
description: Learn how to create a Google Cloud firewall rule that allows browser access to a FastAPI-based LlamaIndex RAG application.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Allow inbound access to the LlamaIndex browser application

Create a firewall rule in Google Cloud Console to expose port 8000 for the browser-based LlamaIndex RAG application.

### Configure the firewall rule in Google Cloud Console

To configure a firewall rule:

1. Navigate to the [Google Cloud console](https://console.cloud.google.com/).
2. Go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Google Cloud console VPC Network Firewall page showing the Create firewall rule button in the top menu bar#center](images/firewall-rule.png "Create a firewall rule in Google Cloud console")

3. Set **Name** to `allow-llamaindex-port`, then select the network you want to bind to your virtual machine.
4. Set **Direction of traffic** to **Ingress**, set **Action on match** to **Allow**, set **Targets** to **All instances in the network**, and set **Source IPv4 ranges** to **0.0.0.0/0**.

![Google Cloud console Create firewall rule form with Name set to allow-llamaindex-port and Direction of traffic set to Ingress#center](images/network-rule.png "Configuring the allow-llamaindex-port firewall rule")

5. Under **Protocols and ports**, select **Specified protocols and ports**.
6. Select the **TCP** checkbox. Port `8000` is used by the FastAPI server that backs the browser-based LlamaIndex RAG application. Enter:

```text
8000
```

![Google Cloud console Protocols and ports section with TCP selected and port 8000 entered#center](images/network-port.png "Setting the LlamaIndex browser application port in the firewall rule")

7. In the same **TCP** field, also add port `22` to allow SSH access to the VM.
8. Select **Create**.

## What you've accomplished and what's next

You've now created a firewall rule that exposes port 8000 for the browser-based LlamaIndex RAG application and port 22 for SSH. The firewall rule uses the network tag `allow-llamaindex-port`, which you'll attach to your virtual machine in the next section.

Next, you'll create a Google Cloud C4A virtual machine and connect to it using SSH.
