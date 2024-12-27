---
title: .NET Aspire
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### What is .NET Aspire?
.NET Aspire is a comprehensive suite of powerful tools, templates, and packages designed to simplify the development of cloud-native applications using the .NET platform. Delivered through a collection of NuGet packages, .NET Aspire provides solutions for building cloud-native apps, enabling developers to build observable and production-ready projects efficiently.

Cloud-native applications are typically composed of small, interconnected services or microservices, rather than a single monolithic codebase. These applications often consume a variety of services such as:

* Databases.
* Messaging systems.
* Caching mechanisms. 

.NET Aspire gives you a consistent set of tools and patterns that help you to build and run distributed applications, taking full advantage of the scalability, resilience, and manageability of cloud infrastructures.

.NET Aspire enhances the local development experience by simplifying the management of your application's configuration and interconnections. It abstracts low-level implementation details, and streamlines the following:

* The setup of service discovery.
* Environment variables.
* Container configurations. 

With a few helper method calls, you can create local resources, wait for the resources to become available, and then configure appropriate connection strings in your projects.

.NET Aspire offers integrations for popular services like Redis and PostgreSQL, ensuring standardized interfaces and seamless connections with your app. These integrations handle specific cloud-native requirements through consistent configuration patterns. By referencing named resources, configurations are injected automatically, simplifying the process of connecting services.

.NET Aspire provides project templates that include boilerplate code and configurations common to cloud-native apps, such as health checks and telemetry, as well as service discovery. It offers tooling experiences for Visual Studio, Visual Studio Code, and .NET CLI to help you create and interact with .NET Aspire projects. The templates come with default settings that you can use to get started quickly, which reduces setup time and increases productivity.

By providing a consistent set of tools and patterns, .NET Aspire streamlines the development process of cloud-native applications. It manages complex applications during the development phase without dealing with low-level implementation details. .NET Aspire easily connects to commonly-used services with standardized interfaces and configurations. There are also various templates and tooling to accelerate project setup and development cycles.

In this Learning Path, you will learn how to create a .NET Aspire application, describe the project, and modify the code on a Windows on Arm development machine. You will then deploy the application:

* Firstly, to an AWS Arm-powered virtual machine.
* Secondly, to a GCP Arm-powered virtual machine.
