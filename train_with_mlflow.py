import numpy as np
import pandas as pd
import pickle
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier

### Load data 
df = pd.read_csv("hand_landmarks_data.csv")  

# --- 1. Normalization ---
landmark_columns = [f"{axis}{i}" for i in range(1, 22) for axis in ['x', 'y', 'z']]

def normalize_landmarks(row):
    landmarks = np.array(row[landmark_columns].values, dtype=np.float64).reshape(21, 3)
    wrist = landmarks[0]
    mid_finger_tip = landmarks[9]
    scale_1 = np.linalg.norm(mid_finger_tip - wrist)
    scale_2 = np.max(np.linalg.norm(landmarks - wrist, axis=1))
    scale = max(scale_1, scale_2)
    scale = 1 if scale == 0 or np.isnan(scale) else scale
    normalized = (landmarks - wrist) / scale
    return normalized.flatten()

df[landmark_columns] = df.apply(normalize_landmarks, axis=1, result_type="expand")
print("✅ Landmarks Normalized")

# --- 2. Label Encoding ---
encoder = LabelEncoder()
df['label'] = encoder.fit_transform(df['label'])

# Save encoder
with open('label_encoder.pkl', 'wb') as file:
    pickle.dump(encoder, file)
print("✅ Labels Encoded & Saved")

# --- 3. Split Data ---
X = df.drop(columns=["label"])
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("✅ Data Split")

# --- 4. Define Helper Function ---
def train_and_log_model(model, model_name):
    with mlflow.start_run(run_name=model_name):
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average='weighted')
        rec = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')

        # Logging Metrics
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("precision", prec)
        mlflow.log_metric("recall", rec)
        mlflow.log_metric("f1_score", f1)

        # Logging Model
        mlflow.sklearn.log_model(model, model_name)

        print(f"\n🔹 {model_name} Results:")
        print(f"Accuracy: {acc * 100:.2f}%")
        print(f"Precision: {prec * 100:.2f}%")
        print(f"Recall: {rec * 100:.2f}%")
        print(f"F1-Score: {f1 * 100:.2f}%")

# --- 5. MLflow Setup ---
mlflow.set_experiment("Hand Gesture Classification")

# --- 6. Train Models & Log ---
train_and_log_model(SVC(kernel="rbf"), "SVM")
train_and_log_model(XGBClassifier(use_label_encoder=False, eval_metric="mlogloss"), "XGBoost")
train_and_log_model(RandomForestClassifier(n_estimators=100), "RandomForest")

print("\n✅ All Models Trained & Logged")