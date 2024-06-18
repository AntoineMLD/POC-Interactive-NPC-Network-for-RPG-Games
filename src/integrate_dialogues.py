from src.configure_and_use_openai_api import generate_dialogue

# Function to clean the generated responses
def clean_response(response):
    response = response.replace('\"', '').strip()  # Remove double quotes and leading/trailing spaces
    response = response.replace('«', '').replace('»', '')  # Remove French quotation marks
    response = response.split('<<')[0]  # Split and keep content before '<<' marker
    response = response.split('1.')[0]  # Split and keep content before '1.' marker
    response = response.split('\n')[0]  # Keep only the first line if multiple lines
    return response.strip()

def integrate_dialogues():
    prompts = {
        "Healer": "The player asks the Healer how they can help save the village. The Healer responds with specific actions like gathering herbs or supplies:",
        "Merchant": "The player asks the Merchant what they can do to help the village in terms of trade. The Merchant explains the items he is looking for such as crystals, rare feathers, or swords:",
        "Blacksmith": "The player asks the Blacksmith for advice on how to fortify the village. The Blacksmith responds with detailed instructions on building barriers and making weapons:",
        "Hunter": "The player asks the Hunter if he has seen any signs of danger in the forest. The Hunter describes what he has observed, such as unusual animals or suspicious tracks:",
        "Guard": "The player asks the Guard how they can contribute to the village's security. The Guard gives specific tasks such as patrolling, watching the borders, or helping the villagers:",
        "Lord": "The player asks the Lord what is necessary to ensure peace in the village. The Lord gives concrete examples of priorities like security, food, and infrastructure:",
        "Farmer": "The player asks the Farmer how they can help with harvesting and field preparation. The Farmer details the tasks to be done such as planting, watering, and harvesting:"
    }

    dialogues = []
    for npc, prompt in prompts.items():
        response = clean_response(generate_dialogue(prompt))
        dialogues.append({"NPC": npc, "Response": response})

    return dialogues

# If you want to run this script directly to see the results
if __name__ == "__main__":
    dialogues = integrate_dialogues()
    for dialogue in dialogues:
        print(f"{dialogue['NPC']} : {dialogue['Response']}")
