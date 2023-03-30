---
# User change
title: "Deploy Memcached as a cache for MySQL on an AWS Arm based Instance"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy Memcached as a cache for MySQL on an AWS Arm based Instance

You can deploy Memcached as a cache for MySQL on an AWS Arm based Instance using Terraform and Ansible. 

In this section, you will deploy Memcached as a cache for MySQL on an AWS Instance. 

If you are new to Terraform, you should look at [Automate AWS EC2 instance creation using Terraform](/learning-paths/server-and-cloud/aws-terraform/terraform/) before starting this Learning Path.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path. 

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools. 

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

Before you begin, you will also need:
- An AWS access key ID and secret access key. 
- An SSH key pair

The instructions to create the keys are below.

### Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for AWS EC2 access. To generate the key-pair, follow this [
documentation](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}


### Generate AWS access keys 

Terraform requires AWS authentication to create AWS resources. You can generate access keys (access key ID and secret access key) to perform authentication. Terraform uses the access keys to make calls to AWS using the AWS CLI. 

To generate an access key and secret access key, follow the [steps from the Terraform Learning Path](/learning-paths/server-and-cloud/aws-terraform/terraform#generate-access-keys-access-key-id-and-secret-access-key).

## Create an AWS EC2 instance using Terraform

Using a text editor, save the code below in a file called `main.tf`.
    
```console
provider "aws" {
  region = "us-east-2"
  access_key  = "AXXXXXXXXXXXXXXXXXXX"
  secret_key   = "AXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
resource "aws_instance" "MYSQL_TEST" {
  count         = "2"
  ami           = "ami-0ca2eafa23bc3dd01"
  instance_type = "t4g.small"
  security_groups= [aws_security_group.Terraformsecurity1.name]
  key_name = aws_key_pair.deployer.key_name
  tags = {
    Name = "MYSQL_TEST"
  }
}
resource "aws_default_vpc" "main" {
  tags = {
    Name = "main"
  }
}
resource "aws_security_group" "Terraformsecurity1" {
  name        = "Terraformsecurity1"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_default_vpc.main.id

  ingress {
    description      = "TLS from VPC"
    from_port        = 3306
    to_port          = 3306
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
    Name = "Terraformsecurity1"
  }

 }
resource "local_file" "inventory" {
    depends_on=[aws_instance.MYSQL_TEST]
    filename = "/tmp/inventory"
    content = <<EOF
[mysql1]
${aws_instance.MYSQL_TEST[0].public_ip}
[mysql2]
${aws_instance.MYSQL_TEST[1].public_ip}
[all:vars]
ansible_connection=ssh
ansible_user=ubuntu
                EOF
}

resource "aws_key_pair" "deployer" {
        key_name   = "id_rsa"
        public_key = file("~/.ssh/id_rsa.pub")
} 
    
```
Make the changes listed below in `main.tf` to match your account settings.

1. In the `provider` section, update all 3 values to use your preferred AWS region and your AWS access key ID and secret access key.

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

The output should be similar to:

```output
Apply complete! Resources: 6 added, 0 changed, 0 destroyed.
```

## Configure MySQL through Ansible

Install MySQL and the required dependencies.

Using a text editor, save the code below in a file called `playbook.yaml`. This Playbook installs & enables MySQL in the instances and creates databases inside them.

```console
---
- hosts: mysql1, mysql2
  remote_user: root
  become: true

  tasks:
    - name: Update the Machine and Install dependencies
      shell: |
             apt-get update -y
             apt-get -y install mysql-server
             apt -y install python3-pip
             pip3 install PyMySQL
    - name: start and enable mysql service
      service:
        name: mysql
        state: started
        enabled: yes
    - name: Change Root Password
      shell: sudo mysql -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '{{Your_mysql_password}}'"
    - name: Create database user with password and all database privileges and 'WITH GRANT OPTION'
      mysql_user:
         login_user: root
         login_password: {{Your_mysql_password}}
         login_host: localhost
         name: Local_user
         host: '%'
         password: {{Give_any_password}}
         priv: '*.*:ALL,GRANT'
         state: present
    - name: Create a new database with name 'arm_test1'
      when: "'mysql1' in group_names"
      community.mysql.mysql_db:
        name: arm_test1
        login_user: root
        login_password: {{Your_mysql_password}}
        login_host: localhost
        state: present
        login_unix_socket: /run/mysqld/mysqld.sock
    - name: Create a new database with name 'arm_test2'
      when: "'mysql2' in group_names"
      community.mysql.mysql_db:
        name: arm_test2
        login_user: root
        login_password: {{Your_mysql_password}}
        login_host: localhost
        state: present
        login_unix_socket: /run/mysqld/mysqld.sock
    - name: MySQL secure installation
      become: yes
      expect:
        command: mysql_secure_installation
        responses:
           'Enter current password for root': '{{Your_mysql_password}}'
           'Set root password': 'n'
           'Remove anonymous users': 'y'
           'Disallow root login remotely': 'n'
           'Remove test database': 'y'
           'Reload privilege tables now': 'y'
        timeout: 1
      register: secure_mysql
      failed_when: "'... Failed!' in secure_mysql.stdout_lines"
    - name: Enable remote login by changing bind-address
      lineinfile:
         path: /etc/mysql/mysql.conf.d/mysqld.cnf
         regexp: '^bind-address'
         line: 'bind-address = 0.0.0.0'
         backup: yes
      notify:
         - Restart mysql
  handlers:
    - name: Restart mysql
      service:
        name: mysql
        state: restarted
```

Replace `{{Your_mysql_password}}` and `{{Give_any_password}}` in this file with your own password.

### Ansible Commands

Substitute your private key name, and run the playbook using the  `ansible-playbook` command:

```console
ansible-playbook playbook.yaml -i /tmp/inventory
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [mysql1, mysql2] ********************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
The authenticity of host '13.59.220.179 (13.59.220.179)' can't be established.
ED25519 key fingerprint is SHA256:6NBcdhBr1+nppeL27zwkXOTVnWUZGRQYVUuJOkQvGY4.
This key is not known by any other names
The authenticity of host '3.15.227.23 (3.15.227.23)' can't be established.
ED25519 key fingerprint is SHA256:0tq05+K/EPSM7rDFQBESqO3feDbk+F3XmZgjOpi6+jM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
yes
ok: [13.59.220.179]
ok: [3.15.227.23]

TASK [Update the Machine and Install dependencies] ***************************************************************************************************************
changed: [13.59.220.179]
changed: [3.15.227.23]

TASK [start and enable mysql service] ****************************************************************************************************************************
ok: [13.59.220.179]
ok: [3.15.227.23]

TASK [Change Root Password] **************************************************************************************************************************************
changed: [13.59.220.179]
changed: [3.15.227.23]

TASK [Create database user with password and all database privileges and 'WITH GRANT OPTION'] ********************************************************************
changed: [13.59.220.179]
changed: [3.15.227.23]

TASK [Create a new database with name 'arm_test1'] ***************************************************************************************************************
skipping: [3.15.227.23]
changed: [13.59.220.179]

TASK [Create a new database with name 'arm_test2'] ***************************************************************************************************************
skipping: [13.59.220.179]
changed: [3.15.227.23]

TASK [MySQL secure installation] *********************************************************************************************************************************
changed: [3.15.227.23]
changed: [13.59.220.179]

TASK [Enable remote login by changing bind-address] **************************************************************************************************************
changed: [3.15.227.23]
changed: [13.59.220.179]

RUNNING HANDLER [Restart mysql] **********************************************************************************************************************************
changed: [13.59.220.179]
changed: [3.15.227.23]

PLAY RECAP *******************************************************************************************************************************************************
13.59.220.179              : ok=9    changed=7    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
3.15.227.23                : ok=9    changed=7    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

## Connect to Database from local machine

To connect to the database, you need the `public-ip` of the instance where MySQL is deployed. You also need to use the MySQL Client to interact with the MySQL database.

```console
apt install mysql-client
```

```console
mysql -h {public_ip of instance where Mysql deployed} -P3306 -u {user of database} -p{password of database}
```
Replace `{public_ip of instance where Mysql deployed}`, `{user of database}` and `{password of database}` with your values. In this example, `user`= `Local_user`, which is getting created in the `playbook.yaml` file. 

The output will be:
```output
ubuntu@ip-172-31-38-39:~/aws-mysql$ mysql -h 13.59.220.179 -P3306 -u Local_user -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.32-0ubuntu0.22.04.2 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

### Access Database and Create Table

1. You can access your database by using the below commands.

```console
show databases;
```

```console
use {your_database};
```

The output will be:

```output
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| arm_test1          |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
mysql> use arm_test1;
Database changed
```

2. Use the below commands to create a table and insert values into it.

```console
create table book(name char(10),id varchar(10));
```
```console
insert into book(name,id) values ('Abook','10'),('Bbook','20'),('Cbook','20'),('Dbook','30'),('Ebook','45'),('Fbook','40'),('Gbook
','69');
```

The output will be:

```output
mysql> create table book(name char(10),id varchar(10));
Query OK, 0 rows affected (0.03 sec)

mysql> insert into book(name,id) values ('Abook','10'),('Bbook','20'),('Cbook','20'),('Dbook','30'),('Ebook','45'),('Fbook','40'),('Gbook
    '> ','69');
Query OK, 7 rows affected (0.01 sec)
Records: 7  Duplicates: 0  Warnings: 0

```

3. Use the below command to access the content of the table.

```console
select * from {{your_table_name}};
```

The output will be:

```output
mysql> select * from book
    -> ;
+--------+------+
| name   | id   |
+--------+------+
| Abook  | 10   |
| Bbook  | 20   |
| Cbook  | 20   |
| Dbook  | 30   |
| Ebook  | 45   |
| Fbook  | 40   |
| Gbook
 | 69   |
+--------+------+
7 rows in set (0.00 sec)
```

4. Now connect to the second instance and repeat the above steps with a different data as shown below.    
       
The output will be:

```output
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| arm_test2          |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use arm_test2;
Database changed
mysql> create table movie(name char(10),id varchar(10));
Query OK, 0 rows affected (0.02 sec)

mysql> insert into movie(name,id) values ('Amovie','1'), ('Bmovie','2'), ('Cmovie','3'), ('Dmovie','4'), ('Emovie','5'), ('Fmovie','6'), ('Gmovie','7');
Query OK, 7 rows affected (0.01 sec)
Records: 7  Duplicates: 0  Warnings: 0

mysql> select * from movie;
+--------+------+
| name   | id   |
+--------+------+
| Amovie | 1    |
| Bmovie | 2    |
| Cmovie | 3    |
| Dmovie | 4    |
| Emovie | 5    |
| Fmovie | 6    |
| Gmovie | 7    |
+--------+------+
7 rows in set (0.00 sec)
```

## Deploy Memcached as a cache for MySQL using Python

You will create two `.py` files on the host machine to deploy Memcached as a MySQL cache using Python: `values.py` and `memcached.py`.  

`values.py` to store the IP addresses of the instances and the databases created in them.
```console
MYSQL_TEST=[["{{public_ip of MYSQL_TEST[0]}}", "arm_test1"],
["{{public_ip of MYSQL_TEST[1]}}", "arm_test2"]]
```
Replace `{{public_ip of MYSQL_TEST[0]}}` & `{{public_ip of MYSQL_TEST[1]}}` with the public IPs generated in the `hosts` file after running the Terraform commands.
`memcached.py` to access data from Memcached and, if not present, store it in the Memcached.       
```console
import sys
import MySQLdb
import pymemcache
from values import *
from ast import literal_eval
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-db", "--database", help="Database")
parser.add_argument("-k", "--key", help="Key")
parser.add_argument("-q", "--query", help="Query")
args = parser.parse_args()

memc = pymemcache.Client("127.0.0.1:11211");

for i in range(0,2):
    if (MYSQL_TEST[i][1]==args.database):
        try:
            conn = MySQLdb.connect (host = MYSQL_TEST[i][0],
                                    user = "{{Your_database_user}}",
                                    passwd = "{{Your_database_password}}",
                                    db = MYSQL_TEST[i][1])
        except MySQLdb.Error as e:
             print ("Error %d: %s" % (e.args[0], e.args[1]))
             sys.exit (1)

        sqldata = memc.get(args.key)

        if not sqldata:
            cursor = conn.cursor()
            cursor.execute(args.query)
            rows = cursor.fetchall()
            memc.set(args.key,rows,120)
            print ("Updated memcached with MySQL data")
            for x in rows:
                print(x)
        else:
            print ("Loaded data from memcached")
            data = tuple(literal_eval(sqldata.decode("utf-8")))
            for row in data:
                print (f"{row[0]},{row[1]}")
        break
else:
    print("this database doesn't exist")            
```
Replace `{{Your_database_user}}` & `{{Your_database_password}}` with the database user and password created through Ansible-Playbook. Also change the `range` in `for loop` according to the number of instances created.

To execute the script, run the following command:
```console
python3 mem.py -db {database_name} -k {key} -q {query}
```
Replace `{database_name}` with the database you want to access, `{query}` with the query you want to run in the database, and `{key}` with a variable to store the result of the query in Memcached.

When the script is executed for the first time, the data is loaded from the MySQL database and stored on the Memcached server.

The output will be:
```output
ubuntu@ip-172-31-38-39:~/aws-mysql$ python3 memcached.py -db arm_test1 -k AA -q "select * from book limit 3"
Updated memcached with MySQL data
('Abook', '10')
('Bbook', '20')
('Cbook', '20')
```
```output
ubuntu@ip-172-31-38-39:~/aws-mysql$ python3 memcached.py -db arm_test2 -k BB -q "select * from movie limit 3"
Updated memcached with MySQL data
('Amovie', '1')
('Bmovie', '2')
('Cmovie', '3')
```

When executed after that, it loads the data from Memcached. In the example above, the information stored in Memcached is in the form of rows from a Python DB cursor. When accessing the information (within the 120-second expiry time), the data is loaded from Memcached and dumped.

The output will be:
```output
ubuntu@ip-172-31-38-39:~/aws-mysql$ python3 memcached.py -db arm_test1 -k AA -q "select * from book limit 3"
Loaded data from memcached
Abook,10
Bbook,20
Cbook,20
```

```output
ubuntu@ip-172-31-38-39:~/aws-mysql$ python3 memcached.py -db arm_test2 -k BB -q "select * from movie limit 3"
Loaded data from memcached
Amovie,1
Bmovie,2
Cmovie,3
```

### Memcached Telnet Commands

Execute the steps below to verify that the MySQL query is getting stored in Memcached.
1. Connect to the Memcached server with Telnet and start a session.
```console
telnet localhost 11211
```
2. Retrieve data from Memcached through Telnet.
```console
get <key>
```
**NOTE:-** Key is the variable in which we store the data. In the above command, we are storing the data from the tables `book` and `movie` in `AA` and `BB` respectively.

The output will be:

```output
ubuntu@ip-172-31-38-39:~/aws-mysql$ telnet localhost 11211
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
get AA
VALUE AA 0 51
(('Abook', '10'), ('Bbook', '20'), ('Cbook', '20'))
END
get BB
VALUE BB 0 51
(('Amovie', '1'), ('Bmovie', '2'), ('Cmovie', '3'))
END
```

You have successfully deployed Memcached as a cache for MySQL on an AWS Arm based Instance.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

Continue the Learning Path to deploy Memcached as a cache for MySQL on an Azure Arm based Instance.

