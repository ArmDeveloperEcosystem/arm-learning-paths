---
title: Installing CDK
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is AWS CDK?

AWS CDK is an AWS-native Infrastructure-as-Code (IaC) tool that supports cloud engineers writing IaC templates in multiple programming languages.
Regardless of the language that you choose, your CDK code eventually transpiles to TypeScript, which generates the CloudFormation templates required to deploy the specified resources.

This Learning Path uses the Python flavor of AWS CDK, because the accompanying Copilot Extension  is also written in Python. Writing both IaC and application code in the same language can be especially helpful for teams without dedicated platform engineers.

## How do I install AWS CDK?

To install the required packages, you need npm and Python installed. 

Next, run:

```bash
npm install -g aws-cdk
```

To verify that the installation was successful, run:

```bash
cdk --version
```

You should see a version number returned, confirming a successful setup.

After the CDK CLI is installed, you can use it to create a new Python CDK environment:

```bash
mkdir copilot-extension-deployment
cd copilot-extension-deployment
cdk init app --language python
```

This sets up convenient file stubs and creates a `requirements.txt` file listing the Python CDK libraries. The `init` command uses the name of the project folder to name various elements of the project. Hyphens in the folder name are converted to underscores. 

Next, install the packages listed in `requirements.txt`:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

You are now ready to specify the AWS services needed for your GitHub Copilot Extension.

