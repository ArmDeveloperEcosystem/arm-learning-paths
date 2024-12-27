---
title: Create an application
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Create a Project

In this section, you will set up the project, which involves installing the Aspire workload.

To create a .NET Aspire application, first ensure that you have [.NET 8.0 or later installed](https://dotnet.microsoft.com/en-us/download/dotnet) on your Windows on Arm development machine.

To find out which version you have, open a Powershell terminal and run:
```console
dotnet --version
```
The output should tell you which version of .NET SDK you have installed on your machine.
 
Next, install the Aspire workload:

```console
dotnet workload install aspire
```
You should see the following output:

```output
Downloading Aspire.Hosting.Sdk.Msi.arm64 (8.2.2)
Installing Aspire.Hosting.Sdk.Msi.arm64 ..... Done
Downloading Aspire.ProjectTemplates.Msi.arm64 (8.2.2)
Installing Aspire.ProjectTemplates.Msi.arm64 ..... Done

Successfully installed workload(s) aspire.
```
Once the Aspire workload is installed, you can create a new application by executing:

```console
dotnet new aspire-starter -o NetAspire.Arm
```
This command generates a solution with the following structure:
* **NetAspire.Arm.AppHost** - the orchestrator, or coordinator, project serves as the backbone of your distributed application. Its primary responsibilities include defining how services connect to one another, configuring ports and endpoints to ensure seamless communication, managing service discovery to enable efficient interactions between components, and handling container orchestration to streamline the deployment and operation of services within your application.

* **NetAspire.Arm.ApiService** - the sample REST API service, built with ASP.NET Core, acts as a core component of your application by implementing business logic and managing data access. The default implementation comes preconfigured with essential features, including a WeatherForecast endpoint for demonstration purposes, built-in health checks to monitor the service’s status, and telemetry setup to track performance and usage metrics.

* **NetAspire.Arm.Web** - the web frontend application, implemented with Blazor, serves as the user-facing layer of your application. It communicates with the API service to provide an interactive experience. This application includes a user interface for presenting data, client-side logic for handling interactions, and preconfigured patterns for consuming services.

* **NetAspire.Arm.ServiceDefaults** - the shared library provides a centralized foundation for common service configurations across your application. It includes a default middleware setup, preconfigured telemetry settings for tracking performance, standard health check implementations, and logging configurations to ensure consistent and efficient monitoring and debugging.

The structure of this project is designed to enhance efficiency and simplify the development of cloud-native applications. At its core, it incorporates features to ensure seamless service interactions, robust monitoring, and an exceptional development experience.

One of the foundational elements is service discovery, which enables automatic service registration, dynamic endpoint resolution, and load balancing. These features ensure that services communicate effectively and handle traffic efficiently, even in complex, distributed environments.

For monitoring and telemetry, the architecture integrates tools like built-in health checks, OpenTelemetry for monitoring, and metrics collection with distributed tracing. These features provide developers with deep insights into application performance, helping to maintain reliability and optimize system operations.

Configuration management offers environment-based settings that make deploying applications across different stages straightforward. Secure secrets management safeguards sensitive information, while standardized service-to-service communication simplifies interactions between microservices.

The architecture is also tailored to improve the development experience. Developers can benefit from local debugging support and a powerful monitoring dashboard. This dashboard provides a detailed view of service health, logs, metrics, trace information, resource usage, and service dependencies. Additionally, hot reload capability allows real-time updates during development, and container support ensures consistency across local and production environments.

This thoughtfully-crafted architecture embodies microservices best practices, promoting scalability, maintainability, and service isolation. It not only simplifies deployment and monitoring, but also fosters developer productivity by streamlining workflows and providing intuitive tools for building modern, distributed applications.

