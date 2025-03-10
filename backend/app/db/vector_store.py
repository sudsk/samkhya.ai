# backend/app/db/vector_store.py
from langchain_community.vectorstores import Chroma, FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_google_vertexai import VertexAIEmbeddings

class VectorStoreManager:
    def __init__(self, embedding_model="vertex_ai"):
        if embedding_model == "vertex_ai":
            self.embeddings = VertexAIEmbeddings()
        else:
            self.embeddings = OpenAIEmbeddings()
        
        # Initialize vector store
        self.vector_store = FAISS.from_documents([], self.embeddings)
    
    def add_documents(self, documents):
        """Add documents to the vector store"""
        self.vector_store.add_documents(documents)
    
    def similarity_search(self, query, k=5):
        """Retrieve relevant documents based on query"""
        return self.vector_store.similarity_search(query, k=k)
