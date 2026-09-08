---
title: Conclusion
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Review what you tested

You created a Java workload in which two threads update separate
`volatile long` fields. JOL showed that the baseline fields were adjacent at
offsets 16 and 24 in a 32-byte object, making it possible for both fields to
occupy one 64-byte cache line. Perf C2C then provided runtime evidence of inter-core
sharing: the baseline report's highest-ranked line contained 36 local peer
hits.

You added `@Contended` to place the two fields in separate contention groups.
JOL showed that the fields moved to offsets 144 and 280, with 128 bytes of
padding between them. This prevented the fields from occupying the same
64-byte cache line, but increased the object size from 32 bytes to 288 bytes.
The extra 256 bytes per object are the memory-footprint cost of this mitigation.

## Review the measured impact

After padding, the highest-ranked line in the Perf C2C report contained 4
local peer hits instead of 36. This approximately 89% reduction in the top-line
peer count is consistent with removing the original false-sharing hot spot.
The addresses came from separate JVM processes, however, so this comparison
does not prove that either reported address belonged to the counter object.

Across five alternating measurement pairs, the median worker-phase runtimes
were:

- Baseline: 15.5 seconds
- Padded: 2.9 seconds

For these measurements, adding `@Contended` reduced the median runtime by
81.5%, making the padded mode approximately 5.42 times faster. The program
performed the same one billion increments in both modes; separating the fields
reduced the cache-line ownership transfers that delayed the baseline workers.

These results apply to this sample, processor, JVM, and test environment.
Object placement, CPU scheduling, topology, and background activity can change
the result. In a real application, use repeated measurements and Perf evidence
before adding `@Contended`, and balance any runtime improvement against the
larger object size, heap occupancy, and possible garbage-collection cost.
