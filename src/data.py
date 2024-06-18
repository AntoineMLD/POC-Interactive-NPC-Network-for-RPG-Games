import pandas as pd
import os

# Create the enriched DataFrame
data = {
    "NPC": ["Healer", "Merchant", "Blacksmith", "Hunter", "Guard", "Lord", "Farmer",
            "Healer", "Merchant", "Blacksmith", "Hunter", "Guard", "Lord", "Farmer",
            "Healer", "Merchant", "Blacksmith", "Hunter", "Guard", "Lord", "Farmer"],
    "Role": ["Healer", "Trader", "Craftsman", "Hunter", "Protector", "Leader", "Worker",
             "Healer", "Trader", "Craftsman", "Hunter", "Protector", "Leader", "Worker",
             "Healer", "Trader", "Craftsman", "Hunter", "Protector", "Leader", "Worker"],
    "Context": ["Health", "Commerce", "Defense", "Exploration", "Security", "Management", "Fields",
                "Attack", "Attack", "Supply", "Quest", "Security", "Ceremony", "Harvest",
                "Supply", "Negotiation", "Construction", "Surveillance", "Reinforcement", "Planning", "Preparation"],
    "Emotion": ["Grateful", "Relieved", "Cautious", "Curious", "Determined", "Authoritative", "Grateful",
                "Worried", "Anxious", "Industrious", "Excited", "Protective", "Solemn", "Happy",
                "Focused", "Satisfied", "Engaged", "Attentive", "Optimistic", "Strategic", "Involved"],
    "Intention": ["Help", "Disseminate", "Protect", "Observe", "Monitor", "Organize", "Work",
                  "Help", "Inform", "Produce", "Explore", "Defend", "Lead", "Collect",
                  "Collect", "Negotiate", "Manufacture", "Patrol", "Reinforce", "Plan", "Organize"],
    "Dialogue": ["I am happy to see you here.", "The Merchant announces that the Healer is looking for rare herbs.", "We need to fortify the village with strong barriers.", "I saw wolf tracks near the forest.", "We need to strengthen the patrols around the village.", "It is crucial to plan our defense against external threats.", "Thank you for helping me harvest the potatoes.",
                 "I fear the attack will cause serious injuries.", "The Merchant has heard rumors of an imminent attack.", "We need more materials for weapons.", "I am searching for a rare creature in the mountains.", "I will not let anyone pass without being checked.", "We must celebrate our victories to boost morale.", "This year's harvest has been abundant thanks to your help.",
                 "I need to gather more medicinal herbs in the forest.", "I found a buyer for our high-quality products.", "I will make new weapons to strengthen our defenses.", "I am monitoring the surroundings for any suspicious activity.", "With new reinforcements, we can effectively protect the village.", "We need to develop a detailed plan for the expansion of our village.", "I need to organize the supplies for the winter."],
    "Rumor/Action": ["Heal", "Healer", "Security", "Warning", "Preparation", "Coordination", "Help",
                     "Heal", "Guard", "Security", "Curiosity", "Security", "Organization", "Help",
                     "Search", "Transaction", "Defense", "Security", "Defense", "Development", "Supply"],
    "Detailed_Context": ["Recovery", "Alert", "Preparation", "Observation", "Security", "Organization", "Harvest",
                         "Preparation", "Precaution", "Resources", "Adventure", "Control", "Celebration", "Storage",
                         "Gathering", "Sale", "Production", "Observation", "Securing", "Strategy", "Organization"],
    "Detailed_Emotions": ["Joy", "Relief", "Caution", "Worry", "Vigilance", "Responsibility", "Gratitude",
                          "Panic", "Alert", "Urgency", "Excitement", "Firmness", "Pride", "Satisfaction",
                          "Focus", "Satisfaction", "Determination", "Attention", "Optimism", "Determination", "Responsibility"]
}

# Create the DataFrame
df_enriched = pd.DataFrame(data)

# Define the path to the src directory
src_dir = os.path.join(os.path.dirname(__file__), "src")

# Ensure the src directory exists
os.makedirs(src_dir, exist_ok=True)

# Define the full path to the CSV file in the src directory
csv_file_path = os.path.join(src_dir, "dialogues_valoria_enriched.csv")

# Save the DataFrame as a CSV file in the src directory
df_enriched.to_csv(csv_file_path, index=False)

print(f"Enriched CSV file saved at {csv_file_path}")
