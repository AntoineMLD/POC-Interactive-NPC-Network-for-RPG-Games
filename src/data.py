import pandas as pd
import os

# Créer le DataFrame enrichi
data = {
    "PNJ": ["Guérisseur", "Marchand", "Forgeron", "Chasseur", "Garde", "Seigneur", "Fermière",
            "Guérisseur", "Marchand", "Forgeron", "Chasseur", "Garde", "Seigneur", "Fermière",
            "Guérisseur", "Marchand", "Forgeron", "Chasseur", "Garde", "Seigneur", "Fermière"],
    "Rôle": ["Soigneur", "Commerçant", "Artisan", "Chasseur", "Protecteur", "Dirigeant", "Travailleur",
             "Soigneur", "Commerçant", "Artisan", "Chasseur", "Protecteur", "Dirigeant", "Travailleur",
             "Soigneur", "Commerçant", "Artisan", "Chasseur", "Protecteur", "Dirigeant", "Travailleur"],
    "Contexte": ["Santé", "Commerce", "Défense", "Exploration", "Sécurité", "Gestion", "Champs",
                 "Attaque", "Attaque", "Approvisionnement", "Quête", "Sécurité", "Cérémonie", "Récolte",
                 "Approvisionnement", "Négociation", "Construction", "Surveillance", "Renfort", "Planification", "Préparation"],
    "Émotion": ["Reconnaissant", "Soulagé", "Précautionneux", "Curieux", "Déterminé", "Autoritaire", "Reconnaissante",
                "Inquiet", "Anxieux", "Industriel", "Excité", "Protecteur", "Solennel", "Content",
                "Concentré", "Satisfait", "Engagé", "Attentif", "Optimiste", "Stratégique", "Impliquée"],
    "Intention": ["Aider", "Diffuser", "Protéger", "Observer", "Surveiller", "Organiser", "Travailler",
                  "Aider", "Informer", "Produire", "Explorer", "Défendre", "Diriger", "Collecter",
                  "Collecter", "Négocier", "Fabriquer", "Patrouiller", "Renforcer", "Planifier", "Organiser"],
    "Dialogue": ["Je suis heureux de vous voir ici.", "Le Marchand annonce que le Guérisseur cherche des herbes rares.", "Nous devons fortifier le village avec des barrières solides.", "J'ai vu des traces de loups près de la forêt.", "Nous devons renforcer les patrouilles autour du village.", "Il est crucial de planifier notre défense contre les menaces extérieures.", "Merci de m'aider à récolter les pommes de terre.",
                 "Je crains que l'attaque ne cause des blessures graves.", "Le Marchand a entendu des rumeurs sur une attaque imminente.", "Nous avons besoin de plus de matériaux pour les armes.", "Je suis à la recherche d'une créature rare dans les montagnes.", "Je ne laisserai personne passer sans être contrôlé.", "Nous devons célébrer nos victoires pour renforcer le moral.", "La récolte cette année a été abondante grâce à votre aide.",
                 "Je dois récupérer plus d'herbes médicinales dans la forêt.", "J'ai trouvé un acheteur pour nos produits de haute qualité.", "Je vais fabriquer de nouvelles armes pour renforcer nos défenses.", "Je surveille les environs pour détecter toute activité suspecte.", "Avec de nouveaux renforts, nous pouvons protéger efficacement le village.", "Nous devons élaborer un plan détaillé pour l'expansion de notre village.", "Je dois organiser les provisions pour l'hiver."],
    "Rumeur/Action": ["Guérir", "Guérisseur", "Sécurité", "Avertissement", "Préparation", "Coordination", "Aide",
                      "Guérir", "Garde", "Sécurité", "Curiosité", "Sécurité", "Organisation", "Aide",
                      "Recherche", "Transaction", "Défense", "Sécurité", "Défense", "Développement", "Approvisionnement"],
    "Contexte_détaillé": ["Récupération", "Alerte", "Préparation", "Observation", "Sécurité", "Organisation", "Récolte",
                          "Préparation", "Précaution", "Ressources", "Aventure", "Contrôle", "Fête", "Stockage",
                          "Collecte", "Vente", "Production", "Observation", "Sécurisation", "Stratégie", "Organisation"],
    "Émotions_détaillées": ["Joie", "Soulagement", "Prudence", "Inquiétude", "Vigilance", "Responsabilité", "Gratitude",
                            "Panique", "Alerte", "Urgence", "Excitation", "Fermeté", "Pride", "Satisfaction",
                            "Focus", "Satisfaction", "Détermination", "Attention", "Optimisme", "Détermination", "Responsabilité"]
}

# Créer le DataFrame
df_enriched = pd.DataFrame(data)

# Définir le chemin du répertoire src
src_dir = os.path.join(os.path.dirname(__file__), "src")

# S'assurer que le répertoire src existe
os.makedirs(src_dir, exist_ok=True)

# Définir le chemin complet du fichier CSV dans le répertoire src
csv_file_path = os.path.join(src_dir, "dialogues_valoria_enriched.csv")

# Enregistrer le DataFrame en tant que fichier CSV dans le répertoire src
df_enriched.to_csv(csv_file_path, index=False)

print(f"Fichier CSV enrichi enregistré sous {csv_file_path}")
        