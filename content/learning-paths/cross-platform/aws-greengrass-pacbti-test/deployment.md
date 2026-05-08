---
title: Deploy the AWS IoT Greengrass custom component

weight: 6

layout: "learningpathall"
---

### Overview

In this section, you use a Greengrass thing group to deploy a set of components, including your PAC/BTI test component, to both Greengrass core devices.

### Create the deployment

1. In the AWS Console, go to **IoT Core** > **Greengrass** > **Deployments**, then select **Create**.

![Greengrass Deployments page showing the Create button to start a new deployment#center](images/deploy-1.png "Greengrass Deployments page")

2. Name your deployment and select the thing group `My_PAC_BTI_Test_Devices`, then select **Next**.

![Greengrass deployment configuration showing the deployment name and the My_PAC_BTI_Test_Devices thing group selected#center](images/deploy-2.png "Deployment name and thing group selection")

3. Select **Next**.

![Greengrass deployment step 2 showing component selection with default components listed#center](images/deploy-3.png "Deployment component selection step")

4. Select **Next**.

![Greengrass deployment step 3 showing component configuration options at their defaults#center](images/deploy-4.png "Deployment component configuration step")

5. Select **Next**.

![Greengrass deployment step 4 showing advanced configuration options at their defaults#center](images/deploy-5.png "Deployment advanced configuration step")

6. Scroll down and select **Deploy**.

![Greengrass deployment review page with the Deploy button at the bottom to confirm and start the deployment#center](images/deploy-6.png "Deployment review and Deploy button")

7. After deployment starts, Greengrass installs and prepares the custom component on each PAC/BTI test device (Thor and RPi5). Wait until the **Execution overview** shows **2** successful targets.

![Greengrass deployment status page showing the Execution overview with 2 successful targets, confirming both devices received the component#center](images/deploy-7.png "Deployment status showing 2 successful targets")

When both devices show successful deployment, you're ready to run PAC/BTI tests on each device.

### What you've accomplished

You created a Greengrass deployment that targeted the thing group containing both PAC/BTI test devices. The deployment installed the PAC/BTI custom component on each device by following the YAML recipe you defined.