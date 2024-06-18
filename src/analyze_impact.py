import pandas as pd
import networkx as nx
import os

def analyze_impact(csv_path, start_node, rumor):
    # Load the enriched dialogue CSV file
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

    # Function to propagate the rumor in the NPC network
    def propagate_rumor(graph, start_node, rumor):
        # Use a queue for BFS (Breadth-First Search) to ensure full propagation
        queue = [start_node]
        impacted_nodes = set()
        
        while queue:
            current_node = queue.pop(0)
            impacted_nodes.add(current_node)
            
            # Propagate the rumor to all neighbors
            for neighbor in graph.neighbors(current_node):
                if neighbor not in impacted_nodes:
                    graph.nodes[neighbor]['rumor'] = rumor
                    queue.append(neighbor)
                    impacted_nodes.add(neighbor)
                    print(f"Rumor propagated from {current_node} to {neighbor}: {rumor}")

        return impacted_nodes

    # Execute rumor propagation
    impacted_nodes = propagate_rumor(G, start_node, rumor)

    # Display nodes with their propagated rumors
    print("\nNodes with propagated rumors:")
    for node, data in G.nodes(data=True):
        if 'rumor' in data:
            print(f"{node} received the rumor: {data['rumor']}")

    # Analyze the impact of rumor propagation
    print("\nAnalysis of relationships after rumor propagation:")

    # Observe relationships after the rumor has spread
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        print(f"{node} is now connected to: {neighbors}")

    # Analyze dynamic changes after propagation
    print("\nAnalysis of strengthened relationships after rumor propagation:")
    for node in G.nodes():
        if 'rumor' in G.nodes[node]:
            print(f"{node} took actions in response to the rumor.")

    # Analyze specific relationships to see if important nodes have been affected
    important_npcs = ["Lord", "Guard", "Blacksmith", "Hunter", "Merchant", "Healer"]
    print("\nSpecific impact on important NPCs:")
    for npc in important_npcs:
        if npc in G.nodes() and 'rumor' in G.nodes[npc]:
            print(f"{npc} was directly affected by the rumor: {G.nodes[npc]['rumor']}")

    return list(impacted_nodes)

# Call the function to perform the analysis if this script is executed directly
if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
    analyze_impact(csv_path, "Guard", "An imminent attack has been reported.")
