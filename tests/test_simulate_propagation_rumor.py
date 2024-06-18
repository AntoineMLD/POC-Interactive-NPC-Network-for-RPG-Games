import unittest
import networkx as nx
from src.simulate_propagation_rumor import load_graph_from_csv, propagate_rumor

class TestSimulatePropagationRumor(unittest.TestCase):

    def setUp(self):
        # Configuration d'un graphe de test
        self.G = nx.Graph()
        self.G.add_nodes_from(["PNJ1", "PNJ2", "PNJ3"])
        self.G.add_edges_from([("PNJ1", "PNJ2"), ("PNJ2", "PNJ3")])
        self.rumor = "Une attaque imminente a été signalée."

    def test_propagate_rumor(self):
        # Teste la propagation des rumeurs
        result = propagate_rumor(self.G, "PNJ1", self.rumor)
        self.assertIn("PNJ2", result)
        self.assertIn("PNJ3", result)
        self.assertEqual(self.G.nodes["PNJ2"].get('rumor'), self.rumor)
        self.assertEqual(self.G.nodes["PNJ3"].get('rumor'), self.rumor)

    def test_load_graph_from_csv(self):
        # Teste le chargement du graphe à partir du CSV
        csv_path = "tests/dialogues_valoria_enriched.csv"  
        G, df = load_graph_from_csv(csv_path)
        self.assertGreater(len(G.nodes), 0)
        self.assertGreater(len(G.edges), 0)

if __name__ == '__main__':
    unittest.main()
