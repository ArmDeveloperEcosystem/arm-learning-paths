---
title: Install CircleCI Machine Runner on SUSE Arm
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install CircleCI Machine Runner on SUSE Arm64

This section shows you how to install and set up the CircleCI Machine Runner on a SUSE Linux Arm64 virtual machine in Google Cloud C4A (Axion). After completing these steps, your VM can run CircleCI jobs natively on Arm.
## Add the CircleCI package repository

Before you install the CircleCI runner, add the official CircleCI package repository to your SUSE system. This step ensures you get the latest Arm64 RPM package.

Run this command to set up the repository:

```bash
curl -s https://packagecloud.io/install/repositories/circleci/runner/script.rpm.sh?any=true | sudo bash
```

This script detects your SUSE version and configures the correct repository automatically.
## Install the CircleCI runner

Before installing, create a symbolic link for `adduser`. The CircleCI runner installation script expects `adduser`, which is standard on Debian/Ubuntu, but SUSE uses `useradd`. This link ensures compatibility:

```bash
sudo ln -s /usr/sbin/useradd /usr/sbin/adduser
```

Next, install the CircleCI runner package using `zypper`:

```bash
sudo zypper install -y circleci-runner
```

## Prepare user and permissions
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
### Configure the runner authentication token

To connect your runner to CircleCI, you need to add the authentication token from your resource class.

First, export your token as an environment variable. Replace `AUTH_TOKEN` with the value you copied from the CircleCI dashboard:

```bash
export RUNNER_AUTH_TOKEN="your_actual_token_here"
```

Next, update the runner configuration file to use your token:

```bash
sudo sed -i "s/<< AUTH_TOKEN >>/$RUNNER_AUTH_TOKEN/g" /etc/circleci-runner/circleci-runner-config.yaml
```

This command replaces the placeholder in the configuration file with your actual token. Your runner is now authenticated with CircleCI.

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

![CircleCI dashboard showing self-hosted runner status. The main panel displays a list of registered runners, including runner name, status indicator showing active, last seen timestamp, and resource class. The interface uses a clean layout with navigation on the left and a white background. The overall tone is professional and informative. alt-text#center](images/dashboard.png "Self-Hosted Runners")

Congratulations! You've successfully installed, configured, and registered your CircleCI Machine Runner on your SUSE Arm64 VM in Google Cloud C4A. Your environment is now ready to run Arm-native CircleCI jobs.

Next, define jobs in the `.circleci/config.yml` file that uses your Arm reesource class. You'll be able to run builds and workflows directly on this runner, taking full advantage of Arm performance and scalability.

Ready to start building? You can now head to the next section and launch your first Arm-native pipeline.
