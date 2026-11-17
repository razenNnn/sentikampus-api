# SentiKampus API

Backend REST API berbasis FastAPI untuk klasifikasi sentimen komentar layanan kampus.

## Endpoint Utama
- `GET /health` : Mengecek status kesehatan server.
- `GET /docs` : Dokumentasi interaktif Swagger UI.
- `POST /api/v1/predict` : Memprediksi sentimen teks komentar (`{"text": "..."}`).

## Deployment
Dideploy menggunakan Docker container pada platform PaaS (Render).