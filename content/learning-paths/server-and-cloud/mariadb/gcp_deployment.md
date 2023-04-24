---
# User change
title: "Install MariaDB on a GCP Arm based instance"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Install MariaDB on a GCP Arm based instance 

You can deploy MariaDB on Google Cloud using Terraform and Ansible. 

In this topic, you will deploy MariaDB on a single Google Cloud instance.

If you are new to Terraform, you should look at [Automate GCP instance creation using Terraform](/learning-paths/server-and-cloud/gcp/terraform/) before starting this Learning Path.

## Before you begin

Any computer which has [Terraform](/install-guides/terraform/), [Ansible](/install-guides/ansible/), and the [Google Cloud CLI](/install-guides/gcloud/) installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine.

You will need an [Google Cloud account](https://console.cloud.google.com/?hl=en-au) to complete this Learning Path. Create an account if you don't have one.

Before you begin you will also need:
- Login to Google Cloud CLI 
- An SSH key pair

The instructions to login to Google Cloud CLI and to create the keys are below.

### Acquire GCP Access Credentials

Terraform on your local machine needs to communicate with GCP.

To obtain GCP user credentials, follow the [Google Cloud Credentials](/install-guides/gcp_login) install guide.

### Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for Arm VMs access. To generate the key-pair, follow this [
documentation](/install-guides/ssh#ssh-keys).

{{% notice Note %}} 
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Create a GCP instance using Terraform

1. Use a text editor to add the contents below to a new file named `main.tf`

```terraform
// instance creation
provider "google" {
  project = "{project_id}"
  region = "us-central1"
  zone = "us-central1-a"
}
resource "google_compute_firewall" "rules" {
  project     = "{project_id}"
  name        = "my-firewall-rule"
  network     = "default"
  description = "Open SSH connection port"
  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "icmp"
  }

  allow {
    protocol  = "tcp"
    ports     = ["22", "3306"]
  }
}
resource "google_compute_instance" "vm_instance" {
  name         = "vmname"
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
output "Master_public_IP" {
  value = [google_compute_instance.vm_instance.network_interface.0.access_config.0.nat_ip]
}
// Generate inventory file
resource "local_file" "inventory" {
    depends_on=[google_compute_instance.vm_instance]
    filename = "/tmp/inventory"
    content = <<EOF
[all]
ansible-target1 ansible_connection=ssh ansible_host=${google_compute_instance.vm_instance.network_interface.0.access_config.0.nat_ip} ansible_user=ubuntu
                EOF
}
```

2. Update `main.tf` with your values

In the `provider` and `google_compute_firewall` sections, update the `project_id` with your value.

The inventory file is automatically generated and does not need to be changed.

## Terraform Commands

Use Terraform to deploy MariaDB on GCP.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. 

This command downloads the dependencies required for Google Cloud.

```bash
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

```bash
terraform plan
```

A long output of resources to be created will be printed. 

### Apply a Terraform execution plan

1. Run `terraform apply` to apply the execution plan and create all GCP resources. 

```bash
terraform apply
```      

2. Answer `yes` to the prompt to confirm you want to create GCP resources. 

The public IP address will be different, but the output should be similar to:

```output
Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

Master_public_IP = [
  "34.67.224.55",
]
```

## Configure MariaDB through Ansible

You can install the MariaDB and the required dependencies using Ansible.

You can use the same `playbook.yaml` file used in the topic, [Install MariaDB on an AWS Arm based instance](/learning-paths/server-and-cloud/mariadb/ec2_deployment#configure-mariadb-through-ansible).

Use a text editor to save the `playbook.yaml` file if you don't already have it. 

### Ansible Commands

Run the playbook using the  `ansible-playbook` command:

```bash
ansible-playbook playbook.yaml -i /tmp/inventory 
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [all] ******************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
The authenticity of host '34.67.224.55 (34.67.224.55)' can't be established.
ED25519 key fingerprint is SHA256:XC9CnqxdGvrGCyo19WtfBsnUyFJU8hCoIDKWxiNaAVc.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [ansible-target1]

TASK [Update the Machine and Install dependencies] **************************************************************************************
changed: [ansible-target1]

TASK [start and enable maridb service] **************************************************************************************************
ok: [ansible-target1]

TASK [Change Root Password] *************************************************************************************************************
changed: [ansible-target1]

TASK [Create database user with password and all database privileges and 'WITH GRANT OPTION'] *******************************************
changed: [ansible-target1]

TASK [MariaDB secure installation] ******************************************************************************************************
changed: [ansible-target1]

TASK [Enable remote login by changing bind-address] *************************************************************************************
changed: [ansible-target1]

RUNNING HANDLER [Restart mariadb] *******************************************************************************************************
changed: [ansible-target1]

PLAY RECAP ******************************************************************************************************************************
ansible-target1            : ok=8    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Connect to Database from local machine

Follow the instructions from the previous section to [connect to the database](/learning-paths/server-and-cloud/mariadb/ec2_deployment#connect-to-database-from-local-machine).

You have successfully deploy MariaDB on a Google Cloud instance.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```bash
terraform destroy
```

