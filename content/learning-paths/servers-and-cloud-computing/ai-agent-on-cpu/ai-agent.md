---
title: Introduction to AI Agents and Agent Use Cases
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview of AI Agents

An AI agent is an integrated system that extends beyond basic text generation by augmenting Large Language Models (LLMs) with tools and domain knowledge. 

Here’s a closer look at the underlying elements:

- **System**: Each AI agent functions as an interconnected ecosystem of components. Below is a list of key factors and components that affect system performance:   
  - **Environment**: The domain in which the AI Agent operates. For instance, in a system that books travel itineraries, this might include airline reservation systems and hotel booking tools.  
  - **Sensors**: The methods the AI agent uses to observe its environment. For a travel agent, these might be APIs that inform the agent about seat availability on flights or room occupancy in hotels.  
  - **Actuators**: Ways the AI agent exerts influence within the environment. In the example of a travel agent, placing a booking or modifying an existing reservation illustrates how actuators function to enact changes within the environment.  

- **Large Language Models**: While agents have long existed, LLMs enhance these systems with powerful language comprehension and data-processing capabilities.  
- **Action Execution**: Rather than just produce text, LLMs within an agent context interpret user instructions and interact with tools to achieve specific objectives.  
- **Tools**: The agent’s available toolkit depends on the software environment and developer-defined boundaries. In the travel agent example in this Learning Path, these tools might be limited to flight and hotel reservation APIs.  
- **Knowledge**: Beyond immediate data sources, the agent can fetch additional details - perhaps from databases or web services - for enhanced decision making.



## Types of AI Agents

AI Agents come in multiple forms. The table below provides an overview of some agent types and examples of their roles in a travel booking system:

| **Agent Category**       | **Key Characteristics**                                                             | **Example Usage in a Travel Booking System**                                                                                                                   |
|--------------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Simple Reflex Agents** | Act directly based on predefined rules or conditions.                                      | Filters incoming messages and forwards travel-related emails to a service center.                                                       |
| **Model-Based Agents**   | Maintain an internal representation of the world and update it based on new inputs.  | Monitors flight prices and flags dramatic fluctuations, guided by historical data.                                                      |
| **Goal-Based Agents**    | Execute actions with the aim of meeting designated objectives.                       | Determines the necessary route (flights, transfers) to get from your current location to your target destination.                       |
| **Utility-Based Agents** | Use scoring or numerical metrics to compare and select actions that fulfill a goal. | Balances cost versus convenience when determining which flights or hotels to book.                                                      |
| **Learning Agents**      | Adapt over time by integrating lessons from previous feedback or experiences.        | Adjusts future booking suggestions based on traveler satisfaction surveys.                                                              |
| **Hierarchical Agents**  | Split tasks into sub-tasks and delegate smaller pieces of work to subordinate agents.| Cancels a trip by breaking down the process into individual steps, such as canceling a flight, a hotel, and a car rental.               |
| **Multi-Agent Systems**  | Involve multiple agents that might cooperate or compete to complete tasks.             | Cooperative: Different agents each manage flights, accommodations, and excursions. Competitive: Several agents vie for limited rooms.   |


## Ideal Applications for AI Agents

AI agents come in multiple forms. They can be grouped into various categories and excel in a wide range of applications:

- **Open-Ended Challenges**: Complex tasks with no predetermined procedure, requiring the agent to determine its own steps.  
- **Procedural or Multi-Step Tasks**: Tasks involving multiple phases or tool integrations that enable the agent to switch between resources.  
- **Continual Improvement**: Contexts where feedback loops enable the agent to refine its behavior for better outcomes.
