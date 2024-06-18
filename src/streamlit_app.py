import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import sys
import os

# Adding the 'src' directory to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from configure_and_use_openai_api import generate_dialogue

# Load the CSV file into a DataFrame
csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
df = pd.read_csv(csv_path)

# Create the graph of interactions between NPCs
G = nx.Graph()
for npc in df['NPC'].unique():
    G.add_node(npc, role=df[df['NPC'] == npc]['Role'].iloc[0])

# Add additional nodes if necessary
additional_nodes = ["Villager"]
for node in additional_nodes:
    if node not in G:
        G.add_node(node, role="Community")

# Add edges based on the interactions described in the CSV file
for index, row in df.iterrows():
    if pd.notna(row['Rumor/Action']):
        G.add_edge(row['NPC'], row['Rumor/Action'], context=row['Detailed_Context'])

# Initialize missing session state keys
if 'selected_npc' not in st.session_state:
    st.session_state.selected_npc = df['NPC'].unique()[0]

if 'selected_scenario' not in st.session_state:
    st.session_state.selected_scenario = "Attack"

if 'rumor' not in st.session_state:
    st.session_state.rumor = "An imminent attack has been reported."

if 'selected_npc_for_help' not in st.session_state:
    st.session_state.selected_npc_for_help = df['NPC'].unique()[0]

if 'selected_context_for_help' not in st.session_state:
    st.session_state.selected_context_for_help = "attack"

if 'quests' not in st.session_state:
    st.session_state.quests = []

if 'completed_quests' not in st.session_state:
    st.session_state.completed_quests = []

if 'interactions' not in st.session_state:
    st.session_state.interactions = []

# Initialize the keys for interactions between NPCs
if 'interaction_npc1' not in st.session_state:
    st.session_state.interaction_npc1 = df['NPC'].unique()[0]

if 'interaction_npc2' not in st.session_state:
    st.session_state.interaction_npc2 = df['NPC'].unique()[1]

if 'interaction_context' not in st.session_state:
    st.session_state.interaction_context = "resource request"

# Streamlit interface
st.title("Interactive NPC Network in Valoria")

# Show NPC options with state management
st.session_state.selected_npc = st.selectbox(
    "Select an NPC:", df['NPC'].unique(), index=list(df['NPC'].unique()).index(st.session_state.selected_npc)
)

# Display interactions of the selected NPC
if st.button("View Interactions"):
    neighbors = list(G.neighbors(st.session_state.selected_npc))
    st.write(f"{st.session_state.selected_npc} is connected with: {neighbors}")

    # Visualize the graph centered on the selected NPC
    subgraph = G.subgraph([st.session_state.selected_npc] + neighbors)
    pos = nx.spring_layout(subgraph)
    plt.figure(figsize=(8, 6))
    nx.draw(subgraph, pos, with_labels=True, node_color='lightblue', edge_color='grey', node_size=2000, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=nx.get_edge_attributes(subgraph, 'context'))
    st.pyplot(plt)

# Function to propagate rumors in the network
def propagate_rumor(graph, start_node, rumor):
    nx.set_node_attributes(graph, {start_node: rumor}, 'rumor')
    for neighbor in graph.neighbors(start_node):
        graph.nodes[neighbor]['rumor'] = rumor
        st.write(f"Rumor propagated from {start_node} to {neighbor}: {rumor}")

# Propagate rumors starting from the selected NPC
st.session_state.rumor = st.text_input("Enter the rumor to propagate:", st.session_state.rumor)

if st.button("Propagate Rumor"):
    propagate_rumor(G, st.session_state.selected_npc, st.session_state.rumor)

    # Display nodes with their propagated rumors
    st.write("Nodes with propagated rumors:")
    for node, data in G.nodes(data=True):
        if 'rumor' in data:
            st.write(f"{node} received the rumor: {data['rumor']}")

# Real-time scenario simulation
st.header("Scenario Simulation")
scenarios = ["Attack", "Resource Gathering", "Festival"]
st.session_state.selected_scenario = st.selectbox(
    "Choose a scenario to simulate:", scenarios, index=scenarios.index(st.session_state.selected_scenario)
)

if st.button("Simulate Scenario"):
    if st.session_state.selected_scenario == "Attack":
        st.write("Simulating an imminent attack...")
        start_node = "Guard"
        rumor = "An imminent attack has been reported."
        propagate_rumor(G, start_node, rumor)
        st.write("The NPCs are preparing for the attack.")
    elif st.session_state.selected_scenario == "Resource Gathering":
        st.write("Simulating resource gathering...")
        start_node = "Farmer"
        rumor = "The wheat harvest starts today."
        propagate_rumor(G, start_node, rumor)
        st.write("The NPCs are mobilizing for the harvest.")
    elif st.session_state.selected_scenario == "Festival":
        st.write("Simulating the village festival...")
        start_node = "Lord"
        rumor = "The village's annual festival starts tonight."
        propagate_rumor(G, start_node, rumor)
        st.write("The NPCs are preparing for the festival.")

# Generate contextual responses for NPCs
def get_contextual_response(npc, context):
    prompt = f"The player asks {npc} how they can help during {context}. {npc} responds directly to the player:"
    response = generate_dialogue(prompt)
    return response

# Select the NPC and context for the request for help
st.session_state.selected_npc_for_help = st.selectbox(
    "Choose an NPC to ask for help:", df['NPC'].unique(), index=list(df['NPC'].unique()).index(st.session_state.selected_npc_for_help)
)
st.session_state.selected_context_for_help = st.selectbox(
    "Choose the context of the request:", ["attack", "harvest", "festival"], index=["attack", "harvest", "festival"].index(st.session_state.selected_context_for_help)
)

