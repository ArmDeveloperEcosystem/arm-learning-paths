---
title: Arm Licensing
author_primary: Ronan Synnott
additional_search_terms:
- success-kits

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: true             # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Most Arm commercial tools are license managed. Arm is migrating to user-based licensing (UBL) which greatly simplifies license configuration. It is available for [Arm Success Kits](../successkits/).

With UBL, you have unlimited access to all components in the success kit you have enabled. The license is cached locally for up to 7 days, enabling remote or traveling users to access tools without connecting to their license server.

Starting any UBL enabled tool when the server is available will renew the license for 7 more days. This renewal attempt is performed once per 24 hours.

If the license is not renewed within 7 days, it is automatically returned to the pool of available licenses. When you next use a UBL licensed tool, it will automatically attempt to check out a new license.

The licenses can be set up as:
* Local license server, an internally managed license server, likely only accessible from your internal network (or by using a VPN).
* Cloud license server, a license server managed by Arm, accessible from anywhere.

Legacy products do not support UBL licensing and use FlexLM licensing instead.
