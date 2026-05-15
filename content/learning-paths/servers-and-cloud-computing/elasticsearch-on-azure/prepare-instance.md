---
title: Install Elasticsearch and ESRally on the Cobalt 100 virtual machine instance

weight: 4

layout: "learningpathall"
---

## Set up the virtual machine for Elasticsearch and ESRally

In this section, you'll prepare your Cobalt 100 virtual machine for Elasticsearch and ESRally. After installing the base packages, you'll install Elasticsearch and the benchmarking tool.

### Install dependencies on virtual machine

Start by updating the package index and installing the system dependencies. This includes `openjdk-21-jdk`, which Elasticsearch requires, and `apt-transport-https`, `ca-certificates`, and `software-properties-common`, which are needed to add external package repositories in the next step:

```bash
sudo apt update
sudo apt install -y build-essential net-tools curl wget python3-dev python3-venv python3-pip openjdk-21-jdk apt-transport-https ca-certificates curl software-properties-common 
sudo apt -y dist-upgrade
sudo apt -y autoremove
sudo apt -y autoclean
```

ESRally requires Python 3.10. Ubuntu 24.04 ships with Python 3.12 by default, which ESRally doesn't support. The `deadsnakes` PPA provides older Python versions for Ubuntu that you can use to install Python 3.10 alongside the system default without replacing it.

Add the deadsnakes PPA and install Python 3.10:

```bash
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.10-dev python3.10 python3.10-venv
```

Create a dedicated virtual environment for ESRally named `rally` using Python 3.10. Then, add two lines to `.bashrc` so both the virtual environment and the `JAVA21_HOME` variable are available in every new shell session. ESRally uses `JAVA21_HOME` to locate the correct JDK at runtime:

```bash
python3.10 -m venv rally
echo "source $HOME/rally/bin/activate" >> $HOME/.bashrc
echo "export JAVA21_HOME=/usr/lib/jvm/java-21-openjdk-arm64" >> $HOME/.bashrc
```

Reload your shell configuration to activate the `rally` virtual environment and set the `JAVA21_HOME` environment variable:

```bash
source $HOME/.bashrc
```

Confirm that Java is available and points to OpenJDK 21:

```bash
which java
java --version
```

The output is similar to:

```output
/usr/bin/java

openjdk 21.0.10 2026-01-20
OpenJDK Runtime Environment (build 21.0.10+7-Ubuntu-124.04)
OpenJDK 64-Bit Server VM (build 21.0.10+7-Ubuntu-124.04, mixed mode, sharing)
```

### Install Elasticsearch and ESRally

Add the Elastic APT package repository and install Elasticsearch. The first command imports the Elastic GPG signing key so `apt` can verify package authenticity. The second registers the Elastic 9.x repository. After installation, enable the service so it starts automatically on reboot, then start it:

```bash
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/9.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-9.x.list
sudo apt update && sudo apt install elasticsearch -y
sudo systemctl enable elasticsearch
sudo systemctl start elasticsearch
```

With Elasticsearch running, install ESRally into the active `rally` virtual environment:

```bash
pip install --upgrade pip
pip install esrally
```

Confirm that Elasticsearch is installed and running:

```bash
sudo systemctl status elasticsearch
```

The output is similar to:

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

Confirm that ESRally is installed:

```bash
esrally --version
```

The output is similar to:

```output
esrally 2.13.0
```

Note the Elasticsearch version your instance is running, as you'll need it in the next section. Elasticsearch 9.x enables HTTPS and authentication by default, so a plain HTTP request to `localhost:9200` returns an HTML redirect rather than JSON. Check the installed package version instead:

```bash
dpkg -l elasticsearch | grep elasticsearch
```

The output shows the installed package version in the third column. For example:

```output
ii  elasticsearch  9.4.0  arm64  Distributed RESTful search engine built for the cloud
```

Use this version value for the `--distribution-version` flag when running ESRally.

## What you've learned and what's next

You've now prepared the virtual machine and installed both Elasticsearch and ESRally. 

Next, you'll run the geonames benchmark and review the baseline performance results.
