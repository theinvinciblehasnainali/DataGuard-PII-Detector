# src/config.py

import os

# Base directory for models - You will update this path 
# once you upload to Hugging Face or store them locally
MODEL_BASE_PATH = "models/" 

# Metadata for your specific versions
MODEL_VERSIONS = {
    "tiny": {
        "versions": ["v1", "v2", "v4"],
        "dataset_size": {
            "v1": "20k", "v2": "20k", "v4": "50k"
        },
        "description": "Fastest, lowest latency, lower contextual depth."
    },
    "small": {
        "versions": ["v4", "v5", "v6", "v7"],
        "dataset_size": "50k",
        "description": "Balanced performance and accuracy."
    },
    "base": {
        "versions": ["v2", "v4"],
        "dataset_size": "100k",
        "description": "Highest accuracy, best for complex PII validation."
    }
}

# The labels these models were trained to detect
LABELS = [
    "O",             # Outside (No PII)
    "B-CNIC",        # Pakistani CNIC
    "B-IBAN",        # Bank IBAN
    "B-PHONE",       # Phone Number
    "B-CREDIT_CARD", # Credit Card
    "B-EMAIL",       # Email Address
    "B-SECRET_KEY"   # API/Secret Keys
]