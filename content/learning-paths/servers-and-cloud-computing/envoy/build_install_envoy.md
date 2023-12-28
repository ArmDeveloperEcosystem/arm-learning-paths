---
# User change
title: "Build and install Envoy"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Envoy is an open-source, high-performance proxy service initially developed by Lyft and now maintained by the Cloud Native Computing Foundation (CNCF). It is designed to be a scalable, flexible, and low-latency service proxy, particularly well-suited for microservices architectures and containerized applications.

### Before you begin

In this section you will learn about different options to install, configure and connect to your Envoy server. If you already know how to deploy a Envoy server, you can skip this learning path, and instead explore the [Learn how to Tune Envoy](/learning-paths/servers-and-cloud-computing/envoy_tune/) learning path. 

### Arm deployment options

There are numerous ways to deploy Envoy on Arm: bare metal, cloud VMs, or the various Envoy services that cloud providers offer. If you already have an Arm system, you can skip over this subsection and continue with installation options.

* Arm Cloud VMs
  * [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp) learning path
  * [AWS EC2](https://aws.amazon.com/ec2/)
    * [Deploy Arm Instances on AWS using Terraform](/learning-paths/servers-and-cloud-computing/aws-terraform) learning path
  * [Azure VMs](https://azure.microsoft.com/en-us/products/virtual-machines/)
    * [Deploy Arm virtual machines on Azure with Terraform](/learning-paths/servers-and-cloud-computing/azure-terraform) learning path
  * [GCP Compute Engine](https://cloud.google.com/compute)
    * [Deploy Arm virtual machines on Google Cloud Platform (GCP) using Terraform](/learning-paths/servers-and-cloud-computing/gcp) learning path
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
* Additional options are listed in the [Get started with Servers and Cloud Computing](/learning-paths/servers-and-cloud-computing/intro) learning path

### Envoy installation options

You can install Envoy in a few different ways. The recommended ways are to download the latest Envoy [binary](https://github.com/envoyproxy/envoy/releases) for your target Arm platform or build it from source. You can follow the steps in this section to build envoy from source.

## Install Bazel

To build Envoy from source you will use Bazel.

On your Ubuntu Linux Arm machine, run the following commands to install Bazel:

```console
sudo wget -O /usr/local/bin/bazel https://github.com/bazelbuild/bazelisk/releases/latest/download/bazelisk-linux-$([ $(uname -m) = "aarch64" ] && echo "arm64" || echo "amd64")
sudo chmod +x /usr/local/bin/bazel
```

## Install external dependencies

On your Ubuntu Linux Arm machine, install the external dependencies as shown below:

```console
sudo apt update \
sudo apt-get install \
   autoconf \
   curl \
   libtool \
   patch \
   python3-pip \
   unzip \
   git \
   virtualenv
```

### Build Envoy from the source code

You will need to download and extract the prebuilt Clang+LLVM package from [LLVM official site](http://releases.llvm.org/download.html) as shown:

```console
cd ~/
wget https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.1/clang+llvm-17.0.1-aarch64-linux-gnu.tar.xz
tar -xvf clang+llvm-17.0.1-aarch64-linux-gnu.tar.xz
```

You can now build Envoy from the source as shown below:

```console
git clone https://github.com/envoyproxy/envoy.git
cd envoy
bazel/setup_clang.sh ~/clang+llvm-17.0.1-aarch64-linux-gnu
echo "build --config=clang" >> user.bazelrc
bazel build -c opt envoy.stripped --jobs=$(nproc)
```

After a successful build, the output should look similar to:

```output
INFO: Elapsed time: 13960.122s, Critical Path: 157.25s
INFO: 14755 processes: 6000 internal, 8753 linux-sandbox, 1 local, 1 worker.
INFO: Build completed successfully, 14755 total actions
```

With Envoy now installed on your Arm machine running Ubuntu, you can follow the steps in the next section to run Envoy as a service.


