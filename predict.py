import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from huggingface_hub import hf_hub_download
import os

app = FastAPI()

# This class defines the structure of the data the API will receive
class CustomerData(BaseModel):
    Age: float
    TypeofContact: str
    CityTier: int
    DurationOfPitch: float
    Occupation: str
    Gender: str
    NumberOfPersonVisiting: int
    NumberOfFollowups: float
    ProductPitched: str
    PreferredPropertyStar: float
    MaritalStatus: str
    NumberOfTrips: float
    Passport: int
    PitchSatisfactionScore: int
    OwnCar: int
    NumberOfChildrenVisiting: float
    Designation: str
    MonthlyIncome: float

# Define the Hugging Face model repository ID
model_repo_id = "maniKKrishnan/tourism-customer-prediction"
model_filename = "best_model.pkl"

# Download the model from the Hugging Face Model Hub when the app starts
try:
    model_path = hf_hub_download(repo_id=model_repo_id, filename=model_filename)
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer Purchase Prediction API!"}

@app.post("/predict")
def predict(data: CustomerData):
    if not model:
        return {"error": "Model not loaded. Please check the logs."}
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[:, 1][0]
    return {
        "prediction": int(prediction[0]),
        "probability": float(probability)
    }