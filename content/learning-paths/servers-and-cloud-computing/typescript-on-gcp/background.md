---
title: Getting started with TypeScript on Google Axion C4A instances

weight: 2

layout: "learningpathall"
---

## Introduction

This Learning Path shows you how to deploy and benchmark TypeScript applications on Arm-based Google Cloud C4A instances powered by Axion processors. You'll provision a SUSE Linux Enterprise Server (SLES) virtual machine (VM), install and configure TypeScript, and measure performance using a JMH-style custom benchmark. By combining TypeScript’s strong typing and developer tooling with the high performance and energy efficiency of Arm-based C4A instances, you can build robust, scalable, and cost-effective cloud-native applications optimized for the future of cloud on Arm.


## Google Axion C4A Arm instances in Google Cloud

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability and performance benefits of the Arm architecture on Google Cloud.

To learn more about Google Axion, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## TypeScript

TypeScript is an open-source, strongly-typed programming language developed and maintained by Microsoft.  

TypeScript builds on JavaScript by adding features like static typing and interfaces. Any valid JavaScript code works in TypeScript, but TypeScript gives you extra tools to write code that is easier to maintain and less prone to errors. 

TypeScript is widely used for web applications, server-side development (Node.js), and large-scale JavaScript projects where type safety and code quality are important. Learn more from the [TypeScript official website](https://www.typescriptlang.org/) and the [TypeScript handbook and documentation](https://www.typescriptlang.org/docs/).
