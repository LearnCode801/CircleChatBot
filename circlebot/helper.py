import os
from langchain_astradb import AstraDBVectorStore
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from langchain_ai21 import AI21LLM




load_dotenv()

ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")
AI21LLM_API_KEY = os.environ.get('AI21LLM_API_KEY')



# Load the Sentence Transformers model for generating embeddings
embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Define an embedding function using Sentence Transformers
class CustomEmbeddingFunction:
    def __init__(self, model):
        self.model = model

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode([text]).tolist()[0]

embedding_function = CustomEmbeddingFunction(embedding_model)


pre_created_vector_store = AstraDBVectorStore(
    embedding=embedding_function,
    collection_name="astra_vector_demo",
    api_endpoint=ASTRA_DB_API_ENDPOINT,
    token=ASTRA_DB_APPLICATION_TOKEN,
    namespace=ASTRA_DB_KEYSPACE
)


def returning_pre_created_vector_store_obj():
    return pre_created_vector_store


def load_AI21Lab_llm():
    
    llm = AI21LLM(model="j2-ultra",api_key=AI21LLM_API_KEY,max_tokens=1024)
    return llm