---
title: Create GitHub Application
weight: 20

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now we need to create a Copilot extension on GitHub to connect to our deployed application.

## Create a GitHub app

> For the most up to date instructions, follow the [official documentation for creating a GitHub App for Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension#creating-a-github-app).

On any page of [GitHub](https://github.com/), click your profile picture and go to Settings. Scroll down to developer settings, and create a GitHub App.

Your GitHub App must have:
    - A name
    - A homepage URL
    - Webhooks deselected

## Get Client ID and Secret

After you create your app, open it up. You will see listed your Client ID under General -> About.

Under that is **Client Secrets**, click "Generate a new client secret" and save the value. You will need it for the next step as part of the flash application.

## Install Application

Click **Install App** in the sidebar, then install your app onto your account.
