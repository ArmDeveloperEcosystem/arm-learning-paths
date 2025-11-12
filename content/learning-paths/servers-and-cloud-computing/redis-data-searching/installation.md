---
title: Install Redis
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Redis on GCP VM
This section provides a complete guide to installing Redis on a **GCP SUSE virtual machine**. Redis will be built from source to ensure compatibility with the Arm architecture and to enable TLS support for secure connections.

### Prerequisites
Before building Redis, update your package repositories and install essential build tools and libraries.

```console
sudo zypper refresh
sudo zypper install -y gcc gcc-c++ make tcl openssl-devel wget
```
### Download and Extract Redis Source Code
This step downloads the Redis 8.2.2 source archive directly from the official GitHub repository, extracts the contents, and navigates into the extracted directory for compilation.

```console
wget https://github.com/redis/redis/archive/refs/tags/8.2.2.tar.gz
tar -xvf 8.2.2.tar.gz
cd redis-8.2.2
```
{{% notice Note %}}
In [this](https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/improve-redis-performance-by-deploying-on-alibaba-cloud-yitian-710-instances) blog, Redis version 6.0.9 is recommended for deployment on Arm-based Alibaba Yitian 710 instances, which deliver up to 36% higher throughput and 20% lower cost compared to equivalent x86-based ECS instances, making it a more efficient and cost-effective choice for Redis workloads.

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Redis version 6.0.9, the minimum recommended on the Arm platforms.
{{% /notice %}}

### Build Redis with TLS Support
**Clean any previous build artifacts (if any):**

```console
make distclean
```
This removes any residual files from a previous build, ensuring a clean build environment.

**Now build Redis dependencies and compile Redis:**

Redis relies on several third-party libraries (such as hiredis, jemalloc, and lua) to optimize performance and functionality. After building dependencies, the Redis source is compiled with BUILD_TLS=yes, enabling support for encrypted TLS connections.

```console
cd deps
sudo make hiredis jemalloc linenoise lua fast_float
cd ..
sudo make BUILD_TLS=yes
```
Note: The BUILD_TLS=yes flag enables TLS (SSL) support for secure Redis connections.

### Verify Redis Binary
After a successful build, check that the redis-server binary exists:

```
cd src
ls -l redis-server
```

You should see a file similar to:

```output
-rwxr-xr-x 1 root root 17869216 Oct 23 11:48 redis-server
```
This confirms that Redis compiled successfully and that the `redis-server` binary is present in the `/src` directory. The file’s permissions indicate it is executable.

### Install Redis System-Wide
This command installs Redis binaries (`redis-server` and `redis-cli`) into system-wide directories (typically `/usr/local/bin`), allowing you to run Redis commands from any location.
To make redis-server and redis-cli accessible globally:

```console
sudo make install
```

Verify installation paths:

```console
which redis-server
which redis-cli
```

Expected:

```output
/usr/local/bin/redis-server
/usr/local/bin/redis-cli
```
This confirms that Redis binaries are available in your system path, verifying a successful installation.

### Verify Installation
Check Redis versions:

```console
redis-server --version
redis-cli --version
```

Output:

```output
redis-server --version
Redis server v=8.2.2 sha=00000000:1 malloc=jemalloc-5.3.0 bits=64 build=72ba144d8c96c783
$ redis-cli --version
$ redis-cli 8.2.2
```
This confirms that Redis has been installed and is ready for use.
