---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm User based licenses

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- licensing
- success-kits

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 20

### Link to official documentation
official_docs: 

weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: true             # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
All Arm tools are license managed. Arm is migrating to a user-based licensing (UBL) system which greatly simplifies license configuration. It is available for [Arm Success Kits](../successkits/).

With a UBL license you have unlimited access to all components within the success kit you have enabled. The license is cached locally for up to 7 days, enabling remote or traveling users to have access to tools without connecting to their license server.

Using any UBL enabled tool when the server is available will renew the 7 days of license. This renewal attempt is performed once per 24 hours.

If the license is not renewed within 7 days, it is automatically returned to the pool of available licenses. When you next use a UBL licensed tool, it will automatically attempt to check out a new license..

The licenses can be set up as:
* Local license server, an internally managed license server, likely only accessible from internal network/VPN.
* Cloud license server, a license server managed by Arm, accessible from anywhere.

Legacy products do not support UBL licensing. For those products, use FlexLM licensing.
