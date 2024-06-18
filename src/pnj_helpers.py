# src/pnj_helpers.py

import networkx as nx
from src.configure_and_use_openai_api import generate_dialogue

def get_contextual_response(pnj, context):
    prompt = f"Le joueur demande à {pnj} comment il peut aider pendant {context}. {pnj} répond directement au joueur :"
    response = generate_dialogue(prompt)
    return response

def get_pnjs_involved_in_quest(start_pnj, context):
    involved_pnjs = [start_pnj]
    if context == "attaque":
        involved_pnjs += ["Garde", "Forgeron", "Chasseur"]
    elif context == "récolte":
        involved_pnjs += ["Fermière", "Marchand"]
    elif context == "festival":
        involved_pnjs += ["Seigneur", "Villageois"]
    return involved_pnjs

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
