---
title: Automate OCI VM instance creation using Terraform

weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This Learning Path uses Terraform to automate creation of Arm virtual machine instances on the Oracle Cloud Infrastructure (OCI). 

## Before you begin 

You may want to review the Learning Path [Getting Started with Oracle OCI](/learning-paths/servers-and-cloud-computing/csp/oci/) before you begin.

Any computer which has the required tools installed can be used. The computer can be your desktop, laptop, or a virtual machine with the required tools.

Refer to the [Terraform install guide](/install-guides/terraform/) for instructions to install Terraform.

You will need an [Oracle OCI account](https://login.oci.oraclecloud.com/) to complete this Learning Path. Create an account if you don’t have one.

Before you begin, you will also need an SSH key pair. 

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

## Create Terraform scripts 

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
  tenancy_ocid = "<tenancy-ocid>"
  user_ocid = "<user-ocid>" 
  private_key_path = "<rsa-private-key-path>"
  fingerprint = "<fingerprint>"
  region = "<region-identifier>"
}
```

Replace each field with the values for your account. You can find these in your profile in the OCI console.

To get the key finger print for your private key run the `openssl` command:

```bash { target="ubuntu:latest" }
openssl rsa -pubout -outform DER -in ~/.oci/rsa_private.pem | openssl md5 -c
```

{{% notice Note %}}
Find your region using the [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm)
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

In the `tf-provider directory`, use a text editor to create a file named `outputs.tf` with the content below: 


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
- installing hashicorp/oci v5.3.0...
- installed hashicorp/oci v5.3.0 (signed by Hashicorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider selections it made above. include this file in your version control repository so that Terraform can guarantee to make the same selections by default when you run "terraform init" in the future.

╷
│ Warning: Additional provider information from registry
│ 
│ The remote registry returned warnings for registry.terraform.io/hashicorp/oci:
│ - For users on Terraform 0.13 or greater, this provider has moved to oracle/oci. Please update your source in
│ required_providers.
╵

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

You now have a folder named `.terraform`` that includes the plugins for the OCI provider.

### Terraform Plan

Run the Terraform plan command.

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

Run your Terraform scripts and get your outputs:

```bash { target="ubuntu:latest" }
terraform apply
```
When prompted for confirmation, enter yes, for your resource to be created.


After you run the apply command, the output is displayed in the terminal.

Example output:


```bash { target="ubuntu:latest" }
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


Congratulations! Your Oracle Cloud Infrastructure account can now authenticate your Oracle Cloud Infrastructure Terraform provider scripts.

# Question: Is a new compartment really needed? Can you use the default (root) compartment? 

## OCI COMPARTMENT ID

First, set up a directory for your Terraform scripts. Then add a provider script so your Oracle Cloud Infrastructure account can authenticate the scripts running from this directory.
In your $HOME directory, create a directory called tf-compartment and change to that directory.

```bash { target="ubuntu:latest" }
mkdir tf-compartment
```

```bash { target="ubuntu:latest" }
cd tf-compartment
```

Copy the provider.tf from earlier 

```bash { target="ubuntu:latest" }
cp ../tf-provider/provider.tf .
```


### Declare a Compartment resource 

Declare an Oracle Cloud Infrastructure compartment resource and then define the specifics for the compartment. 

Create a file called compartment.tf.

Replace the compartment_id with your tenancy-ocid, and name your compartment whatever you please.    

Copy the provider.tf from earlier 

```bash { target="ubuntu:latest" }

