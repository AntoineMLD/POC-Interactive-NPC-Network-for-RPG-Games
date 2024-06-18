import unittest
import networkx as nx
import os
from src.model_relationships import model_relationships

class TestModelRelationships(unittest.TestCase):
    def setUp(self):
        # Chemin relatif vers le fichier CSV de test
        self.csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")

    def test_model_relationships(self):
        # Teste la modélisation des relations
        relationships = model_relationships(self.csv_path)
        self.assertIsInstance(relationships, nx.Graph)
        self.assertGreater(len(relationships.nodes), 0)  # Vérifie que le graphe a des nœuds
        self.assertGreater(len(relationships.edges), 0)  # Vérifie que le graphe a des arêtes

if __name__ == '__main__':
    unittest.main()
