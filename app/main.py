from fastapi import FastAPI
from app.schemas import LandmarkInput
from app.model import GestureModel

app = FastAPI()

model = GestureModel(
    model_path="models/model.pkl",
    encoder_path="models/label_encoder.pkl"
)

@app.get("/")
def read_root():
    return {"message": "Gesture Model API is live 🚀"}

@app.post("/predict")
def predict_gesture(data: LandmarkInput):
    label = model.predict(data.landmarks)
    return {"prediction": label}
