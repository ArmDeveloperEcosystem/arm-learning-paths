---
title: Simulate OpenBMC and UEFI pre-silicon on Neoverse RD-V3

minutes_to_complete: 120

who_is_this_for: This advanced topic is for firmware developers, platform software engineers, and system integrators working on Arm Neoverse-based platforms. It is especially useful for developers exploring pre-silicon development, testing, and integration of Baseboard Management Controllers (BMC) with UEFI firmware. If you are building or validating server-class reference platforms such as RD-V3, before hardware is available, this Learning Path shows you how to simulate and debug the full boot path using Fixed Virtual Platforms (FVPs).

learning_objectives:
  - Understand the role of OpenBMC and UEFI in the Arm server boot flow
  - Simulate the firmware using the RD-V3 FVP
  - Build and launch OpenBMC and UEFI images on the RD-V3 FVP
  - Validate host–BMC communication using UART and Serial over LAN (SoL)
  - Implement and validate a custom IPMI command in OpenBMC

prerequisites:
  - An Arm Neoverse-based Linux machine (cloud or local) running Ubuntu 22.04 LTS
  - At least 80 GB free disk space and 48 GB RAM
  - Working knowledge of Docker, Git, and common Linux terminal tools
  - Basic understanding of the server firmware stack (such as UEFI, BMC, and TF-A)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:42:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 285ebf154e6d58463132fc7914c672250ff2d66d0657710ec7eebd557386cbd4
  summary_generated_at: '2026-10-01T19:42:25Z'
  summary_source_hash: 285ebf154e6d58463132fc7914c672250ff2d66d0657710ec7eebd557386cbd4
  faq_generated_at: '2026-10-01T19:42:25Z'
  faq_source_hash: 285ebf154e6d58463132fc7914c672250ff2d66d0657710ec7eebd557386cbd4
  summary: >-
    Simulate an Arm server boot flow on the Neoverse RD-V3 r1 Fixed Virtual Platform (FVP). You
    build OpenBMC and host UEFI images in a Docker environment, launch the FVP, and follow the
    firmware logs through multiple UART consoles. You then bridge virtual UARTs to validate Serial
    over LAN communication. Finally, you add a C++ Intelligent Platform Management Interface
    (IPMI) handler to OpenBMC, rebuild the image, and verify its response.
  faqs:
  - question: What result should I expect when the RD-V3 FVP starts?
    answer: >-
      Multiple UART consoles open in separate terminal windows for different subsystems, such
      as Neoverse V3, Cortex-M55, Cortex-M7, and the Cortex-A BMC. You should see boot logs for
      both the BMC and host UEFI across these consoles.
  - question: The FVP UART consoles do not appear over SSH. What should I check?
    answer: >-
      The consoles are graphical terminals and require a desktop session. If you are connected
      over SSH only, the windows won't render; launch the simulation from a desktop session.
  - question: Which ports should I bridge to enable Serial over LAN (SoL)?
    answer: >-
      Use the provided bridge: `socat -x tcp:localhost:5005 tcp:localhost:5067`. Verify that these
      port mappings match the endpoints exposed by your running simulation.
  - question: After creating the UART bridge, what should I see when opening the host console
      from the BMC web UI?
    answer: >-
      The host console should be accessible through SoL and display the host’s console output.
      You should see ongoing boot messages or a prompt from the host side.
  - question: How do I validate that my custom IPMI command works?
    answer: >-
      Issue the command using `ipmitool` and check for the expected simple string response. If the
      response is not returned, ensure the C++ handler is integrated and rebuild the OpenBMC image
      before re-running the simulation.
# END generated_summary_faq

author:
  - Odin Shen
  - Ken Zhang

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
  - Neoverse
tools_software_languages:
  - C
  - Docker
  - FVP
  - OpenBMC
  - Yocto/BitBake
  - ipmitool
operatingsystems:
  - Linux

further_reading:
  - resource:
      title: Reference Design software stack architecture
      link: https://neoverse-reference-design.docs.arm.com/en/latest/about/software_stack.html
      type: website
  - resource:
      title: OpenBMC website
      link: https://www.openbmc.org/
      type: website
  - resource:
      title: Meta FVP base (OpenBMC)
      link: https://github.com/openbmc/openbmc/tree/master/meta-evb/meta-evb-arm/meta-evb-fvp-base
      type: website
  - resource:
      title: OpenBMC on FVP PoC
      link: https://gitlab.arm.com/server_management/PoCs/fvp-poc
      type: website
  - resource:
      title: ipmitool documentation
      link: https://linux.die.net/man/1/ipmitool
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
