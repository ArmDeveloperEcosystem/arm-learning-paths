---
# User change
title: "Deploy Redis as a cache for Postgres on an AWS Arm based Instance"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy Redis as a cache for Postgres on an AWS Arm based Instance

You can deploy Redis as a cache for Postgres on an AWS Arm based Instance using Terraform and Ansible. 

In this section, you will deploy Redis as a cache for Postgres on an AWS Instance. 

If you are new to Terraform, you should look at [Automate AWS EC2 instance creation using Terraform](/learning-paths/servers-and-cloud-computing/aws-terraform/terraform/) before starting this Learning Path.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path. 

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools. 

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

Before you begin, you will also need:
- An AWS access key ID and secret access key
- An SSH key pair

The instructions to create the keys are below.

### Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for AWS EC2 access. To generate the key-pair, follow this [guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}


### Acquire AWS Access Credentials

The installation of Terraform on your desktop or laptop needs to communicate with AWS. Thus, Terraform needs to be able to authenticate with AWS.

To generate and configure the Access key ID and Secret access key, follow this [guide](/install-guides/aws_access_keys).

## Create an AWS EC2 instance using Terraform

Using a text editor, save the code below in a file called `main.tf`:

```console
provider "aws" {
  region = "us-east-2"
}
resource "aws_instance" "PSQL_TEST" {
  count           = "2"
  ami             = "ami-0ca2eafa23bc3dd01"
  instance_type   = "t4g.small"
  security_groups = [aws_security_group.Terraformsecurity.name]
  key_name        = aws_key_pair.deployer.key_name

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
    description = "TLS from VPC"
    from_port   = 5432
    to_port     = 5432
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
output "Master_public_IP" {
  value = [aws_instance.PSQL_TEST[0].public_ip, aws_instance.PSQL_TEST[1].public_ip]
}
resource "aws_key_pair" "deployer" {
  key_name   = "id_rsa"
  public_key = file("~/.ssh/id_rsa.pub")
}
// Generate inventory file
resource "local_file" "inventory" {
  depends_on = [aws_instance.PSQL_TEST]
  filename   = "/tmp/inventory"
  content    = <<EOF
          [db_master]
          ${aws_instance.PSQL_TEST[0].public_ip}
          ${aws_instance.PSQL_TEST[1].public_ip}
          [all:vars]
          ansible_connection=ssh
          ansible_user=ubuntu
          EOF
}
```
Make the changes listed below in `main.tf` to match your account settings.

1. In the `provider` section, update the region value to use your preferred AWS region.

2. (optional) In the `aws_instance` section, change the ami value to your preferred Linux distribution. The AMI ID for Ubuntu 22.04 on Arm is `ami-0ca2eafa23bc3dd01`. No change is needed if you want to use Ubuntu AMI. 

{{% notice Note %}}
The instance type is t4g.small. This is an Arm-based instance and requires an Arm Linux distribution.
{{% /notice %}}

The inventory file is automatically generated and does not need to be changed.

## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the dependencies required for AWS.

```console
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

```console
terraform plan
```

A long output of resources to be created will be printed. 

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan and create all AWS resources.

```console
terraform apply
```      

Answer `yes` to the prompt to confirm you want to create AWS resources.

The public IP address will be different, but the output should be similar to:

```output
Apply complete! Resources: 6 added, 0 changed, 0 destroyed.
Outputs:
Master_public_IP = [
  "3.144.105.166",
  "3.139.240.124",
]
```

## Configure Postgres through Ansible

Install Postgres and the required dependencies.

Using a text editor, save the code below in a file called `playbook.yaml`. This Playbook installs & enables Postgres in the instances.

```console
---
- hosts: all
  become: yes

  tasks:
    - name: Update the Machine & Install PostgreSQL
      shell: |
             sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
             sudo wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -
             sudo apt-get update
             sudo apt-get install postgresql -y
             sudo systemctl start postgresql
      become: true
    - name: Update apt repo and cache on all Debian/Ubuntu boxes
      apt:  upgrade=yes update_cache=yes force_apt_get=yes cache_valid_time=3600
      become: true
    - name: Install Python pip and PostgreSQL package
      apt: name={{ item }} update_cache=true state=present force_apt_get=yes
      with_items:
      - python3-pip
      - acl
      become: true
    - name: Start and enable services
      service: "name={{ item }} state=started enabled=yes"
      with_items:
      - postgresql
    - name: Utility present
      ansible.builtin.package:
        name: python3-psycopg2
        state: present
    - name: Replace postgresql configuration file to allow remote connection
      ansible.builtin.lineinfile:
         path: "/etc/postgresql/15/main/postgresql.conf"
         line: '{{ item }}'
         owner: postgres
         group: postgres
         mode: '0777'
      with_items:
          - "listen_addresses = '*'"
      become: yes
      become_user: postgres
    - name: Allow trust connection for the db user
      postgresql_pg_hba:
        dest: "/etc/postgresql/15/main/pg_hba.conf"
        contype: host
        databases: all
        method: trust
        address: 0.0.0.0/0
        users: "all"
        create: true
      become: yes
      become_user: postgres
      notify: restart postgres

  handlers:
    - name: restart postgres
      service: name=postgresql state=restarted        
