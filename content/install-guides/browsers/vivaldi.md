---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Vivaldi

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- browser
- vivaldi

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://help.vivaldi.com/desktop/

weight: 7                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## Installing Vivaldi

Vivaldi is available for Arm Linux and Windows on Arm. 

Visit [Download Vivaldi](https://vivaldi.com/download/) to obtain packages for various operating systems. 


### Linux

Vivaldi is available for Arm Linux. 

1. Download a `.deb` file (Ubuntu/Debian) or a `.rpm` file (Fedora) for ARM64 using the [download area](https://vivaldi.com/download/) 

2. Run the package manager in the directory where you downloaded the file

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/Debian" language="bash">}}
sudo apt-get -y install ./vivaldi*.deb
  {{< /tab >}}
  {{< tab header="Fedora" language="bash">}}
sudo dnf --nogpgcheck -y install ./vivaldi*.rpm
  {{< /tab >}}
{{< /tabpane >}}

If you need a command line only install use the instructions below:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/Debian" language="bash">}}
wget -qO- https://repo.vivaldi.com/archive/linux_signing_key.pub | gpg --dearmor | sudo dd of=/usr/share/keyrings/vivaldi-browser.gpg
echo "deb [signed-by=/usr/share/keyrings/vivaldi-browser.gpg arch=$(dpkg --print-architecture)] https://repo.vivaldi.com/archive/deb/ stable main" | sudo dd of=/etc/apt/sources.list.d/vivaldi-archive.list
sudo apt update && sudo apt install vivaldi-stable -y
  {{< /tab >}}
  {{< tab header="Fedora" language="bash">}}
sudo dnf install dnf-utils -y
sudo dnf config-manager --add-repo https://repo.vivaldi.com/archive/vivaldi-fedora.repo
sudo dnf install vivaldi-stable -y
  {{< /tab >}}
{{< /tabpane >}}


### Windows 

The stable release of Vivaldi is an Arm native application. 

To install Vivaldi on Windows on Arm:

1. Go to the [download page](https://vivaldi.com/download/) and click the Download for Windows button. 

2. Run the downloaded `.exe` file 

3. Find and start Vivaldi from the applications menu
