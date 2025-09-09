---
title: Install MySQL
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install MySQL on Azure Cobalt 100

This section walks you through installing and securing MySQL on an Azure Arm64 virtual machine. You will set up the database, configure access, and verify it’s running—ready for development and testing.

Start by installing MySQL and other essential tools: 

## Install MySQL and tools

1. Update the system and install MySQL
You update your system's package lists to ensure you get the latest versions and then install the MySQL server using the package manager.

```console
sudo apt update
sudo apt install -y mysql-server
```

2. Secure MySQL installation

After installing MySQL, You are locking down your database so only you can access it safely. It’s like setting up a password and cleaning up unused accounts to make sure no one else can mess with your data.

```console
sudo mysql_secure_installation
```
Follow the prompts:

- Set a strong password for root.
- Remove anonymous users.
- Disallow remote root login.
- Remove test databases.
- Reload privilege tables.

3. Start and enable MySQL service
You are turning on the database so it starts working and making sure it stays on every time you turn on your computer.:

```console
sudo systemctl start mysql
sudo systemctl enable mysql
```
Check the status:

```console
sudo systemctl status mysql
```
You should see `active (running)`.

4. Verify MySQL version 

You check the installed version of MySQL to confirm it’s set up correctly and is running.

```console
mysql -V 
```
You should see output similar to the following:

```output
mysql  Ver 8.0.43-0ubuntu0.24.04.1 for Linux on aarch64 ((Ubuntu))
```
5. Access MySQL shell

You log in to the MySQL interface using the root user to interact with the database and perform administrative tasks:

```
sudo mysql
```
You should see output similar to the following:

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

6. Create a new user

You are setting up a new area to store your data and giving someone special permissions to use it. This helps you organize your work better and control who can access it:

```console
sudo mysql
```

Inside the MySQL shell, run:

```sql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'MyStrongPassword!';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
;
EXIT;
```

- Replace **MyStrongPassword!** with the password you want.
- This reloads the privilege tables so your new password takes effect immediately.

## Verify Access with New User 

You test logging into MySQL using the new user account to ensure it works and has the proper permissions. In my case new user is `admin`.

```console
mysql -u admin -p
```
- Enter your current `admin` password.

You should see output similar to the following:

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

MySQL installation is complete. You can now proceed with the baseline testing of MySQL in the next section
