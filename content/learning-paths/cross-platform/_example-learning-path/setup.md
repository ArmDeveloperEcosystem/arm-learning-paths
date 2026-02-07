---
# User change
title: "Learning Path setup"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Set up a computer

There are multiple ways to set up a computer for Learning Path creation. 

Three tools are mandatory:
- A text editor to create and modify markdown files
- [Hugo](https://gohugo.io/) static site generator to review content 
- Git to access the repository and submit contributions

## Fork the repository

You will need a GitHub account to continue. [Sign up](https://github.com/signup) for a new account or use your existing account.

No matter which computer option you choose, the first step is to fork the GitHub repository into your own GitHub account. 

1. Go to the [repository in GitHub](https://github.com/ArmDeveloperEcosystem/arm-learning-paths) 
2. Click `Fork` in the top right area. 
3. Follow the prompts to create a new fork. 
This provides your own copy for you to make changes without impacting the main repository. 

## Set up a development machine 

Three possible ways to set up a development machine are covered below. 

Select **one** that works for you. Please share other ways that work for you

- A [local computer (Linux, macOS, or Windows)](#option-1-set-up-a-local-computer)
- A [remote Linux server](#option-2-set-up-a-remote-linux-server) via SSH (on your local network or from a Cloud Service Provider)

## Option 1: Set up a local computer

The first option is to install the required tools on your local computer. 

1. Install a text editor

Any text editor can be used to create and modify the project markdown files. Many developers use [Visual Studio Code](https://code.visualstudio.com/), but any text editor can be used. 

If you already have a text editor installed go to the next step.

2. Install Git

[Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) using the documentation for your operating system. 

3. Clone the project repository

Clone your fork of the repository to your local machine (substitute `<your-github-account-name>` in the command below). You can copy the path by visiting your fork in GitHub and clicking the Code button.

```bash
git clone https://github.com/<your-github-account-name>/arm-learning-paths
```

You now have a local copy of the repository on your computer. 

4. Install Hugo

Install Hugo so you can see how your changes look before submitting them for review. 

This enables you to run a local web server and see the content just how it will appear when published. 

The easiest way to download Hugo on Linux (Debian/Ubuntu) is using the package manager.

```bash
sudo apt install hugo
```
To install Hugo on macOS, first install Homebrew if it's not already installed, then use Homebrew to install Hugo:

```bash
brew install hugo
```

You can also download the latest version of Hugo for other operating systems from the [releases page](https://github.com/gohugoio/hugo/releases). Hugo works on all major operating systems and architectures. 

For even more ways to install Hugo [check the documentation](https://gohugo.io/getting-started/installing).

Check Hugo is installed correctly and check the version by running this command:

```bash
hugo version
```

Most recent versions of Hugo will work, but you may face errors if the version is too old. 

Navigate into the `arm-learning-paths` folder and run hugo to launch a development version of website on your machine.

```bash
cd arm-learning-paths
hugo server
```

Hugo server will print a message to connect to port 1313

```output
Web Server is available at //localhost:1313/ (bind address 127.0.0.1)
```

Open a browser and go to [http://localhost:1313](http://localhost:1313)

You are now ready to start developing content. The content creation process consists of editing the markdown files for Learning Paths and viewing the changes on your computer using Hugo. 

## Option 2: Set up a remote Linux server

The third option for Learning Path development is to use a remote Linux server, such as an AWS EC2 instance or other cloud virtual machine. The remote Linux server can also be on your local network.

Find the IP address or DNS name of the remote server and make sure you can SSH to the computer. 

Install the same tools as you would on the local computer setup above: 

- Text editor
- Git
- Hugo 

To access the Hugo server on the remote machine, use ssh port forwarding (use port 1313):

```bash
ssh -L 1313:localhost:1313 user@ip-address
```

Clone your fork of the repository to the remote Linux server (substitute your github account name in the command below):
```bash
git clone https://github.com/<your-github-account-name>/arm-learning-paths
```

There are a number of good options for text editors if you don't have a full Linux desktop available on the remote server.

To use Visual Studio Code in the browser on your remote Linux server check the install information for [OpenVSCode Server](/install-guides/openvscode-server/) and [VS Code Tunnels](/install-guides/vscode-tunnels/)

Navigate into the `arm-learning-paths` folder and run hugo to launch a
development version of website on your machine.

```bash
cd arm-learning-paths
hugo server
```

Hugo server will print a message to connect to port 1313

```output
Web Server is available at //localhost:1313/ (bind address 127.0.0.1)
```

Open a browser and go to [http://localhost:1313](http://localhost:1313)

You are now ready to edit markdown files and view the results on the Hugo server. 

{{% notice Note %}}

If your content is not updating/staging on your web browser after you save it correctly then please check the [Troubleshooting section](/learning-paths/cross-platform/_example-learning-path/appendix-5-troubleshooting/).

{{%/notice%}}

The next section will cover how to create and format Learning Paths. 
