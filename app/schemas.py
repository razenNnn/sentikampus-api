from pydantic import BaseModel
from typing import List

class FeatureContribution(BaseModel):
    feature: str
    contribution: float

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: float
    model_version: str = "v1.0.0"
    server_latency_ms: float = 0.0
    explanation: List[FeatureContribution] = []