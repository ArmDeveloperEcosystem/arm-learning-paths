---
# User change
title: "Install Redis in a multi-node configuration"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Install Redis in a multi-node configuration 

You can deploy Redis in a multi-node configuration on AWS Graviton processors using Terraform and Ansible. You will create three primary nodes and three replica nodes.

## Before you begin

You should have the prerequisite tools installed from the topic, [Install Redis on a single AWS Arm based instance](/learning-paths/server-and-cloud/redis/aws_deployment).

Use the same AWS access key ID and secret access key and the same SSH key pair.

## Create AWS EC2 instances using Terraform

Using a text editor, save the code below in a file called `main.tf`. You will create a security group that opens inbound port `22`(ssh). Also every Redis Cluster node requires two TCP connections open. The normal Redis TCP port used to serve clients, for example `6379` plus the port obtained by adding 10000 to the data port, so `16379` in the example.

Scroll down to see the information you need to change in `main.tf`.

```console
provider "aws" {
  region = "us-east-2"
  access_key  = "AXXXXXXXXXXXXXXXXXXX"
  secret_key   = "AXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
resource "aws_instance" "redis-deployment" {
  ami = "ami-0ca2eafa23bc3dd01"
  count = "6"
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
    description      = "Open port for Cluster bus"
    from_port        = 16379
    to_port          = 16379
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

resource "local_file" "inventory" {
    depends_on=[aws_instance.redis-deployment]
    filename = "(your_current_directory)/hosts"
    content = <<EOF
[redis]

${aws_instance.redis-deployment[0].public_dns}
${aws_instance.redis-deployment[1].public_dns}
${aws_instance.redis-deployment[2].public_dns}
${aws_instance.redis-deployment[3].public_dns}
${aws_instance.redis-deployment[4].public_dns}
${aws_instance.redis-deployment[5].public_dns}

[all:vars]
host_key_checking=false
ansible_connection=ssh
ansible_user=ubuntu
                EOF
}

resource "aws_key_pair" "deployer" {
        key_name   = "aws_key"
        public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC/GFk2t5I2WOGWIP11kk9+sS2hwb+SuZV8b6KAi8IPR50pDjBXtBBt/8Apl+cyTmUjIlVxnyV6rS4sGVdKLC7SDNU8nl1SfDuh1HJRtlbMu8k+OmA3i9T/rihz2Qs9htkbSkdZ3bADCd5tcregPIht1bdQkjFK5zpbmiNHqIC1KJYIKfiwHMCLt+3ZQWr8iw1G19hHLbfpvDr0H/ewlrpMNG3StJSo6E2Jec6NZ09takFMl0a2r9Cej3bSQz5TuDnxWFDm1xk2svLojROnNeSH2sVx6UoPDpt05eniqgpYdMysYzxeOwS+qMHzR2IV2+0UoDFMxgcSgnhM36qlSk7H ubuntu@ip-172-XX-XX-XX"
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

The output should be similar to:

```console
Apply complete! Resources: 9 added, 0 changed, 0 destroyed.
```

## Install Redis in a multi-node configuration through Ansible
Install the Redis and the required dependencies. 

Using a text editor, save the code below to in a file called `playbook.yaml`. This is the YAML file for the Ansible playbook. The following playbook contains a collection of tasks that install Redis in a multi-node configuration (3 primary and 3 replica nodes). 

```console
---
- name: Redis Cluster Install
  hosts: redis
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
         protected-mode no
         port 6379
         cluster-enabled yes
         cluster-config-file nodes.conf
         cluster-node-timeout 5000
         daemonize yes
         appendonly yes
      become_user: ubuntu
    - name: Stop redis-server
      shell: service redis-server stop
    - name: Start redis server with configuration files
      shell: redis-server redis.conf
      args:
        chdir: "/home/ubuntu/redis"
      become_user: ubuntu
