---
title: Deploy a component to PocketBeagle 2 with AWS IoT Greengrass 
description: Build a PocketBeagle 2 Yocto image, provision AWS IoT Greengrass nucleus lite, and deploy a Hello World component through an AWS IoT thing group.

minutes_to_complete: 180

draft: true
cascade:
    draft: true


who_is_this_for: This is an advanced topic for embedded Linux developers connecting an Arm-based PocketBeagle 2 to AWS IoT Greengrass.

learning_objectives:
    - Build and boot the PocketBeagle 2 Yocto development image.
    - Provision a unique device identity for Greengrass nucleus lite.
    - Publish an inline Hello World component to AWS IoT Greengrass.
    - Deploy the component through a thing group and verify that it runs on the board.

prerequisites:
    - A PocketBeagle 2, a 32 GB or larger microSD card, a card reader, and a USB-C cable
    - A host computer running Ubuntu 24.04 Linux with sudo access, 16 GB or more RAM, and 250 to 400 GB free disk space
    - An AWS account with permission to manage AWS IoT resources, publish Greengrass components, and create Greengrass deployments
    - The [AWS CLI](/install-guides/aws-cli/) v2 configured with [AWS credentials](/install-guides/aws_access_keys/) and Python 3 installed on the host computer

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-24T19:10:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a87285ac542d39ea9e312990d2fa5e67100f285c85b059b0ae76764f46effaaa
  summary_generated_at: '2026-11-24T19:10:17Z'
  summary_source_hash: a87285ac542d39ea9e312990d2fa5e67100f285c85b059b0ae76764f46effaaa
  faq_generated_at: '2026-11-24T19:10:17Z'
  faq_source_hash: a87285ac542d39ea9e312990d2fa5e67100f285c85b059b0ae76764f46effaaa
  summary: >-
    You'll build and boot a PocketBeagle 2 Yocto image, provision Greengrass nucleus lite, and
    verify a cloud-deployed Hello World component. On an Ubuntu host, you'll use the provided script
    and write the Yocto image to a microSD card. After connecting the board, you'll create its AWS identity
    and confirm that it is healthy. You'll then publish the component, deploy it through a thing
    group, and check its output in the board journal.
  faqs:
  - question: Where should I unpack the PocketBeagle 2 build scripts?
    answer: >-
      Unpack the zip file to a fixed location without spaces, such as a directory under your home
      folder. From there, run `./build-pocketbeagle2.sh --help` to review the script options.
  - question: How do I identify the correct microSD device before writing the image?
    answer: >-
      Use `lsblk -o NAME,SIZE,MODEL,MOUNTPOINTS` to compare device size and model with your card.
      Before using `bmaptool`, check the whole device path, such as `/dev/sdX`, rather than a partition.
  - question: Which AWS account and Region should I use when provisioning and deploying?
    answer: >-
      Use the same AWS account and Region for every step. If you open a new terminal, reapply
      the AWS environment variables before continuing.
  - question: Why doesn't the Hello World component need an S3 bucket?
    answer: >-
      You define the application directly in the `run` lifecycle step of the recipe. Because its
      `Artifacts` list is empty, you don't need a separate script or an S3 bucket.
  - question: How do I know that the Hello World component was deployed and is running on the board?
    answer: >-
      Match the `deploymentId` in `list-effective-deployments` and look for `coreDeviceExecutionStatus` of
      `SUCCEEDED`. Confirm that the `lifecycleState` of the installed component is `RUNNING`, then look for
      repeated Hello World messages in its journal.
# END generated_summary_faq

author: Doug Anson
generate_summary_faq: false
rerun_summary: false
rerun_faqs: false
skilllevels: Advanced
subjects: Embedded Linux

armips:
    - Cortex-A
operatingsystems:
    - Linux

tools_software_languages:
    - Yocto Project
    - AWS IoT Greengrass
    - Python

further_reading:
    - resource:
        title: PocketBeagle 2 quick start
        link: https://docs.beagleboard.org/boards/pocketbeagle-2/02-quick-start.html
        type: documentation
    - resource:
        title: Yocto Scarthgap host requirements
        link: https://docs.yoctoproject.org/scarthgap/ref-manual/system-requirements.html
        type: documentation
    - resource:
        title: AWS IoT Greengrass nucleus lite 2.6.0 provisioning
        link: https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/Provisioning.md
        type: documentation
    - resource:
        title: Greengrass component recipe reference
        link: https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html
        type: documentation
    - resource:
        title: Create Greengrass deployments
        link: https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html
        type: documentation

### FIXED, DO NOT MODIFY
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
