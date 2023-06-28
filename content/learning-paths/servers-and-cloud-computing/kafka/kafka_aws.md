---
# User change
title: "Deploy Cluster Automatically (AWS)"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy a cluster automatically on AWS

You can deploy three node Zookeeper cluster, three node Kafka cluster and one client on AWS Graviton processors using Terraform and Ansible. 
 
If you are new to Terraform, you should look at [Automate AWS EC2 instance creation using Terraform](/learning-paths/servers-and-cloud-computing/aws-terraform/terraform/) before starting this Learning Path.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path. 

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools. 

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

Before you begin you will also need:
- An AWS access key ID and secret access key. 
- An SSH key pair

The instructions to create the keys are below.

## Generate the SSH key-pair

Generate the SSH key-pair (public key, private key) using `ssh-keygen` to use for AWS EC2 access. To generate the key-pair, follow this [guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Acquire AWS Access Credentials

The installation of Terraform on your desktop or laptop needs to communicate with AWS. Thus, Terraform needs to be able to authenticate with AWS. For authentication, generate access keys (access key ID and secret access key). These access keys are used by Terraform for making programmatic calls to AWS via the AWS CLI.

To generate and configure the Access key ID and Secret access key, follow this [guide](/install-guides/aws_access_keys).

## Create seven AWS EC2 instance using Terraform

Using a text editor, save the code below in a file called `main.tf`.

Scroll down to see the information you need to change in `main.tf`.
```console
provider "aws" {
  region = "us-east-2"
}

resource "aws_instance" "KAFKA_TEST" {
  count           = "7"
  ami             = "ami-0ca2eafa23bc3dd01"
  instance_type   = "t4g.small"
  security_groups = [aws_security_group.Terraformsecurity.name]
  key_name        = aws_key_pair.deployer.key_name
  tags = {
    Name = "KAFKA_TEST"
  }
}

resource "aws_default_vpc" "main" {
  tags = {
    Name = "main"
  }
}

resource "aws_security_group" "Terraformsecurity" {
  name        = "Terraformsecurity"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_default_vpc.main.id
  ingress {
    description = "TLS from VPC"
    from_port   = 2181
    to_port     = 2181
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "TLS from VPC"
    from_port   = 9092
    to_port     = 9092
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "TLS from VPC"
    from_port   = 2888
    to_port     = 2888
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "TLS from VPC"
    from_port   = 3888
    to_port     = 3888
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "TLS from VPC"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "Terraformsecurity"
  }
}

resource "local_file" "inventory" {
  depends_on = [aws_instance.KAFKA_TEST]
  filename   = "/tmp/inventory"
  content    = <<EOF
[zookeeper1]
${aws_instance.KAFKA_TEST[0].public_ip}
[zookeeper2]
${aws_instance.KAFKA_TEST[1].public_ip}
[zookeeper3]
${aws_instance.KAFKA_TEST[2].public_ip}
[kafka1]
${aws_instance.KAFKA_TEST[3].public_ip}
[kafka2]
${aws_instance.KAFKA_TEST[4].public_ip}
[kafka3]
${aws_instance.KAFKA_TEST[5].public_ip}
[client]
${aws_instance.KAFKA_TEST[6].public_ip}
[all:vars]
ansible_connection=ssh
ansible_user=ubuntu
zk_1_ip=${aws_instance.KAFKA_TEST[0].public_ip}
zk_2_ip=${aws_instance.KAFKA_TEST[1].public_ip}
zk_3_ip=${aws_instance.KAFKA_TEST[2].public_ip}
kf_1_ip=${aws_instance.KAFKA_TEST[3].public_ip}
kf_2_ip=${aws_instance.KAFKA_TEST[4].public_ip}
kf_3_ip=${aws_instance.KAFKA_TEST[5].public_ip}
                EOF
}

resource "aws_key_pair" "deployer" {
  key_name   = "id_rsa"
  public_key = file("~/.ssh/id_rsa.pub")
}
```
Make the changes listed below in **main.tf** to match your account settings.

1. In the `provider` section, update all 3 values to use your preferred AWS region and your AWS access key ID and secret access key.

2. (optional) In the `aws_instance` section, change the ami value to your preferred Linux distribution. The AMI ID for Ubuntu 22.04 on Arm in the us-east-2 region is `ami-0ca2eafa23bc3dd01 ` No change is needed if you want to use Ubuntu AMI in us-east-2. The AMI ID values are region specific and need to be changed if you use another AWS region. Use the AWS EC2 console to find an AMI ID or refer to [Find a Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html).

{{% notice Note %}}
The instance type is t4g.small. This is an Arm-based instance and requires an Arm Linux distribution.
{{% /notice %}}

The inventory file is automatically generated and does not need to be changed.

## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the dependencies required for AWS.
```console
terraform init
```    
The output should be similar to:
```output
root@ip-172-31-38-39:/home/ubuntu/kf# terraform init

Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Reusing previous version of hashicorp/local from the dependency lock file
- Using previously-installed hashicorp/aws v4.61.0
- Using previously-installed hashicorp/local v2.4.0

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

### Apply the Terraform execution plan

Run `terraform apply` to apply the execution plan and create all AWS resources: 
```console
terraform apply
```
Answer `yes` to the prompt to confirm you want to create AWS resources. 

The output should be similar to:
```output
local_file.inventory: Creating...
local_file.inventory: Creation complete after 0s [id=034d680c1738cdf217a5ad90885e6ec262470127]

Apply complete! Resources: 11 added, 0 changed, 0 destroyed.
```
## Configure three node Zookeeper cluster through Ansible

Using a text editor, save the code below in a file called `zookeeper_cluster.yaml`. It will install the Zookeeper and the required dependencies. This is the YAML file for the Ansible playbook.
```console
- hosts: zookeeper1, zookeeper2, zookeeper3
  become: True    
  tasks:
  - name: Update machines and install Java, Zookeeper
    shell: |
           apt update
           apt install -y default-jdk
           mkdir Zookeeper_node
           cd Zookeeper_node/ && wget https://dlcdn.apache.org/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz && tar -xzf apache-zookeeper-3.8.0-bin.tar.gz && cd apache-zookeeper-3.8.0-bin

  - name: On zookeeper1 instance create Zookeeper directory
    when: "'zookeeper1' in group_names"
    shell: mkdir /tmp/zookeeper && echo 1 >> /tmp/zookeeper/myid
    
  - name: On zookeeper1 instance setup confiuration for Zookeeper cluster
    when: "'zookeeper1' in group_names"
    copy:
      dest: "/home/ubuntu/Zookeeper_node/apache-zookeeper-3.8.0-bin/conf/zoo.cfg"
      content: |
        tickTime=2000
        dataDir=/tmp/zookeeper
        clientPort=2181
        maxClientCnxns=60
        initLimit=10
        syncLimit=5
        4lw.commands.whitelist=*
        server.1=0.0.0.0:2888:3888
        server.2={{zk_2_ip}}:2888:3888
        server.3={{zk_3_ip}}:2888:3888

  - name: On zookeeper2 instance create Zookeeper directory
    when: "'zookeeper2' in group_names"
    shell: mkdir /tmp/zookeeper && echo 2 >> /tmp/zookeeper/myid
    
  - name: On zookeeper1 instance setup confiuration for Zookeeper cluster
    when: "'zookeeper2' in group_names"
    copy:
      dest: "/home/ubuntu/Zookeeper_node/apache-zookeeper-3.8.0-bin/conf/zoo.cfg"
      content: |
        tickTime=2000
        dataDir=/tmp/zookeeper
        clientPort=2181
        maxClientCnxns=60
        initLimit=10
        syncLimit=5
        4lw.commands.whitelist=*
        server.1={{zk_1_ip}}:2888:3888
        server.2=0.0.0.0:2888:3888
        server.3={{zk_3_ip}}:2888:3888
        
  - name: On zookeeper3 instance create Zookeeper directory
    when: "'zookeeper3' in group_names"
    shell: mkdir /tmp/zookeeper && echo 3 >> /tmp/zookeeper/myid
    
  - name: On zookeeper3 instance setup confiuration for Zookeeper cluster
    when: "'zookeeper3' in group_names"
    copy:
      dest: "/home/ubuntu/Zookeeper_node/apache-zookeeper-3.8.0-bin/conf/zoo.cfg"
      content: |
        tickTime=2000
        dataDir=/tmp/zookeeper
        clientPort=2181
        maxClientCnxns=60
        initLimit=10
        syncLimit=5
        4lw.commands.whitelist=*
        server.1={{zk_1_ip}}:2888:3888
        server.2={{zk_2_ip}}:2888:3888
        server.3=0.0.0.0:2888:3888
        
  - name: Start Zookeeper server
    command: /home/ubuntu/Zookeeper_node/apache-zookeeper-3.8.0-bin/bin/zkServer.sh start       
```

### Ansible Commands

Run the playbook using the  `ansible-playbook` command:
```console
ansible-playbook zookeeper_cluster.yaml -i /tmp/inventory
```
Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:
```output
root@ip-172-31-38-39:/home/ubuntu/kf# ansible-playbook zookeeper_cluster.yaml -i /tmp/inventory

PLAY [zookeeper1, zookeeper2, zookeeper3] ***********************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
The authenticity of host '18.222.137.38 (18.222.137.38)' can't be established.
ED25519 key fingerprint is SHA256:078u3zYJtAMqmZTWI1qGLNTdlp/iDtqgxnrUV7NLjNA.
This key is not known by any other names
The authenticity of host '18.117.144.56 (18.117.144.56)' can't be established.
ED25519 key fingerprint is SHA256:pdmVviF1LTQOrM5t0Pp3yrsL+M3DsJdbYjGtmb5h44c.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? ok: [3.140.201.79]
yes
ok: [18.222.137.38]
yes
ok: [18.117.144.56]

TASK [Update machines and install Java, Zookeeper] **************************************************************************************
changed: [18.222.137.38]
changed: [3.140.201.79]
changed: [18.117.144.56]

TASK [On zookeeper1 instance create Zookeeper directory] ********************************************************************************
skipping: [18.117.144.56]
skipping: [3.140.201.79]
changed: [18.222.137.38]

TASK [On zookeeper1 instance setup confiuration for Zookeeper cluster] ******************************************************************
skipping: [18.117.144.56]
skipping: [3.140.201.79]
changed: [18.222.137.38]

TASK [On zookeeper2 instance create Zookeeper directory] ********************************************************************************
skipping: [18.222.137.38]
skipping: [3.140.201.79]
changed: [18.117.144.56]

TASK [On zookeeper1 instance setup confiuration for Zookeeper cluster] ******************************************************************
skipping: [18.222.137.38]
skipping: [3.140.201.79]
changed: [18.117.144.56]

TASK [On zookeeper3 instance create Zookeeper directory] ********************************************************************************
skipping: [18.222.137.38]
skipping: [18.117.144.56]
changed: [3.140.201.79]

TASK [On zookeeper3 instance setup confiuration for Zookeeper cluster] ******************************************************************
skipping: [18.222.137.38]
skipping: [18.117.144.56]
changed: [3.140.201.79]

TASK [Start Zookeeper server] ***********************************************************************************************************
changed: [18.222.137.38]
changed: [18.117.144.56]
changed: [3.140.201.79]

PLAY RECAP ******************************************************************************************************************************
18.117.144.56              : ok=5    changed=4    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0
18.222.137.38              : ok=5    changed=4    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0
3.140.201.79               : ok=5    changed=4    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0
```
## Configure three node Kafka cluster through Ansible

Using a text editor, save the code below in a file called `kafka_cluster.yaml`. It will install the Kafka and the required dependencies. This is the YAML file for the Ansible playbook.
```console
- hosts: kafka1, kafka2, kafka3
  become: True    
  tasks:
  - name: Update machines and install Java, Kafka
    shell: |
           apt update
           apt install -y default-jdk
           mkdir kafka_node
           cd kafka_node/ && wget https://dlcdn.apache.org/kafka/3.2.3/kafka_2.13-3.2.3.tgz && tar -xzf kafka_2.13-3.2.3.tgz && cd kafka_2.13-3.2.3

  - name: On all kafka instances create log directory
    shell: mkdir /tmp/kafka-logs

  - name: On kafka1 instance update broker id
    when: "'kafka1' in group_names"
    lineinfile:
      path: /home/ubuntu/kafka_node/kafka_2.13-3.2.3/config/server.properties
      regexp: '^(.*)broker.id(.*)$'
      line: 'broker.id=1'
      backrefs: yes

  - name: On kafka2 instance update broker id
    when: "'kafka2' in group_names"
    lineinfile:
      path: /home/ubuntu/kafka_node/kafka_2.13-3.2.3/config/server.properties
      regexp: '^(.*)broker.id(.*)$'
      line: 'broker.id=2'
      backrefs: yes

  - name: On kafka3 instance update broker id
    when: "'kafka3' in group_names"
    lineinfile:
      path: /home/ubuntu/kafka_node/kafka_2.13-3.2.3/config/server.properties
      regexp: '^(.*)broker.id(.*)$'
      line: 'broker.id=3'
      backrefs: yes

  - name: On all kafka instance uncomment listeners
    lineinfile:
      path: /home/ubuntu/kafka_node/kafka_2.13-3.2.3/config/server.properties
      regexp: '^(.*)#listeners=PLAINTEXT://:9092(.*)$'
      line: 'listeners=PLAINTEXT://:9092'
      backrefs: yes
 
  - name: On all kafka instance update zookeeper.connect
    lineinfile:
      path: /home/ubuntu/kafka_node/kafka_2.13-3.2.3/config/server.properties
      regexp: '^(.*)zookeeper.connect=localhost:2181(.*)$'
      line: 'zookeeper.connect={{zk_1_ip}}:2181,{{zk_2_ip}}:2181,{{zk_3_ip}}:2181'
      backrefs: yes
      
  - name: Start kafka_server
    command: /home/ubuntu/kafka_node/kafka_2.13-3.2.3/bin/kafka-server-start.sh /home/ubuntu/kafka_node/kafka_2.13-3.2.3/config/server.properties        
```

### Ansible Commands

Run the playbook using the  `ansible-playbook` command:
```console
ansible-playbook kafka_cluster.yaml -i /tmp/inventory
```
Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:
```output
root@ip-172-31-38-39:/home/ubuntu/kf# ansible-playbook kafka_cluster.yaml -i /tmp/inventory

PLAY [kafka1, kafka2, kafka3] ***********************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
The authenticity of host '3.19.64.64 (3.19.64.64)' can't be established.
ED25519 key fingerprint is SHA256:3qKhnEt0Js8LL67OAcIDOsTx8qQGRlQlsJ8ZZX9Fz1E.
This key is not known by any other names
The authenticity of host '3.133.93.119 (3.133.93.119)' can't be established.
ED25519 key fingerprint is SHA256:rI7qWf3fDGIkB+EqrPCa18maKeVck951WklPmeAQoXc.
This key is not known by any other names
The authenticity of host '18.222.0.36 (18.222.0.36)' can't be established.
ED25519 key fingerprint is SHA256:+Gv6OFuOLlaIIiQRtRccpmA5vA0wC7SqriwyudB8K34.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [3.19.64.64]
yes
ok: [3.133.93.119]
yes
ok: [18.222.0.36]

TASK [Update machines and install Java, Kafka] ******************************************************************************************
changed: [18.222.0.36]
changed: [3.133.93.119]
changed: [3.19.64.64]

TASK [On kafka1 instance create log directory] ******************************************************************************************
skipping: [3.133.93.119]
skipping: [18.222.0.36]
changed: [3.19.64.64]

TASK [On kafka1 instance update broker id] **********************************************************************************************
skipping: [3.133.93.119]
skipping: [18.222.0.36]
changed: [3.19.64.64]

TASK [On kafka1 instance uncomment listeners] *******************************************************************************************
skipping: [3.133.93.119]
skipping: [18.222.0.36]
changed: [3.19.64.64]

TASK [On kafka1 instance update zookeeper.connect] **************************************************************************************
skipping: [3.133.93.119]
skipping: [18.222.0.36]
changed: [3.19.64.64]

TASK [On kafka2 instance create log directory] ******************************************************************************************
skipping: [3.19.64.64]
skipping: [18.222.0.36]
changed: [3.133.93.119]

TASK [On kafka2 instance update broker id] **********************************************************************************************
skipping: [3.19.64.64]
skipping: [18.222.0.36]
changed: [3.133.93.119]

TASK [On kafka2 instance uncomment listeners] *******************************************************************************************
skipping: [3.19.64.64]
skipping: [18.222.0.36]
changed: [3.133.93.119]

TASK [On kafka2 instance update zookeeper.connect] **************************************************************************************
skipping: [3.19.64.64]
skipping: [18.222.0.36]
changed: [3.133.93.119]

TASK [On kafka3 instance create log directory] ******************************************************************************************
skipping: [3.19.64.64]
skipping: [3.133.93.119]
changed: [18.222.0.36]

TASK [On kafka3 instance update broker id] **********************************************************************************************
skipping: [3.19.64.64]
skipping: [3.133.93.119]
changed: [18.222.0.36]

TASK [On kafka3 instance uncomment listeners] *******************************************************************************************
skipping: [3.19.64.64]
skipping: [3.133.93.119]
changed: [18.222.0.36]

TASK [On kafka3 instance update zookeeper.connect] **************************************************************************************
skipping: [3.19.64.64]
skipping: [3.133.93.119]
changed: [18.222.0.36]

TASK [Start kafka_server] ***************************************************************************************************************
```
Kafka servers are started on all the three instances and keep the terminal open. Now open a new terminal on the same machine and configure the client through Ansible.

After successfully setting up a 3 node Kafka cluster, we can verify it by creating a topic and storing the events. Follow the steps below to create a topic, write some events into the topic, and then read the events.

## Configure client through Ansible

Using a text editor, save the code below in a file called `client.yaml`. It will install the Kafka and the required dependencies. This is the YAML file for the Ansible playbook.
```console
- hosts: client
  become: true
  tasks:
  - name: Update machines and install Java, Kafka
    shell: |
           apt update
           apt install -y default-jdk
           mkdir kafka_node
           cd kafka_node/ && wget https://dlcdn.apache.org/kafka/3.2.3/kafka_2.13-3.2.3.tgz && tar -xzf kafka_2.13-3.2.3.tgz && cd kafka_2.13-3.2.3
           
  - name: Create a topic
    command: /home/ubuntu/kafka_node/kafka_2.13-3.2.3/bin/kafka-topics.sh --create --topic test-topic --bootstrap-server {{kf_1_ip}}:9092,{{kf_2_ip}}:9092,{{kf_3_ip}}:9092 --replication-factor 3 --partitions 64
```

### Ansible Commands

Run the playbook using the `ansible-playbook` command:
```console
ansible-playbook client.yaml -i /tmp/inventory
```
Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:
```output
root@ip-172-31-38-39:/home/ubuntu/kf# ansible-playbook client.yaml -i /tmp/inventory

PLAY [client] ***************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
The authenticity of host '18.216.149.104 (18.216.149.104)' can't be established.
ED25519 key fingerprint is SHA256:fPpeusF+HmRq8+Rc3erkW7/Je6gTZy/c1iA0eF4Iguo.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [18.216.149.104]

TASK [Update machines and install Java, Kafka] ******************************************************************************************
changed: [18.216.149.104]

TASK [Create a topic] *******************************************************************************************************************
changed: [18.216.149.104]

PLAY RECAP ******************************************************************************************************************************
18.216.149.104             : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
## Describe the topic created:

To describe the topic created ssh on the client instance and run the following command.
```console
ssh ubuntu@client_ip
cd kafka_node/kafka_2.13-3.2.3
./bin/kafka-topics.sh --topic test-topic --bootstrap-server kf_1_ip:9092,kf_2_ip:9092,kf_3_ip:9092 --describe
```
Replace the `client_ip`, `kf_1_ip`, `kf_2_ip`, `kf_3_ip` with the IP of client, kafka1, kafka2 and kafka3 respectively generated in inventory file present at location `/tmp/inventory`.

The output should be similar to:
```output
ubuntu@ip-172-31-31-117:~/kafka_node/kafka_2.13-3.2.3$ ./bin/kafka-topics.sh --topic test-topic --bootstrap-server 3.19.64.64:9092,3.133.93.119:9092,18.222.0.36:9092 --describe
Topic: test-topic       TopicId: J_G3hNvpTjSXoQ4-gyPKYg PartitionCount: 64      ReplicationFactor: 3    Configs: segment.bytes=1073741824
        Topic: test-topic       Partition: 0    Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 1    Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 2    Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 3    Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
        Topic: test-topic       Partition: 4    Leader: 3       Replicas: 3,2,1 Isr: 3,2,1
        Topic: test-topic       Partition: 5    Leader: 1       Replicas: 1,3,2 Isr: 1,3,2
        Topic: test-topic       Partition: 6    Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 7    Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 8    Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 9    Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
        Topic: test-topic       Partition: 10   Leader: 3       Replicas: 3,2,1 Isr: 3,2,1
        Topic: test-topic       Partition: 11   Leader: 1       Replicas: 1,3,2 Isr: 1,3,2
        Topic: test-topic       Partition: 12   Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 13   Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 14   Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 15   Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
        Topic: test-topic       Partition: 16   Leader: 3       Replicas: 3,2,1 Isr: 3,2,1
        Topic: test-topic       Partition: 17   Leader: 1       Replicas: 1,3,2 Isr: 1,3,2
        Topic: test-topic       Partition: 18   Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 19   Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 20   Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 21   Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
        Topic: test-topic       Partition: 22   Leader: 3       Replicas: 3,2,1 Isr: 3,2,1
        Topic: test-topic       Partition: 23   Leader: 1       Replicas: 1,3,2 Isr: 1,3,2
        Topic: test-topic       Partition: 24   Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 25   Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 26   Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 27   Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
        Topic: test-topic       Partition: 28   Leader: 3       Replicas: 3,2,1 Isr: 3,2,1
        Topic: test-topic       Partition: 29   Leader: 1       Replicas: 1,3,2 Isr: 1,3,2
        Topic: test-topic       Partition: 30   Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 31   Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 32   Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 33   Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
        Topic: test-topic       Partition: 34   Leader: 3       Replicas: 3,2,1 Isr: 3,2,1
        Topic: test-topic       Partition: 35   Leader: 1       Replicas: 1,3,2 Isr: 1,3,2
        Topic: test-topic       Partition: 36   Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 37   Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 38   Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 39   Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
        Topic: test-topic       Partition: 40   Leader: 3       Replicas: 3,2,1 Isr: 3,2,1
        Topic: test-topic       Partition: 41   Leader: 1       Replicas: 1,3,2 Isr: 1,3,2
        Topic: test-topic       Partition: 42   Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 43   Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 44   Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 45   Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
        Topic: test-topic       Partition: 46   Leader: 3       Replicas: 3,2,1 Isr: 3,2,1
        Topic: test-topic       Partition: 47   Leader: 1       Replicas: 1,3,2 Isr: 1,3,2
        Topic: test-topic       Partition: 48   Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 49   Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 50   Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 51   Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
        Topic: test-topic       Partition: 52   Leader: 3       Replicas: 3,2,1 Isr: 3,2,1
        Topic: test-topic       Partition: 53   Leader: 1       Replicas: 1,3,2 Isr: 1,3,2
        Topic: test-topic       Partition: 54   Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 55   Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 56   Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 57   Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
        Topic: test-topic       Partition: 58   Leader: 3       Replicas: 3,2,1 Isr: 3,2,1
        Topic: test-topic       Partition: 59   Leader: 1       Replicas: 1,3,2 Isr: 1,3,2
        Topic: test-topic       Partition: 60   Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
        Topic: test-topic       Partition: 61   Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 62   Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 63   Leader: 2       Replicas: 2,1,3 Isr: 2,1,3
```
## Run the producer client to write events into the created topic:

Run the following command in the same client terminal and folder where the topic was created and replace `kf_1_ip`, `kf_2_ip`, `kf_3_ip` with the IP of kafka1, kafka2 and kafka3 respectively generated in inventory file present at location `/tmp/inventory`.
```console
./bin/kafka-console-producer.sh --topic test-topic --bootstrap-server kf_1_ip:9092,kf_2_ip:9092,kf_3_ip:9092
```
The output should be similar to:
```output
ubuntu@ip-172-31-31-117:~/kafka_node/kafka_2.13-3.2.3$ ./bin/kafka-console-producer.sh --topic test-topic --bootstrap-server 3.19.64.64:9092,3.133.93.119:9092,18.222.0.36:9092
>This is the first message written on producer
>
```
## Run the consumer client to read all the events created:

Open a new terminal on the client machine and run the consumer client using the following command.
```console
ssh ubuntu@client_ip
cd kafka_node/kafka_2.13-3.2.3
./bin/kafka-console-consumer.sh --topic test-topic --bootstrap-server kf_1_ip:9092,kf_2_ip:9092,kf_3_ip:9092
```
Replace the `client_ip`, `kf_1_ip`, `kf_2_ip`, `kf_3_ip` with the IP of client, kafka1, kafka2 and kafka3 respectively generated in inventory file present at location `/tmp/inventory`.

The output should be similar to:
```output
ubuntu@ip-172-31-31-117:~/kafka_node/kafka_2.13-3.2.3$ ./bin/kafka-console-consumer.sh --topic test-topic --bootstrap-server 3.19.64.64:9092,3.133.93.119:9092,18.222.0.36:9092
This is the first message written on producer
```
Write a message into the producer client terminal and press enter. You should see the same message appear on consumer client terminal. 

