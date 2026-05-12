---
title: Configure Google Cloud firewall rules for XGBoost
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Allow inbound access to the XGBoost inference API

Create a firewall rule in Google Cloud Console to expose the required port for the XGBoost inference API and browser-based access.

{{% notice Note %}} For help with GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).{{% /notice %}}

## Configure the firewall rule in Google Cloud Console

To configure a firewall rule for the XGBoost inference API:

1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Google Cloud Console VPC Network Firewall page showing the Create firewall rule button in the top menu bar#center](images/firewall-rule.png "Create a firewall rule in Google Cloud Console")

2. Create a firewall rule that exposes the ports required for XGBoost.

3. Set **Name** to `allow-xgboost-8080`, then select the network you want to bind to your virtual machine.

4. Set **Direction of traffic** to **Ingress**, set **Action on match** to **Allow**, set **Targets** to **All instances in the network**, and set **Source IPv4 ranges** to **0.0.0.0/0**.

![Google Cloud Console Create firewall rule form with Name set to allow-xgboost-8080 and Direction of traffic set to Ingress#center](images/network-rule.png "Configuring the allow-xgboost-8080 firewall rule")

5. Under **Protocols and ports**, select **Specified protocols and ports**.
6. Select the **TCP** checkbox and enter:

```text
8080
```

Port 8080 is used for:

* XGBoost inference API access
* Browser-based API validation
* External REST API requests
* Remote inference testing from local systems

![Google Cloud Console Protocols and ports section with TCP selected and port 8080 entered#center](images/network-port.png "Setting XGBoost ports in the firewall rule")

7. Select **Create**.

## What you've accomplished and what's next

You've created a firewall rule to expose the XGBoost inference API externally. You also enabled browser access and remote API connectivity for inference testing.

Next, you'll create a Google Axion C4A Arm virtual machine and attach it to this firewall rule.
