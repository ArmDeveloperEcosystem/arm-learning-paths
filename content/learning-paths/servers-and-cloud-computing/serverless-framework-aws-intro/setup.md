---
title: Set up Serverless Framework for AWS
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section you will set up the Serverless Framework for AWS. This involves several steps, including installing the Serverless Framework, configuring AWS credentials, and creating a new Serverless service.

## Installation
Start by installing Node.js version 18.20.3 or greater and npm (Node Package Manager). You can download and install them from the [official Node.js website](https://nodejs.org/en).

Then, open the terminal or command prompt and type the following:
```console
npm install -g serverless
```

## AWS Credentials
You need AWS credentials to deploy your Serverless application to AWS. You can create these credentials in the AWS Management Console by following these instructions:
1.	Create IAM User:
* Go to the [IAM console](https://console.aws.amazon.com/iam/).
* Create a new user with programmatic access and attach the AdministratorAccess policy.
2. Configure Credentials:
* Use the AWS CLI to configure your credentials. If you don’t have the AWS CLI installed, follow these [installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

Run the following command to configure your credentials:
```
aws configure
```

Enter your Access Key ID, Secret Access Key, and region. You can use a default value for the output.
