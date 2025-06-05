---
title: Add a simple C shared library to your .NET OrchardCore application
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

In this section, you will learn how to integrate a simple C shared library into your .NET OrchardCore application. This process involves creating a C library, compiling it, and then using it within your .NET application. This integration can help you leverage existing C code and libraries, enhancing the functionality and performance of your application.


## Step 1: Create a C shared library

First, you need to create a simple C shared library. This library will contain a function that you will call from your .NET application.

1. Create a new file named `mylib.c` with the following content:

    ```c
    #include <stdio.h>

    void greet() {
        printf("Hello from the C library!\n");
    }
    ```

2. Compile the C file into a shared library:

    ```bash
    gcc -shared -o libmylib.so -fPIC mylib.c
    ```

   This will generate a shared library file (`libmylib.so`).

## Step 2: Use the C library in your .NET application

Now that you have a shared library, you can use it in your .NET application.

1. In your OrchardCore application, create a new class file named `NativeMethods.cs`:

    ```csharp
    using System;
    using System.Runtime.InteropServices;

    public static class NativeMethods
    {
        [DllImport("mylib", EntryPoint = "greet")]
        public static extern void Greet();
    }
    ```

2. Call the `Greet` method from your application. For example, you can add the following code to your main program or a controller:

    ```csharp
    using OrchardCore.Logging;

    var builder = WebApplication.CreateBuilder(args);

    builder.Host.UseNLogHost();

    builder.Services
        .AddOrchardCms()
        // // Orchard Specific Pipeline
        // .ConfigureServices( services => {
        // })
        // .Configure( (app, routes, services) => {
        // })
    ;

    var app = builder.Build();

    Console.WriteLine("Calling native greet..."); // NEW INTEROP LINE
    NativeMethods.Greet();                        // NEW INTEROP LINE

    if (!app.Environment.IsDevelopment())
    {
        app.UseExceptionHandler("/Error");
        // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
        app.UseHsts();
    }

    app.UseHttpsRedirection();
    app.UseStaticFiles();

    app.UseOrchardCore();

    app.Run();
    ```

3. Ensure that dotnet can find your shared library:

```bash
```

## Step 3: Run your application

Now when you run `dotnet run`, you will see

```bash
Calling native greet...
Hello from the C library!
```

in the logging output.

## Compiling for Arm

If you are compiling for Arm directly on Azure Cobalt, the compiler understands what default processor optimizations it should use, and you can compile as done in Step 1 above. However, if you are cross-compiling in your build pipeline, you should specify `-mcpu=neoverse-n2 -O3` when running the cross-compiler:

```bash
aarch64-linux-gnu-gcc -mcpu=neoverse-n2 -O3 -shared -o libmylib.so -fPIC mylib.c
```

The `-mcpu=neoverse-n2` flag specifies the Cobalt architecture, and `-O3` ensures that maximum optimizations are completed (including SIMD opimizations).

In the next section, you will explore the tradeoffs of building native AOT arm64 binaries.
