---
# User change
title: Filter for Graviton-based instances with an Amazon ECS Managed Instances capacity provider

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Create an Amazon ECS cluster and a custom capacity provider

When you use Amazon ECS Managed Instances, you'll need to create a capacity provider. The capacity provider is used to manage compute capacity. 

To specify custom instance requirements and select Arm-based instances, create a custom capacity provider in the AWS management console:

1. Navigate to the [console for Amazon ECS](https://console.aws.amazon.com/ecs/v2).
2. Select **Clusters**.
3. Select **Create cluster**.
4. Under **Cluster configuration**, for **Cluster name**, enter **ecs-managed-instances-cluster**.
5. Under **Infrastructure - *advanced***, select **Fargate and Managed Instances** as the method for obtaining compute capacity. 
6. For **Instance profile**, select the instance profile that you created earlier.
7. For **Infrastructure role**, select the Amazon ECS infrastructure role that you created earlier. 
8. For **Instance selection**, select **Use custom - *advanced***.
9. Select **Add instance attribute** to add a third attribute to the list. 
10. Specify the following values for the attributes:
    - For **CPU (vCPU)**, specify a minimum **Attribute value** of **1** and leave the maximum value blank.
    - For **Memory (MiB)**, specify a minimum **Attribute value** of **3072** and leave the maximum value blank.
    - From the dropdown menu for the third attribute, select **CPU Manufactures**, then select **Amazon** as the **Attribute value**. 
    You'll see a list of instance types that meet the memory, CPU, and CPU manufacturer criteria. By selecting Amazon as the manufacturer, you're filtering for AWS Graviton-based instance types. 
11. Under **Network settings**, configure the following:
    - For **VPC**, select an available VPC such as the default VPC.
    - For **Subnets**, select available subnets that are associated with the VPC.
    - For **Security group**, select **Create a new security group**.
    - For **Security group name**, enter **ecs-managed-instance-sg**.
    - Under **Inbound rules for security groups**, select **HTTP** for **Type** and **Anywhere** for source.
12. Leave other settings as defaults and select **Create**. 

## What you've accomplished and what's next

You've now created an Amazon ECS cluster in which you'll run your container. You've also specified CPU, memory, and CPU manufacturer requirements in a capacity provider to filter for Arm-based instances powered by AWS Graviton. 

Next, you'll run a container on an Arm-based instance that meets the instance requirements. 




