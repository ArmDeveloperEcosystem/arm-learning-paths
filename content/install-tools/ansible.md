---
additional_search_terms:
- Ansible
layout: installtoolsall
minutes_to_complete: 10
multi_install: false
multitool_install_part: false
official_docs: https://docs.ansible.com/ansible/latest/index.html
test_images:
- ubuntu:latest
test_maintenance: false
title: Ansible
author_primary: Jason Andrews
tool_install: true
weight: 1
---

Ansible is an open source, command-line IT automation software application written in Python. It can configure systems, deploy software, and orchestrate advanced workflows to support application deployment, system updates, and more.

Ansible command-line tools can be installed on a variety of Linux distributions. 

[General installation information](https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html) is available which covers all supported operating systems, but it doesn't talk about Arm. 

## Introduction

This article provides a quick solution to install the Ansible command line tools, such as `ansible-playbook` for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```console
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## Download and Install

The easiest way to install the latest version of Ansible for Ubuntu on Arm is to use the PPA (personal package archive).

To enable the PPA and install Ansible run the commands:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y
```

Confirm the Ansible command line tools are installed by running: 

```bash { target="ubuntu:latest" }
ansible-playbook --version
```

The output should be similar to:

```console
ansible-playbook [core 2.14.3]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/ubuntu/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  ansible collection location = /home/ubuntu/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/bin/ansible-playbook
  python version = 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] (/usr/bin/python3)
  jinja version = 3.0.3
  libyaml = True
```

The Ansible command line tools are now ready to use.