from configure_and_use_openai_api import generate_dialogue

# Fonction pour nettoyer les réponses générées
def clean_response(response):
    # Enlever les guillemets doubles et les espaces superflus
    response = response.replace('\"', '').strip()
    # Enlever les éléments entre guillemets français, etc.
    response = response.replace('«', '').replace('»', '')
    # Enlever les parties indésirables ou marqueurs de fin
    response = response.split('<<')[0]
    response = response.split('1.')[0]
    response = response.split('\n')[0]  # Garder uniquement la première ligne si plusieurs lignes
    return response.strip()

# Prompts enrichis avec plus de détails pour couvrir différents aspects des interactions
prompts = {
    "Guérisseur": "Le joueur demande au Guérisseur comment il peut aider à sauver le village. Le Guérisseur répond avec des actions spécifiques comme chercher des herbes ou des provisions :",
    "Marchand": "Le joueur demande au Marchand ce qu'il peut faire pour aider le village en termes de commerce. Le Marchand explique les objets qu'il recherche comme des cristaux, des plumes rares, ou des épées :",
    "Forgeron": "Le joueur demande au Forgeron des conseils sur comment fortifier le village. Le Forgeron répond avec des instructions précises sur la construction de barrières et la fabrication d'armes :",
    "Chasseur": "Le joueur demande au Chasseur s'il a vu des signes de danger dans la forêt. Le Chasseur décrit ce qu'il a observé, comme des animaux inhabituels ou des traces suspectes :",
    "Garde": "Le joueur demande au Garde comment il peut contribuer à la sécurité du village. Le Garde donne des tâches spécifiques comme patrouiller, surveiller les frontières, ou aider les villageois :",
    "Seigneur": "Le joueur demande au Seigneur ce qui est nécessaire pour assurer la paix dans le village. Le Seigneur donne des exemples concrets de priorités comme la sécurité, la nourriture, et les infrastructures :",
    "Fermière": "Le joueur demande à la Fermière comment il peut aider avec la récolte et la préparation des champs. La Fermière détaille les tâches à accomplir comme semer, arroser, et récolter :"
}

# Générer et nettoyer les réponses pour chaque PNJ
for pnj, prompt in prompts.items():
    response = clean_response(generate_dialogue(prompt))
    print(f"{pnj} : {response}")

# Scénarios spécifiques pour tester les réponses incomplètes

# Prompt détaillé pour le Guérisseur
guérisseur_prompt = "Le joueur demande au Guérisseur comment il peut aider à guérir les villageois malades. Le Guérisseur explique exactement ce que le joueur doit faire, comme collecter des herbes spécifiques ou préparer des remèdes :"
guérisseur_response = clean_response(generate_dialogue(guérisseur_prompt))
print(f"Guérisseur (détail) : {guérisseur_response}")

# Prompt détaillé pour le Seigneur
seigneur_prompt = "Le joueur demande au Seigneur ce qu'il faut pour assurer la paix et la prospérité dans le village. Le Seigneur décrit ses priorités en matière de sécurité, de bonheur et de bien-être pour les villageois :"
seigneur_response = clean_response(generate_dialogue(seigneur_prompt))
print(f"Seigneur (détail) : {seigneur_response}")

# Exemple de nouveaux prompts contextuels
additional_prompts = {
    "Guérisseur": "Le joueur informe le Guérisseur qu'il a déjà collecté des herbes rares. Le Guérisseur explique comment les utiliser pour préparer un remède :",
    "Marchand": "Le joueur demande au Marchand ce qu'il peut faire pour améliorer le commerce du village après avoir découvert une mine de cristaux :",
    "Forgeron": "Le joueur informe le Forgeron qu'il a trouvé des matériaux rares. Le Forgeron explique comment les utiliser pour renforcer les défenses du village :",
    "Chasseur": "Le joueur dit au Chasseur qu'il a trouvé des traces étranges dans la forêt. Le Chasseur analyse les traces et donne des conseils sur la prochaine étape :",
    "Garde": "Le joueur informe le Garde qu'il a repoussé une attaque de bandits. Le Garde donne des instructions sur la sécurisation du périmètre :",
    "Seigneur": "Le joueur informe le Seigneur qu'il a réussi à améliorer la sécurité du village. Le Seigneur exprime ses nouvelles priorités pour le bien-être des villageois :",
    "Fermière": "Le joueur informe la Fermière qu'il a réussi à récolter une grande quantité de blé. La Fermière explique comment stocker et utiliser le blé de manière optimale :"
}

# Générer et nettoyer les réponses pour chaque PNJ avec des contextes différents
for pnj, prompt in additional_prompts.items():
    response = clean_response(generate_dialogue(prompt))
    print(f"{pnj} (contexte) : {response}")
