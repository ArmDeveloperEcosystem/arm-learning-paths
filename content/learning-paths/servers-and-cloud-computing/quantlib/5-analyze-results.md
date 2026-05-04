---
title: Analyze and compare benchmark results
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Record your results

To compare benchmark runs effectively, record each run in a consistent format.

A simple table is a good starting point:

| VM size | QuantLib version | Command | Threads | Size | Runtime |

|-----------|------------------|---------|---------|------|---------|

## Identify performance trends

When reviewing results, look for:

- how runtime changes as thread count increases

- whether performance improves with more threads

- where scaling begins to level off

- how runtime changes with problem size

## Ensure fair comparisons

Only change one variable at a time when comparing runs:

- thread count
- workload size
- VM size
- compiler configuration

Keep everything else constant.

## Extend your testing

Once you have a baseline, you can explore:

- larger Azure Cobalt virtual machines
- repeated runs to measure consistency
- different QuantLib versions
- different compiler optimization flags

## What you've accomplished and what's next

You have created a repeatable benchmarking workflow and learned how to interpret the results.

Continue by expanding your experiments or applying this approach to other workloads.