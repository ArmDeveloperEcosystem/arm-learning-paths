---
# User change
title: "Build and run in the cloud"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

The Arm RAN Acceleration Library (ArmRAL) contains a set of functions for accelerating telecommunications applications such as, but not limited to, 5G Radio Access Networks (RANs).

## Select your target hardware

### Local development platform

It may be that you have access to application specific hardware already. Else you may wish to use an [Arm-based desktop](/learning-paths/desktop-and-laptop/intro/).

### Launch an Arm-based instance from Cloud Service Provider

Most Cloud Service Providers (CSPs) now provide Arm-based instances.

See [these instructions](/learning-paths/server-and-cloud/csp/) to launch an Arm-based instance.

## Install necessary build tools

Full details are given in the `Tools` section of the supplied release notes.
```bash { env="DEBIAN_FRONTEND=noninteractive" }
sudo apt update
sudo -E apt install -y build-essential cmake linux-tools-common gcovr doxygen
```
## Download and unpack the library

The library can be downloaded from the [Arm Developer](https://developer.arm.com/downloads/-/arm-ran-acceleration-library) website.

Untar the package to your instance:
```bash { pre_cmd="wget https://developer.arm.com/-/media/Arm%20Developer%20Community/Downloads/Arm%20RAN%20Acceleration%20Library/arm-ran-acceleration-library-23.04-aarch64.tar.gz" }
tar -xf arm-ran-acceleration-library-23.04-aarch64.tar.gz
```
### Create build folder
Navigate into the library directory, then create and enter a build folder (naming is arbitrary)
```bash
cd arm-ran-acceleration-library-23.04
mkdir build
cd build
```
## Build the library as appropriate

The Arm Architecture defines three vector processing technologies.
- [Neon](https://developer.arm.com/Architectures/Neon) (Advanced SIMD - `asimd`)
- [Scalable Vector Extension](https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions) (SVE)
- and [SVE2](https://developer.arm.com/documentation/102340/)

To inspect what features are available on your platform, use:
```bash
cat /proc/cpuinfo
```
### Configure build

We shall build the library along with the supplied validation tests.

If your platform supports (only) Neon, set up build with:
```bash { cwd="arm-ran-acceleration-library-23.04/build" }
cmake -DBUILD_TESTING=On -DARMRAL_ARCH=NEON  ..
```

If you have SVE support, set up build with:
```console
cmake -DBUILD_TESTING=On -DARMRAL_ARCH=SVE  ..
```

If you have SVE2 support, set up build with:
```console
cmake -DBUILD_TESTING=On -DARMRAL_ARCH=SVE2  ..
```

The default install location is `/usr/local`. If you do not have write access to this directory, add:
```console
-DCMAKE_INSTALL_PREFIX=<path>
```

to your `cmake` command line above, for example:
```console
cmake -DBUILD_TESTING=On -DARMRAL_ARCH=SVE -DCMAKE_INSTALL_PREFIX=/home/ubuntu/armral ..
```

For a full description of available build options, see the [Arm RAN Acceleration Library Reference Guide](https://developer.arm.com/documentation/102249).

### Build
To build the library, use:
```bash { cwd="arm-ran-acceleration-library-23.04/build" }
make
```

## Install the library
To install the library, use the command:
```bash { cwd="arm-ran-acceleration-library-23.04/build" }
sudo make install
```

## Build and run tests
To build and run the supplied benchmark example, use:
```bash { cwd="arm-ran-acceleration-library-23.04/build"; ret_code="0" }
make check
```

You will observe run time errors if you build for optimization features that are not available:
```output
...
     Start  5: arm_fir_filter_cs16
5/55 Test  #5: arm_fir_filter_cs16 ..................***Exception: Illegal  0.12 sec
...
```
