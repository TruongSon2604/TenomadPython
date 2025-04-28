from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sklearn.metrics import mean_squared_error

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

templates= Jinja2Templates(directory="templates")
model = joblib.load("student_score_model.pkl")
scaler = joblib.load("scaler.pkl")
rmse = joblib.load("rmse.pkl")

class StudentData(BaseModel):
    study_hours: float
    previous_test_score: float

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("student_score.html", {"request": request})

@app.post("/predict_score")
async def predict_score(data: StudentData):
    input_data = np.array([[data.study_hours, data.previous_test_score]])
    input_scaled = scaler.transform(input_data)
    predicted_score = model.predict(input_scaled)
    return {"predicted_score": predicted_score[0],"rmse":rmse}
