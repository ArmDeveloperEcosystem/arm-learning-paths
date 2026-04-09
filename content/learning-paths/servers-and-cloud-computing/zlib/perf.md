---
layout: learningpathall
title: Use perf to analyze zlib-ng performance
weight: 4
---

## Analyze performance improvements with perf

In the previous section, you learned how to use `zlib-ng` to improve the performance of a Python application for compressing large files.

In this section, you will use `perf` to analyze the performance of the application.

## Install necessary software packages

Install Linux `perf`:

```bash
sudo apt install linux-tools-common linux-tools-generic linux-tools-`uname -r` -y
```

For more information about installing `perf`, review [Perf for Linux on Arm](/install-guides/perf/).

Allow user access to Performance Monitoring Unit (PMU) registers and kernel symbol addresses:

```console
sudo sh -c "echo '1' > /proc/sys/kernel/perf_event_paranoid"
sudo sh -c "echo '0' > /proc/sys/kernel/kptr_restrict"
```

The first setting allows unprivileged access to PMU counters. The second allows `perf` to read kernel symbol addresses from `/proc/kallsyms`, which is needed for complete call graph resolution in flame graphs.

For more information, refer to the [Linux kernel documentation](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html#perf-event-paranoid).

## Profile the default zlib with perf

 Make sure that the `zip.py` program and `largefile` from the [previous section](/learning-paths/servers-and-cloud-computing/zlib/py-zlib/) are available. Confirm the application is working and `largefile.gz` is created when it is run.

```console
python zip.py
```

## Run the example with perf stat using the default zlib

Run `perf stat` with a set of basic hardware events that are reliably available on virtualized Arm instances:

```console
perf stat -e cycles,instructions,cache-references,cache-misses python ./zip.py
```

{{% notice Note %}}
Running `perf stat` without `-e` uses default topdown pipeline slot metrics that require full PMU access. Most cloud VMs expose only a subset of PMU counters, which causes `Failure to read '#slots'` errors and can result in a segfault. Specifying events explicitly avoids this.
{{% /notice %}}

The `perf stat` output shows event counts for the compression run. Make a note of the `cycles` and `instructions` values.

The output is similar to:

```output
 Performance counter stats for 'python ./zip.py':

       12984652076      cycles                                                                  (75.02%)
       45063797078      instructions              #    3.47  insn per cycle                    (74.99%)
       20161747365      cache-references                                                        (75.00%)
          94565361      cache-misses              #    0.47% of all cache refs                 (50.01%)

       4.849571272 seconds time elapsed

       4.722285000 seconds user
       0.126034000 seconds sys
```

## Use perf record and generate the flame graph

You can also record the application activity with `perf record`. `-F` specifies the sampling frequency and `--call-graph dwarf` collects call graphs using DWARF debug info, which works more reliably than frame pointers for Python on Arm cloud VMs:

```console
perf record -F 99 --call-graph dwarf python ./zip.py
```

{{% notice Note %}}
On cloud VMs, you may see warnings about kernel address maps and `kptr_restrict` even after setting it to 0. These are non-fatal — `perf record` still captures userspace samples successfully. Kernel frames in the flame graph may be unresolved, but the `zlib` and Python frames that matter for this analysis will be present.
{{% /notice %}}

To visualize the results, install `FlameGraph`:

```bash
git clone https://github.com/brendangregg/FlameGraph
```

Convert the recorded data to folded stacks and verify the output is non-empty before generating the SVG:

```console
perf script > out.perf-script
./FlameGraph/stackcollapse-perf.pl out.perf-script > out.perf-folded
wc -l out.perf-folded
```

The line count should be greater than 0. Then, generate the flame graph:

```console
./FlameGraph/flamegraph.pl out.perf-folded > flamegraph1.svg
```

Copy the file `flamegraph1.svg` to your computer and open it in a browser or another image application.

## Inspect the perf report

As an alternative, use `perf report` to inspect the profiling data:

```console
perf report
```

The output is similar to:

```output
+   99.78%     0.00%  python   libc.so.6              [.] __libc_start
+   43.04%    43.04%  python   libz.so.1.3            [.] 0x0000000000
+    8.37%     8.37%  python   libz.so.1.3            [.] crc32_z
```

The key observation is that `libz.so.1.3` accounts for a large share of the self time — roughly 43% in the primary deflate path and another 8% in `crc32_z`. This confirms that `zlib` compression is the dominant hotspot in the workload, and that the CRC32 calculation alone is a measurable fraction of total runtime. The many `[unknown]` frames are Python interpreter internals that `perf` cannot resolve without debug symbols, but they do not affect the conclusion.

In the next step, you will run the same workload with `zlib-ng` and compare the hotspot profile.

## Run the example again with perf stat and zlib-ng

This time, use `LD_PRELOAD` to switch to `zlib-ng` and check the performance difference.

```console
LD_PRELOAD=/usr/local/lib/libz.so.1 perf stat -e cycles,instructions,cache-references,cache-misses python ./zip.py
```

The output is similar to:

```output
 Performance counter stats for 'python ./zip.py':

        4897544240      cycles                                                                  (75.00%)
       20992552372      instructions              #    4.29  insn per cycle                    (74.98%)
        7522040735      cache-references                                                        (75.01%)
          93296123      cache-misses              #    1.24% of all cache refs                 (50.01%)

       1.832269220 seconds time elapsed

       1.693647000 seconds user
       0.137971000 seconds sys
```

Comparing against the default `zlib` run:

| Metric | Default zlib | zlib-ng | Change |
|---|---|---|---|
| Cycles | 12,984,652,076 | 4,897,544,240 | -62% |
| Instructions | 45,063,797,078 | 20,992,552,372 | -53% |
| IPC | 3.47 | 4.29 | +24% |
| Cache references | 20,161,747,365 | 7,522,040,735 | -63% |
| Elapsed time | 4.85s | 1.83s | -62% |

The reduction in cycle count and cache references reflects `zlib-ng`'s wider Neon vector paths processing more data per instruction. The higher IPC (4.29 vs 3.47) shows the CPU is executing more useful work per cycle, a direct result of the SIMD-optimized adler32 and deflate routines replacing scalar loops.

## Run perf report with zlib-ng

Run `perf record` and then `perf report` with `zlib-ng` to compare the hotspot profile against the default `zlib` run:

```console
LD_PRELOAD=/usr/local/lib/libz.so.1 perf record -F 99 --call-graph dwarf python ./zip.py
perf report
```

The output is similar to:

```output
+   82.54%     3.37%  python   libz.so.1.3.1.zlib-ng  [.] deflate_slow
+   82.54%     0.00%  python   libz.so.1.3.1.zlib-ng  [.] deflate
+   64.40%    64.40%  python   libz.so.1.3.1.zlib-ng  [.] insert_string_roll
+   11.96%     0.56%  python   libz.so.1.3.1.zlib-ng  [.] fill_window
```

There are two significant changes compared to the default `zlib` report:

- **`libz.so.1.3.1.zlib-ng` is now named in the report**, confirming that `LD_PRELOAD` loaded `zlib-ng` correctly. The default `zlib` report showed an unresolved address at 43% self time; here the same hotspot is identified as `insert_string_roll` — `zlib-ng`'s Neon-accelerated hash chain insertion function.

- **`crc32_z` has disappeared from the top entries entirely.** In the default `zlib` run, `crc32_z` accounted for 8.37% of samples. With `zlib-ng`, ARMv8 hardware CRC32 instructions execute fast enough that CRC32 no longer appears as a measurable hotspot.

The 64.40% figure for `insert_string_roll` looks higher than the 43% from the default `zlib` run, but `perf report` percentages are relative to samples collected *within that run*, not across runs. The `zlib-ng` run completed in 1.83 seconds versus 4.85 seconds for the default `zlib`. 

The `-F 99` flag used in the `perf record` command sets a sampling frequency of 99 Hz, so the number of samples collected is roughly proportional to the run duration — approximately 181 samples for zlib-ng versus 480 for the default `zlib`. The absolute sample counts tell a different story:

| Function | Default zlib | zlib-ng |
|---|---|---|
| Primary deflate hotspot | ~43% × 480 ≈ 206 samples | ~64% × 181 ≈ 116 samples |
| `crc32_z` | ~8% × 480 ≈ 38 samples | not visible |

The function received *fewer* absolute samples with `zlib-ng`, meaning less real time was spent there. It appears as a higher percentage only because the total run time — and therefore total samples — shrank so much.

## Generate the new flame graph

```console
LD_PRELOAD=/usr/local/lib/libz.so.1 perf record -F 99 --call-graph dwarf python ./zip.py
```

```console
perf script > out.perf-script
./FlameGraph/stackcollapse-perf.pl out.perf-script > out.perf-folded
./FlameGraph/flamegraph.pl out.perf-folded > flamegraph2.svg
```

Copy the file `flamegraph2.svg` to your computer. Open it in a browser or other image application and compare it to `flamegraph1.svg`.

Flame graphs have no time axis — frame width represents the proportion of total samples, and each SVG scales to fill its full width regardless of how long the run took. This means you cannot compare absolute widths across the two graphs. What you can compare is the *relative proportion* that `zlib` occupies within each graph:

- In `flamegraph1.svg`, look at what fraction of the total width is occupied by `libz` frames. Then check the same in `flamegraph2.svg`. The `zlib-ng` run should show a similar or slightly larger fraction — because the run is 2.6x shorter but the library is still doing the same work. The meaningful comparison is the `perf stat` cycle and time data from the previous section, not the flame graph widths.
- **What the flame graph is useful for here** is identifying which functions dominate within the `zlib` stack. In `flamegraph1.svg` you should see `crc32_z` as a visible frame. In `flamegraph2.svg` it should be absent or too narrow to label, replaced by `insert_string_roll` as the top frame — confirming the hotspot has shifted from CRC32 to hash insertion after `zlib-ng`'s ARMv8 CRC32 acceleration removes the previous bottleneck.

## What you've learned and what's next

In this Learning Path, you replaced the system `zlib` with `zlib-ng` on an Arm server and measured the performance improvement.

`zlib-ng` is built for modern Arm platforms. Its Neon SIMD and ARMv8 CRC32 acceleration deliver significantly faster compression than the default system library, without requiring any changes to your application code. Using `LD_PRELOAD` makes it straightforward to test and adopt `zlib-ng` for any dynamically linked application. Python, nginx, PostgreSQL, and many others all benefit from the same approach.