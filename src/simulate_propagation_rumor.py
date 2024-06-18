import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os 

def load_graph_from_csv(csv_path):
    df = pd.read_csv(csv_path)

    # Create the graph of interactions between NPCs
    G = nx.Graph()

    # Add nodes for each NPC
    for npc in df['NPC'].unique():
        G.add_node(npc, role=df[df['NPC'] == npc]['Role'].iloc[0])

    # Add edges based on interactions described in the CSV file
    for index, row in df.iterrows():
        if pd.notna(row['Rumor/Action']):
            G.add_edge(row['NPC'], row['Rumor/Action'], context=row['Detailed_Context'])

    return G, df

def propagate_rumor(graph, start_node, rumor):
    # Mark the starting node with the rumor
    nx.set_node_attributes(graph, {start_node: rumor}, 'rumor')

    # Use a queue to propagate the rumor through the graph
    queue = [start_node]
    propagations = []

    while queue:
        current_node = queue.pop(0)
        for neighbor in graph.neighbors(current_node):
            if 'rumor' not in graph.nodes[neighbor]:  # Only propagate if the neighbor has not already received the rumor
                graph.nodes[neighbor]['rumor'] = rumor
                propagations.append(neighbor)
                queue.append(neighbor)
                print(f"Rumor propagated from {current_node} to {neighbor}: {rumor}")

    return propagations

def visualize_graph(graph):
    pos = nx.spring_layout(graph, k=0.5)  # Adjust the parameter k to space out the nodes

    plt.figure(figsize=(14, 10))

    # Ensure all nodes have a defined role
    roles = nx.get_node_attributes(graph, 'role')
    for node in graph.nodes():
        if node not in roles or roles[node] is None:
            roles[node] = 'Unknown'  # Assign a default role

    # Assign colors based on roles
    unique_roles = list(set(roles.values()))
    role_colors = {role: plt.cm.tab10(i % 10) for i, role in enumerate(unique_roles)}

    colors = [role_colors[roles[n]] for n in graph.nodes()]

    # Increase the size of the nodes for certain roles
    sizes = [1000 if roles[n] in ["Garde", "Seigneur"] else 500 for n in graph.nodes()]  # Increase the size of important nodes

    nx.draw_networkx_nodes(graph, pos, node_color=colors, node_size=sizes)
    nx.draw_networkx_edges(graph, pos, edge_color='grey')

    # Add labels to edges to show the context of interactions
    edge_labels = nx.get_edge_attributes(graph, 'context')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10)

    # Add rumor labels to nodes
    node_labels = nx.get_node_attributes(graph, 'rumor')
    nx.draw_networkx_labels(graph, pos, labels=node_labels, font_color='red', font_size=12, font_weight='bold')

    # Add node labels with larger font
    labels = {node: node for node in graph.nodes()}
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=12, font_color='black', font_weight='bold')

    # Add a legend for the roles
    plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=role_colors[role], markersize=10, label=role) for role in unique_roles], loc='upper left', title='Roles')

    plt.title("Rumor Propagation in the NPC Network of Valoria", fontsize=15)
    plt.show()

# If this script is run directly, execute the main functions
if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
    G, df = load_graph_from_csv(csv_path)

    # Execute rumor propagation
    propagate_rumor(G, "Garde", "An imminent attack has been reported.")
    
    # Visualize the graph
    visualize_graph(G)
