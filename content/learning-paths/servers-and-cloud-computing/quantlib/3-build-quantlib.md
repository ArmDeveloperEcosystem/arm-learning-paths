---
title: Build QuantLib with benchmark support
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure the QuantLib build

From the QuantLib source directory:

```bash
cd ~/QuantLib-$QL_VER
```

Run the configure script:
```bash
./configure \
--prefix=/usr/local \
--enable-benchmark \
--enable-parallel-unit-test-runner \
CFLAGS="-g -O2 -mcpu=native" \
CXXFLAGS="-g -O2 -mcpu=native"
```

This configuration:

- installs QuantLib to `/usr/local`
- enables the benchmark executable
- enables parallel test execution
- applies CPU-specific optimization flags


## Build QuantLib

Compile using all available cores:

```bash
make -j$(nproc)
```

{{% notice Note %}}
The build may take 30–45 minutes on smaller instances. Use tmux to avoid losing progress if your SSH session disconnects.
{{% /notice %}}

## Install QuantLib

After the build completes:

```bash
sudo make install
sudo ldconfig
```

## Verify the build

Move to the test suite:
```bash
cd ~/QuantLib-$QL_VER/test-suite
```

Check that the benchmark executable exists:
```bash
ls quantlib-benchmark
```

## What you've accomplished and what's next

You have successfully configured and built QuantLib with benchmark support on an Arm64 Azure Cobalt system.

In the next section, you will run benchmark workloads and explore how performance changes with different parameters.
