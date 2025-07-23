# train.py

import pandas as pd
import string
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import os

# Load training data
df = pd.read_csv("datasets/train.csv")

# Drop uninformative columns
df.drop(columns=["sender", "receiver", "date"], inplace=True)

# Combine 'subject', 'body', 'urls' into a single text feature
def combine_text(row):
    text = f"{row['subject']} {row['body']} {row['urls']}"
    return text.lower().translate(str.maketrans('', '', string.punctuation))

df["text"] = df.apply(combine_text, axis=1)

# Features and target
X = df["text"]
y = df["label"]

# TF-IDF + SVM pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_features=5000)),
    ("svm", SVC(kernel="linear", probability=True))
])

# Train-test split for validation (optional)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
pipeline.fit(X_train, y_train)

# Evaluate on validation set
y_pred = pipeline.predict(X_val)
print("Validation Accuracy:", accuracy_score(y_val, y_pred))
print("Classification Report:\n", classification_report(y_val, y_pred))

# Save the entire pipeline
os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, "models/svm_model.pkl")

print("Model saved to models/svm_model.pkl")
