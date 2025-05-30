# 🚀 Astray Gesture Model Serving API

A FastAPI-based web service for serving the trained hand gesture recognition model. This API allows you to send hand landmark data and receive a predicted gesture in response.

---

## 🧪 Testing

- Backend tested using Pytest & FastAPI's TestClient
- Input validation using Pydantic

---
## 📦 Features

- 🔮 Predict gestures using a pre-trained XGBoost model  
- ⚡ Fast inference via FastAPI  
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

  ---

## 🐳 Containerization with Docker

To run the API in a container, you can build and run the Docker image:

### Build the Docker image

```bash
docker build -t gesture-api .
```

### Build the Docker image

```bash
docker run -p 8000:8000 gesture-api
```
This will start the API inside a Docker container, accessible at:

- **Swagger UI (for testing)**: [http://localhost:8000/docs](http://localhost:8000/docs)  
- **FastAPI root**: [http://localhost:8000](http://localhost:8000)





<img width="958" alt="API" src="https://github.com/user-attachments/assets/33acb1b6-1100-4fb8-8e90-868ecaa9945f" />