```

### Ansible Commands

Run the playbook using the  `ansible-playbook` command:

```console
ansible-playbook playbook.yaml -i /tmp/inventory
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [all] ******************************************************************************************************************************************
TASK [Gathering Facts] ******************************************************************************************************************************
ok: [3.144.105.166]
ok: [3.139.240.124]
TASK [Update the Machine & Install PostgreSQL] ******************************************************************************************************
changed: [3.139.240.124]
changed: [3.144.105.166]
TASK [Update apt repo and cache on all Debian/Ubuntu boxes] *****************************************************************************************
ok: [3.139.240.124]
ok: [3.144.105.166]
TASK [Install Python pip and PostgreSQL package] ****************************************************************************************************
ok: [3.139.240.124] => (item=python3-pip)
ok: [3.144.105.166] => (item=python3-pip)
ok: [3.139.240.124] => (item=acl)
ok: [3.144.105.166] => (item=acl)
TASK [Start and enable services] ********************************************************************************************************************
ok: [3.139.240.124] => (item=postgresql)
ok: [3.144.105.166] => (item=postgresql)
TASK [Utility present] ******************************************************************************************************************************
ok: [3.144.105.166]
ok: [3.139.240.124]
TASK [Replace postgresql configuration file to allow remote connection] *****************************************************************************
ok: [3.139.240.124] => (item=listen_addresses = '*')
ok: [3.144.105.166] => (item=listen_addresses = '*')
TASK [Allow trust connection for the db user] *******************************************************************************************************
ok: [3.139.240.124]
ok: [3.144.105.166]
PLAY RECAP ******************************************************************************************************************************************
3.139.240.124              : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
3.144.105.166              : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Connect to Database from local machine

To connect to the database, you need the `public-ip` of the instance where Postgres is deployed. You also need to use the Postgres Client to interact with the PostgreSQL database.

```console
apt install -y postgresql-client
```

```console
psql -h {public_ip of instance where Postgres deployed} -U postgres
```
Replace `{public_ip of instance where Postgres deployed}` with your value. 

The output will be:
```output
ubuntu@ip-172-31-38-39:~/redis_psql$ psql -h 3.144.105.166 -U postgres
psql (14.7 (Ubuntu 14.7-0ubuntu0.22.04.1), server 15.2 (Ubuntu 15.2-1.pgdg22.04+1))
WARNING: psql major version 14, server major version 15.
         Some psql features might not work.
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.
postgres=#
```

### Access Database and Create Table

1. You can create and access your database by using the commands below:

```console
create database {your_database};
```

```console
\c {your_database};
```

The output will be:

