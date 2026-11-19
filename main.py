from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from rag import retrieve_context
from knowledge_graph import search_knowledge_graph
import requests

# Create FastAPI application
app = FastAPI(title="SpaceScope AI")

# Connect frontend static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Prompt Engineering instructions
SYSTEM_PROMPT = """
You are SpaceScope AI, a friendly space science
learning assistant.

Your responsibilities:
1. Answer questions about space science.
2. Explain concepts in simple English.
3. Assume the user is a beginner.
4. Give examples wherever useful.
5. Organize answers using headings and bullet points.
6. Provide scientifically accurate information.
7. Use the supplied RAG context and Knowledge Graph
   information when answering.
8. Do not invent facts that are not supported by
   the supplied information.
9. Politely redirect unrelated questions.
"""


# Request format
class Question(BaseModel):
    question: str


# Home page
@app.get("/")
def home():
    return FileResponse("static/index.html")


# Ask question API
@app.post("/ask")
def ask_question(data: Question):

    try:
        # Step 1: Retrieve information using RAG
        context_chunks = retrieve_context(data.question)

        rag_context = "\n".join(context_chunks)

        # Step 2: Retrieve information using Knowledge Graph
        graph_results = search_knowledge_graph(data.question)

        graph_context = "\n".join(graph_results)

        # Step 3: Combine both retrieved information
        combined_context = f"""
        RAG INFORMATION:
        {rag_context}

        KNOWLEDGE GRAPH INFORMATION:
        {graph_context}
        """

        # Step 4: Check whether information is available
        if not rag_context and not graph_context:
            return {
                "question": data.question,
                "retrieved_context": "",
                "answer": "Sorry, this information is not available in my space science knowledge base."
            }

        # Step 5: Send combined information to Ollama
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3.2:3b",
                "messages": [
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": f"""
                        Use the following retrieved information
                        to answer the question.

                        {combined_context}

                        Question: {data.question}
                        """
                    }
                ],
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()

        result = response.json()

        # Step 6: Return final answer
        return {
            "question": data.question,
            "retrieved_context": combined_context,
            "answer": result["message"]["content"]
        }

    except requests.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Ollama connection failed. Check whether Ollama is running."
        )
