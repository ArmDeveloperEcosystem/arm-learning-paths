---
title: Create a Google Axion C4A Arm virtual machine 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

In this section you will learn how to provision a **Google Axion C4A Arm virtual machine** on GCP with the **c4a-standard-4 (4 vCPUs, 16 GB Memory)** machine type, using the **Google Cloud Console**. 

For more details, kindly follow the Learning Path on [Getting Started with Google Cloud Platform](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/google/).

### Create an Arm-based Virtual Machine (C4A)

To create a virtual machine based on the C4A Arm architecture:
1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
2. Go to **Compute Engine > VM Instances** and click on **Create Instance**. 
3. Under the **Machine Configuration**:
      - Fill in basic details like **Instance Name**, **Region**, and **Zone**.
      - Choose the **Series** as `C4A`.
      - Select a machine type such as `c4a-standard-4`.
![Instance Screenshot](./image1.png)
4. Under the **OS and Storage**, click on **Change**, and select Arm64 based OS Image of your choice. For this Learning Path, choose **Red Hat Enterprise Linux** as the Operating System with **Red Hat Enterprise Linux 9** as the Version. Make sure you pick the version of image for Arm. Click on the **Select**.
5. Under **Networking**, enable **Allow HTTP traffic** to allow HTTP communication.
6. Click on **Create**, and the instance will launch.
