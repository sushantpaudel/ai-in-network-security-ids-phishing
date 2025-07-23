# Intrusion Detection System

[GitHub Repository](https://github.com/sushantpaudel/ai-in-network-security-ids-phishing)

[Kaggle Dataset](https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection/data)

## About Dataset

### Background

The dataset to be audited was provided which consists of a wide variety of intrusions simulated in a military network environment. It created an environment to acquire raw TCP/IP dump data for a network by simulating a typical US Air Force LAN. The LAN was focused like a real environment and blasted with multiple attacks. A connection is a sequence of TCP packets starting and ending at some time duration between which data flows to and from a source IP address to a target IP address under some well-defined protocol. Also, each connection is labelled as either normal or as an attack with exactly one specific attack type. Each connection record consists of about 100 bytes.
For each TCP/IP connection, 41 quantitative and qualitative features are obtained from normal and attack data (3 qualitative and 38 quantitative features) .The class variable has two categories:
• Normal
• Anomalous



---

### 🔍 Feature Descriptions for Intrusion Detection Dataset

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `duration`                    | Length (in seconds) of the connection                                       |
| `protocol_type`               | Protocol used (e.g., TCP, UDP, ICMP)                                        |
| `service`                     | Network service on the destination (e.g., HTTP, FTP, Telnet)                |
| `flag`                        | Status flag of the connection (e.g., SF = successful connection)            |
| `src_bytes`                  | Number of bytes sent from source to destination                             |
| `dst_bytes`                  | Number of bytes sent from destination to source                             |
| `land`                        | 1 if connection is from/to the same host/port; otherwise 0                  |
| `wrong_fragment`              | Number of wrong fragments in this connection                               |
| `urgent`                      | Number of urgent packets                                                    |
| `hot`                         | Number of "hot" indicators (e.g., access to system directories)             |
| `num_failed_logins`           | Number of failed login attempts                                             |
| `logged_in`                   | 1 if successfully logged in; otherwise 0                                    |
| `num_compromised`             | Number of compromised conditions                                            |
| `root_shell`                  | 1 if root shell was obtained; otherwise 0                                   |
| `su_attempted`                | 1 if "su root" command attempted; otherwise 0                               |
| `num_root`                    | Number of "root" accesses                                                   |
| `num_file_creations`          | Number of file creation operations                                          |
| `num_shells`                  | Number of shell prompts invoked                                             |
| `num_access_files`            | Number of accesses to sensitive files                                       |
| `num_outbound_cmds`           | Number of outbound commands in an ftp session (almost always zero)         |
| `is_host_login`               | 1 if login belongs to host; otherwise 0                                     |
| `is_guest_login`              | 1 if login is a guest login; otherwise 0                                    |
| `count`                       | Number of connections to the same host in the past 2 seconds                |
| `srv_count`                   | Number of connections to the same service in the past 2 seconds             |
| `serror_rate`                 | % of connections that have "SYN" errors                                     |
| `srv_serror_rate`             | % of service connections with "SYN" errors                                  |
| `rerror_rate`                 | % of connections with "REJ" errors                                          |
| `srv_rerror_rate`             | % of service connections with "REJ" errors                                  |
| `same_srv_rate`               | % of connections to the same service                                        |
| `diff_srv_rate`               | % of connections to different services                                      |
| `srv_diff_host_rate`          | % of service connections to different hosts                                 |
| `dst_host_count`              | Number of connections having the same destination host                     |
| `dst_host_srv_count`          | Number of connections having the same destination service                  |
| `dst_host_same_srv_rate`      | % of connections to the same service (to the same host)                     |
| `dst_host_diff_srv_rate`      | % of connections to different services (to the same host)                   |
| `dst_host_same_src_port_rate`| % of connections to the same source port                                    |
| `dst_host_srv_diff_host_rate`| % of service connections to different destination hosts                     |
| `dst_host_serror_rate`        | % of destination host connections with "SYN" errors                         |
| `dst_host_srv_serror_rate`    | % of destination service connections with "SYN" errors                      |
| `dst_host_rerror_rate`        | % of destination host connections with "REJ" errors                         |
| `dst_host_srv_rerror_rate`    | % of destination service connections with "REJ" errors                      |
| `class`                       | Target variable: `normal` or `anomaly` (intrusion)                          |

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

4. **Train the Intrusion Detection model**

```
python3 train.py
```

5. **Test the model**

```
python3 test.py
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