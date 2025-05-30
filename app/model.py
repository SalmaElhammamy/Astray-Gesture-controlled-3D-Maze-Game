import joblib
import os

model = joblib.load(os.path.join("models", "model.pkl"))

def predict(landmarks):
    return model.predict([landmarks])[0]
