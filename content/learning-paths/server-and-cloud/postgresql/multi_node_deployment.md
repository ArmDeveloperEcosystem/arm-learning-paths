---
# User change
title: "Deploy a multi-node PostgreSQL cluster"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy a three-node PostgreSQL cluster

You can deploy PostgreSQL on a three-node cluster running on AWS Graviton processors using Terraform and Ansible. You will create one primary node and two replica nodes.

## Before you begin

You should have the prerequisite tools installed from the previous topic, [Deploy a single instance of PostgreSQL](../single_node_deployment/). 

Use the same AWS access key ID and secret access key and the same SSH key pair. 

## Create three AWS EC2 instances using Terraform

If you want to save the `main.tf` Terraform file from the previous topic make a copy (optional).

```console
cp main.tf main-save.tf
```

Use a text editor to make the required edits to `main.tf`. You are changing from 1 to 3 EC2 instances. 

There are three required modifications to `main.tf`. Each change is marked with comments identified by **3 node change**.

```console

// instance creation
provider "aws" {
  region = "us-east-1"
  access_key  = "AXXXXXXXXXXXXXXXXXXXX"
  secret_key  = "AXXXXXXXXXXXXXXXXXXXX"
}
// 3 node change: add the count line to specify 3 instances
resource "aws_instance" "PSQL_TEST" {
  count         = "3"
  ami           = "ami-0f9bd9098aca2d42b"
  instance_type = "t4g.small"
  security_groups= [aws_security_group.Terraformsecurity.name]
  key_name = aws_key_pair.deployer.key_name
 
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
// 3 node change: replace the previous value = line with this line 
output "Master_public_IP" {
  value = [aws_instance.PSQL_TEST[0].public_ip, aws_instance.PSQL_TEST[1].public_ip, aws_instance.PSQL_TEST[2].public_ip]
}
 resource "aws_key_pair" "deployer" {
         key_name   = "id_rsa"
         public_key = file("~/.ssh/id_rsa.pub")
  }
// Generate inventory file
// 3 node change: replace the single public_ip line with the three shown here.
resource "local_file" "inventory" {
    depends_on= [aws_instance.PSQL_TEST]
    filename = "/tmp/inventory"
    content = <<EOF
          [db_master]
          ${aws_instance.PSQL_TEST[0].public_ip}
          ${aws_instance.PSQL_TEST[1].public_ip}
          ${aws_instance.PSQL_TEST[2].public_ip}
          [all:vars]
          ansible_connection=ssh
          ansible_user=ubuntu
          EOF
}
```

## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Apply the Terraform execution plan

Run `terraform apply` to apply the execution plan and create all AWS resources: 

```console
terraform apply
```      

Answer `yes` to the prompt to confirm you want to create AWS resources. 

The public IP addresses will be different, but the output should be similar to:

```output
Apply complete! Resources: 7 added, 0 changed, 0 destroyed.

Outputs:

Master_public_IP = [
  "44.202.150.180",
  "44.208.26.66",
  "35.175.144.82",
]
```

You will need the IP addresses of each instance in future steps. If needed, you can look them up in the AWS EC2 console. 

## Manual configuration for primary-replica setup

Three nodes are deployed.

Choose the first one one as the primary node and the other two as replica nodes. 

For example, we can choose as below:

Primary node IP address: 44.202.150.180

Replica node 1 IP address: 44.208.26.66 (read-only)

Replica node 2 IP address: 35.175.144.82 (read-only)

Substitute your IP addresses as you follow the steps. 

### Install PostgreSQL

Install PostgreSQL on all three nodes.

{{% notice Note %}}
Install the same version of PostgreSQL on all three nodes for logical replication.
{{% /notice %}}


Use the public IP addresses for your EC2 instances. 

Log in to each node using SSH:

```console
ssh ubuntu@<public-IP-address>
```

Run the commands to install PostgreSQL:

```console
sudo apt-get update
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install postgresql-9.6 -y 
```

### Configure the primary node

SSH to the primary node and perform the steps listed to configure the primary node.
 
```console
ssh ubuntu@<primary-node-public-IP-address>
```

1. Use a text editor to modify the main configuration file `/etc/postgresql/9.6/main/postgresql.conf` (you will need to use sudo to edit)

Search for `listen_addresses` 

The PostgreSQL database server listens for connections from this IP address. 

Remove the # symbol and replace localhost with '*' (with single quotation marks). 

{{% notice Note %}}
In production projects you should limit which IP addresses are allowed to connect to the database.
{{% /notice %}}

```console
# - Connection Settings -

listen_addresses = '*'                  # what IP address(es) to listen on;
                                        # comma-separated list of addresses;
                                        # defaults to 'localhost'; use '*' for all
```

2. Use a text editor to modify the file `/etc/postgresql/9.6/main/pg_hba.conf` (you will need to use sudo to edit)

Enable SSH access to the instance. 

Change the IPv4 address from `127.0.0.1/32` to `0.0.0.0/0` and IPv6 address from ``::1/128`` to ``::/0``

```console
# IPv4 local connections:
host    all             all             0.0.0.0/0            md5
# IPv6 local connections:
host    all             all             ::/0                 md5
```

3. Log in to PostgreSQL using:

```console
cd ~postgres/
sudo su postgres -c psql
```

4. Create the replication user and assign replication privileges

The role (user) is `replication` and the password is `r3plicat1on` 

{{% notice Note %}}
In production projects you should use a strong password.
{{% /notice %}}

