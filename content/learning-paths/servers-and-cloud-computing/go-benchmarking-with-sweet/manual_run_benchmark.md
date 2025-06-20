---
title: Manually running benchmarks
weight: 51

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Section Overview

In this section, you'll run benchmarks manually to understand how `sweet` and `benchstat` work together.

## Run Benchmarks on Each Machine
The following explains how to run the benchmarks by hand on each machine.

1. **Access VM instances:** Navigate to the GCP [VM Instances](https://console.cloud.google.com/compute/instances) console.

2. **Connect to c4a instance:** Click on the `SSH` button next to your `c4a` instance.
   An SSH terminal will open in a new tab.

   ![](images/run_manually/2.png)

3. **Set up environment:** Copy and paste the following into the SSH terminal to setup the environment and change to the sweet directory:

   ```bash
   cd benchmarks/sweet
   export GOPATH=$HOME/go
   export GOBIN=$GOPATH/bin
   export PATH=$PATH:$GOBIN:/usr/local/go/bin
   ```

   ![](images/run_manually/3.png)

{{% notice Note %}}
The above instructions assume you installed the benchmarks in the `~/benchmarks/sweet` directory. If you installed them elsewhere, adjust the path accordingly.
{{% /notice %}}   


4. **Run the benchmark:** Copy and paste the following command to run the `markdown` benchmark with `sweet`:

   ```bash
   sweet run -count 10 -run="markdown" config.toml
   ```

5. **Locate results:** After the benchmark completes, cd to the `results/markdown` directory and list the files to see the `arm-benchmarks.result` file:

   ```bash
   cd results/markdown
   ls -d $PWD/*
   ```

6. **Copy result path:** Copy the absolute pathname of `arm-benchmarks.result`.

7. **Download results:** Click `DOWNLOAD FILE`, and paste the **ABSOLUTE PATHNAME** you just copied for the filename, and then click `Download`. This will download the benchmark results to your local machine.

   ![](images/run_manually/6.png)

8. **Rename the file:** Once downloaded, on your local machine, rename this file to `c4a.result` so you can distinguish it from the x86 results you'll download later. This naming convention will help you clearly identify which results came from which architecture. You'll know the file downloaded successfully if you see the file in your Downloads directory with the name `c4a.result`, as well as the confirmation dialog in your browser:

   ![](images/run_manually/7.png)

9. **Repeat for c4 instance:** Repeat steps 2-8 with your `c4` (x86) instance. Do everything the same, except after downloading the c4's `arm-benchmarks.result` file, rename it to `c4.result`.

Now that you have the results from both VMs, in the next section, you'll learn how to use benchstat to analyze these results and understand the performance differences between the two architectures.