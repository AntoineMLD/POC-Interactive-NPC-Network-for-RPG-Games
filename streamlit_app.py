import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from configure_and_use_openai_api import generate_dialogue

# Charger le fichier CSV enrichi des dialogues
df = pd.read_csv("dialogues_valoria_enriched.csv")

# Créer le graphe des interactions entre les PNJ
G = nx.Graph()
for pnj in df['PNJ'].unique():
    G.add_node(pnj, role=df[df['PNJ'] == pnj]['Rôle'].iloc[0])

# Ajouter explicitement des nœuds supplémentaires si nécessaires
additional_nodes = ["Villageois"]
for node in additional_nodes:
    if node not in G:
        G.add_node(node, role="Communauté")

# Ajouter les arêtes basées sur les interactions
for index, row in df.iterrows():
    if pd.notna(row['Rumeur/Action']):
        G.add_edge(row['PNJ'], row['Rumeur/Action'], context=row['Contexte_détaillé'])

# Initialiser l'état de session pour les interactions et les quêtes
if 'selected_pnj' not in st.session_state:
    st.session_state.selected_pnj = df['PNJ'].unique()[0]

if 'selected_scenario' not in st.session_state:
    st.session_state.selected_scenario = "Attaque"

if 'rumor' not in st.session_state:
    st.session_state.rumor = "Une attaque imminente a été signalée."

if 'selected_pnj_for_help' not in st.session_state:
    st.session_state.selected_pnj_for_help = df['PNJ'].unique()[0]

if 'selected_context_for_help' not in st.session_state:
    st.session_state.selected_context_for_help = "attaque"

if 'quests' not in st.session_state:
    st.session_state.quests = []

if 'completed_quests' not in st.session_state:
    st.session_state.completed_quests = []

if 'interactions' not in st.session_state:
    st.session_state.interactions = []

# Ajouter les initialisations pour les sélections d'interactions entre PNJ
if 'interaction_pnj1' not in st.session_state:
    st.session_state.interaction_pnj1 = df['PNJ'].unique()[0]

if 'interaction_pnj2' not in st.session_state:
    st.session_state.interaction_pnj2 = df['PNJ'].unique()[1]

if 'interaction_context' not in st.session_state:
    st.session_state.interaction_context = "demande de ressources"

# Interface Streamlit
st.title("Réseau de PNJ Interactifs à Valoria")

# Afficher les options de PNJ avec la gestion de l'état
st.session_state.selected_pnj = st.selectbox(
    "Sélectionnez un PNJ:", df['PNJ'].unique(), index=list(df['PNJ'].unique()).index(st.session_state.selected_pnj)
)

# Afficher les interactions du PNJ sélectionné
if st.button("Voir les interactions"):
    neighbors = list(G.neighbors(st.session_state.selected_pnj))
    st.write(f"{st.session_state.selected_pnj} est connecté avec : {neighbors}")

    # Visualiser le graphe centré sur le PNJ sélectionné
    subgraph = G.subgraph([st.session_state.selected_pnj] + neighbors)
    pos = nx.spring_layout(subgraph)
    plt.figure(figsize=(8, 6))
    nx.draw(subgraph, pos, with_labels=True, node_color='lightblue', edge_color='grey', node_size=2000, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=nx.get_edge_attributes(subgraph, 'context'))
    st.pyplot(plt)

# Fonction pour propager des rumeurs dans le réseau
def propagate_rumor(graph, start_node, rumor):
    nx.set_node_attributes(graph, {start_node: rumor}, 'rumor')
    for neighbor in graph.neighbors(start_node):
        graph.nodes[neighbor]['rumor'] = rumor
        st.write(f"Rumeur propagée de {start_node} à {neighbor} : {rumor}")

# Propagation de rumeurs à partir du PNJ sélectionné
st.session_state.rumor = st.text_input("Entrer la rumeur à propager:", st.session_state.rumor)

if st.button("Propager la rumeur"):
    propagate_rumor(G, st.session_state.selected_pnj, st.session_state.rumor)

    # Afficher les nœuds avec leurs rumeurs propagées
    st.write("Nœuds avec les rumeurs propagées :")
    for node, data in G.nodes(data=True):
        if 'rumor' in data:
            st.write(f"{node} a reçu la rumeur : {data['rumor']}")

