import uvicorn
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# FastAPI app
app = FastAPI()

# Request schema
class InsuranceInput(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

@app.post("/predict")
def predict(data: InsuranceInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Predict
    prediction = model.predict(input_df)[0]
    return {"predicted_charge": round(prediction, 2)}

# Run with: uvicorn predict:app --reload
