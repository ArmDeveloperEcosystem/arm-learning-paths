---
title: "Create an example AWS CDK application"
weight: 2

layout: "learningpathall"
---

## Set up a sample AWS CDK application

The AWS Cloud Development Kit (CDK) is an open-source software development framework that you can use to define and deploy applications on Arm-based cloud infrastructure on AWS. 

To deploy an application using the CDK, you'll create the application in a supported programming language. You'll then use the CDK CLI to synthesize the application to an AWS CloudFormation template that's deploys resources on AWS. 

### Before you begin

Make sure that you've completed all prerequisite steps and installed the AWS CDK CLI. For more information, see the [AWS CDK install guide](/install-guides/aws-cdk).

### Initialize a CDK project

In this Learning Path, you'll use Amazon Elastic Container Service (ECS) to deploy containers on AWS Graviton-based Amazon EC2 instances. 

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

In the project, you'll find a file called `arm-cdk-app-stack.js` in the `lib ` directory. This stack definition is what AWS CDK uses to deploy resources.

Update `lib/arm-cdk-app-stack.js` with the following:

```javascript
const cdk = require('aws-cdk-lib');
const ec2 = require('aws-cdk-lib/aws-ec2');
const ecs = require('aws-cdk-lib/aws-ecs');
const ecsPatterns = require('aws-cdk-lib/aws-ecs-patterns');

class ArmCdkAppStack extends cdk.Stack {
  constructor(scope, id, props) {
    super(scope, id, props);
    
    //creates a VPC
    const vpc = new ec2.Vpc(this, 'Vpc', {
      maxAzs: 2,
    });
    
    //creates a cluster
    const cluster = new ecs.Cluster(this, 'Cluster', {
      vpc,
    });

    //adds Graviton-based c6g.large instance to the cluster
    cluster.addCapacity('GravitonCapacity', {
      minCapacity: 1,
      desiredCapacity: 1,
      instanceType: new ec2.InstanceType('c6g.large'),
      machineImage: ecs.EcsOptimizedImage.amazonLinux2(ecs.AmiHardwareType.ARM),
    });

    //creates a task definition
    const taskDefinition = new ecs.Ec2TaskDefinition(this, 'TaskDef');

    //adds container to task definition that uses a hello-world container image
    const container = taskDefinition.addContainer('DefaultContainer', {
      image: ecs.ContainerImage.fromRegistry('hello-world'),
      memoryLimitMiB: 512,
    });

    container.addPortMappings({
      containerPort: 80,
    });

    //deploys a load balanced service with one instantiation of the containerized app
    new ecsPatterns.ApplicationLoadBalancedEc2Service(this, 'Service', {
      cluster,
      taskDefinition,
      desiredCount: 1,
      publicLoadBalancer: true,
    });
  }
}

module.exports = { ArmCdkAppStack };
```

The application uses Amazon ECS to deploy a `hello-world` container image on an AWS Graviton-based `c6g.large` instance. 

## What you've accomplished and what's next

You've now set up a sample application using AWS CDK. 

Next, you'll use AWS CDK to synthesize and deploy the application. 