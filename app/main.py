from time import perf_counter
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .schemas import SentimentRequest, SentimentResponse
from .model_service import predict_text

app = FastAPI(title='SentiKampus API')

# Konfigurasi CORS agar Flutter Web/Mobile dapat mengakses API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Process-Time-Ms"],
)

# --- MIDDLEWARE MONITORING LATENCY (P07) ---
@app.middleware('http')
async def add_process_time(request: Request, call_next):
    start = perf_counter()
    response = await call_next(request)
    elapsed_ms = (perf_counter() - start) * 1000
    
    # Tambahkan latency server ke header response agar bisa dibaca Flutter/Script Benchmark
    response.headers['X-Process-Time-Ms'] = f"{elapsed_ms:.2f}"
    
    # Cetak log telemetry di terminal server
    print({
        'path': request.url.path,
        'status': response.status_code,
        'latency_ms': round(elapsed_ms, 2),
        'model_version': 'v1.0.0'
    })
    
    return response

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/api/v1/predict', response_model=SentimentResponse)
def predict(data: SentimentRequest):
    result = predict_text(data.text)
    return SentimentResponse(**result)