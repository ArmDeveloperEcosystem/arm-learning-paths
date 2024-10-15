---
title: Arm Software Licensing
author_primary: Ronan Synnott
additional_search_terms:
- success kits
- ssk
- hsk
- ubl
- flex

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: true             # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Most Arm commercial tools are license managed. Arm is migrating to user-based licensing (UBL) which greatly simplifies license configuration. It is available for [Arm Success Kits](/install-guides/successkits/) as well as [Arm Development Studio](/install-guides/armds).

Success kits are available as `Hardware Success Kits` (`HSK`) or `Software Success Kits` (`SSK`). See the table below for tooling provided. SSK is a subset of HSK.

With UBL, you have unlimited access to all components in the success kit you have enabled. The license is cached locally for up to 7 days, enabling remote or traveling users to access tools without connecting to their license server.

Starting any UBL enabled tool when the server is available will renew the license for 7 more days. This renewal attempt is performed once per 24 hours.

If the license is not renewed within 7 days, it is automatically returned to the pool of available licenses. When you next use a UBL licensed tool, it will automatically attempt to check out a new license.

User-based licensing can be managed with:
* Local License Server (`LLS`), an internally managed license server, likely only accessible from your internal network or VPN.
* Cloud License Server (`CLS`), a license server managed by Arm, accessible from anywhere.

Legacy product versions do not support UBL licensing and use FlexLM [floating licensing](./flexnet) instead. See the below table.


| Arm Development Tool                        | Earliest version supporting UBL |  SSK  | HSK |
| :-----------------------------------------: | :-----------------------------: | :---: | :-: |
| Arm Compiler for Embedded                   | 6.18                            |  X    |  X  |
| Arm Compiler for Embedded FuSa 6.16         | 6.16.2                          |  X    |  X  |
| Arm Development Studio [`1`]                | 2022.0, 2022.a                  |  X    |  X  |
| Keil MDK                                    | 5.37                            |  X    |  X  |
| Arm Fast Models                             | 11.17.1                         | [`2`] |  X  |
| Arm Socrates [`3`]                          | 1.7.0                           |       |  X  |
| Arm Performance Models Library              | 1.2                             |       |  X  |
| AMBA Viz                                    | 1.1.25                          |       |  X  |

[`1`] Arm Development Studio versions indexed with letters after the period are for those users with access to non-publicly announced IP.

[`2`] A license to run pre-built platforms, including Fixed Virtual Platforms, is provided with SSK. HSK license is necessary to build virtual platforms.

[`3`] Some functionality of Arm Socrates requires an appropriate [Arm IP license](https://developer.arm.com/documentation/101400/010710/Setting-up-licensing/Required-licenses), which may also require a [floating license](./flexnet) to be setup.

## User-based Licensing Video Tutorials

In addition to the set up and install instructions below, a collection of video tutorials are available on the Arm Developer website:

* [Accessing the Arm License Portal](https://developer.arm.com/Additional%20Resources/Video%20Tutorials/User-based%20Licensing%20-%20Accessing%20the%20Arm%20License%20Portal)
* [Cloud-based Licenses and Activation Codes](https://developer.arm.com/Additional%20Resources/Video%20Tutorials/User-based%20Licensing%20-%20Cloud-based%20Licenses%20and%20Activation%20Codes)
* [Local License Server Setup](https://developer.arm.com/Additional%20Resources/Video%20Tutorials/User-based%20Licensing%20-%20Local%20License%20Server%20Setup)
* [End-user Setup](https://developer.arm.com/Additional%20Resources/Video%20Tutorials/User-based%20Licensing%20-%20End%20User%20Setup)
* [Removal of Licenses and Decommissioning Server](https://developer.arm.com/Additional%20Resources/Video%20Tutorials/User-based%20Licensing%20-%20License%20Removal%20and%20Decommissioning%20Server)
