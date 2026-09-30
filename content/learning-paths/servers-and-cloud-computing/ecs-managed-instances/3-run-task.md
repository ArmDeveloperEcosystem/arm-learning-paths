---
# User change
title: Run a container as an Amazon ECS task on AWS Graviton
description: Run an NGINX container as a standalone Amazon ECS task on Managed Instances and verify that it runs on AWS Graviton-based compute.

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Run a standalone Amazon ECS task

You can run a task definition in two ways on Amazon ECS. A *service* maintains a desired number of tasks, replaces failed tasks, and can integrate with a load balancer, which suits long-running applications. A *standalone task* runs once and isn't automatically replaced when it stops, which suits batch jobs and short tests.

You run a standalone task here because you're verifying that a single container lands on Graviton-based compute.

Use the cluster, capacity provider, and task definition that you created earlier to deploy a containerized application as a standalone task:

1. Navigate to the [console for Amazon ECS](https://console.aws.amazon.com/ecs/v2).
2. Select **Clusters**.
3. Select the cluster **ecs-managed-instances-cluster** that you created earlier.
4. Under **Tasks**, select **Run new task**.
5. Under **Task details**, for **Task definition family**, select the **nginx** task definition that you created earlier. 
6. Leave all other values as defaults and select **Create**.

## Verify application deployment 

This is where you confirm the payoff of the Learning Path: that the Amazon CPU-manufacturer and `ARM64` settings you configured earlier caused Amazon ECS to select a Graviton-based instance.

To verify that the application deployed successfully:

1. Select the cluster **ecs-managed-instances-cluster**. 
2. Select **Infrastructure**.
3. Under **Container instances**, note the **Instance type** that AWS chose based on the capacity provider. The `g` in an instance family name, such as `m6g` or `c6g`, indicates an AWS Graviton (Arm-based) processor. The following screenshot shows that the instance type selected by AWS is `m6g.medium`:
      ![Amazon ECS cluster Infrastructure tab showing a completed Managed Instances capacity provider and one active m6g.medium container instance, confirming that AWS selected Graviton-based compute.#center](container-instance.png "Active m6g.medium container instance selected by the capacity provider")
4. Select the container instance that's associated with the ECS Managed Instances capacity provider.
5. Under **Networking**, you'll find the public DNS name and IP address for the instance. Copy the **Public IP** and paste it into a web browser of your choice. 

    You'll see the following welcome message:

    ![Screenshot of the application showing the NGINX welcome page and confirming the web server was deployed on Arm-based compute successfully.#center](nginx-output.png "NGINX welcome page indicating successful deployment")

## What you've accomplished

You've successfully deployed a containerized application on Graviton-based instances using Amazon ECS Managed Instances. You can extend this workflow to deploy containers on AWS-managed Arm-based instances powered by AWS Graviton, while maintaining control over the instance types and features that you use. 

Next, you'll remove the task and the AWS resources that you created.
