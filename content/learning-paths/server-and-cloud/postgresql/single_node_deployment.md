---
# User change
title: "Deploy a single instance of PostgreSQL"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy a single instance of PostgreSQL 

You can deploy PostgreSQL on AWS Graviton processors using Terraform and Ansible. 

In this topic, you will deploy PostgreSQL on a single AWS EC2 instance, and in the next topic you will deploy PostgreSQL on a three-node cluster. 

If you are new to Terraform, you should look at [Automate AWS EC2 instance creation using Terraform](/learning-paths/server-and-cloud/aws/terraform/) before starting this Learning Path.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path. 

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools. 

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

Before you begin you will also need:
- An AWS access key ID and secret access key. 
- An SSH key pair

The instructions to create the keys are below.

### Generate AWS access keys 

Terraform requires AWS authentication to create AWS resources. You can generate access keys (access key ID and secret access key) to perform authentication. Terraform uses the access keys to make calls to AWS using the AWS CLI. 

To generate an access key and secret access key, follow the [steps from the Terraform Learning Path](/learning-paths/server-and-cloud/aws/terraform#generate-access-keys-access-key-id-and-secret-access-key).

### Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for AWS EC2 access: 

```console
ssh-keygen -f aws_key -t rsa -b 2048 -P ""
```

You should now have your AWS access keys and your SSH keys in the current directory.

## Create an AWS EC2 instance using Terraform

Using a text editor, save the code below to in a file called `main.tf`

Scroll down to see the information you need to change in `main.tf`

```console

// instance creation
provider "aws" {
  region = "us-east-2"
  access_key  = "AXXXXXXXXXXXXXXXXXXXX"
  secret_key  = "AXXXXXXXXXXXXXXXXXXXX"
}
resource "aws_instance" "PSQL_TEST" {
  ami           = "ami-0f9bd9098aca2d42b"
  instance_type = "t4g.small"
  security_groups= [aws_security_group.Terraformsecurity.name]
  key_name = "aws_key"
 
  tags = {
    Name = "PSQL_TEST"
  }
}
resource "aws_default_vpc" "main" {
  tags = {
    Name = "main"
  }
}
resource "aws_security_group" "Terraformsecurity" {
  name        = "Terraformsecurity"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_default_vpc.main.id

ingress {
    description      = "TLS from VPC"
    from_port        = 5432
    to_port          = 5432
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
}
ingress {
    description      = "TLS from VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
 tags = {
    Name = "Terraformsecurity"
  }
 }
output "Master_public_IP" {
  value = [aws_instance.PSQL_TEST.public_ip]
}
 resource "aws_key_pair" "deployer" {
         key_name   = "aws_key"
         public_key = "ssh-rsaxxxxxxxxxxxxxx"
  }
// Generate inventory file
resource "local_file" "inventory" {
    depends_on= [aws_instance.PSQL_TEST]
    filename = "(your_current_directory)/hosts"
    content = <<EOF
          [db_master]
          ${aws_instance.PSQL_TEST.public_ip}         
          [all:vars]
          ansible_connection=ssh
          ansible_user=ubuntu
          EOF
}
```

Make the changes listed below in `main.tf` to match your account settings.

1. In the `provider` section, update all 3 values to use your preferred AWS region and your AWS access key ID and secret access key.

2. (optional) In the `aws_instance` section, change the ami value to your preferred Linux distribution. The AMI ID for Ubuntu 22.04 on Arm is `ami-0f9bd9098aca2d42b ` No change is needed if you want to use Ubuntu AMI. 

{{% notice Note %}}
The instance type is t4g.small. This an an Arm-based instance and requires an Arm Linux distribution.
{{% /notice %}}

3. In the `aws_key_pair` section, change the `public_key` value to match your SSH key. Copy and paste the contents of your aws_key.pub file to the `public_key` string. Make sure the string is a single line in the text file.

4. in the `local_file` section, change the `filename` to be the path to your current directory.

The hosts file is automatically generated and does not need to be changed, change the path to the location of the hosts file.


## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the dependencies required for AWS.

```console
terraform init
```
    
The output should be similar to:

```console
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

```console
terraform plan
```

A long output of resources to be created will be printed. 

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan and create all AWS resources: 

```console
terraform apply
```      

Answer `yes` to the prompt to confirm you want to create AWS resources. 

The public IP address will be different, but the output should be similar to:

```console
Apply complete! Resources: 5 added, 0 changed, 0 destroyed.

Outputs:

Master_public_IP = [
  "52.87.146.16",
]
```

## Configure PostgreSQL through Ansible

Install the PostgreSQL database and the required dependencies. 

Using a text editor, save the code below to in a file called `playbook.yaml`. This is the YAML file for the Ansible playbook. 

```console
---
- hosts: all
  become: yes
  become_method: sudo
  
  pre_tasks:
    - name: Update the Machine & Install PostgreSQL
      shell: |
             sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
             sudo wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
             sudo apt-get update
             sudo apt-get install postgresql -y
             sudo systemctl start postgresql
             sudo systemctl status postgresql
      become: true
    - name: Update apt repo and cache on all Debian/Ubuntu boxes
      apt:  upgrade=yes update_cache=yes force_apt_get=yes cache_valid_time=3600
      become: true
    - name: Install Python pip & Python package
      apt: name={{ item }} update_cache=true state=present force_apt_get=yes
      with_items:
      - python3-pip
      become: true
  tasks:
    - name: "Find out if PostgreSQL is initialized"
      ansible.builtin.stat:
        path: "/var/lib/pgsql/main/pg_hba.conf"
      register: init_status

    - name: "Start and enable services"
      service: "name={{ item }} state=started enabled=yes"
      with_items:
        - postgresql
    
  handlers:
    - name: restart postgres
      service: name=postgresql state=restarted

```

No changes are required to the file.

### Ansible Commands

Substitute your private key name, and run the playbook using the  `ansible-playbook` command:

```console
ansible-playbook playbook.yaml -i hosts --key-file aws_key
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```console
PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
The authenticity of host '3.84.22.24 (3.84.22.24)' can't be established.
ED25519 key fingerprint is SHA256:igz06Iz4YiilC08oFy8E5E78KCaJzYIthVpt1zhq9KM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [3.84.22.24]

TASK [Update the Machine & Install PostgreSQL] *********************************
changed: [3.84.22.24]

TASK [Update apt repo and cache on all Debian/Ubuntu boxes] ********************
changed: [3.84.22.24]

TASK [Install Python pip & Python package] *************************************
changed: [3.84.22.24] => (item=python3-pip)

TASK [Find out if PostgreSQL is initialized] ***********************************
ok: [3.84.22.24]

TASK [Start and enable services] ***********************************************
ok: [3.84.22.24] => (item=postgresql)

PLAY RECAP *********************************************************************
3.84.22.24                 : ok=6    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Connect to the database 

Execute the steps below to try out PostgreSQL.

1. Connect to the database using SSH to the public IP of the AWS EC2 instance. 

```console
ssh -i aws_key ubuntu@<public-IP-address>
```

2. Log in to postgres using the commands:

```console
cd ~postgres/
sudo su postgres -c psql
```

This will enter the PostgreSQL command prompt.

```console
psql (15.2 (Ubuntu 15.2-1.pgdg22.04+1))
Type "help" for help.

postgres=# 
```

3. Create a new database:

```console
create database testdb;
```

The output will be:

```console
CREATE DATABASE
```

4. List all databases: 

```console
 \l
```

The output will be:

```console
                                             List of databases
   Name    |  Owner   | Encoding | Collate |  Ctype  | ICU Locale | Locale Provider |   Access privileges   
-----------+----------+----------+---------+---------+------------+-----------------+-----------------------
 postgres  | postgres | UTF8     | C.UTF-8 | C.UTF-8 |            | libc            | 
 template0 | postgres | UTF8     | C.UTF-8 | C.UTF-8 |            | libc            | =c/postgres          +
           |          |          |         |         |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | C.UTF-8 | C.UTF-8 |            | libc            | =c/postgres          +
           |          |          |         |         |            |                 | postgres=CTc/postgres
 testdb    | postgres | UTF8     | C.UTF-8 | C.UTF-8 |            | libc            | 
(4 rows)
```

5. Switch to the new databases:

```console
 \c testdb;
```

The output confirms you have changed to the new database:

```console
You are now connected to database "testdb" as user "postgres".
```

6. Create a new table in the database:

```console
CREATE TABLE company ( emp_name VARCHAR, emp_dpt VARCHAR);
```

The output will be:

```console
CREATE TABLE
```

7. Display the database tables: 

```console
 \dt;
```

The tables will be printed:

```console
          List of relations
 Schema |  Name   | Type  |  Owner   
--------+---------+-------+----------
 public | company | table | postgres
(1 row)
```

8. Insert data into the table:

```console
INSERT INTO company VALUES ('Herry', 'Development'), ('Tom', 'Testing'),('Ankit', 'Sales'),('Manoj', 'HR'),('Noy', 'Presales');
```

The output will be:

```console
INSERT 0 5
```

9. Print the contents of the table:

```console
select * from company;
```

The output will be:

```console
 emp_name |   emp_dpt   
----------+-------------
 Herry    | Development
 Tom      | Testing
 Ankit    | Sales
 Manoj    | HR
 Noy      | Presales
(5 rows)
```

You have successfully installed PostgreSQL on an AWS EC2 instance running Graviton processors. 

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

Continue the Learning Path to create a multi-node PostgreSQL deployment. 
