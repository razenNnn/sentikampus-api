import requests
import streamlit as st

st.set_page_config(page_title="SentiKampus - Web Demo", page_icon="💬")

st.title("SentiKampus 💬")
st.subheader("Analisis Sentimen Komentar Layanan Kampus")

text_input = st.text_area(
    "Masukkan Komentar Layanan",
    placeholder="Contoh: Pelayanan admin sangat bagus dan cepat...",
    height=120
)

if st.button("Analisis Sentimen", use_container_width=True):
    if len(text_input.strip()) < 3:
        st.warning("⚠️ Komentar minimal harus berisi 3 karakter.")
    else:
        with st.spinner("Sedang memproses prediksi model AI..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/api/v1/predict",
                    json={"text": text_input},
                    timeout=10
                )
                if response.status_code == 200:
                    result = response.json()
                    st.success("Analisis Berhasil!")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Label Sentimen", result.get("label", "N/A"))
                    with col2:
                        score_val = result.get("score", 0.0)
                        st.metric("Skor Kepercayaan", f"{score_val:.2f}")
                    st.write("**Progres Skor:**")
                    st.progress(float(score_val))
                else:
                    st.error(f"❌ Server Error: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"🔌 Gagal terhubung ke backend FastAPI: {e}")