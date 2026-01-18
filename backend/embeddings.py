import os
from backend.config import USE_LOCAL_EMBEDDINGS

_model = None

def embed_texts(texts: list[str]) -> list[list[float]]:
    global _model

    if USE_LOCAL_EMBEDDINGS:
        if _model is None:
            from sentence_transformers import SentenceTransformer
            _model = SentenceTransformer("all-MiniLM-L6-v2")

        return _model.encode(
            texts,
            normalize_embeddings=True
        ).tolist()

    # ---- Lite mode: use API embeddings ----
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("LLM_API_KEY"))

    embeddings = []
    for t in texts:
        r = client.embeddings.create(
            model="text-embedding-3-small",
            input=t
        )
        embeddings.append(r.data[0].embedding)

    return embeddings
