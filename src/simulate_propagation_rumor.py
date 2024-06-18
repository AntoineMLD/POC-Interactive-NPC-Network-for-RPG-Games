import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os 

def load_graph_from_csv(csv_path):
    df = pd.read_csv(csv_path)

    # Créer le graphe des interactions entre les PNJ
    G = nx.Graph()

    # Ajouter des nœuds pour chaque PNJ
    for pnj in df['PNJ'].unique():
        G.add_node(pnj, role=df[df['PNJ'] == pnj]['Rôle'].iloc[0])

    # Ajouter des arêtes basées sur les interactions décrites dans le fichier CSV
    for index, row in df.iterrows():
        if pd.notna(row['Rumeur/Action']):
            G.add_edge(row['PNJ'], row['Rumeur/Action'], context=row['Contexte_détaillé'])

    return G, df

def propagate_rumor(graph, start_node, rumor):
    # Marquer le nœud de départ avec la rumeur
    nx.set_node_attributes(graph, {start_node: rumor}, 'rumor')

    # Utiliser une file d'attente pour propager la rumeur à travers le graphe
    queue = [start_node]
    propagations = []

    while queue:
        current_node = queue.pop(0)
        for neighbor in graph.neighbors(current_node):
            if 'rumor' not in graph.nodes[neighbor]:  # Propager seulement si le voisin n'a pas déjà reçu la rumeur
                graph.nodes[neighbor]['rumor'] = rumor
                propagations.append(neighbor)
                queue.append(neighbor)
                print(f"Rumeur propagée de {current_node} à {neighbor} : {rumor}")

    return propagations

def visualize_graph(graph):
    pos = nx.spring_layout(graph, k=0.5)  # Ajuster le paramètre k pour espacer les nœuds

    plt.figure(figsize=(14, 10))

    # Vérifier que tous les nœuds ont un rôle défini
    roles = nx.get_node_attributes(graph, 'role')
    for node in graph.nodes():
        if node not in roles or roles[node] is None:
            roles[node] = 'Unknown'  # Attribuer un rôle par défaut

    # Assigner des couleurs en fonction des rôles
    unique_roles = list(set(roles.values()))
    role_colors = {role: plt.cm.tab10(i % 10) for i, role in enumerate(unique_roles)}

    colors = [role_colors[roles[n]] for n in graph.nodes()]

    # Augmenter la taille des nœuds pour certains rôles
    sizes = [1000 if roles[n] in ["Garde", "Seigneur"] else 500 for n in graph.nodes()]  # Augmenter la taille des nœuds importants

    nx.draw_networkx_nodes(graph, pos, node_color=colors, node_size=sizes)
    nx.draw_networkx_edges(graph, pos, edge_color='grey')

    # Ajouter des étiquettes aux arêtes pour montrer le contexte des interactions
    edge_labels = nx.get_edge_attributes(graph, 'context')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10)

    # Ajouter des étiquettes de rumeurs aux nœuds
    node_labels = nx.get_node_attributes(graph, 'rumor')
    nx.draw_networkx_labels(graph, pos, labels=node_labels, font_color='red', font_size=12, font_weight='bold')

    # Ajouter les étiquettes des nœuds avec une police plus grande
    labels = {node: node for node in graph.nodes()}
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=12, font_color='black', font_weight='bold')

    # Ajouter une légende pour les rôles
    plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=role_colors[role], markersize=10, label=role) for role in unique_roles], loc='upper left', title='Rôles')

    plt.title("Propagation de la Rumeur dans le Réseau de PNJ à Valoria", fontsize=15)
    plt.show()

# Si ce script est exécuté directement, exécuter les fonctions principales
if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
    G, df = load_graph_from_csv(csv_path)

    # Exécuter la propagation de la rumeur
    propagate_rumor(G, "Garde", "Une attaque imminente a été signalée.")
    
    # Visualiser le graphe
    visualize_graph(G)
