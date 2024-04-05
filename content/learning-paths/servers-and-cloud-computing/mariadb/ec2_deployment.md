---
# User change
title: "Install MariaDB on an AWS Arm based instance"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Install MariaDB on an AWS Arm based instance

You can deploy [MariaDB](https://mariadb.org/) on AWS Graviton processors using Terraform and Ansible. 

In this topic, you will deploy MariaDB on a single AWS EC2 instance. 

If you are new to Terraform, you should look at [Automate AWS EC2 instance creation using Terraform](/learning-paths/servers-and-cloud-computing/aws-terraform/terraform/) before starting this Learning Path.

## Before you begin

Any computer which has [Terraform](/install-guides/terraform/), [Ansible](/install-guides/ansible/), and the [AWS CLI](/install-guides/aws-cli/) installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine.

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

Before you begin, you will also need:
- An AWS access key ID and secret access key. 
- An SSH key pair

The instructions to create the keys are below.

### Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for AWS EC2 access. To generate the key-pair, follow the [SSH install guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

### Acquire AWS Access Credentials

Terraform requires AWS authentication to create AWS resources. You can generate access keys (access key ID and secret access key) to perform authentication. Terraform uses the access keys to make calls to AWS using the AWS CLI. 

To generate and configure the Access key ID and Secret access key, follow the [AWS Credentials install guide](/install-guides/aws_access_keys).

## Deploy an AWS EC2 instance using Terraform

Before installing MariaDB, you need to create an AWS EC2 instance. 
   
Use a text editor to add the contents below to a new file named `main.tf`.

```console
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "Mariadb_TEST" {
  ami             = "ami-0a55ba1c20b74fc30"
  instance_type   = "t4g.small"
  security_groups = [aws_security_group.Terraformsecurity.name]
  key_name        = aws_key_pair.deployer.key_name
  tags = {
    Name = "Mariadb_TEST"
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
    description = "TLS from VPC"
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "TLS from VPC"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Terraformsecurity"
  }
}

resource "local_file" "inventory" {
  depends_on = [aws_instance.Mariadb_TEST]
  filename   = "/tmp/inventory"
  content    = <<EOF
[all]
ansible-target1 ansible_connection=ssh ansible_host=${aws_instance.Mariadb_TEST.public_ip} ansible_user=ubuntu
                EOF
}

resource "aws_key_pair" "deployer" {
  key_name   = "id_rsa"
  public_key = file("~/.ssh/id_rsa.pub")
}
```

There are 2 optional changes you can make to the `main.tf` file. 

1. (optional) In the `provider` section, change the region to be your preferred AWS region.

2. (optional) In the `aws_instance` section, change the ami value to your preferred Linux distribution. The AMI ID for Ubuntu 22.04 on Arm is `ami-0a55ba1c20b74fc30`. 

{{% notice Note %}}
The instance type is t4g.small. This is an Arm-based instance and requires an Arm Linux distribution.

The created security group opens inbound ports `22` (ssh) and `3306` (MariaDB). 
{{% /notice %}}


## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the dependencies required for AWS.

```bash
terraform init
```
    
The output should be similar to:

```output
Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/local from the dependency lock file
- Reusing previous version of hashicorp/aws from the dependency lock file
- Using previously-installed hashicorp/local v2.3.0
- Using previously-installed hashicorp/aws v4.52.0

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

The output should be similar to:

```output
Apply complete! Resources: 5 added, 0 changed, 0 destroyed.
```


## Configure MariaDB through Ansible

Ansible is a software tool that provides simple, but powerful, automation of repeated tasks. 

Using a text editor, save the code below in a file named `playbook.yaml` 

This is the YAML file for the Ansible playbook.

```yml
---
- hosts: all
  remote_user: root
  become: true
  tasks:
    - name: Update the Machine and Install dependencies
      shell: |
             apt-get update -y
             apt-get -y install mariadb-server
             apt -y install python3-pip
             pip3 install PyMySQL
      become: true
    - name: start and enable maridb service
      service:
        name: mariadb
        state: started
        enabled: yes
    - name: Change Root Password
      shell: sudo mariadb -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '{{Your_mariadb_password}}'"
    - name: Create database user with password and all database privileges and 'WITH GRANT OPTION'
      mysql_user:
         login_user: root
         login_password: {{Your_mariadb_password}}
         login_host: localhost
         name: Local_user
         host: '%'
         password: {{Give_any_password}}
         priv: '*.*:ALL,GRANT'
         state: present
    - name: MariaDB secure installation
      become: yes
      expect:
        command: mariadb-secure-installation
        responses:
           'Enter current password for root': '{{Your_mariadb_password}}'
           'Set root password': 'n'
           'Remove anonymous users': 'y'
           'Disallow root login remotely': 'n'
           'Remove test database': 'y'
           'Reload privilege tables now': 'y'
        timeout: 1
      register: secure_mariadb
      failed_when: "'... Failed!' in secure_mariadb.stdout_lines"
    - name: Enable remote login by changing bind-address
      lineinfile:
         path: /etc/mysql/mariadb.conf.d/50-server.cnf
         regexp: '^bind-address'
         line: 'bind-address = 0.0.0.0'
         backup: yes
      notify:
         - Restart mariadb
  handlers:
    - name: Restart mariadb
      service:
        name: mariadb
        state: restarted

```

{{% notice Note %}} 
Replace `{{Your_mariadb_password}}` and `{{Give_any_password}}` with your password. 
{{% /notice %}}

In the above `playbook.yml` file, you are creating a local user with all privileges granted and setting the password for the `root` user.

You are also enabling remote login by changing the `bind address` to `0.0.0.0` in the `/etc/mysql/mariadb.conf.d/50-server.cnf` file.

The inventory file `/tmp/inventory` will be generated automatically after the `terraform apply` command.

### Ansible Commands

This `ansible` Playbook uses the MySQL community module that can be installed by running:

```bash
ansible-galaxy collection install community.mysql
```

To run a Playbook, use the `ansible-playbook` command: 

```bash
ansible-playbook playbook.yml -i /tmp/inventory
```

Answer `yes` when prompted for the SSH connection.

Deployment may take a few minutes.

The output should be similar to:

```output
PLAY [all] ******************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
The authenticity of host '3.19.244.136 (3.19.244.136)' can't be established.
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

To connect to the database, you need the `public-ip` of the instance where MariaDB is deployed. 

You also need to use the MariaDB Client to interact with the MariaDB database.

```console
sudo apt install mariadb-client
```

Replace `{public_ip of instance where MariaDB deployed}`, `{user_name of database}` and `{password of database}` with your values. 

In this case `user_name`= `Local_user`, which is have created through the `playbook.yml` file. 


```console
mariadb -h {public_ip of instance where MariaDB deployed} -P3306 -u {user of database} -p{password of database}
```

The output will be:

```output
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 6
Server version: 10.6.12-MariaDB-0ubuntu0.22.04.1 Ubuntu 22.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

### Access Database and Create Table

Execute the steps below to try out MariaDB.

1. Create a database:

```mysql
create database {your_database};
```

The output will be:
```output
MariaDB [(none)]> create database arm_test;
Query OK, 1 row affected (0.001 sec)
```

2. List all databases:

```mysql
show databases;
```

The output will be:
```mysql
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| arm_test          |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```

3. Switch to the new databases:

```mysql
use {your_database};
```

The output will be:

```output
MariaDB [(none)]> use arm_test;
Database changed
```

4. Create a new table in the database.

```mysql
create table book(name char(10),id varchar(10));
```
The output will be:

```output
MariaDB [arm_test]> create table book(name char(10),id varchar(10));
Query OK, 0 rows affected (0.03 sec)

```

5. Insert data into the table:
```mysql
insert into book(name,id) values ('Abook','10'),('Bbook','20'),('Cbook','20'),('Dbook','30'),('Ebook','45'),('Fbook','40'),('Gbook
','69');
```

The output will be:

```output
MariaDB [arm_test]> insert into book(name,id) values ('Abook','10'),('Bbook','20'),('Cbook','20'),('Dbook','30'),('Ebook','45'),('Fbook','40'),('Gbook','69');
Query OK, 7 rows affected (0.01 sec)
Records: 7  Duplicates: 0  Warnings: 0
```

6. Display the database tables:

```mysql
show tables;
```

The output will be:

```output
MariaDB [arm_test]> show tables;
+--------------------+
| Tables_in_arm_test |
+--------------------+
| book               |
+--------------------+
1 row in set (0.001 sec)
```

7. Display the structure of table:

```mysql
describe {{your_table_name}};
```

The output will be:

```output
MariaDB [arm_test]> describe book;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| name  | char(10)    | YES  |     | NULL    |       |
| id    | varchar(10) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.001 sec)
```

8. Print the contents of the table:

```mysql
select * from {{your_table_name}};
```

The output will be:

```output
MariaDB [arm_test]> select * from book;

+--------+------+
| name   | id   |
+--------+------+
| Abook  | 10   |
| Bbook  | 20   |
| Cbook  | 20   |
| Dbook  | 30   |
| Ebook  | 45   |
| Fbook  | 40   |
| Gbook  | 69   |
+--------+------+
7 rows in set (0.00 sec)
```
### Clean up resources

Run `terraform destroy` to delete all resources created.

```bash
terraform destroy
```

