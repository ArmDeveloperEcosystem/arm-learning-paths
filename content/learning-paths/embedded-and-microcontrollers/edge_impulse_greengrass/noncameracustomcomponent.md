---
hide_from_navpane: true
title: Create the non-camera Greengrass support component
description: Create a non-camera Greengrass component that provides sample images to the Edge Impulse runner on devices without cameras.

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create the non-camera custom component

For those edge devices that do not contain a camera, the following component will prepare the edge device with some sample images that can be referenced by the Edge Impulse "Runner" component's JSON configuration (via "gst\_args" settings) to direct the running model to pull its image data from the file (vs. camera). 

### Clone the component repository

Clone the [Edge Impulse AWS Greengrass workshop supplemental repository](https://github.com/edgeimpulse/aws-greengrass-workshop-supplemental). You'll find the following files:

```text
EdgeImpulseRunnerRuntimeInstallerComponent.yaml
artifacts/EdgeImpulseRunnerRuntime/1.0.0/install.sh
artifacts/EdgeImpulseRunnerRuntime/1.0.0/models.tar.gz
artifacts/EdgeImpulseRunnerRuntime/1.0.0/samples.tar.gz
```

### Copy the artifact files to Amazon S3

From the AWS dashboard, select the S3 dashboard and navigate to the same bucket you created for the "Runner" custom component. 

In that bucket, create the following directory structure:

```text
artifacts/EdgeImpulseRunnerRuntime/1.0.0
```

Within the 1.0.0 directory in S3, upload these files to S3 from your cloned repo (located in ./artifacts/EdgeImpulseRunnerRuntime/1.0.0 within your cloned repo):

```text
install.sh
models.tar.gz
samples.tar.gz
```

Next, edit the `EdgeImpulseRunnerRuntimeInstallerComponent.yaml` and change the artifact location from "YOUR\_S3\_ARTIFACT\_BUCKET" to the actual name of your S3 bucket name (you'll see "YOUR\_S3\_ARTIFACT\_BUCKET" near the bottom of the yaml file). Save the file. 

### Register the custom component

Within the AWS dashboard, go to the IoTCore dashboard, then navigate to "Components" under the "Greengrass devices" drop-down on the left hand side. 

![AWS IoT Greengrass components page with the Create component button available#center](./images/gg_create_nc_component_1.png)

Press "Create Component" and select "YAML" as the recipe format type. 

Copy and paste the contents of your updated/modified file `EdgeImpulseRunnerRuntimeInstallerComponent.yaml` into the text window after clearing the initial contents:

![AWS IoT Greengrass component creation page with the YAML recipe editor ready for the component recipe#center](./images/gg_create_nc_component_2.png)

Finally, press "Create Component" and you should now have 2 custom components registered:

![AWS IoT Greengrass registered component list showing the two custom components#center](./images/gg_create_nc_component_3.png)

## What you've accomplished

You've created the non-camera support component and registered it in AWS IoT Greengrass.

Now that the non-camera support component is created, return to the deployment steps and continue with deploying these components to your edge device via the AWS IoT Greengrass deployment mechanism.

Return to the [component deployment steps](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/customcomponentdeployment/) to continue.
