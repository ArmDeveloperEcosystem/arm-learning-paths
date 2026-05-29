---
title: Build QuantLib with benchmark support
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure the build

Return to the QuantLib source directory. This uses the `QL_VER` variable you exported when downloading the source archive:

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

This configuration:

- installs QuantLib to `/usr/local`
- enables the benchmark executable
- enables parallel test execution
- applies CPU-specific optimization flags


## Install QuantLib

Compile using all available cores. The `nproc` command returns the number of processing units visible to the VM, so `make -j$(nproc)` keeps the build command portable across VM sizes:

```bash
make -j$(nproc)
```

{{% notice Note %}}
The build may take 30–45 minutes on the Standard_D4ps_v5. If your SSH session might disconnect, set up tmux before running `make` — see the optional setup steps in the previous section.
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

You should see `quantlib-benchmark` in the output. You will use this executable in the next section.
