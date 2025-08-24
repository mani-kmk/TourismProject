import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import os

# Initialize FastAPI
app = FastAPI()

# Load the trained model
model_path = "best_model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    raise FileNotFoundError(f"Model file '{model_path}' not found.")

# Define the input data model based on your dataset's columns
# NOTE: This model is a placeholder. You must update it with all the
# relevant features from your processed_data.csv file.
class PredictionInput(BaseModel):
    Age: int
    CityTier_2: int
    CityTier_3: int
    DurationOfPitch: int
    Gender_Male: int
    Gender_FeMale: int
    Gender_NotSpecified: int
    NumberOfPersonVisiting: int
    NumberOfFollowups: int
    ProductPitched_Deluxe: int
    ProductPitched_King: int
    ProductPitched_Super: int
    ProductPitched_Basic: int
    PreferredPropertyStar: int
    MaritalStatus_Married: int
    MaritalStatus_Single: int
    MaritalStatus_Unmarried: int
    NumberOfTrips: int
    Passport: int
    PitchSatisfactionScore: int
    OwnCar: int
    NumberOfChildrenVisiting: int
    MonthlyIncome: int


# Define the prediction endpoint
@app.post("/predict")
def predict(data: PredictionInput):
    # Prepare the input data for the model
    input_df = pd.DataFrame([data.dict()])
    
    # Make a prediction
    prediction = model.predict(input_df)[0]
    
    # Return the prediction result
    return {"prediction": int(prediction)}

# Root endpoint for health check
@app.get("/")
def home():
    return {"message": "API is running."}