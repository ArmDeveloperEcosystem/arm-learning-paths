---
title: "Deploy the example AWS CDK application"
weight: 3

layout: "learningpathall"
---

## Synthesize the AWS CDK application

After creating an application using AWS CDK, you'll need to synthesize it:

```bash
cdk synth
```
This step checks for errors in the application code and then translates the code into an AWS CloudFormation template. 

You can find the generated JSON template at `cdk.out/ArmCdkAppStack.template.json`.

## Deploy the CDK stack 

After completing synthesis, you're ready to deploy the application. AWS CDK will deploy the application through the generated AWS CloudFormation stack. 

Deploy the application:

```bash
cdk deploy
```

The output is similar to:

```output

```

## Validate the deployment

## What you've accomplished

You've now synthesized and deployed a sample application using Amazon ECS and the AWS CDK. 

You can use this workflow to programmatically deploy and manage containerized applications on AWS Graviton-based compute. 