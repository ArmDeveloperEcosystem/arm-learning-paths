---
title: Prepare AWS Account
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare Your AWS Account
For this learning path, you will need an active AWS account. If you do not have an AWS account, please refer to the [AWS documentation](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html).

This learning path assumes that you have administrator level privileges for your AWS account.

## Install the AWS Command-Line Tools
For this section, you will need the AWS Command-Line (CLI) tools. Please refer to the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for the steps needed to install the latest version of the AWS CLI.

## Set Up Authentication
You will need to configure your local environment to authenticate with the AWS cloud in order to build the Veraison deployment.

The recommended way to do this is using Single Sign-On (SSO). The steps to do this are documented in Veraison's documentation [here](https://github.com/veraison/services/tree/main/deployments/aws#aws-account).

It is important to ensure that authentication is configured correctly. The best way to do this is to run a simple command-line operation such as the following:

```bash
aws ec2 describe-availability-zones
```

You should see output similar to the following (depending on which AWS region you are using):

```output
{
    "AvailabilityZones": [
        {
            "OptInStatus": "opt-in-not-required",
            "Messages": [],
            "RegionName": "eu-west-1",
            "ZoneName": "eu-west-1a",
            "ZoneId": "euw1-az1",
            "GroupName": "eu-west-1-zg-1",
            "NetworkBorderGroup": "eu-west-1",
            "ZoneType": "availability-zone",
            "State": "available"
        },
        {
            "OptInStatus": "opt-in-not-required",
            "Messages": [],
            "RegionName": "eu-west-1",
            "ZoneName": "eu-west-1b",
            "ZoneId": "euw1-az2",
            "GroupName": "eu-west-1-zg-1",
            "NetworkBorderGroup": "eu-west-1",
            "ZoneType": "availability-zone",
            "State": "available"
        },
        {
            "OptInStatus": "opt-in-not-required",
            "Messages": [],
            "RegionName": "eu-west-1",
            "ZoneName": "eu-west-1c",
            "ZoneId": "euw1-az3",
            "GroupName": "eu-west-1-zg-1",
            "NetworkBorderGroup": "eu-west-1",
            "ZoneType": "availability-zone",
            "State": "available"
        }
    ]
}
```
If this operation fails, please do not attempt to proceed with the next steps of this learning path. Refer to [AWS documentation](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-authentication.html) for help with troubleshooting this step.
