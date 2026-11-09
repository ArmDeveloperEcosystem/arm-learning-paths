---
title: Deploy MySQL on an Azure Arm64 virtual machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Get started with MySQL on an Azure Arm64 virtual machine

This section demonstrates how to install and secure MySQL on an Azure Arm64 virtual machine. It shows you how to do the following:

- Configure the database
- Set up security measures
- Verify that the service is running properly

Follow these steps to ensure that the environment is ready for development, testing, or production deployment.

## Prepare and install MySQL and tools

Ubuntu provides Arm-native MySQL packages. Install them using the system package manager.

## Update the system and install MySQL
Update your system’s package lists. Then, use the package manager to install the MySQL server:

```console
sudo apt update
sudo apt install -y mysql-server
```

## Secure MySQL installation

Review the initial security settings using the `mysql_secure_installation` script. This interactive tool helps you:

- Configure password validation
- Remove anonymous users
- Disable remote root login
- Remove test databases
- Reload privilege tables

These steps strengthen your MySQL server and reduce common vulnerabilities.

To begin securing your MySQL installation, run the following command:

```console
sudo mysql_secure_installation
```
On Ubuntu, the MySQL root account normally uses socket authentication: you administer it with `sudo mysql`. Retain this authentication method. Enable password validation if required, remove anonymous users, disallow remote root login, remove the test database, and reload privileges when prompted. You do not need a MySQL root password for this workflow.

## Start and enable MySQL service
After installing and securing MySQL, the next step is to ensure that the MySQL server process (mysqld) is running. You should also configure it to start automatically whenever your VM boots.

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
● mysql.service - MySQL Community Server
     Loaded: loaded (/usr/lib/systemd/system/mysql.service; enabled; preset: enabled)
     Active: active (running) since Mon 2026-11-09 18:13:34 UTC; 38s ago
   Main PID: 6720 (mysqld)
     Status: "Server is operational"
      Tasks: 38 (limit: 17491)
     Memory: 365.7M (peak: 380.2M)
        CPU: 407ms
     CGroup: /system.slice/mysql.service
             └─6720 /usr/sbin/mysqld
```
You should see `active (running)` in the output, which indicates that MySQL is up and running.

## Verify MySQL version

You can also check the installed version of MySQL to confirm it’s set up correctly and is running.

```console
mysql -V
```
You should see output similar to:

```output
mysql  Ver 8.0.46-0ubuntu0.24.04.4 for Linux on aarch64 ((Ubuntu))
```
## Access MySQL shell

After confirming that MySQL is running, the next step is to log in to the MySQL monitor (shell). It is the command-line interface used to interact with the database server for administrative tasks such as creating users, managing databases, and tuning configurations.

```console
sudo mysql
```
The `mysql>` prompt indicates that you are in the MySQL interactive shell. Run `EXIT;` to return to your VM terminal before continuing.

## Create a new user

Using the root account for everyday database tasks isn't recommended because it exposes your system to unnecessary risks. Instead, create dedicated users with only the privileges they need for their roles.

To get started, access the MySQL shell:

```console
sudo mysql
```

Inside the MySQL shell, create a new user:

```sql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'MyStrongPassword!';
GRANT ALL PRIVILEGES ON baseline_test.* TO 'admin'@'localhost';
GRANT ALL PRIVILEGES ON benchmark_db.* TO 'admin'@'localhost';
EXIT;
```

Replace `MyStrongPassword!` with a strong password of your choice.
These grants let `admin` create and manage the two tutorial databases without global administrative privileges. `CREATE USER` and `GRANT` take effect immediately.

## Verify access with new user

After creating a new MySQL user, test the login. This confirms that the account is configured correctly and can authenticate with the MySQL server.

Run the following command for user `admin`:

```console
mysql -u admin -p
```
Enter the password you created in the previous step. A `mysql>` prompt confirms successful authentication. Run `EXIT;` to return to your VM terminal.

The MySQL installation is complete. You can now proceed with baseline testing of MySQL in the next section.
