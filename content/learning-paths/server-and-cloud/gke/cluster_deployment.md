---
# User change
title: "Deploy an Arm based GKE Cluster using Terraform"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Before you begin

Any computer which has the required tools installed can be used for this section. 

You will need a [Google Cloud account](https://console.cloud.google.com/). Create an account if needed. 

Three tools are required on the computer you are using. Follow the links to install the required tools.
* [Terraform](/install-tools/terraform)
* [Kubectl](/install-tools/kubectl/)
* [Google Cloud CLI](/install-tools/gcloud)

## Create a GKE cluster using Terraform

Login to your GCP account and then create a project in your Google Cloud console, using the dropdown menu next to the Google Cloud logo. 

![Untitled](https://user-images.githubusercontent.com/92863151/215955072-86a16917-2607-4e67-83b4-4303d3c1ffa6.png)

There is generally a default project created, which you can use, or Go to **New Project**.

![Untitled](https://user-images.githubusercontent.com/92863151/215955423-5c97a106-bafe-41bd-9275-e0e8aa5eda3f.png)

Enter the name of your project in the **Project name** field and then select the potential locations for your project in the **Location** field.

Click **Create**. The console navigates to the Dashboard page and your project is created within a few minutes.  

![215677455-5b6bf782-fbfa-43f3-b79e-4808d2975214](https://user-images.githubusercontent.com/92863151/215962792-0e1b4b75-38c1-42c6-9dc8-1c31012cbde0.png)

Go to the **[Dashboard](https://console.cloud.google.com/home?_ga=2.56408877.721166205.1675053595-562732326.1671688536&_gac=1.125526520.1675155465.CjwKCAiAleOeBhBdEiwAfgmXfwdH3kCFBFeYzoKSuP1DzwJq7nY083_qzg7oyP2gwxMvaE0PaHVgFhoCmXoQAvD_BwE)** of Google Cloud console. The **project ID** and **project number** are displayed on the **Project info** Dashboard.

![image](https://user-images.githubusercontent.com/92863151/216250615-c4ca08e0-052c-4573-97db-8a0698b9c341.png)

### Acquire user credentials

Initialize the gcloud CLI by running the following command.

```console
gcloud init
```
This will add the SDK to your PATH and grant the SDK permission to access GCP using your user account credentials. This step requires you to log in and then select the project you want to work in.

![image](https://user-images.githubusercontent.com/92863151/215751413-4d5b1fad-65c7-454c-98dc-abdeb8790fb5.png)

URL is generated as the output of the command. Open the URL in the browser and then copy the authorization code.

![image](https://user-images.githubusercontent.com/92863151/215687299-0216b802-f64d-4d60-97fa-b6f6b495bcdd.png)

Now paste the authorization code as below and then select your cloud project, you can also configure a default compute region and zone but in our case, we are skipping it by selecting "n" because we are defining the same in our Terraform file.

![215687984-6d7a597a-4724-41e6-8ade-2852f864515f](https://user-images.githubusercontent.com/92863151/215691694-70536dce-2db6-4042-a9a0-ec4e1900ecc8.png)

Finally, run the following command to add your GCP account to the Application Default Credentials (ADC) so that Google client libraries can use it for billing and quota. This will allow Terraform to access these credentials to provision resources on gcloud.

```console
gcloud auth application-default login
```

![image](https://user-images.githubusercontent.com/92863151/215689339-f8a9ae9f-7894-44b5-a02e-284b049de476.png)

### Enable APIs

Enable [Compute Engine](https://console.developers.google.com/apis/api/compute.googleapis.com/overview) and [Kubernetes Engine](https://console.cloud.google.com/apis/api/container.googleapis.com/overview) APIs for your Google Cloud project where the Service Account was created, these APIs are required for ```terraform apply``` to work on the configuration.

### Create Service Accounts 

Go to **IAM & Admin » Service Accounts**. Once there, click on **CREATE SERVICE ACCOUNT**. The Service Account credentials are needed for Terraform to interact with **Google Cloud APIs** to create the cluster and related networking components.

![service](https://user-images.githubusercontent.com/92863151/215972459-56135d89-05ad-4e48-b523-9773775b944b.png)

Enter a **service account name** and click on **Create and continue**. You will be prompted to select a [IAM roles](https://cloud.google.com/iam/docs/understanding-roles) for it. 

![service name](https://user-images.githubusercontent.com/92863151/215978422-ff66739a-d4ac-465c-b752-1606de0618bb.png)

To grant the service account access to the project, select **Basic: Owner** from the Role dropdown menu. Click **Done** to finish service account creation. You can also create and manage the [service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts) using gcloudCLI.

![image](https://user-images.githubusercontent.com/92863151/215679930-b6fa31e4-9f8c-427a-af12-96047bbe1158.png)

## Deploy the GKE cluster

For GKE deployment, the Terraform configuration is broken into four files: providers.tf, variables.tf, main.tf, and terraform.tfvars.

Add the following code in **providers.tf** file to configure Terraform to communicate with the Google Cloud API and to create GCP resources. 

```console
provider "google" {
project = var.gcp_project_id
region = var.gcp_region
}


# google_client_config and kubernetes provider must be explicitly specified like the following.

data "google_client_config" "default" {}

provider "kubernetes" {
  host                   = "https://${module.gke.endpoint}"
  token                  = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(module.gke.ca_certificate)
}
```

Create a **variables.tf** file for describing the variables referenced in the other files with their type and a default value. Add the following code in **variables.tf** file:

```console
variable "gcp_project_id" {
type = string
description = "gcp_project_id"
}

variable "gcp_region" {
type = string
description = "GCP region"
}

variable "gke_regional" {
type = bool
description = "Gke regional"
}

variable "gcp_cluster_name" {
type = string
description = "GCP Cluster name"
}

variable "gke_zones" {
type = list(string)
description = "list of zones"
}

variable "gke_network" {
type = string
description = "vpc network"
}

variable "gke_subnetwork" {
type = string
description = "vpc subnetwork"
}
```

Add the following code in **terraform.tfvars** file: This file contains actual values of the variables common to all modules of a specific environment. Here, a zonal cluster has been created but you can create a [regional](https://cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters) cluster as well.

```console
gcp_project_id = "your project ID"
gcp_region = "us-central1"
gke_zones =  ["us-central1-a","us-central1-b","us-central1-f"]
gke_regional = false
gke_network = "default"
gke_subnetwork = "default"
gcp_cluster_name = "your cluster name"
```
**NOTE:-** Replace ```"your project ID"``` and ```"your cluster name"``` with your values.

Add the following code in **main.tf** file, this file contains the main set of configurations for your module.

```console
module "gke" {
  source                     = "terraform-google-modules/kubernetes-engine/google"
  project_id                 = var.gcp_project_id
  name                       = var.gcp_cluster_name
  region                     = var.gcp_region
  regional                   = var.gke_regional
  zones                      = var.gke_zones
  network                    = var.gke_network
  subnetwork                 = var.gke_subnetwork
  ip_range_pods              = ""
  ip_range_services          = ""
  http_load_balancing        = false
  network_policy             = false
  horizontal_pod_autoscaling = true
  filestore_csi_driver       = false

  node_pools = [
    {
      name                      = "default-node-pool"
      machine_type              = "t2a-standard-1"
      min_count                 = 1
      max_count                 = 100
      autoscaling               = true
      spot                      = false
      disk_size_gb              = 100
      disk_type                 = "pd-standard"
      image_type                = "COS_CONTAINERD"
      auto_repair               = true
      auto_upgrade              = true
      service_account           = "your-service-account-name@your-project-id.iam.gserviceaccount.com"
      preemptible               = false
      initial_node_count        = 1
    },
  ]

  node_pools_oauth_scopes = {
    all = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }

  node_pools_labels = {
    all = {}

    default-node-pool = {
      default-node-pool = true
    }
  }

  node_pools_metadata = {
    all = {}

    default-node-pool = {
      node-pool-metadata-custom-value = "my-node-pool"
    }
  }

  node_pools_taints = {
    all = []

    default-node-pool = [
      {
        key    = "default-node-pool"
        value  = true
        effect = "PREFER_NO_SCHEDULE"
      },
    ]
  }

  node_pools_tags = {
    all = []

    default-node-pool = [
      "default-node-pool",
    ]
  }
}
```

**NOTE:-** Replace ```"your-service-account-name@your-project-id.iam.gserviceaccount.com"``` with your service account.

The block labeled **node_pools** is where we enter the **service_account** that we have created earlier, number of nodes **(node_count)** for the cluster, a [minimum CPU platform](https://cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform), [Spot VMs](https://cloud.google.com/kubernetes-engine/docs/concepts/spot-vms), a specific [node image](https://cloud.google.com/kubernetes-engine/docs/concepts/node-images), different [machine types](https://cloud.google.com/compute/docs/machine-types), or a more efficient [virtual network interface](https://cloud.google.com/kubernetes-engine/docs/how-to/using-gvnic). The **machine_type** is how we set the cluster to be deployed with Ampere Altra Arm processor. Here, we select **t2a-standard-1** which is a 1 vCPU that runs on the Ampere Altra Arm processor. Tau T2A standard machine types have 4 GB of system memory per vCPU.

There are various standards for the [Tau T2A machine series](https://cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) that can be selected. This series is available only in the selected [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available).

## Terraform commands

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command is responsible for downloading all dependencies which are required for the AWS provider.


```console
terraform init
```
![image](https://user-images.githubusercontent.com/92863151/215668761-c8f00c5e-f9c4-4861-affa-e3b0262d6c6e.png)

### Create a Terraform execution plan

Run `terraform plan` to create an execution plan.

```console
terraform plan
```

**NOTE:** The **terraform plan** command is optional. You can directly run **terraform apply** command. But it is always better to check the resources about to be created.

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan to your cloud infrastructure. The below command creates all required infrastructure.

```console
terraform apply
```      
![image](https://user-images.githubusercontent.com/92863151/215467099-861825d9-e13e-4a79-90ca-40871c7d99ad.png)

To view your cluster, go to **Kubernetes Engine » Clusters**.

![ke cluster](https://user-images.githubusercontent.com/92863151/216003253-5d58eb04-59b4-4785-a9ce-0372beb4dd5a.jpg)

In Kubernetes Engine, select the **cluster** and click on **connect**.

![Untitled](https://user-images.githubusercontent.com/92863151/215472556-5c3a2e09-d7b2-40eb-8643-7b23f074b5ec.png)

### Configure kubectl

Run the following command to retrieve the access credentials for your cluster and automatically configure kubectl. Clicking **connect** brings up a command. Once this command is executed, we will be able to use kubectl.

![image](https://user-images.githubusercontent.com/92863151/216004839-165a8333-569b-455a-a1a2-1686e9d57e9e.png)

![image](https://user-images.githubusercontent.com/92863151/215474553-92f025a7-f3a4-44c7-9817-4157071578f2.png)

Run the following command to see the status of the nodes. The status must be in ready state.

```console
kubectl get nodes
```
![image](https://user-images.githubusercontent.com/92863151/215474251-22019621-f1bb-4a0b-a312-6fce39cde4ee.png)

Run the following command to see the current pods running on the cluster.

```console
kubectl get pods -A
```
![image](https://user-images.githubusercontent.com/92863151/215474160-e8dec087-1464-4369-be2f-11228cb9fac2.png)

