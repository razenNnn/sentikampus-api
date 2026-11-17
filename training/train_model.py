import pickle
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    'pelayanan cepat', 
    'petugas ramah', 
    'pelayanan lambat', 
    'informasi membingungkan'
]
labels = ['positive', 'positive', 'negative', 'negative']

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('model', LogisticRegression())
])

pipeline.fit(texts, labels)

Path('models').mkdir(exist_ok=True)
with open('models/sentiment.pkl', 'wb') as f:
    pickle.dump(pipeline, f)

print("[SUCCESS] Berkas models/sentiment.pkl berhasil dibuat!")