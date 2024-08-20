---
title: Download and build the PMUv3 plugin
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To get started, navigate to an empty directory on your Arm Linux computer and prepare the PMUv3 plugin. 

## User space PMU access

To use the PMUv3 plugin, you need permission to access the performance counters from userspace applications. 

To enable userspace access until the next reboot, run the following:

```console
sudo sysctl kernel/perf_user_access=1
```

If access is allowed, the command output is as follows:

```output
kernel.perf_user_access = 1
```

You can check if userspace access is enabled any time by running the following:

```console
cat /proc/sys/kernel/perf_user_access
```

A value of 1 means userspace access is enabled and a value of 0 indicates that it's disabled. 

To permanently change the value, add the following line to the file `/etc/sysctl.conf`:

```console
kernel.perf_user_access = 1
```

## Directory structure

The instructions assume you have the Linux kernel source tree, the PMUv3 plugin source code, and your test application in parallel. If you have a different directory structure, you may need to adjust the build commands to find the header files and libraries. 

Here are the 3 directories you will create:

```output
./linux
./PMUv3_plugin
./test
```

## Linux kernel libraries

The PMUv3 plugin requires two Linux Perf related libraries. 

The easiest way to get them is to build them from the Linux source tree.

Download the Linux source using the `git` command as follows:

```console
git clone git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git
```

The Linux kernel repository is large so it will take some time to download. 

Install the GNU compiler. If you are running on Ubuntu, you can run the following:

```console
sudo apt install build-essential -y
```

When the Linux source download is complete, build the Perf libraries `libperf.a` and `libapi.a`:

```console
pushd linux/tools/lib/perf
make
popd
```

### Build the PMUv3 plugin

Get the PMUv3 plugin source code by running:

```console
git clone https://github.com/GayathriNarayana19/PMUv3_plugin.git
```

Copy the Perf libs:

```console
cd PMUv3_plugin
cp ../linux/tools/lib/perf/libperf.a .
cp ../linux/tools/lib/api/libapi.a  .
```

Build the PMUv3 plugin:

```console
gcc -c pmuv3_plugin.c -I ../linux/tools/lib/perf/include -o pmuv3_plugin.o
gcc -c pmuv3_plugin_bundle.c -I ../linux/tools/lib/perf/include -o pmuv3_plugin_bundle.o
g++ -c processing.cpp -I ../linux/tools/lib/perf/include -o processing.o
gcc -c processing.c -I ../linux/tools/lib/perf/include -o processing_c.o
ar rcs libpmuv3_plugin.a pmuv3_plugin.o
ar rcs libpmuv3_plugin_bundle.a pmuv3_plugin_bundle.o processing.o
ar rcs libpmuv3_plugin_bundle.a pmuv3_plugin_bundle.o  processing_c.o
```

To do the static library compilation, run `./build.sh` from **/home/ubuntu/ut_integration/PMUv3_plugin/directory**.
Run `./build.sh` if you are going to instrument around a C++ codebase. If it is a C codebase, comment line 19 of `build.sh`, uncomment line 20, and run `./build.sh`.

You are now ready to use the PMUv3 plugin in your software project. You will now need to add the library `-lpmuv3_plugin_bundle.a` to your C/C++ link command. You can use `-I` to point to the plugin files and `-L` to point to the library location. 

Continue to the next section see the options for instrumenting code.
