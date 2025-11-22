import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import chromadb
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file.")

# Configure Settings
print("Initializing Gemini...")
Settings.llm = Gemini(api_key=GOOGLE_API_KEY, model_name="models/gemini-flash-latest")
print("Initializing Embeddings (this may take a while to download)...")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
print("Settings configured.")

def load_data():
    if not os.path.exists("data"):
        os.makedirs("data")
    reader = SimpleDirectoryReader("data")
    documents = reader.load_data()
    return documents

def init_index():
    documents = load_data()
    
    # Initialize ChromaDB
    db = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = db.get_or_create_collection("quickstart")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    if not documents:
        # If no documents, return an empty index or handle gracefully
        # For this scaffold, we'll assume documents might be added later
        # But to initialize the index properly with storage context, we usually need docs or load from storage
        # If the DB exists, we can load from it.
        try:
            index = VectorStoreIndex.from_vector_store(
                vector_store,
                storage_context=storage_context,
            )
        except Exception:
             # Fallback if empty
             index = VectorStoreIndex.from_documents(
                [], storage_context=storage_context
            )
    else:
        index = VectorStoreIndex.from_documents(
            documents, storage_context=storage_context
        )
        
    return index

def get_chat_engine():
    index = init_index()
    return index.as_chat_engine(chat_mode="context", system_prompt="You are a helpful assistant.")
