---
title: Create your first Windows on Arm application using Microsoft Visual Studio
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Microsoft Visual Studio 

Visual Studio 2022 is an Integrated Development Environment (IDE) developed by Microsoft that empowers developers to build high-performance applications for the Arm architecture. 

You can learn more about [Microsoft Visual Studio on Arm-powered devices](https://learn.microsoft.com/en-us/visualstudio/install/visual-studio-on-arm-devices?view=vs-2022) from the Microsoft Learn website.

There are three editions of Visual Studio 2022 that are tailored to various development needs:
 - Community Edition is a free, fully-featured edition ideal for students, open source contributors, and individual developers.
 - Professional Edition offers professional developer tools, services, and subscription benefits for small teams.
 - Enterprise Edition provides the most comprehensive set of tools and services for large teams and enterprise-level development.

To work out which is the best edition for your needs, see [Compare Visual Studio 2022 Editions](https://visualstudio.microsoft.com/vs/compare/).

{{% notice Note %}}
This Learning Path uses the Community Edition of Visual Studio 2022, but you can also use other editions. 
{{% /notice %}}

Download and install Visual Studio using the [Visual Studio for Windows on Arm](/install-guides/vs-woa/) install guide. Make sure to install C and C++ support and the LLVM compiler. 

## Create a sample project

You are now ready to create a sample Windows on Arm application.

In the interests of ease and simplicity, you are going to create an uncomplicated console application.

On the **Start** window, select **Create a new project**. 

![img1](./figures/vs_new_proj1.png)

In the **Create a new project** window, do the following:

* Select **Console App**.
* Provide a project name, such as `hello-world-1`.
* Click **Next**.

![img2](./figures/vs_new_proj2.png)

After the project is created, you will see a line of `Hello, World!` code in the newly-created C++ file. 

```C++
#include <iostream>

int main()
{
    std::cout << "Hello World!\n";
}
```

Microsoft Visual Studio automatically configures the build environment for the hardware's CPU architecture. However, you will benefit from familiarizing yourself with the relevant settings.

## AArch64 Configuration Settings

Click on the `Debug` drop-down menu, and select `Configuration Manager...`

 ![img4](./figures/vs_console_config1.png)


In the `Project contexts` area you see the platform set to `ARM64`. 

 ![img5](./figures/vs_console_config2.png)

Click `Build -> Build Solution` and your application compiles successfully.

## Run your first Windows on Arm application

Use the green arrow to run the program you just compiled, and you'll see the print statement from your code correctly executed in the console.

 ![img6](./figures/vs_console_exe.png)

You can also use the tools provided by Visual Studio to check the compiled executable.

The [dumpbin](https://learn.microsoft.com/en-us/cpp/build/reference/dumpbin-reference?view=msvc-170) command-line tool is included with Microsoft Visual Studio. It's used to analyze binary files like executable files (.exe), object files (.obj), and dynamic-link libraries (.dll). 

To use `dumpbin` open a Command Prompt with Visual Studio configured by opening Windows search, and looking for `Arm64 Native Tools Command Prompt for VS 2022`. Find and open this application.

A new Command Prompt opens. It's the same as the regular Windows Command Prompt with the addition that Visual Studio tools can be run from the prompt.

Run the command below with the executable you crated as an argument:

```cmd
dumpbin /headers <your exe path>\ConsoleApp1.exe
```

You can see that the file format shows `AA64 machine (ARM64)` in the file header.

 ![img7](./figures/vs_checkmachine.jpeg)

Continue to the next page to build and run a more computation intensive application.