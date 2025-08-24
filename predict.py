import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI
app = FastAPI()

# Load the trained model
model = joblib.load("best_model.pkl")

# Define the input data model
class PredictionInput(BaseModel):
    Age: int
    ProdTaken: int

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
