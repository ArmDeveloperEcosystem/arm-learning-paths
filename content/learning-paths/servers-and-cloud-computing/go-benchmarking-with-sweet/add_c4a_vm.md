---
title: Launch an Arm-based c4a-standard-4 instance
weight: 20

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll launch the first of two VMs used for benchmarking Go applications: the Arm-based c4a-standard-4 instance on Google Cloud, (referred to as "c4a").

## Create the c4a-standard-4 instance

Go to the Google Cloud console: [https://console.cloud.google.com/welcome](https://console.cloud.google.com/welcome).

In the search bar at the top, start typing `vm`, then select **VM instances** when it appears.

![alt-text#center](images/launch_c4a/3.png "Select VM instances")

 On the **VM instances** page, click **Create instance**.

![alt-text#center](images/launch_c4a/4.png "Select Create instance")

 In the **Name** field, enter the name of the instance - here it should be `c4a`.

![alt-text#center](images/launch_c4a/5.png "Enter name of the instance")

Now select the machine series by scrolling down to the Machine series section, and selecting the **C4A** radio button.

![alt-text#center](images/launch_c4a/7.png "Select C4A radio button")

To view machine types, scroll down to the **Machine type** dropdown, and select it to show all available options.

![alt-text#center](images/launch_c4a/8.png "Select Machine type dropdown")

Now choose machine size by selecting **c4a-standard-4** under the **Standard** tab.

![alt-text#center](images/launch_c4a/9.png "Select machine size")

To configure storage, select the **OS and Storage** tab.

![alt-text#center](images/launch_c4a/10.png "Configure storage")

To modify storage settings, select **Change**.

![alt-text#center](images/launch_c4a/11.png "Modify storage settings")

To set disk size, select the **Size (GB)** field and enter "1000" for the value.

![alt-text#center](images/launch_c4a/16.png "Enter value in the Size (GB) field")

Now confirm storage settings by selecting **Select** to continue.

![alt-text#center](images/launch_c4a/18.png "Confirm the selection of settings with the Select button")

To launch the instance, select **Create** to bring up the instance.

![alt-text#center](images/launch_c4a/19.png "Select the Create button to launch the instance")

After a few seconds, your c4a instance is up and running, and you are ready to continue to the next section. 

In the next section, you'll launch the second VM, an Intel-based Emerald Rapids c4-standard-8 (referred to as "c4"), which serves as the comparison system for benchmarking.

