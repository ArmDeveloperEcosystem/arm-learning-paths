---
# User change
title: "Install Redis on a single GCP Arm based instance"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Install Redis on a single GCP Arm based instance 

You can deploy Redis on Google Cloud using Terraform and Ansible. 

In this section, you will deploy Redis on a single Google Cloud instance.

If you are new to Terraform, you should look at [Automate GCP instance creation using Terraform](/learning-paths/servers-and-cloud-computing/gcp/terraform/) before starting this Learning Path.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path. 

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools. 

You will need a [Google Cloud account](https://console.cloud.google.com/?hl=en-au) to complete this Learning Path. Create an account if you don't have one.

Before you begin you will also need:
- Login to Google Cloud CLI 
- An SSH key pair

The instructions to login to Google Cloud CLI and to create the keys are below.

### Generate the SSH key-pair

Generate the SSH key-pair (public key, private key) using `ssh-keygen` to use for Arm VMs access. To generate the key-pair, follow this [guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

### Acquire GCP Access Credentials

The installation of Terraform on your Desktop/Laptop needs to communicate with GCP. Thus, Terraform needs to be authenticated.

To obtain GCP user credentials, follow this [guide](/install-guides/gcloud#acquire-user-credentials).

## Create a GCP instance using Terraform

Using a text editor, save the code below in a file called `main.tf`.

Scroll down to see the information you need to change in `main.tf`.
```console
provider "google" {
  project = "{project_id}"
  region  = "us-central1"
  zone    = "us-central1-a"
}

resource "google_compute_firewall" "rules" {
  project       = "{project_id}"
  name          = "my-firewall-rule"
  network       = "default"
  description   = "Open Redis connection port"
  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "tcp"
    ports    = ["6379"]
  }
}

resource "google_compute_instance" "vm_instance" {
  name         = "vm_name"
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

resource "local_file" "inventory" {
  depends_on = [google_compute_instance.vm_instance]
  filename   = "/tmp/inventory"
  content    = <<EOF
[all]
ansible-target1 ansible_connection=ssh ansible_host=${google_compute_instance.vm_instance.network_interface.0.access_config.0.nat_ip} ansible_user=ubuntu
                EOF
}
```
In the `provider` and `google_compute_firewall` sections, update the `project_id` with your value.

The inventory file is automatically generated and does not need to be changed.

## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the dependencies required for Google Cloud.

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

The public IP address will be different, but the output should be similar to:

```output
Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

Master_public_IP = [
  "34.68.176.131",
]
```

## Configure Redis through Ansible
Install the Redis and the required dependencies. 

You can use the same `playbook.yaml` file used in the section, [Install Redis on a single AWS Arm based instance](/learning-paths/servers-and-cloud-computing/redis/aws_deployment#configure-redis-through-ansible).

### Ansible Commands

Run the playbook using the  `ansible-playbook` command.

```console
ansible-playbook playbook.yaml -i /tmp/inventory
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [all] *****************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
The authenticity of host '34.68.176.131 (34.68.176.131)' can't be established.
ED25519 key fingerprint is SHA256:uWZgVeACoIxRDQ9TrqbpnjUz14x57jTca6iASH3gU7M.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [ansible-target1]

TASK [Update the Machine and install dependencies] *************************************************************************************************************
changed: [ansible-target1]

TASK [Create directories] **************************************************************************************************************************************
changed: [ansible-target1]

TASK [Create configuration files] ******************************************************************************************************************************
changed: [ansible-target1]

TASK [Stop redis-server] ***************************************************************************************************************************************
changed: [ansible-target1]

TASK [Start redis server with configuration files] *************************************************************************************************************
changed: [ansible-target1]

TASK [Set Authentication password] *****************************************************************************************************************************
changed: [ansible-target1]

PLAY RECAP *****************************************************************************************************************************************************
ansible-target1            : ok=7    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Connecting to the Redis server from local machine

Execute the steps below to connect to the remote Redis server from your local machine.
1. Install redis-tools to interact with redis-server.
```console
apt install redis-tools
```
2. Connect to redis-server through redis-cli.
```console
redis-cli -h <public-IP-address> -p 6379
```
The output will be:
```output
ubuntu@ip-172-31-38-39:~$ redis-cli -h 34.68.176.131 -p 6379
34.68.176.131:6379> 
```
3. Authorize Redis with the password set by us in playbook.yaml file.
```console
34.68.176.131:6379> ping
(error) NOAUTH Authentication required.
34.68.176.131:6379> AUTH 123456789
OK
34.68.176.131:6379> ping
PONG
```
4. Try out commands in the redis-cli.
```console
34.68.176.131:6379> set name test
OK
34.68.176.131:6379> get name
"test"
34.68.176.131:6379>
```
You have successfully installed Redis on a Google Cloud instance.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

Continue the Learning Path to deploy Redis on a Docker container.

