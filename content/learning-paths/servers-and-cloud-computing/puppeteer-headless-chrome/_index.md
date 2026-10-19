---
title: Run headless browser tests with Puppeteer on Arm Linux
draft: true
cascade:
    draft: true

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

author: Jason Andrews

generate_summary_faq: true
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
