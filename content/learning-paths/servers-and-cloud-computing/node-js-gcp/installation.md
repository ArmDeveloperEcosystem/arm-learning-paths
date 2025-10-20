---
title: Install Node.js Using Node Version Manager
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Node.js with Node Version Manager (NVM)
This guide walks you through installing **NodeJS** via the Node Version Manager (NVM).  NVM is a powerful tool that allows users to specify which version of **NodeJS** that they want to use. NVM will then download and install the requested vesion using the **NodeJS** official packages. 

### 1. Install Node Version Manager (NVM)
First, we will run this command to download and install NVM into our VM instance:

```console
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Next, we have to activate NVM in our terminal shell.  We can manually activate our current shell via copy and paste of the following into the shell:

```console
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

You should be able to confirm that NVM is available by typing:

```console
nvm --version
```

### 2. Install NodeJS
Now that NVM is installed, we simply type the following commands in our shell to download and install **NodeJS**: 

```console
nvm install v24
nvm use v24
```

Additionally, we can add this command to the bottom of our $HOME/.bashrc file:

```console
echo 'nvm use v24' >> ~/.bashrc
```

### 3. Verify Installation
Check that Node.js and npm (Node’s package manager) are installed correctly.

You should be able to confirm that **NodeJS** is now installed and available!

```console
node --version
npm --version
```

You should see an output similar to:
```output
v24.10.0
11.6.1
```

Node.js installation is complete. You can now proceed with the baseline testing.
