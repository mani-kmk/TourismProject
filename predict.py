import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from huggingface_hub import hf_hub_download

# Initialize the FastAPI app
app = FastAPI()

# Model and repository information
model_repo_id = "maniKKrishnan/tourism-customer-prediction"
model_filename = "model_lgbm.pkl"

# Download the model and load it
try:
    model_path = hf_hub_download(repo_id=model_repo_id, filename=model_filename)
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    raise RuntimeError(f"Failed to download or load model: {e}")

# Define the input data model
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
def predict_outcome(data: PredictionInput):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    prediction_proba = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "prediction_probability": float(prediction_proba)
    }

# A simple root endpoint for health check
@app.get("/")
def read_root():
    return {"message": "API is running! Visit /docs for documentation."}
