---
title: Introduction to AI Agents and Agent Use Cases
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Defining AI Agents

An AI Agent is best understood as an integrated system that goes beyond standard text generation by equipping Large Language Models (LLMs) with tools and domain knowledge. Here’s a closer look at the underlying elements:

- **System**: Each AI Agent functions as an interconnected ecosystem of components.  
  - **Environment**: The domain in which the AI Agent operates. For instance, in a system that books travel itineraries, the relevant environment might include airline reservation systems and hotel booking tools.  
  - **Sensors**: Methods the AI Agent uses to observe its surroundings. In the travel scenario, these could be APIs that inform the agent about seat availability on flights or room occupancy in hotels.  
  - **Actuators**: Ways the AI Agent exerts influence within that environment. In the example of a travel agent, placing a booking or modifying an existing reservation serves as the agent’s “actuators.”  

- **Large Language Models**: While the notion of agents is not new, LLMs bring powerful language comprehension and data-processing capabilities to agent setups.  
- **Performing Actions**: Rather than just produce text, LLMs within an agent context interpret user instructions and interact with tools to achieve specific objectives.  
- **Tools**: The agent’s available toolkit depends on the software environment and developer-defined boundaries. In the travel agent example, these tools might be limited to flight and hotel reservation APIs.  
- **Knowledge**: Beyond immediate data sources, the agent can fetch additional details—perhaps from databases or web services—to enhance decision-making.

---

## Varieties of AI Agents

AI Agents come in multiple forms. The table below provides an overview of some agent types and examples illustrating their roles in a travel-booking system:

| **Agent Category**       | **Key Characteristics**                                                             | **Example in Travel**                                                                                                                   |
|--------------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Simple Reflex Agents** | Act directly based on set rules or conditions.                                      | Filters incoming messages and forwards travel-related emails to a service center.                                                       |
| **Model-Based Agents**   | Maintain an internal representation of the world and update it based on new inputs.  | Monitors flight prices and flags dramatic fluctuations, guided by historical data.                                                      |
| **Goal-Based Agents**    | Execute actions with the aim of meeting designated objectives.                       | Figures out the necessary route (flights, transfers) to get from your current location to your target destination.                       |
| **Utility-Based Agents** | Use scoring or numerical metrics to compare and select actions that fulfill a goal. | Balances cost versus convenience when determining which flights or hotels to book.                                                      |
| **Learning Agents**      | Adapt over time by integrating lessons from previous feedback or experiences.        | Adjusts future booking suggestions based on traveler satisfaction surveys.                                                              |
| **Hierarchical Agents**  | Split tasks into sub-tasks and delegate smaller pieces of work to subordinate agents.| Cancels a trip by breaking down the process into individual steps, such as canceling a flight, a hotel, and a car rental.               |
| **Multi-Agent Systems**  | Involve multiple agents that may cooperate or compete to complete tasks.             | Cooperative: Different agents each manage flights, accommodations, and excursions. Competitive: Several agents vie for limited rooms.   |

---

## Ideal Applications for AI Agents

While the travel scenario illustrates different categories of AI Agents, there are broader circumstances where agents truly excel:

- **Open-Ended Challenges**: Complex tasks with no predetermined procedure, requiring the agent to determine the necessary steps.  
- **Procedural or Multi-Step Tasks**: Endeavors requiring numerous phases or tool integrations, allowing the agent to switch between resources.  
- **Continual Improvement**: Contexts where feedback loops enable the agent to refine its behaviors for better outcomes in the future.
