import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os

def model_relationships(csv_path):
    df = pd.read_csv(csv_path)

    # Créer le graphe des interactions entre les PNJ
    G = nx.Graph()

    # Ajouter des nœuds pour chaque PNJ
    for pnj in df['PNJ'].unique():
        G.add_node(pnj, role=df[df['PNJ'] == pnj]['Rôle'].iloc[0])

    # Ajouter des arêtes basées sur les interactions décrites dans le fichier CSV
    for index, row in df.iterrows():
        if pd.notna(row['Rumeur/Action']):
            G.add_edge(row['PNJ'], row['Rumeur/Action'], context=row['Contexte'])

    return G

def plot_relationships(graph):
    # Positionner les nœuds du graphe pour la visualisation
    pos = nx.spring_layout(graph)

    # Dessiner le graphe
    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='grey', node_size=2000, font_size=10, font_weight='bold')

    # Ajouter des étiquettes aux arêtes pour montrer le contexte des interactions
    edge_labels = nx.get_edge_attributes(graph, 'context')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.title("Graphique des Interactions entre les PNJ à Valoria")
    plt.show()

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
    G = model_relationships(csv_path)
    plot_relationships(G)
