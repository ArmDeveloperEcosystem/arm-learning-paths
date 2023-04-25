---
# User change
title: "Deploy MySQL via Docker"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Install MySQL in a Docker container 

You can deploy MySQL in a Docker container using Ansible. 

## Before you begin

For this section you will need a computer which has [Ansible](/install-guides/ansible/) installed. You can use the same SSH key pair. You also need a cloud instance or VM, or a physical machine with Ubuntu installed, running and ready to deploy MySQL.
 
 
## Deploy a MySQL container using Ansible

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. If you are new to Docker, consider reviewing [Learn how to use Docker](/learning-paths/cross-platform/docker/).

To run Ansible, you can use an Ansible playbook. The playbook uses the `community.docker` collection to deploy MySQL in a container.

The playbook maps the container port to the host port, which is `3306`. 

1. Use a text editor to add the contents below to a new file named `playbook.yml`.

```yml
---
- hosts: all
  remote_user: root
  become: true
  tasks:
    - name: Update the Machine and Install dependencies
      shell: |
             apt-get update -y
             apt-get -y install mysql-client
             apt-get install docker.io -y
             usermod -aG docker ubuntu
             apt-get -y install python3-pip
             pip3 install PyMySQL
             pip3 install docker
      become: true
    - name: Reset ssh connection for changes to take effect
      meta: "reset_connection"
    - name: Log into DockerHub
      community.docker.docker_login:
        username: {{dockerhub_uname}}
        password: {{dockerhub_pass}}
    - name: Deploy MySQL docker container
      docker_container:
        image: mysql:latest
        name: mysql_test
        state: started
        ports:
          - "3306:3306"
        pull: true
        volumes:
         - "db_data:/var/lib/mysql:rw"
         - "/tmp:/tmp:rw"
        restart: true
        env:
          MYSQL_ROOT_PASSWORD: {{your_MySQL_password}}
          MYSQL_USER: local_us
          MYSQL_PASSWORD: Password1
          MYSQL_DATABASE: arm_test

```

2. Edit `playbook.yml` to use your values 

Replace **{{your_MySQL_password}}** with your own password. 

Also, replace **{{dockerhub_uname}}** and **{{dockerhub_pass}}** with your [Docker Hub](https://hub.docker.com/) credentials.

3. Create a `inventory.txt` file and copy the contents given below:
```ansible
[all]
ansible-target1 ansible_connection=ssh ansible_host={{public_ip of VM where MySQL to be deployed}} ansible_user={{user_of VM where MySQL to be deployed}}
```
4. Edit `inventory.txt` to use your values 

Replace **{{public_ip of VM where MySQL to be deployed}}** and **{{user_of VM where MySQL to be deployed}}** with your own values.

{{% notice Note %}} You can use your own inventory file. {{% /notice %}}

### Ansible Commands

1. Run the playbook using the `ansible-playbook` command:

```bash
ansible-playbook playbook.yaml -i {your_inventory_file_location}
```

2. Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [all] *****************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
The authenticity of host '3.143.18.13 (3.143.18.13)' can't be established.
ED25519 key fingerprint is SHA256:uWZgVeACoIxRDQ9TrqbpnjUz14x57jTca6iASH3gU7M.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [ansible-target1]

TASK [Update the Machine and install docker dependencies] *************************************************************************************************************
changed: [ansible-target1]

TASK [Reset ssh connection for changes to take effect] ****************************************************************************************************************

TASK [Log into DockerHub] *********************************************************************************************************************************************
changed: [ansible-target1]

TASK [Deploy MySQL docker containere] *******************************************************************************************************************************
changed: [ansible-target1]

PLAY RECAP ************************************************************************************************************************************************************
ansible-target1            : ok=3    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Connect to Database using your local machine

You can use the instructions from the previous topic to [connect to the database](/learning-paths/server-and-cloud/mysql/ec2_deployment#connect-to-database-using-ec2-instance) and confirm the Docker container deployment is working. 
