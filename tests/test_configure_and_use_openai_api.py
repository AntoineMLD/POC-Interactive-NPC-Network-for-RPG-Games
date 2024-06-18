import unittest
from src.configure_and_use_openai_api import configure_openai_api, generate_dialogue

class TestOpenAIAPI(unittest.TestCase):

    def test_configure_openai_api(self):
        # Test de configuration API
        try:
            configure_openai_api()
        except ValueError as e:
            self.fail(f"Configuration de l'API échouée: {e}")

    def test_generate_dialogue(self):
        # Test de génération de dialogue
        prompt = "Le joueur demande au Guérisseur : Comment puis-je aider le village ?"
        response = generate_dialogue(prompt)
        self.assertTrue(isinstance(response, str) and len(response) > 0, "La réponse ne doit pas être vide")

if __name__ == '__main__':
    unittest.main()
