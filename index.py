from clients.Documentation import DocumentationClient
from clients.LLM import LLMClient
from clients.Chroma import ChromaClient
import time
from const import MISTRAL_API_KEY

docs = DocumentationClient(get_docs=True)
llm_client = LLMClient()
chroma_client = ChromaClient(
    init_collection=True
)

chroma_client.delete_collection("mistral")
print("Collection deleted")

documents = []
ids = []
metadatas = [] 

for i, doc in enumerate(docs.docs):

    summary = llm_client.clean_text(doc['content'])
    print(f"Summary for doc {i}: {summary}")
    

    documents.append(summary)
    ids.append(f"doc_{i}")
    metadatas.append({
        "title": doc['title'],
        "content": doc['content'],
        "summary": summary
    })

    # avoid rate limit
    time.sleep(1)


chroma_client.add_documents(
    collection_name="mistral",
    documents=documents,
    ids=ids,
    metadatas=metadatas
)