import networkx as nx
from src.configure_and_use_openai_api import generate_dialogue

def get_contextual_response(npc, context):
    prompt = f"The player asks {npc} how they can help during {context}. {npc} responds directly to the player:"
    response = generate_dialogue(prompt)
    return response

def get_npcs_involved_in_quest(start_npc, context):
    involved_npcs = [start_npc]
    if context == "attack":
        involved_npcs += ["Guard", "Blacksmith", "Hunter"]
    elif context == "harvest":
        involved_npcs += ["Farmer", "Merchant"]
    elif context == "festival":
        involved_npcs += ["Lord", "Villager"]
    return involved_npcs

def initiate_npc_interaction(npc1, npc2, context):
    if context == "resource request":
        dialogue_steps = [
            f"{npc1} sends a request to {npc2} to provide the necessary resources.",
            f"{npc2} confirms the availability of the resources and sends a response with the quantity and price.",
            f"{npc1} sends the credits to {npc2}.",
            f"{npc2} sends the resources to {npc1}.",
            "The transaction is successfully completed."
        ]
    else:
        dialogue_steps = [f"{npc1} informs {npc2} about {context}. {npc2} reacts accordingly."]

    full_interaction = ""
    for step in dialogue_steps:
        prompt = f"{step} {npc2} responds:"
        response = generate_dialogue(prompt)
        cleaned_response = clean_response(response)
        if not cleaned_response:
            cleaned_response = "The dialogue could not be generated. Try again or set a default message."
        full_interaction += f"{step} {cleaned_response}\n"

    return full_interaction

def clean_response(response):
    response = response.strip().replace('"', '')
    if response.lower() in ["", "response:"]:
        return None
    return response
