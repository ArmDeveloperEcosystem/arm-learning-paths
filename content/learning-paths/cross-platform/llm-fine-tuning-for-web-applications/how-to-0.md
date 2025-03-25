---
title: Create a Jupyter notebook on an Arm server
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You can use a Jupyter notebook running on an Arm server for fine-tuning LLMs.

## Install a Jupyter notebook on an Arm server

Follow the steps below to create, configure, and connect to a Jupyter notebook on an Arm server. 

### Before you begin

You need an Arm server or other Arm Linux machine to run a Jupyter notebook. 

You can use an AWS Graviton4 `r8g.16xlarge` instance to perform fine tuning or a similar Arm server. Refer to [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/) for more information about cloud service providers offering Arm-based instances. 

The instructions are provided for Ubuntu 24.04, but other Linux distributions are possible. 

Make sure you can connect by SSH to the Arm server. 

Jupyter notebooks run on port 8888. You can open this port or use SSH port forwarding. 

Install the required software:

```console
sudo apt-get update
sudo apt-get install python3-pip python3-venv python3-dev python-is-python3 -y
```

Create a Python virtual environment by running:

```bash
python -m venv venv
source venv/bin/activate
```

In your virtual environment, install Jupyter:

```bash
pip install jupyter
```

### Configure a Jupyter notebook

Generate a Jupyter configuration file with the command below:

```console
jupyter notebook --generate-config
```

Use a text edit to edit the configuration file:

```console
~/.jupyter/jupyter_notebook_config.py
```
    
Modify the configuration file to include the lines below:

```console
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.NotebookApp.notebook_dir = '/home/ubuntu'
```

### Open port 888 

To access the Jupyter notebook you need to either open port 8888 in the security group or use SSH port forwarding. 

If you are using a cloud instance, add an incoming rule for TCP access to port 8888 from your IP address. Refer to the cloud service provider documentation for security groups. 

If you want to use SSH port forwarding, you can connect to the Arm server using:

```console
ssh -i <ssh-private-key> -L 8888:localhost:8888 <user>@<ip-address> 
```

### Start Jupyter notebook

Start the Jupyter notebook using:

```console
jupyter notebook
```

URLs are printed in the terminal output. 

If you are using SSH port forwarding copy the URL with 127.0.0.0 and if you are opening port 8888 copy the URL with the IP address of the Arm server.

### Connect to the Jupyter notebook using your browser

Open a web browser on your local machine and paste the copied URL into the address bar and press enter.

You are now connected to Jupyter notebook running on your Arm server.

Click `File` from the menu and navigate to `New` select `Notebook`. For the kernel select `Python 3`.

You see an empty cell in your notebook, and you are ready to use your Jupyter notebook for fine-tuning LLMs.
