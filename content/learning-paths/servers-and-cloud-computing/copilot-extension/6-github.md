---
title: Configuring with GitHub
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now we need to create a Copilot extension on GitHub to connect to our deployed application.

## Creating a GitHub app

> For the most up to date instructions, follow the [official documentation for creating a GitHub App for Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension#creating-a-github-app).

On any page of [GitHub](https://github.com/), click your profile picture and go to Settings. Scroll down to developer settings, and create a GitHub App.

Your GitHub App must have:
    - A name
    - A homepage URL
    - Webhooks deselected

After you create your app, click **Install App** in the sidebar, then install your app on your account.

## Configure GitHub App for Copilot Extension

> For the most up to date instructions, follow the [official documentation for configuring your GitHub App for Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/configuring-your-github-app-for-your-copilot-extension#configuring-your-github-app).

Make the following changes to your GitHub App settings:

- In the "General" settings, in the "Callback URL" field, paste the local address for your agent.
- In the "Permissions & events" settings, grant read-only permissions to Copilot Chat.
- In the "Copilot" settings, set your app type to "Agent," then fill out the remaining fields.

After you update your GitHub App settings, you can start chatting with your extension by typing @YOUR-EXTENSION-NAME in the Copilot Chat window, then sending a prompt as normal.

## Create Client ID and Secret

## Input Callback Endpoints

## OPTIONAL: Register the extension with the marketplace