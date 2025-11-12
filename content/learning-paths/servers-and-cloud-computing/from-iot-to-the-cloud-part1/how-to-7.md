---
title: Azure Container Registry
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You have now learned how to containerize the application. In this next step, you will push the Docker image to the Azure Container Registry. Before you can push the image, you will need to create the container registry in Azure.

### Creating the container registry in Azure
To create the Azure Container Registry, we will use the Azure Command Line Interface (`Azure CLI`):
1. In the WSL console, type the following command and wait for the installation to complete:

```console
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

2.	Login to your Azure subscription:
```console
az login
```
3.	The command will open the web browser and redirect to the Azure login page. Use this page to provide your credentials.

4.	Now create the resource group name rg-arm64 with a default location set to EastUS:
```console
az group create -n rg-arm64 -l eastus
```
5.	Create the Azure Container Registry of name people in the rg-arm64 group using the Basic pricing tier:
```console
az acr create -n people -g rg-arm64 --sku Basic
```

The output of the above commands will look as shown below:
![command prompt#left](figures/20.webp "Figure 20. Creating the Azure Container Registry")

In the next step, we must configure the role assignment so that the current Azure user can push Docker images to the Azure Container Registry. To do so, we use the WSL terminal, in which we type:
```console
USER_ID=$(az ad user show --id "<YOUR_USER_ID>" –query "id" -o tsv)

ACR_ID = $(az acr list --query "[?contains(name, 'people')].id" -o tsv)

az role assignment create --assignee $USER_ID --role AcrPush --scope $ACR_ID
```

{{% notice Note %}} You’ll need to replace <YOUR_USER_ID> with the username you used.  {{% /notice %}}

The last command's output will look as follows:
![command prompt#left](figures/21.webp "Figure 21. Creating the role assignment")
