---
title: Install Elasticsearch and ESRally on the Cobalt 100 virtual machine instance

weight: 4

layout: "learningpathall"
---

## Introduction

In this section, you prepare your Cobalt 100 virtual machine for Elasticsearch and ESRally. After the base packages are installed, you install Elasticsearch and the benchmarking tool.

## Prepare the virtual machine

Start by updating the virtual machine and installing required dependencies.

```bash
sudo apt update
sudo apt install -y build-essential net-tools curl wget python3-dev python3-venv python3-pip openjdk-21-jdk apt-transport-https ca-certificates curl software-properties-common 
sudo apt -y dist-upgrade
sudo apt -y autoremove
sudo apt -y autoclean
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.10-dev python3.10 python3.10-venv
python3.10 -m venv rally
echo "source $HOME/rally/bin/activate" >> $HOME/.bashrc
echo "export JAVA21_HOME=/usr/lib/jvm/java-21-openjdk-arm64" >> $HOME/.bashrc
sudo reboot
```

Open a new SSH shell and confirm that Java is available and points to OpenJDK 21.

```bash
which java
java --version
```

Output should be similar to:

```output
/usr/bin/java

openjdk 21.0.10 2026-01-20
OpenJDK Runtime Environment (build 21.0.10+7-Ubuntu-124.04)
OpenJDK 64-Bit Server VM (build 21.0.10+7-Ubuntu-124.04, mixed mode, sharing)
```

## Install Elasticsearch and ESRally

Now install Elasticsearch from the official package repository, then install ESRally into the virtual environment.

```bash
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/9.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-9.x.list
sudo apt update && sudo apt install elasticsearch -y
sudo systemctl enable elasticsearch
sudo systemctl start elasticsearch
pip install --upgrade pip
pip install esrally
```

Confirm that Elasticsearch is installed and running.

```bash
sudo systemctl status elasticsearch
```

Output should be similar to:

```output
elasticsearch.service - Elasticsearch
     Loaded: loaded (/usr/lib/systemd/system/elasticsearch.service; enabled; preset: enabled)
     Active: active (running) since Thu 2026-04-23 15:18:13 UTC; 2min 3s ago
       Docs: https://www.elastic.co
   Main PID: 722 (java)
      Tasks: 92 (limit: 38379)
     Memory: 16.5G (peak: 16.5G)
        CPU: 43.282s
     CGroup: /system.slice/elasticsearch.service
```

Confirm that ESRally is installed.

```bash
esrally --version
```

Output should be similar to:

```output
esrally 2.13.0
```

## What you've learned and what's next

In this section, you prepared the VM and installed both Elasticsearch and ESRally. In the next section, you will run the geonames benchmark and review the baseline performance results.
