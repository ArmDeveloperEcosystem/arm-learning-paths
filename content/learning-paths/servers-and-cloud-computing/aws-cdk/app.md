---
title: "Create a sample AWS CDK application"
description: Create a JavaScript AWS CDK application that defines an Amazon ECS service running on Arm-based AWS Fargate compute.
weight: 2

layout: "learningpathall"
---

## Set up a sample AWS CDK application

The AWS Cloud Development Kit (AWS CDK) is an open-source infrastructure as code (IaC) software development framework. 

In this section, you'll create a JavaScript CDK application that defines an Amazon Elastic Container Service (ECS) service running on Arm-based AWS Fargate compute.

Arm-based AWS compute is powered by AWS Graviton processors. For more information about AWS Graviton, see [Level up your compute with AWS Graviton](https://aws.amazon.com/ec2/graviton/level-up-with-graviton/).

### Before you begin

Make sure that you've installed the AWS CDK CLI:

```bash
cdk --version
```

The output is similar to:

```output
2.1125.0 (build 71fd29e)
```

For instructions to set up and install the AWS CDK CLI, see the [AWS CDK install guide](/install-guides/aws-cdk).

Make sure you've installed Node.js:

```bash
node --version
```

The output is similar to:
```output
v26.2.0
```

### Initialize a CDK project

Create a directory for your CDK project and navigate to it:

```bash
mkdir arm-cdk-app
cd arm-cdk-app/
```

After navigating into the project directory, initialize a JavaScript CDK project:

```bash
cdk init --language javascript
```

The output is similar to:

```output
Applying project template app for javascript
# Welcome to your CDK JavaScript project

This is a blank project for CDK development with JavaScript.

The `cdk.json` file tells the CDK Toolkit how to execute your app. The build step is not required when using JavaScript.

## Useful commands

* `npm run test`         perform the jest unit tests
* `npx cdk deploy`       deploy this stack to your default AWS account/region
* `npx cdk diff`         compare deployed stack with current state
* `npx cdk synth`        emits the synthesized CloudFormation template

...
```

### Use the AWS CDK with JavaScript to define a sample application

In the project, you'll find a file called `arm-cdk-app-stack.js` in the `lib` directory. AWS CDK uses this stack definition to deploy all necessary AWS resources.

Update `lib/arm-cdk-app-stack.js` to define a load-balanced Amazon ECS service that runs an NGINX web server on an Arm-based AWS Fargate runtime platform.

Replace the contents of the file with the following code:

```javascript
const cdk = require('aws-cdk-lib');
const ecs = require('aws-cdk-lib/aws-ecs');
const ecsPatterns = require('aws-cdk-lib/aws-ecs-patterns');

class ArmCdkAppStack extends cdk.Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    new ecsPatterns.ApplicationLoadBalancedFargateService(this, 'Service', {
      taskImageOptions: {
        image: ecs.ContainerImage.fromRegistry("nginx:latest"),
        containerPort: 80,
      },
      runtimePlatform: {
        cpuArchitecture: ecs.CpuArchitecture.ARM64,
        operatingSystemFamily: ecs.OperatingSystemFamily.LINUX,
      },
      publicLoadBalancer: true,
    });
  }
}

module.exports = { ArmCdkAppStack };
```

## What you've accomplished and what's next

You've now set up a sample JavaScript application using AWS CDK and defined an Amazon ECS service that runs on Arm-based AWS Fargate compute.

Next, you'll use AWS CDK to synthesize and deploy the application.
