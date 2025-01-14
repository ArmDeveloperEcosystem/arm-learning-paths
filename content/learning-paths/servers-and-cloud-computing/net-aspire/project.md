---
title: Create a project and then an application
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Create a project

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
## Create an application

Once the Aspire workload is installed, you can create a new application by executing:

```console
dotnet new aspire-starter -o NetAspire.Arm
```
This command generates a solution with the following structure:
* **NetAspire.Arm.AppHost** - the orchestrator, or coordinator, project serves as the backbone of your distributed application. Its primary responsibilities include:

    - Defining how services connect to one another.
    - Configuring ports and endpoints to ensure seamless communication.
    - Managing service discovery to enable efficient interactions between components.
    - Handling container orchestration to streamline the deployment and operation of services within your application.

* **NetAspire.Arm.ApiService** - the sample REST API service, built with ASP.NET Core, acts as a core component of your application by implementing business logic and managing data access. The default implementation comes preconfigured with essential features, that include:

    * A weatherForecast endpoint for demonstration purposes.
    * Built-in health checks to monitor the service’s status
    * Telemetry setup to track performance and usage metrics.

* **NetAspire.Arm.Web** - the web frontend application, implemented with Blazor, serves as the user-facing layer of your application. It communicates with the API service to provide an interactive experience. This application includes:

    * A user interface for presenting data.
    * Client-side logic for handling interactions.
    * Preconfigured patterns for consuming services.

* **NetAspire.Arm.ServiceDefaults** - the shared library provides a centralized foundation for common service configurations across your application. It includes:

    * A default middleware setup.
    * Preconfigured telemetry settings for tracking performance.
    * Standard health check implementations.
    * Logging configurations to ensure consistent and efficient monitoring and debugging.

The structure of this project is designed to enhance efficiency and simplify the development of cloud-native applications. At its core, it incorporates features to ensure seamless service interactions, robust monitoring, and an exceptional development experience.

#### Service discovery

One of the foundational elements is service discovery, which enables automatic service registration, dynamic endpoint resolution, and load balancing. These features ensure that services communicate effectively and handle traffic efficiently, even in complex, distributed environments.

#### Monitoring and telemetry

For monitoring and telemetry, the architecture integrates tools like built-in health checks, OpenTelemetry for monitoring, and metrics collection with distributed tracing. These features provide developers with deep insights into application performance, helping to maintain reliability and optimize system operations.

#### Configuration management

Configuration management offers environment-based settings that make deploying applications across different stages straightforward. Secure secrets management safeguards sensitive information, while standardized service-to-service communication simplifies interactions between microservices.

#### Improved development experience

The architecture is also tailored to improve the development experience. Developers can benefit from local debugging support and a powerful monitoring dashboard. This dashboard provides a detailed view of the following:

* Service health.
* Logs. 
* Metrics.
* Trace information.
* Resource usage.

This thoughtfully-crafted architecture embodies best practices for microservices, and promotes scalability, maintainability, and service isolation. It not only simplifies deployment and monitoring, but also fosters developer productivity by streamlining workflows and providing intuitive tools for building modern, distributed applications.

