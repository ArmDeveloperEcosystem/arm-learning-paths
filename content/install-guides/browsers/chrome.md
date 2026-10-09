---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Chrome
description: Install Chrome on Arm Linux or Windows on Arm and use a native browser for development and web workflows.

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- browser
- chrome

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author: Jason Andrews

### Link to official documentation
official_docs: https://support.google.com/chrome/

weight: 3                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## How do I install Chrome?

The Chrome browser runs on Windows on Arm as a native ARM64 application. Chrome is also available for Arm Linux. 

### Linux

Chrome is available for Arm Linux.

To install Chrome on Arm Linux:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/Debian" language="bash">}}
wget https://dl.google.com/linux/direct/google-chrome-stable_current_arm64.deb
sudo apt install ./google-chrome-stable_current_arm64.deb
  {{< /tab >}}
{{< /tabpane >}}

### Windows 

To install Chrome on Windows on Arm:

1. Go to the [download page](https://www.google.com/chrome/?platform=win_arm64) and click Download here. Click the Accept and Install button to start the download.

2. Run the downloaded `ChromeSetup.exe` file 

3. Find and start Chrome from the applications menu
