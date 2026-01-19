# 🤖 miniRAG - Enterprise RAG AI Assistant

An advanced **Retrieval-Augmented Generation (RAG)** system with enterprise-grade UI, file upload capabilities, calculated confidence scoring, and comprehensive performance metrics.

## 🔗 Live Demo

Demo URL:  
https://minirag-1c3t.onrender.com



---

## ✨ Key Features

- 📁 **File Upload Support**: PDF and TXT document processing with automatic text extraction
- 🎯 **Calculated Confidence**: Percentage-based confidence scoring (0-99%) with color-coded indicators
- 📊 **Comprehensive Metrics**: Detailed performance tracking including:
  - Retrieval time
  - Reranking time
  - LLM processing time
  - Total response time
  - Token usage
  - Estimated cost
- 🎨 **Enterprise UI**: Professional dark/light theme with animated gradient backgrounds
- 🔍 **Smart Search**: Vector-based semantic search with Qdrant cloud integration
- 🤖 **AI-Powered**: Groq LLM for intelligent question answering
- 📝 **Optional Metadata**: Flexible source field with auto-fill functionality

---

## 🏗️ Project Structure

```
Mini-Rag-Policy-QA/
├── backend/
│   ├── app.py                    # FastAPI main application
│   ├── answer_generator.py       # LLM response generation
│   ├── answer.py                 # Answer processing logic
│   ├── chunking.py               # Document chunking utilities
│   ├── config.py                 # Configuration management
│   ├── context_builder.py        # Context preparation for LLM
│   ├── embeddings.py             # Text embedding generation
│   ├── ingest.py                 # Document ingestion pipeline
│   ├── qdrant_conn.py            # Qdrant database connection
│   ├── rerank.py                 # Result reranking logic
│   ├── retrieve.py               # Vector search retrieval
│   ├── schemas.py                # Pydantic data models
│   ├── vector_store.py           # Vector storage operations
│   └── static/
│       └── index.html            # Enterprise-grade frontend UI
├── eval/                         # Evaluation scripts
├── .env                          # Environment variables (API keys)
├── .env.example                  # Environment template
├── requirements.txt              # Python dependencies
├── runtime.txt                   # Python version specification
└── README.md                     # Project documentation
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12.5+
- Qdrant Cloud account (or local Qdrant instance)
- Groq API key

### 1️⃣ Clone Repository
```bash
git clone https://github.com/anish-143/miniRAG.git
cd miniRAG
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment
Create a `.env` file with:
```env
LLM_API_KEY=your_groq_api_key_here
QDRANT_URL=your_qdrant_cloud_url_here
QDRANT_API_KEY=your_qdrant_api_key_here
```

### 5️⃣ Run the Application
```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
```

### 6️⃣ Access the UI
Open your browser at: **http://localhost:8000/ui/**

---

## 📡 API Endpoints

| Method | Endpoint   | Description                          |
|--------|-----------|--------------------------------------|
| GET    | `/health` | Health check                         |
| POST   | `/ingest` | Ingest document (text + metadata)    |
| POST   | `/upload` | Upload PDF/TXT file                  |
| POST   | `/query`  | Ask questions about documents        |
| GET    | `/ui/`    | Access web interface                 |

---

## 🎯 How It Works

### Document Ingestion Flow
1. **Upload**: User uploads PDF/TXT file or inputs text manually
2. **Chunking**: Document split into overlapping chunks (~800 tokens, 100 token overlap)
3. **Embedding**: Chunks converted to vector embeddings
4. **Storage**: Vectors stored in Qdrant cloud database with metadata

### Query Processing Flow
1. **Query Embedding**: User question converted to vector
2. **Retrieval**: Top-K similar chunks retrieved from Qdrant
3. **Reranking**: Results reranked by relevance
4. **Context Building**: Selected chunks assembled as context
5. **LLM Generation**: Groq generates answer from context
6. **Metrics Calculation**: Performance metrics computed
7. **Confidence Scoring**: Percentage-based confidence calculated
8. **Response**: Answer with metrics, confidence, and sources returned

---

## 📊 Performance Metrics

The system tracks and displays:
- **Retrieval Time**: Vector search duration (ms)
- **Reranking Time**: Result reranking duration (ms)
- **LLM Time**: AI processing duration (ms)
- **Total Time**: End-to-end response time (ms)
- **Tokens Used**: Estimated token count
- **Estimated Cost**: Calculated based on Groq pricing ($0.05/1M tokens)

---

## 🎨 UI Features

- **Dark/Light Theme**: Toggle between themes
- **Animated Background**: Gradient with floating orbs
- **File Upload**: Drag-and-drop or click to upload
- **Optional Source**: Auto-fills with document title
- **Confidence Indicators**: Color-coded percentage scores
  - 🟢 High (85-99%): Green
  - 🟡 Medium (40-84%): Yellow
  - 🔴 Low (0-39%): Red
- **Metrics Dashboard**: Real-time performance statistics
- **Responsive Design**: Works on desktop and mobile

---

## 🔧 Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Qdrant**: Vector database for semantic search
- **Groq**: High-performance LLM API
- **pypdf**: PDF text extraction
- **sentence-transformers**: Text embeddings

### Frontend
- **HTML5/CSS3/JavaScript**: Pure vanilla stack
- **Font Awesome**: Icon library
- **Google Fonts**: Space Grotesk, Inter, JetBrains Mono

---

## ⚙️ Configuration

### Deployment Modes
- **Full Mode**: Uses sentence-transformers and cross-encoder reranking
- **Lite Mode**: Mock embeddings for memory-constrained environments

Set in `.env`:
```env
DEPLOYMENT_MODE=full  # or 'lite'
```

---

## 🧪 Example Usage

### Upload a Document
1. Click "Upload Document"
2. Select PDF/TXT file or paste text
3. Enter title (required)
4. Enter source (optional - auto-fills with title)
5. Click "Ingest"

### Ask Questions
1. Type your question in the query box
2. Click "Ask"
3. View:
   - AI-generated answer
   - Confidence score
   - Performance metrics
   - Retrieved sources

---

## 📝 Example Queries

- "What is blockchain technology?"
- "Explain the consensus mechanism"
- "How does distributed ledger work?"
- "What are smart contracts?"

---

## 👤 Author

**Name:** Anish Kumar  
**Roll No:** 231210016  
**Branch:** Computer Science & Engineering (CSE)  
**College:** National Institute of Technology (NIT) Delhi  
**Email:** 231210016@nitdelhi.ac.in  
**GitHub:** https://github.com/anish-143  
**Resume:** https://drive.google.com/file/d/1-z8Fygk5TdMhaqnXgXh6coy4UCvva60y/view?usp=drive_link

## 📄 License

This project is created for academic purposes at NIT Delhi.

---

## 🙏 Acknowledgments

- NIT Delhi CSE Department
- Qdrant for vector database technology
- Groq for LLM API access
- FastAPI for the excellent framework  


