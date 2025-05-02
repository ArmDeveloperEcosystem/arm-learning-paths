---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Firefox

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- browser
- firefox

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author: Jason Andrews

### Link to official documentation
official_docs: https://support.mozilla.org/en-US/products/firefox/

weight: 6                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## How do I install Firefox?

The Firefox browser runs on Windows on Arm as a native ARM64 application, and is available on Arm Linux distributions. 

Visit the [download page](https://www.mozilla.org/en-US/firefox/all/#product-desktop-release) to obtain packages for various operating systems. 

### Linux

The best way to install Firefox on Arm Linux is to use the package manager for your distribution. 

{{% notice Note %}}
There are no Arm Linux downloads on the download page. 
{{% /notice %}}

To install Firefox on Linux:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo snap install firefox
  {{< /tab >}}
  {{< tab header="Debian" language="bash">}}
sudo apt install firefox-esr
  {{< /tab >}}
  {{< tab header="Fedora" language="bash">}}
sudo dnf install firefox
  {{< /tab >}}
{{< /tabpane >}}

For more ways to install Firefox on Linux refer to [Installing Firefox on Linux](https://support.mozilla.org/en-US/kb/install-firefox-linux)

### Windows 

To install Firefox on Windows on Arm:

1. Go to the [download page](https://www.mozilla.org/en-US/firefox/all/#product-desktop-release) and select the `Windows ARM64/AArch64` installer. 

2. Click **Download Now** 

3. Run the downloaded `.exe` file 

4. Find and start Firefox from the applications menu


