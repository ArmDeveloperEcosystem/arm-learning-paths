---
title: CMSIS Developer Assistant
description: Install CMSIS Developer Assistant in VS Code on Windows, Linux or macOS, connect an AI coding agent, and verify CMSIS project and debugger access.
minutes_to_complete: 30
author: Matt Cossins
official_docs: https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant
additional_search_terms:
  - MCP
  - Codex
  - Cortex-M
  - embedded development
  - AI agent
weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

The CMSIS Developer Assistant is an MCP Server that connects your AI coding agent to CMSIS tools in Visual Studio Code. Your agent can configure projects, build and program firmware, and inspect Arm Cortex-M targets and Ethos-U accelerators.

This guide covers installation of the tool, as well as recommendations on how to get the most value out of it, and suggestions for use-cases and prompts to try.

You can use it for the following tasks:

| Capability | What you can ask the connected agent to do |
|---|---|
| Learning and tutoring | Explain unfamiliar code, project settings and peripheral behaviour. Ask follow-up questions, request a step-by-step walkthrough, or have it check your understanding. |
| Project creation and board setup | Find board and device support, start from a compatible example, configure a compiler and debugger, or add targets and board layers to an existing project. |
| Application development | Propose a design, write or adapt application code, and integrate drivers or software components using the selected platform's support. |
| Building and deployment | Build firmware, investigate compiler errors, program a supported board, or run an application on an FVP. |
| Live debugging and verification | Set breakpoints, step through code, inspect variables, memory, registers and call stacks, investigate faults, and verify a repair on the target. |
| Documentation lookup | Search available device manuals, datasheets and errata, and explain peripheral settings with references to the relevant pages. |
| Build analysis | Inspect memory usage, linker sections and symbols to understand the generated application. |
| Serial communication | Read application output and exchange data with the target through its serial port. |
| Test automation | Create GitHub Actions workflows for CMSIS solution builds and supported FVP tests. |

