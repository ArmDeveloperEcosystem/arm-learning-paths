---
title: Prepare the on-premises source instance

weight: 4

layout: "learningpathall"
---

### Introduction

In this section, you'll install required tools on the on-premises x64 simulator and prepare it as the MySQL migration source.

### Install MySQL Server "on-prem"

Update the on-premises instance and install MySQL server and sysbench. In an SSH session to the on-premises instance, run:

```bash
sudo apt update
sudo apt -y dist-upgrade
sudo apt install -y build-essential net-tools curl wget python3-dev python3-venv python3-pip openjdk-21-jdk apt-transport-https ca-certificates curl software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.10-dev python3.10 python3.10-venv
python3.10 -m venv LnS
echo "source $HOME/LnS/bin/activate" >> $HOME/.bashrc
sudo reboot
```

Log back in to the x64 on-premises server and continue:

```bash
sudo apt install -y mysql-server
sudo apt install -y sysbench
echo innodb_buffer_pool_size = 16G | sudo tee -a /etc/mysql/mysql.conf.d/mysqld.cnf > /dev/null
echo innodb_flush_log_at_trx_commit = 2  | sudo tee -a  /etc/mysql/mysql.conf.d/mysqld.cnf > /dev/null
echo innodb_log_file_size = 3G  | sudo tee -a   /etc/mysql/mysql.conf.d/mysqld.cnf > /dev/null
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
sudo reboot
```

### Confirm mysql client, terraform and Azure CLI are operational

Open a new SSH shell into your x64 VM and confirm the MySQL client is available:

```bash
sudo mysql --version
```

Should see output similar to:

```output
mysql  Ver 8.0.45-0ubuntu0.24.04.1 for Linux on x86_64 ((Ubuntu))
```

Confirm the Terraform installation version:

```bash
terraform --version
```

Should see output similar to:

```output
Terraform v1.14.8
on linux_amd64
```

Confirm the Azure CLI installation version:

```bash
az --version
```

Should see output similar to:

```output
azure-cli                         2.85.0

core                              2.85.0
telemetry                          1.1.0

Dependencies:
msal                              1.35.1
azure-mgmt-resource               24.0.0

Python location '/opt/az/bin/python3'
Config directory '/home/douans01/.azure'
Extensions directory '/home/douans01/.azure/cliextensions'

Python (Linux) 3.13.11 (main, Mar 31 2026, 07:18:38) [GCC 13.3.0]

Legal docs and information: aka.ms/AzureCliLegal


Your CLI is up-to-date.
```

### Create an admin user in MySQL that has a password 

With the MySQL client, enter mysql:

```bash
sudo mysql
```

At the MySQL prompt, run the following commands (example password: `SuperStrongPassword`):

```mysql
CREATE USER 'admin'@'%' IDENTIFIED BY 'SuperStrongPassword';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
quit;
```

Now confirm that you can log into the MySQL environment with that admin user:

```bash
mysql -u admin -p
```

After you supply the password, you should see the MySQL prompt. Type `quit;` to exit.

### Install the sysbench test database as our sample DB to "migrate"

Clone the asset repo:

```bash
cd $HOME
git clone https://github.com/DougAnsonAustinTX/lift-n-shift-assets
```

Once downloaded, restore the DB as follows:

```bash
cd lift-n-shift-assets/testdb
gunzip -c testdb.sql.gz | mysql -h localhost -u admin -p
```

### What we learned and what's next

You prepared the on-premises x64 simulator with MySQL, sysbench, Terraform, and Azure CLI. In the next section, you'll run the migration workflow to move `testdb` to an Arm-based Azure VM.