import unittest
import os
from src.analyze_impact import analyze_impact

class TestAnalyzeImpact(unittest.TestCase):

    def setUp(self):
        # Chemin relatif vers le fichier CSV de test
        self.csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
        self.rumor = "Une attaque imminente a été signalée."
        self.start_node = "Garde"

    def test_analyze_impact(self):
        # Appel de la fonction analyze_impact
        impacted_nodes = analyze_impact(self.csv_path, self.start_node, self.rumor)
        # Vérifier que les nœuds impactés sont corrects (ici vous pouvez ajuster en fonction des résultats attendus)
        self.assertIn("Garde", impacted_nodes)
        self.assertIn("Marchand", impacted_nodes)
        self.assertIn("Chasseur", impacted_nodes)
        
if __name__ == "__main__":
    unittest.main()