# Function to determine NPCs involved in a quest
def get_npcs_involved_in_quest(start_npc, context):
    involved_npcs = [start_npc]
    if context == "attack":
        involved_npcs += ["Guard", "Blacksmith", "Hunter"]
    elif context == "harvest":
        involved_npcs += ["Farmer", "Merchant"]
    elif context == "festival":
        involved_npcs += ["Lord", "Villager"]
    return involved_npcs

# Use the function in the Streamlit interface
if st.button("Ask for Help"):
    response = get_contextual_response(st.session_state.selected_npc_for_help, st.session_state.selected_context_for_help)
    st.write(f"Response from {st.session_state.selected_npc_for_help}: {response}")

    involved_npcs = get_npcs_involved_in_quest(st.session_state.selected_npc_for_help, st.session_state.selected_context_for_help)
    quest_description = f"Help {st.session_state.selected_npc_for_help} with {st.session_state.selected_context_for_help}."
    quest = {
        "Initiator": st.session_state.selected_npc_for_help,
        "Description": quest_description,
        "Status": "Active",
        "Involved_NPCs": involved_npcs
    }
    st.session_state.quests.append(quest)
    st.write(f"Quest initiated by {st.session_state.selected_npc_for_help} with the NPCs involved {involved_npcs}: {quest_description}")

# Function to initiate interactions between NPCs with a transaction structure
def initiate_npc_interaction(npc1, npc2, context):
    if context == "resource request":
        dialogue_steps = [
            f"{npc1} sends a request to {npc2} to provide the necessary resources.",
            f"{npc2} confirms the availability of resources and sends a response with the quantity and price.",
            f"{npc1} sends the credits to {npc2}.",
            f"{npc2} sends the resources to {npc1}.",
            "The transaction is successfully completed."
        ]
    else:
        dialogue_steps = [f"{npc1} informs {npc2} of {context}. {npc2} reacts accordingly."]

    # Generate and display dialogues for each step
    full_interaction = ""
    for step in dialogue_steps:
        prompt = f"{step} {npc2} responds:"
        response = generate_dialogue(prompt)
        cleaned_response = clean_response(response)
        if not cleaned_response:
            cleaned_response = "The dialogue could not be generated. Please try again or set a default message."
        full_interaction += f"{step} {cleaned_response}\n"

    return full_interaction

def clean_response(response):
    response = response.strip().replace('"', '')
    if response.lower() in ["", "response :"]:
        return None
    return response

# Add direct interactions between NPCs
st.header("Direct Interactions between NPCs")
st.session_state.interaction_npc1 = st.selectbox(
    "Select the first NPC for the interaction:", df['NPC'].unique(), key='npc1', index=list(df['NPC'].unique()).index(st.session_state.interaction_npc1)
)
st.session_state.interaction_npc2 = st.selectbox(
    "Select the second NPC for the interaction:", df['NPC'].unique(), key='npc2', index=list(df['NPC'].unique()).index(st.session_state.interaction_npc2)
)
st.session_state.interaction_context = st.selectbox(
    "Choose the context of the interaction:", ["suspicious presence", "resource request", "harvest planning"], index=["suspicious presence", "resource request", "harvest planning"].index(st.session_state.interaction_context)
)

if st.button("Initiate an Interaction between NPCs"):
    interaction_response = initiate_npc_interaction(st.session_state.interaction_npc1, st.session_state.interaction_npc2, st.session_state.interaction_context)
    st.write(f"Interaction between {st.session_state.interaction_npc1} and {st.session_state.interaction_npc2} on the theme '{st.session_state.interaction_context}':")
    st.write(interaction_response)

    # Add the interaction to the interaction history
    st.session_state.interactions.append((st.session_state.interaction_npc1, st.session_state.interaction_npc2, st.session_state.interaction_context, interaction_response))

# Display the interaction history between NPCs
st.subheader("Interaction History between NPCs")
for interaction in st.session_state.interactions:
    st.write(f"{interaction[0]} informed {interaction[1]} on the theme '{interaction[2]}'. Response: {interaction[3]}")

# Display the quest journal
st.subheader("Quest Journal")
for quest in st.session_state.quests:
    st.write(f"Quest by {quest['Initiator']}: {quest['Description']} - Status: {quest['Status']}")
    st.write(f"NPCs involved: {', '.join(quest['Involved_NPCs'])}")
    if st.button(f"Mark as completed", key=f"complete_{quest['Initiator']}"):
        quest['Status'] = "Completed"
        st.session_state.completed_quests.append(quest)
        st.session_state.quests.remove(quest)
        st.success(f"Quest completed: {quest['Description']}")

# Visualize the impact of quests on the NPC network
if st.session_state.quests or st.session_state.completed_quests:
    st.header("Impact of Quests on the NPC Network")
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='grey', node_size=2000, font_size=10, font_weight='bold')

    # Color nodes with active quests
    active_nodes = [n for n in G.nodes if n in [npc for quest in st.session_state.quests for npc in quest['Involved_NPCs']]]
    nx.draw_networkx_nodes(G, pos, nodelist=active_nodes, node_color='yellow')

    # Color nodes with completed quests
    completed_nodes = [n for n in G.nodes if n in [npc for quest in st.session_state.completed_quests for npc in quest['Involved_NPCs']]]
    nx.draw_networkx_nodes(G, pos, nodelist=completed_nodes, node_color='green')

    plt.title("Impact of Quests on the NPC Network")
    st.pyplot(plt)
