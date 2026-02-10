import torch
import torch.nn.functional as F
from src.model_loader import load_pii_model

class PIIDetector:
    def __init__(self, tier="base", version="v4"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer, self.model = load_pii_model(tier, version)
        self.model.to(self.device)
        self.model.eval()

    def predict(self, text):
        # Your Draft's exact settings
        inputs = self.tokenizer(
            text, 
            return_tensors="pt", 
            truncation=True, 
            max_length=128
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)

        # Softmax to get that 99% confidence
        probs = F.softmax(outputs.logits, dim=-1)
        prediction = torch.argmax(probs).item()
        confidence = probs[0][prediction].item()

        # Logic from your Draft
        # Assuming label 1 = LEAK, label 0 = SAFE
        is_leak = (prediction == 1)
        
        # Professional Filter: Ignore "fake" or "test"
        is_fake_test = any(x in text.lower() for x in ["fake", "dummy", "test case"])
        
        if is_leak and not is_fake_test:
            status = "🔴 LEAK"
        else:
            status = "🟢 SAFE"

        return {
            "status": status,
            "confidence": f"{confidence:.2%}",
            "label_id": prediction
        }

if __name__ == "__main__":
    detector = PIIDetector("base", "v4")
    sample = "User Hasan logged in with CNIC 42101-1234567-1"
    
    result = detector.predict(sample)
    print(f"\nAudit: {result['status']} | Confidence: {result['confidence']}")