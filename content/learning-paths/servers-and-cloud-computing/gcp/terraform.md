---
# User change
title: "Automate virtual machine creation with Terraform"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Deploy an Arm based VM using Terraform

## Generate an SSH key pair

Generate an SSH key pair (public key, private key) using `ssh-keygen` to use for Arm VMs access. To generate the key pair, follow this [guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}


## Acquire GCP Access Credentials

The installation of Terraform on your Desktop/Laptop needs to communicate with GCP. Thus, Terraform needs to be authenticated.

To obtain GCP user credentials, follow this [guide](/install-guides/gcloud#acquire-user-credentials).

## Terraform infrastructure
Add resources required to create a VM in `main.tf`.

Add below code in `main.tf` file:

```console
provider "google" {
  project = "project_id"
  region  = "us-central1"
  zone    = "us-central1-a"
}

resource "google_compute_instance" "vm_instance" {
  name         = "instance-arm"
  machine_type = "c4a-standard-1"

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
```

{{% notice Note %}}
Replace `project_ID` with your value which can be found in the [Dashboard](https://console.cloud.google.com/home?_ga=2.56408877.721166205.1675053595-562732326.1671688536&_gac=1.125526520.1675155465.CjwKCAiAleOeBhBdEiwAfgmXfwdH3kCFBFeYzoKSuP1DzwJq7nY083_qzg7oyP2gwxMvaE0PaHVgFhoCmXoQAvD_BwE) of Google Cloud console.
{{% /notice %}}

## Terraform commands

### Initialize Terraform
Run `terraform init` to initialize the Terraform deployment. This command downloads all the modules required to manage your resources.

```
  terraform init
```

The output should be similar to:

```
Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/google...
- Reusing previous version of kreuzwerker/docker from the dependency lock file
- Installing hashicorp/google v4.61.0...
- Installed hashicorp/google v4.61.0 (signed by HashiCorp)
- Using previously-installed kreuzwerker/docker v2.23.1

Terraform has made some changes to the provider dependency selections recorded
in the .terraform.lock.hcl file. Review those changes and commit them to your
version control system if they represent changes you intended to make.

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
```
  terraform plan -out main.tfplan
```
A long output of resources to be created will be printed.


### Apply a Terraform execution plan
Run `terraform apply` to apply the execution plan to your cloud infrastructure. Below command creates all required infrastructure.

```
  terraform apply main.tfplan
```

Output should be similar to:

```output
google_compute_instance.vm_instance: Creating...
google_compute_instance.vm_instance: Still creating... [10s elapsed]
google_compute_instance.vm_instance: Creation complete after 14s [id=projects/massive-woods-383015/zones/us-central1-a/instances/instance-arm]


Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

### Verify created resource
In the Google Cloud console, go to the [VM instances page](https://console.cloud.google.com/compute/instances?_ga=2.159262650.1220602700.1668410849-523068185.1662463135). The VM created through Terraform must be displayed in the screen.

![terraform4 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/320b4c6f-0d2b-44f3-9517-dc427d82a018)

## SSH into the launched instance

Run following command to connect to VM through SSH:

```
  ssh ubuntu@<Public IP>
```

{{% notice Note %}}
Replace `<Public IP>` with the instance's IP.
{{% /notice %}}

Output should be similar to:

```output
The authenticity of host '34.91.147.54 (34.91.147.54)' can't be established.
ECDSA key fingerprint is SHA256:xwUGlczMr7M0ekr3g4axqREera7wUsCc1vEWpeENUAo.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '34.91.147.54' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.15.0-1030-gcp aarch64)
```

### Clean up resources

Run `terraform destroy` to delete all resources created.

```
  terraform destroy
```
