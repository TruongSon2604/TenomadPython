from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import joblib
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse


app= FastAPI()
model = joblib.load("model.pkl")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

class HouseData(BaseModel):
    area: float
    num_bedrooms: int
    num_bathrooms: int

@app.post("/predict")
def predict_price(data: List[HouseData]):
    features= [[item.area, item.num_bedrooms, item.num_bathrooms] for item in data]
    predict_price = model.predict(features)
    return {"predicted_price": predict_price.tolist()}