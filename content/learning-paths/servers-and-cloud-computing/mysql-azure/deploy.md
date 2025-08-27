---
title: Install MySQL on Azure Cobalt 100 processors
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install MySQL on Azure Cobalt 100
Within your running docker container image or your custom Azure Linux VM, follow the instructions to install MySQL.

Start by installing MySQL and other essential tools: 

## Install MySQL and tools

1. Download Essential tools

Update the system and install required libraries and utilities. Required libraries and utilities, are needed for downloading and extracting MySQL. A library symlink is fixed to ensure the MySQL client works properly.

```console
sudo dnf update -y
sudo dnf install -y libaio bc ncurses-libs libgcc libstdc++ ca-certificates wget curl tar
sudo ln -s /usr/lib64/libncursesw.so.6 /usr/lib64/libncurses.so.6
```

2. Download MySQL and Extract the tarball

Download the Arm64 MySQL tarball from the official MySQL website, extract it in `/tmp`, and move it to `/usr/local/mysql`, a standard location for manual installations.

```console
cd /tmp
curl -L -O https://downloads.mysql.com/archives/get/p/23/file/mysql-8.0.42-linux-glibc2.28-aarch64.tar.xz
tar -xf mysql-8.0.42-linux-glibc2.28-aarch64.tar.xz 
```

3. Move MySQL folder to a standard location 

```console
sudo mv mysql-8.0.42-linux-glibc2.28-aarch64 /usr/local/mysql 
``` 

/usr/local/mysql is a common location for manual MySQL installations. 

4. Create a MySQL system user 

Create a special system user `mysql` to run the database securely. This user cannot log in to the shell and ensures MySQL runs with limited permissions.

```console
sudo useradd -r -s /bin/false mysql 
``` 
- **-r** creates a system account (no login shell by default). 
- **-s /bin/false** prevents shell login. 

5. Create the data directory and Set correct ownership

Create a directory for MySQL to store database files and set ownership to the `mysql` user. This allows MySQL to read and write data safely and prevents permission issues.

```console
sudo mkdir -p /usr/local/mysql/data
sudo chown -R mysql:mysql /usr/local/mysql 
sudo chown -R mysql:mysql /usr/local/mysql/data 
```

6. Initialize MySQL (with root password) 

Initialize MySQL to set up system tables and the data directory. Using `--initialize`, MySQL generates a temporary root password for first login.

```console
sudo /usr/local/mysql/mysql-8.0.42-linux-glibc2.28-aarch64/bin/mysqld --initialize --user=mysql --basedir=/usr/local/mysql/mysql-8.0.42-linux-glibc2.28-aarch64 --datadir=/usr/local/mysql/data
```

MySQL sets up the data directory and system tables. During this process, it automatically generates a temporary password for the root user, which looks similar to the following:

```output
2025-08-26T11:57:40.729625Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: 6pvuQf<j4<3o 
```
You can use this password to log in to the MySQL shell for the first time and then change it to a password of your choice. 

**Optional: Initialize MySQL without a password (insecure, for learning)** 

{{% notice Note %}}Warning: This is insecure and should never be used in production. It’s only for practice or local experiments.{{% /notice %}}

You can set up MySQL so that the `root` user does not require a password—useful for learning or testing on a local machine.

```console
sudo /usr/local/mysql/mysql-8.0.42-linux-glibc2.28-aarch64/bin/mysqld --initialize-insecure --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data
```
This will initialize **MySQL without a password** for `root`, perfect for learning or testing locally.

7. Start MySQL server Add MySQL binaries to your PATH

Start the MySQL server in the background using `mysqld_safe`. Add MySQL binaries to the system `PATH` so commands like `mysql` can be run from any location.

```console
sudo /usr/local/mysql/bin/mysqld_safe --datadir=/usr/local/mysql/data &
echo 'export PATH=/usr/local/mysql/bin:$PATH' >> ~/.bashrc 
source ~/.bashrc 
```

8. Verify MySQL version 

Check the MySQL version to confirm that the server is installed and accessible.

```console
mysql -V 
```
You should see output similar to the following:

```output
mysql  Ver 8.0.42 for Linux on aarch64 (MySQL Community Server - GPL)
```

## Checks that MySQL is installed and accessible. 

1. Connect to MySQL as root 

Log in to MySQL as `root` using the temporary password. Change the root password using `ALTER USER` and apply it with `FLUSH PRIVILEGES` to secure the installation for future use.

```console
mysql -u root -p
```
- Enter your current root password (temporary password if initialized with --initialize).

You should see output similar to the following:

```output
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.42

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> exit
```
2. Change the Root Password

Change the root password using `ALTER USER` and apply it with `FLUSH PRIVILEGES` to secure the installation for future use.
Once in the MySQL shell, run:

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewStrongPassword!';
FLUSH PRIVILEGES;
```

- Replace **NewStrongPassword!** with the password you want.
- This reloads the privilege tables so your new password takes effect immediately.

MySQL installation is complete. You can now proceed with the baseline testing of MySQL in the next section
