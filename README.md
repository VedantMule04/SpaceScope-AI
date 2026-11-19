# 🚀 SpaceScope AI – Space Science Learning Assistant

SpaceScope AI is an AI-powered space science learning assistant that answers beginner-friendly questions about the universe, planets, galaxies, stars, black holes, and space exploration.

The project combines **Retrieval-Augmented Generation (RAG)** and a **Knowledge Graph** to retrieve relevant information from a local knowledge base and relationships between space science entities. The retrieved information is passed to a locally running LLM to generate answers.

## 🎯 Project Objectives

- Provide simple and understandable explanations of space science.
- Retrieve relevant information from a custom knowledge base using RAG.
- Represent space science concepts and their relationships using a Knowledge Graph.
- Combine document retrieval and graph-based information retrieval.
- Generate responses using a locally running Large Language Model.

## ✨ Key Features

- Interactive browser-based chat interface.
- RAG-based document retrieval.
- Knowledge Graph with entities and relationships.
- Semantic similarity search using embeddings.
- AI-generated answers using Llama 3.2.
- Local LLM execution using Ollama.
- FastAPI backend for handling user questions.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Backend API |
| HTML, CSS, JavaScript | Frontend |
| Sentence Transformers | Text embeddings |
| Scikit-learn | Cosine similarity |
| NetworkX | Knowledge Graph |
| Ollama | Local LLM execution |
| Llama 3.2 3B | Answer generation |
| Uvicorn | FastAPI server |

## 🧠 How It Works

1. The user enters a space science question through the website.
2. FastAPI receives the question.
3. The RAG component searches the local knowledge document using embeddings and cosine similarity.
4. The Knowledge Graph component searches for relevant entities and relationships.
5. The retrieved information from both components is combined.
6. The combined context is sent to the Llama 3.2 model through Ollama.
7. The generated answer is returned and displayed on the website.

## 📂 Project Structure

```text
SpaceScope-AI/
│
├── documents/
│   └── solar_system.txt
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── main.py
├── rag.py
├── knowledge_graph.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nageabhishek530-cloud/SpaceScope-AI.git
```

### 2. Open the Project Folder

```bash
cd SpaceScope-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Download Ollama from:

https://ollama.com/

### 6. Download the Llama 3.2 Model

```bash
ollama pull llama3.2:3b
```

Make sure the Ollama service is running.

### 7. Run the FastAPI Application

```bash
uvicorn main:app --reload
```

### 8. Open the Application

Open your browser and visit:

**http://127.0.0.1:8000**

FastAPI Swagger documentation:

**http://127.0.0.1:8000/docs**

## 🔍 Example Questions

- Tell me about the Solar System.
- Why is Mars called the Red Planet?
- What is the Milky Way?
- Which planet is the largest?
- What is a black hole?
- Tell me about Chandrayaan-3.

## 📌 Current Limitations

- The Knowledge Graph currently contains manually defined entities and relationships.
- Graph retrieval uses keyword matching.
- The knowledge base has limited coverage of space science topics.
- The application requires Ollama and the Llama 3.2 model to run locally.
- The project does not currently include persistent chat history or user authentication.

## 🚀 Future Enhancements

- Expand the Knowledge Graph with more space science entities and relationships.
- Improve natural-language entity extraction and graph retrieval.
- Add graph visualization.
- Support PDF document ingestion.
- Improve retrieval accuracy.
- Add source references for retrieved information.
- Deploy the application to a cloud platform.

## 👨‍💻 Author

**Abhishek Namdev Nage**
**Vedant Nandkumar Mule**
**Pratik Pandurang Zadke**
B.Tech – Computer Engineering

Dr. Babasaheb Ambedkar Technological University (DBATU)

---
