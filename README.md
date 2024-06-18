# Interactive NPC Network for RPG Games

Welcome to the "Interactive NPC Network for RPG Games" project. This repository showcases a proof of concept (PoC) for developing an interactive network of Non-Player Characters (NPCs) within a fictional village setting, where NPCs communicate, propagate rumors, and dynamically influence the game environment.

## Overview

In this project, we created a network of NPCs in the village of Valoria, each with specific roles and the ability to interact with one another. The NPCs can:

- **Communicate**: NPCs can exchange information and engage in dialogues based on various contexts and scenarios.
- **Propagate Rumors**: Information, such as threats or events, can spread through the network, affecting the behavior of other NPCs.
- **Influence the Game in Real-Time**: Interactions and rumors dynamically alter the game's environment and NPC behaviors, providing an immersive experience for players.

## Key Features

1. **Dynamic NPC Dialogues**:
   - Context-aware conversations generated using Natural Language Processing (NLP) to simulate realistic interactions.
   - NPCs respond to the player and each other, providing a rich narrative experience.

2. **Rumor Propagation**:
   - Implementation of a system where rumors and information spread through the NPC network.
   - The propagation of rumors influences NPC behavior and game events in real-time.

3. **Interactive Scenarios**:
   - Simulation of various scenarios, such as village attacks, resource gathering, and festival preparations.
   - NPCs coordinate their actions and responses based on the scenario context.

4. **Visual Representation**:
   - Graphical visualization of the NPC network and their interactions using NetworkX and Matplotlib.
   - Real-time updates to the network as NPCs communicate and propagate information.

## Installation and Setup

To get started with the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AntoineMLD/interactive-npc-network.git
   cd interactive-npc-network

    Create a Virtual Environment:

    bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Dependencies:

bash

pip install -r requirements.txt

Run the Application:

bash

    streamlit run streamlit_app.py

Usage
Simulate NPC Interactions

    Select a Scenario: Choose a scenario such as "Attack", "Resource Gathering", or "Festival" to simulate how NPCs interact in different contexts.
    Propagate Rumors: Input a rumor and see how it spreads through the NPC network, influencing their behaviors.
    Direct NPC Interactions: Select two NPCs and a context for their interaction, and observe the generated dialogue and resulting actions.

Visualize the NPC Network

    Use the provided visualizations to explore how NPCs are connected and how information propagates through the network.
    Track the impact of quests and interactions on the network in real-time.

Project Structure

    dialogues_valoria_enriched.csv: A CSV file containing detailed dialogues, contexts, and emotions for each NPC.
    configure_and_use_openai_api.py: Script to configure and interact with the OpenAI API for generating dialogues.
    simulate_propagation_rumor.py: Script to simulate the propagation of rumors through the NPC network.
    streamlit_app.py: Main application file using Streamlit for interactive visualization and scenario simulation.
    requirements.txt: List of dependencies required to run the project.

Future Enhancements

    Complex NPC Interactions: Expand the scope of NPC interactions to include more complex scenarios and multi-character dialogues.
    Dynamic Real-Time Integration: Integrate the NPC interactions into a real-time game environment.
    Enhanced User Interface: Improve the user interface for better visualization and interaction with the NPC network.

Contributing

We welcome contributions to enhance the NPC interaction system. If you'd like to contribute, please fork the repository and submit a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
Contact

For any questions or feedback, please contact us at your-email@example.com.

Thank you for exploring the Interactive NPC Network for RPG Games project. We hope this PoC inspires further developments in immersive NPC interactions in gaming!
