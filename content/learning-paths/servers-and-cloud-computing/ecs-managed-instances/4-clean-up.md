---
# User change
title: Clean up AWS resources
description: Remove the Amazon ECS task, capacity provider, cluster, task definition, and optional IAM resources created in this Learning Path.

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Remove AWS resources in order

Remove the resources that you created to avoid ongoing charges. You can't delete a cluster while a cluster-scoped capacity provider is still attached. You can't delete a capacity provider while it's part of the cluster's default capacity provider strategy, or has running tasks.

Clean up resources in the following order:

1. Stop the running task.
2. Delete the capacity provider.
3. Delete the cluster.
4. Deregister and delete the task definition.

You can clean up resources using either the AWS Management Console or the AWS CLI.

## Stop the running task

First, stop the running task.

### Use the AWS Management Console

To stop the task using the console:

1. Navigate to the [console for Amazon ECS](https://console.aws.amazon.com/ecs/v2).
2. Select **Clusters**.
3. Select the cluster **ecs-managed-instances-cluster** that you created earlier.
4. Select **Tasks**.
5. Select the running task.
6. Select **Stop**, then select **Stop selected**.

### Use the AWS CLI

Find the running task Amazon Resource Name (ARN), then use the ARN to stop it:

```console
TASK_ARN=$(aws ecs list-tasks --cluster ecs-managed-instances-cluster --query 'taskArns[0]' --output text)
aws ecs stop-task --cluster ecs-managed-instances-cluster --task "$TASK_ARN"
```

## Delete the capacity provider

Next, delete the ECS Managed Instances capacity provider. Deleting the capacity provider deprovisions and terminates the compute.

### Use the AWS Management Console

To delete the capacity provider using the console:

1. Navigate to the [console for Amazon ECS](https://console.aws.amazon.com/ecs/v2).
2. Select **Clusters**.
3. Select the cluster **ecs-managed-instances-cluster**.
4. Select **Actions**, then select **Update cluster**.
5. Locate the capacity provider for ECS Managed Instances under **Cluster configuration**, and select **Remove**.
6. Select **Update**.
7. Select **Infrastructure**.
8. Under **Capacity providers**, select the capacity provider for ECS Managed Instances, then select **Delete**. Deletion can take a few minutes. 

### Use the AWS CLI

Find the name of the capacity provider that's associated with the cluster:

```console
aws ecs describe-clusters \
  --clusters ecs-managed-instances-cluster \
  --query 'clusters[0].capacityProviders' \
  --output text
```

The capacity provider is part of the cluster's default capacity provider strategy. Clear the default strategy before deleting the capacity provider:

```console
aws ecs put-cluster-capacity-providers \
  --cluster ecs-managed-instances-cluster \
  --capacity-providers `[]` \
  --default-capacity-provider-strategy `[]`
```

Then, delete the capacity provider, replacing `<capacity-provider-name>` with the name from the earlier command:

```console
aws ecs delete-capacity-provider \
  --capacity-provider <capacity-provider-name> \
  --cluster ecs-managed-instances-cluster
```
It can take a few minutes to reach `DELETE_COMPLETE`.

## Delete the cluster

After deleting the capacity provider, delete the cluster.

### Use the AWS Management Console

To delete the cluster using the console:

1. Navigate to the [console for Amazon ECS](https://console.aws.amazon.com/ecs/v2).
2. Select **Clusters**.
3. Select the cluster **ecs-managed-instances-cluster**.
4. Select **Actions**, then select **Delete cluster**.

### Use the AWS CLI

Run the following command to delete the cluster using the CLI:

```console
aws ecs delete-cluster --cluster ecs-managed-instances-cluster
```

## Deregister and delete the task definition

Finally, you can deregister and delete the task definition.

### Use the AWS Management Console

To deregister and delete the task definition using the console:

1. Navigate to the [console for Amazon ECS](https://console.aws.amazon.com/ecs/v2).
2. Select **Task definitions**.
3. Select the **nginx** task definition that you created earlier.
4. Select the task definition revision, for example **nginx:1**.
5. Select **Deregister**.
6. After the task definition revision is deregistered, select **Delete**.

### Use the AWS CLI

Run the following command to deregister and delete the task definition using the CLI:

```console
aws ecs deregister-task-definition --task-definition nginx:1
aws ecs delete-task-definitions --task-definitions nginx:1
```

## (Optional) Remove the IAM roles

You can also remove the IAM roles and instance profile that you created earlier:

```console
aws iam remove-role-from-instance-profile \
  --instance-profile-name ecsInstanceRole \
  --role-name ecsInstanceRole
aws iam delete-instance-profile --instance-profile-name ecsInstanceRole

aws iam detach-role-policy \
  --role-name ecsInstanceRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonECSInstanceRolePolicyForManagedInstances
aws iam delete-role --role-name ecsInstanceRole

aws iam detach-role-policy \
  --role-name ecsInfrastructureRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonECSInfrastructureRolePolicyForManagedInstances
aws iam delete-role --role-name ecsInfrastructureRole
```

## What you've accomplished

You've cleaned up all resources that you created to test deploying containers on AWS Graviton with Amazon ECS Managed Instances.

You can extend the Learning Path workflow to deploy containers on AWS-managed Arm-based instances powered by AWS Graviton, while maintaining control over the instance types and features that you use.
