---
title: Ask the agent to connect to a phone
description: Install Google's DDP skill, describe the phone you want, approve the cost, and let the agent connect and display its screen.
weight: 4
layout: learningpathall
---

## Install the DDP agent skill

In the workspace from platform setup, install the skill from [Google's DDP agent documentation](https://docs.cloud.google.com/developer-device-platform/agent-skill):

```bash
npx skills add https://github.com/google/skills --skill developer-device-platform-basics
```

Choose your coding agent and a project-local installation. Start a fresh agent session in this workspace so it discovers the skill, and confirm that `developer-device-platform-basics` appears among its available skills.

The skill teaches the agent how to find and reserve a device, manage the session, and establish the connection. You can now describe the phone you want in natural language.

## Ask for a phone and its screen

With your agent using the Google Cloud project you verified on the previous page, give it this prompt:

```text
Use the DDP skill and my configured Google Cloud project to connect
to a Pixel 11 with the latest stable Android version available.
Keep the session within 20 minutes and US$3, ask me to approve the
cost, and show me the phone's screen with scrcpy.
```

The agent can look up the current device configuration, check availability, and prepare the connection. You don't need to translate your request into catalog IDs, Android API levels, or connection commands. If the requested phone or Android version isn't available, the agent should explain the options before reserving an alternative.

{{% notice Note %}}
As with all prompts, you may need to provide more details depending on the agent you're using. The reference experiment in this Learning Path used GPT-6.1 Sol in High mode. Other agents and reasoning settings haven't been tested. Describe any missing behavior or error to your agent so it can investigate.
{{% /notice %}}

## Approve the reservation

The DDP skill asks for explicit approval before creating a billable session. Review the project, phone, Android version, duration, and estimated cost that the agent proposes. Check [Google's current DDP price](https://cloud.google.com/products/developer-device-platform#pricing), then answer the agent's approval question. If the proposed session would exceed your budget, reduce the duration before approving it.

Keep the approval to one session within the prompt's limits. The agent should set the expiration, connect to the reserved phone, and report when the session ends. Complete any sign-in or consent steps yourself.

The agent handles the reservation and connection through Google's DDP skill. Keep it running while you use the phone.

## Try the connected phone

The scrcpy window should show the reserved phone's current screen. Check that the agent's reported model and Android version match the reservation you approved.

Click to tap, drag to swipe, and use your keyboard to type into a text field. Try opening the app drawer and returning to the home screen. The agent can also save and inspect a screenshot through the same connection:

<img src="/learning-paths/mobile-graphics-and-gaming/google-ddp-get-started/images/ddp-connected-phone.jpg" width="240" alt="Home screen of the remote Pixel 11 captured through its exact ADB connection. Seeing the phone screen confirms the screenshot route works before the agent starts interacting with Termux." title="Inspect a real screenshot from the reserved phone" class="content-uploaded-image centered" />
<span class="content-image-caption centered">Inspect a real screenshot from the reserved phone</span>

If the screen doesn't appear or control doesn't work, describe what happened to the agent. It can inspect the connection, correct the viewer settings, and try again within the existing session. You can review its observations without managing ports or issuing device commands yourself.

## See what the agent handled

Your request gave the agent a device, an outcome, and spending limits. It translated that into device discovery, a reservation, a connection, and a working screen. Its report should include the session expiration and the location of a saved screenshot, along with enough device information to confirm that it connected to the phone you approved.

Keep the same agent conversation open for the TinyStories experiment on the next page. The agent will use this connection to install the tools, choose compatible Arm optimizations, measure their effect, and release the phone.

If you stop here, ask the agent to release this session and confirm that it has ended. Closing the viewer alone doesn't release the reservation.

## What you've accomplished and what's next

You've installed the DDP skill, requested a phone in natural language, approved its cost, and interacted with the remote device. Next, you'll describe an Arm performance experiment and let the agent handle its setup and measurements.
