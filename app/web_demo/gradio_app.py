import requests
import gradio as gr

def analyze_sentiment(text):
    if len(text.strip()) < 3:
        return "Warning: Minimal 3 karakter", 0.0
    
    try:
        response = requests.post(
            'http://127.0.0.1:8000/api/v1/predict',
            json={'text': text},
            timeout=10
        )
        if response.status_code == 200:
            result = response.json()
            return result['label'], float(result['score'])
        else:
            return f"Error {response.status_code}", 0.0
    except Exception as e:
        return "Koneksi Gagal", 0.0

demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=4, placeholder="Tulis komentar ulasan kampus di sini...", label="Komentar Layanan"),
    outputs=[
        gr.Textbox(label="Label Sentimen"),
        gr.Number(label="Skor Kepercayaan")
    ],
    title="SentiKampus - Gradio Web Interface",
    description="Prototipe cepat analisis sentimen ulasan mahasiswa berbasis API."
)

if __name__ == "__main__":
    demo.launch()