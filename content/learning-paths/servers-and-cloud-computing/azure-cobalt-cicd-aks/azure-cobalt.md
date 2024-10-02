---
title: "Create self-hosted GitHub Actions Runner and AKS cluster based on Arm-based Microsoft Cobalt VMs"

weight: 2

layout: "learningpathall"
---

## Overview

In this learning path, you will build a .NET 8-based web application using a self-hosted GitHub Actions Arm64 runner. You will deploy the application in an Azure Kubernetes Cluster, running on Microsoft Cobalt 100-based VMs. Self-hosted runners offer increased control and flexibility in terms of infrastructure, operating systems, and tools than GitHub-hosted runners.

{{% notice Note %}}
GitHub-hosted Arm64 runners are now Generally Available. If your GitHub account is part of a Team or an Enterprise Cloud plan, you can use GitHub-hosted Arm64 runners. Follow this [learning path](/learning-paths/cross-platform/github-arm-runners/) to learn how you can configure a GitHub-managed runner.
{{% /notice %}}

## What is Azure Cobalt 100?

Cobalt 100 is Microsoft’s first Arm-based server processor, built using the Armv9 Neoverse-N2 CPU. The Cobalt 100 processor is optimized for the performance of scale out cloud-based applications. 

The Azure Cobalt 100 VM instances include: 

* General purpose -`Dpsv6 and Dplsv6`. 
* Memory optimized - `Epsv6`virtual machines. 

