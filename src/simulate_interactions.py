import pandas as pd
import networkx as nx
import os

def load_graph_from_csv(csv_path):
    # Charger le fichier CSV
    df = pd.read_csv(csv_path)
    
    # Créer le graphe
    G = nx.Graph()
    
    # Ajouter des nœuds et des arêtes à partir du CSV
    for index, row in df.iterrows():
        G.add_node(row['PNJ'], role=row['Rôle'])
        # Ajouter des relations basées sur le contexte ou d'autres colonnes
        if 'Rumeur/Action' in row and pd.notna(row['Rumeur/Action']):
            G.add_edge(row['PNJ'], row['Rumeur/Action'], relationship=row['Contexte'])
    
    return G, df

def simulate_interaction(pnj, dialogue, df):
    role = df[df['PNJ'] == pnj]['Rôle'].iloc[0] if not df[df['PNJ'] == pnj].empty else "Unknown"
    interaction = f"{pnj} ({role}): {dialogue}"
    print(interaction)
    return interaction

def propagate_rumor(graph, start_node, rumor):
    nx.set_node_attributes(graph, {start_node: rumor}, 'rumor')
    propagations = []
    for neighbor in graph.neighbors(start_node):
        graph.nodes[neighbor]['rumor'] = rumor
        propagation = f"Rumeur propagée de {start_node} à {neighbor}: {rumor}"
        print(propagation)
        propagations.append(propagation)
    return propagations

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
    G, df = load_graph_from_csv(csv_path)
    
    # Exemple de simulation d'interaction
    simulate_interaction("Guérisseur", "Merci pour votre aide avec ces herbes rares.", df)
    simulate_interaction("Marchand", "Le Guérisseur m'a dit que vous l'avez aidé.", df)
    simulate_interaction("Forgeron", "Le Marchand m'a parlé de votre aide précieuse.", df)
    
    # Exécuter la propagation de rumeur
    propagate_rumor(G, "Guérisseur", "Le joueur a aidé le Guérisseur avec des herbes rares.")
    propagate_rumor(G, "Forgeron", "Le joueur a trouvé une épée magique.")
