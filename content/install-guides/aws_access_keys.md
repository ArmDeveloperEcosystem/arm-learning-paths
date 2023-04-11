---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Acquire AWS Access Credentials for Automation

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

### Link to official documentation
official_docs: https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-methods

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

In this section you will learn how to generate Access keys. Access keys consist of an access key ID and secret access key, which are used to sign programmatic requests that you make to AWS.

## Generate Access keys (access key ID and secret access key)

Go to My Security Credentials

![alt-text #center](https://user-images.githubusercontent.com/87687468/190137370-87b8ca2a-0b38-4732-80fc-3ea70c72e431.png "Security credentials")

On Your Security Credentials page click on create access keys (access key ID and secret access key)

![alt-text #center](https://user-images.githubusercontent.com/87687468/190137925-c725359a-cdab-468f-8195-8cce9c1be0ae.png "Access keys")

Copy the Access Key ID and Secret Access Key

![alt-text #center](https://user-images.githubusercontent.com/87687468/190138349-7cc0007c-def1-48b7-ad1e-4ee5b97f4b90.png "Copy keys")

## Configure the AWS CLI

First, make sure AWS CLI is installed in your local system. To install AWS CLI, follow this [guide](/install-guides/aws-cli). Then run the following command to set up your AWS CLI installation:

```console
aws configure
```
The output from the command should look like:

```output
$ aws configure
AWS Access Key ID [****************OAGK]: AXXXXXXXXXXXXXXXXXXX
AWS Secret Access Key [****************t3iE]: uXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Default region name [us-east-2]: us-east-2
Default output format [json]: json
```

Replace the value of `Access key ID`, `Secret access key`, `AWS Region` and `Output format` with your values.
