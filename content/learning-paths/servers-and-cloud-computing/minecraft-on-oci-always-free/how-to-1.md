---
title: Starting an OCI A4 instance on OCI Always Free
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connecting to Oracle Cloud Infrastructure

1. Log on to [Oracle Cloud](https://cloud.oracle.com) (we should double-check the experience)
2. On the OCI dashboard, navigate to Compute -> Instances to start a new instance
3. Click on "Create instance", then: 
    * Choose one of the availability domains offered to you with A1 instances available
    * Select "Change shape" and set the instance type to Ampere A1 Flex
    * Choose "Advanced Options" and allocated 2 OCPUs and 8GB of memory to our instance
    * Choose "Oracle Linux 9" or one of the other available images in "Change image", then click Next
4. Use the default security options, and configure networking as follows:
    * When prompted, create a new Virtual Cloud Network (VCN) and public subnet to allow you to access the instance remotely
    * Create an SSH key pair which you can use to connect to your instance over SSH once it is created
    * Make sure that you download both the public and private key for future use
5. Use default Storage options
6. After verifying that the instance is correctly configured, choose "Create" to provision a new instance


