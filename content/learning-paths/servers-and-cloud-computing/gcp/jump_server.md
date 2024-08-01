---
# User change
title: "Deploy Arm instances on GCP and provide access via Jump Server"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Infrastructure automation for other Learning Paths

Some learning paths may require one or more server nodes to complete. The Terraform files shown here can be used as a platform to work on those learning paths. The intent is for you to modify these as needed to support other learning path activities.

## Deploy Arm instances on GCP and provide access via Jump Server

### Introduction to Jump Server
A Jump Server (also known as a bastion host) is an intermediary device responsible for funneling traffic through firewalls using a supervised secure channel. By creating a barrier between networks, jump servers create an added layer of security against outsiders wanting to maliciously access sensitive company data. Only those with the right credentials can log into a jump server and obtain authorization to proceed to a different security zone.

{{% notice Note %}}
An alternative to setting up a Jump server like below is to use [IAP](https://cloud.google.com/compute/docs/connect/ssh-using-iap).
{{% /notice %}}

### Generate an SSH key pair

Generate an SSH key pair (public key, private key) using `ssh-keygen`. To generate the key pair, follow this [guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

### Acquire GCP Access Credentials

The installation of Terraform on your Desktop/Laptop needs to communicate with GCP. Thus, Terraform needs to be authenticated.

To obtain GCP user credentials, follow this [guide](/install-guides/gcloud/#acquire-user-credentials). 

### Deploying Arm instances on GCP and providing access via Jump Server
For deploying Arm instances on GCP and providing access via Jump Server, the Terraform configuration is broken into 4 files: `main.tf`, `outputs.tf`, `variables.tf`, `terraform.tfvars`, and a modules directory that contains `vpc-network` and `network-firewall` directories.

Add the following code in `main.tf`. It creates an instance with OS Login configured to use as a bastion host and a private instance to use alongside the bastion host.
```console
terraform {
  required_version = ">= 0.12.26"
}

# Create a Management Network for shared services
module "management_network" {
  source  = "./modules/vpc-network"
  project = var.project
  region  = var.region
}

# Add public key to IAM user
data "google_client_openid_userinfo" "me" {}
resource "google_os_login_ssh_public_key" "cache" {
  project = var.project
  user    = data.google_client_openid_userinfo.me.email
  key     = file("~/.ssh/id_rsa.pub")
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
  machine_type = "c4a-standard-1"
  zone         = var.zone
  tags         = ["public"]
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
  project                   = var.project
  name                      = "bastion-private"
  machine_type              = "c4a-standard-1"
  zone                      = var.zone
  allow_stopping_for_update = true
  tags                      = ["private"]
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

Add the following code in `outputs.tf`. It defines the output values for this configuration.
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

Create a `variables.tf` describing the variables referenced in the other files with their type and a default value.
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

{{% notice Note %}}
Replace `project_ID` with your value which can be found in the [Dashboard](https://console.cloud.google.com/home?_ga=2.56408877.721166205.1675053595-562732326.1671688536&_gac=1.125526520.1675155465.CjwKCAiAleOeBhBdEiwAfgmXfwdH3kCFBFeYzoKSuP1DzwJq7nY083_qzg7oyP2gwxMvaE0PaHVgFhoCmXoQAvD_BwE) of Google Cloud console. The [region and zone](https://cloud.google.com/compute/docs/regions-zones#available) are selected depending on the machine type.
{{% /notice %}}

Now create a `modules` directory and inside it create a `network-firewall` and `vpc-network` directories.

```bash
mkdir -p modules/network-firewall
mkdir -p modules/vpc-network
```

Add the following code in `vpc-network/main.tf`.
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
  name    = "bastion-router"
  project = var.project
  region  = var.region
  network = google_compute_network.vpc.self_link
}

# Public Subnetwork Config
resource "google_compute_subnetwork" "vpc_subnetwork_public" {
  name                     = "bastion-subnetwork-public"
  project                  = var.project
  region                   = var.region
  network                  = google_compute_network.vpc.self_link
  private_ip_google_access = true
  ip_cidr_range            = cidrsubnet(var.cidr_block, var.cidr_subnetwork_width_delta, 0)
  secondary_ip_range {
    range_name    = "public-cluster"
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
  name                   = "bastion-nat"
  project                = var.project
  region                 = var.region
  router                 = google_compute_router.vpc_router.name
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
  name                     = "bastion-subnetwork-private"
  project                  = var.project
  region                   = var.region
  network                  = google_compute_network.vpc.self_link
  private_ip_google_access = true
  ip_cidr_range            = cidrsubnet(var.cidr_block, var.cidr_subnetwork_width_delta, 1 * (1 + var.cidr_subnetwork_spacing))
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
  source                                = "../network-firewall"
  project                               = var.project
  network                               = google_compute_network.vpc.self_link
  allowed_public_restricted_subnetworks = var.allowed_public_restricted_subnetworks
  public_subnetwork                     = google_compute_subnetwork.vpc_subnetwork_public.self_link
  private_subnetwork                    = google_compute_subnetwork.vpc_subnetwork_private.self_link
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

Add the following code in `network-firewall/main.tf`.
```console
data "google_compute_subnetwork" "public_subnetwork" {
  self_link = var.public_subnetwork
}

data "google_compute_subnetwork" "private_subnetwork" {
  self_link = var.private_subnetwork
}

# public - allow ingress from anywhere
resource "google_compute_firewall" "public_allow_all_inbound" {
  name          = "bastion-public-allow-ingress"
  project       = var.project
  network       = var.network
  target_tags   = ["public"]
  direction     = "INGRESS"
  source_ranges = ["0.0.0.0/0"]
  priority      = "1000"
  allow {
    protocol = "all"
  }
}

# public - allow ingress from specific sources
resource "google_compute_firewall" "public_restricted_allow_inbound" {
  count         = length(var.allowed_public_restricted_subnetworks) > 0 ? 1 : 0
  name          = "bastion-public-restricted-allow-ingress"
  project       = var.project
  network       = var.network
  target_tags   = ["public-restricted"]
  direction     = "INGRESS"
  source_ranges = var.allowed_public_restricted_subnetworks
  priority      = "1000"
  allow {
    protocol = "all"
  }
}

# private - allow ingress from within this network
resource "google_compute_firewall" "private_allow_all_network_inbound" {
  name        = "bastion-private-allow-ingress"
  project     = var.project
  network     = var.network
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
  name        = "bastion-allow-restricted-inbound"
  project     = var.project
  network     = var.network
  target_tags = ["private-persistence"]
  direction   = "INGRESS"
  # source_tags is implicitly within this network; tags are only applied to instances that rest within the same network
  source_tags = ["private", "private-persistence"]
  priority    = "1000"
  allow {
    protocol = "all"
  }
}
```

Add the following code in `network-firewall/variables.tf`.
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
To deploy the instances, you need to initialize Terraform, generate an execution plan and apply the execution plan to your cloud infrastructure. Follow this [documentation](/learning-paths/servers-and-cloud-computing/gcp/terraform#terraform-commands) to deploy the `main.tf` file.

### Verify the Instance and Bastion Host setup
In the Google Cloud console, go to the [VM instances page](https://console.cloud.google.com/compute/instances?_ga=2.159262650.1220602700.1668410849-523068185.1662463135). The instances you created through Terraform must be displayed on the screen.

![gcp_jump #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/47ebebb4-678d-464d-b85e-e6bcc3d8c0f1)

### Use Jump Host to access the Private Instance
Connect to a target server via a Jump Host using the `-J` flag from the command line. This tells SSH to make a connection to the jump host and then establish a TCP forwarding to the target server, from there.
```console
  ssh -J username@jump-host-IP username@target-server-IP
```

Output should be similar to:

```output
The authenticity of host '34.90.184.41 (34.90.184.41)' can't be established.
ECDSA key fingerprint is SHA256:6kCBV5W8ZlXSbxGbFjWVVcKqeMQAYmY1F4VWXhlEKI0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '34.90.184.41' (ECDSA) to the list of known hosts.
The authenticity of host '10.0.16.2 (<no hostip for proxy command>)' can't be established.
ECDSA key fingerprint is SHA256:fwAf7+hlpO4CiUxpAZ38VF+hbWoZAFatQ3mZB/ddltc.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.0.16.2' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.15.0-1030-gcp aarch64)
```

{{% notice Note %}}
Replace `jump-host-IP` with the external IP of the bastion host, `target-server-IP` with the internal IP of the private instance and **username** with the IAM email address like abc@1234.com -> abc_1234_com
{{% /notice %}}


### Clean up resources
Run `terraform destroy` to delete all resources created.
```console
  terraform destroy
```
