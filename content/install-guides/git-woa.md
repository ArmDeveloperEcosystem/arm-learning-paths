---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Git for Windows on Arm

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- git
- windows
- woa
- windows on arm
- open source windows on arm

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

### Link to official documentation
official_docs: https://git-scm.com/doc

author_primary: Jason Andrews

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Git has native support for [Windows on Arm](https://learn.microsoft.com/en-us/windows/arm/overview). Starting with version 2.47.1, an official installer is available. 

In addition to Windows laptops, Windows on Arm instances are available with Microsoft Azure. For further information, see [Deploy a Windows on Arm virtual machine on Microsoft Azure](/learning-paths/cross-platform/woa_azure/).

## How do I download and install Git for Windows on Arm?

Git releases are available in [GitHub releases](https://github.com/git-for-windows/git/releases/).

Use a browser to download the desired release file. The Git releases for Windows on Arm have `arm64.exe` in the filename.

You can also download from a Windows PowerShell with the following command:

```command
curl https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.1/Git-2.47.1-arm64.exe -o Git-2.47.1-arm64.exe
```

Once you have downloaded Git, run the installer `.exe` file on a Windows on Arm machine. 

The installer starts. 

Click **Next** to acknowledge the GNU General Public License.

Set the destination location or accept the default location, and click **Next**.

Continue to click **Next** for the configuration settings. You can accept all defaults if you are unsure of specific settings.

At the end of the install process, you see the screen below indicating setup has finished installing Git:

![Install](/install-guides/_images/git-woa.png)

Click the **Finish** button to complete installation. 

## How do I use Git on Windows? 

You can use Git on Windows from a Command Prompt or using Git Bash. 

Git Bash is a Linux-like terminal experience which includes Git and many other Linux commands. 

{{% notice Note %}}
Git is not automatically added to your search path during installation. 
{{% /notice %}}

To use Git, click the Windows **Start** button and then click **All apps**.

You see the Git folder in the G section.

![Start](/install-guides/_images/git2-woa.png)

There are menu items for multiple ways to start Git. 

## How can I use Git in a Windows Command Prompt?

Start a Git Command Prompt by selecting **Git CMD** from the **Start** menu.

![CMD](/install-guides/_images/git3-woa.png)


To see the help message, enter:

```cmd
git help
```

You can use Git from this Command Prompt. 

## How can I use Git with Git Bash?

To use Git in a Linux-like environment, select **Git Bash** from the start menu.

![CMD](/install-guides/_images/git4-woa.png)

Click the colored icon in the top-left corner of the Git Bash window, and then click **Options** to change the appearance of the window, including colors, fonts, and font sizes. 

![Options](/install-guides/_images/git5-woa.png)

You are now ready to use Git on your Windows on Arm device. 
