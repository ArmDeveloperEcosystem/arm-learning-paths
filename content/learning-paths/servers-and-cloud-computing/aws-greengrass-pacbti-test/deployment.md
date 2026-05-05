---
title: Deploying an AWS IoT Greengrass custom component

weight: 6

layout: "learningpathall"
---

### Introduction

In this section, you use a Greengrass thing group to deploy a set of components, including your PAC/BTI test component, to both Greengrass core devices.

### Create Deployment

1. In the AWS Console, go to **IoT Core** -> **Greengrass** -> **Deployments**, then select **Create**.

![Creating a Greengrass deployment](images/deploy-1.png "Creating a deployment")

2. Name your deployment and select the thing group `My_PAC_BTI_Test_Devices`, then select **Next**.

![Name and select thing group](images/deploy-2.png "Creating a deployment")

3. Select **Next**.

![Select Defaults](images/deploy-3.png "Select Defaults")

4. Select **Next**.

![Select Defaults](images/deploy-4.png "Select Defaults")

5. Select **Next**.

![Select Defaults](images/deploy-5.png "Select Defaults")

6. Scroll down and select **Deploy**.

![Deploy](images/deploy-6.png "Deploy")

7. Once deployed, Greengrass installs and prepares the custom component on each PAC/BTI test device (Thor and RPi5). Wait until the **Execution overview** shows **2** successful targets.

![Deploy status](images/deploy-7.png "Deploy status")

When both devices show successful deployment, you're ready to run PAC/BTI tests on each device.

### What we learned

In this section, you created a Greengrass deployment that targeted the thing group containing both PAC/BTI test devices. The deployment installed the PAC/BTI custom component by following the YAML recipe you defined.