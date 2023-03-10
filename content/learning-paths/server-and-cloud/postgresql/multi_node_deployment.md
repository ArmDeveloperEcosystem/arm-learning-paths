---
# User change
title: "Deploy a 3-node PostgreSQL cluster with two hot standby servers"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy multi-node PostgreSQL cluster

## Before you begin
Any computer which has the required tools installed can be used for this section.

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start). Create an account if needed.

Below tools are required on the computer you are using. Follow the links to install the required tools.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html)
* [Ansible](https://www.cyberciti.biz/faq/how-to-install-and-configure-latest-version-of-ansible-on-ubuntu-linux/)
* [Terraform](/install-tools/terraform)

## Generate Access keys (Access key ID and Secret access key)

The installation of Terraform on your desktop or laptop needs to communicate with AWS. Thus, Terraform needs to be able to authenticate with AWS. For authentication, generate access keys (Access key ID and Secret access key). These access keys are used by Terraform for making programmatic calls to AWS via AWS CLI. To generate an Access key and Secret key, follow this [documentation](/learning-paths/server-and-cloud/aws/terraform#generate-access-keys-access-key-id-and-secret-access-key).

## Generate key-pair(public key, private key) using ssh keygen

Before using Terraform, first generate the key-pair (public key, private key) using `ssh-keygen`. Then associate both public and private keys with AWS EC2 instances. To generate the key-pair, follow this [documentation](/learning-paths/server-and-cloud/aws/terraform#generate-key-pairpublic-key-private-key-using-ssh-keygen).


## Deploy EC2 instances via Terraform

After generating the public and private keys, we have to create an EC2 instance. Then we will push our public key to the **authorized_keys** folder in **~/.ssh**. We will also create a security group that opens inbound ports **22**(ssh) and **5432**(PSQL). Below is a Terraform file called **main.tf**.


```console
// instance creation

provider "aws" {
  region = "us-east-2"
  access_key  = "AXXXXXXXXXXXXXXXXX"
  secret_key  = "AXXXXXXXXXXXXXXXXX"
}
resource "aws_instance" "PSQL_TEST" {
  count         = "3"
  ami           = "ami-064593a301006939b"
  instance_type = "t4g.small"
  security_groups= [aws_security_group.Terraformsecurity.name]
  key_name = "task2-key"
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
 resource "aws_key_pair" "deployer" {
         key_name   = "task2-key"
         public_key = "ssh-rsaxxxxxxxxxxxxxx"
  }

output "Master_public_IP" {
  value = [aws_instance.PSQL_TEST[0].public_ip, aws_instance.PSQL_TEST[1].public_ip, aws_instance.PSQL_TEST[2].public_ip]

}
```
**NOTE:-** Replace **public_key**, **access_key**, **secret_key**, and **key_name** with respective values.

Now, use the below Terraform commands to deploy the **main.tf** file.

## Terraform Commands

### Initialize Terraform and Create a Terraform execution plan
To deploy the instances, we need to initialize Terraform, generate an execution plan and apply the execution plan to our cloud infrastructure. Follow this [documentation](/learning-paths/server-and-cloud/aws/terraform#initialize-terraform) to initialize and create a Terraform execution plan for main.tf file.

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan to your cloud infrastructure. The below command creates all required infrastructure.

```console
terraform apply
```      
![image](https://user-images.githubusercontent.com/92078754/220016789-31a86235-19e5-4f3d-959c-003b7a63c8b5.png)

## Manual configuration for primary-replica setup

Three nodes are deployed by above Terraform configuration and we can choose one as Primary node and rest as replica nodes. For example, we can choose as below:

**Primary node IP:** 3.15.154.99

**Replica node IP:** 13.58.196.137 (hot standby server that is read-only)

**Replica1 node IP:** 3.145.160.81  (hot standby server that is read-only)

### Install PostgreSQL Server

The first step is to install PostgreSQL on the Primary and both the Replica nodes. 

**NOTE:** You need to install the same version of PostgreSQL(v9.6) on all three nodes for logical replication.

Log into all three nodes using `ssh -i ~/.ssh/private_key username@host` and follow the commands below for PostgreSQL installation.
```console
sudo apt-get update
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install postgresql-9.6  
```

### Configure Primary Node

SSH to the **primary node** and follow the steps below to make configuration changes.
 
```console
ssh -i ~/.ssh/private_key ubuntu@{{ primary_node_ip }}
```
Next, edit the main configuration file **/etc/postgresql/9.6/main/postgresql.conf** using your editor.
With the file open, locate the **listen_addresses** directive. This directive specifies the IP address under which the PostgreSQL database server listens for connections. You can simply  remove the # symbol and replace localhost with '*' in the single quotation. Although we are allowing connections from any IP address, in practice, it's good to limit which IP addresses are allowed to connect to the database.

![image](https://user-images.githubusercontent.com/92078754/215722631-7ec6ac62-7726-4fee-821c-ad1149699efd.png)

Next, go to **pg_hba.conf** file in this location **/etc/postgresql/9.6/main/pg_hba.conf**. To access your instance using SSH, we need to enable all IPv4 & IPv6 addresses. To do so, change the IPv4 address from **127.0.0.1/32** (localhost) to **0.0.0.0/0** and IPv6 address from **::1/128** to **::/0**.

![image](https://user-images.githubusercontent.com/92078754/217788571-697413fe-141a-4266-8800-b6b6c82a7dbd.png) 

Next, log into PostgreSQL by using the below commands.
```console
cd ~postgres/
sudo su postgres -c psql
```
Then run the following command to create the replication user and assign replication privileges. In this command, **replication** is the role(user) name while **password** is the user’s password. Be sure to provide a strong password, unlike the one we have used which is purely for demo purposes.

```console
CREATE ROLE replication WITH REPLICATION PASSWORD 'password' LOGIN;
```
![image](https://user-images.githubusercontent.com/92078754/215955679-50b6cb30-1f4e-4ca1-90d3-4758b1a69de7.png)

Then logout from the PostgreSQL prompt.

![image](https://user-images.githubusercontent.com/92078754/215955930-590628a4-463b-4090-b2d2-12defed9aeb0.png)

Next, stop the PostgreSQL by using `sudo systemctl stop postgresql` command.

Next, locate the **wal_level** directive in the **/etc/postgresql/9.6/main/postgresql.conf file**, this setting specifies the amount of information to be written to the Write Ahead Log (WAL) file.
Uncomment the line and set it to hot_standby as shown below.

![image](https://user-images.githubusercontent.com/92078754/215723032-7e1486d7-8ac5-4eee-8be8-206c8a18eb24.png)

Next, locate the **max_wal_sender** and **wal_keep_segments**. **max_wal_sender** Specifies the maximum number of concurrent connections from standby servers (i.e., the maximum number of simultaneously running WAL sender processes) and **max_wal_sender** Specifies the minimum number of past log file segments kept in the pg_xlog directory, in case a standby server needs to fetch them for streaming replication. 

![image](https://user-images.githubusercontent.com/92078754/215723543-ece14cf8-f235-4a47-8966-0d6cbcb9e7da.png)

Next, locate the **archive_mode** by default, it is set to off when set to on, it will store the backup of replicas. Also, add **archive_command** while storing the data.  Any **%p** in the string is replaced by the path name of the file to archive, and any **%f** is replaced by only the file name. (The path name is relative to the working directory of the server, i.e., the cluster's data directory).

![image](https://user-images.githubusercontent.com/92078754/217772707-5b8d51fc-ed75-46d3-9593-4b74e72d96e7.png)


These changes are required in the configuration file. Save the changes and exit.

Next, create an archive directory and grant permission(The **chown** command changes the owner of a file) to it by following below commands.
```console
sudo mkdir /var/lib/postgresql/9.6/archive
sudo chown postgres.postgres /var/lib/postgresql/9.6/archive
```
Next, access the **/etc/postgresql/9.6/main/pg_hba.conf** configuration file.
Append the line at the end of the configuration file as shown in the snippet below. This allows the replica and replica1 **ip-adresses** to connect with the master node using replication.

![image](https://user-images.githubusercontent.com/92078754/220019422-46ce732e-7104-43a3-9eaf-9f97027efac0.png)

Save the changes and close this file. Then restart PostgreSQL service.

```console
sudo systemctl restart postgresql
```
### Configure Replica Nodes(Replica & Replica1)

**NOTE:** Follow the below steps to configure both the replicas.

Before the replica node starts replicating data from the primary node, you need to create a copy of the primary node’s data directory to the replica’s data directory. To achieve this, stop the PostgreSQL service on the replica node using below command.

```console
sudo systemctl stop postgresql 
```
Next, remove all files in the replica’s data directory in order to start on a clean state and make room for the primary node data directory using below command.

```console
sudo rm -rf /var/lib/postgresql/9.6/main/*
```

Now run the pg_basebackup utility to copy data from the primary node to the replica node using below command.

```console
pg_basebackup -h {{ host_server_ip }} -D /var/lib/postgresql/9.6/main/ -P -U {{ replication_user }}
```
![image](https://user-images.githubusercontent.com/92078754/217457056-08ace6cf-4608-4d2f-b969-186ace92fd65.png)

Now we must modify **/etc/postgresql/9.6/main/postgresql.conf** to change **hot_standby=off** to **hot_standby=on**.

![image](https://user-images.githubusercontent.com/92078754/215724525-3efb4088-2118-4ba9-9138-41b50f076a66.png)

Lastly, we need to create a **recovery.conf** file in the data directory **/var/lib/postgresql/9.6/main/**. Otherwise, replication will not happen.

Add the following code in the **recovery.conf** file.

```console
standby_mode = 'on'
primary_conninfo = 'host=3.15.154.99 port=5432 user=replication password=password'
trigger_file = '/var/lib/postgresql/9.6/trigger'
restore_command = 'cp /var/lib/postgresql/9.6/archive/%f "%p"'
```
**NOTE:** In primaryconf_info, you can replace **host={primary_server_ip}**, **user={replication_name}** and **password={replication_role_password}**.

Now, start the PostgreSQL server. The replica will now be running in hot standby mode.
```console
sudo systemctl start postgresql
```
## Test Replication Setup

In **primary node**, create a database with database name **postgresql** using below commands.
```console
create database postgresql;
```

![image](https://user-images.githubusercontent.com/92078754/217457571-e2cfd18c-f27b-4ac8-9c96-dc38d81d5970.png)

In **replica node**, the database **postgresql** is created in the primary node will replicate on the replica node and produces below error while writing something here.

![image](https://user-images.githubusercontent.com/92078754/217457990-ceedf971-1334-483d-906f-2a005f7e13f3.png)

**Replica1:** Here, the data from primary node is also replicated and produces below error while writing something here.

![image](https://user-images.githubusercontent.com/92078754/217460213-91bf664f-f498-4b8d-b817-b5476954273b.png)













