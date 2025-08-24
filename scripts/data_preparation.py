import pandas as pd
import os

def prepare_data():
    # Define file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, 'tourism_dataset.csv')
    processed_data_path = os.path.join(project_root, 'processed_data.csv')

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

    # Ensure all columns are numeric
    for col in data.columns:
        if data[col].dtype == 'object':
            print(f"Warning: Column '{col}' is still of object type. Check data.")

    # Save the processed data
    data.to_csv(processed_data_path, index=False)
    print("Data preparation complete. Processed data saved to processed_data.csv")

if __name__ == "__main__":
    prepare_data()
