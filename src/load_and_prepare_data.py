import pandas as pd
import os

# Function to load the data
def load_data(csv_path):
    # Load the CSV file
    df = pd.read_csv(csv_path)
    return df

# Function to prepare the data
def prepare_data(df):
    # For example, we could perform some basic preparations like removing unnecessary columns
    # or manipulating the data as needed
    # For now, just return the original DataFrame
    return df

# Calling the functions to run the data preparation script
if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "dialogues_valoria_enriched.csv")
    df = load_data(csv_path)
    print("Overview of the loaded data:")
    print(df.head())

    print("\nDistribution of roles:")
    print(df['Role'].value_counts())

    print("\nDistribution of emotions:")
    print(df['Émotion'].value_counts())

    print("\nDistribution of intentions:")
    print(df['Intention'].value_counts())
