---
# User change
title: Run a container as an Amazon ECS task on AWS Graviton

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Run a standalone Amazon ECS task

Use the cluster, capacity provider, and task definition that you created earlier to deploy a containerized application as a standalone task:

1. Navigate to the [console for Amazon ECS](https://console.aws.amazon.com/ecs/v2).
2. Select **Clusters**.
3. Select the cluster **ecs-managed-instances-cluster** that you created earlier.
4. Under **Tasks**, select **Run new task**.
5. Under **Task details**, for **Task definition family**, select the task definition **ecs-managed-instances-graviton-task-def** that you created earlier. 
6. Under **Environment**, for **Capacity provider strategy**, select **Use cluster default**.
7. Under **Networking**, use the same VPC, subnets, and security group that you used for the cluster. 
8. Choose **Create**.

## Verify application deployment 

To verify that the application deployed successfully:

1. Under **Tasks**, select the task that you created. 
2. Under **Configuration**, note that the **Operating system/Architecture** is **Linux/ARM64**.
3. Under **Networking**, copy the **Public IP** and paste it into a web browser of your choice. 

    You'll see the following welcome message:

    ![Screenshot of the application showing the NGINX welcome page and confirming the web server was deployed on Arm-based compute successfully.#center](nginx-output.png "NGINX welcome page indicating successful deployment")

## What you've accomplished

You've successfully deployed a containerized application on Graviton-based instances using Amazon ECS Managed Instances. 

To avoid accruing costs, stop the task after you've completed testing. For more information, see [Stopping an Amazon ECS task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/standalone-task-stop.html). Also consider [deleting the cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete_cluster-new-console.html), [deregistering the task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deregister-task-definition-v2.html), and [deleting the task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete-task-definition-v2.html). 

You can extend this workflow to control other compute attributes and deploy multiple containers on Graviton-based instances. 