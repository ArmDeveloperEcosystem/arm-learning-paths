---
# User change
title: Set up the AWS environment
description: Create the IAM roles required by Amazon ECS Managed Instances and register an Arm64 task definition for an NGINX container.

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## What Amazon ECS Managed Instances is

Amazon ECS Managed Instances is a compute option for deploying containers on AWS. Compared to AWS Fargate, you can maintain greater control over the Amazon EC2 feature and instance types that are used. 

Some of the compute attributes that you can control include the following:

- vCPU count
- Memory
- Accelerator type
- Local storage
- Instance type and family
- CPU manufacturer


AWS automatically selects an instance based on the compute attributes that you specify. With Amazon ECS Managed Instances, infrastructure management — such as software and OS patching, instance scaling, and maintenance — are handled by AWS on your behalf. 

For more information, see [Architect for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html) in the Amazon ECS documentation. 

## Create AWS IAM roles

To use Amazon ECS managed instances, you need an instance profile and an infrastructure role.

Start by creating an infrastructure role for Amazon ECS Managed Instances that uses the `AmazonECSInfrastructureRolePolicyForManagedInstances` managed policy. For instructions to create the role, see [Amazon ECS infrastructure IAM role](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html) in the Amazon ECS documentation. 

After creating an infrastructure role, create the instance profile. Ensure that the name of the instance role starts with `ecsInstanceRole`, and that you're using the `AmazonECSInstanceRolePolicyForManagedInstances` managed policy. For instructions to create the role, see [Amazon ECS Managed Instances instance profile](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-profile.html) in the Amazon ECS documentation.


## Register an Arm-compatible Amazon ECS task definition 

Task definitions are a blueprint for containerized applications on Amazon ECS. 

To deploy a containerized application on Arm-based AWS compute, register a task definition that supports the `ARM64` architecture:

1. Navigate to the [console for Amazon ECS](https://console.aws.amazon.com/ecs/v2).
2. Select **Task definitions**.
3. Select **Create new task definition**, then **Create new task definition with JSON**.
4. Paste the following JSON:

    ```json
    {
      "family": "nginx",
      "containerDefinitions": [
        {
          "name": "ecs-managed-instances-graviton-task-def",
          "image": "nginx",
          "cpu": 0,
          "portMappings": [
            {
              "containerPort": 80,
              "hostPort": 80,
              "protocol": "tcp",
              "name": "nginx-80-tcp",
              "appProtocol": "http"
            }
          ],
          "essential": true,
          "environment": [],
          "environmentFiles": [],
          "mountPoints": [],
          "volumesFrom": [],
          "ulimits": [],
          "systemControls": []
        }
      ],
      "networkMode": "host",
      "volumes": [],
      "placementConstraints": [],
      "requiresCompatibilities": [
        "MANAGED_INSTANCES"
      ],
      "cpu": "1024",
      "memory": "3072",
      "runtimePlatform": {
        "cpuArchitecture": "ARM64",
        "operatingSystemFamily": "LINUX"
      },
      "enableFaultInjection": false
    }
    ```

5. Select **Create**.

## What you've accomplished and what's next

You've now learned what Amazon ECS Managed Instances is, created the necessary AWS IAM roles, and registered a task definition that is compatible with the Arm architecture. 

Next, you'll use the available compute attributes to select Arm-based instances for running 
