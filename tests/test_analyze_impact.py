import unittest
import os
from src.analyze_impact import analyze_impact

class TestAnalyzeImpact(unittest.TestCase):

    def setUp(self):
        # Relative path to the test CSV file
        self.csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
        self.rumor = "An imminent attack has been reported."
        self.start_node = "Guard"

    def test_analyze_impact(self):
        # Call the analyze_impact function
        impacted_nodes = analyze_impact(self.csv_path, self.start_node, self.rumor)
        # Check that the impacted nodes are correct (you can adjust based on expected results)
        self.assertIn("Guard", impacted_nodes)
        self.assertIn("Merchant", impacted_nodes)
        self.assertIn("Hunter", impacted_nodes)
        
if __name__ == "__main__":
    unittest.main()
