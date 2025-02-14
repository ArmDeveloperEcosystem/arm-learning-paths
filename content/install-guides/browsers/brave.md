---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Brave

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- browser
- brave

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author: Jason Andrews

### Link to official documentation
official_docs: https://support.brave.com/hc/en-us/categories/360001053032-Desktop-Browser

weight: 2                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## Installing Brave

The Brave browser runs on Windows on Arm as a native ARM64 application, and is available on Arm Linux distributions. 

### Linux

To install Brave on Linux:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/Debian" language="bash">}}
sudo apt install curl
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser -y
  {{< /tab >}}
  {{< tab header="Fedora" language="bash">}}
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo
sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc
sudo dnf install brave-browser
  {{< /tab >}}
{{< /tabpane >}}

For more ways to install Brave on Linux refer to [Installing Brave on Linux](https://brave.com/linux/)

### Windows 

Brave is a native ARM64 application. If you visit [brave.com](https://www.brave.com) and download from a Windows on Arm computer you will install the native version. 

Additional Brave releases for Windows on Arm are available on [GitHub](https://github.com/brave/brave-browser) 

To download the offline installer, use the files with `Standalone` in the name. 

To install Brave on Windows on Arm:

1. Click on latest release on the right side of the page. 

2. Find and download the offline install file `BraveBrowserStandaloneSetupArm64.exe`

3. Run the install file to install the browser

4. Find and start Brave from the applications menu

{{% notice Note %}}
If you want the smaller, online installer download the file `BraveBrowserSetupArm64.exe`
{{% /notice %}}




