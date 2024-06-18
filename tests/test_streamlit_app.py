import unittest
from src.pnj_helpers import get_contextual_response, get_pnjs_involved_in_quest, initiate_pnj_interaction

class TestStreamlitApp(unittest.TestCase):

    def test_get_contextual_response(self):
        response = get_contextual_response("Guérisseur", "festival")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def test_get_pnjs_involved_in_quest(self):
        involved_pnjs = get_pnjs_involved_in_quest("Guérisseur", "attaque")
        self.assertIn("Guérisseur", involved_pnjs)
        self.assertIn("Garde", involved_pnjs)

    def test_initiate_pnj_interaction(self):
        interaction = initiate_pnj_interaction("Guérisseur", "Garde", "demande de ressources")
        self.assertIsInstance(interaction, str)
        self.assertGreater(len(interaction), 0)
        self.assertIn("Guérisseur", interaction)
        self.assertIn("Garde", interaction)

if __name__ == '__main__':
    unittest.main()
