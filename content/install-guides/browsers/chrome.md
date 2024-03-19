---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Chrome

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- browser
- chrome

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 5

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://support.google.com/chrome/

weight: 3                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: false             # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: true    # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## Installing Chrome

The Chrome browser runs on Windows on Arm natively on the Beta release channel, and using emulation on the Stable release channel. Chrome is not available for Arm Linux. 

### Linux

Chrome is not available for Arm Linux. 

### Windows 

#### Native 

To install Chrome on Windows on Arm:

1. Go to the [download page](https://www.google.com/chrome/beta/?platform=win_arm64) and click the Download Chrome Beta button.

2. Run the downloaded `ChromeSetup.exe` file 

3. Find and start Chrome from the applications menu

{{% notice Note %}}
The native Windows on Arm version of Chrome is currently on the Beta channel. This is a preview version of new features in development and is updated weekly, but is faster than emulation.
{{% /notice %}}

#### Emulation

If you prefer to use a Stable version, you can run using emulation. 

Emulation is slower than native and shortens battery life.

1. Download the Windows installer from [Google Chrome](https://www.google.com/chrome/)

2. Run the `ChromeSetup.exe` installer 

3. Find and start Chrome from the applications menu 

{{% notice Note %}}
The Chrome setup program installs the 32-bit x86 version of Chrome.
{{% /notice %}}

