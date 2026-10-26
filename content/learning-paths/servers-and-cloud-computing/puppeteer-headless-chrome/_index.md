---
title: Run headless browser tests with Puppeteer on Arm Linux

description: Install Chrome and Puppeteer on Arm Linux servers running Ubuntu 24.04 or Amazon Linux 2023, write headless tests against a local Hugo site, and automate them with GitHub Actions on an Arm runner.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers who want to automate web testing with headless Chrome and Puppeteer on Arm-based servers in a CI/CD pipeline.

learning_objectives:
    - Install Chrome and Puppeteer on Ubuntu 24.04 or Amazon Linux 2023 (arm64).
    - Write Puppeteer scripts that navigate a locally served Hugo site, assert on page content, and capture screenshots.
    - Automate Puppeteer tests with GitHub Actions on an Arm runner.

prerequisites:
    - An Arm Linux server running Ubuntu 24.04 or Amazon Linux 2023
    - Basic familiarity with Node.js and npm
    - A GitHub account

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-22T19:03:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 02ddb996ad638737c71583095341f003b414aeb43a3259cdc2f6d99f0b278b27
  summary_generated_at: '2026-10-22T19:03:16Z'
  summary_source_hash: 02ddb996ad638737c71583095341f003b414aeb43a3259cdc2f6d99f0b278b27
  faq_generated_at: '2026-10-22T19:03:16Z'
  faq_source_hash: 02ddb996ad638737c71583095341f003b414aeb43a3259cdc2f6d99f0b278b27
  summary: >-
    You'll run headless Chrome tests with Puppeteer on an Arm Linux server and automate them with
    GitHub Actions. First, you'll install Chrome and Node.js on Ubuntu 24.04 or Amazon Linux 2023.
    Then, you'll run three scripts against a local Hugo site to check page content, validate a
    documentation link, and capture a screenshot. Finally, you'll add a workflow that runs the
    scripts on an Arm runner.
#   faqs:
#   - question: Which Chrome package should I install on my distribution, and how do I verify it
#       installed correctly?
#     answer: >-
#       Use the official arm64 Chrome package that matches your distribution: Debian-based for Ubuntu
#       24.04 or RPM-based for Amazon Linux 2023. After installation, run `google-chrome --version`
#       and expect a Chrome version number.
#   - question: How do I confirm my Node.js version meets Puppeteer’s requirement?
#     answer: >-
#       You need Node.js 18 or later for Puppeteer. Install Node.js v20 as shown, then run
#       `node --version` and `npm --version` to verify the installed versions.
#   - question: What do I need in my repository before writing and running the tests against the
#       Hugo site?
#     answer: >-
#       You authenticate with GitHub using `gh auth login`, then fork and clone the Ecosystem Dashboard
#       for Arm repository. Add your Puppeteer scripts inside the clone so you can commit them for the
#       workflow.
#   - question: How do I verify the GitHub Actions workflow?
#     answer: >-
#       You can trigger it manually with **Run workflow** on the `main` branch. In a successful run,
#       the three test steps and screenshot upload show green check marks, and you can download the
#       `dashboard-screenshot` artifact from the run summary.
#   - question: Which runner architecture should I choose for GitHub Actions?
#     answer: >-
#       Use `runs-on: ubuntu-24.04-arm` to select a GitHub-hosted runner with 64-bit Arm hardware,
#       matching your Arm server's architecture.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Web
armips:
    - Neoverse
tools_software_languages:
    - Chrome
    - Node.js
    - Puppeteer
    - Hugo
    - GitHub Actions
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Chrome install guide
        link: /install-guides/browsers/chrome/
        type: documentation
    - resource:
        title: Puppeteer documentation
        link: https://pptr.dev/
        type: documentation
    - resource:
        title: Puppeteer examples on GitHub
        link: https://github.com/puppeteer/puppeteer/tree/main/examples
        type: website
    - resource:
        title: GitHub Actions on Arm runners
        link: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
