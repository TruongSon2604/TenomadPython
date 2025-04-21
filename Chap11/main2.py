from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

# Thêm middleware CORS để chấp nhận yêu cầu từ tất cả các nguồn (hoặc bạn có thể giới hạn ở một nguồn cụ thể)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load mô hình và scaler đã được train từ trước
model = joblib.load("california_housing_model_no_population.pkl")
scaler = joblib.load("scaler_no_population.pkl")

class HousingData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveOccup: float
    Latitude: float
    Longitude: float
    AveHouseVal: float

# API endpoint dự đoán giá nhà
@app.post("/predict")
async def predict(data: HousingData):
    input_data = np.array([[
        data.MedInc, data.HouseAge, data.AveRooms, data.AveOccup,
        data.Latitude, data.Longitude, data.AveHouseVal
    ]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    return {"prediction": prediction[0]}