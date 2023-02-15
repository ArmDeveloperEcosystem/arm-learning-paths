---
layout: learningpathall
title: Find Arm hardware
weight: 2
---
Server hardware, based on Arm Neoverse processors, is available from cloud service providers (CSPs) and server vendors. 

## Cloud Service Providers 

Creating an account with a cloud service provider (CSPs) is the easiest way to get started with Arm. CSPs offer introductory free credits to start learning cloud services. A pay-as-you-go model makes it easy to try out Arm hardware at little to no cost. 

Software developers often try Arm hardware as a way to reduce cost and improve application performance.

Major cloud providers offer Arm instances based on Neoverse processors. For example:
- [Alibaba Cloud](https://www.alibabacloud.com/product/ecs/g8m)
- [Amazon Web Services (AWS)](https://aws.amazon.com/ec2/graviton/)
- [Google Cloud](https://cloud.google.com/compute/docs/instances/arm-on-compute)
- [Microsoft Azure](https://azure.microsoft.com/en-us/blog/azure-virtual-machines-with-ampere-altra-arm-based-processors-generally-available/)
- [Oracle Cloud](https://www.oracle.com/cloud/compute/arm/)

Free tier offers are currently available.
- [Amazon EC2 t4g.small instances powered by AWS Graviton2 processors are free until Dec 31st 2023](https://aws.amazon.com/ec2/instance-types/t4/)
- [Oracle free tier includes up to 4 instances of ARM Ampere A1 Compute which are always free](https://www.oracle.com/cloud/free/)
- [Until April 5, 2023 Tau T2A VMs in Google Cloud are available for a free trial](https://cloud.google.com/compute/docs/instances/create-arm-vm-instance#t2afreetrial)

[Get started with Arm-based cloud service platforms](/learning-paths/server-and-cloud/csp/) explains how to create an account and start an Arm virtual machine using the cloud service providers listed above.

##  Arm SystemReady Certified hardware

[Arm SystemReady](https://www.arm.com/architecture/system-architectures/systemready-certification-program) is a program that certifies that systems meet the SystemReady standards, giving confidence that operating systems (OS) and subsequent layers of software just work.

You can find a full list of SystemReady SR Certified Systems on the [Arm website](https://www.arm.com/architecture/system-architectures/systemready-certification-program/sr) along with links to purchase Arm servers.

More developer hardware options are available from the [Works on Arm initiative](https://www.arm.com/markets/computing-infrastructure/works-on-arm). 

## Server software development

Servers typically run, and are provided with, the Linux operating system. Popular distributions for servers include Ubuntu, Red Hat, SUSE Linux, and Debian. Vendor specific distributions, such as Amazon Linux and Oracle Linux are also available.

If `gcc` is not pre-installed with your distribution, you can [install using a package manager](/install-tools/gcc/#native).

You may also wish to install [Arm Compiler for Linux](/install-tools/acfl/) for HPC applications.

[Migrating applications to Arm servers](/learning-paths/server-and-cloud/migration/) is a good place to start analyzing existing applications and reviewing guidance for developers interested in trying Arm hardware. 
