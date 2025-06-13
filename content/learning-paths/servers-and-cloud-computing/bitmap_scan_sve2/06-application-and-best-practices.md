---
# User change
title: "Applications and optimization best practices"

weight: 7

layout: "learningpathall"
---
## Applications to database systems

Optimized bitmap scanning can accelerate several core operations in modern database engines, particularly those used for analytical and vectorized workloads.

### Bitmap index scans
Bitmap indexes are widely used in analytical databases to accelerate queries with multiple filter predicates across large datasets. The NEON and SVE implementations can significantly speed up the scanning of these bitmap indexes, especially for queries with low selectivity.

### Bloom filter checks

Bloom filters are probabilistic structures used to test set membership, commonly employed in join filters or subquery elimination. Vectorized scanning via NEON or SVE accelerates these checks by quickly rejecting rows that don’t match, reducing the workload on subsequent stages of the query.

### Column filtering

Columnar databases frequently use bitmap filters to track which rows satisfy filter conditions. These bitmaps can be scanned in a vectorized fashion using NEON or SVE instructions, substantially speeding up predicate evaluation and minimizing CPU cycles spent on row selection.

## Best practices

Based on the benchmark results, here are some best practices for optimizing bitmap scanning operations:

* Choose the right implementation based on the expected bit density**:
   - For empty bit vectors: NEON is optimal
   - For very sparse bit vectors (0.001% - 0.1% set bits): SVE is optimal due to efficient skipping
   - For medium to high densities (> 0.1% density): SVE still outperforms NEON

* Implement Early Termination**: Always include a fast path for the no-hits case, as this can provide dramatic performance improvements.

* Use Byte-level Skipping**: Even in scalar implementations, skipping empty bytes can provide significant performance improvements.

* Consider Memory Access Patterns**: Optimize memory access patterns to improve cache utilization.

* Leverage Vector Instructions**: Use NEON or SVE/SVE2 instructions to process multiple bytes in parallel.

## Conclusion

Scalable Vector Extension (SVE) instructions provide a powerful and portable way to accelerate bitmap scanning in modern database systems. When implemented on Arm Neoverse V2–based servers like AWS Graviton4, they deliver substantial performance improvements across a wide range of bit densities.

The SVE implementation shows particularly impressive performance for sparse bitvectors (0.001% - 0.1% density), where it outperforms both scalar and NEON implementations. For higher densities, it maintains a performance advantage by amortizing scan costs across wider vectors.

These performance improvements can translate directly to faster query execution times, especially for analytical workloads that involve multiple bitmap operations.



