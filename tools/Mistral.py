from smolagents import Tool
from clients.LLM import LLMClient
from clients.Chroma import ChromaClient
from const import MISTRAL_API_KEY

class MistralTool(Tool):
    name = "mistral_documentation_retrieval"
    description = "This is a tool that retrieves relevant informations from the Mistral documentation based on the user's query. It returns parts from the documentation that are relevant to the user's query."
    inputs = {
        "query": {
            "type": "string",
            "description": "A short, consice and precise query that sums up what the user is looking for in mistral documentation",
        }
    }
    output_type = "string"

    def forward(self, query: str):
        llm = LLMClient()

        chroma_client = ChromaClient(
            init_collection=True
        )

        embeddings = llm.get_single_embedding(query)

        results_query = chroma_client.query_documents_from_embeddings("mistral", embeddings, n_results=4)
        
        results_text = "A list of relevant informations from the Mistral documentation:\n"
        for result in results_query['metadatas'][0]:
            results_text += f"Title: {result['title']}\nContent: {result['content']}\n\n"
        
        if results_text:
            results_text = results_text.rstrip()
            
        return results_text
