import pandas as pd
import networkx as nx
from configure_and_use_openai_api import generate_dialogue

# Charger le fichier CSV
df = pd.read_csv("dialogues_valoria.csv")

# Créer le graphe
G = nx.Graph()

# Ajouter des nœuds et des arêtes à partir du CSV
for index, row in df.iterrows():
    G.add_node(row['PNJ'], role=row['Rôle'])
    # Ajouter des relations basées sur le contexte ou d'autres colonnes
    if 'Rumeur/Action' in row and pd.notna(row['Rumeur/Action']):
        G.add_edge(row['PNJ'], row['Rumeur/Action'], relationship=row['Contexte'])

# Fonction pour simuler une interaction entre les PNJ
def simulate_interaction(pnj, dialogue):
    print(f"{pnj} ({df[df['PNJ'] == pnj]['Rôle'].iloc[0]}): {dialogue}")

# Exemple de simulation d'interaction
simulate_interaction("Guérisseur", "Merci pour votre aide avec ces herbes rares.")
simulate_interaction("Marchand", "Le Guérisseur m'a dit que vous l'avez aidé.")
simulate_interaction("Forgeron", "Le Marchand m'a parlé de votre aide précieuse.")

# Propagation de rumeur dans le réseau de PNJ
def propagate_rumor(graph, start_node, rumor):
    nx.set_node_attributes(graph, {start_node: rumor}, 'rumor')
    for neighbor in graph.neighbors(start_node):
        graph.nodes[neighbor]['rumor'] = rumor
        print(f"Rumeur propagée de {start_node} à {neighbor}: {rumor}")

# Exécuter la propagation de rumeur
propagate_rumor(G, "Guérisseur", "Le joueur a aidé le Guérisseur avec des herbes rares.")
propagate_rumor(G, "Forgeron", "Le joueur a trouvé une épée magique.")
