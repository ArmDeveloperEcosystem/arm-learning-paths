---
title: "Synthesize and deploy the sample AWS CDK application"
weight: 3

layout: "learningpathall"
---

## Synthesize the AWS CDK application

Before you can deploy an application using the AWS CDK, you need to synthesize it. During synthesis, the AWS CDK checks for errors in the application code and then translates the code into an AWS CloudFormation template. 

Synthesize the application:

```bash
cdk synth
```
You can find the generated JSON template at `cdk.out/ArmCdkAppStack.template.json`. 

## Deploy the AWS CDK application 

After completing synthesis, you're ready to deploy the application. AWS CDK deploys the application through the generated AWS CloudFormation stack. 

Deploy the application:

```bash
cdk deploy
```
The last couple lines of the output include a URL to the web server and the load balancer's DNS name:

```output
Outputs:
ArmCdkAppStack.MyWebServerLoadBalancerDNSXXXXXXX = Hello-MyWeb-ZZZZZZZZZZZZZ-ZZZZZZZZZZ.us-east-1.elb.amazonaws.com
ArmCdkAppStack.MyWebServerServiceURLYYYYYYYY = http://Hello-MyWeb-ZZZZZZZZZZZZZ-ZZZZZZZZZZ.us-east-1.elb.amazonaws.com
```

## Verify application deployment

Open the URL from the deployment output in a web browser of your choice. 

You'll see the following welcome message:

![Screenshot of the application showing the NGINX welcome page and confirming the web server was deployed on Arm-based compute successfully.#center](nginx-output.png "NGINX welcome page indicating successful deployment")

## Clean up AWS resources

After you've validated the deployment, clean up the AWS resources that you created with AWS CDK to avoid incurring costs:

```bash
cdk destroy
```
You'll be prompted to confirm whether you want to delete the resources. Enter `y`. 

## What you've accomplished

You've now synthesized and deployed a sample containerized application on Arm-based compute using Amazon ECS and the AWS CDK. After verifying that the deployment was successful, you cleaned up resources.

You can use this workflow to programmatically deploy and manage containerized applications on Arm-based compute powered by AWS Graviton processors. 