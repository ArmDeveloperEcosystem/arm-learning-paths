---
title: Create a basic OrchardCore application
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Create a basic OrchardCore application

In this section, you will learn how to create and compile a basic OrchardCore CMS application. OrchardCore is a modular and multi-tenant application framework built with ASP.NET Core, which can be used to create content-driven websites.

## Step 1: Set up your development environment

1. **Install .NET SDK**: Follow the instructions on the [.NET download page](https://dotnet.microsoft.com/download) to install the SDK for your operating system.

2. **Verify installations**: Open a terminal and run the following commands to verify the installations:

   ```bash
   dotnet --version
   node --version
   ```

## Step 2: Install the OrchardCore Templates

To start building an OrchardCore application, you need to install the OrchardCore templates. Open your terminal and run the following command:

```bash
dotnet new -i OrchardCore.ProjectTemplates::1.0.0-rc2-13450
```

This command installs the OrchardCore project templates, which you will use to create a new application.

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

2. **Run the application**: Start the application with:

   ```bash
   dotnet run --urls http://0.0.0.0:8080
   ```

3. **Access the application**: Open a web browser and navigate to `http://[instance IP]:8080` to see your OrchardCore application in action, where `[instance IP]` is the public IP of your Azure Cobalt instance.

4. **Configure the application as a blog** In the resulting configuration page, 

You have successfully created and run a basic OrchardCore CMS application. In the next sections, you will learn how to integrate a C shared library into your .NET application and explore performance optimizations for Arm architecture.