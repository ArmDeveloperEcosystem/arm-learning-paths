---
title: Prepare AWS Account
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare your AWS account
You’ll need an active AWS account for this Learning Path. If you don't have one yet, refer to the [AWS documentation](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html).

{{% notice Note %}}
This Learning Path assumes that you have administrator-level privileges for your AWS account. {{% /notice %}}

## Install AWS command-line tools
You’ll need the AWS Command-Line Interface (CLI) installed for this section. Follow the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) to install the latest version.

## Set up authentication
You'll need to set up your local environment to authenticate with AWS before deploying Veraison.

The recommended method is Single Sign-On (SSO). Follow the steps in [Veraison's AWS account documentation](https://github.com/veraison/services/tree/main/deployments/aws#aws-account).

To confirm authentication is configured correctly, run a simple command, such as:

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
If this operation fails, pause here and troubleshoot using the [AWS documentation](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-authentication.html) before continuing.
