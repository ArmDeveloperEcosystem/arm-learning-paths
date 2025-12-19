---
title: Install Redis
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Redis on GCP VM
This section provides a complete guide to installing Redis on a GCP SUSE virtual machine. You will build Redis from source to ensure compatibility with the Arm architecture and to enable TLS support for secure connections.

## Prerequisites
Before building Redis, update your package repositories and install essential build tools and libraries:

```console
sudo zypper refresh
sudo zypper install -y gcc gcc-c++ make tcl openssl-devel wget
```
## Download and extract Redis source code

Now download the Redis 8.2.2 source archive directly from the official GitHub repository, extract the contents, and navigate into the extracted directory for compilation:

```console
wget https://github.com/redis/redis/archive/refs/tags/8.2.2.tar.gz
tar -xvf 8.2.2.tar.gz
cd redis-8.2.2
```
{{% notice Note %}}
In this blog [Improve Redis performance up to 36% by deploying on Alibaba Cloud Yitian 710 instances](https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/improve-redis-performance-by-deploying-on-alibaba-cloud-yitian-710-instances), Redis version 6.0.9 is recommended for deployment on Arm-based Alibaba Yitian 710 instances. These instances deliver up to 36% higher throughput and 20% lower cost compared to equivalent x86-based ECS instances, making it a more efficient and cost-effective choice for Redis workloads.

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Redis version 6.0.9, the minimum recommended on the Arm platforms.
{{% /notice %}}

Clean any previous build artifacts (if any):

```console
make distclean
```
This removes any residual files from a previous build, ensuring a clean build environment.

Build Redis dependencies and compile Redis:

Redis relies on several third-party libraries (such as hiredis, jemalloc, and lua) to optimize performance and functionality. After building dependencies, the Redis source is compiled with BUILD_TLS=yes, enabling support for encrypted TLS connections.

```console
cd deps
sudo make hiredis jemalloc linenoise lua fast_float
cd ..
sudo make BUILD_TLS=yes
```

{{% notice Note %}}
The `BUILD_TLS=yes` flag enables TLS (SSL) support for secure Redis connections.
{{% /notice %}}

## Verify Redis binary

After a successful build, check that the `redis-server` binary exists:

```
cd src
ls -l redis-server
```

The output is similar to:

```output
-rwxr-xr-x 1 root root 17869216 Oct 23 11:48 redis-server
```
This confirms that Redis compiled successfully and that the `redis-server` binary is present in the `/src` directory. The file’s permissions indicate it is executable.

## Install Redis system-wide
Use the following command to install Redis binaries (`redis-server` and `redis-cli`) globally, making them accessible from any directory:

```console
sudo make install
```

This places `redis-server` and `redis-cli` into `/usr/local/bin`, allowing you to run Redis commands from anywhere on your system.

Verify installation paths:

```console
which redis-server
which redis-cli
```

The expected output is:

```output
/usr/local/bin/redis-server
/usr/local/bin/redis-cli
```

This confirms that Redis binaries are installed in your system path.

### Verify installation

Check Redis versions:

```console
redis-server --version
redis-cli --version
```

The expected output is:

```output
redis-server --version
Redis server v=8.2.2 sha=00000000:1 malloc=jemalloc-5.3.0 bits=64 build=72ba144d8c96c783
$ redis-cli --version
$ redis-cli 8.2.2
```
This confirms that Redis has been installed and is ready for use.
