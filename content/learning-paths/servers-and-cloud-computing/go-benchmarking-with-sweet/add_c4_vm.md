---
title: Launch an Intel Emerald Rapids c4-standard-8 instance
weight: 30

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll set up the second benchmarking system: an Intel-based Emerald Rapids `c4-standard-8` instance on Google Cloud (referred to as **c4**).

## Create the c4-standard-8 instance

Follow the same steps from the previous section where you launched the c4a instance, but make the following changes for the Intel-based c4-standard-8:

* In the **Name** field, enter "c4".
* In the **Machine types for common workloads** section, select the **c4** radio button.
![alt-text#center](images/launch_c4/3.png "Select the c4 radio button")

* In the **Machine configuration** section, open the dropdown select `c4-standard-8`.

![alt-text#center](images/launch_c4/4.png "Open the dropdown and select `c4-standard-8`")

* In the **Machine type** section, open the dropdown and select `c4-standard-8` under the **Standard** tab.

![alt-text#center](images/launch_c4/5.png "Select `c4-standard-8`")

{{% notice Note %}} 
Be sure to set the disk size to **1000 GB** in the **OS and Storage** tab, just as you did for the `c4a` instance.
{{% /notice %}}

After the c4 instance starts up, you are ready to continue to the next section, where you'll install the benchmarking software.
