---
title: Configure and run an architecture-agnostic OrchardCore app on Arm and x86 using .NET AnyCPU
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run a .NET OrchardCore application on Arm and x86

In this section, you will configure and run your OrchardCore application on both Arm and x86 architectures using .NET's AnyCPU configuration. This architecture-agnostic approach simplifies deployment and ensures that your application runs smoothly on diverse hardware, including cloud VMs, local development boxes, and edge devices.

The AnyCPU feature has existed since .NET Framework 2.0, but its current behavior (particularly how it handles 32-bit vs. 64-bit execution) was defined in .NET Framework 4.5. 

{{% notice Note %}}
In .NET Core and .NET 5+, AnyCPU still lets the runtime decide which architecture to use, but keep in mind that your build must match the runtime environment's bitness (32-bit vs. 64-bit). Since .NET 8 targets 64-bit by default, this Learning Path assumes 64-bit runtime environments on both Arm64 and x86_64.
{{% /notice %}}

## Configure the project for AnyCPU

To make your OrchardCore application architecture-agnostic, configure the project to use the AnyCPU platform target. This allows the .NET runtime to select the appropriate architecture at runtime.

1. Open your OrchardCore project `MyOrchardCoreApp.csproj` in your IDE.

2. Add the `<PlatformTarget>` element to your existing `<PropertyGroup>`:

```xml
<PropertyGroup>
  <PlatformTarget>AnyCPU</PlatformTarget>
</PropertyGroup>
```

3. Save the `.csproj` file.

## Build and run on any platform

You can now build your application once and run it on either an x86_64 or Arm64 system.

Build the application:

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

Using the AnyCPU configuration offers several advantages:

- **Flexibility**: Deploy your application on a wide range of devices without modifying your code.
- **Efficiency**: Eliminate the need to maintain separate builds for different architectures.
- **Scalability**: Easily scale your application across different hardware platforms.

This approach ensures that your OrchardCore application runs consistently on both Arm and x86 architectures.
