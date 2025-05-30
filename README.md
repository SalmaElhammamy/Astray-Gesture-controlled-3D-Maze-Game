# Astray-Gesture-controlled-3D-Maze-Game - Research Repository
This repository contains the research and experimentation code for training gesture recognition models for the Astray 3D Maze Game. The goal is to classify hand gestures using MediaPipe landmarks and select the best-performing model based on performance metrics and MLflow tracking.


---

## 🔬 Models Trained

We trained <img width="954" alt="mlflow_1" src="https://github.com/user-attachments/assets/6fc1a2be-d6a8-4137-b5b3-495ffd651769" />
and evaluated three classification models:

- **SVM (Support Vector Machine)**
- **Random Forest**
- **XGBoost**

All models were tracked using MLflow for reproducibility and performance comparison.



---

## 📊 Model Comparison
<img width="957" alt="mlFlow_2" src="https://github.com/user-attachments/assets/846b12e0-d7a1-4b97-9951-e1c0d61100df" />


| Model         | Accuracy | Precision | Recall | F1-Score |
|---------------|----------|-----------|--------|----------|
| SVM           | 96.46%   | 96.53%    | 96.46% | 96.46%   |
| XGBoost       | 98.09%   | 98.10%    | 98.09% | 98.09%   |
| Random Forest | 97.72%   | 97.73%    | 97.72% | 97.72%   |

🏆 **Best Model**: **XGBoost**, due to its high accuracy and balanced precision, recall, and F1-score.




<img width="958" alt="mlflow_3" src="https://github.com/user-attachments/assets/14ef1a08-5415-4411-901b-8b2ef20af624" />
