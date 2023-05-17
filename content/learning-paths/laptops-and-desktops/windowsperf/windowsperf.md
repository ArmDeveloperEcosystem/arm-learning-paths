---
layout: learningpathall
title: WindowsPerf
weight: 2
---
[WindowsPerf](https://gitlab.com/Linaro/WindowsPerf/windowsperf) is a port of the popular Linux [perf](https://perf.wiki.kernel.org) tool for performance analysis.

Learn more in this [blog](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/announcing-windowsperf) announcing the first release.

## Windows on Arm platform

You will need access to a Windows on Arm (WoA) [Desktop, laptop, or development platform](/learning-paths/laptops-and-desktops/intro/find-hardware).

{{% notice  Virtual Machines%}}
WindowsPerf cannot be used on virtual machines, such as cloud instances.
{{% /notice %}}

## Windows Driver Kit (WDK) and Visual Studio

WindowsPerf relies on `dll` files installed with Visual Studio and installers from the Windows Driver Kit extension.

This Microsoft [article](https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk) explains the installation process.

See also the [Visual Studio on WoA install guide](/install-guides/vs-woa/).

## Download WindowsPerf

The latest release package `windowsperf-bin-<version>.zip` can be downloaded from the Linaro GitLab repository:
```url
https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/releases
```
Unzip the package to your preferred location.

Open a `Windows Command Prompt` terminal as `Administrator`, and navigate to the `windowsperf-bin-<version>` directory.

## Install wperf driver

You can install the kernel driver using either the Visual Studio [devcon](#devcon) utility or the supplied [installer](#devgen).

### Install with devcon {#devcon}

Navigate into the `wperf-driver` folder, and use `devcon` to install the driver:
```command
cd wperf-driver
devcon install wperf-driver.inf Root\WPERFDRIVER
```
You will see output similar to:
```output
Device node created. Install is complete when drivers are installed...
Updating drivers for Root\WPERFDRIVER from <path>\wperf-driver.inf.
Drivers installed successfully.
```
### Install with wperf-devgen {#devgen}

Copy the `wperf-devgen.exe` executable to the `wperf-driver` folder.
```command
copy wperf-devgen.exe wperf-driver\
```
Navigate to the `wperf-driver` folder and run the installer:
```command
cd wperf-driver
wperf-devgen install
```
You will see output similar to:
```output
Executing command: install.
Install requested.
Waiting for device creation...
Device installed successfully.
Trying to install driver...
Success installing driver.
```

## Verify install

You can check everything is working by running the `wperf` executable:
```command
cd ..
wperf -version
```
You should see output similar to:
```output
Component     Version
=========     =======
wperf         2.4.0
wperf-driver  2.4.0
```

## Using wperf
For a complete list of available options enter:
```cmd
wperf -h
```
### Generate a test output

Generate a list of available `events` to be profiled with:
```command
wperf -l
```
Specify the `event` to profile with `-e`. Groups of events, known as `metrics` can be specified with `-m`.

For example, generate a report for Core 0 (`-c 0`) for two seconds (`-d 2`) with:
```command
wperf stat -e cpu_cycles -m icache -c 0 -d 2
```
This will output a report similar to:
```output
        counter value  event name        event idx  event note
        =============  ==========        =========  ==========
          649,973,325  cycle             fixed      e
          277,788,076  l1i_cache         0x14       g0,icache
            7,415,699  l1i_cache_refill  0x01       g0,icache
                    0  l2i_cache         0x27       g0,icache
                    0  l2i_cache_refill  0x28       g0,icache
          813,129,394  inst_retired      0x08       g0,icache
          649,973,325  cpu_cycles        0x11       e
```
Example use cases are provided in the WindowsPerf [documentation](https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/blob/main/wperf/README.md#counting-model).
