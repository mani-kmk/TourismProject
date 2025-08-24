import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import os
from huggingface_hub import hf_hub_download

# Initialize FastAPI
app = FastAPI()

# Download the trained model from the Hugging Face Hub
model_repo_id = "maniKKrishnan/tourism-customer-prediction"
model_filename = "best_model.pkl"

try:
    model_path = hf_hub_download(repo_id=model_repo_id, filename=model_filename)
    model = joblib.load(model_path)
    print("Model downloaded and loaded successfully.")
except Exception as e:
    raise RuntimeError(f"Failed to download or load model: {e}")

# Define the input data model based on your dataset's columns
class PredictionInput(BaseModel):
    Age: int
    CityTier: int
    DurationOfPitch: int
    NumberOfPersonVisiting: int
    NumberOfFollowups: int
    PreferredPropertyStar: int
    NumberOfTrips: int
    Passport: int
    PitchSatisfactionScore: int
    OwnCar: int
    NumberOfChildrenVisiting: int
    MonthlyIncome: int
    TypeofContact_SelfEnquiry: int
    Occupation_LargeBusiness: int
    Occupation_Salaried: int
    Occupation_SmallBusiness: int
    Gender_Male: int
    ProductPitched_Deluxe: int
    ProductPitched_King: int
    ProductPitched_Super: int
    MaritalStatus_Married: int
    MaritalStatus_Single: int
    MaritalStatus_Unmarried: int

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
