---
title: 9. AWS Account Cleanup (Optional)
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cleanup

**AWS workshop attendees**: The temporary AWS account given to you will automatically be deleted. No other action is necessary at this time. 

**Personal AWS Accounts**: To minimize costs of your AWS resources, you can go to the AWS IoTCore Greengrass deployments page and revise your deployment. In the revision, remove the Edge Impulse custom component from the deployment and redeploy. This will shutdown the "runner" service on your edge device and will no longer send messages into IoTCore when inference results are present. Additionally, if using the EC2 edge device in the workshop, you will want to navigate to the EC2 dashboard, select your EC2 instance you created, and then set the instance state to "terminated" via the "Instance state" button/dropdown. You can also cancel your Greengrass deployments and delete both your Greengrass core device as well as your IoT Thing for your core device (all accomplished via the IoTCore dashboard). 
