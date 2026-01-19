import hashlib
import os
import requests
from backend.config import USE_LOCAL_EMBEDDINGS

EMBEDDING_DIM = 384

# ---------- FULL MODE (LOCAL / REAL) ----------
if USE_LOCAL_EMBEDDINGS:
    from sentence_transformers import SentenceTransformer

    _model = None

    def get_model():
        global _model
        if _model is None:
            _model = SentenceTransformer("all-MiniLM-L6-v2")
        return _model

    def embed_texts(texts: list[str]) -> list[list[float]]:
        return get_model().encode(
            texts,
            normalize_embeddings=True
        ).tolist()

# ---------- LITE MODE (API-BASED FOR RENDER) ----------
else:
    def embed_with_hf_api(texts: list[str]) -> list[list[float]]:
        """Use Hugging Face Inference API for free embeddings"""
        hf_token = os.getenv("HUGGINGFACE_TOKEN")
        
        if not hf_token:
            # No token, use fallback
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

    def embed_texts(texts: list[str]) -> list[list[float]]:
        """Try HF API first, fallback to deterministic if unavailable"""
        embeddings = embed_with_hf_api(texts)
        
        if embeddings:
            return embeddings
        else:
            # Fallback to deterministic embeddings
            print("Using fallback embeddings (no HF token)")
            return [fake_embedding(t) for t in texts]
