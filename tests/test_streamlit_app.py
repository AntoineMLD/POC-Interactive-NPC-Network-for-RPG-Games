import unittest
from src.pnj_helpers import get_contextual_response, get_npcs_involved_in_quest, initiate_npc_interaction

class TestStreamlitApp(unittest.TestCase):

    def test_get_contextual_response(self):
        response = get_contextual_response("Healer", "festival")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def test_get_npcs_involved_in_quest(self):
        involved_npcs = get_npcs_involved_in_quest("Healer", "attack")
        self.assertIn("Healer", involved_npcs)
        self.assertIn("Guard", involved_npcs)

    def test_initiate_npc_interaction(self):
        interaction = initiate_npc_interaction("Healer", "Guard", "resource request")
        self.assertIsInstance(interaction, str)
        self.assertGreater(len(interaction), 0)
        self.assertIn("Healer", interaction)
        self.assertIn("Guard", interaction)

if __name__ == '__main__':
    unittest.main()
