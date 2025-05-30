from fastapi import FastAPI
from app.schemas import LandmarkInput
from app.model import predict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Gesture Model API is live 🚀"}

@app.post("/predict")
def predict_gesture(data: LandmarkInput):
    label = predict(data.landmarks)
    return {"prediction": label}
