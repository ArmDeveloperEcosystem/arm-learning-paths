---
# User change
title: "Install RunsOn"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

[RunsOn](https://runs-on.com) is a self-hosted runner manager for GitHub Actions that you can install in your own AWS account. It will automatically spawn EC2 VMs as self-hosted runners for your GitHub Actions workflows.

Runners are launched in less than 30s, and they are between 7x to 15x cheaper than official GitHub runners. You can also select any of the instance types offered by AWS, including arm instances (Graviton processors).

RunsOn can be used for free for non-commercial projects. For commercial projects, a 15-day demo license is available (see [pricing](https://runs-on.com/pricing/)).

## Installation

1. Connect to your AWS account: using your AWS credentials, log into your AWS console, in the account where you want to setup RunsOn (it's best to install RunsOn in its own AWS sub-account if you can, for better isolation and security).

2. Create the CloudFormation stack and GitHub app for RunsOn by following the official [installation guide](https://runs-on.com/guides/install/). This will take about 10 minutes.

3. At the end, follow the link to the deployed AppRunner service endpoint, and you should see a page indicating that your installation is successful. At this point you can start using RunsOn to spawn runners for your GitHub Actions workflows.

![RunsOn success page #center](images/success.jpg "RunsOn success page")

You can now visit the next page in this tutorial to learn how to use your new runners in your workflows.