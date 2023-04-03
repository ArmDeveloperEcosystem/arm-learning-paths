---
# User change
title: "Deploy single instance of MySQL"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

#  Deploy single instance of MySQL 

## Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for AWS EC2 access. To generate the key-pair, follow this [
documentation](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Generate Access keys (access key ID and secret access key)

The installation of Terraform on your desktop or laptop needs to communicate with AWS. Thus, Terraform needs to be able to authenticate with AWS. For authentication, generate access keys (access key ID and secret access key). These access keys are used by Terraform for making programmatic calls to AWS via the AWS CLI.
  
- Go to My Security Credentials
   
![image](https://user-images.githubusercontent.com/87687468/190137370-87b8ca2a-0b38-4732-80fc-3ea70c72e431.png)

- On Your Security Credentials page click on create access keys (access key ID and secret access key)
   
![image](https://user-images.githubusercontent.com/87687468/190137925-c725359a-cdab-468f-8195-8cce9c1be0ae.png)
   
- Copy the Access Key ID and Secret Access Key 

![image](https://user-images.githubusercontent.com/87687468/190138349-7cc0007c-def1-48b7-ad1e-4ee5b97f4b90.png)

## Deploy EC2 instance via Terraform

After generating the public and private keys, we have to create an EC2 instance. Then we will push our public key to the **authorized_keys** folder in `~/.ssh`. We will also create a security group that opens inbound ports `22`(ssh) and `3306`(MySQL). Below is a Terraform file called `main.tf` which will do this for us.

```console
provider "aws" {
  region = "us-east-2"
  access_key  = "AXXXXXXXXXXXXXXXXXXX"
  secret_key   = "AAXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}

resource "aws_instance" "MYSQL_TEST" {
  ami           = "ami-064593a301006939b"
  instance_type = "t4g.small"
  security_groups= [aws_security_group.Terraformsecurity.name]
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

resource "aws_security_group" "Terraformsecurity" {
  name        = "Terraformsecurity"
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
    Name = "Terraformsecurity"
  }
}

resource "local_file" "inventory" {
    depends_on=[aws_instance.MYSQL_TEST]
    filename = "/tmp/inventory"
    content = <<EOF
[all]
ansible-target1 ansible_connection=ssh ansible_host=${aws_instance.MYSQL_TEST.public_ip} ansible_user=ubuntu
                EOF
}

resource "aws_key_pair" "deployer" {
        key_name   = "id_rsa"
        public_key = file("~/.ssh/id_rsa.pub")
 }
```
{{% notice Note %}}
Replace `access_key`, and `secret_key` with your values.
{{% /notice %}}

Now, use the below Terraform commands to deploy the `main.tf` file.


### Terraform Commands

#### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command is responsible for downloading all dependencies which are required for the AWS provider.

```bash
terraform init
```

This gives the following output:

```output
Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Reusing previous version of hashicorp/local from the dependency lock file
- Using previously-installed hashicorp/local v2.4.0
- Using previously-installed hashicorp/aws v4.59.0

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

#### Create a Terraform execution plan

Run `terraform plan` to create an execution plan.

```bash
terraform plan
```

{{% notice Note %}}
The `terraform plan` command is optional. You can directly run `terraform apply` command. But it is always better to check the resources about to be created.
{{% /notice %}}

#### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan to your cloud infrastructure. The below command creates all required infrastructure.

```bash
terraform apply
```

In the output, you will need to confirm the actions to perform by typing `yes`: 

```output
[...]
Plan: 5 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_key_pair.deployer: Creating...
aws_default_vpc.main: Creating...
aws_key_pair.deployer: Creation complete after 1s [id=id_rsa]
aws_default_vpc.main: Creation complete after 3s [id=vpc-08d4df87625044841]
aws_security_group.Terraformsecurity: Creating...
aws_security_group.Terraformsecurity: Creation complete after 3s [id=sg-020f83a21c9b398ee]
aws_instance.MYSQL_TEST: Creating...
aws_instance.MYSQL_TEST: Still creating... [10s elapsed]
aws_instance.MYSQL_TEST: Creation complete after 13s [id=i-0d52fbdc1c16b977e]
local_file.inventory: Creating...
local_file.inventory: Creation complete after 0s [id=849e18d25f98a73da5064c52221d65a094b11d5a]

Apply complete! Resources: 5 added, 0 changed, 0 destroyed.
```

## Configure MySQL through Ansible
Ansible is a software tool that provides simple but powerful automation for cross-platform computer support.
Ansible allows you to configure not just one computer, but potentially a whole network of computers at once.
To run Ansible, we have to create a `playbook.yml` file, which is also known as `Ansible-Playbook`. This playbook contains a collection of tasks.

Here is the complete YML file of `Ansible-Playbook`.
```yaml
---
- hosts: all
  remote_user: root
  become: true

  tasks:
    - name: Update the Machine
      shell: apt-get update -y
    - name: Installing Mysql-Server
      shell: apt-get -y install mysql-server
    - name: Installing PIP for enabling MySQL Modules
      shell: apt -y install python3-pip
    - name: Installing Mysql dependencies
      shell: pip3 install PyMySQL
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
    - name: Create a new database with name 'arm_test'
      community.mysql.mysql_db:
        name: arm_test
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
      register: secure_mariadb
      failed_when: "'... Failed!' in secure_mariadb.stdout_lines"
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
{{% notice Note %}}
Replace `{{Your_mysql_password}}` and `{{Give_any_password}}` with your password.
{{% /notice %}}

In our case, the inventory file `/tmp/inventory` will be generated automatically after the `terraform apply` command.

### Ansible Commands

This `ansible` Playbook uses the MySQL community module that can be installed by running the following command after installation:

```bash
ansible-galaxy collection install community.mysql
```

To run a Playbook, we need to use the `ansible-playbook` command. 

```bash
ansible-playbook playbook.yml -i /tmp/inventory --key-file /home/ubuntu/.ssh/id_rsa
```

Answer `yes` when prompted for the SSH connection.

Deployment may take a few minutes.

The output should be similar to:

```output
PLAY [all] *****************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
The authenticity of host '3.21.27.138 (3.21.27.138)' can't be established.
ED25519 key fingerprint is SHA256:LHk4u86Sw5Uw7WPPvKaz7qp2mKyxn+X7Gxz1DogTL+4.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [ansible-target1]

TASK [Update the Machine] ***************************************************************************************************************
changed: [ansible-target1]

TASK [Installing Mysql-Server] **********************************************************************************************************
changed: [ansible-target1]

TASK [Installing PIP for enabling MySQL Modules] ****************************************************************************************
changed: [ansible-target1]

TASK [Installing Mysql dependencies] ****************************************************************************************************
changed: [ansible-target1]

TASK [start and enable mysql service] ***************************************************************************************************
ok: [ansible-target1]

TASK [Change Root Password] *************************************************************************************************************
changed: [ansible-target1]

TASK [Create database user with password and all database privileges and 'WITH GRANT OPTION'] *******************************************
changed: [ansible-target1]

TASK [Create a new database with name 'arm_test'] ***************************************************************************************
changed: [ansible-target1]

TASK [MySQL secure installation] ********************************************************************************************************
changed: [ansible-target1]

TASK [Enable remote login by changing bind-address] *************************************************************************************
changed: [ansible-target1]

RUNNING HANDLER [Restart mysql] *********************************************************************************************************
changed: [ansible-target1]

PLAY RECAP ******************************************************************************************************************************
ansible-target1            : ok=12   changed=10   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Connect to Database using EC2 instance

To connect to the database, we also need to use the MySQL Client on the local machine to interact with the remote MySQL database. You can install it with:

```bash
sudo apt install mysql-client
```

We also need to retrieve the `public-ip` of the instance where MySQL is deployed. 

```bash
mysql -h {public_ip of instance where Mysql deployed} -P3306 -u Local_user -p{password of database}
```

{{% notice Note %}}
Replace `{public_ip of instance where Mysql deployed}` and `{password of database}` with your values. In our case, we have set the user name to `Local_user` through the `playbook.yml` file.
{{% /notice %}}

Here is the expected output:

```output
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
Server version: 8.0.32-0ubuntu0.22.04.2 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

### Access Database and Create Table

We can list available databases by using the below command in MySQL console.

```console { output_lines = "2-11" }
show databases;
+--------------------+
| Database           |
+--------------------+
| arm_test           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.10 sec)
```

And access our database by using:

```console { output_lines = "2" }
use arm_test;
Database changed
```

To list tables in the database:

```console { output_lines= "2" }
show tables;
Empty set (0.09 sec)
```

Use the below commands to create a table:

```console { output_lines= "2" }
create table book(name char(10),id varchar(10));
Query OK, 0 rows affected (0.12 sec)
```

And insert values into it.

```console { output_lines= "2,3" }
insert into book(name,id) values ('Abook','10'),('Bbook','20'),('Cbook','20'),('Dbook','30'),('Ebook','45'),('Fbook','40'),('Gbook','69');
Query OK, 7 rows affected (0.11 sec)
Records: 7  Duplicates: 0  Warnings: 0
```
To display information about the table:
```console { output_lines= "2-8" }
describe book;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| name  | char(10)    | YES  |     | NULL    |       |
| id    | varchar(10) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.10 sec)
```

Use the below command to access the content of the table.

```console { output_lines= "2-13" }
select * from book;
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
7 rows in set (0.09 sec)
```
