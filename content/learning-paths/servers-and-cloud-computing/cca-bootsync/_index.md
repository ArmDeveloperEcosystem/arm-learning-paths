---
title: Secure Realms during boot using Arm Confidential Compute Architecture (CCA) BootSync
description: Use Arm CCA BootSync on an RME-enabled FVP to inject UEFI variables and secrets to unlock the disk during boot, then verify Secure Boot and encrypted root file system startup.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers who want to understand how Arm CCA BootSync supports early Realm boot workflows such as UEFI Secure Boot and encrypted disk boot.

learning_objectives:
  - Understand why BootSync is needed before the Realm guest operating system has networking.
  - Understand how the Boot Injection Protocol uses key exchange, attestation, and Boot Information Blocks to support the BootSync workflow.
  - Use BootSync to inject UEFI variables and secret data into an Arm CCA Realm.
  - Launch Arm CCA Realms with UEFI Secure Boot and an encrypted root file system on an Armv9-A AEM Base Fixed Virtual Platform (FVP) with Realm Management Extension (RME) support.

prerequisites:
  - A cloud-based instance or an AArch64 or x86_64 computer running Linux. For more information about using cloud-based instances, see the [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/) Learning Path.
  - Completion of the [Run an application in a Realm using the Arm Confidential Compute Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container/) Learning Path

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-17T18:27:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5b4a562e119669be2adcee1e0f304ca8cd2032cc5b6056ad01a88251019c010c
  summary_generated_at: '2026-07-17T18:27:39Z'
  summary_source_hash: 5b4a562e119669be2adcee1e0f304ca8cd2032cc5b6056ad01a88251019c010c
  faq_generated_at: '2026-07-17T18:27:39Z'
  faq_source_hash: 5b4a562e119669be2adcee1e0f304ca8cd2032cc5b6056ad01a88251019c010c
  summary: >-
    You'll use Arm CCA BootSync on an RME-enabled Armv9-A AEM Base FVP
    to deliver UEFI variables and secrets to a Realm during early boot, then validate Secure Boot
    and encrypted disk startup. First, you'll launch a Realm without injected data to observe
    firmware attestation. Next, you'll provide variable data for BootSync to complete and verify that Secure Boot rejects the unsigned kernel. After signing the kernel, you'll verify that Secure Boot is active. Finally, you'll encrypt the Realm root file system, inject the file system decryption secret through
    BootSync, and confirm that the disk unlocks during boot.
  faqs:
  - question: Do I need networking inside the Realm to deliver boot data?
    answer: >-
      No. BootSync operates before the guest operating system has networking and uses the Boot Injection protocol to provide early boot data.
  - question: How do I know BootSync requested variable data?
    answer: >-
      In the User Context service log, you'll see `BIB Variable Data Requested`
      and the expected `<RPV>_VAR.dat` file name. If the file is missing,
      BootSync reports `BootSyncNotDone`, and the Realm boots without Secure
      Boot enabled.
  - question: What result should I expect when Secure Boot is configured but the kernel is unsigned?
    answer: >-
      The unsigned kernel is rejected. This confirms that UEFI Secure Boot is enforcing signature
      verification.
  - question: After I sign the kernel, how do I verify that Secure Boot is enabled?
    answer: >-
      The signed kernel boots successfully and the Secure Boot UEFI variable reports `1`. Check
      that value to confirm the state.
  - question: How do I confirm the encrypted root file system unlocks correctly?
    answer: >-
      After BootSync supplies the correct passphrase, the boot log reports
      `LUKS partition unlocked, switching root`. Run `df -h` and verify that
      `/dev/mapper/cryptroot` is mounted at `/`.
# END generated_summary_faq

author:
  - Anton Antonov
  - Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
  - Neoverse
  - Cortex-A
operatingsystems:
  - Linux
tools_software_languages:
  - FVP
  - RME
  - CCA
  - Docker
  - EDK2
  - Cryptsetup

further_reading:
  - resource:
      title: Arm Confidential Compute Architecture
      link: https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture
      type: website
  - resource:
      title: Arm Confidential Compute Architecture Open-Source enablement
      link: https://www.youtube.com/watch?v=JXrNkYysuXw
      type: video
  - resource:
      title: Learn the architecture - Realm Management Extension
      link: https://developer.arm.com/documentation/den0126
      type: documentation
  - resource:
      title: Realm Management Monitor Specification
      link: https://developer.arm.com/documentation/den0137/latest/
      type: documentation
  - resource:
      title: Realm Host Interface Specification
      link: https://developer.arm.com/documentation/den0148/latest/
      type: documentation
  - resource:
      title: ArmCcaBootSync README
      link: https://gitlab.arm.com/linux-arm/edk2-cca/-/blob/cca/4441_measured_boot_v1/ArmVirtPkg/ArmCcaBootSync/Readme.md
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

