---
title: Find Bottlenecks with Top-Down
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run Topdown analysis

As shown in the `main.cpp` listing below, the program generates a 1920×1080 bitmap image of the fractal. To identify performance bottlenecks, run the Topdown recipe in Arm Performix (APX). APX uses microarchitectural sampling to show which instruction pipeline stages dominate program latency, then highlights ways to improve those bottlenecks.

**Note**: Replace the first string argument in `myplot.draw()` with the absolute path to your image folder, then rebuild the application. Otherwise, the image is written to `/tmp/atperf/tools/atperf-agent`, which is periodically deleted.

```cpp
#include "Mandelbrot.h"
#include <iostream>

using namespace std;

int main(){

    Mandelbrot::Mandelbrot myplot(1920, 1080);
    myplot.draw("/path/to/images/green.bmp", Mandelbrot::Mandelbrot::GREEN);

    return 0;
}
```

On your host machine, open Arm Performix and select the **Topdown** recipe.

![config](./topdown-config.jpg)

Select the target you configured in the setup phase. If this is your first run on this target, you likely need to select **Install Tools** to copy collection tools to the target. Next, select the **Workload type**. You can sample the whole system or attach to an existing process, but in this exercise you launch a new process. Use the full path to your executable because the **Workload** field does not currently support shell-style path expansion.

You can set a time limit for the workload and customize metrics if you already know what to investigate.

The **Collect managed code stacks** toggle matters for Java/JVM or .NET workloads.

You can also select High, Normal, or Low sampling rates to trade off collection overhead and sampling granularity.

Select **Run Recipe** to launch the workload and collect performance data.

## View Run Results

Performix generates a high-level instruction pipeline view, highlighting where most time is spent.

![topdown-results.jpg](topdown-results.jpg)

In this breakdown, Backend Stalls dominate samples. Within that category, work is split between Load Operations and integer and floating-point operations.
There is no measured SIMD activity, even though this workload is highly parallelizable.

The **Insights** panel highlights ALU contention as a likely improvement opportunity.

![topdown-insights.jpg](topdown-insights.jpg)

To inspect executed instruction types in more detail, use the Instruction Mix recipe in the next step.