---
title: Benchmark your platform with System Characterization
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run the System Characterization recipe

To understand your platform's memory performance in its current configuration, run the System Characterization recipe in Arm Performix.
![Arm Performix System Characterization configuration screen#center](./preparing-target.webp "System Characterization Configuration")
You have options to collect reasonable default results, or just static system configuration details, or pick and choose benchmarks to run.

Select the target you configured in the setup section. If this is your first run on this target, you might need to select **Install Tools** to copy the collection tools to the target. After the tools are installed, you will see that the target is ready.

Note that the 'Workload type' field is fixed at 'Profile the whole system'. System Characterization examines your whole platform; it does not profile an application or workload.

At the bottom of the recipe configuration page there is a pre-run check to ensure that necessary packages (like the aforementioned `numactrl`) are installed.
![Arm Performix pre-run check#center](./pre-run-check-succeeds.webp "Pre-run Check")

When your configuration is ready, select **Run Recipe** to launch the workload and collect the performance data.
You'll see a progress wheel with a rough time estimate. Note that when manually selecting many benchmarks, the run can take around 30 minutes.
![Arm Performix System Characterization progress#center](./collecting-benchmarks.webp "Collecting Benchmarks")

## View the run results

Arm Performix's System Characterization recipe generates a variety of analysis points. Tabular data is presented in the GUI in tabs like "Idle Latency" and "Peak Bandwidth". Raw data, .csv files, and graphical plots are available through the "Open Run Directory" button on the "Summary" tab. We'll go into several of these  results in the next sections.

![Arm Performix System Characterization report#center](report-generated.webp "Results Summary for run")

## What you've learned and what's next

In this section:
- You ran the System Characterization recipe on your target machine
- You saw a variety of results appear in the run's results page

Next, you'll walk through some of the results collected from various benchmarks.
