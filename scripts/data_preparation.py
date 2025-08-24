import pandas as pd
import os

def prepare_data():
    # Define file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, 'tourism_dataset.csv')
    
    # Load the raw data
    try:
        data = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Error: The file '{data_path}' was not found.")
        return

    print("Data loaded. Performing data cleaning and one-hot encoding...")
    
    # Identify categorical columns to be encoded
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns

    # Drop any rows with missing values
    data.dropna(inplace=True)

    # Apply one-hot encoding
    data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)
    
    # Save the processed data to the project root
    data.to_csv(os.path.join(project_root, 'processed_data.csv'), index=False)
    print("Data preparation complete. Processed data saved to processed_data.csv")

if __name__ == "__main__":
    prepare_data()