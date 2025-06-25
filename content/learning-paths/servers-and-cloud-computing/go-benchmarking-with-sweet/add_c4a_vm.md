---
title: Launching a Google Axion instance
weight: 20

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
In this section, you'll learn how to spin up the first of two different VMs used for benchmarking Go tests, an Arm-based Google Axion c4a-standard-4 (c4a for short).

## Creating the c4a-standard-4 Instance

1. **Access Google Cloud Console:** Navigate to [https://console.cloud.google.com/welcome](https://console.cloud.google.com/welcome)

2. **Search for VM instances:** Click into the Search field.

3. **Find VM Instances:** Start typing `vm` until the UI auto-completes `VM Instances`, then click it.

![](images/launch_c4a/3.png)

The VM Instances page appears.

4. **Create a new instance:** Click `Create instance`

![](images/launch_c4a/4.png)

The Machine configuration page appears.

5. **Name your instance:** Click the `Name` field, and enter "c4a" for the `Name`.

![](images/launch_c4a/5.png)

6. **Select machine series:** Scroll down to the Machine series section, and select the C4A radio button.

![](images/launch_c4a/7.png)

7. **View machine types:** Scroll down to the Machine type dropdown, and click it to show all available options.

![](images/launch_c4a/8.png)

8. **Choose machine size:** Select "c4a-standard-4" under the Standard tab.

![](images/launch_c4a/9.png)

9. **Configure storage:** Click the "OS and Storage" tab.

![](images/launch_c4a/10.png)

10. **Modify storage settings:** Click "Change"

![](images/launch_c4a/11.png)

11. **Set disk size:** Double-click the "Size (GB)" field, then enter "1000" for the value.

![](images/launch_c4a/16.png)

12. **Confirm storage settings:** Click "Select" to continue.

![](images/launch_c4a/18.png)

13. **Launch the instance:** Click "Create" to bring up the instance.

![](images/launch_c4a/19.png)

After a few seconds, your c4a instance starts up, and you are ready to continue to the next section. In the next step, you will launch the second VM, an Intel-based Emerald Rapids c4-standard-8 (c4 for short), which will serve as the comparison system for our benchmarking tests.

