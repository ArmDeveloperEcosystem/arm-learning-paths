---
# User change
title: "Deploy containers using ECS on AWS Graviton processors"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Deploy ECS containers on AWS Graviton processor

Amazon Elastic Container Service (ECS) is a fully managed container orchestration service that makes it easy to deploy, manage, and scale containerized applications. You will learn how to deploy a simple application to ECS and run it on a Fargate cluster. Fargate is a serverless service so you don’t need to worry about provisioning or maintaining EC2 instances (virtual machines).  Fargate supports AWS Graviton processors so you can run containers for the Arm architecture. You will also learn how to create and configure the necessary Identity and Access Management (IAM) user and role permissions.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path. 

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine.

Use the [Docker install guide](/install-guides/docker/), the [AWS CLI install guide](/install-guides/aws-cli/), and the [Terraform install guide](/install-guides/terraform/) if you need to setup any of these tools on your machine.

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

## Create an IAM user and assign permissions

Login to your AWS account as the root user and search for IAM.

![ecs1 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/4b23375b-a3b8-49f7-b77f-1f3651b2ecf2)

From the IAM dashboard select `Users` from the left menu and click on `Add user` from the top of the page.

![ecs2 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/8659eace-12fb-40cd-a239-2a6ca5521d97)

On the `Add user` screen enter a username and select the check box before `Provide user access to the AWS Management Console`. Then select `I want to create an IAM user` and click `Next`

![ecs3 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/0efeb281-2b19-4bc7-b132-10b62f609755)

### Create an ECR policy

You will need access to the Amazon Elastic Container Registry (ECR) to store container images.  You can create a new policy to attach to the IAM user.

To do so, select `Create policy`.

![ecs4 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/43763182-a73e-435d-8a29-05cff61c59ee)

Under `Service`, select `Elastic Container Registry`. 

Select `All Elastic Container Registry actions (ecr:*)` under `Actions allowed`. 

![ecs5 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/0e500091-a103-4387-a862-d0c17eb51036)

Under `Resources`, select `specific` and `Add ARN`. Here you can select the `region` and select `Any` for Repository name under `This account` and click on `Add ARNs`.

![ecs6 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/e2feb854-4bdc-4f38-bf75-d1defbf6e75e)

Skip the tags by clicking `Next`. 

Fill in an appropriate policy name. You can use `ECR_FullAccess` and select `Create policy`.

### Attaching the access policy

ECS requires permissions for services such as creating ECS clusters and launching containers. 

The best way to add permissions to the new IAM user is to use an Amazon managed policy to grant access.

Select `Attach existing policies directly` under `Set permissions` and search for `AmazonECS_FullAccess` & `ECR_FullAccess`. 

Select the checkbox next to the policies.

![ecs7 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/c903a3d6-4908-41ab-ad03-3f3f53053fe2)

Select `Next` to review and then `Create user`. 

![ecs8 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/8e4ca606-56fb-4421-b3b6-4ae2fa6ea203)

When you create the user you will see a confirmation screen. 

Save the information in safe place. You will need it to deploy containers.  

A new user is now visible on the `IAM > Users` page. Click on the user and go to the `Security credentials` section. 

Click on `Create access key`

![ecs9 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/996129d3-7d59-43e2-b1d8-84373f0a9d3e)


![ecs10 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/1c59aa74-ac56-4477-90c1-5d601163d373)

Select `Command Line Interface (CLI)` and click on `Next`

![ecs11 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/7dd0b41b-34d5-419f-937d-9c6ff656be84)

Add a description and click `Create access key`

![ecs12 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/67ca5f82-67bc-4528-9564-3e7ecb48c886)

Save `Access key` and `Secret access key`, you will need them to configure the AWS CLI. 

## Create an Elastic Container Registry (ECR)

You can create a repository in ECR to store container images. 

You will need the Amazon Resource Name (ARN), a unique identifier for all AWS resources, of the repository to properly tag and upload a container image.

Log in to the AWS console with the `test_user` credentials you created earlier. 

AWS will ask for your `account id`, `username`, and `password`.

![ecs13 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/360c57f3-ec3d-425b-8339-f9050d3cb0bd)

Change your password when prompted. 

![ecs14 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/b5be4ac8-daf5-471d-aab5-782151647ace)

Once you log in, search for Elastic Container Registry.

![ecs15 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/5b9c2db7-f770-4d6c-a717-167775a5a04e)

From there fill in the name of the repository as `myapp` and leave the defaults for everything else.

![ecs16 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/eaca4082-371b-4d11-b390-1d0a89423d31)

Select `Create Repository` in the lower right of the page and your repository will be created. 

You will see your repository in the list, and the ARN (here it is called a URI for universal resource identifier) which you will need to push your container image to ECR. 

Copy the URI for the next step.

![ecs17 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/c1463f63-88a2-4912-86e4-e129541b3f56)

## Create the Docker image

You can use the Nginx web server as a test application. 

You can either pull the image from Docker Hub or build it from source files. The instructions below use the container image from Docker Hub.

Download the Nginx image for Arm64 platform using the below command. 

```console
docker pull arm64v8/nginx
```

Tag the image with the ECR URI so it can be saved to the newly created ECR repository. 

