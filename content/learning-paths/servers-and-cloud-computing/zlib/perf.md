---
layout: learningpathall
title: Use perf to analyze zlib performance
weight: 4
---

## Install necessary software packages

Install Linux `perf`:

```bash
sudo apt install linux-tools-common linux-tools-generic linux-tools-`uname -r` -y
```

For more information about installing `perf` review [Perf for Linux on Arm](/install-guides/perf/).

Allow user access to PMU (Performance Monitoring Unit) registers:

```console
sudo sh -c "echo '1' > /proc/sys/kernel/perf_event_paranoid"
```

For more information refer to the [Linux kernel documentation](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html#perf-event-paranoid).

## Detailed Steps

The previous section explained how to run a Python program to compress large files and increase performance with `zlib-cloudflare`. Now use `perf` to look at the performance.

Continue with the same `zip.py` program as the previous section. Make sure to start with `zip.py` and `largefile` available. Confirm the application is working and `largefile.gz` is created when it is run.

```bash
python ./zip.py
```

## Run the example with perf using the default zlib

Run with the default `zlib` and time the execution.

```console
perf stat python ./zip.py
```

The `perf stat` command will display counts of a few selected PMU events. 

## Use perf record and generate the flame graph

You can also record the application activity with `perf record`. `-F` specifies the sampling frequency and `-g` enables to collect the backtrace:

```console
perf record -F 99 -g python ./zip.py
```

To visualize the results, you can generate an image with `FlameGraph`. Install it with: 

```bash
sudo apt install git -y
git clone https://github.com/brendangregg/FlameGraph
```

Generate the graph:

```console
perf script | ./FlameGraph/stackcollapse-perf.pl > out.perf-folded && ./FlameGraph/flamegraph.pl out.perf-folded > flamegraph1.svg
```

Copy the file `flamegraph1.svg` to your computer and open it in a browser or another image application.

## Look at the report

As an alternative, use `perf report` to inspect the profiling data:

```console
perf report
```

Note that the `zlib` and the `deflate` function are taking significant time.

## Run the example again with perf stat and zlib-cloudflare

This time use `LD_PRELOAD` to change to `zlib-cloudflare` instead and check the performance difference. 

Adjust the path to the Cloudflare `libz.so` as needed. 

```console
LD_PRELOAD=/usr/local/lib/libz.so  perf stat python ./zip.py
```

## Generate the new flame graph

```console
LD_PRELOAD=/usr/local/lib/libz.so perf record -F 99 -g python ./zip.py
```

```console
perf script | ./FlameGraph/stackcollapse-perf.pl > out.perf-folded && ./FlameGraph/flamegraph.pl out.perf-folded > flamegraph2.svg
```

Copy the file `flamegraph2.svg` to your computer. Open it in a browser or other image application and compare it to `flamegraph1.svg`.