# test.py

import joblib

# Load the saved model pipeline
model = joblib.load("models/svm_model.pkl")

# Collect user input
print("\n=== Phishing Email Detection ===")
subject = input("Enter email subject: ")
body = input("Enter email body: ")
urls = input("Enter URLs (if any, separate by space): ")

# Preprocess input
import string

def preprocess_input(subject, body, urls):
    combined = f"{subject} {body} {urls}"
    return combined.lower().translate(str.maketrans('', '', string.punctuation))

text_input = preprocess_input(subject, body, urls)

# Predict
prediction = model.predict([text_input])[0]
probability = model.predict_proba([text_input])[0][prediction]

# Output result
label = "Phishing" if prediction == 1 else "Legitimate"
print(f"\n📧 The email is classified as: **{label}**")
print(f"🔒 Confidence: {probability * 100:.2f}%")
