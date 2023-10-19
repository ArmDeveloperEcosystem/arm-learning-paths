---
title: Automate OCI VM instance creation using Terraform

weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This Learning Path uses Terraform to automate creation of Arm virtual machine instances on Oracle Cloud Infrastructure (OCI).

## Before you begin

You may want to review the Learning Path [Getting Started with Oracle OCI](/learning-paths/servers-and-cloud-computing/csp/oci/) before you begin.

Any computer which has the required tools installed can be used. The computer can be your desktop, laptop, or a virtual machine with the required tools. The command format assumes you are working on a Linux machine.

Refer to the [Terraform install guide](/install-guides/terraform/) for installation instructions.

You will need an [Oracle OCI account](https://cloud.oracle.com/) to complete this Learning Path. [Create an account](https://signup.oraclecloud.com/) and use Oracle Cloud Free Tier if you don’t already have an account.

## Acquire OCI access credentials

To deploy architectures, Terraform on your desktop or laptop communicates with OCI. For this to work, Terraform needs to be authenticated.

For authentication, you need to generate keys. These keys are used by Terraform to make programmatic calls to OCI.

To generate and configure the keys, follow the steps below.

Confirm Terraform is installed:

```console
terraform -v
```

The output will be similar to: 

```console
Terraform v1.5.5
on linux_arm64
```

Create a new directory to store the key files:

```console
mkdir $HOME/.oci
```

Generate a private key and adjust the permissions:

```console
openssl genrsa -out $HOME/.oci/rsa_private.pem 2048
chmod 600 $HOME/.oci/rsa_private.pem 
```

Generate a public key:

```console
openssl rsa -pubout -in $HOME/.oci/rsa_private.pem -out $HOME/.oci/rsa_public.pem 
```

Display the public key file:

```console
cd $HOME/.oci
cat rsa_public.pem
```

Copy the public key including the first and last lines including `----BEGIN PUBLIC KEY----` and `----END PUBLIC KEY---`

In the OCI web console, click on the Profile icon in the upper right corner and then click your profile on the drop down menu. 

Click `API Keys` on the left side of the page and then `ADD API Key`

Select `Paste a public key` as shown below and paste the contents of your public key in the box. Make sure to include the `----BEGIN PUBLIC KEY----` and `----END PUBLIC KEY---`

![alt-text #center](https://user-images.githubusercontent.com/89662128/250157622-288f0781-7707-4e6a-8a15-a389e453307b.jpg "Click paste a public key")

You have connected your keys with your OCI account.

## Prepare your Infrastructure as Code

Terraform provides the ability to share your code, with colleagues or publicly, without exposing any personal information. 

With Terraform you also have the flexibility to deploy the same infrastructure in different regions, compartments, and more. For this reason, you should create generic files to define the provider, the compartment, the domains and use a file containing the variable values used in the generic files.

You can share the template of the variables files, but be careful to share share your actual variable values. 

The first step is to create a directory for your code:

```console
mkdir ~/arm-on-oci
cd ~/arm-on-oci
```

### Terraform Provider

In this directory, use a text editor to create a file called `provider.tf` with the following information:

```console
provider "oci" {
  tenancy_ocid = var.tenancy_ocid
  region = var.region
  user_ocid = var.user_ocid
  fingerprint = var.fingerprint
  private_key_path = var.private_key_path
}
```

You will notice there isn't any real data in the file, just variables. You will be able
to share this file when you want to deploy on Oracle Cloud Infrastructure.

### Terraform Variables

You can create the file that will contain the values for the variables.

Start by creating the template file that will be shared with the code in case you want to publish your infrastructure or modules somewhere like GitHub.

The template file is called `terraform.tfvars.template`.

Use a text editor to create `terraform.tfvars.template` with the contents: 

```console
# Oracle Cloud Infrastructure Authentication
tenancy_ocid = "ocid1.tenancy.<REPLACE_ME>"
user_ocid = "ocid1.user.oc1..<REPLACE_ME>"
fingerprint= "<REPLACE_ME>"
private_key_path = "<REPLACE_ME>.pem"

# Region
region = "<REPLACE_ME>" # example: eu-frankfurt-1

# Compartment
compartment_ocid = "ocid1.compartment.<REPLACE_ME>"

# Keys Configuration
ssh_authorized_keys_path = "<REPLACE_ME>.pub"
ssh_private_key_path = "<REPLACE_ME>"
```

There is no confidential content in the file.

Copy the file to the file that should NOT be shared and will contain the values for the variables. The file is `terraform.tfvars`.

```console
cp terraform.tfvars.template terraform.tfvars
```

Use a text editor to replace each field with the values for your OCI account. You can find the Tenancy information OCID and the User information OCID in your account profile in the OCI console.

The private key is at `~/.oci/rsa_private.pem`

To get the key fingerprint for your private key run the `openssl` command:

```console
openssl rsa -pubout -outform DER -in ~/.oci/rsa_private.pem | openssl md5 -c
```

{{% notice Note %}}
Find your region using the [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm). For example, the region could be `us-ashburn-1`
{{% /notice %}}

The value for `ssh_authorized_keys_path` and `ssh_private_key_path` define the location of the ssh key you will use to connect to your instance using SSH.

For the `ubuntu` user name, it is:

```console
ssh_authorized_keys_path = "/home/ubuntu/.ssh/id_rsa.pub"
ssh_private_key_path = "/home/ubuntu/.ssh/id_rsa"
```

{{% notice Note %}}
If you don't have `id_rsa` and `id_rsa.pub` in your `~/.ssh` directory run 
`ssh-keygen` to generate a new key. Accept the default values when prompted and the files will be created. 
{{% /notice %}}

Terraform also requires variables to be defined in a dedicated file. 

Use a text editor to create `variables.tf` with the following contents:

```console
variable "tenancy_ocid" {
  description = "Tenancy's OCID"
}

variable "user_ocid" {
  description = "User's OCID"
  default = ""
}

variable "fingerprint" {
  description = "Key Fingerprint"
  default     = ""
}

variable "private_key_path" {
  description = "The private key path to pem."
  default     = ""
}

variable "region" {
  description = "OCI Region"
}

variable "compartment_ocid" {
  description = "Compartment's OCID where VCN will be created. "
}

variable "ssh_authorized_keys_path" {
  description = "Public SSH keys path to be included in the ~/.ssh/authorized_keys file for the default user on the instance."
  default     = ""
}

variable "ssh_private_key_path" {
  description = "The private key path to access instance."
  default     = ""
}
```

## Initialize Terraform

Initialize the Terraform directory: 

```console
terraform init
```

The output should be similar to:

```output

Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/oci...
- Installing hashicorp/oci v5.7.0...
- Installed hashicorp/oci v5.7.0 (signed by HashiCorp)

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

You now have a directory named `.terraform` that includes the plugins for the OCI provider.

## Testing the authentication

To test the setup, you can ask Terraform to do something.

To begin, ask Terraform to display all availability domains.

In the same directory, create a file `availability-domains.tf` with the following contents:

```console

# Source from https://registry.terraform.io/providers/oracle/oci/latest/docs/data-sources/identity_availability_domains

# Tenancy is the root or parent to all compartments or if you have 
# created one, you can use that one in the terraform.tfvars file.

data "oci_identity_availability_domains" "ads" {
  compartment_id = var.tenancy_ocid 
}

output "all-availability-domains-in-your-tenancy" {
  value = data.oci_identity_availability_domains.ads.availability_domains
}
```

{{% notice Note %}}
Make sure `provider.tf` and `availability-domains.tf` are in the same directory. Terraform processes all the files in a directory in the correct order.
{{% /notice %}}

### Terraform Plan

Run the `terraform plan` command to print the availability domains:

```console
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

You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure.
```

### Terraform Apply

Run the Terraform `apply` command to save the output values to the Terraform state:

```console
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

{{% notice Note %}}
After you run `apply` and you try to `plan` again, you won't see the output anymore. You can see it again if you run `terraform destroy` first.
{{% /notice %}}

## Create an Ampere compute instance

To create your first Arm compute instance, several other resources are required:

- a virtual cloud network (VCN)
- a subnet (public)
- an internet gateway (to access the Internet)
- a routing table (public)
- a security list (public)

You will notice the use of _public_. This mean that the resources have the possibility to be accessed from the public internet (they could have a public IP address assigned to them).

In OCI, some services are only available in a private subnet, those are not accessible directly from the internet (for example MySQL HeatWave Database Service).

### Network Resources

Start by defining all the resources listed above in a dedicated Terraform file named `network.tf`:

```console
data "oci_identity_availability_domains" "ad" {
  compartment_id = var.tenancy_ocid
}

resource "oci_core_virtual_network" "armvcn" {
  cidr_block = "10.0.0.0/16" 
  compartment_id = var.compartment_ocid
  display_name = "ampere_vcn"
  dns_label = "armvcn"
}

resource "oci_core_internet_gateway" "internet_gateway_for_arm" {
  compartment_id = var.compartment_ocid
  display_name = "internet_gateway_for_arm"
  vcn_id = oci_core_virtual_network.armvcn.id
}

resource "oci_core_route_table" "public_route_table" {
  compartment_id = var.compartment_ocid
  vcn_id = oci_core_virtual_network.armvcn.id
  display_name = "RouteTableForArmPublic"
  route_rules {
    destination = "0.0.0.0/0"
    network_entity_id = oci_core_internet_gateway.internet_gateway_for_arm.id
  }
}

resource "oci_core_security_list" "public_arm_security_list" {
  compartment_id = var.compartment_ocid
  display_name = "Allow Public SSH Connections to Ampere Compute Instance"
  vcn_id = oci_core_virtual_network.armvcn.id
  egress_security_rules {
    destination = "0.0.0.0/0"
    protocol = "6"
  }
  ingress_security_rules {
    tcp_options {
      max = 22
      min = 22
    }
    protocol = "6"
    source   = "0.0.0.0/0"
  }
}

resource "oci_core_subnet" "arm_public_subnet" {
  cidr_block = "10.0.0.0/24" 
  display_name = "arm_public_subnet"
  compartment_id = var.compartment_ocid
  vcn_id = oci_core_virtual_network.armvcn.id
  route_table_id =  oci_core_route_table.public_route_table.id 
  security_list_ids = [oci_core_security_list.public_arm_security_list.id]
  dns_label = "armpublic"
}
```

Run Terraform `plan` and `apply` to create the resources in in OCI:

```console
terraform plan ; terraform apply
```

Answer `yes` when prompted. 

The output confirms the added resources:

```output
...
Apply complete! Resources: 5 added, 0 changed, 0 destroyed.
```

The list of availability zones is printed as output. You can stop that from happening by deleting the file `availability-domains.tf`.

### Create an Arm (Ampere) compute instance

It's time to deploy your first Arm-based A1 compute instance.

Use a text editor to create a file named `compute.tf`:

<!--```bash { line_numbers="true", data_line_highlight="42" } -->
```bash {line_numbers="true", data_start="4", data_line="4-5,7"}
locals {
    ssh_key = file(var.ssh_authorized_keys_path)
}

data "oci_core_images" "images_for_shape" {
    compartment_id = var.compartment_ocid
    operating_system = "Oracle Linux"
    operating_system_version = "9"
    shape = "VM.Standard.A1.Flex"
    sort_by = "TIMECREATED"
    sort_order = "DESC"
}

resource "oci_core_instance" "Ampere" {
  compartment_id      = var.compartment_ocid
  display_name        = "Always Free Ampere Compute"
  availability_domain = data.oci_identity_availability_domains.ad.availability_domains[0].name
  fault_domain        = "FAULT-DOMAIN-1"
  shape = "VM.Standard.A1.Flex"

  dynamic "shape_config" {
    for_each = [1]
    content {
      memory_in_gbs = 16
      ocpus = 2 
    }
  }

  create_vnic_details {
    subnet_id        = oci_core_subnet.arm_public_subnet.id
    display_name     = "nic_arm_1"
    assign_public_ip =  true
    hostname_label   = "ampere1"
  }

  metadata = {
    ssh_authorized_keys = local.ssh_key
  }

  source_details {
    source_id   = data.oci_core_images.images_for_shape.images[0].id
    source_type = "image"
  }  

  timeouts {
    create = "10m"
  }

}
```

Run the `apply` command to deploy an Arm compute instance:

```console
terraform apply
```

The output shows 1 resource added:

```output
...
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Before connecting to your new compute instance, take a more detailed look at the file `compute.tf`:

__Lines 1 to 3__: define new local variables. In this section includes only one variable which holds the publish SSH key. 

__Lines 5 to 12__: specify an image compatible with the shape. 

To use an Always Free Ampere shape, use __`VM.Standard.A1.Flex`__.

As you can see, these lines list the compatible shapes using Oracle Linux 9
sorted by date (descending). This means that the first element of the list will be the
most recent image.

__Lines 14 to 49__: this is the definition of the compute instance.

__Lines 21 to 27__: define some specifications for the instance. With the __Flex__ shape, you need to specify the amount of memory and OCPUs.

__Lines 29 to 34__: create a Virtual Network Interface card to be connected to the public subnet.

__Lines 36 to 38__: specify the metadata for the compute instance, the public SSH key so you can connect using SSH. 

__Lines 40 to 43__: which image to use. Use the first one of the list (`[0]`).

__Lines 45 to 47__: specify the timeout for the instance creation.


### Output the IP address

Instead of using the OCI console to find the IP address, it's more convenient to display it directly using Terraform.

Use a text editor to create the file `outputs.tf`:

```console
output "public_ip" {
  value = oci_core_instance.Ampere.public_ip
}
``` 

Run `terraform refresh` to print the IP address:

```console
terraform refresh
```

```output
[...]
oci_core_instance.Ampere: Refreshing state... [id=ocid1.instance.oc1.iad.xxxxpgw2a]

Outputs:

public_ip = "1xx.xxx.xxx.x8"
```

## Connect using SSH

You can now connect to your new Ampere compute instance using SSH:

Substitute the printed IP address into the SSH command:

```console
ssh -i ~/.ssh/id_rsa opc@1xx.xxx.xxx.x8
```

You will log in as the user ocp as shown in the output below:

```output
The authenticity of host '1xx.xxx.xxx.x8 (1xx.xxx.xxx.x8)' can't be established.
ED25XXX key fingerprint is SHA256:wkFGCurGe+5AJtVmPIKCAqUKhw+xxxxxxxxxxxxxxxx.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '1xx.xxx.xxx.x8' (ED25XXX) to the list of known hosts.
[opc@ampere1 ~]$
```

Verify the Arm architecture using the `lscpu` command:

```console
lscpu 
```

Some output is omitted, but you should see `aarch64` as the architecture and `Neoverse-N1` as the CPU Model name:

```output
Architecture:           aarch64
  CPU op-mode(s):       32-bit, 64-bit
  Byte Order:           Little Endian
CPU(s):                 2
  On-line CPU(s) list:  0,1
Vendor ID:              ARM
  Model name:           Neoverse-N1
    Model:              1
    Thread(s) per core: 1
    Core(s) per socket: 2
    Socket(s):          1
    Stepping:           r3p1
    BogoMIPS:           50.00
    Flags:              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asim
                        drdm lrcpc dcpop asimddp ssbs
```

You have deployed your first Ampere Compute instance in OCI using Terraform.

To delete the resources run:

```console
terraform destroy
```