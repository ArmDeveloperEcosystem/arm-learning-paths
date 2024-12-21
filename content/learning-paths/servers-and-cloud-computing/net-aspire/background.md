---
title: Background
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### What is the .NET Aspire
.NET Aspire is a comprehensive suite of powerful tools, templates, and packages designed to simplify the development of cloud-native applications using the .NET platform. Delivered through a collection of NuGet packages, .NET Aspire addresses specific cloud-native concerns, enabling developers to build observable and production-ready apps efficiently.

Cloud-native applications are typically composed of small, interconnected services or microservices rather than a single monolithic codebase. These applications often consume a variety of services such as databases, messaging systems, and caching mechanisms. With .NET Aspire you get a consistent set of tools and patterns that help you build and run distributed applications, taking full advantage of the scalability, resilience, and manageability of cloud infrastructures.

.NET Aspire enhances the local development experience by simplifying the management of your application's configuration and interconnections. It abstracts low-level implementation details, streamlining the setup of service discovery, environment variables, and container configurations. Specifically, with a few helper method calls, you can create local resources (like a Redis container), wait for them to become available, and configure appropriate connection strings in your projects.

.NET Aspire offers integrations for popular services like Redis and PostgreSQL, ensuring standardized interfaces and seamless connections with your app. These integrations handle cloud-native concerns such as health checks and telemetry through consistent configuration patterns. By referencing named resources, configurations are injected automatically, simplifying the process of connecting services.

.NET Aspire provides project templates that include boilerplate code and configurations common to cloud-native apps, such as telemetry, health checks, and service discovery. It offers tooling experiences for Visual Studio, Visual Studio Code, and the .NET CLI to help you create and interact with .NET Aspire projects. The templates come with defaults to help you get started quickly, reducing setup time and increasing productivity.

By providing a consistent set of tools and patterns, .NET Aspire streamlines the development process of cloud-native applications. It manages complex applications during the development phase without dealing with low-level implementation details. .NET Aspire easily connects to commonly used services with standardized interfaces and configurations. There are also various templates and tooling to accelerate project setup and development cycles. Finally, with .NET Aspire, you can create applications that are ready for production with built-in support for telemetry, health checks, and service discovery.

In this Learning Path, you will learn how to create a .NET Aspire application, describe the project, and modify the code on a Windows on Arm development machine. You will then deploy the application to AWS and GCP Arm-powered virtual machines.
