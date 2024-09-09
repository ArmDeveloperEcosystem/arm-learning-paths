---
# User change
title: "Install RunsOn in your AWS account"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

[RunsOn](https://runs-on.com) is a self-hosted runner manager for GitHub Actions that you can install in your own AWS account. It will automatically spawn EC2 VMs as self-hosted runners for your GitHub Actions workflows.

Runners are launched in less than 30 seconds, and you can select any of the instance types offered by AWS, including Arm instances with AWS Graviton processors. With Graviton processors you can run GitHub Actions on Neoverse N1, Neoverse V1, and Neoverse V2 processors.

RunsOn is free for non-commercial projects. For commercial projects, a 15-day demo license is available (see [pricing](https://runs-on.com/pricing/)).


## Before you begin

You will need 3 things to install RunsOn in your AWS account. 
- The name of your GitHub organization. If you are using a personal account, this is just your GitHub username.
- A license key. This is a string you obtain from RunsOn by e-mail by following the instructions below.
- An e-mail address you want to use to receive notifications from RunsOn.

## Install RunsOn

Follow the 3 step process to install RunsOn:

1. Connect to your AWS account: using your AWS credentials, log in to the AWS console for the account where you want to setup RunsOn. It's best to install RunsOn in its own AWS sub-account if you can, for better isolation and security.

2. Create the CloudFormation stack and GitHub app for RunsOn by following the official [installation guide](https://runs-on.com/guides/install/). This will take about 10 minutes.

    The installation guide has a link at the top to obtain the license key. 
    
    Once you have your key, proceed with the installation guide by selecting the AWS region you want to use, creating the CloudFormation stack, and installing the GitHub app. 

3. At the end, follow the link to the deployed AppRunner service endpoint, and you should see a page indicating that your installation is successful. 

    At this point you can start using RunsOn to spawn runners for your GitHub Actions workflows.

![RunsOn success page #center](images/success.jpg "RunsOn success page")

Continue to the next page to learn how to use your new runners in GitHub Actions workflows.