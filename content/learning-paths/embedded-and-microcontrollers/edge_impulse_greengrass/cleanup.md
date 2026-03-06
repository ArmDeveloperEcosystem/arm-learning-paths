---
title: Clean up AWS resources
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clean up AWS resources (optional)

After completing this Learning Path, clean up the AWS resources you created to avoid ongoing costs. The steps below are optional — skip any that you want to keep for further experimentation.

### Remove the Greengrass deployment

Navigate to **AWS IoT Core** > **Greengrass** > **Deployments**. Select your deployment and revise it to remove the Edge Impulse custom component. Redeploy the updated configuration. This shuts down the Runner service on your edge device and stops MQTT messages from being published to IoT Core.

### Delete the Greengrass core device

In **AWS IoT Core** > **Greengrass** > **Core devices**, select the core device you created and delete it. Also navigate to **AWS IoT Core** > **All devices** > **Things** and delete the IoT thing associated with your core device.

### Delete the S3 bucket

Navigate to **S3** in the AWS Console. Select the bucket you created for the component artifacts, empty it, and delete it.

### Delete the Secrets Manager secret

Navigate to **Secrets Manager** in the AWS Console. Select the **EI_API_KEY** secret and delete it. By default, Secrets Manager schedules deletion after a waiting period.

### Terminate the EC2 instance

If you used an EC2 instance as your edge device, navigate to the **EC2** dashboard. Select your instance, then choose **Instance state** > **Terminate instance**.

## Congratulations

You've completed this Learning Path. You set up an Arm-based edge device, built and deployed an Edge Impulse ML model through AWS IoT Greengrass, verified live inference, and used MQTT commands to control the Runner service remotely.
