# train.py

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

# Load training data
df_train = pd.read_csv("datasets/train.csv")

# Separate features and target
X_train = df_train.drop("class", axis=1)
y_train = df_train["class"].map({"normal": 0, "anomaly": 1})  # Encode labels

# One-hot encode categorical variables
categorical_cols = ["protocol_type", "service", "flag"]
X_train = pd.get_dummies(X_train, columns=categorical_cols)

# Save column names for later use in test.py
feature_names = X_train.columns.tolist()

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred_train = model.predict(X_train_scaled)
acc = accuracy_score(y_train, y_pred_train)
print(f"Training Accuracy: {acc:.4f}")

# Save model artifacts
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/logistic_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(feature_names, "models/feature_names.pkl")  # NEW: Save feature names
