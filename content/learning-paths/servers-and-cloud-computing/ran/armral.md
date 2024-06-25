---
# User change
title: "Build and run ArmRAL"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

The Arm RAN Acceleration Library (ArmRAL) contains a set of functions for accelerating telecommunications applications such as, but not limited to, 5G Radio Access Networks (RANs).

ArmRAL is an open-source code base under the permissive BSD license.

## Before you begin

A development machine is required to build and run ArmRAL.

You can use a local Arm server or [Arm laptop or desktop machine](/learning-paths/laptops-and-desktops/intro/) as a development platform.

Alternatively, you can use an Arm-based instance from a cloud service provider. Refer to [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/) for cloud options.

The instructions are for Ubuntu or Debian Linux distributions.

## Install necessary build tools

Install the necessary tools to build the code:

```bash { env="DEBIAN_FRONTEND=noninteractive" }
sudo apt update
sudo -E apt install -y build-essential cmake linux-tools-common gcovr doxygen
```

## Download the source code

The source code is available from the [GitLab repository](https://gitlab.arm.com/networking/ral/-/tree/main)

Use `git` to download the code:

```bash
git clone https://git.gitlab.arm.com/networking/ral.git
```

## Create a build folder

Navigate to the source directory and create an empty build directory: 

```bash
cd ral
mkdir build
cd build
```

## Inspect the Arm processor features

The Arm Architecture defines three vector processing technologies.

- [Neon](https://developer.arm.com/Architectures/Neon) (`asimd`)
- [Scalable Vector Extension](https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions) (`sve`)
- [SVE2](https://developer.arm.com/documentation/102340/) (`sve2`)

To check which features are available on your platform, use:

```bash
cat /proc/cpuinfo
```

Look at the flags and check for values `asimd`, `sve`, or `sve2`.

Use the features available on your hardware when you run `cmake` in the next section.

## Configure the build

If your platform supports only Neon (`asimd`), set up the build with:

```bash { cwd="ral/build" }
cmake -DBUILD_TESTING=On -DARMRAL_ARCH=NEON  ..
```

If you have SVE support, set up the build with:

```console
cmake -DBUILD_TESTING=On -DARMRAL_ARCH=SVE  ..
```

If you have SVE2 support, set up the build with:

```console
cmake -DBUILD_TESTING=On -DARMRAL_ARCH=SVE2  ..
```

The default install location is `/usr/local`. If you do not have write access to this directory, set a different installation location by adding `-DCMAKE_INSTALL_PREFIX=<path>` to the `cmake` command.

For example:

```console
cmake -DBUILD_TESTING=On -DARMRAL_ARCH=SVE -DCMAKE_INSTALL_PREFIX=/home/ubuntu/armral ..
```

## Build the code

Build the library using `make`:

```bash { cwd="ran/build" }
make
```

## Install the library

Install the library: 

```bash { cwd="ran/build" }
sudo make install
```

## Run the tests

Build and run the supplied benchmark example by running:

```bash { cwd="ral/build",ret_code="0" }
make check
```

If everything runs correctly you see the message:

```output
100% tests passed, 0 tests failed out of 56
```

You will see errors if you build for optimization features that are not available:

The output will be similar to:

```output
...

61/64 Test #61: ldpc_awgn ............................   Passed  255.05 sec
      Start 62: modulation_awgn
62/64 Test #62: modulation_awgn ......................   Passed   28.39 sec
      Start 63: polar_awgn
63/64 Test #63: polar_awgn ...........................   Passed  390.17 sec
      Start 64: turbo_awgn
64/64 Test #64: turbo_awgn ...........................   Passed  190.39 sec

100% tests passed, 0 tests failed out of 64

Total Test time (real) = 1095.82 sec
[100%] Built target check

...
```

You are now ready to create applications with ArmRAL.

For a full description of available build options, see the [Arm RAN Acceleration Library Reference Guide](https://developer.arm.com/documentation/102249).