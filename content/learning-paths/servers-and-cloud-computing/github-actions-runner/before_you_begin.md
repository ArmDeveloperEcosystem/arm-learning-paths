---
# User change
title: "About RunsOn and before you begin"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

[RunsOn](https://runs-on.com) is a self-hosted runner manager for GitHub Actions that you can install in your own AWS account. It will automatically spawn EC2 VMs as self-hosted runners for your GitHub Actions workflows.

Runners are launched in less than 30 seconds, and you can select any of the instance types offered by AWS, including Arm instances with AWS Graviton processors. With Graviton processors, you can run GitHub Actions on Neoverse N1, Neoverse V1, and Neoverse V2 processors.

RunsOn is free for non-commercial projects. For commercial projects, a 15-day demo license is available (see [pricing](https://runs-on.com/pricing/)).


## Before you begin

You need the following to install RunsOn in your AWS account: 
- The name of your GitHub organization. If you are using a personal account, this is your GitHub username.
- A license key. This is a string you obtain from RunsOn by e-mail.
- An e-mail address you want to use to receive notifications from RunsOn.