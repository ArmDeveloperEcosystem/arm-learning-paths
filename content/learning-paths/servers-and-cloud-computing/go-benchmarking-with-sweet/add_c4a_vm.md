---
title: Launch an Arm-based c4a-standard-4 instance
weight: 20

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll launch the first of two VMs used for benchmarking Go applications: the Arm-based c4a-standard-4 instance on Google Cloud, (referred to as "c4a").

## Create the c4a-standard-4 instance

To access the Google Cloud console, navigate to [https://console.cloud.google.com/welcome](https://console.cloud.google.com/welcome).

In the search bar at the top, start typing `vm`, then select **VM Instances** when it appears.

![alt-text#center](images/launch_c4a/3.png)

 On the **VM Instances** page, click **Create instance**.

![alt-text#center](images/launch_c4a/4.png)

 In the **Name** field, enter `c4a`.

![alt-text#center](images/launch_c4a/5.png)

Now select machine series by scrolling down to the Machine series section, and selecting the **C4A** radio button.

![alt-text#center](images/launch_c4a/7.png)

To view machine types, scroll down to the **Machine type** dropdown, and select it to show all available options.

![alt-text#center](images/launch_c4a/8.png)

Now choose machine size by selecting **c4a-standard-4** under the **Standard** tab.

![alt-text#center](images/launch_c4a/9.png)

To configure storage, select the **OS and Storage** tab.

![alt-text#center](images/launch_c4a/10.png)

To modify storage settings, select **Change**.

![alt-text#center](images/launch_c4a/11.png)

To set disk size, select the **Size (GB)** field and enter "1000" for the value.

![alt-text#center](images/launch_c4a/16.png)

Now confirm storage settings by selecting **Select** to continue.

![alt-text#center](images/launch_c4a/18.png)

To launch the instance, select **Create** to bring up the instance.

![alt-text#center](images/launch_c4a/19.png)

After a few seconds, your c4a instance is up and running, and you are ready to continue to the next section. 

In the next section, you'll launch the second VM, an Intel-based Emerald Rapids c4-standard-8 (referred to as "c4"), which serves as the comparison system for benchmarking.

