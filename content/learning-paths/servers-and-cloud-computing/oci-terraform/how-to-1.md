---
title: Automate OCI VM instance creation using Terraform

weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This Learning Path uses Terraform to automate creation of Arm virtual machine instances on the Oracle Cloud Infrastructure (OCI). 

## Before you begin 

You may want to review the Learning Path [Getting Started with Oracle OCI](/learning-paths/servers-and-cloud-computing/csp/oci/) before you begin.

Any computer which has the required tools installed can be used. The computer can be your desktop, laptop, or a virtual machine with the required tools. The command format assumes you are working on a Linux machine.

Refer to the [Terraform install guide](/install-guides/terraform/) for instructions to install Terraform.

You will need an [Oracle OCI account](https://cloud.oracle.com/) to complete this Learning Path. [Create an account](https://signup.oraclecloud.com/) and use Oracle Cloud Free Tier if you don’t have an account yet.

## Acquire OCI Access Credentials

The installation of Terraform on your desktop or laptop needs to communicate with OCI. To to this, Terraform needs to be authenticated.

For authentication, generate access keys (access key ID and secret access key). These access keys are used by Terraform for making programmatic calls to OCI via the OCI CLI.

To generate and configure the Access key ID and Secret access key, follow the steps below: 

Confirm Terraform is installed:

```bash { target="ubuntu:latest" }
terraform -v
```

The output will be similar to: 

```bash { target="ubuntu:latest" }
Terraform v1.5.3
on linux_arm64
```

Start configuration by creating a new directory for OCI:

```bash { target="ubuntu:latest" }
mkdir $HOME/.oci
```

Generate a private key in PEM format and adjust the permissions:

```bash { target="ubuntu:latest" }
openssl genrsa -out $HOME/.oci/rsa_private.pem 2048
chmod 600 $HOME/.oci/rsa_private.pem 
```

Generate a public key:

```bash { target="ubuntu:latest" }
openssl rsa -pubout -in $HOME/.oci/rsa_private.pem -out $HOME/.oci/rsa_public.pem 
```

Display the public key file:

```bash { target="ubuntu:latest" }
cd $HOME/.oci
cat rsa_public.pem
```

Copy the public key including the `----BEGIN PUBLIC KEY----` and `----END PUBLIC KEY---`

In the OCI web console, click on the Profile icon in the upper right corner and then click your profile on the drop down menu. 

Click `API Keys` on the left side of the page and then `ADD API Key`

Select `Paste a public key` as shown below and paste the contents of your public key in the box. Make sure to include the `----BEGIN PUBLIC KEY----` and `----END PUBLIC KEY---`

![alt-text #center](https://user-images.githubusercontent.com/89662128/250157622-288f0781-7707-4e6a-8a15-a389e453307b.jpg "Click paste a public key")

Now you have connected your RSA keys to your OCI account.

## Setup Terraform authentication 

Create a directory for the Terraform scripts. 

In your home directory, create a directory called tf-provider and change to that directory.

```bash { target="ubuntu:latest" }
mkdir $HOME/tf-provider
cd $HOME/tf-provider
```

Use a text editor to create a new file named `provider.tf`

Add the code below to `provider.tf` and save the file:

```console
provider "oci" {
# Variables.
variable "tenancy_ocid"         { type = string }
variable "user_ocid"            { type = string }
variable "private_key_path"     { type = string }
variable "fingerprint"          { type = string }
variable "region"               { type = string }
variable "root_compartment_id"  { type = string }


# Resources
provider "oci" {
  tenancy_ocid     = var.tenancy_ocid
  user_ocid        = var.user_ocid
  private_key_path = var.private_key_path
  fingerprint      = var.fingerprint
  region           = var.region
}
}
```

Replace each field with the values for your account. You can find the Tenancy information OCID and the User information OCID in your account profile in the OCI console.

The private key is at `$HOME/.oci/rsa_private.pem`

To get the key finger print for your private key run the `openssl` command:

```bash { target="ubuntu:latest" }
openssl rsa -pubout -outform DER -in ~/.oci/rsa_private.pem | openssl md5 -c
```

{{% notice Note %}}
Find your region using the [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm). For example, the region could be `us-ashburn-1`
{{% /notice %}}


### Add a data source

In the same `tf-provider` directory use a text editor to create a file named `availability-domains.tf`:

```bash { target="ubuntu:latest" }

# Source from https://registry.terraform.io/providers/oracle/oci/latest/docs/data-sources/identity_availability_domains

# Tenancy is the root or parent to all compartments.
# For this tutorial, use the value of <tenancy-ocid> for the compartment OCID.

data "oci_identity_availability_domains" "ads" {
  compartment_id = "<tenancy-ocid>"
}
```

Modify the `<tenancy-ocid>` value to be your tenancy OCID from your profile. 

{{% notice Note %}}
Make sure `provider.tf` and `availability-domains.tf` are in the same directory. Terraform processes all the files in a directory in the correct order.
{{% /notice %}}

### Add outputs

The data source `oci_identity_availability_domains` fetches a list of availability domains. In this section, you declare an output block to print the fetched information.

In the same directory, use a text editor to create a file named `outputs.tf` with the content below: 


```bash { target="ubuntu:latest" }
# Output the "list" of all availability domains.
output "all-availability-domains-in-your-tenancy" {
  value = data.oci_identity_availability_domains.ads.availability_domains
}
```

## Initialize Terraform 

Use `terraform init` to run the scripts: 

```bash { target="ubuntu:latest" }
terraform init
```

The output should be similar to: 

```output

Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/oci...
- Installing hashicorp/oci v5.6.0...
- Installed hashicorp/oci v5.6.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

╷
│ Warning: Additional provider information from registry
│
│ The remote registry returned warnings for registry.terraform.io/hashicorp/oci:
│ - For users on Terraform 0.13 or greater, this provider has moved to oracle/oci. Please update your source in required_providers.
╵

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

You now have a folder named `.terraform` that includes the plugins for the OCI provider.

### Terraform Plan

Run the Terraform `plan` command:

```bash { target="ubuntu:latest" }
terraform plan
```

The output will be similar to:

```output
   Changes to Outputs:
  + all-availability-domains-in-your-tenancy = [
      + {
          + compartment_id = "ocid1.tenancy.oc1..xxx"
          + id             = "ocid1.availabilitydomain.xxx"
          + name           = "QnsC:US-ASHBURN-AD-1"
        },
      + {
          + compartment_id = "ocid1.tenancy.oc1..xxx"
          + id             = "ocid1.availabilitydomain.xxx"
          + name           = "QnsC:US-ASHBURN-AD-2"
        },
      + {
          + compartment_id = "ocid1.tenancy.oc1..xxx"
          + id             = "ocid1.availabilitydomain.xxx"
          + name           = "QnsC:US-ASHBURN-AD-3"
        },
    ]

You can apply this plan to save these new output values to the Terraform state, without changing any real
infrastructure.
```

### Terraform Apply

Run the Terraform `apply` command to generate the outputs:

```bash { target="ubuntu:latest" }
terraform apply
```

When prompted for confirmation, enter `yes` for your resource to be created.

After you run the apply command, the output is displayed in the terminal.

The output will be similar to:

```output
    Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

all-availability-domains-in-your-tenancy = tolist([
  {
    "compartment_id" = "ocid1.tenancy.xxx"
    "id" = "ocid1.availabilitydomain.xxx"
    "name" = "QnsC:US-ASHBURN-AD-1"
  },
  {
    "compartment_id" = "ocid1.tenancy.xxx"
    "id" = "ocid1.availabilitydomain.xxx"
    "name" = "QnsC:US-ASHBURN-AD-2"
  },
  {
    "compartment_id" = "ocid1.tenancy.xxx"
    "id" = "ocid1.availabilitydomain.xxx"
    "name" = "QnsC:US-ASHBURN-AD-3"
  },
])
```

Your Oracle Cloud Infrastructure account is now authenticated using your Terraform provider scripts.

## Create an OCI Compartment

A compartment is a logical grouping of resources in OCI. Compartments organize your resources and help with access control. Compartments are found in the Identity area of OCI. 

To create a new compartment using Terraform, create a new directory for your Terraform scripts:

```bash { target="ubuntu:latest" }
mkdir $HOME/tf-compartment
cd $HOME/tf-compartment
```

Copy the provider.tf from the previous section: 

```bash { target="ubuntu:latest" }
cp ../tf-provider/provider.tf .
```

### Declare a Compartment resource 

Declare a compartment resource and then define the specifics for the compartment. 

Use a text editor to create a new file called `compartment.tf`

Replace the compartment_id with your Tenancy OCID (used in previous section), and pick a name and description for your compartment.

```bash { target="ubuntu:latest" }
resource "oci_identity_compartment" "tf-compartment" {
    # Required
    compartment_id = "<tenancy-ocid>"
    description = "Compartment for Terraform resources."
    name = "<your-compartment-name>"
}
```

### Add Outputs

In the same directory, use a text editor to create a file named `outputs.tf`.

Add the following code to `outputs.tf`: 

```bash { target="ubuntu:latest" }

# Outputs for compartment

output "compartment-name" {
  value = oci_identity_compartment.tf-compartment.name
}

output "compartment-OCID" {
  value = oci_identity_compartment.tf-compartment.id
}
```
 
 ## Create a Compartment 

Use the Terraform `init` command to run the scripts: 

```bash { target="ubuntu:latest" }
terraform init
```

The output will be similar to:

```bash { target="ubuntu:latest" }

Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/oci...
- Installing hashicorp/oci v5.6.0...
- Installed hashicorp/oci v5.6.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

╷
│ Warning: Additional provider information from registry
│
│ The remote registry returned warnings for registry.terraform.io/hashicorp/oci:
│ - For users on Terraform 0.13 or greater, this provider has moved to oracle/oci. Please update your source in required_providers.
╵

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

You now have a folder named `.terraform` that includes the plugins for the OCI provider.

Run the Terraform `plan` command to the resources that will be created:

```bash { target="ubuntu:latest" }
terraform plan
```

Confirm that you have 1 resource to add: 

Plan: 1 to add, 0 to change, 0 to destroy.

The output is similar to:

```output
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
  + create

Terraform will perform the following actions:

  # oci_identity_compartment.tf-compartment will be created
  + resource "oci_identity_compartment" "tf-compartment" {
      + compartment_id = "ocid1.tenancy.xxx"
      + defined_tags   = (known after apply)
      + description    = "Compartment for Terraform resources."
      + freeform_tags  = (known after apply)
      + id             = (known after apply)
      + inactive_state = (known after apply)
      + is_accessible  = (known after apply)
      + name           = "<your-compartment-name>"
      + state          = (known after apply)
      + time_created   = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + compartment-OCID = (known after apply)
  + compartment-name = "<your-compartment-name>"
```

Use the Terraform `apply` command to create the compartment:

```bash { target="ubuntu:latest" }
terraform apply
```

When prompted for confirmation, enter `yes` for your resource to be created.

The output is similar to:

```output
oci_identity_compartment.tf-compartment: Creating...
oci_identity_compartment.tf-compartment: Creation complete after 9s [id=xxx]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

compartment-OCID = ocid1.compartment.xxx
compartment-name = <your-compartment-name>
```

You have successfully created an OCI compartment using Terraform. You can see the new compartment in the OCI console in the Identity area. You can also search for `compartment` in the console.

## Create a compute instance

Create a new directory titled oci_compute and copy over the files from tf-provider

```bash { target="ubuntu:latest" }
mkdir oci_compute
```

Create a file called "oci_compute.tf" with the following contents. You may edit the [compute shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm) to the desired ARM processor

```bash { target="ubuntu:latest" }
# Variables 
variable "compartment_id"              { type = string }
variable "compute_name"                { type = string }
variable "compute_subnet_id"           { type = string }
variable "compute_image_id"            { type = string }
variable "compute_ssh_authorized_keys" { type = string }

variable "compute_shape" {
  type    = string
  default = "VM.Standard.A1.Flex"
}

variable "compute_cpus" {
  type    = string
  default = "1"
}

variable "compute_memory_in_gbs" {
  type    = string
  default = "1"
}


# Resources
data "oci_identity_availability_domains" "ads" {
  compartment_id = var.compartment_id
}

resource "oci_core_instance" "tf_compute" {
  # Required
  availability_domain = data.oci_identity_availability_domains.ads.availability_domains[0].name
  compartment_id      = var.compartment_id
  shape               = var.compute_shape

  source_details {
    source_id         = var.compute_image_id
    source_type       = "image"
  }

  # Optional
  display_name        = var.compute_name

  shape_config {
    ocpus         = var.compute_cpus
    memory_in_gbs = var.compute_memory_in_gbs
  }

  create_vnic_details {
    subnet_id         = var.compute_subnet_id
    assign_public_ip  = true
  }

  metadata = {
    ssh_authorized_keys = file(var.compute_ssh_authorized_keys)
  } 

  preserve_boot_volume = false
}


# Outputs
output "compute_id" {
  value = oci_core_instance.tf_compute.id
}

output "db_state" {
  value = oci_core_instance.tf_compute.state
}

output "compute_public_ip" {
  value = oci_core_instance.tf_compute.public_ip
}
```

Next run the commands below to create your infrastructure:

```bash { target="ubuntu:latest" }
terraform init
```

Use the terraform plan command to test the execution plan.

```bash { target="ubuntu:latest" }
terraform plan
```

Example output:

```output
resource "oci_core_instance" "tf_compute" {
      + availability_domain                 = "oVQK:UK-LONDON-1-AD-1"
      + boot_volume_id                      = (known after apply)
      + compartment_id                      = "ocid1.compartment.oc1..aaaaaaaa.."
      + dedicated_vm_host_id                = (known after apply)
      + defined_tags                        = (known after apply)
      + display_name                        = "obvm2"
      + fault_domain                        = (known after apply)
      + freeform_tags                       = (known after apply)
      + hostname_label                      = (known after apply)
      + id                                  = (known after apply)
      + image                               = (known after apply)
      + ipxe_script                         = (known after apply)
      + is_pv_encryption_in_transit_enabled = (known after apply)
      + launch_mode                         = (known after apply)
      + metadata                            = {
          + "ssh_authorized_keys" = <<-EOT
                ssh-rsa AAAAB3Nza...nElEbgK/ username@machine-name
            EOT
        }
      + preserve_boot_volume                = false
      + private_ip                          = (known after apply)
      + public_ip                           = (known after apply)
      + region                              = (known after apply)
      + shape                               = "VM.Standard.E2.1.Micro"
      + state                               = (known after apply)
      + subnet_id                           = (known after apply)
      + system_tags                         = (known after apply)
      + time_created                        = (known after apply)
      + time_maintenance_reboot_due         = (known after apply)

      + agent_config {
          + are_all_plugins_disabled = (known after apply)
          + is_management_disabled   = (known after apply)
          + is_monitoring_disabled   = (known after apply)

          + plugins_config {
              + desired_state = (known after apply)
              + name          = (known after apply)
            }
        }

      + availability_config {
          + recovery_action = (known after apply)
        }

      + create_vnic_details {
          + assign_public_ip       = "true"
          + defined_tags           = (known after apply)
          + display_name           = (known after apply)
          + freeform_tags          = (known after apply)
          + hostname_label         = (known after apply)
          + private_ip             = (known after apply)
          + skip_source_dest_check = (known after apply)
          + subnet_id              = "ocid1.subnet.oc1.uk-london-1.aaaaaaaa..."
          + vlan_id                = (known after apply)
        }

      + instance_options {
          + are_legacy_imds_endpoints_disabled = (known after apply)
        }

      + launch_options {
          + boot_volume_type                    = (known after apply)
          + firmware                            = (known after apply)
          + is_consistent_volume_naming_enabled = (known after apply)
          + is_pv_encryption_in_transit_enabled = (known after apply)
          + network_type                        = (known after apply)
          + remote_data_volume_type             = (known after apply)
        }

      + platform_config {
          + numa_nodes_per_socket = (known after apply)
          + type                  = (known after apply)
        }

      + shape_config {
          + gpu_description               = (known after apply)
          + gpus                          = (known after apply)
          + local_disk_description        = (known after apply)
          + local_disks                   = (known after apply)
          + local_disks_total_size_in_gbs = (known after apply)
          + max_vnic_attachments          = (known after apply)
          + memory_in_gbs                 = 1
          + networking_bandwidth_in_gbps  = (known after apply)
          + ocpus                         = 1
          + processor_description         = (known after apply)
        }

      + source_details {
          + boot_volume_size_in_gbs = (known after apply)
          + kms_key_id              = (known after apply)
          + source_id               = "ocid1.image.oc1.uk-london-1.aaaaaaaa..."
          + source_type             = "image"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + compute_id        = (known after apply)
  + compute_public_ip = (known after apply)
  + db_state          = (known after apply)
```



Use the terraform apply command to create the OCI compute instance.


```bash { target="ubuntu:latest" }
terraform apply
```

Example output:

```output
esource "oci_core_instance" "tf_compute" {
      + availability_domain                 = "oVQK:UK-LONDON-1-AD-1"
      + boot_volume_id                      = (known after apply)
      + compartment_id                      = "ocid1.compartment.oc1..aaaaaaaa..."
      + dedicated_vm_host_id                = (known after apply)
      + defined_tags                        = (known after apply)
      + display_name                        = "obvm2"
      + fault_domain                        = (known after apply)
      + freeform_tags                       = (known after apply)
      + hostname_label                      = (known after apply)
      + id                                  = (known after apply)
      + image                               = (known after apply)
      + ipxe_script                         = (known after apply)
      + is_pv_encryption_in_transit_enabled = (known after apply)
      + launch_mode                         = (known after apply)
      + metadata                            = {
          + "ssh_authorized_keys" = <<-EOT
                ssh-rsa AAAAB3Nza...nElEbgK/ username@machine-name
            EOT
        }
      + preserve_boot_volume                = false
      + private_ip                          = (known after apply)
      + public_ip                           = (known after apply)
      + region                              = (known after apply)
      + shape                               = "VM.Standard.E2.1.Micro"
      + state                               = (known after apply)
      + subnet_id                           = (known after apply)
      + system_tags                         = (known after apply)
      + time_created                        = (known after apply)
      + time_maintenance_reboot_due         = (known after apply)

      + agent_config {
          + are_all_plugins_disabled = (known after apply)
          + is_management_disabled   = (known after apply)
          + is_monitoring_disabled   = (known after apply)

          + plugins_config {
              + desired_state = (known after apply)
              + name          = (known after apply)
            }
        }

      + availability_config {
          + recovery_action = (known after apply)
        }

      + create_vnic_details {
          + assign_public_ip       = "true"
          + defined_tags           = (known after apply)
          + display_name           = (known after apply)
          + freeform_tags          = (known after apply)
          + hostname_label         = (known after apply)
          + private_ip             = (known after apply)
          + skip_source_dest_check = (known after apply)
          + subnet_id              = "ocid1.subnet.oc1.uk-london-1.aaaaaaaa..."
          + vlan_id                = (known after apply)
        }

      + instance_options {
          + are_legacy_imds_endpoints_disabled = (known after apply)
        }

      + launch_options {
          + boot_volume_type                    = (known after apply)
          + firmware                            = (known after apply)
          + is_consistent_volume_naming_enabled = (known after apply)
          + is_pv_encryption_in_transit_enabled = (known after apply)
          + network_type                        = (known after apply)
          + remote_data_volume_type             = (known after apply)
        }

      + platform_config {
          + numa_nodes_per_socket = (known after apply)
          + type                  = (known after apply)
        }

      + shape_config {
          + gpu_description               = (known after apply)
          + gpus                          = (known after apply)
          + local_disk_description        = (known after apply)
          + local_disks                   = (known after apply)
          + local_disks_total_size_in_gbs = (known after apply)
          + max_vnic_attachments          = (known after apply)
          + memory_in_gbs                 = 1
          + networking_bandwidth_in_gbps  = (known after apply)
          + ocpus                         = 1
          + processor_description         = (known after apply)
        }

      + source_details {
          + boot_volume_size_in_gbs = (known after apply)
          + kms_key_id              = (known after apply)
          + source_id               = "ocid1.image.oc1.uk-london-1.aaaaaaaa..."
          + source_type             = "image"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + compute_id        = (known after apply)
  + compute_public_ip = (known after apply)
  + db_state          = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

oci_core_instance.tf_compute: Creating...
oci_core_instance.tf_compute: Still creating... [10s elapsed]
oci_core_instance.tf_compute: Still creating... [20s elapsed]
oci_core_instance.tf_compute: Still creating... [30s elapsed]
oci_core_instance.tf_compute: Still creating... [40s elapsed]
oci_core_instance.tf_compute: Still creating... [50s elapsed]
oci_core_instance.tf_compute: Still creating... [1m0s elapsed]
oci_core_instance.tf_compute: Still creating... [1m10s elapsed]
oci_core_instance.tf_compute: Still creating... [1m20s elapsed]
oci_core_instance.tf_compute: Still creating... [1m30s elapsed]
oci_core_instance.tf_compute: Creation complete after 1m37s [id=ocid1.instance.oc1.uk-london-1.anwgiljt...]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

compute_id = "ocid1.instance.oc1.uk-london-1.anwgiljt..."
compute_public_ip = "XXX.XXX.XX.XX"
db_state = "RUNNING"
```




