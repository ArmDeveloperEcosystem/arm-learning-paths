---
title: Install WordPress and MySQL on an always free ARM tier on OCI 

weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This Learning Path shows how to install MySQL Community Server and WordPress on an Arm virtual machine instance in Oracle Cloud Infrastructure (OCI).

## Before you begin

You may want to review the Learning Path [Getting Started with Oracle OCI](/learning-paths/servers-and-cloud-computing/csp/oci/) before you begin.

You will need an [Oracle OCI account](https://cloud.oracle.com/) to complete this Learning Path. [Create an account](https://signup.oraclecloud.com/) and use Oracle Cloud Free Tier if you don’t already have an account.

## Deploying a Compute Instance

You can deploy manually an ARM (Ampere) compute instance in OCI via the console or use Terraform.

If you want to deploy a raw compute instance using Terraform, you can follow this learning path [Deploy Arm Instances on Oracle Cloud Infrastructure (OCI) using Terraform](https://learn.arm.com/learning-paths/servers-and-cloud-computing/oci-terraform/).

## Connecting to the Compute Instance

To install WordPress and MySQL, we need first to connect in SSH to the compute instance.

```console
$ ssh -i ~/.ssh/id_rsa_oci opc@1xx.xxx.xxx.xx0
The authenticity of host '1xx.xxx.xxx.xx0 (1xx.xxx.xxx.xx0)' can't be established.
ED2XXXX key fingerprint is SHA256:xxxxxxxxXXxxxxxxxxxxxXXxxxxxxxxxxXXxxxxXXxx.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '1xx.xxx.xxx.xx0' (ED2XXXX) to the list of known hosts.
[opc@ampere1 ~]$
```

## Installing MySQL

We start by installing MySQL 8.1, latest Innovation Release, using the Community repository.

We need to install the Yum repository for the OS version we have installed:

```console
cat /etc/oracle-release 
Oracle Linux Server release 9.2
```

We visit https://dev.mysql.com/downloads/repo/yum/ to get the latest repository's rpm:

```console
sudo rpm -ivh https://dev.mysql.com/get/mysql80-community-release-el9-4.noarch.rpm
```

And we install MySQL and MySQL Shell:

```console
sudo dnf install -y mysql-community-server mysql-shell \
                 --enablerepo mysql-innovation-community --enablerepo mysql-tools-innovation-community
```

## Preparing the Database

We need to start MySQL and change the `root` password:

```console
sudo systemctl start mysqld
```

By default, MySQL generates a password for the `root` user:

```console
sudo grep password /var/log/mysqld.log 
2023-09-06T08:47:37.029047Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: cMP,ycA01Yoq
```

Let's connect to the MySQL instance using MySQL Shell:

```console
mysqlsh --sql mysql://root@localhost
Please provide the password for 'root@localhost': ************
Save password for 'root@localhost'? [Y]es/[N]o/Ne[v]er (default No): no
Error during auto-completion cache update: You must reset your password using ALTER USER statement before executing this statement.
MySQL Shell 8.1.1

Copyright (c) 2016, 2023, Oracle and/or its affiliates.
Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
Other names may be trademarks of their respective owners.

Type '\help' or '\?' for help; '\quit' to exit.
Creating a Classic session to 'root@localhost'
Your MySQL connection id is 8
No default schema selected; type \use <schema> to set one.
 MySQL  localhost  SQL > 
```

And change the password:

```sql
SQL > set password='MyPassw0rd!';
Query OK, 0 rows affected (0.0247 sec)
```

We can create a database for WordPress and a dedicated user:

```sql
SQL > create database wordpress;
SQL > create user wordpress identified by 'WPpassw0rd!';
SQL > grant all privileges on wordpress.* to wordpress;
```

## Installing the Webserver

We use Apache as webserver. We need to install httpd, PHP and several PHP modules:

```console
sudo yum install -y httpd php php-mysqlnd php-zip php-gd php-mbstring php-xml php-json
```

## Staring Apache

Now we need to start apache and configure the system to start it again in case of a reboot or a crash:

```console
sudo systemctl enable httpd --now
```

## Security

We need to open the firewall to let http (and eventually https) connections to reach our webserver.

So we open the firewall:

```console
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-port=443/tcp
sudo firewall-cmd --reload
```

We also need to modify the Security List in OCI's console.

We select the Compute Instance's subnet:

![img1](images/01.png)

Then we click on the default security list:

![img1](images/02.png)

And we add a new rule to allow http and https connections (TCP ports 80 and 443) for the world (0.0.0.0/0):

![img1](images/03.png)

When done, we can try to use the compute instance's public ip in a browser and we should see the following page:

![img1](images/04.png)

### SE Linux

We also need to make some modification to SE Linux to allow Apache to write data and to connect to MySQL:

```console
sudo chcon -t httpd_sys_rw_content_t /var/www/html -R
sudo setsebool -P httpd_can_network_connect_db 1
```

## Installing WordPress

We can download the lastest WordPress release using the following command:

```console
curl -O https://wordpress.org/latest.tar.gz
```

And we extract the previous tarball in the web root directory:

```console
sudo tar zxf latest.tar.gz -C /var/www/html/ --strip 1
```

We need to adjust the ownership of the newly extracted files:

```console
sudo chown apache. -R /var/www/html/
```

We also need to create a new folder for the eventual uploads and set the ownership correctly:

```console
sudo mkdir /var/www/html/wp-content/uploads
sudo chown apache:apache /var/www/html/wp-content/uploads
```

In the browser where we use the Compute Instance's public IP, we just need to refresh the page and
we should now see the WordPress installation wizard:

![img1](images/05.png)

Then we need to use the credentials we have created in MySQL for the WordPress user and use `127.0.0.1` as database host:

![img1](images/06.png)

Just follow the next steps in the Wizard and at the end of it, you should see your WordPress instance using MySQL on an ARM Shape (Ampere always Free) on OCI:

![img1](images/07.png)