resource "oci_identity_compartment" "tf-compartment" {
    # Required
    compartment_id = "<tenancy-ocid>"
    description = "Compartment for Terraform resources."
    name = "<your-compartment-name>"
}
```


### Add Outputs

In the tf-compartment directory, create a file called outputs.tf. 

IMPORTANT: Ensure that outputs.tf, provider.tf, and compartment.tf are in the same directory.

Add the following code to outputs.tf.

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

Run your Terraform scripts. After, your account authenticates the scripts, Terraform creates a compartment in your tenancy.

Initialize a working directory in the tf-compartment directory.

```bash { target="ubuntu:latest" }
terraform init
```

Confirm that Terraform has been successfully initialized!

Example output:


```bash { target="ubuntu:latest" }
Initializing provider plugins...
- Finding latest version of hashicorp/oci...
- installing hashicorp/oci v5.3.0...
- installed hashicorp/oci v5.3.0 (signed by Hashicorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider selections it made above. include this file in your version control repository so that Terraform can guarantee to make the same selections by default when you run "terraform init" in the future.

╷
│ Warning: Additional provider information from registry
│ 
│ The remote registry returned warnings for registry.terraform.io/hashicorp/oci:
│ - For users on Terraform 0.13 or greater, this provider has moved to oracle/oci. Please update your source in
│ required_providers.

Terraform has been successfully initialized!
```

Create an execution plan to check the changes.

```bash { target="ubuntu:latest" }
terraform plan
```

Confirm that you have Plan: 1 to add, 0 to change, 0 to destroy.

Example output: 

```bash { target="ubuntu:latest" }
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



```bash { target="ubuntu:latest" }
terraform apply
```

Confirm Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Example Output:

```bash { target="ubuntu:latest" }
oci_identity_compartment.tf-compartment: Creating...
oci_identity_compartment.tf-compartment: Creation complete after 9s [id=xxx]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

compartment-OCID = ocid1.compartment.xxx
compartment-name = <your-compartment-name>
```

Congratulations! You have successfully logged in and created a compartment in your tenancy, using the Oracle Cloud Infrastructure Terraform provider.

## Create a Compute Instance

  Create SSH Encryption Keys 

  Run the command below to generate SSH Keys
```bash { target="ubuntu:latest" }
ssh-keygen -t rsa -N "" -b 2048 -C <your-ssh-key-name> -f <your-ssh-key-name>
```
The command generates some random text art used to generate the keys. When complete, you have two files:

The private key file: <your-ssh-key-name>
The public key file: <your-ssh-key-name>.pub

You use these files to connect to your compute instance.

### Create a Virtual Cloud Network (VCN)

1. To create a VCN you must open your OCI console and click the Oracle Cloud Icon to go to the main landing page. 

      Scroll down to Launch Resources.
      Select set up a network with a wizard.

2. In the Start VCN Wizard workflow, select VCN with Internet Connectivity and then click Start VCN Wizard .

3. Fill in basic information:

      VCN Name: your-vcn-name
     
      Compartment: your-compartment-name

4. In the Configure VCN and Subnets section, keep the default values for the CIDR blocks:

      VCN CIDR BLOCK: 10.0.0.0/16

      PUBLIC SUBNET CIDR BLOCK: 10.0.0.0/24

      PRIVATE SUBNET CIDR BLOCK: 10.0.1.0/24

5. For DNS Resolution, uncheck Use DNS hostnames in this VCN.

6. Click Next.

      The Create a VCN with Internet Connectivity configuration dialog is displayed (not shown here) confirming all the values you just entered.

7. Click Create to create your VCN.
      The Creating Resources dialog is displayed (not shown here) showing all VCN components being created.
    
8. Click View Virtual Cloud Network to view your new VCN.



### Required Information

1. Compartment Name: your-compartment-name
      Find your compartment name from the Create a Compartment tutorial you performed in the Before you Begin section.

2. Collect the following information from the Oracle Cloud Infrastructure Console.

      In the Console search bar, enter your-compartment-name.
  
      Click your-compartment-name in the search results.
      
      Copy the OCID.


      Subnet ID: <subnet-ocid>
      Open the navigation menu and click Networking, and then click Virtual Cloud Networks.

      Click <your-vcn-name> from section 2.

      Click the public subnet and copy OCID.

    
3. Find the source id for the image of the compute instance.
      Source ID: source-ocid

    In the Console's top navigation bar, find your region.

    Go to [Image Release Notes]([guide](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm)).

    Click Ubuntu 20.04 and click the latest image: Canonical-Ubuntu-20.04-aarch64-2023.06.30-0

    Find the image for your region and copy OCID

4. Choose the shape for the compute instance.
  
  Shape: VM.Standard.A1.Flex
    To choose a different ARM shape, go to [VM Standard Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#vmshapes__vm-standard).

5. Collect the following information from your environment.

    SSH Authorized Key (public key path): ssh-public-key-path

    From section 1, get the path to the SSH public key on your environment.

      You use this path when you set up the compute instance.


    Private SSH Key Path: ssh-private-key-path

      From the Create SSH Encryption Keys section, get the path to the SSH private key.
        
      You use this private key to connect to your compute instance.


## Add Authentication

First, set up a directory for your Terraform scripts. Then add a provider script so your Oracle Cloud Infrastructure account can authenticate the scripts running from this directory.

In your $HOME directory, create a directory called tf-compute and change to that directory.

```bash { target="ubuntu:latest" }
mkdir tf-compute
```
```bash { target="ubuntu:latest" }
cd tf-compute
```


Copy the provider.tf file from earlier, into the tf-compute directory.

```bash { target="ubuntu:latest" }
cp ../tf-provider/provider.tf .
```

Next fetch the name of an availability domain from your account. An availability domain is one of the required inputs to create a compute instance.

Copy the availability-domains.tf file from before, into the tf-compute directory.

```bash { target="ubuntu:latest" }
cp ../tf-provider/availability-domains.tf .
```

Example code:

```bash { target="ubuntu:latest" }
# Source from https://registry.terraform.io/providers/oracle/oci/latest/docs/data-sources/identity_availability_domains

data "oci_identity_availability_domains" "ads" {
  compartment_id = "<tenancy-ocid>"
}
```


In the tf-compute directory, create a file called outputs.tf.

To output the name of the first availability domain in the list of oci_identity_availability_domains, add the following code to outputs.tf.

```bash { target="ubuntu:latest" }

# The "name" of the availability domain to be used for the compute instance.
output "name-of-first-availability-domain" {
  value = data.oci_identity_availability_domains.ads.availability_domains[0].name
}
```

Run your scripts with Terraform:


```bash { target="ubuntu:latest" }
terraform init
```



```bash { target="ubuntu:latest" }
terraform plan
```


```bash { target="ubuntu:latest" }
terraform apply
```

Example output:


```bash { target="ubuntu:latest" }
name-of-first-availability-domain = QnsC:US-ASHBURN-AD-1
```

Declare an Oracle Cloud Infrastructure compute resource, and then define the specifics for the instance.

Create a file called compute.tf.

Add the following code to compute.tf

```bash { target="ubuntu:latest" }
resource "oci_core_instance" "ubuntu_instance" {
    # Required
    availability_domain = data.oci_identity_availability_domains.ads.availability_domains[0].name
    compartment_id = "<compartment-ocid>"
    shape = "VM.Standard2.1"
    source_details {
        source_id = "<source-ocid>"
        source_type = "image"
    }

    # Optional
    display_name = "<your-ubuntu-instance-name>"
    create_vnic_details {
        assign_public_ip = true
        subnet_id = "<subnet-ocid>"
    }
    metadata = {
        ssh_authorized_keys = file("<ssh-public-key-path>")
    } 
    preserve_boot_volume = false
}
```


## Add Outputs

Add output blocks to your code to get information about your compute instance after Terraform creates it.

Open the outputs.tf file.

Create an output block for the public IP of the instance:

The public IP is available after the instance is created.

You use the public IP to connect to the instance.

Add the following code to outputs.tf:

```bash { target="ubuntu:latest" }

# Outputs for compute instance

output "public-ip-for-compute-instance" {
  value = oci_core_instance.ubuntu_instance.public_ip
}
```

Add a few more outputs to describe the compute instance:
  
  display_name
  
  id
  
  region
  
  shape
  
  state
  
  ocpus
  
  memory_in_gbs
  
  time_created

  ```bash { target="ubuntu:latest" }

output "instance-name" {
  value = oci_core_instance.ubuntu_instance.display_name
}

output "instance-OCID" {
  value = oci_core_instance.ubuntu_instance.id
}

output "instance-region" {
  value = oci_core_instance.ubuntu_instance.region
}

output "instance-shape" {
  value = oci_core_instance.ubuntu_instance.shape
}

output "instance-state" {
  value = oci_core_instance.ubuntu_instance.state
}

output "instance-OCPUs" {
  value = oci_core_instance.ubuntu_instance.shape_config[0].ocpus
}

output "instance-memory-in-GBs" {
  value = oci_core_instance.ubuntu_instance.shape_config[0].memory_in_gbs
}

output "time-created" {
  value = oci_core_instance.ubuntu_instance.time_created
}
```

### Create an Instance 

Run your Terraform scripts. After, your account authenticates the scripts, Terraform creates a compute instance in a compartment in your tenancy. Use your SSH keys to connect to the instance. When you no longer need your instance, destroy it with Terraform.

```bash { target="ubuntu:latest" }
terraform init
```

```bash { target="ubuntu:latest" }
terraform plan
```


```bash { target="ubuntu:latest" }
terraform apply
```

When prompted for confirmation, enter yes, for your resource to be created.

After the instance is created, the outputs that you defined including your-public-ip-address are displayed in the output terminal.

### Connect to the instance 

From your terminal, enter the outputs for your compute instance:

```bash { target="ubuntu:latest" }
terraform output
```

Copy the public IP address from the outputs.

From your Linux machine, connect to your VM with this ssh command:

```bash { target="ubuntu:latest" }
ssh -i <ssh-private-key-path> ubuntu@<your-public-ip-address>
```

### Destroy the Instance 

After you no longer need your compute instance, you can terminate it with the following command:

```bash { target="ubuntu:latest" }
terraform destroy
```

When prompted for confirmation, enter yes, for your compute instance to be terminated.