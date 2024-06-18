import unittest
from src.integrate_dialogues import integrate_dialogues, clean_response

class TestIntegrateDialogues(unittest.TestCase):

    def test_integrate_dialogues(self):
        # Test the integration of dialogues
        dialogues = integrate_dialogues()
        self.assertIsInstance(dialogues, list)
        self.assertGreater(len(dialogues), 0)
        for dialogue in dialogues:
            self.assertIsInstance(dialogue, dict)
            self.assertIn("NPC", dialogue)
            self.assertIn("Response", dialogue)
            self.assertIsInstance(dialogue["NPC"], str)
            self.assertIsInstance(dialogue["Response"], str)

    def test_clean_response(self):
        # Test the cleaning of generated responses
        raw_response = '\"Hello! How can I help you?\"'
        cleaned_response = clean_response(raw_response)
        self.assertEqual(cleaned_response, 'Hello! How can I help you?')

if __name__ == '__main__':
    unittest.main()
