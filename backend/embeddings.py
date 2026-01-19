import hashlib
import os
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
    from openai import OpenAI
    
    _openai_client = None
    
    def get_openai_client():
        global _openai_client
        if _openai_client is None:
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                # Fallback to mock embeddings if no API key
                return None
            _openai_client = OpenAI(api_key=api_key)
        return _openai_client
    
    def fake_embedding(text: str, dim: int = EMBEDDING_DIM):
        """Fallback mock embedding if OpenAI not available"""
        h = hashlib.sha256(text.encode()).digest()
        vec = []
        while len(vec) < dim:
            for b in h:
                vec.append(b / 255.0)
                if len(vec) == dim:
                    break
        return vec

    def embed_texts(texts: list[str]) -> list[list[float]]:
        """Use OpenAI embeddings API in lite mode for better quality"""
        client = get_openai_client()
        
        if client:
            try:
                response = client.embeddings.create(
                    model="text-embedding-3-small",
                    input=texts
                )
                return [item.embedding for item in response.data]
            except Exception as e:
                print(f"OpenAI API error: {e}, falling back to mock embeddings")
                return [fake_embedding(t) for t in texts]
        else:
            # Use mock embeddings if no OpenAI key
            return [fake_embedding(t) for t in texts]
