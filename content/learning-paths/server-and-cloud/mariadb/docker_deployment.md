---
# User change
title: "Deploy MariaDB via Docker"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Install MariaDB in a Docker container 

You can deploy MariaDB in a Docker container using Terraform and Ansible. 

## Before you begin

The required tools for this section are the same as the previous section, You will need a computer which has [Terraform](/install-guides/terraform/), [Ansible](/install-guides/ansible/), and the [AWS CLI](/install-guides/aws-cli/) installed.

You an use the same SSH key pair.

## Create an AWS EC2 instance using Terraform

You can use the same Terraform file used in the topic, [Install MariaDB on an AWS Arm based instance](/learning-paths/server-and-cloud/mariadb/ec2_deployment#deploy-ec2-instance-via-terraform).

## Terraform Commands

Use a text editor to copy and save `main.tf`. If you already have it from the last topic you can use the same file. 

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the dependencies required for AWS.

```bash
terraform init
```
    
The output should be similar to:

```output
Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/local...
- Finding latest version of hashicorp/aws...
- Installing hashicorp/local v2.4.0...
- Installed hashicorp/local v2.4.0 (signed by HashiCorp)
- Installing hashicorp/aws v4.58.0...
- Installed hashicorp/aws v4.58.0 (signed by HashiCorp)

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

Run `terraform apply` to apply the execution plan and create all AWS resources. 

```bash
terraform apply
```      

Answer `yes` to the prompt to confirm you want to create AWS resources. 

The public IP address will be different, but the output should be similar to:

```output
Apply complete! Resources: 5 added, 0 changed, 0 destroyed.
```

You now have an AWS EC2 virtual machine running, and are ready to deploy MariaDB. 

## Deploy a MariaDB container using Ansible

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. If you are new to Docker, consider reviewing [Learn how to use Docker](/learning-paths/cross-platform/docker/).

To run Ansible, you can an Ansible playbook. The playbook uses the `community.docker` collection to deploy MariaDB in a container.

The playbook maps the container port to the host port, which is `3306`. 

1. Use a text editor to add the contents below to a new file named `playbook.yml`.

```yml
---
- hosts: all
  remote_user: root
  become: true
  tasks:
    - name: Update the Machine and Install dependencies
      shell: |
             apt-get update -y
             apt-get -y install mariadb-client
             apt-get install docker.io -y
             usermod -aG docker ubuntu
             apt-get -y install python3-pip
             pip3 install PyMySQL
             pip3 install docker
      become: true
    - name: Reset ssh connection for changes to take effect
      meta: "reset_connection"
    - name: Log into DockerHub
      community.docker.docker_login:
        username: {{dockerhub_uname}}
        password: {{dockerhub_pass}}
    - name: Deploy mariadb docker container
      docker_container:
        image: mariadb:latest
        name: mariadb_test
        state: started
        ports:
          - "3306:3306"
        pull: true
        volumes:
         - "db_data:/var/lib/mysql:rw"
         - "mariadb-socket:/var/run/mysqld:rw"
         - "/tmp:/tmp:rw"
        restart: true
        env:
          MARIADB_ROOT_PASSWORD: {{your_mariadb_password}}
          MARIADB_USER: local_us
          MARIADB_PASSWORD: Armtest123
          MARIADB_DATABASE: arm_test

```

2. Edit `playbook.yml` to use your values 

Replace **{{your_mariadb_password}}** with your own password. 

Also, replace **{{dockerhub_uname}}** and **{{dockerhub_pass}}** with your [Docker Hub](https://hub.docker.com/) credentials. 

### Ansible Commands

1. Run the playbook using the `ansible-playbook` command:

```bash
ansible-playbook playbook.yaml -i /tmp/inventory
```

2. Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [all] *****************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
The authenticity of host 'ec2-3-135-226-118.us-east-2.compute.amazonaws.com (172.31.30.40)' can't be established.
ED25519 key fingerprint is SHA256:uWZgVeACoIxRDQ9TrqbpnjUz14x57jTca6iASH3gU7M.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [ansible-target1]

TASK [Update the Machine and install docker dependencies] *************************************************************************************************************
changed: [ansible-target1]

TASK [Reset ssh connection for changes to take effect] ****************************************************************************************************************

TASK [Log into DockerHub] *********************************************************************************************************************************************
changed: [ansible-target1]

TASK [Deploy mariadb docker containere] *******************************************************************************************************************************
changed: [ansible-target1]

PLAY RECAP ************************************************************************************************************************************************************
ansible-target1            : ok=3    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Connect to Database using your local machine

You can use the instructions from the previous topic to [connect to the database](/learning-paths/server-and-cloud/mariadb/ec2_deployment#connect-to-database-from-local-machine) and confirm the Docker container deployment is working. 

### Clean up resources

Run `terraform destroy` to delete all resources created.

```bash
terraform destroy
```
