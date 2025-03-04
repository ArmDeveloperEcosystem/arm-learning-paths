---
title: Glibc tests on FVP
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare kernel headers

For this step you need the GCC cross-toolchain for the `aarch64-none-linux-gnu` target.
We can use the same toolchain as we used for building the kernel.

Since we are going to use our Glibc on a system running a specific version of the kernel,
we should build the Glibc using the kernel headers of the same version. The Glibc build
scripts automatically pick up your host system's kernel headers unless configured to use
headers from a specific directory. To ensure that we use correct headers for the kernel,
we need to install them from source.

We presume that the kernel source is in the `linux` subfolder, and we will install the
headers in the `linux-headers` subfolder. To do this, run the following commands in the
workspace directory:

```bash
# Make sure that cross GCC is on the PATH
export PATH=/path/to/cross/gcc/bin:${PATH}

# Specify target architecture
export ARCH=arm64

# Specify cross compiler
export CROSS_COMPILE=aarch64-none-linux-gnu-

# Install headers
make -C linux headers_install INSTALL_HDR_PATH=$(pwd)/linux-headers
```

You should see kernel headers in the `/home/user/workspace/linux-headers/include` folder now.
We will use this path during the next step.

## Get Glibc sources and build for AArch64 target

In the workspace directory, clone the Glibc Git repository:

```bash
git clone git://sourceware.org/git/glibc.git
```

To make the following command simpler, let's introduce the `CROSS` variable (notice the hyphen
at the end):

```bash
CROSS=/path/to/cross/gcc/bin/aarch64-none-linux-gnu-
```

Now configure the cross-build for the `aarch64-none-linux-gnu` target:

```bash
# Create build folder:
mkdir glibc-build
cd glibc-build

# Configure Glibc:
LC_ALL=C BUILD_CC=gcc \
CC=${CROSS}gcc CXX=${CROSS}g++ \
NM=${CROSS}nm READELF=${CROSS}readelf \
AR=${CROSS}ar GPROF=${CROSS}gprof \
OBJDUMP=${CROSS}objdump OBJCOPY=${CROSS}objcopy \
RANLIB=${CROSS}ranlib \
../glibc/configure --prefix=/usr \
  --host=aarch64-none-linux-gnu \
  --enable-hardcoded-path-in-tests \
  --with-headers=/home/user/workspace/linux-headers/include
```

Notice the path to the kernel headers in the last parameter in the `configure` command and
also the `include` at the end of it.

Finally, run the build:

```bash
make -j$(nproc)
```

## Run tests on FVP

If you are using an AArch64 host, you can run Glibc tests both on your host and on the FVP
from the same build tree. Before we run some tests, we need to make sure that we have two
important prerequisites in place.

First, we need to copy the target libraries from your toolchain's sysroot to ensure that
the tests are using them rather than your OS's libraries. Run the following commands in the
`glibc-build` folder:

```bash
cp $(${CROSS}gcc -print-file-name=libstdc++.so.6) .
cp $(${CROSS}gcc -print-file-name=libgcc_s.so.1) .
```

Next, we will build the testroot. A Glibc testroot is a collection of files that resembles
an installation of the Glibc that we have just built. It allows us to create the correct
environment for the tests without actually installing the Glibc. Tun the following command
int the Glibc build folder:

```bash
make $(pwd)/testroot.pristine/install.stamp
```

Now we can run the tests. Let's start with a single test to understand the structure of the
command. Ensure the following:

 * The FVP is running
 * The guest system accepts SSH connections
 * The Glibc source and build folders are available in the guest system via the NFS share
 * The paths to these folders on the host and the guest systems are the same

We should set the `TIMEOUTFACTOR` environment variable to extend the timeout for some of the
tests that may fail just because execution takes longer than usual. This is expected on an
emulated platform such as an FVP:

```bash
export TIMEOUTFACTOR=10
```

If you see any timeouts when running tests on the FVP, increase this value.

To tell the Glibc test system to execute the tests on a remote system (in our case this
means on the guest system running on the FVP), we will use the test wrapper script that
is part of the Glibc sources: `scripts/cross-test-ssh.sh`. By default it uses `ssh` as a
command to start an SSH connection, but it is possible to override it via the `--ssh` option.
However, this option only accepts single word values. To avoid complexities related to
using `sh` instead of `bash` and Bash aliases not being expanded in non-interactive shells,
the easiest way to proceed is as follows:

 * Create a simple shell script and save it using file name `ussh`:

```bash
#!/usr/bin/env bash
dbclient -p 8022 "$@"
```

 * Make it executable using the `chmod u+x` command
 * Save this script in one of the directories in your `PATH`.

To run a single test, use this command:

```bash
make test t=misc/tst-aarch64-pkey \
  test-wrapper="/home/user/workspace/glibc/scripts/cross-test-ssh.sh --ssh ussh fvp"
```

Let's see what we have here. The `test` target will build (or rebuild) one test and all
its dependencies and then run this test. This target requires one parameter, `t`, with the
name of the test that we need to run. The Glibc tests are grouped into folders, and a test name
would normally look like `misc/tst-aarch64-pkey` where `misc` is the name of the group and
`tst-aarch64-pkey` is the name of the test in this group.

When we use SSH test wrapper to run a test on the FVP we need to supply its absolute path along
with any of the script's arguments as a value of the `test-wrapper` make parameter. Here,
we use the `--ssh` option of the wrapper script to tell it to use the `ussh` command instead
of `ssh` and we use `fvp` as the hostname of the remote system. All the setup that we have
done in the previous steps makes using this wrapper script easier.

To run the same test on your AArch64 host rather than on the FVP, just omit the `test-wrapper=...`
parameter.

With this particular test, you may see that on your AArch64 host, it reports that it is not
supported:

```
UNSUPPORTED: misc/tst-aarch64-pkey
original exit status 77
```

And on your FVP with the Linux kernel 6.13 or newer, you should get:

```
PASS: misc/tst-aarch64-pkey
original exit status 0
```

To run a group of tests, use the following command with the `check` target:

```bash
make check -C /home/user/workspace/glibc/argp \
  objdir=`pwd` \
  test-wrapper="/home/user/workspace/glibc/scripts/cross-test-ssh.sh --ssh ussh fvp"
```

In this instance, we are building and running tests from the `argp` folder. We use the `-C`
option of `make` to point it to the right directory, and we also supply a path to the
build folder via the `objdir` parameter (which should be the current directory since we are
running this command from within the build folder). The `test-wrapper` part remains the same.

To run all the tests, simply do:

```bash
make check \
  test-wrapper="/home/user/workspace/glibc/scripts/cross-test-ssh.sh --ssh ussh fvp"
```

Note that this will take a considerable amount of time. Also, notice that we are not using
a parallel `make` command for running tests on the FVP. The reason is that the Fast Models
simulation code runs primarily on a single thread, and running tests in parallel would not
speed up the execution.
