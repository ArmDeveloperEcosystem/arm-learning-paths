---
title: Run a .NET OrchardCore application on Arm and x86
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run a .NET OrchardCore application on Arm and x86

In this section, you will learn how to configure and run your OrchardCore application on both Arm and x86 architectures using the .NET AnyCPU configuration. This approach allows your application to be architecture-agnostic, enabling easier deployment across different hardware platforms.

The AnyCPU feature has existed since .NET Framework 2.0, but its current behavior (particularly how it handles 32-bit vs. 64-bit execution) was defined in .NET Framework 4.5.

## Configure the project for AnyCPU

To make your OrchardCore application architecture-agnostic, you need to configure it to use the AnyCPU platform target. This allows the .NET runtime to choose the appropriate architecture at runtime.

First, open your OrchardCore project `MyOrchardCoreApp.csproj` in your preferred IDE.

Next, find the `<PropertyGroup>` and add the `<PlatformTarget>` element to `AnyCPU`:

```xml
<PropertyGroup>
  <PlatformTarget>AnyCPU</PlatformTarget>
</PropertyGroup>
```

Save the `.csproj` file:

## Build once, run anywhere

You can now build your application on either an x86 or Arm host machine and deploy it on any architecture:

```bash
dotnet build -c Release
```

Run the application:

```bash
dotnet run --urls http://0.0.0.0:8080
```

Your application should now be runnable on any architecture. All you have to do is copy the `MyOrchardCoreApp` directory to any computer with the .NET 8 runtime installed and run the command shown from within the `MyOrchardCoreApp` directory:

```bash
dotnet ./bin/Release/net8.0/MyOrchardCoreApp.dll --urls http://0.0.0.0:8080
```

## Benefits of architecture-agnostic applications

By configuring your application to be architecture-agnostic, you gain several benefits:

- **Flexibility**: Deploy your application on a wide range of devices without modification.
- **Efficiency**: Reduce the need for maintaining separate builds for different architectures.
- **Scalability**: Easily scale your application across different hardware platforms.

This approach ensures that your OrchardCore application can run seamlessly on both Arm and x86 architectures.
