---
title: Manually running benchmarks
weight: 51

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll download the results of the benchmark you ran manually in the previous sections from each VM. You will use these results to understand how `sweet` and `benchstat` work together.

## Download Benchmark Results from each VM
Lets walk through the steps to manually download the sweet benchmark results from your initial run on each VM.


1. **Locate results:** Change directory to the `results/markdown` directory and list the files to see the `arm-benchmarks.result` file:

   ```bash
   cd results/markdown
   ls -d $PWD/*
   ```

2. **Copy result path:** Copy the absolute pathname of `arm-benchmarks.result`.

3. **Download results:** Click `DOWNLOAD FILE`, and paste the **ABSOLUTE PATHNAME** you just copied for the filename, and then click `Download`. This will download the benchmark results to your local machine.

   ![](images/run_manually/6.png)

4. **Rename the file:** Once downloaded, on your local machine, rename this file to `c4a.result` so you can distinguish it from the x86 results you'll download later. This naming convention will help you clearly identify which results came from which architecture. You'll know the file downloaded successfully if you see the file in your Downloads directory with the name `c4a.result`, as well as the confirmation dialog in your browser:

   ![](images/run_manually/7.png)

5. **Repeat for c4 instance:** Repeat steps 2-8 with your `c4` (x86) instance. Do everything the same, except after downloading the c4's `arm-benchmarks.result` file, rename it to `c4.result`.

Now that you have the results from both VMs, in the next section, you'll learn how to use benchstat to analyze these results and understand the performance differences between the two architectures.
