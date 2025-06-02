---
title: Create GitHub Application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Create a GitHub app

Now you need to create a Copilot extension on GitHub to connect to the deployed application.

For the most up-to-date instructions, follow the official documentation for [Creating a GitHub App for Copilot Extension](https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension/creating-a-github-app-for-your-copilot-extension#creating-a-github-app).

On any page of [GitHub](https://github.com/), click your profile picture and go to **Settings**. 

Scroll down to **Developer Settings**, and go to [Create a GitHub App](https://github.com/settings/apps).

![Create GitHub Application screen](images/githubapp-create.png)

Your GitHub App must have:
- A name.
- A homepage URL.

Make sure **Webhook -> Active** is deselected.

![GitHub App name and URL](images/githubapp-name.png)
![Webhook deselected](images/githubapp-deselected.png)

The rest can be the default values.

Scroll to the bottom and click **Create GitHub App**.

## Get Client ID and Secret

After you create your app, open it up. You will see your Client ID listed under **General -> About**.

![Client ID and Secret](images/githubapp-clientid.png)

Under this is **Client Secrets**. Click **Generate a new client secret** and save the value. Make sure you copy it before it goes away, as you will need it for the next step as part of the Flask application.

## Install Application

Click **Install App** in the sidebar, then install your app onto your account.

![Install](images/githubapp-install.png)
