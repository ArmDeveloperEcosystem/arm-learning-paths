---
title: Integrate a C shared library into your .NET OrchardCore app 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Create a C shared library

In this section, you’ll integrate a simple C shared library into your .NET OrchardCore application, by doing the following:

- Write a C function
- Compile it into a shared object (`.so`)
- Call it from C# using `DllImport`

This allows you to reuse existing C code and improve performance by accessing native functionality.

Create a file named `mylib.c` with the following:

```c
#include <stdio.h>

void greet() {
    printf("Hello from the C library!\n");
}
```

Compile the C file into a shared library:

```bash
gcc -shared -o libmylib.so -fPIC mylib.c
```

This creates a shared object file named `libmylib.so` which your .NET application can call at runtime.

## Use the C library in your .NET application

Now that you have a shared library, you can use it in your .NET application.

In your OrchardCore application, create a new class file named `NativeMethods.cs`:

```csharp
using System;
using System.Runtime.InteropServices;

public static class NativeMethods
{
    [DllImport("mylib", EntryPoint = "greet")]
    public static extern void Greet();
}
```
{{% notice Note %}}
On Linux, the `DllImport("mylib")` attribute resolves to `libmylib.so`. On Windows, the runtime would look for `mylib.dll`, and on macOS, `libmylib.dylib`.
{{% /notice %}}

Call the `Greet` method from your application. For example, you can add the following code to your main program `Program.cs` as shown:

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

Ensure that dotnet can find your shared library:

```bash
export LD_LIBRARY_PATH=$(pwd):$LD_LIBRARY_PATH
```

## Run your application

When you run `dotnet run`, you’ll see the following output:

```bash
Calling native greet...
Hello from the C library!
```

## Compiling for Arm

If you are compiling for Arm directly on Azure Cobalt, the compiler understands the default processor optimizations it should use, and you can compile in the same way as above. 

However, if you are cross-compiling in your build pipeline, you should specify `-mcpu=neoverse-n2 -O3` when running the cross-compiler:

```bash
aarch64-linux-gnu-gcc -mcpu=neoverse-n2 -O3 -shared -o libmylib.so -fPIC mylib.c
```

The `-mcpu=neoverse-n2` flag specifies the Cobalt architecture, and `-O3` ensures that maximum optimizations are completed (including SIMD optimizations).

In the next section, you’ll make your native interop cross-platform by using the AnyCPU feature and runtime dispatch strategies.
