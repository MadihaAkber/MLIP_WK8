from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(title="California House Price Predictor")

model_path = Path(__file__).resolve().parent.parent / "models" / "best_model.pkl"
model = joblib.load(model_path)


class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.get("/")
def home():
    return {"message": "House Price Prediction API is running"}


@app.post("/predict")
def predict(features: HouseFeatures):
    data = pd.DataFrame([features.model_dump()])
    prediction = model.predict(data)[0]

    return {
        "predicted_price_usd": round(float(prediction) * 100000, 2)
    }