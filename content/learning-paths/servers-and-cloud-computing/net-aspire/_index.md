---
title: Run a .NET Aspire application on Arm-based VMs on AWS and GCP

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in learning how to deploy .NET Aspire applications on Arm-based virtual machines (VMs) on Amazon Web Services (AWS) and Google Cloud Platform (GCP).

learning_objectives: 
    - Understand .NET Aspire developer tools.
    - Create a .NET Aspire application.
    - Modify code on a Windows on Arm development machine.
    - Deploy a .NET Aspire application to Arm-powered virtual machines in the Cloud.
prerequisites:
    - A Windows on Arm machine such as the Lenovo Thinkpad X13s running Windows 11, to build the .NET Aspire project  
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from AWS or GCP
    - A code edito, such as [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) 

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:39:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 09c62748f1623172f6adbc48bb3411abd4bad6c0e477c8c0aa66b19f8369db69
  summary_generated_at: '2026-10-01T19:39:10Z'
  summary_source_hash: 09c62748f1623172f6adbc48bb3411abd4bad6c0e477c8c0aa66b19f8369db69
  faq_generated_at: '2026-10-01T19:39:10Z'
  faq_source_hash: 09c62748f1623172f6adbc48bb3411abd4bad6c0e477c8c0aa66b19f8369db69
  summary: >-
    You'll create and run a .NET Aspire application on a Windows on Arm development machine, then deploy
    it to an Arm-based VM. First, you'll install the Aspire workload, trust the local HTTPS
    certificate, and inspect the application through its startup output and dashboard. You'll then
    add a compute-intensive service, rebuild the application, and deploy it to an AWS Graviton-based
    EC2 instance. You can also complete these steps on an Arm-based Google Cloud VMs.
  faqs:
  - question: How do I verify the .NET SDK and install the Aspire workload before creating the
      project?
    answer: >-
      Run `dotnet --version` in PowerShell and confirm that you have .NET SDK 8.0 or later.
      Then run `dotnet workload install aspire` and check for `Successfully installed workload(s) aspire.`
  - question: Why do I need to trust the HTTPS development certificate, and how do I do it?
    answer: >-
      You use HTTPS when running the application locally. Run `dotnet dev-certs https --trust`
      before starting your application to trust its HTTPS development certificate.
  - question: Which project do I run to start the distributed application, and what output should
      I expect?
    answer: >-
      From the project directory, run `dotnet run --project NetAspire.Arm.AppHost`. You should see
      messages such as `Building...`, an Aspire version line, and `Distributed application starting`.
  - question: Where do I add the intensive computations, and how can I confirm the change worked?
    answer: >-
      Add the supplied `ComputationService.cs` code to `NetAspire.Arm.ApiService`. In `Program.cs`,
      update the `/weatherforecast` handler to call `ComputationService.PerformIntensiveCalculations(matrixSize: 800)`.
      Run `dotnet run --project NetAspire.Arm.AppHost`, select **Weather** in your web frontend,
      then open **Traces** in the dashboard to inspect the longer request duration.
  - question: Which ports do I need to expose to access the deployed application?
    answer: >-
      Allow TCP traffic on the actual ports your application uses; the example uses `7133`,
      `7511`, and `17222`. Match your application's port values in the AWS EC2 security group
      or a Google Cloud firewall rule associated with your VM's `dotnet-app` network tag.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
platforms:
  - AWS Graviton
  - Google Axion

armips:
    - Neoverse

tools_software_languages:
    - dotnet
    - csharp 
    - Visual Studio Code

operatingsystems:
    - Windows
    - Linux

further_reading:
    - resource:
        title: .NET Aspire Overview
        link: https://learn.microsoft.com/en-us/dotnet/aspire/get-started/aspire-overview
        type: Documentation
    - resource:
        title: Compute Service - Amazon EC2
        link: https://aws.amazon.com/pm/ec2
        type: Documentation
    - resource:
        title: Compute Service - Google GCP
        link: https://cloud.google.com/products/compute/
        type: Documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
