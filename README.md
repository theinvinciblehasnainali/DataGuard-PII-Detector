# DataGuard-PII-Detector
This repository hosts the DataGuard DLP Project's Machine Learning Models. These models (using the BERT NLP Family) have been trained and fine-tuned on datasets up to the size of 100k and tested with different versions. Used BERT: Base, Small, Tiny. The latest versions are ready for use and can be fine-tuned further as needed.

---

# 🛡️ DataGuard: Contextual PII Detection System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Hugging Face](https://img.shields.io/badge/Models-Hugging%20Face-yellow?logo=huggingface&logoColor=black)](https://huggingface.co/theinvinciblehasnainali/DataGuard-Weights)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)]()

**DataGuard** is a Deep Learning-based Data Leakage Prevention (DLP) engine designed specifically for identifying sensitive Pakistani Personally Identifiable Information (PII) with high contextual awareness.

Unlike traditional Regex-based scanners that blindly flag every 13-digit number, DataGuard uses **BERT Sequence Classification** to understand the *intent* behind the data. It accurately distinguishes between a harmless serial number and a genuine CNIC leak.

---

## 🌟 Key Features

* **Context-Aware Analysis:** uses the `bert-base-uncased` architecture to analyze the surrounding words of a potential leak.
    * *Example:* "Order ID 42101..." ➡️ **🟢 SAFE**
    * *Example:* "User CNIC is 42101..." ➡️ **🔴 LEAK**
* **High-Precision Models:** Achieves **99.96% confidence** on validation datasets containing mixed Pakistani PII (CNIC, IBAN, Phone Numbers).
* **Multi-Tier Architecture:** Deployable on everything from cloud servers to edge devices.
    * **Base (v4):** Maximum Accuracy (Server-grade).
    * **Small (v7):** Balanced performance.
    * **Tiny (v4):** Ultra-fast inference for real-time streams.
* **Automated Weight Management:** Built-in scripts to sync heavy model weights (4GB+) directly from Hugging Face.

---

## 🏗️ Architecture & Performance

DataGuard moves beyond simple Named Entity Recognition (NER) by utilizing **Sequence Classification**. The model evaluates the entire semantic structure of a sentence to determine if it constitutes a security risk.

| Model Tier | Backbone | Size | Use Case | Accuracy |
| :--- | :--- | :--- | :--- | :--- |
| **DataGuard Base** | BERT-Base | ~420 MB | Deep Audits / Forensics | **99.96%** |
| **DataGuard Small** | DistilBERT | ~260 MB | Real-time API | 97.5% |
| **DataGuard Tiny** | MobileBERT | ~120 MB | Browser / Edge / Mobile | 94.2% |

---

## 👥 Project Team

This project is the result of a collaborative effort to bring advanced AI security to the DataGuard ecosystem.

| Name | Role | Contribution |
| :--- | :--- | :--- |
| **Hasnain Ali** | **Lead AI Engineer & UI/UX** | Model Training (BERT Fine-tuning), Inference Logic, & Frontend Design. |
| **Hassan Naseer** | Project Manager | Project Architecture, Roadmap Planning, and Resource Management. |
| **Sayyad Ali Naqi** | Backend Engineer | API Integration, Database Management, and Server Deployment. |
| **Feroz u Din** | ML Operations (MLOps) | Pipeline Automation, Model Versioning, and Deployment Strategy. |
| **Hafiz M. Imdadullah Chishti** | Frontend Engineer | Dashboard Implementation and Client-Side Logic. |

---

## 🚀 Installation & Setup

### Prerequisites
* Python 3.8 or higher
* Git
* Internet connection (for downloading weights)

### 1. Clone the Repository
```bash
git clone [https://github.com/theinvinciblehasnainali/DataGuard-PII-Detector.git](https://github.com/theinvinciblehasnainali/DataGuard-PII-Detector.git)
cd DataGuard-PII-Detector

```

### 2. Install Dependencies

We recommend using a virtual environment.

```bash
# Create and activate virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

```

### 3. Download Model Weights (Automated)

Since the model weights (~4.30 GB) are too large for GitHub, they are hosted on Hugging Face. We have provided a setup script to handle this automatically.

```bash
python setup_models.py

```

*This script will fetch the `base`, `small`, and `tiny` models from [Hugging Face](https://www.google.com/url?sa=E&source=gmail&q=https://huggingface.co/theinvinciblehasnainali/DataGuard-Weights) and place them in the `models/` directory.*

---

## 💻 Usage

### Quick Audit (Command Line)

To test the model immediately on a sample string:

```bash
python -m src.inference

```

### Python API Integration

You can easily import DataGuard into your own Python scripts:

```python
from src.inference import PIIDetector

# Initialize the detector (Choose 'base', 'small', or 'tiny')
detector = PIIDetector(tier="base", version="v4")

# Run a prediction
text = "The user with CNIC 42101-1234567-1 accessed the system."
result = detector.predict(text)

print(result)
# Output:
# {
#   "status": "🔴 LEAK",
#   "confidence": "99.96%",
#   "label_id": 1
# }

```

---

## 🔮 Roadmap & Future Enhancements

We are constantly improving DataGuard. Here is what's coming next:

* **[ ] PDF & Document Scanning:** Direct support for scanning invoices, resumes, and legal documents.
* **[ ] OCR Integration:** Detecting PII inside images and scanned IDs.
* **[ ] API Containerization:** Docker support for easy cloud deployment (AWS/Azure).

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

---

## 🙏 Acknowledgments

* **Hugging Face:** For hosting the model weights and providing the `transformers` library.
* **Google Research:** For the original BERT architecture.

```

```