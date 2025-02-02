---
title: Learn about GitHub Copilot Extensions
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What are GitHub Copilot Extensions?

Copilot Extensions provide an integration point to expand the functionality of Copilot chat, allowing developers to introduce external tools, services, and custom behaviors into the chat experience. 

You can use an extension to customize the capabilities of Copilot in a variety of ways. Some examples include targeting Copilot for a specific type of user, such as an Arm software developer, by querying specific documentation or prioritizing responses for the developers environment. Copilot Extensions can also integrate additional LLMs, use different APIs, and connect to other AI tools that are not used by Copilot. 

A Copilot Extension allows you to build curated experiences that are targeted for specific developer topics. 

Think about what you want to offer, or build for yourself, that is beyond or better than what Copilot can already do. If you have ideas, you can try them using a Copilot Extension. 

Extensions can be private, public, or shared in the GitHub Marketplace. 

This Learning Path is a "hello world" tutorial for a simple extension in Python. It explains how to create a private extension by running Python on a Linux computer, using ngrok to expose the endpoint, and creating a GitHub App to configure the extension in your GitHub account. After this, you can invoke your private extension from GitHub chat.

## How do I get started with GitHub Copilot?

Before building an extension, make sure Copilot is configured and working in your GitHub account. 

Refer to the [Quickstart for GitHub Copilot](https://docs.github.com/en/copilot/quickstart) to get started.

You can use [GitHub Copilot free](https://github.com/features/copilot?utm_source=topcopilotfree&utm_medium=blog&utm_campaign=launch) at no cost, subject to a usage limit.

## How do I invoke GitHub Copilot Extensions?

You can use extensions on any platform where you can use Copilot chat. This includes the GitHub website, various IDEs, and the command line. 

Extensions are invoked using `@` followed by the name of the extension. For example, the [Arm extension for GitHub Copilot](https://github.com/marketplace/arm-for-github-copilot) is invoked using `@arm` in the chat. 

You can install the Arm extension from the GitHub marketplace and practice using `@arm` to invoke it. Information about how to use it is in the [Arm for GitHub Copilot repository](https://github.com/arm/copilot-extension).

Continue to learn how to create your own extension using Python.

