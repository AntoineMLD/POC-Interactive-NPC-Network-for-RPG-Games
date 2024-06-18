import pandas as pd
import networkx as nx
import os

def load_graph_from_csv(csv_path):
    # Load the CSV file
    df = pd.read_csv(csv_path)
    
    # Create the graph
    G = nx.Graph()
    
    # Add nodes and edges from the CSV
    for index, row in df.iterrows():
        G.add_node(row['NPC'], role=row['Role'])
        # Add relationships based on context or other columns
        if 'Rumor/Action' in row and pd.notna(row['Rumor/Action']):
            G.add_edge(row['NPC'], row['Rumor/Action'], relationship=row['Context'])
    
    return G, df

def simulate_interaction(npc, dialogue, df):
    role = df[df['NPC'] == npc]['Role'].iloc[0] if not df[df['NPC'] == npc].empty else "Unknown"
    interaction = f"{npc} ({role}): {dialogue}"
    print(interaction)
    return interaction

def propagate_rumor(graph, start_node, rumor):
    nx.set_node_attributes(graph, {start_node: rumor}, 'rumor')
    propagations = []
    for neighbor in graph.neighbors(start_node):
        graph.nodes[neighbor]['rumor'] = rumor
        propagation = f"Rumor propagated from {start_node} to {neighbor}: {rumor}"
        print(propagation)
        propagations.append(propagation)
    return propagations

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
    G, df = load_graph_from_csv(csv_path)
    
    # Example of interaction simulation
    simulate_interaction("Healer", "Thank you for your help with these rare herbs.", df)
    simulate_interaction("Merchant", "The Healer told me that you helped him.", df)
    simulate_interaction("Blacksmith", "The Merchant spoke of your valuable assistance.", df)
    
    # Execute rumor propagation
    propagate_rumor(G, "Healer", "The player helped the Healer with some rare herbs.")
    propagate_rumor(G, "Blacksmith", "The player found a magical sword.")
