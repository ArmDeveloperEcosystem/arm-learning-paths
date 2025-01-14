---
# User change
title: "Evaluating performance on Arm hardware (Optional)" 

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this section you will learn alternative ways to build the development environment and compile with a different compiler, on Arm hardware. 

The changes you made in `main.cpp` and `CMakeLists.txt` in [Application porting](/learning-paths/embedded-and-microcontrollers/migration/5_application_porting) stay the same when running on actual Arm hardware.

## Arm hardware

The following Arm hardware has been selected due to their high availability.
* Remote hardware
  * [AWS EC2](https://aws.amazon.com/ec2/) instances are easily accessible
* Physical hardware
  * [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) is a popular off-the-shelf single-board computer

### AWS EC2 with Graviton processors

AWS EC2 instances with Graviton processors use the `aarch64` architecture. Graviton2 and Graviton3 have different vector engine technologies.

* Graviton2 (c6g.medium)
  * Ubuntu 22.04.2 LTS,
  * 16GB storage (default is 8GB)
  * [Arm Neoverse N1](https://www.arm.com/products/silicon-ip-cpu/neoverse/neoverse-n1)
    * 2 x NEON engine 128b vector width
* Graviton3 (c7g.medium)
  * Ubuntu 22.04.2 LTS
  * 16GB storage (default is 8GB)
  * [Arm Neoverse V1](https://www.arm.com/products/silicon-ip-cpu/neoverse/neoverse-v1)
    * 2 x SVE engine 256b vector width (4 x NEON engine 128b vector width support)

For more information on Graviton, refer to [Getting Started with AWS](/learning-paths/servers-and-cloud-computing/csp/aws/) and the [AWS Graviton Technical Guide](https://github.com/aws/aws-graviton-getting-started).

Create a Graviton instance and connect using `ssh` with the `-X` option to allow for display forwarding. 

Replace `INSERT_KEY_PEM_FILE` and `INSERT_GRAVITON_INSTANCE_IP_ADDRESS` with your SSH key and public IP address: 

```bash
ssh -X -i "INSERT_KEY_PEM_FILE" ubuntu@INSERT_GRAVITON_INSTANCE_IP_ADDRESS
```

Install [Docker Engine](/install-guides/docker/docker-engine/) on the EC2 instance.

### Raspberry Pi 4

The Raspberry Pi is setup just like a normal desktop computer and the following is assumed:
* Running Raspberry Pi OS (64-bit)
* Docker is installed
* MicroSD card inserted
* Display, mouse and keyboard connected
* Internet connection

Refer to [Get started with the Raspberry Pi 4](/learning-paths/embedded-and-microcontrollers/rpi/) for more information about using the Raspberry Pi 4 for software development, including how to install Docker engine. 

## Development environment and application porting

Use the same Dockerfile as before, see [Development environment](/learning-paths/embedded-and-microcontrollers/migration/4_development_environment#gcc-container).

You can build the development environment natively on Arm using `docker build` instead of `docker buildx`. 

To build the GCC development environment, run the following command:

```bash
docker build -t sobel_gcc_example .
```

Run the container:

```bash
docker run --rm -ti --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_gcc_example
```

Follow the same steps to port the application as described in [Application porting](/learning-paths/embedded-and-microcontrollers/migration/5_application_porting/) to build and run the application.

### ACfL

In addition to the GCC development environment, you can also use Arm Compiler for Linux ([ACfL](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux)). 

Pull the development container from the `armswdev` repository and rename it `sobel_acfl_example`:

```bash
docker pull armswdev/arm-compiler-for-linux
docker tag armswdev/arm-compiler-for-linux sobel_acfl_example
```

Run the container:

```bash
docker run --rm -ti --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_acfl_example
```

The container doesn't have OpenCV.

Install OpenCV by running the command:

```bash
sudo apt-get update && sudo apt-get install -y libopencv-dev
```

Follow the same steps to port the application as described in [Application porting](/learning-paths/embedded-and-microcontrollers/migration/5_application_porting). 

To use Arm Compiler for Linux you need to change the compiler in `CMakeLists.txt` as shown below:

```output
set(CMAKE_C_COMPILER "/opt/arm/arm-linux-compiler-23.04_Generic-AArch64_Ubuntu-22.04_aarch64-linux/bin/armclang")
set(CMAKE_CXX_COMPILER "/opt/arm/arm-linux-compiler-23.04_Generic-AArch64_Ubuntu-22.04_aarch64-linux/bin/armclang++")
```

Make the changes by running the following command:

```bash
sed -i "6i set(CMAKE_C_COMPILER\ \"/opt/arm/arm-linux-compiler-23.04_Ubuntu-22.04/bin/armclang\")" src/CMakeLists.txt
sed -i "7i set(CMAKE_CXX_COMPILER\ \"/opt/arm/arm-linux-compiler-23.04_Ubuntu-22.04/bin/armclang++\")\n" src/CMakeLists.txt
```

## Application compilation and execution

Compile and run the application:

```bash
cmake -S src -B build
cd build/
make
./sobel_simd_opencv
```

## Results

The output is the same as when running using QEMU. A noticeable difference compared to QEMU is that the _SIMD_ implementation runs faster, which is expected. QEMU should not be used for performance measurement purposes.

In the results presented below, a value >1 is faster and a value <1 is slower in comparison to the normalized value. In short, higher values are better.

### AWS EC2

| | Graviton2 | | Graviton3 | |
| --- | --- | --- | --- | --- | --- | --- |
| Compiler | GCC 12.2.0 | ACfL 22.1 | GCC 12.2.0 | ACfL 22.1 |
| Non-SIMD | 1.0 | 1.0 | 1.7 | 1.8 |
| SIMD     | 3.4 | 3.8 | 5.8 | 6.7 |
| OpenCV   | 0.3 | 0.3 | 0.4 | 0.5 |

The results in the table above have been normalized to the _Graviton2 Non-SIMD_ value, giving the relative speed-up. 

You observe the following:
* Graviton3 runs the Sobel filter workload faster than Graviton2
* ACfL performs slightly better than GCC for the _SIMD_ implementation of the Sobel filter

### Raspberry Pi 4

| | Raspberry Pi 4 | |
| --- | --- | --- |
| Compiler | GCC 11.3.0 | ACfL 22.1 |
| Non-SIMD | 1.0 | 0.9 |
| SIMD     | 2.7 | 3.0 |
| OpenCV   | 0.3 | 0.3 |  

The results in the table above have been normalized to the _Raspberry Pi 4 Non-SIMD_ value, giving the relative speed-up. 

You observe the following:
* ACfL performs slightly better than GCC for the _SIMD_ implementation of the Sobel filter
