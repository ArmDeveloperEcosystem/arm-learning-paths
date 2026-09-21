---
title: Load a MAPPO policy with the Arm Device Connect dashboard
description: Use the Arm Device Connect dashboard to distribute, select, and validate an exported MAPPO policy on an Arm cloud instance.
minutes_to_complete: 45

who_is_this_for: This Learning Path is for machine learning developers who have exported a MAPPO actor and want to validate its deployment workflow through a browser-based Device Connect dashboard.

draft: true
cascade:
    draft: true

learning_objectives:
    - Set up the MAPPO Device Connect dashboard on an Arm cloud instance.
    - Serve an exported MAPPO actor to a simulated device through Device Connect.
    - Load, arm, and validate the selected actor without connecting physical hardware.

prerequisites:
    - An Arm-based Ubuntu 24.04 cloud instance with SSH access, `sudo` privileges, and internet access.
    - The actor-only `.npz` artifact created in the [MAPPO training Learning Path](/learning-paths/servers-and-cloud-computing/train-mappo-navigation-arm-cloud/).
    - A local browser and permission to forward port 8080 through SSH.

author: Waheed Brown

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Neoverse
tools_software_languages:
    - Arm Device Connect
    - MAPPO
    - Python
    - NumPy
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Train a MAPPO navigation policy on Arm cloud
        link: /learning-paths/servers-and-cloud-computing/train-mappo-navigation-arm-cloud/
        type: website
    - resource:
        title: MAPPO Arm cloud Physical AI demo
        link: https://github.com/armwaheed/mappo-arm-cloud-physical-ai
        type: website
    - resource:
        title: Arm Device Connect repository
        link: https://github.com/arm/device-connect
        type: website
    - resource:
        title: BenchMARL repository
        link: https://github.com/facebookresearch/BenchMARL
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
