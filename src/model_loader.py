# src/model_loader.py
import os
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def load_pii_model(model_tier, version):
    # Absolute path logic
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    model_path = os.path.join(project_root, "models", model_tier, version).replace("\\", "/")

    print(f"🔄 Loading Sequence Classifier from: {model_path}")

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    
    return tokenizer, model