![An AI agent connects through CMSIS Developer Assistant to CMSIS Solution, CMSIS Debugger, packs and documentation, and skills, with feedback from a Cortex-M or Ethos-U target.#center](/install-guides/_images/cmsis-developer-assistant-workflow.png "CMSIS Developer Assistant connects the agent to development tools and the target")

## Before you begin

Install desktop VS Code from the [Visual Studio Code download page](https://code.visualstudio.com/download), selecting your host operating system and architecture.

Install and sign in to an MCP-capable coding agent. The extension has been tested with [Codex CLI](/install-guides/codex-cli/), [Claude Code](/install-guides/claude-code/), [GitHub Copilot](/install-guides/github-copilot/), and Kimi Code.

## Install the extension

Use the shortcut for your operating system to open the Command Palette in VS Code:

{{< tabpane-normal >}}
  {{< tab header="Windows / Linux" >}}

Press **Ctrl+Shift+P** to open the Command Palette.

  {{< /tab >}}
  {{< tab header="macOS" >}}

Press **Cmd+Shift+P** to open the Command Palette.

  {{< /tab >}}
{{< /tabpane-normal >}}

Open the VS Code Extensions view. Find [CMSIS Developer Assistant, published by Arm](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-developer-assistant), and install it.

![CMSIS Developer Assistant Marketplace listing showing Arm as the verified publisher and the Install button.#center](/install-guides/_images/install_cmsis_mcp.png)

{{% notice Install from CLI %}}
Alternatively, if the VS Code `code` command is on your path, run the following in PowerShell on Windows or a terminal on Linux/macOS:

```console
code --install-extension arm.cmsis-developer-assistant
```

Reload VS Code when prompted. Confirm installation from the same host environment:

```console
code --list-extensions
```

The list should contain the extension identifier, ignoring capitalization:

```output
arm.cmsis-developer-assistant
```
{{% /notice %}}

## Install the CMSIS tools

With Developer Assistant installed, install the [Arm Keil Studio for VS Code extension pack](/install-guides/keilstudio_vs/). It provides CMSIS Solution, CMSIS Debugger and Arm Tools Environment Manager for creating, building and debugging projects.

Follow the linked guide's extension-pack installation steps. Return here once the extensions are installed. When you create or open a CMSIS project below, complete any tool installation and licence prompts shown by Arm Tools Environment Manager. The required tools depend on the project.

## Connect your coding agent

Open a project folder you intend to use and trust it when VS Code prompts you. From the Command Palette, run **CMSIS Developer Assistant: Configure Agent** and choose your agent. Review the configuration and agent-rule changes offered by the extension before accepting them.

Restart the agent session so it can load the updated configuration. Leave VS Code running while using Developer Assistant.

In the agent chat, enter:

```input
/cmsis-help
```

If the agent does not expose slash commands, ask:

```input
Check my CMSIS Developer Assistant setup. Report whether you can reach its MCP tools and find the procedure for creating a project for a supported board.
```

The agent should report a working connection and available CMSIS workflows:

| Command | Use it for |
|---|---|
| `/cmsis-bootstrap` | Start from an empty VS Code window and get a project building and debugging. |
| `/cmsis-project` | Create, extend or retarget CMSIS and Zephyr projects. |
| `/add-board-layer` | Add a board layer to an existing csolution. |
| `/cmsis-debug-live` | Investigate faults, hangs, wrong values or silent peripherals on hardware. |
| `/cmsis-pack-docs` | Look up registers, peripherals, errata and board facts with page citations. |
| `/create-csolution-github-action` | Add continuous integration for builds or FVP tests. |
| `/cmsis-help` | Show available capabilities. |

Ask it to list the VS Code windows through Developer Assistant and identify your workspace. If several windows are open, select the intended one using **CMSIS Developer Assistant: Select Target Window**, or ask the agent to pin it.

## Using CMSIS Developer Assistant

A good way to use CMSIS Developer Assistant, is to start by describing your goal and constraints. Ask the agent to propose an approach and measurable test criteria, then review them before implementation. The agent can build, run and inspect the application through the CMSIS tools, use target observations to investigate failures, and verify changes against the agreed criteria. Review any source changes and results before accepting the application, and ask the agent to support its explanations and conclusions with source references, available documentation and target observations. 

You are now ready to start using the CMSIS Developer Assistant. For some suggestions on prompts and use-cases to try, see the optional sections below.

## (Optional) Use-cases and prompts to try

### Create a Blinky project on a Cortex-M FVP

An Arm Fixed Virtual Platform (FVP) simulates a target system on the host. The [Corstone-320 FVP](https://arm-software.github.io/AVH/main/simulation/html/index.html) includes Cortex-M85 and Ethos-U85.

Follow the [Arm FVP installation guide](/install-guides/fm_fvp/) for your chosen FVP and host. On macOS, use [AVH FVPs on macOS](/install-guides/fvps-on-macos/) for the Docker wrapper and its prerequisites.

Complete the relevant guide's installation and licence steps before continuing. Give the agent the FVP executable path and say whether it runs natively or in a container. Ask it to use the FVP setup procedure available through `/cmsis-help` to configure the CMSIS debugger connection.

After telling your agent where to find the FVP, ask your agent to use CMSIS Developer Assistant, and create a Blinky example:

```input
Use CMSIS Developer Assistant to create a Blinky example for the installed FVP. Ask me if you are unsure which FVP or where it is installed. Configure the simulation debugger through CMSIS Solution, build and start the model, and stop at main. Then verify the example's LED state changes through a supported model display or debugger-visible peripheral state. Report the selected example, target, breakpoint and observed state. If this model/example combination or debug connection is unsupported, report the missing requirement.
```

The agent should create and build a Blinky project for your FVP, start the simulation, and stop at `main`. After continuing, the simulated LED state should change as described by the example. The agent should confirm this and report what it observed.

### Create a Blinky project on a Cortex-M board

If you are using a physical Cortex-M board, the steps are very similar.

Complete the board vendor's initial setup, including any required firmware, debug-access configuration or provisioning. Connect your board and probe.

Tell your agent which board you are using, and how you have connected it. Then give it the following prompt.

```input
Using CMSIS Developer Assistant, create a Blinky example for my board. Ask me if you are unsure which board you should be using. Create the project in a suitable workspace, and ask me to confirm where if necessary, reusing the vendor's board support and startup code. Confirm the selected example and target before programming. Build, load and debug through the CMSIS tools, stop at main, then run the application. Report the build result, breakpoint location and expected LED behaviour. Ask me to handle any tool download, licence or workspace-trust prompts.
```

Answer any required setup questions. Finish by asking the agent to clear its breakpoints and stop debugging.

### Explore your project with the assistant

After either Blinky check, keep the project open and ask the agent to explain how it works:

```input
Using CMSIS Developer Assistant, identify the device, board or FVP, and software packs configured in this project. Explain which peripherals Blinky uses and how the code changes the LED state. Use the project source and available target documentation, and cite the relevant files and manual sections. Tell me if any required documentation is unavailable.
```

The answer should identify your configured target and connect the explanation to its source code and documentation. Check the cited files and references. This verifies that the assistant can retrieve project and device information as well as build and debug.

Continue the conversation as you would with a tutor. Ask for a simpler explanation, question an assumption, or request a walkthrough of a function. For example:

```input
Walk me through the path from main to the LED update, one step at a time. Explain how the update interval is set and how I could verify it with the debugger. Ask me a question to check my understanding before suggesting changes.
```

### Create an AI application running on the Arm Ethos-U NPU

Use an Ethos-U-equipped Cortex-M board, such as an Alif E8 Appkit or DevKit, or use a Corstone FVP. Start with a small model and test inputs supplied by a compatible CMSIS example.

The [CMSIS-Ethos-U integration examples](https://arm-software.github.io/CMSIS-Ethos-U/main/integration/index.html) provide starting points for Ethos-U55, Ethos-U65 and Ethos-U85. Select the example for your accelerator, then use the board support and model configuration for your actual target.

| Target | What the agent must establish |
|---|---|
| FVP | The model executable, supported CMSIS example, accelerator variant and MAC configuration, and simulation debugger connection. Corstone-320 provides an Ethos-U85 target. |
| Physical board | The exact board and core, BSP/DFP, probe, accelerator configuration, accessible memory and any vendor provisioning. |

A model compiled for one target is not automatically suitable for another, even when both use the same Ethos-U variant. The compiled model, driver, linker placement and memory configuration must agree. The agent should reuse verified platform support and report any missing support rather than guess register addresses or reuse another board's binary.

Tell your agent which board or FVP you are using, and how to find it.

Then send this request:

```input
Create a small inference application for Ethos-U. If you are unsure which board or FVP you should use, ask. Once you know, check which Ethos-U configuration it uses. Use CMSIS Developer Assistant to find a compatible CMSIS-Ethos-U example and reuse its board support, runtime and supplied model/test inputs. Confirm the target configuration and test criteria before implementation. Compile the model for this target if required, configure the project and debugger, build, and deploy or start the simulation. Run the supplied inputs and compare the complete outputs with the supplied references using their documented tolerances. Repeat the first input and verify consistent results. Inspect accelerator submission and successful completion so that a correct output alone is not treated as proof of NPU execution. Show the source changes, build result and target evidence when finished. Ask me for required setup actions or information; if platform support is missing, identify it before proceeding.
```

Answer required questions and review the changes and programming actions according to your agent settings. Workspace trust, tool downloads and licence acceptance can still require your input.

Check that:

- The selected board or FVP and Ethos-U configuration match your request.
- The application builds and runs on that target.
- Repeating an input produces consistent output.
- Live target evidence confirms successful NPU execution.

If a check fails, ask the agent to investigate the live target and verify its repair. Successful build and inference return codes alone are insufficient.

### Use an existing application

You can also use Developer Assistant to investigate and debug an existing CMSIS application. Open its solution, select the correct target window, and describe the observed failure and expected behaviour. The agent can use breakpoints, variables, memory and peripheral inspection to collect evidence, propose a repair and verify it on the target.

## Troubleshooting

| Symptom | What to check |
|---|---|
| The extension command is missing | Confirm installation in the active VS Code instance and reload the window. |
| The agent cannot see CMSIS tools | Run Configure Agent again for that agent, then restart its session. Use `/cmsis-help` to check the connection. |
| A new project window is absent from the agent's window list | Check Workspace Trust and tools prompts in that window; allow its extensions to activate before retrying. |
| Calls target another project | Select or pin the intended target window and confirm the reported workspace. |
| The wrong FVP solution is active | In directories containing several solutions, explicitly select the solution for your accelerator and confirm its target. Wait for tool installation to finish before retrying. |
| Build works but debugging does not | Check the selected probe and target, board power and vendor setup. Ask for session status and recent problems before retrying. |
| A continuously running FVP will not pause or stop | If stopping through CMSIS fails, stop only that test model container in Docker Desktop before relaunching. |
| The debugger remains unresponsive | Stop debugging. If needed, reconnect the board/probe and reload the workspace. Collect **CMSIS Developer Assistant: Copy Recent Problems** for a report. |

For additional workflows and configuration details, see the [Developer Assistant documentation](https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant).
