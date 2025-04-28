from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("california_housing_model_no_population.pkl")
scaler = joblib.load("scaler_no_population.pkl")
model_rmse = joblib.load("model_rmse.pkl")

class HousingData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveOccup: float
    Latitude: float
    Longitude: float
    AveHouseVal: float

@app.post("/predict")
async def predict(data: HousingData):
    input_data = np.array([[
        data.MedInc, data.HouseAge, data.AveRooms, data.AveOccup,
        data.Latitude, data.Longitude, data.AveHouseVal
    ]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    return {
        "prediction": float(prediction[0]),
        "model_rmse": float(model_rmse)
    }