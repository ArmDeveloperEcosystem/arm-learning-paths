---
title: Build and Run an OrchardCore CMS App on Azure Cobalt
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Getting started with the OrchardCore App 

In this section, you'll build and run a basic [OrchardCore](https://github.com/OrchardCMS/OrchardCore) CMS application, which is a popular Linux-based .NET workload. OrchardCore is a modular and multi-tenant application framework built with ASP.NET Core, that's commonly used to create content-driven websites.

## Step 1: Set up your development environment

1. Launch an Azure Cobalt 100 instance running Ubuntu 24.04, and open port 8080 to the internet. For setup instructions, see the [Create an Azure Cobalt 100 VM](../../cobalt) Learning Path.

2. **Install .NET SDK**:

```bash
wget https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install -y dotnet-sdk-8.0
```

3. Verify the installation:

```bash
dotnet --version
```

You should see output similar to:

```output
8.0.117
```

4. Install gcc for compiling your application:

```bash
sudo apt install gcc g++ build-essential -y
```

## Step 2: Install the OrchardCore Templates

To start building an OrchardCore application, you need to install the OrchardCore templates. Open your terminal and run the following command:

```bash
dotnet new install OrchardCore.ProjectTemplates::2.1.7
```

This command installs the OrchardCore project templates, which you will use to create a new application.

The output will look like:

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

## Step 3: Create a new OrchardCore application

1. **Create a new project**: Use the `dotnet` CLI to create a new OrchardCore application.

```bash
dotnet new occms -n MyOrchardCoreApp
```

   This command creates a new OrchardCore CMS application in a directory named `MyOrchardCoreApp`.

2. **Navigate to the project directory**:

```bash
cd MyOrchardCoreApp
```

## Step 4: Run the OrchardCore application

1. **Build the application**: Compile the application using the following command:

```bash
dotnet build
```

The output will look like:

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
2. **Run the application**: Start the application with:

```bash
dotnet run --urls http://0.0.0.0:8080
```

3. **Access the application**: Open a web browser and navigate to `http://[instance IP]:8080` to see your OrchardCore application in action, where `[instance IP]` is the public IP of your Azure Cobalt instance.

4. **Configure the application as a blog** In the resulting configuration page, 

You have successfully created and run a basic OrchardCore CMS application. In the next sections, you will learn how to integrate a C shared library into your .NET application and explore performance optimizations for Arm architecture.
