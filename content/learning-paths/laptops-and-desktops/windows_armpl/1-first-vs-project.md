---
title: Create a Windows on Arm application
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Create a sample project

You are now ready to create a Windows on Arm application.

For your first project, you will create a simple console application.

As shown in Figure 1, go to the **Start** window, and select **Create a new project**.  

![vs_new_proj1.png alt-text#center](./figures/vs_new_proj1.png "Figure 1: Create a new project.")

As shown in Figure 2, in the **Configure your new project** window, do the following:

* Select **Console App**.
* Provide a project name, such as `ConsoleApp1`.
* Click **Next**.

![img2 alt-text#center](./figures/vs_new_proj2.png "Figure 2: Configure your new project.")

After you have created the project, you will see a line of `Hello, World!` code in the newly-created C++ file. 

```C++
#include <iostream>

int main()
{
    std::cout << "Hello World!\n";
}
```

Whilst Microsoft Visual Studio automatically configures the build environment for the hardware of the CPU architecture, you will still benefit from familiarizing yourself with the relevant configuration settings and learning what to use.

## ARM64 Configuration Settings

Click on the **Debug** drop-down menu, and select **Configuration Manager...**

 ![img4](./figures/vs_console_config1.png)


In the **Project contexts** area, you will see the platform set to `ARM64`. 

 ![img5](./figures/vs_console_config2.png)

Click **Build**, then **Build Solution**, and your application compiles successfully.

## Run your first Windows on Arm application

Use the green arrow to run the program you compiled, and you will see the print statement from your code correctly executed in the console.

 ![img6](./figures/vs_console_exe.png)

You can also use the tools provided by Visual Studio to check the compiled executable.

The [dumpbin](https://learn.microsoft.com/en-us/cpp/build/reference/dumpbin-reference?view=msvc-170) command-line tool is included with Microsoft Visual Studio. You can use it to analyze binary files such as executable files (.exe), object files (.obj), and dynamic-link libraries (.dll). 

To use `dumpbin`, open a command prompt with Visual Studio configured by opening Windows search, and look for `Arm64 Native Tools Command Prompt for VS 2022`. Find this application, and open it.

A new command prompt opens. It is the same as the regular Windows command prompt, but with the added benefit that you can run Visual Studio tools from the prompt.

Run the command below, replacing the text with the details of the executable that you created as an argument:

```cmd
dumpbin /headers <your exe path>\ConsoleApp1.exe
```

You can see that the file format shows `AA64 machine (ARM64)` in the file header.

 ![img7](./figures/vs_checkmachine.jpeg)

Continue to the next page to build and run a more computation-intensive application.