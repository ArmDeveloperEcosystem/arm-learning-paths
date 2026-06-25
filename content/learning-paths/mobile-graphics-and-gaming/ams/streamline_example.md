---
# User change
title: Interpret an example Arm Streamline report

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## View the example Arm Streamline report

To help you understand the capabilities of Streamline, an example Streamline profile is provided with Arm Performance Studio.

1. To open the example profile, in Streamline, select `File` > `Import`.
2. Select `Import Streamline Sample Captures` and click `Next`.
    ![Screenshot of the Streamline Import dialog with Import Streamline Sample Captures selected before clicking Next#center](images/import.png "Import Streamline Sample Captures")

3. Select the Android example and click `Finish`.
    ![Screenshot of the Import Sample Captures dialog with the Android GPU Bound Example selected before clicking Finish#center](images/samples.png "Select sample captures")

4. Double-click on the report in `Streamline Data`, then click `Analyze` when prompted. After the report is processed, you'll see an interactive timeline.
![Screenshot of the Streamline Timeline tab for the Android GPU Bound Example showing CPU cycles, draw calls, frame rate, Mali core cycles, and process activity#center](images/timeline.png "Streamline Timeline")

## Analyze the results

The charts in the `Timeline` view show the performance counter activity captured from the device. Hover over the charts to see the values at that point in time. Use the Calipers to focus on particular windows of activity. Refer to the [Streamline User Guide](https://developer.arm.com/documentation/101816/latest/Analyze-your-capture) for full instructions on how to use the features in the `Timeline` view.

Understanding the output of Streamline is key to the usefulness of Streamline. [Android performance triage with Streamline](https://developer.arm.com/documentation/102540/latest/) describes how to understand the capture from a number of points of view, depending on what information you are trying to extract from it.

## What you've accomplished and what's next

You've now viewed an example Arm Streamline report and interpreted the results using Arm documentation. 

Next, you'll use Arm Streamline to capture data for your application. 

