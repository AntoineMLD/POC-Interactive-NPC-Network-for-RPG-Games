import unittest
import os
from src.simulate_interactions import load_graph_from_csv, simulate_interaction, propagate_rumor

class TestSimulateInteractions(unittest.TestCase):
    def setUp(self):
        # Chemin relatif vers le fichier CSV de test
        self.csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
        self.G, self.df = load_graph_from_csv(self.csv_path)

    def test_simulate_interaction(self):
        # Teste la simulation d'une interaction
        response = simulate_interaction("Guérisseur", "Merci pour votre aide avec ces herbes rares.", self.df)
        self.assertIn("Guérisseur (Soigneur): Merci pour votre aide avec ces herbes rares.", response)

    def test_propagate_rumor(self):
        # Teste la propagation d'une rumeur
        propagations = propagate_rumor(self.G, "Guérisseur", "Le joueur a aidé le Guérisseur avec des herbes rares.")
        self.assertGreater(len(propagations), 0)
        for propagation in propagations:
            self.assertIn("Guérisseur", propagation)
            self.assertIn("Le joueur a aidé le Guérisseur avec des herbes rares.", propagation)

if __name__ == '__main__':
    unittest.main()
