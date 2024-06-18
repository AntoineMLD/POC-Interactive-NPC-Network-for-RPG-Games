from src.configure_and_use_openai_api import generate_dialogue

# Fonction pour nettoyer les réponses générées
def clean_response(response):
    response = response.replace('\"', '').strip()
    response = response.replace('«', '').replace('»', '')
    response = response.split('<<')[0]
    response = response.split('1.')[0]
    response = response.split('\n')[0]  # Garder uniquement la première ligne si plusieurs lignes
    return response.strip()

def integrate_dialogues():
    prompts = {
        "Guérisseur": "Le joueur demande au Guérisseur comment il peut aider à sauver le village. Le Guérisseur répond avec des actions spécifiques comme chercher des herbes ou des provisions :",
        "Marchand": "Le joueur demande au Marchand ce qu'il peut faire pour aider le village en termes de commerce. Le Marchand explique les objets qu'il recherche comme des cristaux, des plumes rares, ou des épées :",
        "Forgeron": "Le joueur demande au Forgeron des conseils sur comment fortifier le village. Le Forgeron répond avec des instructions précises sur la construction de barrières et la fabrication d'armes :",
        "Chasseur": "Le joueur demande au Chasseur s'il a vu des signes de danger dans la forêt. Le Chasseur décrit ce qu'il a observé, comme des animaux inhabituels ou des traces suspectes :",
        "Garde": "Le joueur demande au Garde comment il peut contribuer à la sécurité du village. Le Garde donne des tâches spécifiques comme patrouiller, surveiller les frontières, ou aider les villageois :",
        "Seigneur": "Le joueur demande au Seigneur ce qui est nécessaire pour assurer la paix dans le village. Le Seigneur donne des exemples concrets de priorités comme la sécurité, la nourriture, et les infrastructures :",
        "Fermière": "Le joueur demande à la Fermière comment il peut aider avec la récolte et la préparation des champs. La Fermière détaille les tâches à accomplir comme semer, arroser, et récolter :"
    }

    dialogues = []
    for pnj, prompt in prompts.items():
        response = clean_response(generate_dialogue(prompt))
        dialogues.append({"PNJ": pnj, "Réponse": response})

    return dialogues

# Si vous souhaitez exécuter ce script directement pour voir les résultats
if __name__ == "__main__":
    dialogues = integrate_dialogues()
    for dialogue in dialogues:
        print(f"{dialogue['PNJ']} : {dialogue['Réponse']}")
