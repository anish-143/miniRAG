import os
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION = os.getenv("QDRANT_COLLECTION")

DEPLOYMENT_MODE = os.getenv("DEPLOYMENT_MODE", "full")

VECTOR_SIZE = 384  # must match embed_texts output

_client = None


def get_client():
    global _client
    if _client is None:
        _client = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY
        )
    return _client


def ensure_collection():
    client = get_client()
    collections = [c.name for c in client.get_collections().collections]

    if COLLECTION in collections:
        # 🔒 Local safety: never delete data
        if DEPLOYMENT_MODE == "full":
            return

        # ♻️ Lite mode: recreate safely
        client.delete_collection(COLLECTION)

    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE
        )
    )
