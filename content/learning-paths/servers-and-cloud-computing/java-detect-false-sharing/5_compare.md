---
title: Compare baseline and padded runtimes
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Measure repeated pairs

Use the dual-mode program from the previous step. Keep the JDK, logical CPUs,
iteration count, JVM flags, and background system load consistent. First run
one warm-up pair:

```bash
for mode in baseline padded; do
  taskset -c 0,1 "$java_bin" \
    --add-exports java.base/jdk.internal.vm.annotation=ALL-UNNAMED \
    -XX:-RestrictContended FalseSharingDemo "$mode"
done
```

Then collect five measured pairs, alternating which mode runs first. Save the
program output so the individual results remain available:

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
Run alternating baseline and padded pairs. Do not draw a conclusion from one
timing comparison.
{{% /notice %}}

Confirm that every line has the expected mode and `sum=1000000000`. Display
the five elapsed values for each mode in ascending order:

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

```output
baseline: 14.929432 15.045710 15.537969 16.851870 17.709697
baseline median: 15.537969

padded: 2.866497 2.867312 2.867552 2.869511 2.909067
padded median: 2.867552
```

With five measurements, the third sorted value is the median.

The baseline commonly takes considerably longer because the writers repeatedly
transfer ownership of their shared cache line. The exact difference depends on
object placement, scheduling, processor topology, and system noise. If results
overlap, repeat more pairs and examine their variability before concluding that
padding helped.


{{% notice Note %}}
The reported `seconds=` value comes from `System.nanoTime()` around the worker
phase. It excludes JVM startup but includes the release of the start latch,
worker execution, and the joins. It is therefore useful for comparing these two
modes, but it is not an end-to-end application latency measurement.
{{% /notice %}}
