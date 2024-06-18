import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Charger le fichier CSV enrichi des dialogues
df = pd.read_csv("dialogues_valoria.csv")

# Créer le graphe des interactions entre les PNJ
G = nx.Graph()

# Ajouter des nœuds pour chaque PNJ
for pnj in df['PNJ'].unique():
    G.add_node(pnj, role=df[df['PNJ'] == pnj]['Rôle'].iloc[0])

# Ajouter des arêtes basées sur les interactions décrites dans le fichier CSV
for index, row in df.iterrows():
    if pd.notna(row['Rumeur/Action']):
        G.add_edge(row['PNJ'], row['Rumeur/Action'], context=row['Contexte_détaillé'])

# Fonction pour simuler la propagation d'une rumeur dans le réseau de PNJ
def propagate_rumor(graph, start_node, rumor):
    # Marquer le nœud de départ avec la rumeur
    nx.set_node_attributes(graph, {start_node: rumor}, 'rumor')
    
    # Propager la rumeur aux voisins
    for neighbor in graph.neighbors(start_node):
        graph.nodes[neighbor]['rumor'] = rumor
        print(f"Rumeur propagée de {start_node} à {neighbor} : {rumor}")

# Scénario de propagation de la rumeur : Attaque imminente
start_node = "Garde"
rumor = "Une attaque imminente a été signalée."

# Exécuter la propagation de la rumeur
propagate_rumor(G, start_node, rumor)

# Afficher les nœuds avec leurs rumeurs propagées
for node, data in G.nodes(data=True):
    if 'rumor' in data:
        print(f"{node} a reçu la rumeur : {data['rumor']}")

# Visualiser le graphe avec les rumeurs propagées
pos = nx.spring_layout(G, k=0.5)  # Ajuster le paramètre k pour espacer les nœuds

plt.figure(figsize=(14, 10))

# Vérifier que tous les nœuds ont un rôle défini
roles = nx.get_node_attributes(G, 'role')
for node in G.nodes():
    if node not in roles or roles[node] is None:
        roles[node] = 'Unknown'  # Attribuer un rôle par défaut

# Assigner des couleurs en fonction des rôles
unique_roles = list(set(roles.values()))
role_colors = {role: plt.cm.tab10(i % 10) for i, role in enumerate(unique_roles)}

colors = [role_colors[roles[n]] for n in G.nodes()]

# Augmenter la taille des nœuds pour certains rôles
sizes = [1000 if roles[n] in ["Garde", "Seigneur"] else 500 for n in G.nodes()]  # Augmenter la taille des nœuds importants

nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=sizes)
nx.draw_networkx_edges(G, pos, edge_color='grey')

# Ajouter des étiquettes aux arêtes pour montrer le contexte des interactions
edge_labels = nx.get_edge_attributes(G, 'context')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Ajouter des étiquettes de rumeurs aux nœuds
node_labels = nx.get_node_attributes(G, 'rumor')
nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='red', font_size=12, font_weight='bold')

# Ajouter les étiquettes des nœuds avec une police plus grande
labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=12, font_color='black', font_weight='bold')

# Ajouter une légende pour les rôles
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=role_colors[role], markersize=10, label=role) for role in unique_roles], loc='upper left', title='Rôles')

plt.title("Propagation de la Rumeur dans le Réseau de PNJ à Valoria", fontsize=15)
plt.show()
