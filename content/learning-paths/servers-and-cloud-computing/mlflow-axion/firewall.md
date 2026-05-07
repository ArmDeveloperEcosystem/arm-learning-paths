---
title: Configure Google Cloud firewall rules for MLflow
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a firewall rule in Google Cloud Console

Create a firewall rule in Google Cloud Console to expose required ports for the MLflow UI and model serving API.

{{% notice Note %}}For help with GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).{{% /notice %}}

## Configure the firewall rule

Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.

![Google Cloud Console VPC Network Firewall page showing the Create firewall rule button in the top menu bar#center](images/firewall-rule.png "Create a firewall rule in Google Cloud Console")

Next, create the firewall rule that exposes the ports required for MLflow.

Set the **Name** of the new rule to "allow-mlflow-ports". Select the network that you intend to bind to your VM.

Set **Direction of traffic** to "Ingress". Set **Allow on match** to "Allow" and **Targets** to "All instances in the network". Set **Source IPv4 ranges** to "0.0.0.0/0".

![Google Cloud Console Create firewall rule form with Name set to allow-mlflow-ports and Direction of traffic set to Ingress#center](images/network-rule.png "Configuring the allow-mlflow-ports firewall rule")

Finally, select **Specified protocols and ports** under the **Protocols and ports** section. Select the **TCP** checkbox and enter:

```text
5000,6000
```

* **5000** → MLflow Tracking UI
* **6000** → MLflow Model Serving API

Then select **Create**.

![Google Cloud Console Protocols and ports section with TCP selected and ports 5000 and 6000 entered#center](images/network-port.png "Setting MLflow ports in the firewall rule")

## What you've learned and what's next

In this section, you:

* Created a firewall rule to expose MLflow UI and model serving API
* Enabled external access to monitor experiments and access deployed models

Next, you'll create a C4A Arm VM and attach it to this firewall rule.
