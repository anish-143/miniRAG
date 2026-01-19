"""
Startup script for Mini RAG System
Run this to start the local development server
"""
import uvicorn
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

if __name__ == "__main__":
    print("=" * 60)
    print("Mini RAG Policy QA System")
    print("=" * 60)
    print("\nStarting server...")
    print("\n📍 Server URL: http://localhost:8000")
    print("📍 UI URL: http://localhost:8000/ui")
    print("📍 API Docs: http://localhost:8000/docs")
    print("\nPress CTRL+C to stop\n")
    print("=" * 60)
    
    try:
        uvicorn.run(
            "backend.app:app",
            host="0.0.0.0",
            port=8000,
            reload=False,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped")
