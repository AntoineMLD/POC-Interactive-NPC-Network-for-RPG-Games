import unittest
import networkx as nx
from src.simulate_propagation_rumor import load_graph_from_csv, propagate_rumor

class TestSimulatePropagationRumor(unittest.TestCase):

    def setUp(self):
        # Setting up a test graph
        self.G = nx.Graph()
        self.G.add_nodes_from(["NPC1", "NPC2", "NPC3"])
        self.G.add_edges_from([("NPC1", "NPC2"), ("NPC2", "NPC3")])
        self.rumor = "An imminent attack has been reported."

    def test_propagate_rumor(self):
        # Testing rumor propagation
        result = propagate_rumor(self.G, "NPC1", self.rumor)
        self.assertIn("NPC2", result)
        self.assertIn("NPC3", result)
        self.assertEqual(self.G.nodes["NPC2"].get('rumor'), self.rumor)
        self.assertEqual(self.G.nodes["NPC3"].get('rumor'), self.rumor)

    def test_load_graph_from_csv(self):
        # Testing graph loading from CSV
        csv_path = "tests/dialogues_valoria_enriched.csv"  
        G, df = load_graph_from_csv(csv_path)
        self.assertGreater(len(G.nodes), 0)
        self.assertGreater(len(G.edges), 0)

if __name__ == '__main__':
    unittest.main()
