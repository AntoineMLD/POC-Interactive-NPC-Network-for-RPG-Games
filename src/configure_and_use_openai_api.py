import openai
import os
from dotenv import load_dotenv

# Construire le chemin vers le fichier .env dans le répertoire racine
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

def configure_openai_api():
    """Configure les paramètres de l'API OpenAI en utilisant les variables d'environnement."""
    openai.api_type = "azure"
    openai.api_key = os.getenv("openai_api_key")
    openai.api_base = os.getenv("openai_api_base")
    openai.api_version = os.getenv("openai_api_version")

    # Vérification des valeurs chargées
    if None in [openai.api_key, openai.api_base, openai.api_version]:
        raise ValueError("Une ou plusieurs variables d'environnement sont manquantes ou incorrectes. Vérifiez votre fichier .env.")

# Appel de la fonction pour configurer l'API au chargement du module
configure_openai_api()

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
if __name__ == "__main__":
    prompt = "Le joueur demande au Guérisseur : Comment puis-je aider le village ?"
    response = generate_dialogue(prompt)
    print(f"Réponse du modèle : {response}")
