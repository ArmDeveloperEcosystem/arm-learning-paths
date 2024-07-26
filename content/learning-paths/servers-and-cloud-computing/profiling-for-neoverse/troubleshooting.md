---
title: Troubleshooting
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section outlines some common problems that can be encountered when you are deploying the tools, and their solutions.

## Capture data size is very large

When capturing with `-I poll`, the size of the data capture is very large.

The polling mode is provided as a fallback for systems without the kernel patches. To capture data for function-attribution without the patches, the tool must use a very high sample rate which increases the captured data size.

Apply the kernel patch as described in the [Install guide](/install-guides/streamline-cli/), and run `sl-record` without the `-I` option, which is equivalent to `-I inherit`. The kernel patch implements strobed sampling, allowing you to alternate between a fast "mark" window that is captured and a slow "space" window that is skipped.

## Capture reports file descriptor exhaustion {.section}

The application runs out of file descriptors when capturing with `-I poll`.

The polling mode is provided as a fallback for systems without the kernel patches. To attach `perf` counter groups to a new application thread you
must open new file handles for each counter group for every core in the system.

Apply the kernel patch as described in the [Install guide](/install-guides/streamline-cli/), and run `sl-record` without the `-I` option, which is equivalent to `-I inherit`. The kernel patch allows `perf` counter groups to be inherited by new child threads, avoiding the need to open new file handles.

## Capture impacts application performance {.section}

Application performance is impacted by running `sl-record` on a high core count system.

Capturing and storing the profiling data has an overhead on the running system, especially when multiplexing counters with Perf.

Limit the running application to a subset of the CPU cores, leaving a small number of cores free for `sl-record`. For example, on a 64 core system Arm recommends limiting the application to 60 cores.
