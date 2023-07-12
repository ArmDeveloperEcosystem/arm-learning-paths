---
title: Automate OCI instance creation using Terraform

weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This Learning Path uses [Terraform Cloud](https://registry.terraform.io/) to automate creation of Arm instances. Reader may wish to also see:
* [Getting Started with Oracle OCI](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/oci/)

## Before you begin 
You should have the prerequisite tools installed before starting the Learning Path.

Any computer which has the required tools installed can be used for this section. The computer can be your desktop, laptop, or a virtual machine with the required tools.

You will need an [Oracle OCI account](https://login.oci.oraclecloud.com/) to complete this Learning Path. Create an account if you don’t have one.

Before you begin, you will also need:

- Login to the OCI CLI
- An SSH key pair 

The instructions to login to the OCI CLI and create these keys are below.

### Generate an SSH key-pair

Generate the SSH key-pair (public key, private key) using `ssh-keygen` to use for OCI access. To generate the key-pair, follow this [guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}



### Acquire OCI Access Credentials

The installation of Terraform on your desktop or laptop needs to communicate with OCI. Thus, Terraform needs to be authenticated.

For authentication, generate access keys (access key ID and secret access key). These access keys are used by Terraform for making programmatic calls to OCI via the OCI CLI.

To generate and configure the Access key ID and Secret access key, follow the steps below: 

First Check if Terraform is installed.

```bash { target="ubuntu:latest" }
terraform -v
```


example output:

```bash { target="ubuntu:latest" }
Terraform v1.5.2
on linux_arm64
```


if terraform is not installed follow this [guide](https://learn.arm.com/install-guides/terraform/)

Now that you have confirmed Terraform is installed we will now configure terraform with OCI. 

```bash { target="ubuntu:latest" }
mkdir $HOME/.oci
```

You must generate a private key in PEM format and configure the API key with Oracle. follow the steps below to do so: 
```bash { target="ubuntu:latest" }
openssl genrsa -out $HOME/.oci/rsa_private.pem 2048
```
This makes it so only you can read and write to the key
```bash { target="ubuntu:latest" }
chmod 600 $HOME/.oci/rsa_private.pem 
```

Generate the public key:
This makes it so only you can read and write to the key
```bash { target="ubuntu:latest" }
openssl rsa -pubout -in $HOME/.oci/rsa_private.pem -out $HOME/.oci/rsa_public.pem 
```

open the file:
```bash { target="ubuntu:latest" }
cd $HOME/.oci
ls -lta 
```

Copy the public key including the ----BEGIN PUBLIC KEY---- and ----END PUBLIC KEY---:
```bash { target="ubuntu:latest" }
cat rsa_public.pem
```

Example output: 

```bash { target="ubuntu:latest" }
dr.xxxxx.   2 opc opc   51 May  4 01:30 .
-rw-rw-r--. 1 opc opc  451 May  4 01:30 rsa_public.pem
-rw-------. 1 opc opc 1629 May  4 01:30 rsa_private.pem
drwx------. 5 opc opc 145  May  4 01:29 .. 
opc @terraform-test.oci $ cat rsa_public.pem
-----BEGIN PUBLIC KEY------
# Your key here
-----END PUBLIC KEY-------
```



Now you add your public key to your user account in the OCI web console:

![alt-text #center](https://user-images.githubusercontent.com/89662128/250157622-288f0781-7707-4e6a-8a15-a389e453307b.jpg "Click paste a public key")

Now you have connected your RSA keys to your OCI account.



## Create Scripts 

For this section you need you API key for terraform authentication.

First, set up a directory for Terraform scripts. Then add a provider script so your OCI account can authenticate the scripts running from this directory.


In <your-home-directory>, create a directory called tf-provider and change to that directory.
```bash { target="ubuntu:latest" }
mkdir tf-provider
cd tf-provider
```

Create a file called "provider.tf"

Add the following code to provider.tf:

Replace the fields with brackets, with information from the Gather Required Information section.
Add quotations around string values.

```bash { target="ubuntu:latest" }
provider "oci" {
  tenancy_ocid = "<tenancy-ocid>"
  user_ocid = "<user-ocid>" 
  private_key_path = "<rsa-private-key-path>"
  fingerprint = "<fingerprint>"
  region = "<region-identifier>"
}
```
Tip: you can find all the values needed in your profile. use this article to find your region: [guide](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm)


### Add a Data Source

In this section, you fetch a list of the availability domains in your tenancy. By fetching data, you confirm that your OCI account authenticates your provider.tf script and you get information from your account.


In the tf-provider directory, create a file called availability-domains.tf

```bash { target="ubuntu:latest" }
# Source from https://registry.terraform.io/providers/oracle/oci/latest/docs/data-sources/identity_availability_domains

# Tenancy is the root or parent to all compartments.
# For this tutorial, use the value of <tenancy-ocid> for the compartment OCID.

data "oci_identity_availability_domains" "ads" {
  compartment_id = "<tenancy-ocid>"
}
```

##### IMPORTANT
Ensure provider.tf and availability-domains.tf are in the same directory. Terraform processes all the files in a directory in the correct order, based on their relationship. For a modular approach and future reuse, separate the provider file from other scripts.


### Add Outputs

The data source oci_identity_availability_domains, fetches a list of availability domains. In this section, you declare an output block to print the fetched information.

In the tf-provider directory, create a file called outputs.tf

Add the following code to outputs.tf


```bash { target="ubuntu:latest" }
# Output the "list" of all availability domains.
output "all-availability-domains-in-your-tenancy" {
  value = data.oci_identity_availability_domains.ads.availability_domains
}
```

##### IMPORTANT
Ensure outputs.tf, provider.tf, and availability-domains.tf are in the same directory.


## Run Scripts

Run your Terraform scripts. After your account authenticates the scripts, Terraform fetches your tenancy's availability domains.

```bash { target="ubuntu:latest" }
    terraform init
```

Example output:

```bash { target="ubuntu:latest" }
    ubuntu@gubay-oracle-test:~/tf-provider$ terraform init

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
```




Check the contents of the tf-provider directory: 

```bash { target="ubuntu:latest" }
    ls -a
```

You now have a folder called .terraform that includes the plugins for the oci provider.

### Plan

Run the Terraform plan command.

```bash { target="ubuntu:latest" }
    terraform plan
```

Confirm that you have Plan: 0 to add, 0 to change, 0 to destroy.

Example output:


```bash { target="ubuntu:latest" }
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


### Apply

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


### Declare a Compartment rescource 

Declare an Oracle Cloud Infrastructure compartment resource and then define the specifics for the compartment. 

Create a file called compartment.tf.

Replace the compartment_id with your tenency-ocid, and name your compartment whatever you please.    

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











