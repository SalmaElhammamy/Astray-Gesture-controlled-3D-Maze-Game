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





<img width="958" alt="API" src="https://github.com/user-attachments/assets/33acb1b6-1100-4fb8-8e90-868ecaa9945f" />

