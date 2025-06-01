# 🚀 Astray Gesture Model Serving API

A FastAPI-based web service for serving the trained hand gesture recognition model. This API allows you to send hand landmark data and receive a predicted gesture in response.

---

## 🧪 Testing

- Backend tested using **Pytest** & FastAPI’s **TestClient**  
- Input validation using **Pydantic**

---

## 📦 Features

- 🔮 Predict gestures using a pre-trained **XGBoost** model  
- ⚡ Fast inference via **FastAPI**  
- 📁 Modular and clean project structure  
- 🧪 Interactive API docs at `/docs`  

---

## ▶️ Run the API Server

Use **Uvicorn** to start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Once it starts, visit:

- **Swagger UI (for testing)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **FastAPI root**: [http://127.0.0.1:8000](http://127.0.0.1:8000)

<img width="958" alt="API" src="https://github.com/user-attachments/assets/33acb1b6-1100-4fb8-8e90-868ecaa9945f" />

---

## 🌐 Live Deployment
This API is also deployed live using **ClawCloud**. You can access the online API here:

- **Live Swagger Docs**: https://idmiunzktedg.us-east-1.clawcloudrun.com/docs  
- **Live Base URL**: https://idmiunzktedg.us-east-1.clawcloudrun.com

---

## 🐳 Containerization with Docker

To run the API in a container, you can build and run the Docker image:

### Build the Docker image

```bash
docker build -t gesture-api .
```

### Run the Docker container

```bash
docker run -p 8000:8000 gesture-api
```

This will start the API inside a Docker container, accessible at:

- **Swagger UI (for testing)**: [http://localhost:8000/docs](http://localhost:8000/docs)  
- **FastAPI root**: [http://localhost:8000](http://localhost:8000)

<img width="748" alt="docker_2" src="https://github.com/user-attachments/assets/7897eb62-fa2d-48b2-ab06-a03473921456" />

<img width="946" alt="docker_1" src="https://github.com/user-attachments/assets/cc53d6cd-c525-4954-80b8-e9a67fbc29c3" />

---

## 📊 Monitoring Metrics

To maintain a reliable and robust API, we monitor key metrics using **Prometheus** and **Grafana**:

### ✅ Model-related Metric: Prediction Latency
We track the model’s response time to identify any slowness or degradation in prediction speed.

### ✅ Data-related Metric: Invalid Input Count
We monitor the number of invalid landmark inputs received to detect issues in the incoming data stream.

### ✅ Server-related Metric: API Request Count
We keep track of how many requests hit our server to understand usage patterns and performance.

---

## 📈 Grafana Dashboard (Live Monitoring)

Metrics are visualized using a Grafana dashboard connected to Prometheus. It includes real-time panels for:

- 🔁 Total API requests (`request_count_total`)  
- ⏱️ Average prediction latency (`prediction_latency_seconds`)  
- 🚫 Invalid input count (`invalid_input_count_total`)  


<img width="954" alt="Dashboard" src="https://github.com/user-attachments/assets/5787dc9f-8336-4b2b-bd7f-3b5a8dcbb793" />
