---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: AWS Credentials

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- cloud
- deploy

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

In this section you will learn how to generate and configure Access keys. Access keys consist of an access key ID and secret access key, which are used to sign programmatic requests that you make to AWS.

## What should I do before generating AWS Access keys?

Install the AWS CLI on your machine using the [install guide](/install-guides/aws-cli/).

## How do I generate AWS Access keys (access key ID and secret access key)?

Go to My Security Credentials

![aws1 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/e1ab1ea2-86a0-404e-be52-629f9f1a9695)

On Your Security Credentials page click on `Create access key`

![aws2 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/a5d9dcd7-640d-44ee-9bc8-791c10796b13 "Access keys")


Copy the `Access key ID` and `Secret access key`

![aws3 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/699c3643-f979-4548-81f9-4300828b6a06 "Copy keys")


## Configure the AWS CLI

Run the following command to set up your AWS CLI:

```console
aws configure
```
The output from the command will be similar to:

```output
$ aws configure
AWS Access Key ID [****************OAGK]: AXXXXXXXXXXXXXXXXXXX
AWS Secret Access Key [****************t3iE]: uXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Default region name [us-east-2]: us-east-2
Default output format [json]: json
```

Replace the value of `Access Key ID`, `Secret Access Key`, `region name` and `output format` with your unique values.

After a successful configuration, you will be able to use the AWS CLI and automation tools like [Terraform](/install-guides/terraform/) from the terminal.
