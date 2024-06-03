---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Chromium

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- browser
- chromium

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://www.chromium.org/Home/

weight: 4                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## How do I install Chromium?

The Chromium browser runs on Windows on Arm as a native ARM64 application, and is available on Arm Linux distributions.

[The Chromium area of woolyss.com](https://chromium.woolyss.com/) provides Chromium downloads. 

{{% notice Note1%}}
Google API keys are missing from Chromium so you will not be able to sync information with your Google account.
{{% /notice %}}

### How do I install Chromium on Arm Linux?

The best way to install Chromium on Arm Linux is to use the package manager for your distribution. 

To install Chromium on Linux:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt install chromium-browser -y
  {{< /tab >}}
  {{< tab header="Debian" language="bash">}}
sudo apt install chromium -y
  {{< /tab >}}
  {{< tab header="Fedora" language="bash">}}
sudo dnf install chromium -y
  {{< /tab >}}
{{< /tabpane >}}

Depending on your version of Ubuntu, Chromium may be installed as a snap from the [Canonical Snap Store](https://snapcraft.io/). 

### How do I install Chromium on Windows on Arm? 

Chromium is available as a native ARM64 application for Windows on Arm. 

1. Visit the [download section of woolyss.com](https://chromium.woolyss.com/#windows-on-arm) for the current releases. 

2. Click on **Installer** for the version you want to use.

3. Run the downloaded `mini_installer.exe`

The install is silent so you will not see anything, but Chromium will be installed. 

4. Find and start Chromium from the applications menu

{{% notice Note2%}}
Chromium on Windows on Arm does not update itself so you need to update manually to get new versions.
{{% /notice %}}

{{% notice Note3%}}
Certain types of videos don't play with Chromium. Video support is less than other browsers without DRM. 
{{% /notice %}}

