---
# User change
title: "Deploy Memcached as a cache for Postgres on a Google Cloud Arm based Instance"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy Memcached as a cache for Postgres on a Google Cloud Arm based Instance

You can deploy Memcached as a cache for Postgres on Google Cloud using Terraform and Ansible. 

In this section, you will deploy Memcached as a cache for Postgres on a Google Cloud instance.

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

Using a text editor, save the code below in a file called `main.tf`. Here we are creating 2 instances.

```console
provider "google" {
  project = "{project_id}"
  region = "us-central1"
  zone = "us-central1-a"
}

resource "google_compute_instance" "PSQL_TEST" {
  name         = "psqltest-${count.index+1}"
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
  description = "Open ssh connection and psql port"
  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "icmp"
  }

  allow {
    protocol  = "tcp"
    ports     = ["22", "5432"]
  }
}

resource "google_compute_network" "default" {
  name = "test-network1"
}
resource "local_file" "inventory" {
    depends_on=[google_compute_instance.PSQL_TEST]
    filename = "/tmp/inventory"
    content = <<EOF
[db_master]
${google_compute_instance.PSQL_TEST[0].network_interface.0.access_config.0.nat_ip}
${google_compute_instance.PSQL_TEST[1].network_interface.0.access_config.0.nat_ip}
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

## Configure Postgres through Ansible

Install Postgres and the required dependencies on both the instances. 

You can use the same `playbook.yaml` file used in the section, [Deploy Memcached as a cache for Postgres on an AWS Arm based Instance](/learning-paths/server-and-cloud/memcached/memcached_psql_aws#configure-postgres-through-ansible).

### Ansible Commands

Run the playbook using the `ansible-playbook` command:

```console
ansible-playbook playbook.yaml -i /tmp/inventory
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [all] *****************************************************************************************************************************************************
TASK [Gathering Facts] *****************************************************************************************************************************************
The authenticity of host '34.123.220.201 (34.123.220.201)' can't be established.
ED25519 key fingerprint is SHA256:uovagzUgma1rzZ5k4vLu2XytOB7c8zxmqwaZnCCc1fo.
This key is not known by any other names
The authenticity of host '34.66.63.213 (34.66.63.213)' can't be established.
ED25519 key fingerprint is SHA256:QjI0vHnjqAI8ySD4JOzwnH6akD+UBpmHZiS0DV6xf7Q.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
yes
ok: [34.123.220.201]
ok: [34.66.63.213]
TASK [Update the Machine & Install PostgreSQL] *****************************************************************************************************************
changed: [34.123.220.201]
changed: [34.66.63.213]
TASK [Update apt repo and cache on all Debian/Ubuntu boxes] ****************************************************************************************************
changed: [34.66.63.213]
changed: [34.123.220.201]
TASK [Install PostgreSQL packages] *****************************************************************************************************************************
changed: [34.66.63.213]
changed: [34.123.220.201]
TASK [Install Python pip] **************************************************************************************************************************************
changed: [34.66.63.213] => (item=python3-pip)
changed: [34.123.220.201] => (item=python3-pip)
TASK [Start and enable services] *******************************************************************************************************************************
ok: [34.66.63.213] => (item=postgresql)
ok: [34.123.220.201] => (item=postgresql)
TASK [Utility present] *****************************************************************************************************************************************
changed: [34.66.63.213]
changed: [34.123.220.201]
TASK [Replace postgresql configuration file to allow remote connection] ****************************************************************************************
changed: [34.66.63.213] => (item=listen_addresses = '*')
[WARNING]: Module remote_tmp /var/lib/postgresql/.ansible/tmp did not exist and was created with a mode of 0700, this may cause issues when running as another
user. To avoid this, create the remote_tmp dir with the correct permissions manually
changed: [34.123.220.201] => (item=listen_addresses = '*')
TASK [Allow trust connection for the db user] ******************************************************************************************************************
changed: [34.66.63.213]
changed: [34.123.220.201]
RUNNING HANDLER [restart postgres] *****************************************************************************************************************************
changed: [34.66.63.213]
changed: [34.123.220.201]
PLAY RECAP *****************************************************************************************************************************************************
34.123.220.201             : ok=10   changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
34.66.63.213               : ok=10   changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Connect to Database from local machine

Follow the instructions given in this [documentation](/learning-paths/server-and-cloud/memcached/memcached_psql_aws#connect-to-database-from-local-machine) to connect to the database from local machine.

## Deploy Memcached as a cache for Postgres using Python

Follow the instructions given in this [documentation](/learning-paths/server-and-cloud/memcached/memcached_psql_aws#deploy-memcached-as-a-cache-for-postgres-using-python) to deploy Memcached as a cache for PostgreSQL using Python.

You have successfully deployed Memcached as a cache for PostgreSQL on a Google Cloud Arm based Instance.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```
