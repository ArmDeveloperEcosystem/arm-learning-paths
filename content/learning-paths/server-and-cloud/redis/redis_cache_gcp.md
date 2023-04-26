---
# User change
title: "Deploy Redis as a cache for MySQL on a GCP Arm based Instance"

weight: 10 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy Redis as a cache for MySQL on a GCP Arm based Instance

You can deploy Redis as a cache for MySQL on Google Cloud using Terraform and Ansible. 

In this section, you will deploy Redis as a cache for MySQL on a Google Cloud instance.

If you are new to Terraform, you should look at [Automate GCP instance creation using Terraform](/learning-paths/server-and-cloud/gcp/terraform/) before starting this Learning Path.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path. 

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools. 

You will need a [Google Cloud account](https://console.cloud.google.com/?hl=en-au) to complete this Learning Path. Create an account if you don't have one.

Before you begin you will also need:
- Login to the Google Cloud CLI 
- An SSH key pair

The instructions to login to the Google Cloud CLI and create the keys are below.

### Acquire GCP Access Credentials

The installation of Terraform on your Desktop/Laptop needs to communicate with GCP. Thus, Terraform needs to be authenticated.

To obtain GCP user credentials, follow this [guide](/install-guides/gcp_login).

### Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for GCP instance access. To generate the key-pair, follow this [
guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}} 
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Create GCP instances using Terraform

Using a text editor, save the code below in a file called `main.tf`. Here you are creating 2 instances.
    
```console
provider "google" {
  project = "{project_id}"
  region = "us-central1"
  zone = "us-central1-a"
}

resource "google_compute_instance" "MYSQL_TEST" {
  name         = "mysqltest-${count.index+1}"
  count        = "2"
  machine_type = "t2a-standard-1"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts-arm64"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral public IP
    }
  }
  metadata = {
     ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }  
}

resource "google_compute_firewall" "rules" {
  project     = "{project_id}"
  name        = "my-firewall-rule"
  network     = "default"
  description = "Open ssh connection and mysql port"
  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "icmp"
  }

  allow {
    protocol  = "tcp"
    ports     = ["22", "3306"]
  }
}

resource "google_compute_network" "default" {
  name = "test-network1"
}
resource "local_file" "inventory" {
    depends_on=[google_compute_instance.MYSQL_TEST]
    filename = "/tmp/inventory"
    content = <<EOF
[mysql1]
${google_compute_instance.MYSQL_TEST[0].network_interface.0.access_config.0.nat_ip}
[mysql2]
${google_compute_instance.MYSQL_TEST[1].network_interface.0.access_config.0.nat_ip}
[all:vars]
ansible_connection=ssh
ansible_user=ubuntu
                EOF
}
```
In the `provider` and `google_compute_firewall` sections, update the `project_id` with your value.

The inventory file is automatically generated and does not need to be changed.

## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the dependencies required for GCP.

```console
terraform init
```
    
The output should be similar to:

```output
Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/google...
- Finding latest version of hashicorp/local...
- Installing hashicorp/google v4.57.0...
- Installed hashicorp/google v4.57.0 (signed by HashiCorp)
- Installing hashicorp/local v2.4.0...
- Installed hashicorp/local v2.4.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

```

### Create a Terraform execution plan

Run `terraform plan` to create an execution plan.

```console
terraform plan
```

A long output of resources to be created will be printed. 

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan and create all GCP resources. 

```console
terraform apply
```      

Answer `yes` to the prompt to confirm you want to create GCP resources. 

The output should be similar to:

```output
Apply complete! Resources: 5 added, 0 changed, 0 destroyed.

```

## Configure MySQL through Ansible

Install MySQL and the required dependencies on both the instances. 

You can use the same `playbook.yaml` file used in the section, [Deploy Redis as a cache for MySQL on an AWS Arm based Instance](/learning-paths/server-and-cloud/redis/redis_cache_aws#configure-mysql-through-ansible).

### Ansible Commands

Run the playbook using the `ansible-playbook` command:

```console
ansible-playbook playbook.yaml -i /tmp/inventory
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [mysql1, mysql2] ********************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
The authenticity of host '34.28.237.71 (34.28.237.71)' can't be established.
ED25519 key fingerprint is SHA256:xOr4xr3TvaRdPxX4QlxhYpjf9mykgmhAtWElxkhqK3w.
This key is not known by any other names
The authenticity of host '35.222.119.249 (35.222.119.249)' can't be established.
ED25519 key fingerprint is SHA256:gHsDuIJ9IVFrOeeYUZXMEvFOu5tXL0ZB78aHwZjooTI.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
yes
ok: [34.28.237.71]
ok: [35.222.119.249]

TASK [Update the Machine and Install dependencies] ***************************************************************************************************************
changed: [35.222.119.249]
changed: [34.28.237.71]

TASK [start and enable mysql service] ****************************************************************************************************************************
ok: [34.28.237.71]
ok: [35.222.119.249]

TASK [Change Root Password] **************************************************************************************************************************************
changed: [34.28.237.71]
changed: [35.222.119.249]

TASK [Create database user with password and all database privileges and 'WITH GRANT OPTION'] ********************************************************************
changed: [34.28.237.71]
changed: [35.222.119.249]

TASK [Create a new database with name 'arm_test1'] ***************************************************************************************************************
skipping: [35.222.119.249]
changed: [34.28.237.71]

TASK [Create a new database with name 'arm_test2'] ***************************************************************************************************************
skipping: [34.28.237.71]
changed: [35.222.119.249]

TASK [MySQL secure installation] *********************************************************************************************************************************
changed: [35.222.119.249]
changed: [34.28.237.71]

TASK [Enable remote login by changing bind-address] **************************************************************************************************************
changed: [34.28.237.71]
changed: [35.222.119.249]

RUNNING HANDLER [Restart mysql] **********************************************************************************************************************************
changed: [35.222.119.249]
changed: [34.28.237.71]

PLAY RECAP *******************************************************************************************************************************************************
34.28.237.71               : ok=9    changed=7    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
35.222.119.249             : ok=9    changed=7    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

## Connect to Database from local machine

Follow the instructions given in this [documentation](/learning-paths/server-and-cloud/redis/redis_cache_aws#connect-to-database-from-local-machine) to connect to the database from local machine.

## Deploy Redis as a cache for MySQL using Python

Follow the instructions given in this [documentation](/learning-paths/server-and-cloud/redis/redis_cache_aws#deploy-redis-as-a-cache-for-mysql-using-python) to deploy Redis as a cache for MySQL using Python.

You have successfully deployed Redis as a cache for MySQL on a Google Cloud Arm based Instance.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

