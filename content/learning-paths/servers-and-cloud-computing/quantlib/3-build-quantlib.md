---
title: Build QuantLib with benchmark support
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure the build

Return to the QuantLib source directory. The directory uses the `QL_VER` variable that you exported when downloading the source archive:

```bash
cd ~/QuantLib-$QL_VER
```

Run the configure script with benchmark support enabled:
```bash
./configure \
--prefix=/usr/local \
--enable-benchmark \
--enable-parallel-unit-test-runner \
CFLAGS="-g -O2 -mcpu=native" \
CXXFLAGS="-g -O2 -mcpu=native"
```

This configuration installs QuantLib to `/usr/local`. It enables the benchmark executable and parallel test execution, and it applies CPU-specific optimization flags. 

## Install QuantLib

Compile using all available cores. The `nproc` command returns the number of processing units visible to the VM, so `make -j$(nproc)` keeps the build command portable across VM sizes:

```bash
make -j$(nproc)
```

{{% notice Note %}}
The build may take 30–45 minutes on the Standard_D4ps_v5. If your SSH session might disconnect, set up tmux before running `make` — see [(Optional) Use tmux for remote builds](/learning-paths/servers-and-cloud-computing/quantlib/2-setup-environment/#optional-use-tmux-for-remote-builds) in the previous section.
{{% /notice %}}

After the build completes, install QuantLib into `/usr/local` and refresh the dynamic linker cache:

```bash
sudo make install
sudo ldconfig
```

Move to the test suite and check that the benchmark executable was created:

```bash
cd ~/QuantLib-$QL_VER/test-suite
ls quantlib-benchmark
```

You should see `quantlib-benchmark` in the output. You'll use this executable in the next section.

## What you've accomplished and what's next

You've now completed the installation of QuantLib after building it with support for benchmarking. 

Next, you'll run benchmarks on QuantLib with different sizes and thread counts.