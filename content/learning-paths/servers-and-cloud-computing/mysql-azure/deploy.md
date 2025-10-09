---
title: Install MySQL
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install MySQL on Azure Cobalt 100

This section demonstrates how to install and secure MySQL on an Azure Arm64 virtual machine. You will configure the database, set up security measures, and verify that the service is running properly, making the environment ready for development, testing, or production deployment.

## Install MySQL and Tools

Before installing MySQL, it’s important to ensure your VM is updated so you have the latest Arm64-optimized libraries and security patches. Ubuntu and other modern Linux distributions maintain Arm-native MySQL packages, so installation is straightforward with the system package manager.

1. Update the system and install MySQL
Update your system's package lists to ensure you get the latest versions and then install the MySQL server using the package manager.

```console
sudo apt update
sudo apt install -y mysql-server
```

2. Secure MySQL installation

Once MySQL is installed, the default configuration is functional but not secure. 
You will lock down your database so only you can access it safely. This involves setting up a password and cleaning up unused accounts to make sure no one else can access your data.

```console
sudo mysql_secure_installation
```
This interactive script walks you through several critical security steps. Follow the prompts:

- Set a strong password for root.
- Remove anonymous users.
- Disallow remote root login.
- Remove test databases.
- Reload privilege tables.

After securing your MySQL installation, the database is significantly harder to compromise.

3. Start and enable MySQL service
After installation and securing MySQL, the next step is to ensure that the MySQL server process (mysqld) is running and configured to start automatically whenever your VM boots.

```console
sudo systemctl start mysql
sudo systemctl enable mysql
```
Verify MySQL Status:

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

4. Verify MySQL version 

You check also check the installed version of MySQL to confirm it’s set up correctly and is running.

```console
mysql -V 
```
You should see output similar to:

```output
mysql  Ver 8.0.43-0ubuntu0.24.04.1 for Linux on aarch64 ((Ubuntu))
```
5. Access MySQL shell

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

6. Create a new user

While the root account gives you full control, it’s best practice to avoid using it for day-to-day database operations. Instead, you should create separate users with specific privileges.
Start by entering the MySQL shell:

```console
sudo mysql
```

Inside the shell, create a new user:

```sql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'MyStrongPassword!';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EXIT;
```

Replace `MyStrongPassword!` with a strong password of your choice.
`FLUSH PRIVILEGES;` Reloads the in-memory privilege tables from disk, applying changes immediately.

## Verify Access with New User 

Once you’ve created a new MySQL user, it’s critical to test login and confirm that the account works as expected. This ensures the account is properly configured and can authenticate against the MySQL server.

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
