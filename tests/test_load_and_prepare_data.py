import unittest
from src.load_and_prepare_data import load_data, prepare_data
import os

class TestLoadAndPrepareData(unittest.TestCase):
    def setUp(self):
        # Relative path to the test CSV file
        self.csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")

    def test_load_data(self):
        # Tests data loading
        data = load_data(self.csv_path)
        self.assertFalse(data.empty)  # Checks that the DataFrame is not empty

    def test_prepare_data(self):
        # Tests data preparation
        data = load_data(self.csv_path)
        prepared_data = prepare_data(data)
        self.assertIn("NPC", prepared_data.columns)  # Checks that the 'NPC' column is present in the prepared DataFrame

if __name__ == '__main__':
    unittest.main()
