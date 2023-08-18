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

To be able to deploy architectures, Terraform installed on your desktop or laptop needs to communicate with OCI. To to this, Terraform needs to be authenticated.

For authentication, you need to generate access keys (access key ID and secret access key). These access keys are used by Terraform for making programmatic calls to OCI via the OCI CLI.

To generate and configure the Access key ID and Secret access key, follow the steps below:

Confirm Terraform is installed:

```bash { target="ubuntu:latest" }
terraform -v
```

The output will be similar to: 

```bash { target="ubuntu:latest" }
Terraform v1.5.4
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

## Prepare your Infrastructure as Code

The benefit of Terraform is to have the possibility to share your infrastructure's code
(with colleagues but also publicly).

You also have the possibility to deploy the same infrastructure on different region, compartment, ... For this reason, I'm in favor to create generic files to define the provider, the compartment, the domains and use a file containing the values of variables used in this generic files.

This also allows to not share any confidential information but just a template of the variables files.

The first step is to define a folder for our code:

```bash { target="ubuntu:latest" }
mkdir ~/arm-on-oci
cd ~/arm-on-oci
```

### Terraform Provider

In this directory, we create a new file called `provider.tf` with the following content:

```console
provider "oci" {
  tenancy_ocid = var.tenancy_ocid
  region = var.region
  user_ocid = var.user_ocid
  fingerprint = var.fingerprint
  private_key_path = var.private_key_path
}
```

You can notice that we don't insert any sensible data in that file. We will be able
to share this file for all our Terraform code we want to deploy on Oracle Cloud Infrastructure.

### Terraform Variables

We can now already create the file that will contain the value for all the variables.

We start by creating the template file that will be shared with the code in case we want to publish our infrastructure or modules somewhere like GitHub.

The template file is called `terraform.tfvars.template`.

For the moment, the content of the file should be like this:

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

Again on that file, there is no confidential content.

We copy the file to the file that should not be shared and will contain all the real values for these variables. The file is `terraform.tfvars`.

```bash { target="ubuntu:latest" }
cp terraform.tfvars.template terraform.tfvars
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

The value for `ssh_authorized_keys_path` and `ssh_private_key_path` define the location of the ssh key you will use to connect to your instance.

On my system, this is how it looks like: 

```console
ssh_authorized_keys_path = "/home/fred/.ssh/id_rsa_oci.pub"
ssh_private_key_path = "/home/fred/.ssh/id_rsa_oci"
```

{{% notice Note %}}
Use `ssh-keygen` to generate a new key if you don't have already a SSH key to use.
{{% /notice %}}

Terraform also requires variables to be defined in a dedicated file. We create `variables.tf` with the following content:

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

Use `terraform init` to run the scripts:

```bash { target="ubuntu:latest" }
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

You now have a folder named `.terraform` that includes the plugins for the OCI provider.

## Testing the authentication

To test that all information is correct, we need to ask Terraform to do something.

We will ask to Terraform to just display all availability domains.

In the same directory, we now create a file `availability-domains.tf` that as the following content:

```bash { target="ubuntu:latest" }

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

Run the Terraform `plan` command specifying the variables file:

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

You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure.
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

{{% notice Note %}}
If you use `apply` and you try to `plan` again, you won't see the output anymore. You could see it again if you `destroy` first.
{{% /notice %}}

## Create an Ampere compute instance

To create your first ARM compute instance, several other resources are required such as:

- a virtual cloud network (VCN)
- a subnet (public)
- an internet gateway (to access the Internet)
- a routing table (public)
- a security list (public)

You can notice that we use _public_. This mean that those resource have the possibility to be accessed from a public network such Internet, they could have a public IP assigned to them.

In OCI, some services are only available in a private subnet, those are not accessible directly from the Internet (for example MySQL HeatWave Database Service).

### Network Resources

We will start by defining all the resources listed above in a dedicated Terraform file: `network.tf`:

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

We can plan and apply those resources to OCI:

```bash { target="ubuntu:latest" }
$ terraform plan
$ terraform apply
...
Apply complete! Resources: 5 added, 0 changed, 0 destroyed.
```

The list of availability zones are still in the output. We can remove that by deleting the file `availability-domains.tf`.

### ARM Compute Instance (Ampere)

It's now time to deploy our first ARM Compute instance.

We start by creating a new file `compute.tf`:

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

And we can now apply our code to deploy our first ARM compute instance in OCI:

```bash
$ terraform apply
...
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Before we connect to our new compute instance, let's have a more detailed look at the file `compute.tf`:

__Lines 1 to 3__: define the new local variables. In our example we only have one in which we add the content of our public ssh key by reading the file:

__Lines 5 to 12__: we specify an image compatible with our shape. 

To use an Always Free Ampere shape, we use __`VM.Standard.A1.Flex`__.

As you can see, these lines will list all the compatible shapes using Oracle Linux 9
sorted by date descending. This mean that the first element of the list will be the
most recent image.

__Lines 14 to 49__: this is the definition of the compute instance.

__Lines 21 to 27__: here we define some specifications for our instance. As we use a __Flex__ shape, we need to specify the amount of memory and OCPUs.

__Lines 29 to 34__: we create a Virtual Network Interface Card to be connected to the public subnet we created.

__Lines 36 to 38__: we specify the metadata for the compute instance. Here we only specify our public ssh key we can use to later connect to it.

__Lines 40 to 43__: we tell which image to use. As you can see we use the first one of the list (`[0]`).

__Lines 45 to 47__: we just specify the timeout for the creation.


### Outputs

You may have noticed, that our compute instance has been deployed, but to know it's IP address, we need to use OCI Console.

It's much more convenient to display the information direclty via Terraform when we deploy it.

Let's create the file `outputs.tf`:

```bash
output "public_ip" {
  value = oci_core_instance.Ampere.public_ip
}
``` 

We can now run `terraform refresh`:

```bash
$ terraform refresh
[...]
oci_core_instance.Ampere: Refreshing state... [id=ocid1.instance.oc1.iad.xxxxpgw2a]

Outputs:

public_ip = "1xx.xxx.xxx.x8"
```

## Connection

Now it's time to finally connect to our new Ampere compute instance on OCI using SSH:

```bash
$ ssh -i /home/fred/.ssh/id_rsa_oci opc@1xx.xxx.xxx.x8
The authenticity of host '1xx.xxx.xxx.x8 (1xx.xxx.xxx.x8)' can't be established.
ED25XXX key fingerprint is SHA256:wkFGCurGe+5AJtVmPIKCAqUKhw+xxxxxxxxxxxxxxxx.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '1xx.xxx.xxx.x8' (ED25XXX) to the list of known hosts.
[opc@ampere1 ~]$
```

We can verify the architecture:

```bash
[opc@ampere1 ~]$ lscpu 
Architecture:           aarch64
  CPU op-mode(s):       32-bit, 64-bit
  Byte Order:           Little Endian
CPU(s):                 2
  On-line CPU(s) list:  0,1
[...]  
```

Done ! You have deployed your first Ampere Compute instance in OCI using Terraform, congrats !