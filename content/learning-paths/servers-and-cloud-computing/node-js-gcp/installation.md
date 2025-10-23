---
title: Install Node.js using Node Version Manager
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
This section shows you how to install Node.js using Node Version Manager (NVM). NVM lets you choose which Node.js version to use and handles the download and installation for you. You’ll use official Node.js packages, making setup simple and reliable.

## Install Node Version Manager (NVM)
First, use this command to download and install NVM into your VM instance:

```console
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Next, activate Node Version Manager (NVM) in your current terminal session. Copy and paste the following commands into your shell to load NVM and enable command completion:

```console
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

This step ensures that NVM commands are available in your shell. If you open a new terminal, repeat these commands or add them to your `~/.bashrc` file for automatic activation:

```console
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

Confirm that NVM is available by typing:

```console
nvm --version
```

## Install Node.js
Now that NVM is installed, download and install Node.js: 

```console
nvm install v24
nvm use v24
```

Next, add this command to the bottom of your $HOME/.bashrc file:

```console
echo 'nvm use v24' >> ~/.bashrc
```

## Verify installation
Check that Node.js and npm (Node.js package manager) are installed correctly by using this command that confirms that **NodeJS** is installed and available:

```console
node --version
npm --version
```

You should see an output similar to:
```output
v24.10.0
11.6.1
```

This shows you that Node.js installation is complete. You can now proceed with the baseline testing.

## What you've accomplished

You've successfully provisioned a Google Axion C4A Arm virtual machine running SUSE Linux Enterprise Server. You're now ready to install Node.js and deploy your workloads on Arm.


