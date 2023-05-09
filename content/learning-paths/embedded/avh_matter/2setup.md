---
# User change
title: "Prepare AVH instances of Raspberry Pi 4"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

You will need a user account for [Arm Virtual Hardware 3rd Party Hardware](https://avh.arm.com/). Refer to [Arm Virtual Hardware install guide](/install-guides/avh#thirdparty) for more information.

A [GitHub](https://github.com) account is also required.

GitHub requires that a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) be set. If you do not have this on your account already, navigate to `Settings` > `Developer Settings` > `Personal Access Tokens`, click on `Generate new token`, and save the token locally.

Ensure you have enabled the token to `Update GitHub Action workflows`.

You may wish to create a local scratch pad text file containing the below details (which will be unique to you), so that you can easily copy and paste from.

```
YOUR_GITHUB_USERNAME
YOUR_PERSONAL_ACCESS_TOKEN
git config --global user.name "YOUR_GITHUB_USERNAME"
git config --global user.email YOUR_EMAIL_ADDRESS
```

## Login to Arm Virtual Hardware console

Open your browser, and navigate to Arm Virtual Hardware dashboard:
```console
https://app.avh.arm.com/
```
## Create TWO Raspberry Pi 4 virtual devices

Click on `Create Device`.

Select `Raspberry Pi 4` from the list of available devices.

Select `Raspberry Pi OS lite` from the example firmware packages.

Name the device `chip-tool` (though the naming is arbitrary `chip-tool` is used later in the session) and create device.

While this is being created, click `Devices` and repeat steps to create a second instance (suggest `lighting-app` as name).

Open each instance in its own browser pane.

## Login to virtual Raspberry Pi instances

When your instances are created, select the `Console` tab, and log into each Raspberry Pi 4 instance.

- Username: `pi`
- Password: `raspberry`

Repeat for the other instance.

It is also possible to log in via the CLCD window view. However it is easier to copy and paste (`Shift+Insert`) to the Console view.

## (Optional) Connect via SSH

The `Console` view within the browser will suffice to complete this Learning Path.

If you wish to connect via `SSH` (rather than `Console`), it is easiest to follow the SSH tunnel connection instructions specified in the `Connect` tab. 

As an alternative, you can also download and install the appropriate [OpenVPN Community](https://openvpn.net/community-downloads) version for your host. Click on `DOWNLOAD OVPN FILE` within the `Connect via VPN` section.

In the `OpenVPN` GUI, select `Import` > `Import file...` and browse to the downloaded `OVPN file`. Click `Connect`.

On your host, open terminal(s), and connect to the virtual hardware instance(s) with the command shown in the `Connect` tab, or use your preferred terminal application.

## Install necessary software components

You shall build the Matter examples on the virtual Raspberry Pi 4 instances. To prepare for this, install the necessary dependencies on **each** instance. This can be done in parallel on both instances.
```console
sudo apt-get update
sudo apt-get install -y git gcc g++ pkg-config libssl-dev libdbus-1-dev libglib2.0-dev libavahi-client-dev ninja-build python3-venv python3-dev python3-pip unzip libgirepository1.0-dev libcairo2-dev libreadline-dev libpango1.0-dev
```
We shall also build ZAP from source on our instances. ZAP is generally installed as a third-party tool via CIPD during the build environment bootstrap but zap packages are currently NOT available for arm64.
```console
git clone https://github.com/project-chip/zap.git ~/zap
cd ~/zap
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo src-script/install-packages-ubuntu
npm ci
export ZAP_DEVELOPMENT_PATH=~/zap
cd ~
```
This will also verify that your instances are working correctly.
