---
# User change
title: Create a custom example

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

The IP Explorer simulation systems provide a software package to allow you to create your own benchmarking application.

Sample projects are provided, including a C source file that allows you to focus on the area of code of interest (`marked` code).

## Build machine

In order to build and test your application before uploading to IP Explorer, you should use a Linux machine with the appropriate compiler(s) ([Arm GNU Toolchain](/install-guides/gcc/arm-gnu/) or [Arm Compiler for Embedded](/install-guides/armclang/)) installed.

## Download the software package

Clone the following repository to get the latest software package.

```command
git clone https://gitlab.arm.com/ip-explorer/user-software
```

Navigate to the `Applications` folder, and locate the `app-template` folder.

Copy this folder to create your own example (`my_example` in the below).

Rename the `app-template.c` file to match the name of your project:

```command
cd user-software/benchmark-package/Applications
cp -r app-template my_example
cd my_example
mv app-template.c my_example.c
```

## Modify source with your code

Using your preferred text editor, open the above `my_example.c`.

The source is a C `main()` function, with two (optional, but recommended) functions, `start_marker()` and `stop_marker()`.

These functions define the `marked` code from the cycle count reports, and can be used to isolate the key part of your code that you wish to benchmark, while allowing set up code, or `printf()` like statements to output results to not be considered in the benchmark.

Modify the source as appropriate for your code and save. You can use the example code from the documentation here:

```C
int main()
{
    double a = 3.14;
    double b = 6.023456;
    double product;

    (void) start_marker();
    product = a * b;
    (void) stop_marker();

    printf("Product = %.2lf\n", product);

    return 0;
}
```

## Define the simulation systems you wish to run the code on

Return to the `benchmark-package` directory of the software package.

Note the folder names within the `Systems` directory, which define the known simulations that the code can be run on.

```output
$ ls Systems/
a32x4_nic-400       a53x2_nic-400_64kb  m0px1_cache    m23x1-axi4    m4x1_cache_2kb    m52x1-axi4  r52x1_nic-400
a34x4_nic-400       a55_nic400_cci_500  m0px1_nocache  m33x1-axi4    m4x1_cache_64kb   m55x1-axi4  r5x1_nic-400
a35x4_nic-400       a5x4_nic-400        m0x1_cache     m3x1_cache    m4x1_nocache_ws0  m7x1-axi4   r82x1-axi4
a53x2_nic-400_32kb  a7x4_nic-400        m0x1_nocache   m3x1_nocache  m4x1_nocache_ws4  m85x1-axi4  r8x4_nic-400
```
We shall use `m0x1_nocache` and `m7x1-axi4`.

Open `sw_options.json` with an appropriate text editor. Enter details of your custom application.

```json
{
        "software_name": ["my_example"],
        "software_description":["This is my custom software example"],
        "software_version": ["1.0"],
        "valid_compilers": ["AC6","GCC"],
        "compiler_version": ["6.18", "11.2.1"],
        "valid_systems": ["m0x1_nocache", "m7x1-axi4"]
}
```

## Create software package to upload

Use the `app_checker` utility to verify that everything is correct. If it is, a `custom-software.tgz` bundle will be created in the `user-software` top level.
```command
./app_checker.py -t
```
```output
INFO: Found possible combination: 'my_example' on 'm0x1_nocache' built with 'AC6'.
INFO: Combination is valid.
INFO: Found possible combination: 'my_example' on 'm0x1_nocache' built with 'GCC'.
INFO: Combination is valid.
INFO: Found possible combination: 'my_example' on 'm7x1-axi4' built with 'AC6'.
INFO: Combination is valid.
INFO: Found possible combination: 'my_example' on 'm7x1-axi4' built with 'GCC'.
INFO: Combination is valid.
INFO: Found 4 valid build combinations in 'sw_options.json'
INFO: The 'sw_options.json' file has no errors.
INFO: Tar file ../custom-software.tgz created.
```
You are now ready to upload your example to IP Explorer.

## (Optional) Test build your application

To ensure the project will build correctly you can test it on your local machine before uploading it:

```command
bash ./build_app.sh my_example m0x1_nocache AC6
```
