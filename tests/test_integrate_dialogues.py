import unittest
from src.integrate_dialogues import integrate_dialogues, clean_response

class TestIntegrateDialogues(unittest.TestCase):

    def test_integrate_dialogues(self):
        # Teste l'intégration des dialogues
        dialogues = integrate_dialogues()
        self.assertIsInstance(dialogues, list)
        self.assertGreater(len(dialogues), 0)
        for dialogue in dialogues:
            self.assertIsInstance(dialogue, dict)
            self.assertIn("PNJ", dialogue)
            self.assertIn("Réponse", dialogue)
            self.assertIsInstance(dialogue["PNJ"], str)
            self.assertIsInstance(dialogue["Réponse"], str)

    def test_clean_response(self):
        # Teste le nettoyage des réponses générées
        raw_response = '\"Hello! How can I help you?\"'
        cleaned_response = clean_response(raw_response)
        self.assertEqual(cleaned_response, 'Hello! How can I help you?')

if __name__ == '__main__':
    unittest.main()
