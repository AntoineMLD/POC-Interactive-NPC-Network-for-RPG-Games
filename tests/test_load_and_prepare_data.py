import unittest
from src.load_and_prepare_data import load_data, prepare_data
import os

class TestLoadAndPrepareData(unittest.TestCase):
    def setUp(self):
        # Chemin relatif vers le fichier CSV de test
        self.csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")

    def test_load_data(self):
        # Teste le chargement des données
        data = load_data(self.csv_path)
        self.assertFalse(data.empty)  # Vérifie que le DataFrame n'est pas vide

    def test_prepare_data(self):
        # Teste la préparation des données
        data = load_data(self.csv_path)
        prepared_data = prepare_data(data)
        self.assertIn("PNJ", prepared_data.columns)  # Vérifie que la colonne 'PNJ' est présente dans le DataFrame préparé

if __name__ == '__main__':
    unittest.main()
