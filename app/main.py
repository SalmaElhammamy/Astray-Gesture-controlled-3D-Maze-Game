from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from app.schemas import LandmarkInput
from app.model import GestureModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = GestureModel(
    model_path="models/model.pkl",
    encoder_path="models/label_encoder.pkl"
)

# Prometheus metrics
REQUEST_COUNT = Counter('request_count', 'Total API requests')
PREDICTION_LATENCY = Histogram('prediction_latency_seconds', 'Prediction latency in seconds')
INVALID_INPUTS = Counter('invalid_input_count', 'Count of invalid inputs received')

# Middleware to track metrics on every request
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    REQUEST_COUNT.inc()
    with PREDICTION_LATENCY.time():
        response = await call_next(request)
    return response

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Gesture Model API is live 🚀"}

# Prediction endpoint
@app.post("/predict")
def predict_gesture(data: LandmarkInput):
    try:
        label = model.predict(data.landmarks)
    except Exception:
        INVALID_INPUTS.inc()
        raise
    return {"prediction": label}

# Metrics endpoint for Prometheus to scrape
@app.get("/metrics")
async def metrics():
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)
