---
# User change
title: "Application execution" 

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Application execution
To run the application on our new target platform, the following steps will be taken:
1. Launch the developer environment
2. Make porting modifications
3. Compile
4. Run

Depending on target platform and compiler, there will be slight differences in how to execute the application.

## QEMU

Create the Dockerfile and then build the cross-platform GCC development environment as described in sections:
* [Development environment - GCC](../4_development_environment#gcc)
* [Development environment - Cross-platform](../4_development_environment#cross-platform)

and run the container on your `x86_64` machine using the following command:
```bash
xhost +local:*
docker run -it --rm --platform linux/aarch64 --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_gcc_example /bin/bash
```

Then follow the instructions from sections:
* [Application porting - Compiler options porting](../3_application_porting#compiler-options-porting)
* [Application porting - x86 intrinsics porting](../3_application_porting#x86-intrinsics-porting)

Finally, compile and run the application.
```bash
cmake -S src -B build
cd build/
make
./sobel_simd_opencv
```

Note: only the container is cross-compiled and the application is natively compiled as it is built inside the emulated `aarch64` environment.

## AWS EC2

Start by configuring the type of Graviton instance. In this example two different Graviton instances were selected. The instructions on how to execute the ported application are the same for both instances.
* Graviton2 (t4g.medium)
  * Ubuntu 22.04.2 LTS,
  * 16GB storage (default is 8GB)
  * Arm Neoverse N1
    * NEON 128b vector width
* Graviton3 (c7g.medium)
  * Ubuntu 22.04.2 LTS
  * 16GB storage (default is 8GB)
  * Arm Neoverse V1
    * SVE 256b vector width
      * SVE can run NEON instructions

For more information on Graviton, see [AWS Graviton Getting Started](https://github.com/aws/aws-graviton-getting-started).

Once the Graviton instance is running, connect to it using `ssh` with the `-X` option to allow for display forwarding. Don't forget to replace `INSERT_KEY.PEM` and `INSERT_GRAVITON_INSTANCE_IP_ADDRESS` before running the command.
```bash
ssh -X -i "INSERT_KEY.PEM" ubuntu@INSERT_GRAVITON_INSTANCE_IP_ADDRESS
```

Install [Docker Engine](https://learn.arm.com/install-guides/docker/docker-engine/) and next launch your GCC/ACfL development environment.

### GCC

Build the native GCC development container as described in sections:
* [Development environment - GCC](../4_development_environment#gcc)
* [Development environment - Native](../4_development_environment#native)

and then run the container.
```bash
docker run --rm -ti --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_gcc_example
```

Now follow the instructions from sections:
* [Application porting - Compiler options porting](../3_application_porting#compiler-options-porting)
* [Application porting - x86 intrinsics porting](../3_application_porting#x86-intrinsics-porting)

Finally, compile and run the application.
```bash
cmake -S src -B build
cd build/
make
./sobel_simd_opencv
```

### ACfL
Start by pulling the ACfL development container,
* [Development environment - ACfL](../4_development-environment#acfl)

then run the container
```bash
docker run --rm -ti --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_acfl_example
```

and install OpenCV inside the container.
```bash
sudo apt-get update && sudo apt-get install -y libopencv-dev
```

Now follow the instructions from sections:
* [Application porting - Compiler options porting](../3_application_porting#compiler-options-porting)
* [Application porting - x86 intrinsics porting](../3_application_porting#x86-intrinsics-porting)

We want to set ACfL as the C/C++ compiler, this is achieved by adding these lines to `CMakeLists.txt`.
```output
set(CMAKE_C_COMPILER "/opt/arm/arm-linux-compiler-23.04_Generic-AArch64_Ubuntu-22.04_aarch64-linux/bin/armclang")
set(CMAKE_CXX_COMPILER "/opt/arm/arm-linux-compiler-23.04_Generic-AArch64_Ubuntu-22.04_aarch64-linux/bin/armclang++")
```

Use the following command to achieve this:
```bash
sed -i "6i set(CMAKE_C_COMPILER\ \"/opt/arm/arm-linux-compiler-23.04_Ubuntu-22.04/bin/armclang\")" src/CMakeLists.txt
sed -i "7i set(CMAKE_CXX_COMPILER\ \"/opt/arm/arm-linux-compiler-23.04_Ubuntu-22.04/bin/armclang++\")\n" src/CMakeLists.txt
```

Finally, compile and run the application.
```bash
cmake -S src -B build
cd build/
make
./sobel_simd_opencv
```

## Raspberry Pi 4

On the Raspberry Pi 4 the following is assumed:
* Running Raspberry Pi OS (64-bit)
* Docker is installed
  * See [Install Docker Engine on Debian](https://docs.docker.com/engine/install/debian/)
* uSD card inserted
* Connected to a display
* Mouse and keyboard
* An internet connection

The steps are then the same as for the Graviton GCC and ACfL sections:
* [Application execution - GCC](#gcc)
* [Application execution - ACfL](#acfl)

Now that we've run the ported application on all three of our hardware targets, let's take a look at the results!