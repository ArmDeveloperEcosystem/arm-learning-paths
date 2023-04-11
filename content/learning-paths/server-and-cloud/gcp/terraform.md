---
# User change
title: "Automate virtual machine creation with Terraform"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Deploy an Arm based VM using Terraform

## Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for Arm VMs access. To generate the key-pair, follow this [documentation](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Acquire GCP Access Credentials

The installation of Terraform on your Desktop/Laptop needs to communicate with GCP. Thus, Terraform needs to be authenticated.

To obtain GCP user credentials, follow this [documentation](/install-guides/gcp_login).

## Terraform infrastructure
Add resources required to create a VM in `main.tf`.

Add below code in `main.tf` file:

```
provider "google" {
  project = "project_id"
  region = "us-central1"
  zone = "us-central1-a"
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
```

## Terraform commands

### Initialize Terraform
Run `terraform init` to initialize the Terraform deployment. This command downloads all the modules required to manage your resources.

```
  terraform init
```

![image](https://user-images.githubusercontent.com/67620689/204243851-df54e9a3-8c9f-402d-9265-25cb035d14b1.PNG)

### Create a Terraform execution plan

Run `terraform plan` to create an execution plan.
```
  terraform plan -out main.tfplan
```
**Key points:**

* The **terraform plan** command is optional. We can directly run **terraform apply** command. But it is always better to check the resources about to be created.
* The terraform plan command creates an execution plan, but doesn't execute it. Instead, it determines what actions are necessary to create the configuration specified in your configuration files. This pattern allows you to verify whether the execution plan matches your expectations before making any changes to actual resources.
* The optional `-out` parameter allows you to specify an output file for the plan. Using the `-out` parameter ensures that the plan you reviewed is exactly what is applied.

### Apply a Terraform execution plan
Run `terraform apply` to apply the execution plan to your cloud infrastructure. Below command creates all required infrastructure.

```
  terraform apply main.tfplan
```
![image](https://user-images.githubusercontent.com/67620689/204243999-583c2187-b9d1-4b91-9349-fe48b8089d45.PNG)

### Verify created resource
In the Google Cloud console, go to the [VM instances page](https://console.cloud.google.com/compute/instances?_ga=2.159262650.1220602700.1668410849-523068185.1662463135). The VM we created through Terraform must be displayed in the screen.

![image](https://user-images.githubusercontent.com/67620689/204244210-00741212-de05-49f9-b4eb-e4943b809c70.PNG)

## SSH into the launched instance

Run following command to connect to VM through SSH:

```
  ssh ubuntu@<Public IP>
```
![image](https://user-images.githubusercontent.com/67620689/227440366-00847742-a431-4439-88fe-6b9147e9d042.PNG)

### Clean up resources

Run `terraform destroy` to delete all resources created.

```
  terraform destroy
```
![image](https://user-images.githubusercontent.com/67620689/204245617-e95de65d-0fad-4bf2-95c8-8816f03d9fc2.PNG)
