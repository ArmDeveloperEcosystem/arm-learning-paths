---
title: Install CircleCI Machine Runner on SUSE Arm
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install CircleCI Machine Runner on SUSE Arm64

This section explains how to install and configure the CircleCI Machine Runner on a SUSE Linux Arm64 virtual machine running on Google Cloud C4A (Axion). By installing this runner, you enable your own VM to execute CircleCI Arm-native jobs.

### Add CircleCI Package Repository

Because SUSE is an RPM-based Linux distribution, you first need to add the official CircleCI package repository from PackageCloud:

```console
curl -s https://packagecloud.io/install/repositories/circleci/runner/script.rpm.sh?any=true | sudo bash
```
This command automatically detects your distribution and adds the appropriate repository configuration for SUSE-based systems.

### Install the CircleCI Runner
Before installation, create a symbolic link for `adduser`. The CircleCI runner installation script is primarily built for Debian/Ubuntu systems, which use the `adduser` command. SUSE uses `useradd` instead.

```bash
sudo ln -s /usr/sbin/useradd /usr/sbin/adduser
```

Now install the CircleCI runner package:

```console
sudo zypper install -y circleci-runner
```
### Prepare User and Permissions
Before starting the CircleCI runner, ensure the correct user, group, and directory permissions are in place. These steps ensure the runner operates securely and has proper access to its configuration and work directories.

Create CircleCI system user and group: 
```bash
sudo useradd -m -r circleci
sudo groupadd --system circleci
```
Set up CircleCI directories and permissions:
```bash
sudo mkdir -p /var/lib/circleci
sudo chown -R circleci:circleci /var/lib/circleci
sudo chown -R circleci:circleci /etc/circleci-runner
```
Reload systemd and restart the runner service:
```bash
sudo systemctl daemon-reload
sudo systemctl restart circleci-runner
```
Verify service status:
```bash
sudo systemctl status circleci-runner
```

### Configure the Runner Token

Now, configure the authentication token that connects your runner to CircleCI.
Use the token generated earlier from your Resource Class in the CircleCI dashboard.

```console
export RUNNER_AUTH_TOKEN="AUTH_TOKEN "
sudo sed -i "s/<< AUTH_TOKEN >>/$RUNNER_AUTH_TOKEN/g" /etc/circleci-runner/circleci-runner-config.yaml
```
Replace AUTH_TOKEN with the actual token copied from the CircleCI dashboard.

### Enable and Start the Runner
Enable the CircleCI service to start automatically at boot, then start and verify the runner:

```console
sudo systemctl enable circleci-runner
sudo systemctl start circleci-runner
sudo systemctl status circleci-runner
```

If the status shows active (running), your runner is successfully installed and connected to CircleCI.

```output
● circleci-runner.service - Run the CircleCI self-hosted runner agent
     Loaded: loaded (/usr/lib/systemd/system/circleci-runner.service; enabled; vendor preset: disabled)
     Active: active (running) since Thu 2025-10-09 08:59:40 UTC; 2h 29min ago
   Main PID: 10150 (circleci-runner)
      Tasks: 9
        CPU: 1.524s
     CGroup: /system.slice/circleci-runner.service
             └─ 10150 /usr/bin/circleci-runner machine -c /etc/circleci-runner/circleci-runner-config.yaml

Oct 09 11:12:11 lpprojectsusearm64 circleci-runner[10150]: 11:12:11 7927c 72.264ms worker loop: claim:  app.backoff_ms=5000 a>
Oct 09 11:15:03 lpprojectsusearm64 circleci-runner[10150]: 11:15:03 6f109 46.059ms POST /api/v3/runner/claim app.loop_name=cl>
Oct 09 11:15:03 lpprojectsusearm64 circleci-runner[10150]: 11:15:03 6f109 46.119ms claim app.loop_name=claim:  mode=agent res>
Oct 09 11:15:03 lpprojectsusearm64 circleci-runner[10150]: 11:15:03 6f109 46.144ms worker loop: claim:  app.backoff_ms=5000 a>
```
You can also confirm that your runner is connected and active by visiting the Self-Hosted Runners page in the CircleCI web dashboard.

![Self-Hosted Runners alt-text#center](images/dashboard.png "Figure 1: Self-Hosted Runners ")
