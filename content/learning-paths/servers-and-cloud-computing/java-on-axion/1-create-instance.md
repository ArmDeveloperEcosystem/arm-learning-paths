---
title: Create an Arm-based VM instance with Google Axion CPU
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create an Axion instance

Axion is Google’s first Arm-based server processor, built using the Armv9 Neoverse V2 CPU. Created specifically for the data center, Axion delivers industry-leading performance and energy efficiency. To learn more about Google Axion, refer to this [page](http://cloud.google.com/products/axion/)

There are several ways to create an Arm-based Google Axion VM: the Google Cloud console, the gcloud CLI tool, or using your choice of IaC (Infrastructure as Code).

This guide will use the gcloud CLI. If you would like to read more about deploying to Google Cloud via IaC, please check out the [Learning Path to Deploy Arm virtual machines on Google Cloud Platform (GCP) using Terraform](https://learn.arm.com/learning-paths/servers-and-cloud-computing/gcp/).

If you have never used the Google Cloud Platform before, please review [Getting Started with Google Cloud Platform](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/google/).

#### Open and configure the Google Cloud Shell Editor

The gcloud CLI is pre-installed in Cloud Shell Editor, which is the quickest way to access a terminal with the gcloud CLI. It can be found at [shell.cloud.google.com](https://shell.cloud.google.com/).

Once the shell is available, configure it to use your Google Cloud project ID:

```bash
gcloud config set project [PROJECT_ID]
```
#### Create the instance

Run the following command, being careful to replace `[YOUR ZONE]` with the appropriate zone:

```bash
gcloud compute instances create test-app-instance --image-family=ubuntu-2404-lts-arm64  --image-project=ubuntu-os-cloud  --machine-type=c4a-standard-2 --scopes userinfo-email,cloud-platform  --zone [YOUR ZONE] --tags http-server
```

{{% notice Note %}}
The command above will use the default network in your GCP project. If you want to use an existing network and subnet that's different from the default, please use the following flags:

```bash
--network=[YOUR NETWORK] --subnet=[YOUR SUBNET]
```
{{% /notice %}}

#### Configure network access

In the next section you will run a Java web server that serves on port 8080. To set up access to your instance for this, run:

```bash
gcloud compute firewall-rules create default-allow-http-8080 --network=[YOUR NETWORK] --allow tcp:8080 --source-ranges 0.0.0.0/0 --target-tags http-server --description "Allow port 8080 access to http-server"
```

If you want to use the default network, you can omit the `--network` flag.

#### Obtain the IP of your instance

To obtain the external IP of your instance, run

```bash
gcloud compute instances list
```

You will see an entry that looks like this:

```bash
NAME: test-app-instance
ZONE: us-central1-a
MACHINE_TYPE: c4a-standard-2
PREEMPTIBLE: 
INTERNAL_IP: XX.XX.XX.XX
EXTERNAL_IP: XX.XX.XX.XX
STATUS: RUNNING
```

Save the EXTERNAL_IP for the next section.
