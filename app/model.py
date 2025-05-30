import numpy as np
import joblib

class GestureModel:
    def __init__(self, model_path, scaler_path=None, encoder_path=None):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path) if scaler_path else None
        self.encoder = joblib.load(encoder_path) if encoder_path else None

    def predict(self, landmarks):
        input_array = np.array(landmarks).reshape(1, -1)
        
        if self.scaler:
            input_array = self.scaler.transform(input_array)
        
        prediction = self.model.predict(input_array)[0]
        
        # Convert NumPy type to native Python type
        if isinstance(prediction, np.generic):
            prediction = prediction.item()

        # Optionally decode if label encoder was used
        if self.encoder:
            prediction = self.encoder.inverse_transform([prediction])[0]
        
        return prediction
