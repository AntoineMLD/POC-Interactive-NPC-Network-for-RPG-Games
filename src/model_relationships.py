import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os

def model_relationships(csv_path):
    df = pd.read_csv(csv_path)

    # Create the graph of interactions between NPCs
    G = nx.Graph()

    # Add nodes for each NPC
    for npc in df['NPC'].unique():
        G.add_node(npc, role=df[df['NPC'] == npc]['Role'].iloc[0])

    # Add edges based on interactions described in the CSV file
    for index, row in df.iterrows():
        if pd.notna(row['Rumor/Action']):
            G.add_edge(row['NPC'], row['Rumor/Action'], context=row['Context'])

    return G

def plot_relationships(graph):
    # Position the nodes of the graph for visualization
    pos = nx.spring_layout(graph)

    # Draw the graph
    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='grey', node_size=2000, font_size=10, font_weight='bold')

    # Add labels to the edges to show the context of interactions
    edge_labels = nx.get_edge_attributes(graph, 'context')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.title("Graph of Interactions between NPCs in Valoria")
    plt.show()

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
    G = model_relationships(csv_path)
    plot_relationships(G)
