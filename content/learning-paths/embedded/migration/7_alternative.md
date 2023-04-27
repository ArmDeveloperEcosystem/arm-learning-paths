---
# User change
title: "Alternative (Optional)" 

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Alternative (Optional) 

In this section we'll show alternative ways to build the development environment and compile with a different compiler, on Arm hardware. The changes we made in `main.cpp` and `CMakeLists.txt` in [Application porting](../5_application_porting) stay the same when running on actual Arm hardware.

## Arm hardware

The following Arm hardware has been selected for this guide due to their high availability.
* remote hardware
  * [AWS EC2](https://aws.amazon.com/ec2/) instances are easily accessible
* physical hardware
  * [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) is a popular off-the-shelf single-board computer

### AWS EC2

The Graviton instances are Arm and in this example two different have been selected because they use different vector engine technologies.
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

Install [Docker Engine](https://learn.arm.com/install-guides/docker/docker-engine/).

### Raspberry Pi 4

The Raspberry Pi is setup just like a normal dekstop computer and the following is assumed:
* Running Raspberry Pi OS (64-bit)
* Docker is installed
  * See [Install Docker Engine on Debian](https://docs.docker.com/engine/install/debian/)
* uSD card inserted
* Display, mouse and keyboard connected
* Internet connection

## Development environment and application porting

Use the same Dockerfile as before, see [Development environment](4_development_environment#gcc), we'll build our development environment natively on Arm, i.e., not use `buildx`. To build the GCC development environment, run the following command.
```bash
docker build -t sobel_gcc_example .
```

and run the container
```bash
docker run --rm -ti --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_gcc_example
```

Then follow the same steps to port the application as described in [Application porting](../5_application_porting).

### ACfL

In addition to the GCC development environment, we'll introduce the Arm Compiler for Linux ([ACfL](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux)). Pull the development container from the `armswdev` registry
```bash
docker pull armswdev/arm-compiler-for-linux
docker tag armswdev/arm-compiler-for-linux sobel_acfl_example
```

and run it.
```bash
docker run --rm -ti --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_acfl_example
```

The container doesn't have OpenCV support, install it by running the command below.
```bash
sudo apt-get update && sudo apt-get install -y libopencv-dev
```

Then follow the same steps to port the application as described in [Application porting](../5_application_porting). Once the original porting work has been complete, we need to switch compiler in `CMakeLists.txt` as shown below.
```output
set(CMAKE_C_COMPILER "/opt/arm/arm-linux-compiler-23.04_Generic-AArch64_Ubuntu-22.04_aarch64-linux/bin/armclang")
set(CMAKE_CXX_COMPILER "/opt/arm/arm-linux-compiler-23.04_Generic-AArch64_Ubuntu-22.04_aarch64-linux/bin/armclang++")
```

This can be done by running the following command.

```bash
sed -i "6i set(CMAKE_C_COMPILER\ \"/opt/arm/arm-linux-compiler-23.04_Ubuntu-22.04/bin/armclang\")" src/CMakeLists.txt
sed -i "7i set(CMAKE_CXX_COMPILER\ \"/opt/arm/arm-linux-compiler-23.04_Ubuntu-22.04/bin/armclang++\")\n" src/CMakeLists.txt
```

## Application compilation and execution

Now compile and run the application.
```bash
cmake -S src -B build
cd build/
make
./sobel_simd_opencv
```

## Results

The output is the same as when running using QEMU. A noticable difference compared to QEMU is that the _SIMD_ implementation runs faster, which is expected. QEMU should not be used for performance measurement purposes.

In the results presented below, a value >1 is faster and a value <1 is slower in comparison to the normalized value. In short, higher values are better.

### AWS EC2

| | Graviton2 | | Graviton3 | |
| --- | --- | --- | --- | --- | --- | --- |
| Compiler | GCC 12.2.0 | ACfL 22.1 | GCC 12.2.0 | ACfL 22.1 |
| Non-SIMD | 1.0 | 1.0 | 1.7 | 1.8 |
| SIMD     | 3.4 | 3.8 | 5.8 | 6.7 |
| OpenCV   | 0.3 | 0.3 | 0.4 | 0.5 |

The results in the table above have been normalized to the _Graviton2 Non-SIMD_ value, giving the relative speed-up. We observe the following:
* Graviton3 runs the Sobel filter workload faster than Graviton2
* ACfL performs slighlty better than GCC for the _SIMD_ implementaion of the Sobel filter

### Raspberry Pi 4

| | Raspberry Pi 4 | |
| --- | --- | --- |
| Compiler | GCC 11.3.0 | ACfL 22.1 |
| Non-SIMD | 1.0 | 0.9 |
| SIMD     | 2.7 | 3.0 |
| OpenCV   | 0.3 | 0.3 |  

The results in the table above have been normalized to the _Raspberry Pi 4 Non-SIMD_ value, giving the relative speed-up. We observe the following:
* ACfL performs slighlty better than GCC for the _SIMD_ implementaion of the Sobel filter
