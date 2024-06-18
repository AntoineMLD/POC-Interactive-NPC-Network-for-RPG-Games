import pandas as pd
import networkx as nx

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
print("\nNœuds avec les rumeurs propagées:")
for node, data in G.nodes(data=True):
    if 'rumor' in data:
        print(f"{node} a reçu la rumeur : {data['rumor']}")

# Analyse de l'impact de la propagation des rumeurs
print("\nAnalyse des relations après la propagation de la rumeur:")

# Observer les relations après la propagation de la rumeur
for node in G.nodes():
    neighbors = list(G.neighbors(node))
    print(f"{node} est maintenant connecté à : {neighbors}")

# Analyser les changements de dynamique après la propagation
print("\nAnalyse des relations renforcées après la propagation de la rumeur:")
for node in G.nodes():
    if 'rumor' in G.nodes[node]:
        print(f"{node} a pris des mesures en réponse à la rumeur.")

# Analyser les relations spécifiques pour voir si des nœuds importants ont été affectés
important_pnjs = ["Seigneur", "Garde", "Forgeron", "Chasseur", "Marchand", "Guérisseur"]
print("\nImpact spécifique sur les PNJ importants:")
for pnj in important_pnjs:
    if pnj in G.nodes() and 'rumor' in G.nodes[pnj]:
        print(f"{pnj} a été directement affecté par la rumeur : {G.nodes[pnj]['rumor']}")
