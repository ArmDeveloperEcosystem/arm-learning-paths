---
title: "Set up Chrome and Node.js for headless testing"
description: "Install and verify Google Chrome and Node.js v20 on Ubuntu 24.04 or Amazon Linux 2023 (arm64) for headless testing."

weight: 3

layout: "learningpathall"
---

## Install and verify Google Chrome

Google Chrome publishes official arm64 packages for both Debian-based and RPM-based Linux distributions. Install the package that matches your distribution by completing the [Chrome installation steps for Linux](/install-guides/browsers/chrome/).

Verify the installation on Linux by printing the Chrome version:

```bash
google-chrome --version
```

The output is similar to:

```output
Google Chrome 155.0.8059.84 
```

## Install and verify Node.js

Puppeteer requires Node.js 18 or later. Install Node.js v20 LTS by using the package manager for your distribution:

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

## What you've accomplished and what's next

You've installed Chrome, Node.js, and `npm` on your Arm Linux server and verified their versions. 

Next, you'll install `puppeteer-core` and write tests against a locally served Hugo site.
