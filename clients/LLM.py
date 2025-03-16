import mistralai
from const import MISTRAL_API_KEY
class LLMClient:

    """
    High level Mistral client
    """

    def __init__(self):
        self.client = mistralai.Mistral(api_key=MISTRAL_API_KEY)

    def clean_text(self, text: str) -> str:

        prompt = f"""
Below you will find a text from an online documentation. Your job is to describe the core content in a single, direct sentence.
Focus only on the essential information. Be concise and straightforward.

FORMAT: Write only a brief, imperative description. Use active voice.

EXAMPLE OUTPUT: Instructions and code snippets for querying the Mistral Large model using IBM's SDK or HTTP calls, emphasizing the importance of proper tokenization.

TEXT: {text}
"""


        response = self.client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )

        return response.choices[0].message.content
    
    def get_embeddings(self, texts: list[str]) -> list[float]:
        model = "mistral-embed"

        response = self.client.embeddings.create(
            model=model,
            inputs=texts,
        )

        return [
            embedding.embedding for embedding in response.data
        ]
    
    def get_single_embedding(self, text: str) -> list[float]:
        return self.get_embeddings([text])[0]
    
    