---
title: Profiling the Application using Streamline
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup Arm Streamline

Follow these steps to configure Arm Streamline Performance Analyzer to capture Mali GPU related data:

* Confirm you Android device is connected to the development machine.
* Navigate to **Start tab**, select **Android (adb)**, select the device and then select the application to debug.
* Click on **Select Counters**

![Select device #center](images/streamline_select.png "Select device")

which opens a new window:

![Select counters #center](images/streamline_select_counters.png "Select counters")

* Search for **Mali Timeline Events: Perfetto**
* Make sure it is listed in the **Events to collect**
* Click Save

## Profiling the application using Streamline

Once you have selected the device, the application and metrics to be collected, click on the **start capture** button. 

This automatically starts the application and begins collecting the profiling data. 

Make sure the application is running as desired on your Android device. After a few seconds, you can stop the capture. 

Wait until Streamline completes processing the data. 

Switch to *Mali Timeline* view as shown below:

!["Mali Timeline Streamline" #center](images/Streamline-mali-timeline.png "Mali Timeline Streamline")

You may have to zoom into the data to the maximum (`500 us`), since you are rendering a very simple 3D object. 

You can analyze 2 consecutive frames as shown below:

!["Two consecutive frames" #center](./images/Streamline-mali-analysis.png "Two consecutive frames")

Arm has worked with the Dawn team to optimize data uploading to GPU buffers for Mali GPUs. 

Arm has implemented a **Fast Path** mechanism wherein the Vertex Queue starts processing in parallel while an earlier Fragment Queue is being processed. 

As you can see from the above picture, there is some overlap between Fragment Queue of first frame and Vertex Queue of the consecutive frame. 

This shows that the application is hitting the **Fast Path** that Arm has implemented to optimize performance of Dawn for Mali GPUs. 

The overlap is small since the application is rendering the same simple 3D object under different orientation. You can extend the application to render complex objects with multiple *Uniform Buffers*. This would show the overlap in more detail.

{{% notice Tip %}}
Feel free to experiment with different counters in Streamline and explore the other CPU profiling data as well.
{{% /notice %}}
