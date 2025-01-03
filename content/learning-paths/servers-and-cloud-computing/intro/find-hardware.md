---
layout: learningpathall
title: Find Arm hardware
weight: 3
---
Server hardware, based on Arm Neoverse processors, is available from cloud service providers (CSPs) and server vendors. 

## Cloud Service Providers 

Creating an account with a cloud service provider (CSP) is the easiest way to get started with Arm. CSPs offer introductory free credits to start learning cloud services. A pay-as-you-go model makes it easy to try out Arm hardware at little cost, if any. 

Software developers often try Arm hardware as a way to reduce cost and improve application performance.

Cloud providers offer Arm instances based on Neoverse processors. For example:
- [Alibaba Cloud](https://www.alibabacloud.com/product/ecs/g8m)
- [Amazon Web Services (AWS)](https://aws.amazon.com/ec2/graviton/)
- [Google Cloud](https://cloud.google.com/compute/docs/instances/arm-on-compute)
- [Microsoft Azure](https://azure.microsoft.com/en-us/blog/azure-virtual-machines-with-ampere-altra-arm-based-processors-generally-available/)
- [Oracle Cloud](https://www.oracle.com/cloud/compute/arm/)
- [Equinix](https://deploy.equinix.com/product/servers/c3-large-arm64/)
- [Scaleway](https://www.scaleway.com/en/cost-optimized-instances-based-on-arm/)
- [Hetzner Cloud](https://www.hetzner.com/news/arm64-cloud)

Free tier offers are currently available:
- [Amazon EC2 t4g.small instances powered by AWS Graviton2 processors are free until Dec 31st 2024](https://aws.amazon.com/ec2/instance-types/t4/)
- [Oracle free tier includes up to 4 instances of ARM Ampere A1 Compute which are always free](https://www.oracle.com/cloud/free/)

[Get started with Arm-based cloud service platforms](/learning-paths/servers-and-cloud-computing/csp/) explains how to create an account and start an Arm virtual machine using the cloud service providers listed above.

## Works on Arm (free cloud resources)

The [Works on Arm](https://www.arm.com/markets/computing-infrastructure/works-on-arm) initiative enables developers to build, test, and optimize projects on the Arm64 architecture by providing free access to Arm based developer platforms, cloud instances, and CI/CD environments. Arm has partnered with cloud service providers to make Neoverse compute available to developers.

Consider [applying for Arm resources on an Equinix Cluster](https://github.com/WorksOnArm/equinix-metal-arm64-cluster).

## Academic offers from Cloud Service Providers

Below is a list of Arm cloud partners that have existing academic offers for students and teaching staff who wish to use Arm-based instances. 

- [Microsoft Azure Student Offer](https://azure.microsoft.com/en-us/free/students)
- [Google Cloud for Faculty](https://cloud.google.com/edu/faculty?hl=en)
- [Google Cloud for Researchers](https://cloud.google.com/edu/researchers?hl=en)
- [Alibaba Cloud Academic Empowerment Program](https://edu.alibabacloud.com/campus/index?spm=a3c0i.11593861.4363105600.24.6d326d84ZWObih)
- [NVIDIA Higher Education Research](https://www.nvidia.com/en-gb/industries/higher-education-research/academic-grant-program/)
- [Oracle Cloud Education](https://www.oracle.com/uk/government/education/)

##  Arm SystemReady Certified hardware

[Arm SystemReady](https://www.arm.com/architecture/system-architectures/systemready-certification-program) is a program that certifies that systems meet the SystemReady standards, giving you confidence that operating systems (OS) and subsequent layers of software just work.

You can find a full list of SystemReady SR Certified Systems on the [Arm website](https://www.arm.com/architecture/system-architectures/systemready-certification-program/sr) along with links to purchase Arm servers.

## Server software development

Servers typically run the Linux operating system. Popular distributions for servers include Ubuntu, Red Hat, SUSE Linux, and Debian. Vendor specific distributions, such as Amazon Linux and Oracle Linux are also available.

If the GNU compiler is not pre-installed with your distribution, you can [install it using a package manager](/install-guides/gcc/native/).

You can also install [Arm Compiler for Linux](/install-guides/acfl/) for HPC applications.

[Migrating applications to Arm servers](/learning-paths/servers-and-cloud-computing/migration/) is a good place to start analyzing existing applications and reviewing guidance for developers interested in trying Arm hardware. 
