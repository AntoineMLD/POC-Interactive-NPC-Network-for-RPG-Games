import pandas as pd
import os

# Fonction pour charger les données
def load_data(csv_path):
    # Charger le fichier CSV
    df = pd.read_csv(csv_path)
    return df

# Fonction pour préparer les données
def prepare_data(df):
    # Par exemple, nous pourrions faire quelques préparations de base comme enlever les colonnes inutiles
    # ou manipuler les données selon les besoins
    # Pour l'instant, renvoyons simplement le DataFrame original
    return df

# Appel des fonctions pour exécuter le script de préparation de données
if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
    df = load_data(csv_path)
    print("Aperçu des données chargées :")
    print(df.head())

    print("\nDistribution des rôles :")
    print(df['Rôle'].value_counts())

    print("\nDistribution des émotions :")
    print(df['Émotion'].value_counts())

    print("\nDistribution des intentions :")
    print(df['Intention'].value_counts())
