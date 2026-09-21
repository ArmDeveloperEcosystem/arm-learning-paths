---
title: Conclusion
description: Review how JOL, Perf C2C, and repeated measurements reveal false sharing and evaluate the trade-offs of contention padding.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Review what you tested

You created a Java workload in which two threads update separate
`volatile long` fields, used JOL to inspect their layout, and used Perf C2C to
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
comparison does not prove that either reported address belonged to the counter
object.

Across the five representative alternating measurement pairs, the median
worker-phase runtimes were:

- Baseline: 15.5 seconds
- Padded: 2.9 seconds

For these representative measurements, adding `@Contended` reduced the median
runtime by 81.5%, making the padded mode approximately 5.42 times faster. The
program performed the same one billion increments in both modes; separating
the fields reduced the cache-line ownership transfers that delayed the
baseline workers.

These results apply to this sample, processor, JVM, and test environment.
Object placement, CPU scheduling, topology, and background activity can change
the result. In a real application, use repeated measurements and Perf evidence
before adding `@Contended`, and balance any runtime improvement against the
larger object size, heap occupancy, and possible garbage-collection cost.