```
**NOTE:-** Since the allocation of primary and replica nodes is random at the time of cluster creation, it is difficult to know which nodes are primary and which nodes are replica. Hence, for the multi-node configuration, we need to turn off **protected-mode**, which is enabled by default, so that we can connect to the primary and replica nodes. Also, the **bind address** is by default set to `127.0.0.1` due to which port 6379 becomes unavailable for binding with the public IP of the remote server. Thus, we set the bind configuration option to `0.0.0.0`.

### Ansible Commands

Substitute your private key name, and run the playbook using the  `ansible-playbook` command.

```console
ansible-playbook playbook.yaml -i hosts --key-file aws_key
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```console
PLAY [Redis Cluster Install] *************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
The authenticity of host 'ec2-13-58-162-195.us-east-2.compute.amazonaws.com (172.31.28.72)' can't be established.
ED25519 key fingerprint is SHA256:tr9tgt90kYwO0TTcqixWAL3FfpfxVHN2pEZlWevxp+g.
This key is not known by any other names
The authenticity of host 'ec2-18-217-125-204.us-east-2.compute.amazonaws.com (172.31.23.206)' can't be established.
ED25519 key fingerprint is SHA256:liR6mlOvk2hfxArrwNkYvrP9a6flWDE63rIYHUMol7s.
This key is not known by any other names
The authenticity of host 'ec2-3-142-240-147.us-east-2.compute.amazonaws.com (172.31.21.161)' can't be established.
ED25519 key fingerprint is SHA256:k0xJlAKunLQhmtQzay0D0i+XO8C9N8y1AxF4qnoKOxI.
This key is not known by any other names
The authenticity of host 'ec2-3-17-132-158.us-east-2.compute.amazonaws.com (172.31.30.32)' can't be established.
ED25519 key fingerprint is SHA256:Bvhc5zvHx4vl4Cnpz1VUgwE0WwSjnj8CSvHStiNwnA0.
This key is not known by any other names
The authenticity of host 'ec2-3-23-96-163.us-east-2.compute.amazonaws.com (172.31.27.229)' can't be established.
ED25519 key fingerprint is SHA256:Z5XybSrhgkScd1P0eeFMVWgFVm8to+771TAaRyvBVlY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
yes
yes
ok: [ec2-13-58-162-195.us-east-2.compute.amazonaws.com]
The authenticity of host 'ec2-3-17-161-89.us-east-2.compute.amazonaws.com (172.31.23.88)' can't be established.
ED25519 key fingerprint is SHA256:8dKquVwCvXEjCpJ6oOJ4OScISz4UwYlkFJRWJBt11ZM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
yes
ok: [ec2-18-217-125-204.us-east-2.compute.amazonaws.com]
yes
ok: [ec2-3-142-240-147.us-east-2.compute.amazonaws.com]
ok: [ec2-3-17-132-158.us-east-2.compute.amazonaws.com]
ok: [ec2-3-23-96-163.us-east-2.compute.amazonaws.com]
ok: [ec2-3-17-161-89.us-east-2.compute.amazonaws.com]

TASK [Update the Machine and install dependencies] ***************************************************************************************************************
changed: [ec2-3-23-96-163.us-east-2.compute.amazonaws.com]
changed: [ec2-18-217-125-204.us-east-2.compute.amazonaws.com]
changed: [ec2-3-17-132-158.us-east-2.compute.amazonaws.com]
changed: [ec2-13-58-162-195.us-east-2.compute.amazonaws.com]
changed: [ec2-3-142-240-147.us-east-2.compute.amazonaws.com]
changed: [ec2-3-17-161-89.us-east-2.compute.amazonaws.com]

TASK [Create directories] ****************************************************************************************************************************************
changed: [ec2-3-142-240-147.us-east-2.compute.amazonaws.com]
changed: [ec2-3-23-96-163.us-east-2.compute.amazonaws.com]
changed: [ec2-18-217-125-204.us-east-2.compute.amazonaws.com]
changed: [ec2-13-58-162-195.us-east-2.compute.amazonaws.com]
changed: [ec2-3-17-132-158.us-east-2.compute.amazonaws.com]
changed: [ec2-3-17-161-89.us-east-2.compute.amazonaws.com]

TASK [Create configuration files] ********************************************************************************************************************************
changed: [ec2-3-17-132-158.us-east-2.compute.amazonaws.com]
changed: [ec2-3-142-240-147.us-east-2.compute.amazonaws.com]
changed: [ec2-13-58-162-195.us-east-2.compute.amazonaws.com]
changed: [ec2-3-23-96-163.us-east-2.compute.amazonaws.com]
changed: [ec2-18-217-125-204.us-east-2.compute.amazonaws.com]
changed: [ec2-3-17-161-89.us-east-2.compute.amazonaws.com]

TASK [Stop redis-server] *****************************************************************************************************************************************
changed: [ec2-3-17-132-158.us-east-2.compute.amazonaws.com]
changed: [ec2-13-58-162-195.us-east-2.compute.amazonaws.com]
changed: [ec2-3-142-240-147.us-east-2.compute.amazonaws.com]
changed: [ec2-18-217-125-204.us-east-2.compute.amazonaws.com]
changed: [ec2-3-23-96-163.us-east-2.compute.amazonaws.com]
changed: [ec2-3-17-161-89.us-east-2.compute.amazonaws.com]

TASK [Start redis server with configuration files] ***************************************************************************************************************
changed: [ec2-13-58-162-195.us-east-2.compute.amazonaws.com]
changed: [ec2-3-17-132-158.us-east-2.compute.amazonaws.com]
changed: [ec2-3-23-96-163.us-east-2.compute.amazonaws.com]
changed: [ec2-3-142-240-147.us-east-2.compute.amazonaws.com]
changed: [ec2-18-217-125-204.us-east-2.compute.amazonaws.com]
changed: [ec2-3-17-161-89.us-east-2.compute.amazonaws.com]

PLAY RECAP *******************************************************************************************************************************************************
ec2-13-58-162-195.us-east-2.compute.amazonaws.com : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ec2-18-217-125-204.us-east-2.compute.amazonaws.com : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ec2-3-142-240-147.us-east-2.compute.amazonaws.com : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ec2-3-17-132-158.us-east-2.compute.amazonaws.com : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ec2-3-17-161-89.us-east-2.compute.amazonaws.com : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ec2-3-23-96-163.us-east-2.compute.amazonaws.com : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Create a Redis cluster

After the Redis installation has been completed on all servers, lift the cluster up with the help of the following command.

```console
redis-cli --cluster create {redis-deployment[0].public_ip}:6379 {redis-deployment[1].public_ip}:6379 {redis-deployment[2].public_ip}:6379 {redis-deployment[3].public_ip}:6379 {redis-deployment[4].public_ip}:6379 {redis-deployment[5].public_ip}:6379 --cluster-replicas 1
```
Replace `redis-deployment[n].public_ip` with their respective values.

The output should be similar to:

```console
>>> Performing hash slots allocation on 6 nodes...
Master[0] -> Slots 0 - 5460
Master[1] -> Slots 5461 - 10922
Master[2] -> Slots 10923 - 16383
Adding replica ec2-3-142-208-82.us-east-2.compute.amazonaws.com:6379 to ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379
Adding replica ec2-52-15-94-91.us-east-2.compute.amazonaws.com:6379 to ec2-18-191-103-96.us-east-2.compute.amazonaws.com:6379
Adding replica ec2-3-133-91-199.us-east-2.compute.amazonaws.com:6379 to ec2-18-220-255-133.us-east-2.compute.amazonaws.com:6379
M: e01e0295b9e1e4129f86c33880f8eb5873c77f05 ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379
   slots:[0-5460] (5461 slots) master
