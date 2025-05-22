---
title: Launching an Arm Axion C4a Instance
weight: 20

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
 In this learning path, you'll learn how to benchmark Go code against two newly created systems.  In this chapter, you bring up the first system, an Arm-based Google Axion c4a-standard-4 (c4a for short).  

### Creating the c4a-standard-4 instance

1\. Navigate to [https://console.cloud.google.com/welcome](https://console.cloud.google.com/welcome)


2\. Click into the Search field.


3\. Start typing `vm` until the UI auto-completes `VM Instances`, then click it.

![](images/launch_c4a/3.png)

The VM Instances page appears.

5\. Click `Create instance`

![](images/launch_c4a/4.png)

The Machine configuration page appears.

6\. Click the `Name` field, and enter "c4a" for the `Name`.


![](images/launch_c4a/5.png)



8\. Scroll down to the Machine series section, and select the C4A radio button.

![](images/launch_c4a/7.png)



9\. Scroll down to the Machine type dropdown, and click it to show all available options.

![](images/launch_c4a/8.png)



10\. Select "c4a-standard-4" under the Standard tab.

![](images/launch_c4a/9.png)



11\. Click the "OS and Storage" tab.

![](images/launch_c4a/10.png)



12\. Click "Change"

![](images/launch_c4a/11.png)



13\. Double-click the "Size (GB)" field, then enter "1000" for the value.


![](images/launch_c4a/16.png)

15\. Click "Select" to continue.

![](images/launch_c4a/18.png)

16\. Click "Create" to bring up the instance.

![](images/launch_c4a/19.png)

After a few seconds, our c4a starts up, and you are ready to continue on to the next section, where you will launch the second system, an Intel-based Emerald Rapids c4-standard-8 (c4 for short).

