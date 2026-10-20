---
title: "Set up Chrome and Node.js for headless testing"
description: "Install Google Chrome and Node.js v20 on Ubuntu 24.04 or Amazon Linux 2023 (arm64)."

weight: 3

layout: "learningpathall"
---

## Install Chrome

Google Chrome publishes official arm64 packages for both Debian-based and RPM-based Linux distributions. Install the package that matches your distribution.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu 24.04" language="bash" >}}
sudo apt-get update
wget https://dl.google.com/linux/direct/google-chrome-stable_current_arm64.deb
sudo apt install -y ./google-chrome-stable_current_arm64.deb
  {{< /tab >}}
  {{< tab header="Amazon Linux 2023" language="bash" >}}
wget https://dl.google.com/linux/direct/google-chrome-stable_current_aarch64.rpm
sudo dnf install -y ./google-chrome-stable_current_aarch64.rpm
  {{< /tab >}}
{{< /tabpane >}}

For more detail on installing Chrome on Arm Linux, see the [Chrome install guide](/install-guides/browsers/chrome/).

Verify the installation by printing the Chrome version:

```bash
google-chrome --version
```

The output is similar to:

```output
Google Chrome 155.0.8059.84 
```

## Install Node.js

Puppeteer requires Node.js 18 or later. Install Node.js v20 LTS using your distribution's package manager.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu 24.04" language="bash" >}}
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
  {{< /tab >}}
  {{< tab header="Amazon Linux 2023" language="bash" >}}
sudo dnf install -y nodejs npm
  {{< /tab >}}
{{< /tabpane >}}

Verify that Node.js and npm are installed:

```bash
node --version
npm --version
```

The output is similar to:

```output
v20.20.2
10.8.2
```

## What you've accomplished

You've installed Chrome, Node.js, and npm on your Arm Linux server and verified their versions. Next, you'll install `puppeteer-core` and write tests against a locally served Hugo site.
