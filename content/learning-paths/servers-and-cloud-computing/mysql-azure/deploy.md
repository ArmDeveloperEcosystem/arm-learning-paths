---
title: Deploy MySQL on an Azure Arm64 virtual machine for secure cloud database hosting
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Getting started with MySQL on an Azure Arm64 virtual machine

This section demonstrates how to install and secure MySQL on an Azure Arm64 virtual machine. It shows you how to do the following:

- Configure the database
- Set up security measures
- Verify that the service is running properly

Following these steps ensures that the environment is ready for development, testing, or production deployment.

## Prepare and install MySQL and tools 

First, update your VM to ensure you have the latest Arm64-optimized libraries and security patches. Ubuntu and other modern Linux distributions maintain Arm-native MySQL packages, so installation is straightforward with the system package manager.

## Update the system and install MySQL
Update your system's package lists to ensure you get the latest versions and then install the MySQL server using the package manager:

```console
sudo apt update
sudo apt install -y mysql-server
```

## Secure MySQL installation

Once MySQL is installed, the default configuration is functional but not secure. To protect your database, you will use the `mysql_secure_installation` script, which guides you through the following essential security steps:

- Set a strong password for the root account
- Remove anonymous users
- Disable remote root login
- Remove test databases
- Reload privilege tables

These actions help ensure that only authorized users can access your MySQL server and that default vulnerabilities are eliminated.

To begin securing your MySQL installation, run the following command:

```console
sudo mysql_secure_installation
```
The interactive script walks you through several critical security steps. After following these and securing your MySQL installation, the database is significantly harder to compromise.

## Start and enable MySQL service
After installation and securing MySQL, the next step is to ensure that the MySQL server process (mysqld) is running and configured to start automatically whenever your VM boots. 

Use the following command:

```console
sudo systemctl start mysql
sudo systemctl enable mysql
```
## Verify MySQL status

Check the status of the MySQL service to confirm that it is running and enabled:

```console
sudo systemctl status mysql
```
You should see output similar to:

```output
mysql.service - MySQL Community Server
     Loaded: loaded (/usr/lib/systemd/system/mysql.service; enabled; preset: enabled)
     Active: active (running) since Tue 2025-09-30 20:31:48 UTC; 1min 53s ago
   Main PID: 3255 (mysqld)
     Status: "Server is operational"
      Tasks: 39 (limit: 19099)
     Memory: 366.4M (peak: 380.2M)
        CPU: 952ms
     CGroup: /system.slice/mysql.service
             └─3255 /usr/sbin/mysqld
```
You should see `active (running)` in the output, which indicates that MySQL is up and running.

## Verify MySQL version 

You can also check the installed version of MySQL to confirm it’s set up correctly and is running.

```console
mysql -V 
```
You should see output similar to:

```output
mysql  Ver 8.0.43-0ubuntu0.24.04.1 for Linux on aarch64 ((Ubuntu))
```
## Access MySQL shell

After confirming that MySQL is running, the next step is to log in to the MySQL monitor (shell). This is the command-line interface used to interact with the database server for administrative tasks such as creating users, managing databases, and tuning configurations.

```
sudo mysql
```
You should see output similar to:

```output
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 17
Server version: 8.0.43-0ubuntu0.24.04.1 (Ubuntu)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```
The `mysql> prompt` indicates you are now in the MySQL interactive shell and can issue SQL commands.

## Create a new user

While the root account gives you full control, it’s best practice to avoid using it for day-to-day database operations. Instead, you should create separate users with specific privileges.
Start by entering the MySQL shell:

```console
sudo mysql
```

Inside the MySQL shell, create a new user:

```sql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'MyStrongPassword!';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EXIT;
```

Replace `MyStrongPassword!` with a strong password of your choice.
`FLUSH PRIVILEGES;` Reloads the in-memory privilege tables from disk, applying changes immediately.

## Verify access with new user 

After creating a new MySQL user, test the login. This confirms that the account is configured correctly and can authenticate with the MySQL server.

Run the following command ( for user `admin`):

```console
mysql -u admin -p
```
You will then be asked to enter the password you created in the previous step.

You should see output similar to:

```output
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 8.0.43-0ubuntu0.24.04.1 (Ubuntu)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement
mysql> exit
```

With this, the MySQL installation is complete. You can now proceed with baseline testing of MySQL in the next section.
