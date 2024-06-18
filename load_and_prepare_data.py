import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("dialogues_valoria.csv")

# Afficher les premières lignes du DataFrame pour vérifier le chargement
print("Aperçu des données chargées :")
print(df.head())

# Analyser les distributions des rôles, des émotions et des intentions
print("\nDistribution des rôles :")
print(df['Rôle'].value_counts())

print("\nDistribution des émotions :")
print(df['Émotion'].value_counts())

print("\nDistribution des intentions :")
print(df['Intention'].value_counts())
