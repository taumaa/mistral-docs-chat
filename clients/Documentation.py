import requests

DOC_URL = "https://docs.mistral.ai/search-doc-1741654145924.json"

class DocumentationClient:

    def __init__(self, get_docs: bool = False):
        self.docs = []
        if get_docs:
            self.get_docs()

    def get_docs(self):
        try:
            doc = requests.get(DOC_URL).json().get("searchDocs")
            self.docs = [
                {
                    "title": x.get("title"),
                    "content": x.get("content"),
                }
                for x in doc
                if x.get("content") != ""
                and x.get("title") != ""
                and len(x.get("content")) < 30000
            ]
        except KeyError:
            raise ValueError("Invalid documentation format")

