# Phishing Email Detection System

[GitHub Repository](https://github.com/sushantpaudel/ai-in-network-security-ids-phishing)

[Kaggle Dataset - All](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset/data)

## About Dataset

### PHISHING EMAIL DATASET
This dataset was compiled by researchers to study phishing email tactics. It combines emails from a variety of sources to create a comprehensive resource for analysis.

### Initial Datasets:
- Enron and Ling Datasets: These datasets focus on the core content of phishing emails, containing subject lines, email body text, and labels indicating whether the email is spam (phishing) or legitimate.
- CEAS, Nazario, Nigerian Fraud, and SpamAssassin Datasets: These datasets provide broader context for the emails, including sender information, recipient information, date, and labels for spam/legitimate classification.

### Final Dataset:
The final dataset combines the information from the initial datasets into a single resource for analysis. This dataset contains:
- Approximately 82,500 emails
- 42,891 spam emails
- 39,595 legitimate emails

This dataset allows researchers to study the content of phishing emails and the context in which they are sent to improve detection methods.

---

### 🔍 Feature Descriptions for Phishing Email Detection System

---

### 🚀 Setup Instructions

1. **Create Python virtual environment**

```
python3 -m venv venv
```

2. **Activate the virtual environment**

```
# Linux/Mac
source ./venv/bin/activate

# Windows
.\venv\Scripts\activate
```

3. **Install dependencies**

```
pip install -r requirements.txt
```

4. **Open Jupyter Lab Browser(IDE)**

```
jupyter lab
```

6. **Evaluate results**



## Understanding Evaluation Metrics

**True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN)**
- **True Positive (TP)**: The model correctly identifies a positive case (e.g., correctly detecting an intrusion).
- **True Negative (TN)**: The model correctly identifies a negative case (e.g., correctly recognizing normal traffic).
- **False Positive (FP)**: The model incorrectly labels a negative case as positive (e.g., flagging normal traffic as an intrusion — also called a false alarm).
- **False Negative (FN)**: The model incorrectly labels a positive case as negative (e.g., missing an actual intrusion).

**Confusion Matrix**
- A table that shows the number of correct and incorrect predictions made by the model, broken down by each class. It helps to visualize true positives, true negatives, false positives, and false negatives.

**Precision**
- The ratio of correctly predicted positive observations to the total predicted positives. It answers: Of all instances flagged as anomalies, how many were actually anomalies?

**Recall (Sensitivity)**
- The ratio of correctly predicted positive observations to all actual positives. It answers: Of all actual anomalies, how many did the model correctly identify?

**F1 Score**
- The harmonic mean of precision and recall. It provides a balance between precision and recall, especially useful when you need to seek a balance between false positives and false negatives.

These metrics are critical for intrusion detection systems because:
- High precision means fewer false alarms (false positives), which helps avoid overwhelming security teams with unnecessary alerts.
- High recall ensures the system catches most of the real threats, minimizing missed intrusions.
- The F1 score helps balance these two, providing a single measure of overall accuracy.