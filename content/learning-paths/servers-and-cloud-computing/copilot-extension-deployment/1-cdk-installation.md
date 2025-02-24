---
title: CDK installation
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is AWS CDK?

AWS CDK is an AWS-native Infrastructure as Code tool that allows cloud engineers to write IaC templates in many different languages. Regardless of the language used, all CDK code eventually transpiles to TypeScript, and the TypeScript generates CloudFormation templates, which then deploy the specified resources.

This Learning Path uses the Python flavor of AWS CDK, because the Copilot Extension that will be deployed is also written in Python. Writing both IaC and application code in the same language is helpful for certain teams, especially those without dedicated platform engineers.

## How do I install AWS CDK?

To install the required packages, you will need npm and Python installed. Next, run:

```bash
npm install -g aws-cdk
```

To verify that the installation was successful, run:

```bash
cdk --version
```

You should see a version number returned, signifying success.

After the CDK CLI is installed, you can use it to create a new Python CDK environment:

```bash
mkdir copilot-extension-deployment
cd copilot-extension-deployment
cdk init app --language python
```

This will set up convenient file stubs, as well as create a `requirements.txt` file with the Python CDK libraries required. The `init` command uses the name of the project folder to name various elements of the project. Hyphens in the folder name are converted to underscores. Install the packages in the `requirements.txt`:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

Now you are ready to specify the AWS services needed for your GitHub Copilot Extension.

