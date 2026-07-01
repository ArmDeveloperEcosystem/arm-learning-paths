---
title: Run an end-to-end Attestation Flow with Arm CCA
description: Learn how to deploy a CCA realm on an FVP with RME support and connect it with attestation services to create an end-to-end confidential computing workflow.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for software developers who want to learn how to run an end-to-end attestation flow with Arm's Confidential Computing Architecture (CCA).  

learning_objectives:
     - Describe how you can use attestation with Arm's Confidential Computing Architecture (CCA).
     - Deploy a simple workload in a CCA realm on an Armv9-A AEM Base Fixed Virtual Platform (FVP) that has support for RME extensions. 
     - Connect the workload with additional software services to create an end-to-end example that uses attestation to unlock the confidential processing of data.

prerequisites:
    - An AArch64 or x86_64 computer running Linux. You can use cloud instances, see this list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).
    - Completion of [Get Started with CCA Attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison/) Learning Path.
    - Completion of the [Run an application in a Realm using the Arm Confidential Computing Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container/) Learning Path.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:42:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ba896cb418c6ae4f96029081ac9ef1f9193e8983425ad7a316c184b5b6017fbf
  summary_generated_at: '2026-06-30T21:42:00Z'
  summary_source_hash: ba896cb418c6ae4f96029081ac9ef1f9193e8983425ad7a316c184b5b6017fbf
  faq_generated_at: '2026-06-30T21:42:00Z'
  faq_source_hash: ba896cb418c6ae4f96029081ac9ef1f9193e8983425ad7a316c184b5b6017fbf
  summary: >-
    You'll deploy a sample workload in a Linux realm on
    an Armv9-A AEM Base Fixed Virtual Platform (FVP) with Realm Management Extension (RME) support
    and connect it to attestation services to control access to secrets. First, you'll start a minimal
    Key Broker Server (KBS) from the Veraison project in a container, then integrate it with the
    realm so that confidential data is released only after successful attestation. You'll focus
    on the flow of evidence, verification, and key release to recognize a complete
    end-to-end run when service logs report a successful attestation result and the workload in
    the realm receives its key.
  faqs:
  - question: Which components need to be running to exercise the end-to-end flow?
    answer: >-
      You need the RME-enabled Armv9-A AEM Base FVP hosting a Linux realm, the attestation services,
      and the Veraison Key Broker Server (KBS) container. Run these in the order described so
      that attestation can evaluate the realm before secrets are requested.
  - question: How do I know the Key Broker Server is ready?
    answer: >-
      After starting the provided container image, confirm the container is running and check
      its logs for a startup or listening message. Proceed only when the KBS indicates it is ready
      to handle requests.
  - question: What result should I expect when attestation succeeds?
    answer: >-
      The attestation services accept the realm’s evidence, and the KBS authorizes release of
      a key or secret. You should see logs showing a positive attestation outcome and the workload
      receiving the expected data.
  - question: When should the confidential data be released to the realm?
    answer: >-
      Only after the attestation step verifies that the Linux realm provides the required level
      of confidential isolation. The example gates key release on that successful verification.
  - question: What should I check if attestation fails or no key is returned?
    answer: >-
      Verify the Linux realm is running on the RME-enabled FVP and that the attestation services
      and KBS are up and reachable. Inspect their logs for configuration or connectivity errors,
      then restart the flow after addressing the issue.
# END generated_summary_faq

author: 
    - Arnaud de Grandmaison
    - Paul Howard
    - Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse 
operatingsystems:
    - Linux 
tools_software_languages:
    - GCC
    - FVP
    - RME
    - CCA
    - Docker
    - Veraison
    - Runbook

further_reading:
    - resource:
        title: Arm Confidential Compute Architecture
        link: https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture
        type: website
    - resource:
        title: Arm Confidential Compute Architecture open source enablement
        link: https://www.youtube.com/watch?v=JXrNkYysuXw
        type: video
    - resource:
        title: Learn the architecture - Realm Management Extension
        link: https://developer.arm.com/documentation/den0126
        type: documentation
    - resource:
        title: Realm Management Monitor specification
        link: https://developer.arm.com/documentation/den0137/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

