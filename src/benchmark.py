# src/benchmark.py

import time
from .inference import PIIDetector

def run_benchmark():
    test_sample = "Please transfer funds to IBAN PK12BANK0000001234567890 for the CNIC 42101-1111111-1."
    tiers = [
        ("base", "v4"),
        ("small", "v7"),
        ("tiny", "v4")
    ]
    
    print(f"{'Tier':<10} | {'Time (s)':<10} | {'Findings'}")
    print("-" * 40)
    
    for tier, ver in tiers:
        start_time = time.time()
        
        # Load and Predict
        detector = PIIDetector(tier=tier, version=ver)
        results = detector.predict(test_sample)
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"{tier:<10} | {duration:<10.4f} | {len(results)} items found")

if __name__ == "__main__":
    run_benchmark()