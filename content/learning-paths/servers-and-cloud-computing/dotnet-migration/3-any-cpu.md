---
title: Run a .NET OrchardCore application on Arm and x86
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Run a .NET OrchardCore application on Arm and x86

In this section, you will learn how to configure and run your OrchardCore application on both Arm and x86 architectures using the .NET AnyCPU configuration. This approach allows your application to be architecture agnostic, providing flexibility and ease of deployment across different hardware platforms.

## Configure the project for AnyCPU

To make your OrchardCore application architecture agnostic, you need to configure it to use the AnyCPU platform target. This allows the .NET runtime to choose the appropriate architecture at runtime.

1. Open your OrchardCore project in your preferred IDE.
2. Locate the `.csproj` file for your project.
3. Modify the `<PlatformTarget>` element to `AnyCPU`:

   ```xml
   <PropertyGroup>
     <PlatformTarget>AnyCPU</PlatformTarget>
   </PropertyGroup>
   ```

4. Save the changes to the `.csproj` file.

## Build once, run anywhere

   ```bash
   dotnet build -c Release
   ```

4. Run the application:

   ```bash
   dotnet run
   ```

Your application should now be runnable on any architecture.

## Benefits of architecture agnostic applications

By configuring your application to be architecture agnostic, you gain several benefits:

- **Flexibility**: Deploy your application on a wide range of devices without modification.
- **Efficiency**: Reduce the need for maintaining separate builds for different architectures.
- **Scalability**: Easily scale your application across different hardware platforms.

This approach ensures that your OrchardCore application can run seamlessly on both Arm and x86 architectures.