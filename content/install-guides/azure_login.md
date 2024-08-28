---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Azure Authentication

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- cloud
- deploy

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-login

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

In this section you will learn how to authenticate to the Azure environment using the Azure CLI. After log in, the CLI allows you to query and interact with Azure cloud resources.

## Before you begin

Install the Azure CLI on your machine using the [install guide](/install-guides/azure-cli/).

## Sign in interactively

Run the following command to initiate the log in:

```console
az login
```

The output will be similar to what is shown here:

```output
ubuntu@ip-172-31-17-218:~$ az login
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code E5NKJA2HM to authenticate.
```

Open the link in a browser, enter the code that you receive in the above message, and log in into your Azure account. 

You will see the command line details as shown below after you log in.

![azure #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/1b11ecbe-0e70-48c3-a9bf-6712ad2fba4a)

After a successful log in, you will be able to use the [Azure CLI](/install-guides/azure-cli/) and automation tools like [Terraform](/install-guides/terraform/) from the terminal.
