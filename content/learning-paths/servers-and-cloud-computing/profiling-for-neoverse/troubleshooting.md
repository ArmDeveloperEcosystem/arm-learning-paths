---
title: Troubleshooting
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section outlines some common problems that can be encountered when you are deploying the tools, and their solutions.

## Capture data size is very large

Data size can be very large when capturing with `-I poll`. This occurs
because the polling mode is provided as a fallback for systems without the
kernel patches. To capture data for function-attribution without the patches,
the tool must use a very high sample rate which increases the captured data
size.

To avoid this issue, apply the kernel patch as described in the [Install guide](/install-guides/streamline-cli/), and run `sl-record` without the `-I` option. The kernel patch implements strobed sampling, allowing the tool to alternate between a fast "mark" window that is captured and a slow "space" window that is skipped.

## Capture data size using SPE is very large

SPE uses hardware sampling that allows a high sample rate. Captured data size
scales as "core count * sample rate * capture duration", which can result in
very large SPE data sets in systems with many CPU cores, using a high sample
rate, or with a long application duration.

When profiling long running applications with SPE, Arm recommends increasing
the size of the SPE sample window. Use the `-F` option to set the number of
micro-ops between samples (default 2500000).

## Capture reports file descriptor exhaustion

The application runs out of file descriptors when capturing with `-I poll`.

This occurs because the polling mode is provided as a fallback for systems without the kernel patches. To attach `perf` counter groups to a new application thread you must open a new file descriptor for each counter group for every core in the system. This operation has O(counters * cores * threads) complexity, and requires a very large number of file descriptors on Arm Neoverse systems which can have both high core count and high thread count.

To avoid this, apply the kernel patch as described in the [Install guide](/install-guides/streamline-cli/), and run `sl-record` without the `-I` option, which is equivalent to `-I inherit`. The kernel patch allows new child threads to inherit `perf` counter groups, avoiding the need to open new file descriptors.

If it is not possible to install the kernel patches, you can increase the number of allowed file descriptors per process:

```
sudo ulimit -n -H $((64*1024*1024))
sudo ulimit -n -S $((64*1024*1024))
```

## Capture reports SPE Aux data missing in Streamline GUI

The Streamline GUI contains "SPE Aux data missing" markers in the Timeline view when opening the capture. This occurs because a sample buffer overflowed before
`sl-record` was able to store the data it contained.

There are three changes you can make to mitigate this problem:

* You can reduce SPE sample rate.
* You can increase the size of the `perf` sample buffer.
* You can increase the size of the internal `sl-record` sample buffer.

To reduce SPE sample rate, use the `-F` option to increase the number of micro-operations between samples (default is 2500000).

To increase the size of the `perf` sample buffer, you can either manually increase the `mlock` limit (value must be a multiple of 4):

```
echo <num_kb> | sudo tee /proc/sys/kernel/perf_event_mlock_kb
```

Alternatively, you can run `sl-record` as root, which bypasses the `mlock` limit.

To increase the size of the `sl-record` internal sample buffer, use the `-Z <num_pages>` option to specify the number of 4K pages to use. A buffer of
this size is allocated per core in the system, so ensure that you leave enough memory for your application to run on systems with many CPU cores.

## Capture impacts application performance

Application performance is impacted by running under `sl-record` on a high core count system.

This occurs because capturing and storing the profiling data has an overhead on the running system, especially when multiplexing counters with Perf.

To mitigate this issue, limit the running application to a subset of the CPU cores, leaving a small number of cores free for `sl-record`. For example, on a
64 core system Arm recommends limiting the application to 60 cores.
