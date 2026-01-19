from backend.config import USE_RERANKER

_model = None

def rerank_chunks(query: str, chunks: list[dict], top_n: int = 5):
    if not chunks:
        return []

    if not USE_RERANKER:
        # Lite mode: skip reranking
        return chunks[:top_n]

    global _model
    if _model is None:
        try:
            from sentence_transformers import CrossEncoder
            _model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        except ImportError:
            print("WARNING: sentence-transformers not available, skipping reranking")
            return chunks[:top_n]

    pairs = [(query, c["text"]) for c in chunks]
    scores = _model.predict(pairs)

    for c, score in zip(chunks, scores):
        c["score"] = float(score)

    chunks.sort(key=lambda x: x["score"], reverse=True)
    return chunks[:top_n]
