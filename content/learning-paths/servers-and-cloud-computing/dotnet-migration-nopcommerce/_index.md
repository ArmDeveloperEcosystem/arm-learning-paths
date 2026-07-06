---
title: Migrate and optimize a .NET nopCommerce application on Microsoft Azure
    
minutes_to_complete: 75

who_is_this_for: This Learning Path is for .NET and platform engineers migrating a production .NET application to Arm-based infrastructure on Azure.

learning_objectives:
    - Build a pinned nopCommerce release and baseline on Arm with the same .NET toolchain
    - Produce an SBOM and resolve platform-specific dependency cascades
    - Containerize with Dockerfile and .NET SDK multi-arch publish workflows
    - Apply architecture-conditional runtime tuning with measured results
    - Use the Arm MCP Server to automate endpoint selection, test generation, and optimization planning

prerequisites:
    - Azure account with permissions to create virtual machines
    - Azure CLI (`az`) installed locally
    - Docker and .NET 9 SDK familiarity
    - Basic Linux command-line knowledge

author: Joe Stech

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
cloud_service_providers:
  - Microsoft Azure
tools_software_languages:
    - .NET
    - C#
    - Docker
    - Azure CLI
    - PostgreSQL
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: nopCommerce repository
        link: https://github.com/nopSolutions/nopCommerce
        type: documentation
    - resource:
        title: .NET SDK container publish overview
        link: https://learn.microsoft.com/dotnet/core/containers/overview
        type: documentation
    - resource:
        title: GitHub Copilot modernization for .NET
        link: https://learn.microsoft.com/dotnet/core/porting/github-copilot-app-modernization/overview
        type: documentation
    - resource:
        title: .NET on Arm
        link: https://learn.microsoft.com/dotnet/core/install/linux-arm64
        type: documentation
    - resource:
        title: SixLabors ImageSharp
        link: https://docs.sixlabors.com/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
