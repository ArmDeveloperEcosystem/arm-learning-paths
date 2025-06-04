---
title: Explore TieredPGO tradeoffs in OrchardCore
weight: 5

### FIXED, DO NOT MODIFY
t: learningpathall
---

## Introduction

In this section, we will explore the tradeoffs of using TieredPGO (Profile Guided Optimization) in the context of an OrchardCore CMS application. TieredPGO is a powerful optimization technique in .NET that can significantly impact the performance of your application. We will relate these tradeoffs back to our OrchardCore example to provide a practical understanding.

## Understanding TieredPGO

TieredPGO is a feature in .NET that allows the runtime to optimize code execution based on the actual usage patterns observed during the application's execution. It combines the benefits of both Tiered Compilation and Profile Guided Optimization to improve performance.

### Key Concepts

- **Tiered Compilation**: This allows the .NET runtime to initially compile methods with a quick, less-optimized version and later replace them with more optimized versions as the application runs.
- **Profile Guided Optimization (PGO)**: This uses runtime data to inform the JIT (Just-In-Time) compiler about which parts of the code are most frequently executed, allowing it to focus optimization efforts on those areas.

## Tradeoffs of Using TieredPGO

While TieredPGO can enhance performance, it also comes with certain tradeoffs:

1. **Startup Time**: The initial startup time of the application might be slightly longer due to the profiling overhead.
2. **Memory Usage**: Additional memory is used to store profiling data and multiple versions of compiled methods.
3. **Complexity**: Understanding and tuning TieredPGO requires a deeper knowledge of the application's runtime behavior.

### Example: Enabling TieredPGO

To enable TieredPGO in your OrchardCore application, you can set the following environment variables:

```bash
export DOTNET_TieredPGO=1
export DOTNET_TieredCompilation=1
```

### Observing the Impact

1. **Performance Gains**: Run your OrchardCore application and monitor the performance improvements in frequently accessed pages or components.
2. **Profiling Overhead**: Measure the startup time and memory usage to understand the impact of enabling TieredPGO.
3. **Optimization Focus**: Identify which parts of your application benefit the most from TieredPGO and consider if the tradeoffs are acceptable.

TieredPGO offers a compelling way to optimize .NET applications by leveraging runtime profiling data. In the context of an OrchardCore CMS application, it can lead to significant performance improvements, especially in high-traffic scenarios. However, it's essential to weigh the tradeoffs, such as increased startup time and memory usage, to determine if it's the right choice for your application.
