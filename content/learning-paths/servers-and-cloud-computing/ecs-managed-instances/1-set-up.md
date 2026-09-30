---
# User change
title: Set up IAM roles and an Arm task definition
description: Create the IAM roles required by Amazon ECS Managed Instances and register an Arm64 task definition for an NGINX container.

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Understand Amazon ECS Managed Instances

Amazon ECS Managed Instances is a compute option for deploying containers on AWS. It sits between AWS Fargate and the Amazon EC2 launch type: AWS manages the infrastructure for you, while you retain access to specific Amazon EC2 instance types, including the ability to use AWS Graviton-based instances.

Amazon ECS runs your tasks using one of the following compute options:

| Compute option | Who manages the instances | Instance type control | Best for |
|----------------|---------------------------|-----------------------|----------|
| AWS Fargate | AWS (serverless, one isolated environment per task) | None | Simple workloads where you don't need to choose instance types |
| ECS Managed Instances | AWS (provisioning, scaling, patching, maintenance) | Yes, including AWS Graviton | Workloads that need specific EC2 capabilities without managing infrastructure |
| Amazon EC2 launch type | You (instances, scaling, patching, AMIs) | Full | Workloads that need maximum control over the instances |

Compared with AWS Fargate, Amazon ECS Managed Instances gives you greater control over the Amazon EC2 features and instance types used to run your containers. Fargate runs each task in its own isolated environment. By contrast, Amazon ECS Managed Instances can place multiple tasks on a larger instance to improve utilization. It also gives you access to the full range of Amazon EC2 instance types.

Some of the compute attributes that you can control include the following:

- vCPU count
- Memory
- Local storage
- Instance type and family
- CPU manufacturer

AWS automatically selects an instance based on the compute attributes that you specify. With Amazon ECS Managed Instances, AWS handles infrastructure management on your behalf, including software and operating system patching, instance scaling, and maintenance.

You'll create IAM roles with the AWS CLI and register a task definition with either the AWS CLI or the AWS Management Console. On the following pages, you'll use the console to create the cluster, capacity provider, and task.

## Before you begin

Before continuing, install and configure the [AWS CLI](/install-guides/aws-cli/), and confirm that you can sign in to the AWS Management Console.

## Create AWS IAM roles

To use Amazon ECS Managed Instances, you need two IAM roles:

- An infrastructure role that allows Amazon ECS to manage the lifecycle of your managed instances on your behalf.
- An instance role, made available to instances through an instance profile, that the Amazon ECS agent assumes to register instances with your cluster and communicate with the Amazon ECS service.

You'll create these roles with the AWS CLI. Make sure your credentials have permission to create IAM roles.

### Create the infrastructure role

First, create a file named `ecs-infrastructure-trust-policy.json` with the following trust policy. This allows the Amazon ECS service to assume the role.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAccessToECSForInfrastructureManagement",
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Next, create a role named `ecsInfrastructureRole` using this trust policy:

```console
aws iam create-role \
  --role-name ecsInfrastructureRole \
  --assume-role-policy-document file://ecs-infrastructure-trust-policy.json
```

Finally, attach the `AmazonECSInfrastructureRolePolicyForManagedInstances` managed policy to the role:

```console
aws iam attach-role-policy \
  --role-name ecsInfrastructureRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonECSInfrastructureRolePolicyForManagedInstances
```

### Create the instance role and instance profile

First, create a file named `ecsInstanceRole-trust-policy.json` with the following trust policy. This allows Amazon EC2 to assume the role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Next, create a role named `ecsInstanceRole` using this trust policy:

```console
aws iam create-role \
  --role-name ecsInstanceRole \
  --assume-role-policy-document file://ecsInstanceRole-trust-policy.json
```

Then, attach the `AmazonECSInstanceRolePolicyForManagedInstances` managed policy to the role:

```console
aws iam attach-role-policy \
  --role-name ecsInstanceRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonECSInstanceRolePolicyForManagedInstances
```

Finally, create an instance profile, then add the role to it:

```console
aws iam create-instance-profile --instance-profile-name ecsInstanceRole

aws iam add-role-to-instance-profile \
  --instance-profile-name ecsInstanceRole \
  --role-name ecsInstanceRole
```

### Verify the roles and instance profile

Confirm that both roles and the instance profile were created successfully:

```console
aws iam get-role --role-name ecsInfrastructureRole --query 'Role.RoleName' --output text
aws iam get-instance-profile --instance-profile-name ecsInstanceRole --query 'InstanceProfile.Roles[0].RoleName' --output text
```

The commands return `ecsInfrastructureRole` and `ecsInstanceRole`. 

You'll use both when you create the cluster on the next page.

## Register an Arm Amazon ECS task definition

An Amazon ECS task definition is a blueprint for a containerized application.

To deploy a containerized application on Arm-based AWS compute, register a task definition that supports the `ARM64` architecture.

Create a file named `nginx-task-def.json` with the following contents. The `runtimePlatform` block sets the architecture to `ARM64`, and `requiresCompatibilities` includes `MANAGED_INSTANCES`:

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

Register the task definition using either the AWS CLI or the AWS Management Console.

### Use the AWS CLI

Register the task definition from the file:

```console
aws ecs register-task-definition --cli-input-json file://nginx-task-def.json
```

The command returns the registered task definition, including its `family` (`nginx`) and `revision` number.

### Alternative: use the AWS Management Console

Instead of using the AWS CLI, you can register the same task definition in the console:

1. Navigate to the [console for Amazon ECS](https://console.aws.amazon.com/ecs/v2).
2. Select **Task definitions**.
3. Select **Create new task definition**, then **Create new task definition with JSON**.
4. Paste the task definition JSON from this page.
5. Select **Create**.

## What you've accomplished and what's next

You've now learned what Amazon ECS Managed Instances is, created the necessary AWS IAM roles, and registered a task definition that is compatible with the Arm architecture. 

Next, you'll create an Amazon ECS cluster and a capacity provider that uses compute attributes to select AWS Graviton-based instances.
