---
title: Launching a Google Axion instance
weight: 20

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Launch an Arm-based c4a-standard-4 instance
In this section, you'll launch the first of two VMs used for benchmarking Go applications: the Arm-based c4a-standard-4 instance on Google Cloud, also referred to as c4a.

## Creating the c4a-standard-4 instance

1. **Access Google Cloud console:** Navigate to [https://console.cloud.google.com/welcome](https://console.cloud.google.com/welcome)

2. **Search for VM instances:** Select the search field.

3. **Find VM Instances:** Start typing `vm` until the UI auto-completes `VM Instances`, then select it.

![](images/launch_c4a/3.png)

The VM Instances page appears.

4. **Create a new instance:** Select **Create instance**

![](images/launch_c4a/4.png)

The Machine configuration page appears.

5. **Name your instance:** Select the **Name** field, and enter "c4a".

![](images/launch_c4a/5.png)

6. **Select machine series:** Scroll down to the Machine series section, and select the C4A radio button.

![](images/launch_c4a/7.png)

7. **View machine types:** Scroll down to the Machine type dropdown, and select it to show all available options.

![](images/launch_c4a/8.png)

8. **Choose machine size:** Select **c4a-standard-4** under the Standard tab.

![](images/launch_c4a/9.png)

9. **Configure storage:** select the **OS and Storage** tab.

![](images/launch_c4a/10.png)

10. **Modify storage settings:** select **Change**

![](images/launch_c4a/11.png)

11. **Set disk size:** Select the **Size (GB)** field, then enter "1000" for the value.

![](images/launch_c4a/16.png)

12. **Confirm storage settings:** Select **Select** to continue.

![](images/launch_c4a/18.png)

13. **Launch the instance:** select **Create** to bring up the instance.

![](images/launch_c4a/19.png)

After a few seconds, your c4a instance starts up, and you are ready to continue to the next section. In the next section, you will launch the second VM, an Intel-based Emerald Rapids c4-standard-8 (abbreviated to c4), which serves as the comparison system for our benchmarking tests.

