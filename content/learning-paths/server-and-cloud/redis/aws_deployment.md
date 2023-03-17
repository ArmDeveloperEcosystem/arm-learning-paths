---
# User change
title: "Install Redis on a single AWS Arm based instance"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Install Redis on a single AWS Arm based instance 

You can deploy Redis on AWS Graviton processors using Terraform and Ansible. 

In this topic, you will deploy Redis on a single AWS EC2 instance, and in the next topic you will deploy Redis on a single Azure instance. 

If you are new to Terraform, you should look at [Automate AWS EC2 instance creation using Terraform](/learning-paths/server-and-cloud/aws/terraform/) before starting this Learning Path.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path. 

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools. 

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

Before you begin you will also need:
- An AWS access key ID and secret access key
- An SSH key pair

The instructions to create the keys are below.

### Generate AWS access keys 

Terraform requires AWS authentication to create AWS resources. You can generate access keys (access key ID and secret access key) to perform authentication. Terraform uses the access keys to make calls to AWS using the AWS CLI. 

To generate an access key and secret access key, follow the [steps from the Terraform Learning Path](/learning-paths/server-and-cloud/aws/terraform#generate-access-keys-access-key-id-and-secret-access-key).

### Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for AWS EC2 access. 

```console
ssh-keygen -f aws_key -t rsa -b 2048 -P ""
```

You should now have your AWS access keys and your SSH keys in the current directory.

## Create an AWS EC2 instance using Terraform

Using a text editor, save the code below in a file called `main.tf`.

Scroll down to see the information you need to change in `main.tf`.

```console
provider "aws" {
  region = "us-east-2"
  access_key  = "AXXXXXXXXXXXXXXXXXXX"
  secret_key   = "AAXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
resource "aws_instance" "redis-deployment" {
  ami = "ami-0ca2eafa23bc3dd01"
  instance_type = "t4g.small"
  key_name= "aws_key"
  vpc_security_group_ids = [aws_security_group.main.id]
}

resource "aws_security_group" "main" {
  name        = "main"
  description = "Allow TLS inbound traffic"

  ingress {
    description      = "Open redis connection port"
    from_port        = 6379
    to_port          = 6379
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  ingress {
    description      = "Allow ssh to instance"
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
}

output "Master_public_IP" {
  value = [aws_instance.redis-deployment.public_ip]
}

resource "local_file" "inventory" {
    depends_on=[aws_instance.redis-deployment]
    filename = "(your_current_directory)/hosts"
    content = <<EOF
[all]
ansible-target1 ansible_connection=ssh ansible_host=${aws_instance.redis-deployment.public_dns} ansible_user=ubuntu
                EOF
}

resource "aws_key_pair" "deployer" {
        key_name   = "aws_key"
        public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCUZXm6T6JTQBuxw7aFaH6gmxDnjSOnHbrI59nf+YCHPqIHMlGaxWw0/xlaJiJynjOt67Zjeu1wNPifh2tzdN3UUD7eUFSGcLQaCFBDorDzfZpz4wLDguRuOngnXw+2Z3Iihy2rCH+5CIP2nCBZ+LuZuZ0oUd9rbGy6pb2gLmF89GYzs2RGG+bFaRR/3n3zR5ehgCYzJjFGzI8HrvyBlFFDgLqvI2KwcHwU2iHjjhAt54XzJ1oqevRGBiET/8RVsLNu+6UCHW6HE9r+T5yQZH50nYkSl/QKlxBj0tGHXAahhOBpk0ukwUlfbGcK6SVXmqtZaOuMNlNvssbocdg1KwOH ubuntu@ip-172-31-XXXX-XXXX"
}
```
Make the changes listed below in `main.tf` to match your account settings.

1. In the `provider` section, update all 3 values to use your preferred AWS region and your AWS access key ID and secret access key.

2. (optional) In the `aws_instance` section, change the ami value to your preferred Linux distribution. The AMI ID for Ubuntu 22.04 on Arm is `ami-0ca2eafa23bc3dd01`. No change is needed if you want to use Ubuntu AMI. 

{{% notice Note %}}
The instance type is t4g.small. This an an Arm-based instance and requires an Arm Linux distribution.
{{% /notice %}}

3. In the `aws_key_pair` section, change the `public_key` value to match your SSH key. Copy and paste the contents of your `aws_key.pub` file to the `public_key` string. Make sure the string is a single line in the text file.

4. In the `local_file` section, change the `filename` to be the path to your current directory.

The hosts file is automatically generated and does not need to be changed, change the path to the location of the hosts file.


## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the dependencies required for AWS.

```console
terraform init
```
    
The output should be similar to:

```console
Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/local...
- Finding latest version of hashicorp/aws...
- Installing hashicorp/local v2.4.0...
- Installed hashicorp/local v2.4.0 (signed by HashiCorp)
- Installing hashicorp/aws v4.58.0...
- Installed hashicorp/aws v4.58.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

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

The public IP address will be different, but the output should be similar to:

```console
Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

Master_public_IP = [
  "3.135.226.118",
]
```

## Configure Redis through Ansible
Install the Redis and the required dependencies. 

Using a text editor, save the code below to in a file called `playbook.yaml`. This is the YAML file for the Ansible playbook. 

```console
---
- hosts: all
  become: true
  become_user: root
  remote_user: ubuntu

  tasks:
    - name: Update the Machine and install dependencies
      shell: |
             apt-get update -y
             curl -fsSL "https://packages.redis.io/gpg" | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
             echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" |  tee /etc/apt/sources.list.d/redis.list
             apt install -y redis-tools redis
    - name: Create directories
      file:
        path: "/home/ubuntu/redis"
        state: directory
      become_user: ubuntu
    - name: Create configuration files
      copy:
        dest: "/home/ubuntu/redis/redis.conf"
        content: |
          bind 0.0.0.0
          port 6379
          protected-mode yes
          cluster-enabled no
          daemonize yes
          appendonly no
      become_user: ubuntu
    - name: Stop redis-server
      shell: service redis-server stop
    - name: Start redis server with configuration files
      shell: redis-server redis.conf
      args:
        chdir: "/home/ubuntu/redis"
      become_user: ubuntu
    - name: Set Authentication password
      shell: redis-cli -p 6379 CONFIG SET requirepass "{password}"
      become_user: ubuntu
```
Replace `{password}` with your value.

### Ansible Commands

Substitute your private key name, and run the playbook using the  `ansible-playbook` command.

```console
ansible-playbook playbook.yaml -i hosts --key-file aws_key
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```console
PLAY [all] *****************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
The authenticity of host 'ec2-3-135-226-118.us-east-2.compute.amazonaws.com (172.31.30.40)' can't be established.
ED25519 key fingerprint is SHA256:uWZgVeACoIxRDQ9TrqbpnjUz14x57jTca6iASH3gU7M.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [ansible-target1]

TASK [Update the Machine and install dependencies] *************************************************************************************************************
changed: [ansible-target1]

TASK [Create directories] **************************************************************************************************************************************
changed: [ansible-target1]

TASK [Create configuration files] ******************************************************************************************************************************
changed: [ansible-target1]

TASK [Stop redis-server] ***************************************************************************************************************************************
changed: [ansible-target1]

TASK [Start redis server with configuration files] *************************************************************************************************************
changed: [ansible-target1]

TASK [Set Authentication password] *****************************************************************************************************************************
changed: [ansible-target1]

PLAY RECAP *****************************************************************************************************************************************************
ansible-target1            : ok=7    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Connecting to the Redis server from local machine

Execute the steps below to connect to the remote Redis server from your local machine.
1. We need to install redis-tools to interact with redis-server.
```console
apt install redis-tools
```
2. Connect to redis-server through redis-cli.
```console
redis-cli -h <public-IP-address> -p 6379
```
The output will be:
```console
ubuntu@ip-172-31-38-39:~$ redis-cli -h 172.31.30.40 -p 6379
172.31.30.40:6379> 
```
3. Authorize Redis with the password set by us in playbook.yaml file.
```console
172.31.30.40:6379> ping
(error) NOAUTH Authentication required.
172.31.30.40:6379> AUTH 123456789
OK
172.31.30.40:6379> ping
PONG
```
4. Try out commands in the redis-cli.
```console
172.31.30.40:6379> set name test
OK
172.31.30.40:6379> get name
"test"
172.31.30.40:6379>
```
You have successfully installed Redis on an AWS EC2 instance running Graviton processors.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

Continue the Learning Path to deploy Redis on a single Azure instance.