```output
postgres=# create database arm_test1;
CREATE DATABASE
postgres=# \c arm_test1
psql (14.7 (Ubuntu 14.7-0ubuntu0.22.04.1), server 15.2 (Ubuntu 15.2-1.pgdg22.04+1))
WARNING: psql major version 14, server major version 15.
         Some psql features might not work.
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
You are now connected to database "arm_test1" as user "postgres".```
```

2. Use the commands below to create a table and insert values into it:

```console
create table book(name char(10),id varchar(10));
```
```console
insert into book(name,id) values ('Abook','10'),('Bbook','20'),('Cbook','20'),('Dbook','30'),('Ebook','45'),('Fbook','40'),('Gbook
','69');
```

The output will be:

```output
arm_test1=# create table book(name char(10),id varchar(10));
CREATE TABLE
arm_test1=# insert into book(name,id) values ('Abook','10'),('Bbook','20'),('Cbook','20'),('Dbook','30'),('Ebook','45'),('Fbook','40'),('Gbook
','69');
INSERT 0 7
```

3. Use the command below to access the content of the table.

```console
select * from {{your_table_name}};
```

The output will be:

```output
arm_test1=# select * from book;
    name    | id
------------+----
 Abook      | 10
 Bbook      | 20
 Cbook      | 20
 Dbook      | 30
 Ebook      | 45
 Fbook      | 40
 Gbook     +| 69
            |
(7 rows)
```

4. Now connect to the second instance and repeat the above steps with a different database as shown below.    

The output will be:

```output
postgres=# create database arm_test2;
CREATE DATABASE
postgres=# \c arm_test2
psql (14.7 (Ubuntu 14.7-0ubuntu0.22.04.1), server 15.2 (Ubuntu 15.2-1.pgdg22.04+1))
WARNING: psql major version 14, server major version 15.
         Some psql features might not work.
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
You are now connected to database "arm_test2" as user "postgres".
arm_test2=# create table movie(name char(10),id varchar(10));
CREATE TABLE
arm_test2=# insert into movie(name,id) values ('Amovie','1'), ('Bmovie','2'), ('Cmovie','3'), ('Dmovie','4'), ('Emovie','5'), ('Fmovie','6'), ('Gmovie','7');
INSERT 0 7
arm_test2=# select * from movie;
    name    | id
------------+----
 Amovie     | 1
 Bmovie     | 2
 Cmovie     | 3
 Dmovie     | 4
 Emovie     | 5
 Fmovie     | 6
 Gmovie     | 7
(7 rows)
```


## Deploy Redis as a cache for Postgres using Python

You will create two `.py` files on the host machine to deploy Redis as a Postgres cache using Python: `values.py` and `redis_cache.py`.

Create `values.py` with the content below to store the IP addresses of the instances and the databases created in them.
```console
PSQL_TEST=[["{{public_ip of PSQL_TEST[0]}}", "arm_test1"],
["{{public_ip of PSQL_TEST[1]}}", "arm_test2"]]
```
Replace `{{public_ip of PSQL_TEST[0]}}` & `{{public_ip of PSQL_TEST[1]}}` with the public IPs generated in the `/tmp/inventory` file after running the Terraform commands.

Create `redis_cache.py` with content below to access data from Redis Cache and, if not present, store it in the Redis Cache.   
```console
import sys
import psycopg2
import redis
from values import *
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-db", "--database", help="Database")
parser.add_argument("-k", "--key", help="Key")
parser.add_argument("-q", "--query", help="Query")
args = parser.parse_args()

R_SERVER = redis.Redis(
    host='localhost',
    port='6379')

for i in range(0,2):
    if (PSQL_TEST[i][1]==args.database):
        try:
            conn = psycopg2.connect (host = PSQL_TEST[i][0], dbname = PSQL_TEST[i][1], user="postgres")
        except psycopg2.OperationalError as e:
             print('Unable to connect!\n{0}').format(e)
             sys.exit (1)

        psqldata = R_SERVER.get(args.key)

        if not psqldata:
            cursor = conn.cursor()
            cursor.execute(args.query)
            rows = cursor.fetchall()
            mystr = ' '.join(map(str,rows))
            R_SERVER.set(args.key,mystr,120)
            print ("Updated redis with PSQL data")
            print (rows)
        else:
            print ("Loaded data from redis")
            print (psqldata)
        break
else:
    print("this database doesn't exist")
```
Change the `range` in `for loop` according to the number of instances created.

Install the required Python modules using `pip` and other required dependency:
```console
apt-get install redis
```
```console
pip install redis
```

To execute the `redis_cache.py` script, run the following command:
```console
python3 redis_cache.py -db {database_name} -k {key} -q {query}
```
Replace `{database_name}` with the database you want to access, `{query}` with the query you want to run in the database, and `{key}` with a variable to store the result of the query in Redis cache.

When the script is executed for the first time, the data is loaded from the Postgres database and stored in the Redis cache.

The output will be:
```output
ubuntu@ip-172-31-38-39:~/redis_psql$ python3 redis_cache.py  -db arm_test1 -k AA -q "select * from book limit 3"
Updated redis with PSQL data
[('Abook     ', '10'), ('Bbook     ', '20'), ('Cbook     ', '20')]
```

```output
ubuntu@ip-172-31-38-39:~/redis_psql$ python3 redis_cache.py  -db arm_test2 -k BB -q "select * from movie limit 3"
Updated redis with PSQL data
[('Amovie    ', '1'), ('Bmovie    ', '2'), ('Cmovie    ', '3')]
```

When executed after that, it loads the data from Redis cache. In the example above, the information stored in Redis cache is in the form of string. When accessing the information (within the 120-second expiry time), the data is loaded from Redis cache and dumped.

The output will be:
```output
ubuntu@ip-172-31-38-39:~/redis_psql$ python3 redis_cache.py  -db arm_test1 -k AA -q "select * from book limit 3"
Loaded data from redis
b"('Abook     ', '10') ('Bbook     ', '20') ('Cbook     ', '20')"
```

```output
ubuntu@ip-172-31-38-39:~/redis_psql$ python3 redis_cache.py  -db arm_test2 -k BB -q "select * from movie limit 3"
Loaded data from redis
b"('Amovie    ', '1') ('Bmovie    ', '2') ('Cmovie    ', '3')"
```

### Redis-cli Commands

Execute the steps below to verify that the PostgreSQL query is getting stored in Redis cache.

1. Install redis-tools to interact with redis-server.
```console
apt install redis-tools
```
2. Connect to redis-server through redis-cli.
```console
redis-cli -p 6379
```
3. Retrieve data from Redis cache.
```console
get <key>
```
{{% notice Note %}}
Key is the variable in which you store the data. In the above command, you are storing the data from the tables `book` and `movie` in `AA` and `BB` respectively.
{{% /notice %}}

The output will be:

```output
ubuntu@ip-172-31-38-39:~/redis_psql$ redis-cli -p 6379
127.0.0.1:6379> get AA
"('Abook     ', '10') ('Bbook     ', '20') ('Cbook     ', '20')"
127.0.0.1:6379> get BB
"('Amovie    ', '1') ('Bmovie    ', '2') ('Cmovie    ', '3')"
127.0.0.1:6379>
```

You have successfully deployed Redis as a cache for Postgres on an AWS Arm based Instance.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

Continue the Learning Path to deploy Redis as a cache for Postgres on an Azure Arm based Instance.
