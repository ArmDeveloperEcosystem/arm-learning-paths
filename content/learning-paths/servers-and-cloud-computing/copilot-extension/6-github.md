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

### In the "General" settings

In the "Callback URL" field, put the URL of your agent you deployed in the previous step.

If you want to test locally and use an ephemeral domain in ngrok, you will need to update this URL every time you restart your ngrok server.

### In the "Permissions & events" settings

Grant read-only permissions to Copilot Chat.

### In the "Copilot" settings

Set your app type to "Agent," then fill out the remaining fields.

## Test it out

After you update your GitHub App settings, you can start chatting with your extension by typing @YOUR-EXTENSION-NAME in the Copilot Chat window, then sending a prompt as normal.

## OPTIONAL: Publish your extension on the marketplace

> For the most up to date instructions, follow the [official documentation for listing your extension on the marketplace](https://docs.github.com/en/copilot/building-copilot-extensions/managing-the-availability-of-your-copilot-extension#listing-your-copilot-extension-on-the-github-marketplace).

If you would like to make your extension public so that anyone can use it, go into your GitHub App advanced settings. 

You will see one of two options:

### Make public

If you see the Make public option, your extension is currently private. It can only be installed by your organization (or the user) that created the app. You can click Make public to allow any other account to install your Copilot Extension, or leave your settings as they are to keep your app private.

### Make private

If you see the Make private option, your extension is currently public. The extension can be installed by any account. You can click Make private to only allow your organization (or user) that created the app to install it, or leave your settings as they are to keep your app public.


