---
title: Perform the lift-and-shift migration into Azure cloud

weight: 5

layout: "learningpathall"
---

### Introduction

In this section, you'll use the lift-and-shift scripts to migrate MySQL from your on-premises x64 simulator to an Arm-based Azure VM.

### Download the lift-n-shift script set

Open an SSH shell into your on-premises instance and go to the asset repository you already downloaded:

```bash
cd $HOME/lift-n-shift-assets
```

### Configure the lift-n-shift script

Run the following script to create an SSH key pair. Press Enter when prompted for a passphrase:

```bash
scripts/create_ssh_key.sh
```

You should get a key that looks something like this:

```output
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDczfgUuS4pnNSXnNeK4lRR+CcmxCH+/Vl+aP9dhtGYX7DEVrWrKy9Hq7AKs3y1AUyW85MGBJEkgy8WQZui6T92UNZz+MGVoKm/++SyO/
....
tH33RAoBg2q3mJJgOCqCQ8k5kfAww== azureuser@YOUR_X64_ON_PREM_HOST
```

Save this key. You will use it in the next step.

Create a copy of the terraform.tfvars.example to terraform.tfvars:

```bash
cp terraform.tfvars.example terraform.tfvars
```

In an editor, open `terraform.tfvars` and make the following edits:

```edit
location              = "eastus2"
prefix                = "mysql-migrate"

source_mysql_database = "testdb"

admin_username        = "azureadmin"
ssh_public_key        = "RSA_KEY_GOES_HERE"

allowed_ssh_cidr      = "YOUR_PUBLIC_IP/32"
allowed_mysql_cidr    = "YOUR_PUBLIC_IP/32"

allow_mysql_inbound = true
vm_size         = "Standard_E4pds_v6"
os_disk_size_gb = 48

tags = {
  environment = "prod"
  application = "testdb-migration"
  owner       = "admin"
  managed_by  = "terraform"
}
```

You need to edit:
1. `location` with the Azure region you want to use.
2. `prefix` to match your naming preference.
3. `RSA_KEY_GOES_HERE` with the SSH public key created above. Make sure to include the `ssh-rsa` keyword as well within the RSA Key.
4. `YOUR_PUBLIC_IP` with the public IP address of your on-premises x64 instance.

You can leave the remaining values unchanged for this tutorial.

### Log into Azure with the CLI

On the on-premises SSH shell, run:

```bash
az login
```

And follow the prompts to log into your Azure account. 

### Start the migration

On the on-premises SSH shell, run:

```bash
scripts/migrate.sh testdb
```

This starts migration of the local `testdb` database into the Arm-based VM you configured in `terraform.tfvars`.

Assuming no errors in the tfvars config file, eventually you will receive a prompt:

```output
Migrating local DB: testdb to Cloud...
Creating Cloud VM...
Cloud VM created.
Backing up the local DB testdb...
Enter password:
```

Supply the password you set for the local MySQL `admin` user in the previous section. 

```output
Migrating local DB: testdb to Cloud...
Creating Cloud VM...
Cloud VM created.
Backing up the local DB testdb...
Enter password: 
```

You'll now be prompted for password again. Follow the detailed steps below to fetch this password.

```output
Restoring local DB testdb onto the Cloud VM: Admin: admin IP: 20.98.229.225
You will need to open a second window and ssh into the VM and then look in /root for the password
Enter password:
```

To retrieve this password:

1. Open another shell into your on-premises x64 instance.
2. In that shell, check `$HOME/.ssh` and note the SSH private key filename ending in `rsa`.
3. In the Azure portal, locate your new Arm-based VM under **Virtual Machines**.
4. Record the VM public IP address.
5. Back in the second on-premises shell, run the following command with your key filename and VM IP:


```bash
ssh -i $HOME/.ssh/YOUR_RSA_FILENAME azureadmin@YOUR_ARM_BASED_VM_PUBLIC_IP_ADDRESS
```

You should now have a shell on the Arm-based Azure VM. In that shell, run:

```bash
sudo su - 
cat /root/mysql_root_password.txt
```

This is the required password. Supply it in your first SSH session on the on-premises host and let the script continue:

```output
Migrating local DB: testdb to Cloud...
Creating Cloud VM...
Cloud VM created.
Backing up the local DB testdb...
Enter password: 
Restoring local DB testdb onto the Cloud VM: Admin: admin IP: 20.98.229.225
You will need to open a second window and ssh into the VM and then look in /root for the password
Enter password: 
```

{{% notice Note %}}
The original script may time out waiting for this second password. If it does, right in that same shell, type the following replacing YOUR_ARM_BASED_VM_PUBLIC_IP_ADDRESS with the public IP address of your newly created Arm-based VM:

```bash
 gunzip -c testdb.sql.gz | mysql -h YOUR_ARM_BASED_VM_PUBLIC_IP_ADDRESS -u admin -p 
```

You will be prompted again for the second password you retrieved previously. Enter it to complete the migration.
{{% /notice %}}

At this point, your on-premises MySQL database (`testdb`) has been migrated to a new Arm-based VM in Azure.

### What we learned and what's next

This script and procedure migrates a MySQL database from an on-premises x64 source to an Arm-based Azure VM. Your `testdb` database is now ready for benchmarking with sysbench in the target environment.