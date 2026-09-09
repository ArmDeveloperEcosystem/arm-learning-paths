---
hide_from_navpane: true
title: Clean up AWS resources
description: Remove AWS IoT Greengrass and related cloud resources created for the Edge Impulse deployment when the project is complete.
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clean up AWS resources that you've finished using

After completing this Learning Path, clean up the AWS resources that you created to avoid ongoing costs. 

### Remove the Greengrass deployment

To remove the Greengrass deployment:

1. Navigate to **AWS IoT Core** > **Greengrass** > **Deployments**. 
2. Select your deployment and revise it to remove the Edge Impulse custom component. 
3. Redeploy the updated configuration. 

This shuts down the Edge Impulse Linux Runner service on your edge device and stops MQTT messages from being published to IoT Core.

### Delete the Greengrass core device

To delete the Greengrass core device:

1. Navigate to **AWS IoT Core** > **Greengrass** > **Core devices**. 
2. Select the core device that you created and delete it. 
3. Navigate to **AWS IoT Core** > **All devices** > **Things**. 
4. Delete the IoT thing associated with your core device.

### Delete the S3 bucket

To delete the S3 bucket:

1. Navigate to **S3** in the AWS Console. 
2. Select the bucket that you created for the component artifacts.
3. Empty the S3 bucket.
4. Delete the bucket.

### Delete the Secrets Manager secret

To delete the Secrets Manager secret:

1. Navigate to **Secrets Manager** in the AWS Console.
2. Select the **EI_API_KEY** secret.
3. Delete the selected secret. 

By default, Secrets Manager schedules deletion after a waiting period.

### Terminate the EC2 instance

To terminate the EC2 instance:

1. Navigate to the **EC2** dashboard. 
2. Select your instance.
3. Choose **Instance state** > **Terminate instance**.

## What you've accomplished

You've cleaned up AWS resources that you created for this Learning Path.

You can return to [Verify inference and view results](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/running) to complete the Learning Path. 
