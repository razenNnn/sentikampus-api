from time import perf_counter

def predict_text(text: str) -> dict:
    start = perf_counter()
    
    # Logika inferensi / XAI sederhanamu
    # Contoh ekstraksi fitur kata untuk XAI:
    words = text.lower().split()
    explanation = []
    
    # Contoh pemetaan nilai kontribusi kata
    weights = {"bagus": 0.45, "cepat": 0.38, "lambat": -0.42, "error": -0.50, "jelek": -0.38}
    for word in words:
        if word in weights:
            explanation.append({"feature": word, "contribution": weights[word]})
            
    # Tentukan label dan skor
    score_val = sum([item["contribution"] for item in explanation])
    label = "Positif" if score_val >= 0 else "Negatif"
    
    elapsed_ms = (perf_counter() - start) * 1000
    
    return {
        "label": label,
        "score": round(abs(score_val) if score_val != 0 else 0.85, 2),
        "model_version": "v1.0.0",
        "server_latency_ms": round(elapsed_ms, 2),
        "explanation": explanation
    }