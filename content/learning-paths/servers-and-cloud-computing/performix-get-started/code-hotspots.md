---
title: Find code hotspots in the scalar dot-product application

description: Use Arm Performix Code Hotspots to identify functions that consume the most CPU time in a sample C++ application.

weight: 4

layout: learningpathall
---

## Run the Code Hotspots recipe

The Code Hotspots recipe in Arm Performix identifies which functions in your application consume the most CPU time. This analysis helps identify areas of code that can benefit from optimization.

To run the recipe:

1. In Performix, select the **Code Hotspots** recipe from the list of available recipes.

    ![Arm Performix Code Hotspots setup form with a ready target, the scalar workload and profiling options configured, a passing pre-run check, and the Run Recipe button#center](images/code_hotspots_run_recipe.png "Selecting the Code Hotspots recipe")

1. Specify the path to your compiled binary and any necessary parameters. Performix assumes the home directory as the base path, so use the relative path from `$HOME`. For this example, run the program with 16M floats and an iteration count of 2000 to ensure sufficient runtime for meaningful sampling:

    ```bash
    performix-analysis/dot_scalar 16777216 2000
    ```

    Arm recommends collecting at least 20 seconds of profiling data to ensure statistically meaningful sampling. Adjust the iteration count if needed for your hardware.

1. Select **Run Recipe** to start the analysis. Performix launches the program on the target and collects periodic samples during execution.

## Interpret the results

After the run completes, Performix displays the results, including a flame graph that highlights where the CPU spends most of its time. Each box represents a function, and its width indicates how frequently it appears in the samples. The stacked layout shows call paths, helping you see how each function is reached.

You can identify optimization opportunities by focusing on the widest blocks, which represent the most significant contributors to runtime.

The `dot_scalar` function dominates the flame graph, indicating it accounts for a large proportion of total CPU cycles.

![Arm Performix Code Hotspots Flame Graph view showing dot_scalar as the hottest function and the Insights panel reporting that it accounts for 99.99% of samples, identifying it as the main optimization target#center](images/code_hotspots_flame_graph.png "Code Hotspots flame graph")

The **Insights** panel shows the sample count. This function accounts for 99.47% of samples.

Switch to the **Call Stack** view to see how the hotspot function is reached and whether its cost comes from the function itself or its callees.

![Arm Performix Call Stack view tracing execution from main through run_bench to dot_scalar, which helps identify how the hotspot is reached#center](images/code_hotspots_call_stacks.png "Call Stack view")

Double-click the hotspot function to open the **Source Code Viewer** and inspect the exact lines of code associated with high CPU usage. When you open the **Source Code Viewer** for the first time, you need to specify the root directory of your source code so Performix can map profiling data to the correct files.

{{% notice Note %}}
The **Source Code Viewer** runs on your local machine. To view annotated source on Performix, copy `scalar_dot_product.cpp` from the target to your local machine:

```bash
 scp username@your-server:~/performix-analysis/scalar_dot_product.cpp .
 ```
{{% /notice %}}

![Arm Performix Source Code Viewer highlighting the hot loop inside dot_scalar with per-line sample counts, showing where the function spends its time#center](images/code_hotspots_source.png "Source code viewer for dot_scalar")

## What you've accomplished and what's next

You identified the `dot_scalar` function as the dominant hotspot in the application. This is expected because it handles all the computation, but knowing it's hot doesn't tell you whether the time is being spent efficiently.

Next, you'll use the CPU Microarchitecture recipe to understand why this function is a bottleneck.
