import chromadb

chroma_client = chromadb.HttpClient(host='localhost', port=8000)
print("ChromaDB heartbeat:", chroma_client.heartbeat())

# Test Llama 3 on Ollama
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")
response = llm.invoke("Hello, how are you?")
print("Llama 3 response:", response)

