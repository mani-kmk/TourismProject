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
