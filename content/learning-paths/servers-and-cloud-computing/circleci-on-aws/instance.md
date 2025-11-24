---
title: Create an AWS EC2 Arm64 Graviton2 Instance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will learn how to set up an AWS Graviton Arm64 EC2 instance on Amazon Web Services (AWS) using the `m6g.large` instance type in the AWS Management Console. 

{{% notice Note %}}
For support on AWS setup, see the Learning Path [Getting started with AWS](/learning-paths/servers-and-cloud-computing/csp/aws/).
{{% /notice %}}


## Set up an instance in the AWS Management Console

To create your virtual machine:  
- Navigate to the [AWS Management Console](https://aws.amazon.com/console/).  
- Go to EC2 > Instances and select Launch Instance.  
- Under Instance configuration:  
   - Enter an appropriate Instance name.
   - Choose an Amazon Machine Image (AMI) such as Ubuntu 24.04 ARM64.

     ![AWS Management Console showing the Amazon Machine Image selection screen with Ubuntu 24.04 ARM64 highlighted. The interface displays a list of available AMIs, each with details such as name, architecture, and description. The wider environment includes navigation menus on the left and a search bar at the top. The mood is neutral and instructional, focused on guiding users through selecting an appropriate AMI. Visible text includes Amazon Machine Image, Ubuntu 24.04 ARM64, and related AMI details. alt-text#center](images/aws1.png "Figure 1: Amazon Machine Image (AMI)")
     
   - Under Instance type, select a Graviton-based type `m6g.large`.

  ![AWS Management Console displaying the instance type selection screen with m6g.xlarge highlighted. The primary subject is the list of available EC2 instance types, each showing details such as name, vCPUs, memory, and architecture. The m6g.xlarge row is selected, indicating 2 vCPUs and 8 GB memory, with Arm64 architecture. The wider environment includes navigation menus on the left and a search bar at the top. Visible text includes Instance type, m6g.xlarge, vCPUs, Memory, and Arm64. The tone is neutral and instructional, guiding users to select the correct instance type. #alt-text#center](images/aws2.png "Instance type")

   - Configure your Key pair (login) by either creating a new key pair or selecting an existing one to securely access your instance. 
   - In Network settings, ensure that Allow HTTP traffic from the internet and Allow HTTPS traffic from the internet are checked.

     ![AWS Management Console showing the Network settings configuration screen for launching an EC2 instance. The primary subject is the Network settings panel, where the options Allow HTTP traffic from the internet and Allow HTTPS traffic from the internet are both checked. The wider environment includes navigation menus on the left and a summary of instance configuration steps at the top. Visible text includes Network settings, Allow HTTP traffic from the internet, and Allow HTTPS traffic from the internet. The tone is neutral and instructional, guiding users to enable the correct network access for their instance. #alt-text#center](images/aws3.png "Figure 3: Network settings")

  {{% notice Network security %}}
  Be careful with permissive network inbound rules, as they pose a security risk. Good practice is to configure the machine to only allow traffic from your IP.
  {{% /notice %}}
  

   - Adjust Storage settings as needed — for this setup, 30 GB of gp3 (SSD) storage is sufficient.  
   - Click Launch Instance to create your virtual machine.  