Run the `replication` command:

```console
CREATE ROLE replication WITH REPLICATION PASSWORD 'r3plicat1on' LOGIN;
```

The result is:

```output
CREATE ROLE
```

Run the du command:

```console
\du
```

The result is

```output
                                    List of roles
  Role name  |                         Attributes                         | Member of 
-------------+------------------------------------------------------------+-----------
 postgres    | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 replication | Replication                                                | {}
```

5. Log out from the PostgreSQL command prompt

Execute the quit command:

```console
\q
```

6. Stop PostgreSQL by using: 

```console
sudo systemctl stop postgresql
```

No output is printed from this command. 

7. Use a text editor to modify the file `/etc/postgresql/9.6/main/postgresql.conf` (you will need to use sudo to edit)

There are a number of edits to this file.

- Uncomment the line `wal_level` and set the value to hot_standby

```console
wal_level = hot_standby                 # minimal, replica, or logical
```

- Modify the `max_wal_senders` value to be 5

```console
max_wal_senders = 5             # max number of walsender processes
```

- Modify the `wal_keep_segments` value to be 32

```console
wal_keep_segments = 32          # in logfile segments, 16MB each; 0 disables
```

- Modify the `archive_mode` to be `on` and add the archive command on the next line:

```console
archive_mode = on               # enables archiving; off, on, or always
                                # (change requires restart)
archive_command = 'cp %p /var/lib/postgresql/9.6/archive/%f'
```

When `archive_mode` is `on` it will store the backup of replicas. 

The `%p` is replaced by the path name of the file to archive. 

The `%f` is replaced by only the file name. 

The path name is relative to the working directory of the server (the cluster's data directory).

You have completed the configuration file changes.

Save the changes and exit.

8. Create an archive directory and grant permission using:

```console
sudo mkdir /var/lib/postgresql/9.6/archive
sudo chown postgres.postgres /var/lib/postgresql/9.6/archive
```

9. Use a text editor to modify the file `/etc/postgresql/9.6/main/pg_hba.conf` (you will need to use sudo to edit)

Append the line at the end of the configuration file as shown in the snippet below. 

Use the IP addresses of your two replica instances. 

```console
host    replication     replication        44.208.26.66/32         md5
host    replication     replication        35.175.144.82/32        md5
```

This allows the two replica instances to connect with the master node using replication.

10. Restart the PostgreSQL service:

```console
sudo systemctl restart postgresql
```

### Configure the replica nodes

{{% notice Note %}}
Perform the steps below to configure each replica node. Make sure to do it on both instances.
{{% /notice %}}

1. Before the replica node starts replicating data from the primary node, you need to create a copy of the primary node’s data directory to the replica’s data directory. To achieve this, stop the PostgreSQL service on the replica node using below command.

```console
sudo systemctl stop postgresql 
```

2. Next, remove all files in the replica’s data directory in order to start on a clean state and make room for the primary node data directory using below command.

```console
sudo -u postgres bash -c 'rm -rf /var/lib/postgresql/9.6/main/*'
```

3. Now run the pg_basebackup utility to copy data from the primary node to the replica node using below command.

The `-U` option is the username (role) created in the earlier step.

Substitute the host_server_ip to be the IP address of your primary instance.

```console
sudo pg_basebackup -h 44.202.150.180 -D /var/lib/postgresql/9.6/main/ -P -U replication
```

Enter the password as `r3plicat1on` 

4. Use a text editor to modify the file `/etc/postgresql/9.6/main/postgresql.conf` (you will need to use sudo to edit)

Change the `hot_standby` value to `on`:

```console
hot_standby=on
```

5. Use a text editor to create a new file at `/var/lib/postgresql/9.6/main/recovery.conf` (you will need to use sudo to create)

Add the lines below to the new file. You must use the IP address as your primary node.

```console
standby_mode = 'on'
primary_conninfo = 'host=44.202.150.180 port=5432 user=replication password=r3plicat1on'
trigger_file = '/var/lib/postgresql/9.6/trigger'
restore_command = 'cp /var/lib/postgresql/9.6/archive/%f "%p"'
```

6. Start the PostgreSQL server. 

The replica will now be running in hot standby mode.

```console
sudo systemctl start postgresql
```

## Test Replication Setup

1. On the primary node, create a database with database name `postgresql` using:

Start the command prompt:

```console
cd ~postgres
sudo su postgres -c psql
```

Create the database:

```console
create database postgresql;
```

The output should be:

```output
CREATE DATABASE
```

Print the database list:

```console
\l
```

The output will be similar to:

```output
                              List of databases
    Name    |  Owner   | Encoding | Collate |  Ctype  |   Access privileges   
------------+----------+----------+---------+---------+-----------------------
 postgres   | postgres | UTF8     | C.UTF-8 | C.UTF-8 | 
 postgresql | postgres | UTF8     | C.UTF-8 | C.UTF-8 | 
 template0  | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
            |          |          |         |         | postgres=CTc/postgres
 template1  | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
            |          |          |         |         | postgres=CTc/postgres
(4 rows)
```

Quite the command prompt:

```console
\q
```

2. On a replica node, try to write data to the new database

Start the command prompt:

```console
cd ~postgres
sudo su postgres -c psql
```

Create the database:

```console
create database mydb;
```

The error shows the database is in read-only mode and does not accept writes:

```output
ERROR: 

```

You have completed the creation of a three-node PostgreSQL cluster on AWS Graviton processors.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```
