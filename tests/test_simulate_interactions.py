import unittest
import os
from src.simulate_interactions import load_graph_from_csv, simulate_interaction, propagate_rumor

class TestSimulateInteractions(unittest.TestCase):
    def setUp(self):
        # Relative path to the test CSV file
        self.csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
        self.G, self.df = load_graph_from_csv(self.csv_path)

    def test_simulate_interaction(self):
        # Test the simulation of an interaction
        response = simulate_interaction("Healer", "Thank you for your help with these rare herbs.", self.df)
        self.assertIn("Healer (Healer): Thank you for your help with these rare herbs.", response)

    def test_propagate_rumor(self):
        # Test the propagation of a rumor
        propagations = propagate_rumor(self.G, "Healer", "The player helped the Healer with rare herbs.")
        self.assertGreater(len(propagations), 0)
        for propagation in propagations:
            self.assertIn("Healer", propagation)
            self.assertIn("The player helped the Healer with rare herbs.", propagation)

if __name__ == '__main__':
    unittest.main()
