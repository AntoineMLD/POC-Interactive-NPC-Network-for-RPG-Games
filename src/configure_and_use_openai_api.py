import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Configurer l'API OpenAI pour utiliser Azure
openai.api_type = "azure"
openai.api_key = os.getenv("openai_api_key")
openai.api_base = os.getenv("openai_api_base")
openai.api_version = os.getenv("openai_api_version")

# Vérification des valeurs chargées
if None in [openai.api_key, openai.api_base, openai.api_version]:
    raise ValueError("Une ou plusieurs variables d'environnement sont manquantes ou incorrectes. Vérifiez votre fichier .env.")

# Fonction pour générer un dialogue avec GPT-3.5 Turbo
def generate_dialogue(prompt):
    response = openai.Completion.create(
        engine=os.getenv("openai_api_deployment"),
        prompt=prompt,
        max_tokens=200,      # Augmenter le nombre de tokens pour permettre des réponses plus longues si nécessaire
        temperature=0.7,     # Contrôle la créativité de la réponse
        n=1,                 # Nombre de réponses à générer
        stop=["\n", "Joueur", "Le"]  # Arrêter après ces tokens pour éviter des réponses trop longues ou incomplètes
    )
    return response.choices[0].text.strip()

# Exemple d'utilisation
prompt = "Le joueur demande au Guérisseur : Comment puis-je aider le village ?"
response = generate_dialogue(prompt)
print(f"Réponse du modèle : {response}")
