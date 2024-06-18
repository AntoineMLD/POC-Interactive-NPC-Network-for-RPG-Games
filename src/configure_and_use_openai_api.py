import openai
import os
from dotenv import load_dotenv

# Build the path to the .env file in the root directory
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

def configure_openai_api():
    """Configure OpenAI API settings using environment variables."""
    openai.api_type = "azure"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_base = os.getenv("OPENAI_API_BASE")
    openai.api_version = os.getenv("OPENAI_API_VERSION")

    # Check loaded values
    if None in [openai.api_key, openai.api_base, openai.api_version]:
        raise ValueError("One or more environment variables are missing or incorrect. Check your .env file.")

# Call the function to configure the API when the module is loaded
configure_openai_api()

# Function to generate a dialogue with GPT-3.5 Turbo
def generate_dialogue(prompt):
    response = openai.Completion.create(
        engine=os.getenv("OPENAI_API_DEPLOYMENT"),
        prompt=prompt,
        max_tokens=200,      # Increase the number of tokens to allow for longer responses if necessary
        temperature=0.7,     # Controls the creativity of the response
        n=1,                 # Number of responses to generate
        stop=["\n", "Player", "The"]  # Stop after these tokens to avoid overly long or incomplete responses
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    prompt = "The player asks the Healer: How can I help the village?"
    response = generate_dialogue(prompt)
    print(f"Model response: {response}")
