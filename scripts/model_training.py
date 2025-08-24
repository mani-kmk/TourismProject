import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

def train_model():
    # Define file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    processed_data_path = os.path.join(project_root, 'processed_data.csv')

    # Load the processed data
    try:
        data = pd.read_csv(processed_data_path)
    except FileNotFoundError:
        print(f"Error: Processed data file '{processed_data_path}' was not found.")
        return

    # Assuming 'ProdTaken' is your target variable
    X = data.drop('ProdTaken', axis=1)
    y = data['ProdTaken']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    print("Training the model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model training complete.")

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")

    # Save the trained model to the project root
    joblib.dump(model, os.path.join(project_root, 'best_model.pkl'))
    print("Model saved to best_model.pkl")

if __name__ == "__main__":
    train_model()
