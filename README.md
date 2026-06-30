#  DocuMind

### AI-Powered Research Paper Learning Assistant using Retrieval-Augmented Generation (RAG)

---

##  Overview

DocuMind is an **AI-powered Research Paper Learning Assistant** that helps users understand complex academic papers through **Retrieval-Augmented Generation (RAG)**. It retrieves the most relevant sections of a paper using semantic search and generates grounded explanations instead of generic LLM responses.

Unlike traditional PDF chatbots that simply answer questions, DocuMind retrieves the most relevant sections of a research paper using semantic search and generates grounded explanations for key aspects such as the paper's summary, methodology, experimental results, limitations, and future work.

The application combines **Sentence Transformers**, **ChromaDB**, and a locally hosted **Phi-3** Large Language Model through **Ollama** to provide context-aware responses while displaying page-level supporting evidence for transparency.

---

##  Features

-  Upload research papers in PDF format
-  Semantic search using Sentence Transformers
-  Retrieval-Augmented Generation (RAG)
-  ChromaDB vector database
-  Local inference using Phi-3 via Ollama
-  AI-generated paper summaries
-  Methodology explanation
-  Experimental results analysis
-  Limitations identification
-  Future work analysis
-  Page-level supporting evidence
-  Chat history
-  Interactive Streamlit interface

---

##  System Architecture

```text
                PDF Upload
                     │
                     ▼
              PyMuPDF Extraction
                     │
                     ▼
             Recursive Chunking
                     │
                     ▼
      Sentence Transformer Embeddings
                     │
                     ▼
             ChromaDB Vector Store
                     │
                     ▼
             Semantic Retrieval
                     │
                     ▼
          Phi-3 (Ollama Local LLM)
                     │
                     ▼
      Structured Research Explanations
                     │
                     ▼
             Streamlit Frontend
```

---

##  Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Frontend | Streamlit |
| PDF Processing | PyMuPDF |
| Chunking | LangChain RecursiveCharacterTextSplitter |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| Retrieval | Semantic Search (RAG) |
| LLM | Phi-3 (Ollama) |

---

##  Project Structure

```text
DocuMind/
│
├── app.py
├── pdf_processor.py
├── chunking.py
├── embeddings.py
├── vector_store.py
├── retrieval.py
├── generator.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

##  Installation

Clone the repository

```bash
git clone https://github.com/yourusername/DocuMind.git
```

Move into the project

```bash
cd DocuMind
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Phi-3

```bash
ollama run phi3
```

Launch the application

```bash
streamlit run app.py
```

---

##  Usage

1. Upload a research paper in PDF format.
2. Click **Process PDF**.
3. Wait for the document to be indexed.
4. Use either:
   -  Summary
   -  Methodology
   -  Results
   -  Limitations
   -  Future Work
   -  Custom Questions
5. Review the generated explanation together with page-level supporting evidence.

---

##  Future Improvements

- Hybrid Retrieval (BM25 + Semantic Search)
- Cross-Encoder Re-ranking
- Section-aware Chunking
- Multi-document comparison
- PDF text highlighting
- Citation extraction

---

##  Author

**Nandini Kumari**

Computer Engineering Student

Thapar Institute of Engineering & Technology