---
title: Build and run an OrchardCore CMS app on Azure Cobalt
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Getting started with the OrchardCore app 

In this section, you'll build and run a basic [OrchardCore](https://github.com/OrchardCMS/OrchardCore) CMS application, which is a popular Linux-based .NET workload. OrchardCore is a modular and multi-tenant application framework built with ASP.NET Core, that's commonly used to create content-driven websites.

## Set up your development environment

First, launch an Azure Cobalt 100 instance running Ubuntu 24.04, and open port 8080 to the internet. 

For setup instructions, see the [Create an Azure Cobalt 100 VM](../../cobalt) Learning Path.

Next, install .NET SDK:

```bash
wget https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install -y dotnet-sdk-8.0
```

Verify the installation:

```bash
dotnet --version
```

You should then see output similar to:

```output
8.0.117
```

Install gcc for compiling your application:

```bash
sudo apt install gcc g++ build-essential -y
```

## Install the OrchardCore templates

Install the OrchardCore templates:

```bash
dotnet new install OrchardCore.ProjectTemplates::2.1.7
```

This command installs the OrchardCore project templates you'll use to create a new OrchardCore application.

Expected output:

```output
Success: OrchardCore.ProjectTemplates::2.1.7 installed the following templates:
Template Name             Short Name   Language  Tags
------------------------  -----------  --------  --------------------
Orchard Core Cms Module   ocmodulecms  [C#]      Web/Orchard Core/CMS
Orchard Core Cms Web App  occms        [C#]      Web/Orchard Core/CMS
Orchard Core Mvc Module   ocmodulemvc  [C#]      Web/Orchard Core/Mvc
Orchard Core Mvc Web App  ocmvc        [C#]      Web/Orchard Core/Mvc
Orchard Core Theme        octheme      [C#]      Web/Orchard Core/CMS
```

## Create a new OrchardCore application

First, create a new project using the `dotnet` CLI to create a new OrchardCore application:

```bash
dotnet new occms -n MyOrchardCoreApp
```

This command creates a new OrchardCore CMS application in a directory named `MyOrchardCoreApp`.

Now navigate to the project directory:

```bash
cd MyOrchardCoreApp
```

## Run the OrchardCore application

Build the application: 

```bash
dotnet build
```

The output should look like:

```output
MSBuild version 17.8.27+3ab07f0cf for .NET
  Determining projects to restore...
  Restored /home/azureuser/MyOrchardCoreApp/MyOrchardCoreApp.csproj (in 28.95 sec).
  MyOrchardCoreApp -> /home/azureuser/MyOrchardCoreApp/bin/Debug/net8.0/MyOrchardCoreApp.dll
  Copying translation files: MyOrchardCoreApp

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:38.05
```
Run the application:

```bash
dotnet run --urls http://0.0.0.0:8080
```

Access the application:

* In your browser, navigate to `http://[instance IP]:8080` to see your OrchardCore application in action. 

* Replace `[instance IP]` with your VM’s public IP address. You can find it in the Azure portal under the Networking tab of your virtual machine.

Configure the application: 

On the setup screen, choose the Blog recipe and complete the admin credentials and database configuration to finish setup.

## Summary and next steps

You have successfully created and run a basic OrchardCore CMS application. In the next sections, you will learn how to integrate a C shared library into your .NET application and explore performance optimizations for Arm architecture.