# Simulation de scénarios en temps réel
st.header("Simulation de Scénarios")
scenarios = ["Attaque", "Récolte de ressources", "Festival"]
st.session_state.selected_scenario = st.selectbox(
    "Choisissez un scénario à simuler:", scenarios, index=scenarios.index(st.session_state.selected_scenario)
)

if st.button("Simuler le scénario"):
    if st.session_state.selected_scenario == "Attaque":
        st.write("Simulation d'une attaque imminente...")
        start_node = "Garde"
        rumor = "Une attaque imminente a été signalée."
        propagate_rumor(G, start_node, rumor)
        st.write("Les PNJ se préparent pour l'attaque.")
    elif st.session_state.selected_scenario == "Récolte de ressources":
        st.write("Simulation de la récolte des ressources...")
        start_node = "Fermière"
        rumor = "La récolte du blé commence aujourd'hui."
        propagate_rumor(G, start_node, rumor)
        st.write("Les PNJ se mobilisent pour la récolte.")
    elif st.session_state.selected_scenario == "Festival":
        st.write("Simulation du festival du village...")
        start_node = "Seigneur"
        rumor = "Le festival annuel du village commence ce soir."
        propagate_rumor(G, start_node, rumor)
        st.write("Les PNJ se préparent pour le festival.")

# Générer des réponses contextuelles pour les PNJ
def get_contextual_response(pnj, context):
    prompt = f"Le joueur demande à {pnj} comment il peut aider pendant {context}. {pnj} répond directement au joueur :"
    response = generate_dialogue(prompt)
    return response

# Sélectionner le PNJ et le contexte pour la demande d'aide
st.session_state.selected_pnj_for_help = st.selectbox(
    "Choisissez un PNJ pour demander de l'aide:", df['PNJ'].unique(), index=list(df['PNJ'].unique()).index(st.session_state.selected_pnj_for_help)
)
st.session_state.selected_context_for_help = st.selectbox(
    "Choisissez le contexte de la demande:", ["attaque", "récolte", "festival"], index=["attaque", "récolte", "festival"].index(st.session_state.selected_context_for_help)
)

# Fonction pour déterminer les PNJ impliqués dans une quête
def get_pnjs_involved_in_quest(start_pnj, context):
    involved_pnjs = [start_pnj]
    if context == "attaque":
        involved_pnjs += ["Garde", "Forgeron", "Chasseur"]
    elif context == "récolte":
        involved_pnjs += ["Fermière", "Marchand"]
    elif context == "festival":
        involved_pnjs += ["Seigneur", "Villageois"]
    return involved_pnjs

# Utilisation de la fonction dans l'interface Streamlit
if st.button("Demander de l'aide"):
    response = get_contextual_response(st.session_state.selected_pnj_for_help, st.session_state.selected_context_for_help)
    st.write(f"Réponse de {st.session_state.selected_pnj_for_help} : {response}")

    involved_pnjs = get_pnjs_involved_in_quest(st.session_state.selected_pnj_for_help, st.session_state.selected_context_for_help)
    quest_description = f"Aidez {st.session_state.selected_pnj_for_help} à {st.session_state.selected_context_for_help}."
    quest = {
        "Initiateur": st.session_state.selected_pnj_for_help,
        "Description": quest_description,
        "Status": "Active",
        "Involved_PNJs": involved_pnjs
    }
    st.session_state.quests.append(quest)
    st.write(f"Quête initiée par {st.session_state.selected_pnj_for_help} avec les PNJ impliqués {involved_pnjs} : {quest_description}")

