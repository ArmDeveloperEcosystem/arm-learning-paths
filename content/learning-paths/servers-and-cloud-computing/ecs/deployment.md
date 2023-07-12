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

![image #center](https://user-images.githubusercontent.com/87687468/235642307-130785da-6ddd-4eb4-afc3-382d441c1c9d.png)

From the IAM dashboard select `Users` from the left menu and click on `Add user` from the top of the page.

![user #center](https://user-images.githubusercontent.com/87687468/235642557-f2db9563-7c4f-4882-a40a-d81a3c84b9d3.png)

On the `Add user` screen enter a username and select the check box before `Provide user access to the AWS Management Console`. Then select `I want to create an IAM user` and click `Next`

![image #center](https://user-images.githubusercontent.com/87687468/236792673-6e6f4690-f06e-45b3-b87d-243872ddc3a6.png)

### Create an ECR policy

You will need access to the Amazon Elastic Container Registry (ECR) to store container images.  You can create a new policy to attach to the IAM user.

To do so, select `Create policy`.

![permission #center](https://user-images.githubusercontent.com/87687468/237015604-85e79e95-20c8-42b4-a489-f8453693c6ce.png)

Under `Service`, select `Elastic Container Registry`. 

Select `All Elastic Container Registry actions (ecr:*)` under `Actions allowed`. 

![policy #center](https://user-images.githubusercontent.com/87687468/237007344-ef0af46f-d96c-49ed-96e2-9cae5415cc95.png)

Under `Resources`, select `specific` and `Add ARN`. Here you can select the `region` and select `Any` for Repository name under `This account` and click on `Add ARNs`.

![image #center](https://github.com/akhandpuresoftware/arm-learning-paths/assets/87687468/17dc8e33-deec-49e5-a38f-21e204b8c2eb)

Skip the tags by clicking `Next`. 

Fill in an appropriate policy name. You can use `ECR_FullAccess` and select `Create policy`.

### Attaching the access policy

ECS requires permissions for services such as creating ECS clusters and launching containers. 

The best way to add permissions to the new IAM user is to use an Amazon managed policy to grant access.

Select `Attach existing policies directly` under `Set permissions` and search for `AmazonECS_FullAccess` & `ECR_FullAccess`. 

Select the checkbox next to the policies.

![permission1 #center](https://github.com/akhandpuresoftware/arm-learning-paths/assets/87687468/fb69eced-d5be-413f-b550-bef713cad2cc)

Select `Next` to review and then `Create user`. 

![image #center](https://user-images.githubusercontent.com/87687468/237018931-b11edaa3-a78e-40e1-9680-b87cdca27a3e.png)

When you create the user you will see a confirmation screen. 

Save the information in safe place. You will need it to deploy containers.  

A new user is now visible on the `IAM > Users` page. Click on the user and go to the `Security credentials` section. 

Click on `Create access key`

![image #center](https://user-images.githubusercontent.com/87687468/236796346-390f5193-b5cf-4132-a18d-37ea23eba5a9.png)


![image #center](https://user-images.githubusercontent.com/87687468/236796580-521971ca-d3ad-4ce6-a5c4-47aa59d62427.png)

Select `Command Line Interface (CLI)` and click on `Next`

![image #center](https://user-images.githubusercontent.com/87687468/236796940-8a5dcb6a-2008-49c2-a117-72379df22f9d.png)

Add a description and click `Create access key`

![image #center](https://user-images.githubusercontent.com/87687468/236797205-a6a795af-6988-41ed-96da-e2da63bd0a4a.png)

Save `Access key` and `Secret access key`, you will need them to configure the AWS CLI. 

## Create an Elastic Container Registry (ECR)

You can create a repository in ECR to store container images. 

You will need the Amazon Resource Name (ARN), a unique identifier for all AWS resources, of the repository to properly tag and upload a container image.

Log in to the AWS console with the `test_user` credentials you created earlier. 

AWS will ask for your `account id`, `username`, and `password`.

![image #center](https://github.com/akhandpuresoftware/arm-learning-paths/assets/87687468/15119efa-95ec-4dcc-b886-f9152f0f7bc8)

Change your password when prompted. 

![image #center](https://github.com/akhandpuresoftware/arm-learning-paths/assets/87687468/f741024d-1dd2-4a4a-88ed-e340eff26726)

Once you log in, search for Elastic Container Registry.

![image #center](https://user-images.githubusercontent.com/87687468/236801302-7ea5a6ff-09ff-4a35-81d6-576880e240bd.png)

From there fill in the name of the repository as `myapp` and leave the defaults for everything else.

![image #center](https://github.com/akhandpuresoftware/arm-learning-paths/assets/87687468/727d18c4-fe52-4211-abc0-7a0f0d9ea123)

Select `Create Repository` in the lower right of the page and your repository will be created. 

You will see your repository in the list, and the ARN (here it is called a URI for universal resource identifier) which you will need to push your container image to ECR. 

Copy the URI for the next step.

![image #center](https://github.com/akhandpuresoftware/arm-learning-paths/assets/87687468/aa09712b-9950-49f3-8280-8109aee81135)

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

![image #center](https://user-images.githubusercontent.com/87687468/235840042-e7461d64-1c1f-4a61-b930-fb1c24d36281.png)

Name the cluster and the leave the other options with the default values. 

Select `Create`

![image #center](https://user-images.githubusercontent.com/87687468/235840668-d13d607d-b546-4d5f-bf95-00b0f57e8322.png)

A cluster will be created as shown below:

![image #center](https://user-images.githubusercontent.com/87687468/235840972-51355567-ac19-476d-b969-7c010cb41688.png)

## Create an ECS task

An ECS Task is the action that takes your container image and deploys it as a running container. 

To create an ECS Task do the following:

Select `Task Definitions` from the left menu. Then select `Create new Task Definition`

![image #center](https://user-images.githubusercontent.com/87687468/235845002-667547ac-5cb4-4dfb-b81c-0c379bd45745.png)

Enter the name of the `Task definition family` in  `Task definition configuration` 

Enter the name of your container and ARN of our image in the Image box. 

You can copy this from the ECR dashboard if you haven’t already. Leave everything else with default values. 

Click `Next`

![image #center](https://github.com/akhandpuresoftware/arm-learning-paths/assets/87687468/9f057197-22c6-41b3-86f3-813f2a5a9aaf)

{{% notice Note %}} No additional port mapping is needed because Nginx runs on port 80 by default.{{% /notice %}} 

Under Environment Section, select `Operating system/Architecture` as  `Linux/ARM64` and leave everything else as default values. 

Click `Next` in the lower right corner of the dialog.

![mod1 #center](https://github.com/akhandpuresoftware/arm-learning-paths/assets/87687468/3730bb71-bd9e-4b84-ae1c-e39214507292)

![image #center](https://user-images.githubusercontent.com/87687468/235848013-599bfcbe-27a1-4a47-a7ab-2914081b9b2d.png)


![image #center](https://github.com/akhandpuresoftware/arm-learning-paths/assets/87687468/507793d5-08be-46cf-b31f-e626d0bc3505)

Review everything and click on `create` 

Go to the ECS page, select Task Definitions and you should see the new task with a status of ACTIVE.

![image #center](https://user-images.githubusercontent.com/87687468/235849100-2865c98a-77fd-45f9-8d49-5c9acac0f5e9.png)

Select the task in the task definition list. 

Click `Deploy` and select `Run Task`

![image #center](https://user-images.githubusercontent.com/87687468/235880090-aad4cd44-51fd-4e2d-aaf4-d4450db656e5.png)

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

![image #center](https://user-images.githubusercontent.com/87687468/236180290-963d6e6b-a67c-4a74-a102-20f8faa871f5.png)

Click on the link in the Task column and find the Public IP address in the `Configuration` section of the Task page.

![image #center](https://user-images.githubusercontent.com/87687468/236181529-38d2bb22-59d6-4cd5-a7bc-123fcbe39917.png)

Enter the public IP address in your browser to see your app running.

![image #center](https://user-images.githubusercontent.com/87687468/236188907-5953f69d-98c2-4def-b5b2-b6b71186af19.png)

## Shut down the app

When you are done, you’ll want to shut down your Nginx application to avoid charges.

From the ECS page select `Clusters` from the left menu and select your cluster from the list of clusters.

![image #center](https://user-images.githubusercontent.com/87687468/236189556-7516dd61-f9fd-4807-96c3-a9a47d08c9b2.png)

From the table at the bottom of the page select `Tasks`. 

Check the box next to the running task and select `Stop` from the dropdown menu at the top of the table.

![image #center](https://user-images.githubusercontent.com/87687468/236190146-48ec2000-50dc-4772-b4c4-f440577b50b4.png)
