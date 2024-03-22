---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm IP Explorer

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- architecture
- soc
- ip
- cortex-a
- cortex-r
- cortex-m
- cortex

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author_primary: Ronan Synnott

### Link to official documentation
official_docs: https://www.arm.com/products/ip-explorer

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

Arm IP Explorer is a cloud-based tool used to accelerate IP selection and SoC design. 
It also includes a simulation feature used by software developers for benchmarking Arm processors as part of the IP selection process.

## Before you begin

An Arm account is required to access Arm IP Explorer.

To create an Arm account, enter your e-mail on the [registration form](https://www.arm.com/register) and follow the instructions.

## Installation

As Arm IP Explorer is a cloud application, it does not require any installation.

You can access Arm IP Explorer using a browser by visiting [ipexplorer.arm.com](https://ipexplorer.arm.com/)

If your Arm account is not setup for access, you will be presented with a request access form.

Fill out the form, Arm will review your request, and grant access, if appropriate.

## Explore Arm IP

Use the `Explore` buttons to learn about the features of various Arm IP and compare them against each other.

They are broken down into different sections:
* Explore Processors
* Explore Interconnect
* Explore System IPs
* Explore Subsystems

You can configure IP blocks to your needs to be able to make comparisons in terms of performance, power efficiency, silicon area, and other parameters.

You can save your configured IP for later use, as well as render the RTL for your configuration (**Note** that this requires an appropriate license from Arm).

## Simulate Processors

To help evaluate the performance of the processors, Arm IP Explorer provides a number of RTL-based simulation systems that allow you to run benchmark code on them.

## Create SoC Concept

A `SoC Concept` is the first step towards the architectural design of your device.

You can select any of the Arm IPs that you wish to use, including those configured previously, and define how they can be connected.

![SoC Concept #center](../_images/soc_concept.png "SoC Concept")

You can invite other users to help review your design. These could be others from your organization, contacts within Arm that you are engaged with, or from a different organization that you are working with on the project.

{{% notice Arm Approved Design Partners %}}
Use the `Design Partners` link within `Arm IP Explorer` for information on Arm Approved Design Partners.
{{% /notice %}}

The design can then be exported to a `json` format suitable for importing to [Arm Socrates](https://www.arm.com/products/development-tools/system-ip/system-ip-tools/socrates) for further configuration.

See also the [Arm Socrates Install Guide](/install-guides/socrates/).