# Fonction pour initier des interactions entre les PNJ avec une structure de transaction
def initiate_pnj_interaction(pnj1, pnj2, context):
    if context == "demande de ressources":
        dialogue_steps = [
            f"{pnj1} envoie une requête à {pnj2} pour fournir les ressources nécessaires.",
            f"{pnj2} confirme la disponibilité des ressources et envoie une réponse avec la quantité et le prix.",
            f"{pnj1} envoie les crédits à {pnj2}.",
            f"{pnj2} envoie les ressources à {pnj1}.",
            "La transaction est complétée avec succès."
        ]
    else:
        dialogue_steps = [f"{pnj1} informe {pnj2} de {context}. {pnj2} réagit en conséquence."]

    # Générer et afficher les dialogues pour chaque étape
    full_interaction = ""
    for step in dialogue_steps:
        prompt = f"{step} {pnj2} répond :"
        response = generate_dialogue(prompt)
        cleaned_response = clean_response(response)
        if not cleaned_response:
            cleaned_response = "Le dialogue n'a pas pu être généré. Réessayez ou définissez un message par défaut."
        full_interaction += f"{step} {cleaned_response}\n"

    return full_interaction

def clean_response(response):
    response = response.strip().replace('"', '')
    if response.lower() in ["", "réponse :"]:
        return None
    return response

# Ajouter des interactions directes entre les PNJ
st.header("Interactions Directes entre PNJ")
st.session_state.interaction_pnj1 = st.selectbox(
    "Sélectionnez le premier PNJ pour l'interaction :", df['PNJ'].unique(), key='pnj1', index=list(df['PNJ'].unique()).index(st.session_state.interaction_pnj1)
)
st.session_state.interaction_pnj2 = st.selectbox(
    "Sélectionnez le deuxième PNJ pour l'interaction :", df['PNJ'].unique(), key='pnj2', index=list(df['PNJ'].unique()).index(st.session_state.interaction_pnj2)
)
st.session_state.interaction_context = st.selectbox(
    "Choisissez le contexte de l'interaction :", ["présence suspecte", "demande de ressources", "planification de la récolte"], index=["présence suspecte", "demande de ressources", "planification de la récolte"].index(st.session_state.interaction_context)
)

if st.button("Initier une interaction entre PNJ"):
    interaction_response = initiate_pnj_interaction(st.session_state.interaction_pnj1, st.session_state.interaction_pnj2, st.session_state.interaction_context)
    st.write(f"Interaction entre {st.session_state.interaction_pnj1} et {st.session_state.interaction_pnj2} sur le thème '{st.session_state.interaction_context}':")
    st.write(interaction_response)

    # Ajouter l'interaction à l'historique des interactions
    st.session_state.interactions.append((st.session_state.interaction_pnj1, st.session_state.interaction_pnj2, st.session_state.interaction_context, interaction_response))

# Afficher l'historique des interactions entre PNJ
st.subheader("Historique des Interactions entre PNJ")
for interaction in st.session_state.interactions:
    st.write(f"{interaction[0]} a informé {interaction[1]} sur le thème '{interaction[2]}'. Réponse : {interaction[3]}")

# Afficher le journal des quêtes
st.subheader("Journal des Quêtes")
for quest in st.session_state.quests:
    st.write(f"Quête de {quest['Initiateur']} : {quest['Description']} - Statut : {quest['Status']}")
    st.write(f"PNJ impliqués : {', '.join(quest['Involved_PNJs'])}")
    if st.button(f"Marquer comme terminée", key=f"complete_{quest['Initiateur']}"):
        quest['Status'] = "Terminée"
        st.session_state.completed_quests.append(quest)
        st.session_state.quests.remove(quest)
        st.success(f"Quête terminée : {quest['Description']}")

# Visualiser l'impact des quêtes sur le réseau de PNJ
if st.session_state.quests or st.session_state.completed_quests:
    st.header("Impact des Quêtes sur le Réseau de PNJ")
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='grey', node_size=2000, font_size=10, font_weight='bold')

    # Colorer les nœuds avec des quêtes actives
    active_nodes = [n for n in G.nodes if n in [pnj for quest in st.session_state.quests for pnj in quest['Involved_PNJs']]]
    nx.draw_networkx_nodes(G, pos, nodelist=active_nodes, node_color='yellow')

    # Colorer les nœuds avec des quêtes terminées
    completed_nodes = [n for n in G.nodes if n in [pnj for quest in st.session_state.completed_quests for pnj in quest['Involved_PNJs']]]
    nx.draw_networkx_nodes(G, pos, nodelist=completed_nodes, node_color='green')

    plt.title("Impact des Quêtes sur le Réseau de PNJ")
    st.pyplot(plt)
