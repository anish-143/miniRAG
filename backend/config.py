import os

# Deployment mode: "full" (local models) or "lite" (API-only, deploy-safe)
DEPLOYMENT_MODE = os.getenv("DEPLOYMENT_MODE", "full")

USE_LOCAL_EMBEDDINGS = DEPLOYMENT_MODE == "full"
USE_RERANKER = DEPLOYMENT_MODE == "full"

# Qdrant config (read directly where needed)
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "policylens_chunks")
