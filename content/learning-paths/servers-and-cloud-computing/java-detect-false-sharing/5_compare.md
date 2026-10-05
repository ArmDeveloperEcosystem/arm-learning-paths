---
title: Compare baseline and padded runtimes
description: Run repeated baseline and padded measurements to compare Java worker-phase runtimes under consistent test conditions.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Measure repeated pairs

Use the dual-mode program to measure repeated pairs. Keep the Java Development Kit (JDK), logical CPUs,
iteration count, Java Virtual Machine (JVM) flags, and background system load consistent.

First, run one warm-up pair:

```bash
for mode in baseline padded; do
  taskset -c 0,1 "$java_bin" \
    --add-exports java.base/jdk.internal.vm.annotation=ALL-UNNAMED \
    -XX:-RestrictContended FalseSharingDemo "$mode"
done
```

Then, collect five measured pairs, alternating which mode runs first.

Save the program output so that the individual results remain available:

```bash
: > timings.txt
for pair in 1 2 3 4 5; do
  if (( pair % 2 )); then
    modes="baseline padded"
  else
    modes="padded baseline"
  fi

  for mode in $modes; do
    taskset -c 0,1 "$java_bin" \
      --add-exports java.base/jdk.internal.vm.annotation=ALL-UNNAMED \
      -XX:-RestrictContended FalseSharingDemo "$mode" | tee -a timings.txt
  done
done
```

{{% notice Note %}}
Run alternating baseline and padded pairs. Don't draw a conclusion from one
timing comparison.
{{% /notice %}}

Confirm that every line has the expected mode and `sum=1000000000`.

Display the five elapsed values for each mode in ascending order:

```bash
for mode in baseline padded; do
  awk -v selected="$mode" '
    $1 == "mode=" selected {
      for (i = 1; i <= NF; i++)
        if ($i ~ /^seconds=/) {
          split($i, value, "=")
          print value[2]
        }
    }' timings.txt | sort -n | awk -v selected="$mode" '
      { values[NR] = $1 }
      END {
        printf "%s: ", selected
        for (i = 1; i <= NR; i++) printf "%s%s", values[i], (i < NR ? " " : "\n")
        if (NR == 5) printf "%s median: %s\n", selected, values[3]
      }'
done
```

The output is similar to:

```output
baseline: 14.929432 15.045710 15.537969 16.851870 17.709697
baseline median: 15.537969

padded: 2.866497 2.867312 2.867552 2.869511 2.909067
padded median: 2.867552
```

With five measurements, the third sorted value is the median.

The baseline usually takes considerably longer because the writers repeatedly
transfer ownership of their shared cache line. The exact difference depends on
object placement, scheduling, processor topology, and system noise. If results
overlap, repeat more pairs and examine their variability before concluding that
padding helped.


{{% notice Note %}}
The reported `seconds=` value comes from `System.nanoTime()` around the worker
phase. It excludes JVM startup but includes the release of the start latch,
worker execution, and the joins. The value is therefore useful for comparing these two
modes, but it's not an end-to-end application latency measurement.
{{% /notice %}}

## Review what you tested

You created a Java workload in which two threads update separate
`volatile long` fields, used Java Object Layout (JOL) to inspect their layout, and used Perf C2C to
observe inter-core sharing. You then added `@Contended` to place the fields in
separate contention groups and inspected the padded layout.

In the representative results, the baseline fields were adjacent at offsets
16 and 24 in a 32-byte object, making it possible for both fields to occupy one
64-byte cache line. The baseline report's highest-ranked line contained 36
local peer hits. After padding, JOL showed that the fields moved to offsets 144
and 280, with 128 bytes of padding between them. This prevented the fields from
occupying the same 64-byte cache line, but increased the object size from 32
bytes to 288 bytes. The extra 256 bytes per object are the memory-footprint
cost of this mitigation.

## Review the measured impact

Compare the absolute peer-hit counts in the baseline and padded Perf C2C
reports, then use repeated timing pairs to compare their median worker-phase
runtimes. Account for the memory-footprint cost when deciding whether to apply
contention padding.

In the representative Perf C2C results, the highest-ranked line after padding
contained 4 local peer hits instead of 36. This approximately 89% reduction in
the top-line peer count is consistent with removing the original false-sharing
hot spot. The addresses came from separate JVM processes, however, so this
comparison doesn't prove that either reported address belonged to the counter
object.

Across the five representative alternating measurement pairs, the median
worker-phase runtimes were the following:

- Baseline: 15.5 seconds
- Padded: 2.9 seconds

For these representative measurements, adding `@Contended` reduced the median
runtime by 81.5%, making the padded mode approximately 5.42 times faster.

The program performed the same one billion increments in both modes. Separating
the fields reduced the cache-line ownership transfers that delayed the
baseline workers.

These results apply to this sample, processor, JVM, and test environment.
Object placement, CPU scheduling, topology, and background activity can change
the result. In a real application, use repeated measurements and Perf evidence
before adding `@Contended`, and balance any runtime improvement against the
larger object size, heap occupancy, and possible garbage-collection cost.


## What you've accomplished

You've now compared baseline and padded Java worker-phase runtimes.

You can extend this workflow to real applications to add padding and measure runtime improvements.
