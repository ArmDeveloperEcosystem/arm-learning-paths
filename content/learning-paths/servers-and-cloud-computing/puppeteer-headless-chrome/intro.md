---
title: "Understand headless browser testing with Puppeteer"
description: Understand how headless Chrome and Puppeteer support automated web testing on Arm Linux servers and in GitHub Actions.

weight: 2

layout: "learningpathall"
---

## Headless browsers and why they matter

A headless browser renders pages, executes JavaScript, and processes CSS without opening a browser window. This makes it useful on servers and in containers and CI/CD pipelines without a graphical display.

You can use headless browsers programmatically for automated regression testing after every code change. Headless browsers allow you to perform the following UI tests without needing to check manually:

- Navigate pages
- Fill in forms
- Assert that the right content appears in the UI

You can also run these tests automatically on pull requests to detect the following issues before merging changes:

- Broken pages
- Invalid links
- Missing elements

Besides regression testing, you can use a headless browser to accomplish the following tasks:

- Visual diffing
- Generating PDFs from HTML
- Scraping pages where the content is rendered by JavaScript

## Google Chrome on Arm

Google Chrome holds the largest share of global browser traffic. Running tests against Chrome can therefore give you the highest confidence that your code works for most users. Chrome is available as an arm64 binary for Linux. When you run Chrome on an Arm server, there's no emulation layer between the browser and the CPU. The browser compiles and runs JavaScript with the same V8 engine as Chrome on other platforms, at full original speed. 

## What Puppeteer is

Puppeteer is a Node.js library maintained by the Chrome team. It communicates with Chrome over the DevTools Protocol, a low-level interface that exposes full control over the browser. 

The following are some of the functionalities that the DevTools Protocol exposes: 

- Navigation
- DOM inspection
- Network interception
- Screenshot capture

Puppeteer works with the system-installed Chrome binary, so you don't need a separate browser download on the server.

## What you'll build

You'll install Chrome and Puppeteer on an Arm Linux server running Ubuntu 24.04 or Amazon Linux 2023. Then, you'll write test scripts that run against a locally served Hugo site. To finish, you'll automate those tests with a GitHub Actions workflow that runs on an Arm runner whenever a pull request targets the main branch.

## What you've learned and what's next

You've learned what Puppeteer is, why headless browsers matter, and how you'll implement headless browser testing. 

Next, you'll set up Chrome and Node.js for testing. 
