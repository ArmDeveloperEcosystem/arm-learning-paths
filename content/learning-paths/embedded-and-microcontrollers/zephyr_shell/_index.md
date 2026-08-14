---
title: Create an interactive shell for Zephyr RTOS on Arm Cortex-M

description: Learn how to enable and configure the Zephyr shell subsystem on Arm Cortex-M, then build and run MQTT and UART shell backend examples using Workbench for Zephyr in Visual Studio Code.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded developers who want to add an interactive command-line shell to a Zephyr RTOS application on Arm Cortex-M.

learning_objectives:
    - Enable and tailor Zephyr shell (Kconfig/prj.conf) to produce a minimal CLI footprint
    - Build and flash shell-enabled Zephyr apps using MQTT and UART shell backends on an Arm Cortex-M board
    - Use the Zephyr shell for board bring-up, diagnostics, and interactive testing

prerequisites:
    - Basic familiarity with embedded C programming
    - Visual Studio Code with the Workbench for Zephyr extension installed and configured
    - Docker Desktop, Docker Engine, or another Docker-compatible runtime installed on your host computer (for the MQTT shell example, if you're not installing Mosquitto on host)
    - A Zephyr-supported Arm Cortex-M board (for example, NXP FRDM-MCXN947)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T19:03:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 79914e86f5106d018bbbf251c30941dae38e584851067c5007097d6d4c9c2b54
  summary_generated_at: '2026-08-13T19:03:28Z'
  summary_source_hash: 79914e86f5106d018bbbf251c30941dae38e584851067c5007097d6d4c9c2b54
  faq_generated_at: '2026-08-13T19:03:28Z'
  faq_source_hash: 79914e86f5106d018bbbf251c30941dae38e584851067c5007097d6d4c9c2b54
  summary: >-
    You'll enable and configure the Zephyr shell on an Arm Cortex-M board with Workbench for Zephyr.
    First, you'll update `prj.conf` for the shell and selected MQTT or UART backend. Then, you'll
    build and flash from Visual Studio Code, verify the shell prompt, and use built-in modules for
    bring-up and diagnostics over Ethernet or USB serial.
  faqs:
  - question: How do I know the Zephyr shell is enabled and working after I flash the board?
    answer: >-
      You should see a shell prompt on the selected backend after boot. Run a built-in command
      such as `kernel version` to confirm the shell responds.
  - question: Do I need to add networking code in main.c for the MQTT shell example?
    answer: >-
      No. The MQTT example starts the shell, network stack, DHCP client, and MQTT shell backend
      from configuration options in `prj.conf`.
  - question: Which backend should I use if I want to interact locally during bring-up?
    answer: >-
      Use the UART shell backend. It maps shell input and output to the active UART console over
      the board’s USB serial interface and doesn't require network connectivity.
  - question: What should I check if I don’t see any shell output over UART?
    answer: >-
      Verify that the UART shell backend is enabled in `prj.conf` and that you're connected to
      the board’s USB serial interface selected as the active console. Use a serial terminal application
      supported on your host OS to view the console.
  - question: What should I check if the MQTT shell doesn't connect to the broker?
    answer: >-
      Confirm `CONFIG_SHELL_BACKEND_MQTT` is enabled and that required networking options are set
      in `prj.conf` so the device can obtain network connectivity. Ensure the MQTT broker is reachable
      from the board over Ethernet.
# END generated_summary_faq

author: 
    - Ayoub Bourjilat
    - Odin Shen
    - Akash Malik

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: RTOS Fundamentals
armips:
    - Cortex-M
operatingsystems:
    - RTOS
tools_software_languages:
    - Zephyr
    - C

further_reading:
    - resource:
        title: Zephyr Project Documentation
        link: https://docs.zephyrproject.org/latest/index.html
        type: documentation
    - resource:
        title: Workbench for Zephyr Official Website
        link: https://z-workbench.com/
        type: website
    - resource:
        title: Zephyr Shell subsystem documentation
        link: https://docs.zephyrproject.org/latest/services/shell/index.html
        type: documentation
    - resource:
        title: AC6 Zephyr Training
        link: https://www.ac6-training.com/en/cours.php/cat_oRT/ref_oRT5/zephyr-rtos-programming
        type: website

# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