M: a871235e3fc81a8feee28527c3ae1435d4f9a7f0 ec2-18-191-103-96.us-east-2.compute.amazonaws.com:6379
   slots:[5461-10922] (5462 slots) master
M: d8965922e7ec90de5e8218c136f2b744be4cb258 ec2-18-220-255-133.us-east-2.compute.amazonaws.com:6379
   slots:[10923-16383] (5461 slots) master
S: 54214adb94bd90ca4ca69d9ca1cf4469594b7b48 ec2-3-133-91-199.us-east-2.compute.amazonaws.com:6379
   replicates d8965922e7ec90de5e8218c136f2b744be4cb258
S: 0e088022aabf1d8eaa65fef9b87dd46a9434caf6 ec2-3-142-208-82.us-east-2.compute.amazonaws.com:6379
   replicates e01e0295b9e1e4129f86c33880f8eb5873c77f05
S: cadd3b1b0c3975726fbf9859105df8ef60b837d2 ec2-52-15-94-91.us-east-2.compute.amazonaws.com:6379
   replicates a871235e3fc81a8feee28527c3ae1435d4f9a7f0
Can I set the above configuration? (type 'yes' to accept): yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
...
>>> Performing Cluster Check (using node ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379)
M: e01e0295b9e1e4129f86c33880f8eb5873c77f05 ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379
   slots:[0-5460] (5461 slots) master
   1 additional replica(s)
M: a871235e3fc81a8feee28527c3ae1435d4f9a7f0 172.31.26.201:6379
   slots:[5461-10922] (5462 slots) master
   1 additional replica(s)
