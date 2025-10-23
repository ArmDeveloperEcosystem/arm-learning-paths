---
title: Getting Started with Google Cloud Platform
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will learn how to provision a Google Axion C4A Arm virtual machine on Google Cloud Platform (GCP) using the `c4a-standard-4` (4 vCPUs, 16 GB memory) machine type in the Google Cloud Console.  

{{% notice Note %}}
For support on GCP setup, see the Learning Path [Getting started with Google Cloud Platform](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/google/).
{{% /notice %}}

## Provision a Google Axion C4A Arm VM in Google Cloud Console

To create a virtual machine based on the C4A instance type:
- Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
- Go to **Compute Engine > VM Instances** and select **Create Instance**. 
- Under **Machine configuration**:
   - Populate fields such as **Instance name**, **Region**, and **Zone**.
   - Set **Series** to `C4A`.
   - Select `c4a-standard-4` for machine type.

   ![Create a Google Axion C4A Arm virtual machine in the Google Cloud Console with c4a-standard-4 selected alt-text#center](images/gcp-vm.png "Creating a Google Axion C4A Arm virtual machine in Google Cloud Console")


- Under **OS and Storage**, select **Change**, then choose an Arm64-based OS image. For this Learning Path, use **SUSE Linux Enterprise Server** or **Ubuntu**. 
   - If using use **SUSE Linux Enterprise Server**. Select "Pay As You Go" for the license type. 
   - If using **Ubuntu**, under the **Version** tab, please scroll down and select the aarch64 version of **Ubuntu 22.04 LTS**.
- Once appropriately selected, please Click **Select**. 
- Under **Networking**, enable **Allow HTTP traffic**.
- Click **Create** to launch the instance.
- Once created, you should see a "SSH" option to the right in your list of VM instances.  Click on this to launch a SSH shell into your VM instance:

![Invoke a SSH session via your browser alt-text#center](images/gcp-ssh.png "Invoke a SSH session into your running VM instance")

- A window from your browser should come up and you should now see a shell into your VM instance:

![Terminal Shell in your VM instance alt-text#center](images/gcp-shell.png "Terminal shell in your VM instance")

## Explore your instance

### Run uname

Use the [uname](https://en.wikipedia.org/wiki/Uname) utility to verify that you are using an Arm-based server. For example:

```console
uname -m
```
will identify the host machine as `aarch64`.

### Run hello world

Install the `gcc` compiler:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt update
sudo apt install -y build-essential
  {{< /tab >}}
  {{< tab header="SUSE Linux" language="bash">}}
sudo zypper refresh
sudo zypper install -y gcc
  {{< /tab >}}
{{< /tabpane >}}

Using a text editor of your choice, create a file named `hello.c` with the contents below:

```C
#include <stdio.h>
int main(){
    printf("hello world\n");
    return 0;
}
```
Build and run the application:

```console
gcc hello.c -o hello
./hello
```

The output is shown below:

```output
hello world
```

## Automating Arm Based Infrastructure Deployment

Cloud infrastructure deployment is typically done via Infrastructure as code (IaC) automation tools. There are Cloud Service Provider specific tools like [Google Cloud Deployment Manager](https://cloud.google.com/deployment-manager/docs/).

There are also Cloud Service Provider agnostic tools like [Terraform](https://www.terraform.io/).There is a [deploying Arm VMs on (GCP) using Terraform learning path](/learning-paths/servers-and-cloud-computing/gcp) that should be reviewed next.