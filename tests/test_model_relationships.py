import unittest
import networkx as nx
import os
from src.model_relationships import model_relationships

class TestModelRelationships(unittest.TestCase):
    def setUp(self):
        # Relative path to the test CSV file
        self.csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")

    def test_model_relationships(self):
        # Test the modeling of relationships
        relationships = model_relationships(self.csv_path)
        self.assertIsInstance(relationships, nx.Graph)
        self.assertGreater(len(relationships.nodes), 0)  # Checks that the graph has nodes
        self.assertGreater(len(relationships.edges), 0)  # Checks that the graph has edges

if __name__ == '__main__':
    unittest.main()
