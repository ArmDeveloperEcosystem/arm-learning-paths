---
title: "Deploy Arm virtual machines on Google Cloud Platform (GCP) using Terraform"

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for anyone new to using Arm virtual machines in the Google Cloud Platform (GCP)

learning_objectives:
    - Automate Arm virtual machine creation using Terraform
    - Deploy Arm instances on GCP and provide access via Jump Server
    - Provide infrastructure basics, code knowledge and files that could help with future learning paths

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/). Create an account if needed.
    - A computer with [Terraform](/install-guides/terraform) installed.
    - A computer with [Google Cloud CLI](/install-guides/gcloud) installed.

author: Jason Andrews

##### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform
    - Bastion

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Create an Arm VM instance
        link: https://cloud.google.com/compute/docs/instances/create-arm-vm-instance#startinstanceconsole
        type: documentation
    - resource:
        title: Connect to Linux VMs 
        link: https://cloud.google.com/compute/docs/instances/connecting-to-instance#console
        type: documentation
    - resource:
        title: About bastion hosts
        link: https://cloud.google.com/solutions/connecting-securely#bastion
        type: documentation


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