M: d8965922e7ec90de5e8218c136f2b744be4cb258 172.31.19.70:6379
   slots:[10923-16383] (5461 slots) master
   1 additional replica(s)
S: cadd3b1b0c3975726fbf9859105df8ef60b837d2 172.31.29.216:6379
   slots: (0 slots) slave
   replicates a871235e3fc81a8feee28527c3ae1435d4f9a7f0
S: 0e088022aabf1d8eaa65fef9b87dd46a9434caf6 172.31.26.125:6379
   slots: (0 slots) slave
   replicates e01e0295b9e1e4129f86c33880f8eb5873c77f05
S: 54214adb94bd90ca4ca69d9ca1cf4469594b7b48 172.31.22.1:6379
   slots: (0 slots) slave
   replicates d8965922e7ec90de5e8218c136f2b744be4cb258
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
```

## Status of the Redis Cluster

`cluster info` provides **info** style information about Redis Cluster vital parameters.
```console
redis-cli -c -h {redis-deployment[n].public_ip} -p 6379 cluster info
```
Replace `{redis-deployment[n].public_ip}` with the IP of any of the instances created.

The output should be similar to:

```console
cluster_state:ok
cluster_slots_assigned:16384
cluster_slots_ok:16384
cluster_slots_pfail:0
cluster_slots_fail:0
cluster_known_nodes:6
cluster_size:3
cluster_current_epoch:6
cluster_my_epoch:1
cluster_stats_messages_ping_sent:482
cluster_stats_messages_pong_sent:478
cluster_stats_messages_sent:960
cluster_stats_messages_ping_received:473
cluster_stats_messages_pong_received:482
cluster_stats_messages_meet_received:5
cluster_stats_messages_received:960
```

**cluster_state** is **ok** if the node is able to receive queries.

The `cluster nodes` command can be sent to any node in the cluster and provides the state of the cluster and the information for each node according to the local view the queried node has of the cluster.
```console
redis-cli -c -h {redis-deployment[n].public_ip} -p 6379 cluster nodes
```
The output should be similar to:

```console
a871235e3fc81a8feee28527c3ae1435d4f9a7f0 172.31.26.201:6379@16379 master - 0 1678791540000 2 connected 5461-10922
d8965922e7ec90de5e8218c136f2b744be4cb258 172.31.19.70:6379@16379 master - 0 1678791539596 3 connected 10923-16383
cadd3b1b0c3975726fbf9859105df8ef60b837d2 172.31.29.216:6379@16379 slave a871235e3fc81a8feee28527c3ae1435d4f9a7f0 0 1678791539000 6 connected
0e088022aabf1d8eaa65fef9b87dd46a9434caf6 172.31.26.125:6379@16379 slave e01e0295b9e1e4129f86c33880f8eb5873c77f05 0 1678791540800 5 connected
e01e0295b9e1e4129f86c33880f8eb5873c77f05 172.31.23.74:6379@16379 myself,master - 0 1678791539000 1 connected 0-5460
54214adb94bd90ca4ca69d9ca1cf4469594b7b48 172.31.22.1:6379@16379 slave d8965922e7ec90de5e8218c136f2b744be4cb258 0 1678791541300 4 connected
```

## Connecting to Redis cluster from local machine

Execute the steps below to connect to the remote Redis server from your local machine.
1. We need to install redis-tools to interact with redis-server.
```console
apt install redis-tools
```
2. Connect to redis-server through redis-cli.
```console
redis-cli -c -h <public-IP-address> -p 6379
```
The output will be:
```console
ubuntu@ip-172-31-38-39:~$ redis-cli -c -h ec2-18-117-150-63.us-east-2.compute.amazonaws.com -p 6379
ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379>
```
3. Try out commands in the redis-cli.              
The redis-cli will run in interactive mode. We can connect to any of the nodes, the command will get redirected to primary node.
```console
ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379> ping
PONG
ec2-18-117-150-63.us-east-2.compute.amazonaws.com:6379> set name test
-> Redirected to slot [5798] located at 172.31.26.201:6379
OK
172.31.26.201:6379> get name
"test"
172.31.26.201:6379> set ans sample
-> Redirected to slot [2698] located at 172.31.23.74:6379
OK
172.31.23.74:6379> get ans
"sample"
172.31.23.74:6379> get name
-> Redirected to slot [5798] located at 172.31.26.201:6379
"test"
172.31.26.201:6379>
```
You have successfully installed Redis in a multi-node configuration.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

