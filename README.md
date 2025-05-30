# Astray-Gesture-controlled-3D-Maze-Game - Research Repository
This repository contains the research and experimentation code for training gesture recognition models for the Astray 3D Maze Game. The goal is to classify hand gestures using MediaPipe landmarks and select the best-performing model based on performance metrics and MLflow tracking.


---

## 🔬 Models Trained

We trained and evaluated three classification models:

- **SVM (Support Vector Machine)**
- **Random Forest**
- **XGBoost**

All models were tracked using MLflow for reproducibility and performance comparison.

---

## 📊 Model Comparison

| Model         | Accuracy | Precision | Recall | F1-Score |
|---------------|----------|-----------|--------|----------|
| SVM           | 96.46%   | 96.53%    | 96.46% | 96.46%   |
| XGBoost       | 98.09%   | 98.10%    | 98.09% | 98.09%   |
| Random Forest | 97.72%   | 97.73%    | 97.72% | 97.72%   |

🏆 **Best Model**: **XGBoost**, due to its high accuracy and balanced precision, recall, and F1-score.




