---
# User change
title: "Prepare AWS account for GitHub integration"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
AWS and GitHub provide powerful functionality for cloud-based development flows. We will learn how to integrate these technologies for the purpose of automating test and validation on Arm Virtual Hardware.

## Fork and clone example project

Arm provides an example project to help you get started. This also includes a template to assist setting up your AWS account.

Fork the example into your GitHub repository from:
```url
https://github.com/ARM-software/AVH-GetStarted/fork
```
Full documentation on the example is available [here](https://arm-software.github.io/AVH/main/examples/html/GetStarted.html).

For documentation on the CI/CD workflow see [here](https://arm-software.github.io/AVH/main/examples/html/GetStarted.html#GS_SetupCI).

## CloudFormation stack {#steps}

Within this project, there is a file:
```output
    infrastructure/cloudformation/Arm-AVH-CloudFormation-Template.yaml
```
which can be used to help set up your AWS account appropriately.

Navigate to `CloudFormation` area of your AWS console, and click on `Create stack`.

Select `Template is ready`, and `Upload a template file`, and browse to the above `Arm-AVH-CloudFormation-Template.yaml`. Click Next.

Enter an (arbirary) `Stack name` and `S3BucketName`, and select the `VpcId` (likely only one option present) from the pull down. Click Next.

Leave `Configure stack options` as default for all. Click Next.

Optionally make tag and other settings in the `Review stackname` page, else keep as defaults. Accept any acknowledgements presented. Click Submit.

Your `CloudFormation stack` will be generated. The process takes a few minutes, click refresh to follow progress.

When complete, a list of key values will be shown in the `Outputs` tab. We shall return to these later.

### Stack generation issues

`Arm-AVH-CloudFormation-Template.yaml` contains permission settings that relate to corporate AWS accounts. If you have issues generating the stack, edit the file, commenting out lines containing:
```
    PermissionsBoundary: !Sub 'arn:aws:iam::${AWS::AccountId}:policy/ProjAdminsPermBoundaryv2'
```
and repeat the [steps](#steps) to create the stack.

## IAM trust policy

Navigate to `IAM` > `Roles`, and click on the Role Name `Proj-AVHRole`, which was created by the above `CloudFormation stack`.

Navigate to the `Trust relationships` tab, and click on `Edit trust policy` to edit the JSON.

Replace the text:
```console
YOUR_GITHUB_ORG/YOUR_GITHUB_REP
```
with appropriate values for your personal GitHub repository. Wild-card characters are allowed.

For example, to enable all of `mygithubid`'s repositories, use:
```console
mygithubid/*
```
Click `Update policy` when done.

Your AWS account is now set up for use with the example project.
