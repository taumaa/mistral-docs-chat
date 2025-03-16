import chromadb, mistralai
from const import MISTRAL_API_KEY

class MistralEmbeddings(chromadb.EmbeddingFunction):
    def __init__(self, api_key: str):
        self.client = mistralai.Mistral(api_key=api_key)
        self.model = "mistral-embed"

    def __call__(self, input: chromadb.Documents) -> chromadb.Embeddings:
        response = self.client.embeddings.create(
            model=self.model,
            inputs=input,
        )
        return [embedding.embedding for embedding in response.data]

class ChromaClient:
    def __init__(self, mistral_api_key: str = MISTRAL_API_KEY, init_collection: bool = False):
        self.client = chromadb.PersistentClient(path="db")
        self.embeddings = MistralEmbeddings(api_key=mistral_api_key)
        if init_collection:
            self.mistral_collection = self.get_or_create_collection("mistral")

    def get_or_create_collection(self, name: str):
        return self.client.get_or_create_collection(
            name,
            embedding_function=self.embeddings
        )
    
    def delete_collection(self, name: str):
        self.client.delete_collection(name)

    def query_documents_from_embeddings(self, collection_name: str, embeddings: list[float], n_results: int = 10):
        return self.mistral_collection.query(
            query_embeddings=embeddings,
            n_results=n_results
        )
    
    def add_documents(self, collection_name: str, documents: list[str], ids: list[str], metadatas: list[dict] = None):
        """Add documents to a collection with their IDs and optional metadata"""
        collection = self.get_or_create_collection(collection_name)
        collection.add(
            documents=documents,
            ids=ids,
            metadatas=metadatas
        )
        
        
        
        