```console
docker tag arm64v8/nginx [uri]
```

{{% notice Note %}} 
Replace `[uri]` with your respective URI 
{{% /notice %}}

## Log in to ECR 

Configure CLI access to your AWS account using the access key and secret access key you saved.

Run the command below to configure the AWS CLI:

```console
aws configure
```

The `configure` command will ask for the access key and secret access key you saved while creating the IAM user. 

Next, generate an ECR log in token for Docker. 

The ECR log in token is piped to `docker login` so you can push the container image to ECR using the Docker CLI. 

Make sure to replace `[your account number]` with your account number. 

```console
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin [your account number].dkr.ecr.us-east-2.amazonaws.com
```

If the command succeeds, you will see a `Login Succeeded` message.

## Upload your Docker image to ECR

Use below command to push the image to the ECR repository.

```console
docker push [your account number].dkr.ecr.us-east-2.amazonaws.com/myapp
```

{{% notice Note %}} 
Replace `[your account number]` with your AWS account number.
{{% /notice %}}

## Create a Fargate cluster

Search for `Elastic Container Service` and select `Elastic Container Service`

From the left menu select `Clusters` and then select `Create cluster`

![ecs18 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/21bb5009-0c2f-40a4-b0b8-4861e8d6cb80)

Name the cluster and the leave the other options with the default values. 

Select `Create`

![image #center](https://user-images.githubusercontent.com/87687468/235840668-d13d607d-b546-4d5f-bf95-00b0f57e8322.png)

A cluster will be created as shown below:

![ecs20 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/0a5d8d23-cb37-4b5c-a32a-faccd194f2e9)

## Create an ECS task

An ECS Task is the action that takes your container image and deploys it as a running container. 

To create an ECS Task do the following:

Select `Task Definitions` from the left menu. Then select `Create new Task Definition`

![ecs21 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/74d6e0d1-a1a2-49df-a476-cbaf12a2cee3)

Enter the name of the `Task definition family` in  `Task definition configuration` 

Enter the name of your container and ARN of our image in the Image box. 

You can copy this from the ECR dashboard if you haven’t already. Leave everything else with default values. 

Click `Next`

![ecs22 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/649e1811-d322-428e-901c-8b73636e018e)

{{% notice Note %}} No additional port mapping is needed because Nginx runs on port 80 by default.{{% /notice %}} 

Under Environment Section, select `Operating system/Architecture` as  `Linux/ARM64` and leave everything else as default values. 

Click `Next` in the lower right corner of the dialog.

![image #center](https://user-images.githubusercontent.com/87687468/235848013-599bfcbe-27a1-4a47-a7ab-2914081b9b2d.png)


![ecs23 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/3d54fea6-2a2d-4f99-90f5-bd44e8096e21)

Review everything and click on `create` 

Go to the ECS page, select Task Definitions and you should see the new task with a status of ACTIVE.

![ecs26 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/8e5435f9-1abc-433d-b58c-f64b5c6fe7bc)

Select the task in the task definition list. 

Click `Deploy` and select `Run Task`

![ecs27 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/fe258c65-5809-4d04-9c89-9f8bfe568a90)

Select your cluster from drop down menu of `Existing cluster`. 

In Networking section, select a virtual private cloud (VPC) from the list. If you are building a custom app this should be the VPC assigned to any other AWS services you will need to access from your application. For Nginx, any VPC works. Add at least one subnet.

Edit the security group. Because `Nginx` runs on port 80 by default, and port 80 is open for the container, you also need to open port 80 in the security group. 

Select `Create a new security group` and enter a Security group name and security group description and add a Custom TCP inbound rule that opens port 80.

Auto-assign public IP should be set to ENABLED.

Click on `Create`

![1 #center](https://user-images.githubusercontent.com/87687468/235882089-9d7064d5-d2e2-44f6-99fa-1a94947ca246.JPG)


![image #center](https://user-images.githubusercontent.com/87687468/236178142-dd2d264d-4f5f-44aa-90c9-87f9601acac4.png)

With everything set up, run the task by clicking `Create` in the lower right corner.

## Check that Nginx is running 

After you run the task, you will be forwarded to the Fargate-cluster page. 

When the `Last status`` of your cluster changes to `RUNNING`, your app is up and running. 

You may have to refresh the table a couple of times before the status is `RUNNING` 

![ecs30 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/fd34b03f-46ff-4db5-b26a-43dc7324800f)

Click on the link in the Task column and find the Public IP address in the `Configuration` section of the Task page.

![ecs31 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/053c0f13-ee8c-4903-9832-a601014ddaa6)

Enter the public IP address in your browser to see your app running.

![ecs32 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/25457add-25bc-4c6d-9c2d-cd2fefebcfe2)

## Shut down the app

When you are done, you’ll want to shut down your Nginx application to avoid charges.

From the ECS page select `Clusters` from the left menu and select your cluster from the list of clusters.

![ecs33 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/c578a377-bcd6-4934-8eff-5cfb839fca1a)

From the table at the bottom of the page select `Tasks`. 

Check the box next to the running task and select `Stop` from the dropdown menu at the top of the table.

![ecs34 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/5c48811b-35a8-4ee0-85b1-03ba946ea04d)
