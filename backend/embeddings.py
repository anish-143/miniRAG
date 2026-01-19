import hashlib
import os
import requests
from backend.config import USE_LOCAL_EMBEDDINGS

EMBEDDING_DIM = 384

# ---------- COMMON FUNCTIONS ----------
def embed_with_hf_api(texts: list[str]) -> list[list[float]]:
    """Use Hugging Face Inference API for free embeddings"""
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    
    if not hf_token:
        return None
        
    api_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
    headers = {"Authorization": f"Bearer {hf_token}"}
    
    try:
        response = requests.post(
            api_url,
            headers=headers,
            json={"inputs": texts, "options": {"wait_for_model": True}}
        )
        
        if response.status_code == 200:
            embeddings = response.json()
            # Normalize embeddings
            import numpy as np
            embeddings = np.array(embeddings)
            norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
            embeddings = embeddings / norms
            return embeddings.tolist()
        else:
            print(f"HF API error: {response.status_code}")
            return None
    except Exception as e:
        print(f"HF API exception: {e}")
        return None

def fake_embedding(text: str, dim: int = EMBEDDING_DIM):
    """Fallback deterministic embedding"""
    h = hashlib.sha256(text.encode()).digest()
    vec = []
    while len(vec) < dim:
        for b in h:
            vec.append(b / 255.0)
            if len(vec) == dim:
                break
    return vec

def fallback_embed(texts: list[str]) -> list[list[float]]:
    """Try HF API first, fallback to deterministic"""
    embeddings = embed_with_hf_api(texts)
    if embeddings:
        return embeddings
    else:
        print("Using fallback embeddings (no HF token)")
        return [fake_embedding(t) for t in texts]

# ---------- FULL MODE (LOCAL / REAL) ----------
if USE_LOCAL_EMBEDDINGS:
    try:
        from sentence_transformers import SentenceTransformer
        TRANSFORMERS_AVAILABLE = True
    except ImportError:
        print("WARNING: sentence-transformers not available, using lite mode")
        TRANSFORMERS_AVAILABLE = False

    _model = None

    def get_model():
        global _model
        if not TRANSFORMERS_AVAILABLE:
            return None
        if _model is None:
            _model = SentenceTransformer("all-MiniLM-L6-v2")
        return _model

    def embed_texts(texts: list[str]) -> list[list[float]]:
        model = get_model()
        if model:
            return model.encode(
                texts,
                normalize_embeddings=True
            ).tolist()
        else:
            # Fallback to API/mock
            return fallback_embed(texts)

# ---------- LITE MODE (API-BASED FOR RENDER) ----------
else:
    def embed_texts(texts: list[str]) -> list[list[float]]:
        return fallback_embed(texts)