To learn more about Azure Cobalt 100, refer to this [blog](https://techcommunity.microsoft.com/t5/azure-compute-blog/announcing-the-preview-of-new-azure-vms-based-on-the-azure/ba-p/4146353).

Creating a virtual machine based on Azure Cobalt 100 is no different than creating any other VM in Azure. To create this VM, launch the [Azure portal](https://portal.azure.com/) and navigate to Virtual Machines. Select `Create Azure Virtual Machine` in the portal and fill in the details such as `Name`, and `Region`. In the `Size` field, click on `See all sizes` and select the `D-Series v6` family of VMs. Select `D2psv6` from the list and create the VM.

![azure-cobalt-vm #center](_images/azure-cobalt-vm.png)

To learn more about Arm-based VMs in Azure, refer to this [learning path](/learning-paths/servers-and-cloud-computing/csp/azure)

## Configure GitHub Repository

The source code for the application and configuration files required to follow this learning path are hosted in this [github repository](https://github.com/pbk8s/msbuild-azure). This repository also contains the Dockerfile and Kubernetes deployment manifests required to deploy this .NET 8 based application. 

Start by forking this repository.

Once the GitHub repository is forked successfully, navigate to the `Settings` tab and click `Actions` in the left navigation pane. In `Runners`, select `New self-hosted runner` which opens up a new page to configure the runner. For `Runner image` select `Linux` and `Architecture` as `ARM64`. Execute the commands shown on this page on the `D2psv6` VM you created in previous step.

Once the runner is configured successfully, you will see a self-hosted runner appear on the same page in GitHub.

To learn more about creating an Arm-based self-hosted runner refer to this [learning path](/learning-paths/laptops-and-desktops/self_hosted_cicd_github/)

## Create an AKS cluster with Arm-based Azure Cobalt 100 nodes using Terraform

You can create an Arm-based AKS cluster by following the steps in this [learning path](/learning-paths/servers-and-cloud-computing/aks/cluster-deployment/). Make sure to update the `main.tf` file with the correct VM as shown:

```console
`vm_size` = `Standard_D2ps_v6`
```
Once the cluster creation is successful, you can proceed to the next section.

## Create container registry with ACR

Create a container registry in Azure Container Registry to host the docker images for your application. Use the following command to create the registry:

```console
az acr create --resource-group myResourceGroup --name mycontainerregistry
```
## Set up GitHub Secrets

GitHub Actions needs access to Azure Container Registry to push application docker images and Azure Kubernetes Service to deploy application pods. Create the following secrets in your GitHub repository:

- `ACR_Name` with the name of your Azure Container Registry
- `AZURE_CREDENTIALS` with Azure Credentials of a Service Principal
- `CLUSTER_NAME` with the name of your AKS cluster
- `CLUSTER_RESOURCE_GROUP_NAME` with the name of your resource group

Refer to this [guide](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-secret) if you need help with signing into Azure using GitHub Actions. 

## Deploy a .NET based application 

.NET added support for arm64 applications starting with version 6. Several performance enhancements have been made in later versions. The latest version that supports Arm64 targets is .NET 9. In this learning path you will use the .NET 8 SDK for application development.

In your fork of the github repository inspect the `aks-ga-demo.csproj` file. Verify that the `TargetFramework` field has `net8.0` as the value. The contents of the file are shown below:

```console
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>aks_ga_demo</RootNamespace>
  </PropertyGroup>

</Project>
```

You can inspect the contents of the `Dockerfile` within your repository as well. This is a multi-stage Dockerfile with the following stages: 

1. `base` stage - Prepares the base environment with the `.NET 8 SDK` and exposes ports 80 and 443.
2. `build` stage - Restores dependencies and builds the application
3. `publish` stage - Publishes the application making it ready for deployment
4. `final` stage - Copies the published application into the final image and sets the entry point to run the application

```console
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["aks-ga-demo.csproj", "./"]
RUN dotnet restore "./aks-ga-demo.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "aks-ga-demo.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "aks-ga-demo.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "aks-ga-demo.dll"]
```

Now, navigate to the `k8s` folder and check the Kubernetes yaml files. The `deployment.yml` file defines a deployment for the application. It specifies the container image to use from ACR and exposes port 80 for the application. The deployment ensures that the application runs with the defined resource constraints and is accessible on the specified port.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: githubactions-aks-demo
spec:
  selector:
    matchLabels:
      app: githubactions-aks-demo
  template:
    metadata:
      labels:
        app: githubactions-aks-demo
    spec:
      containers:
      - name: githubactions-aks-demo
        image: msbuilddemo.azurecr.io/githubactions-aks-demo
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"
        ports:
        - containerPort: 80
```

The `service.yml` file defines a `Service` and uses `LoadBalancer` to expose the service externally on port 8080, directing traffic to the application’s container on port 80.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: githubactions-aks-demo-service
spec:
  selector:
    app: githubactions-aks-demo
  type: LoadBalancer
  ports:
  - port: 8080
    targetPort: 80
```

Finally, let's look at the GitHub Actions file located at `.github/workflows/deploytoAKS.yml` 

```yaml
name: Deploy .NET app

on:
  workflow_dispatch:
  push:
  

jobs:
  deploy:
    name: Deploy application
    runs-on: self-hosted
    
    steps:
      - name: Checkout repo
        uses: actions/checkout@v2

      - name: Build image
        run: docker build -t githubactions-aks-demo:'${{github.sha}}' .
      
      - name: Azure login
        uses: azure/login@v1.4.6
        with:
          creds: '${{ secrets.AZURE_CREDENTIALS }}'

      - name: ACR login
        run: az acr login --name msbuilddemo

      - name: Tag and push image
        run: |
          docker tag githubactions-aks-demo:'${{github.sha}}' msbuilddemo.azurecr.io/githubactions-aks-demo:'${{github.sha}}'
          docker push msbuilddemo.azurecr.io/githubactions-aks-demo:'${{github.sha}}'

      - name: Get AKS credentials
        env:
          CLUSTER_RESOURCE_GROUP_NAME: ${{ secrets.CLUSTER_RESOURCE_GROUP_NAME }}
          CLUSTER_NAME: ${{ secrets.CLUSTER_NAME }}
        run: |
          az aks get-credentials \
            --resource-group $CLUSTER_RESOURCE_GROUP_NAME \
            --name $CLUSTER_NAME \
            --overwrite-existing
      
      - name: Deploy application
        uses: Azure/k8s-deploy@v1
        with:
          action: deploy
          manifests: |
           k8s/deployment.yml
           k8s/service.yml
          images: |
            msbuilddemo.azurecr.io/githubactions-aks-demo:${{github.sha }}
```

This GitHub Actions yaml file defines a workflow to deploy a .NET application to Azure Kubernetes Service (AKS). This workflow runs on the self-hosted GitHub Actions runner that you configured earlier. This workflow can be triggered manually or on a push to the repository. 

It has the following main steps:

1. `Checkout repo` - Checks out the repository code.
2. `Build image` - Builds a Docker image of the application.
3. `Azure login` - Logs in to Azure using stored credentials in GitHub Secrets.
4. `ACR login` - Logs in to Azure Container Registry (ACR).
5. `Tag and push image` - Tags and pushes the Docker image to Azure Container Registry.
6. `Get AKS credentials` - Retrieves Azure Kubernetes Cluster credentials.
7. `Deploy application` - Deploys the application to AKS using specified Kubernetes manifests.

## Run the CI/CD pipeline

Trigger the pipeline manually by navigating to `Actions` tab in the GitHub repository. Select `Deploy .NET app` and click on `Run Workflow`. You can also execute the pipeline by making a commit to the repository. Once the pipeline executes successfully, you should see the Actions output similar to what is shown below:

![github-run #center](_images/github-run.png)

You can check your kubernetes cluster and see new application pods deployed on the cluster as shown below:

![kubernetes-deployment #center](_images/kubernetes-deployment.png)




