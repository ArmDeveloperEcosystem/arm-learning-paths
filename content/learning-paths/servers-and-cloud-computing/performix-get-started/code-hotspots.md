---
title: Analyze code hotspots

weight: 5

layout: learningpathall
---
Let's use the Code Hotspots recipe in Arm Performix to identify which functions in the example workload consume the most CPU time. This analysis helps to identify areas of the code that may benefit from optimization.

## Run the Code Hotspots recipe

1. In Performix, select the Code Hotspots recipe from the list of available recipes.

    ![Run the Code Hotspots recipe in Arm Performix #center](images/code_hotspots_run_recipe.png "Run the Code Hotspots recipe in Arm Performix")

1. Specify the path to your compiled workload and any necessary parameters. For this example, run the workload with 16M floats and an iteration count of 2000 to ensure a runtime of around 30 seconds:

    ```bash
    ./dot_scalar 16777216 2000
    ```

    Arm recommends collecting at least 20 seconds of profiling data to ensure statistically meaningful sampling. 

1. Select **Run Recipe** to start the analysis. Arm Performix will launch the workload and collect periodic samples during execution.

## Interpret the results

Once the run completes, Arm Performix will display the results, including a flame graph that highlights where the CPU spends most of its time. Each box represents a function, and its width indicates how frequently it appears in the samples. The stacked layout shows call paths, helping you see how each function is reached. In practice, you can quickly identify optimization opportunities by focusing on the widest blocks, which represent the most significant contributors to runtime.

In this example, the `dot_scalar` function dominates the flame graph, indicating it accounts for a large proportion of total CPU cycles.

 ![The flame graph in Arm Performix #center](images/code_hotspots_flame_graph.png "The flame graph in Arm Performix")

 The insights panel shows that this function accounts for 99.96% of samples. If we hover over this function in the flame graph, we see the sample count.

 ![Show the sample count by hovering over a function in the flame graph #center](images/flame_graph_sample_count.png "Show the sample count by hovering over a function in the flame graph")

Switch to the Call Stack view to see how the hotspot function is reached and whether its cost comes from the function itself or its callees.

 ![The call stacks view in Arm Performix #center](images/code_hotspots_call_stacks.png "Viewing call stacks in Arm Performix")

Double-click the hotspot function to open the source code viewer and inspect the exact lines of code associated with high CPU usage. When you open the Source Code Viewer for the first time, you may need to specify the root directory of your source code so Performix can map profiling data to the correct files.

![Viewing source code in Arm Performix #center](images/code_hotspots_source.png "Viewing source code in Arm Performix")

With the Code Hotspots analysis complete, you have identified the `dot_scalar` function as a key area for optimization. We might expect this function to be hot, as it is handling all the computation for the workload. But let’s look closer to check if this time is being spent efficiently. Next, let's use the CPU Microarchitecture recipe to understand why this function is a bottleneck.
