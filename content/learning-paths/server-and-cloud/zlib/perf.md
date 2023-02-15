---
layout: learningpathall
title: Use perf to analyze zlib performance
weight: 4
---

## Prerequisites

* An [Arm based instance](/learning-paths/server-and-cloud/csp/) from an appropriate cloud service provider.

This learning path has been verified on AWS EC2 and Oracle cloud services, running `Ubuntu Linux 20.04` and `Ubuntu Linux 22.04`.

* Linux perf must be installed

```bash
sudo apt install linux-tools-common linux-tools-generic linux-tools-`uname -r` -y
```

```console
sudo sh -c "echo '1' > /proc/sys/kernel/perf_event_paranoid"
```

## Detailed Steps

The previous section explained how to run a Python program to compress large file and increase performance with zlib-cloudflare. 

Let's use perf to look at the performance.

Continue with the same zip.py program as the previous section.

Make sure to start with zip.py and largefile available. 

Confirm the application is working and largefile.gz is created when it is run.

```bash
python ./zip.py
```

## Run the example with perf using the default zlib

Run with the default libz and time the execution.

```console
perf stat python ./zip.py
```

## Use perf record and generate the flame graph

Generate the flame graph using the FlameGraph project from GitHub. 

Record application activity.

```console
perf record -F 99 -g python ./zip.py
```

Generate an image with the flame graph. 

Install the flame graph script. 

```bash
sudo apt install git -y
git clone https://github.com/brendangregg/FlameGraph
```

Generate the graph.

```console
perf script | ./FlameGraph/stackcollapse-perf.pl > out.perf-folded && ./FlameGraph/flamegraph.pl out.perf-folded > flamegraph1.svg
```

Copy the file flamegraph1.svg to your computer and open it in a browser or other image application.

## Look at the report

Use perf report to see a performance report

```console
perf report
```

Note that the zlib and the crc32 function is taking significant time

## Run the example again with perf stat and zlib-cloudflare

This time use LD_PRELOAD to change to zlib-cloudflare instead and check the performance difference. 

Adjust the path to the zlib-cloudflare libz.so as needed. 

```console
LD_PRELOAD=/usr/local/lib/libz.so  perf stat python ./zip.py
```

## Generate the new flame graph

```console
perf record -F 99 -g python ./zip.py
```

```console
perf script | ./FlameGraph/stackcollapse-perf.pl > out.perf-folded && ./FlameGraph/flamegraph.pl out.perf-folded > flamegraph2.svg
```

Copy the file flamegraph2.svg to your computer and open it in a browser or other image application and compare it to flamegraph1.svg