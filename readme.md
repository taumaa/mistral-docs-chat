# Mistral Documentation Chat

A smart chatbot that leverages Huggingface's Smolagents framework and Mistral AI models to implement RAG for querying Mistral AI's documentation using natural language.

## About the Project

This project creates an interactive chat interface that leverages vector embeddings and semantic search to find relevant information from Mistral AI's documentation. It uses the following components:

- **Documentation Retrieval**: Fetches and processes Mistral's documentation
- **Vector Database**: Stores document embeddings for efficient semantic search
- **LLM Integration**: Uses Mistral's own models to understand queries and generate responses
- **Tool-based Agent**: Implements a tool-calling agent architecture for flexible query handling 

## Tools Used

- **Mistral AI**: LLM provider for embeddings and text generation
- **ChromaDB**: Vector database for storing and querying document embeddings
- **Smolagents**: Framework for building tool-using agents
- **Gradio**: Web interface for interacting with the chatbot

## How to Launch

### Prerequisites

- Python
- Mistral API key

### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mistral-docs-chat
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your API key:
   ```
   cp const.example.py const.py
   ```
   Then edit `const.py` to add your Mistral API key:
   ```python
   MISTRAL_API_KEY = "your-api-key-here"
   ```

### Running the Application

1. Launch the chat interface:
   ```
   python main.py
   ```
   This will start a Gradio web interface where you can interact with the chatbot.

2. Open your browser and navigate to the URL displayed in the terminal (typically http://127.0.0.1:7860).

3. (Optional) By default, the vector database is already populated with Mistral documentation. If you want to refresh the database at any time, you can run:
   ```
   python index.py
   ```
   to reindex the whole Mistral documentation.
