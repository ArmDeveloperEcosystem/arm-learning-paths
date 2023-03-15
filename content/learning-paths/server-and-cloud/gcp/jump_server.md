---
# User change
title: "Deploy Arm instances on GCP and provide access via Jump Server"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

Any computer which has the required tools installed can be used for this section.

You will need a [Google Cloud account](https://console.cloud.google.com/). Create an account if needed.

Two tools are required on the computer you are using. Follow the links to install the required tools.
* [Terraform](/install-tools/terraform)
* [Google Cloud CLI](/install-tools/gcloud)

## Deploy Arm instances on GCP and provide access via Jump Server

### Introduction to Jump Server
A Jump Server (also known as a bastion host) is an intermediary device responsible for funneling traffic through firewalls using a supervised secure channel. By creating a barrier between networks, jump servers create an added layer of security against outsiders wanting to maliciously access sensitive company data. Only those with the right credentials can log into a jump server and obtain authorization to proceed to a different security zone.

### Acquire user credentials

To acquire user credentials follow this [documentation](/learning-paths/server-and-cloud/gcp/terraform#acquire-user-credentials).

### Generate key-pair(public key, private key) using ssh keygen

Before using Terraform, first generate the key-pair (public key, private key) using `ssh-keygen`. To generate the key-pair, follow this [documentation](/learning-paths/server-and-cloud/gcp/terraform#generate-key-pairpublic-key-private-key-using-ssh-keygen).

### Deploying Arm instances on GCP and providing access via Jump Server
For deploying Arm instances on GCP and providing access via Jump Server, the Terraform configuration is broken into 4 files: **main.tf**, **outputs.tf**, **variables.tf**, **terraform.tfvars**, and a modules directory that contains **vpc-network** and **network-firewall** directories.

Add the following code in **main.tf**. It creates an instance with OS Login configured to use as a bastion host and a private instance to use alongside the bastion host.
```console
terraform {
  required_version = ">= 0.12.26"
}

# Create a Management Network for shared services
module "management_network" {
  source = "./modules/vpc-network"
  project     = var.project
  region      = var.region
}

# Add public key to IAM user
data "google_client_openid_userinfo" "me" {}
resource "google_os_login_ssh_public_key" "cache" {
  project = var.project
  user = data.google_client_openid_userinfo.me.email
  key  = file("path/to/id_rsa.pub")
}

# Ensure IAM user is allowed to use OS Login
resource "google_project_iam_member" "project" {
  project = var.project
  role    = "roles/compute.osAdminLogin"
  member  = "user:${data.google_client_openid_userinfo.me.email}"
}

# Create an instance with OS Login configured to use as a bastion host
resource "google_compute_instance" "bastion_host" {
  project      = var.project
  name         = "bastion-vm"
  machine_type = "t2a-standard-1"
  zone         = var.zone
  tags = ["public"]
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts-arm64"
    }
  }
  network_interface {
    subnetwork = module.management_network.public_subnetwork
    access_config {
      nat_ip = var.static_ip
    }
  }
  metadata = {
    enable-oslogin = "TRUE"
  }
}
# Create a private instance to use alongside the bastion host.
resource "google_compute_instance" "private" {
  project = var.project
  name         = "bastion-private"
  machine_type = "t2a-standard-1"
  zone         = var.zone
  allow_stopping_for_update = true
  tags = ["private"]
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts-arm64"
    }
  }
  network_interface {
    subnetwork = module.management_network.private_subnetwork
  }
  metadata = {
    enable-oslogin = "TRUE"
  }
}
```

**NOTE:-** Replace **path/to/id_rsa.pub** with the location of the public key file.

Add the following code in **outputs.tf**. It defines the output values for this configuration.
```console
output "public_ip_bastion_host" {
  description = "The public IP of the bastion host."
  value       = google_compute_instance.bastion_host.network_interface[0].access_config[0].nat_ip
}

output "private_ip_instance" {
  description = "Private IP of the private instance"
  value       = google_compute_instance.private.network_interface[0].network_ip
}
```

Create a **variables.tf** describing the variables referenced in the other files with their type and a default value.
```console
variable "project" {
  description = "The name of the GCP Project where all resources will be launched."
  type        = string
}

variable "region" {
  description = "The region in which the VPC netowrk's subnetwork will be created."
  type        = string
}

variable "zone" {
  description = "The zone in which the bastion host VM instance will be launched. Must be within the region."
  type        = string
}

variable "static_ip" {
  description = "A static IP address to attach to the instance. The default will allocate an ephemeral IP"
  type        = string
  default     = null
}
```

Add the following code in **terraform.tfvars** This file contains actual values of the variables defined in **variables.tf**
```console
project = "project_ID"
region = "us-central1"
zone = "us-central1-a"
```
**NOTE:-** Replace **project_ID** with your value which can be found in the [Dashboard](https://console.cloud.google.com/home?_ga=2.56408877.721166205.1675053595-562732326.1671688536&_gac=1.125526520.1675155465.CjwKCAiAleOeBhBdEiwAfgmXfwdH3kCFBFeYzoKSuP1DzwJq7nY083_qzg7oyP2gwxMvaE0PaHVgFhoCmXoQAvD_BwE) of Google Cloud console. The [region and zone](https://cloud.google.com/compute/docs/regions-zones#available) are selected depending on the machine type. In our case, it's the [Tau T2A](https://cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) series.

Now create a **modules** directory and inside it create a **network-firewall** and **vpc-network** directories.

Add the following code in **vpc-network/main.tf**.
```console
resource "google_compute_network" "vpc" {
  name    = "bastion-network"
  project = var.project
  # Always define custom subnetworks- one subnetwork per region isn't useful for an opinionated setup
  auto_create_subnetworks = "false"
  # A global routing mode can have an unexpected impact on load balancers; always use a regional mode
  routing_mode = "REGIONAL"
}

resource "google_compute_router" "vpc_router" {
  name = "bastion-router"
  project = var.project
  region  = var.region
  network = google_compute_network.vpc.self_link
}

# Public Subnetwork Config
resource "google_compute_subnetwork" "vpc_subnetwork_public" {
  name = "bastion-subnetwork-public"
  project = var.project
  region  = var.region
  network = google_compute_network.vpc.self_link
  private_ip_google_access = true
  ip_cidr_range            = cidrsubnet(var.cidr_block, var.cidr_subnetwork_width_delta, 0)
  secondary_ip_range {
    range_name = "public-cluster"
    ip_cidr_range = cidrsubnet(var.secondary_cidr_block, var.secondary_cidr_subnetwork_width_delta, 0)
  }
  secondary_ip_range {
    range_name = "public-services"
    ip_cidr_range = var.public_services_secondary_cidr_block != null ? var.public_services_secondary_cidr_block : cidrsubnet(
      var.secondary_cidr_block,
      var.secondary_cidr_subnetwork_width_delta,
      1 * (2 + var.secondary_cidr_subnetwork_spacing)
    )
  }
  dynamic "log_config" {
    for_each = var.log_config == null ? [] : tolist([var.log_config])
    content {
      aggregation_interval = var.log_config.aggregation_interval
      flow_sampling        = var.log_config.flow_sampling
      metadata             = var.log_config.metadata
    }
  }
}

resource "google_compute_router_nat" "vpc_nat" {
  name = "bastion-nat"
  project = var.project
  region  = var.region
  router  = google_compute_router.vpc_router.name
  nat_ip_allocate_option = "AUTO_ONLY"
  # "Manually" define the subnetworks for which the NAT is used, so that we can exclude the public subnetwork
  source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"
  subnetwork {
    name                    = google_compute_subnetwork.vpc_subnetwork_public.self_link
    source_ip_ranges_to_nat = ["ALL_IP_RANGES"]
  }
}

# Private Subnetwork Config
resource "google_compute_subnetwork" "vpc_subnetwork_private" {
  name = "bastion-subnetwork-private"
  project = var.project
  region  = var.region
  network = google_compute_network.vpc.self_link
  private_ip_google_access = true
  ip_cidr_range = cidrsubnet(var.cidr_block, var.cidr_subnetwork_width_delta, 1 * (1 + var.cidr_subnetwork_spacing))
  secondary_ip_range {
    range_name = "private-services"
    ip_cidr_range = var.private_services_secondary_cidr_block != null ? var.private_services_secondary_cidr_block : cidrsubnet(
      var.secondary_cidr_block,
      var.secondary_cidr_subnetwork_width_delta,
      1 * (1 + var.secondary_cidr_subnetwork_spacing)
    )
  }
  dynamic "log_config" {
    for_each = var.log_config == null ? [] : tolist([var.log_config])
    content {
      aggregation_interval = var.log_config.aggregation_interval
      flow_sampling        = var.log_config.flow_sampling
      metadata             = var.log_config.metadata
    }
  }
}

# Attach Firewall Rules to allow inbound traffic to tagged instances
module "network_firewall" {
  source = "../network-firewall"
  project                               = var.project
  network                               = google_compute_network.vpc.self_link
  allowed_public_restricted_subnetworks = var.allowed_public_restricted_subnetworks
  public_subnetwork  = google_compute_subnetwork.vpc_subnetwork_public.self_link
  private_subnetwork = google_compute_subnetwork.vpc_subnetwork_private.self_link
}
```

Add the following code in **vpc-network/outputs.tf**.
```console
output "public_subnetwork" {
  description = "A reference (self_link) to the public subnetwork"
  value       = google_compute_subnetwork.vpc_subnetwork_public.self_link
}

output "private_subnetwork" {
  description = "A reference (self_link) to the private subnetwork"
  value       = google_compute_subnetwork.vpc_subnetwork_private.self_link
}
```

Add the following code in **vpc-network/variables.tf**.
```console
variable "project" {
  description = "The project ID for the network"
  type        = string
}

variable "region" {
  description = "The region for subnetworks in the network"
  type        = string
}

variable "cidr_block" {
  description = "The IP address range of the VPC in CIDR notation. A prefix of /16 is recommended. Do not use a prefix higher than /27."
  default     = "10.0.0.0/16"
  type        = string
}

variable "cidr_subnetwork_width_delta" {
  description = "The difference between your network and subnetwork netmask; an /16 network and a /20 subnetwork would be 4."
  type        = number
  default     = 4
}

variable "cidr_subnetwork_spacing" {
  description = "How many subnetwork-mask sized spaces to leave between each subnetwork type."
  type        = number
  default     = 0
}

variable "secondary_cidr_block" {
  description = "The IP address range of the VPC's secondary address range in CIDR notation. A prefix of /16 is recommended."
  type        = string
  default     = "10.1.0.0/16"
}

variable "public_services_secondary_cidr_block" {
  description = "The IP address range of the VPC's public services secondary address range in CIDR notation."
  type        = string
  default     = null
}

variable "private_services_secondary_cidr_block" {
  description = "The IP address range of the VPC's private services secondary address range in CIDR notation."
  type        = string
  default     = null
}

variable "secondary_cidr_subnetwork_width_delta" {
  description = "Difference between your network and subnetwork's secondary range netmask; an /16 network and a /20 subnetwork would be 4."
  type        = number
  default     = 4
}

variable "secondary_cidr_subnetwork_spacing" {
  description = "How many subnetwork-mask sized spaces to leave between each subnetwork type's secondary ranges."
  type        = number
  default     = 0
}

variable "log_config" {
  description = "The logging options for the subnetwork flow logs."
  type = object({
    aggregation_interval = string
    flow_sampling        = number
    metadata             = string
  })

  default = {
    aggregation_interval = "INTERVAL_10_MIN"
    flow_sampling        = 0.5
    metadata             = "INCLUDE_ALL_METADATA"
  }
}

variable "allowed_public_restricted_subnetworks" {
  description = "The public networks that is allowed access to the public_restricted subnetwork of the network"
  default     = []
  type        = list(string)
}
```

Add the following code in **network-firewall/main.tf**.
```console
data "google_compute_subnetwork" "public_subnetwork" {
  self_link = var.public_subnetwork
}

data "google_compute_subnetwork" "private_subnetwork" {
  self_link = var.private_subnetwork
}

# public - allow ingress from anywhere
resource "google_compute_firewall" "public_allow_all_inbound" {
  name = "bastion-public-allow-ingress"
  project = var.project
  network = var.network
  target_tags   = ["public"]
  direction     = "INGRESS"
  source_ranges = ["0.0.0.0/0"]
  priority = "1000"
  allow {
    protocol = "all"
  }
}

# public - allow ingress from specific sources
resource "google_compute_firewall" "public_restricted_allow_inbound" {
  count = length(var.allowed_public_restricted_subnetworks) > 0 ? 1 : 0
  name = "bastion-public-restricted-allow-ingress"
  project = var.project
  network = var.network
  target_tags   = ["public-restricted"]
  direction     = "INGRESS"
  source_ranges = var.allowed_public_restricted_subnetworks
  priority = "1000"
  allow {
    protocol = "all"
  }
}

# private - allow ingress from within this network
resource "google_compute_firewall" "private_allow_all_network_inbound" {
  name = "bastion-private-allow-ingress"
  project = var.project
  network = var.network
  target_tags = ["private"]
  direction   = "INGRESS"
  source_ranges = [
    data.google_compute_subnetwork.public_subnetwork.ip_cidr_range,
    data.google_compute_subnetwork.public_subnetwork.secondary_ip_range[0].ip_cidr_range,
    data.google_compute_subnetwork.public_subnetwork.secondary_ip_range[1].ip_cidr_range,
    data.google_compute_subnetwork.private_subnetwork.ip_cidr_range,
    data.google_compute_subnetwork.private_subnetwork.secondary_ip_range[0].ip_cidr_range,
  ]
  priority = "1000"
  allow {
    protocol = "all"
  }
}

# private-persistence - allow ingress from `private` and `private-persistence` instances in this network
resource "google_compute_firewall" "private_allow_restricted_network_inbound" {
  name = "bastion-allow-restricted-inbound"
  project = var.project
  network = var.network
  target_tags = ["private-persistence"]
  direction   = "INGRESS"
  # source_tags is implicitly within this network; tags are only applied to instances that rest within the same network
  source_tags = ["private", "private-persistence"]
  priority = "1000"
  allow {
    protocol = "all"
  }
}
```

Add the following code in **network-firewall/variables.tf**.
```console
variable "network" {
  description = "A reference (self_link) to the VPC network to apply firewall rules to"
  type        = string
}

variable "public_subnetwork" {
  description = "A reference (self_link) to the public subnetwork of the network"
  type        = string
}

variable "allowed_public_restricted_subnetworks" {
  description = "The public networks that is allowed access to the public_restricted subnetwork of the network"
  default     = []
  type        = list(string)
}

variable "private_subnetwork" {
  description = "A reference (self_link) to the private subnetwork of the network"
  type        = string
}

variable "project" {
  description = "The project to create the firewall rules in. Must match the network project."
  type        = string
}
```

### Terraform Commands
To deploy the instances, we need to initialize Terraform, generate an execution plan and apply the execution plan to our cloud infrastructure. Follow this [documentation](/learning-paths/server-and-cloud/gcp/terraform#terraform-commands) to deploy the **main.tf** file.

### Verify the Instance and Bastion Host setup
In the Google Cloud console, go to the [VM instances page](https://console.cloud.google.com/compute/instances?_ga=2.159262650.1220602700.1668410849-523068185.1662463135). The instances we created through Terraform must be displayed on the screen.

![image](https://user-images.githubusercontent.com/67620689/222353051-483be628-6466-44f5-85b5-d7a7039b7dad.PNG)

### Use Jump Host to access the Private Instance
Connect to a target server via a Jump Host using the `-J` flag from the command line. This tells ssh to make a connection to the jump host and then establish a TCP forwarding to the target server, from there.
```console
  ssh -J username@jump-host-IP username@target-server-IP
```

![image](https://user-images.githubusercontent.com/67620689/222424103-1a3309c4-357d-4b23-964d-deb69e69376b.PNG)

**NOTE:-** Replace **jump-host-IP** with the external IP of the host, **target-server-IP** with the internal IP of the private instance and **username** with the IAM email address like abc@1234.com -> abc_1234_com


### Clean up resources
Run `terraform destroy` to delete all resources created.
```console
  terraform destroy
```

![image](https://user-images.githubusercontent.com/67620689/222353072-8d13897c-ebeb-4c4c-ad31-f65681b74dc6.PNG)
