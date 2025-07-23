# test.py

import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Load test data
df_test = pd.read_csv("datasets/test.csv")

# Separate features and labels
y_test = df_test["class"].map({"normal": 0, "anomaly": 1})  # Encode target
X_test = df_test.drop("class", axis=1)  # Drop target from features

# One-hot encode categorical variables
categorical_cols = ["protocol_type", "service", "flag"]
X_test = pd.get_dummies(X_test, columns=categorical_cols)

# Load scaler, model, and feature names from training
scaler = joblib.load("models/scaler.pkl")
model = joblib.load("models/logistic_model.pkl")
feature_names = joblib.load("models/feature_names.pkl")

# Ensure test features match training features
X_test = X_test.reindex(columns=feature_names, fill_value=0)

# Scale test data
X_test_scaled = scaler.transform(X_test)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Evaluate
acc = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {acc:.4f}")

cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)

# Plot confusion matrix
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Normal", "Anomaly"], yticklabels=["Normal", "Anomaly"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# Plot classification report
metrics_df = pd.DataFrame(report).transpose()
metrics_df = metrics_df.loc[["0", "1"], ["precision", "recall", "f1-score"]]
metrics_df.rename(index={"0": "Normal", "1": "Anomaly"}, inplace=True)

metrics_df.plot(kind="bar", figsize=(8, 6), colormap="viridis")
plt.title("Classification Metrics by Class")
plt.ylabel("Score")
plt.ylim(0, 1)
plt.grid(axis="y")
plt.tight_layout()
plt.show()
