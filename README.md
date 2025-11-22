# RAG Chatbot with Gemini & ChromaDB

A Python-based RAG (Retrieval-Augmented Generation) chatbot that uses Google's Gemini for the LLM, ChromaDB for vector storage, and Streamlit for the web interface.

## Features

-   **RAG Pipeline**: Ingests and indexes documents from a local directory.
-   **Gemini Integration**: Uses Google's Gemini Pro (via `models/gemini-flash-latest`) for high-quality responses.
-   **Vector Search**: Utilizes ChromaDB for efficient similarity search.
-   **Interactive UI**: Clean and responsive chat interface built with Streamlit.
-   **Contextual History**: Maintains chat history for conversational context.

## Tech Stack

-   **Language**: Python 3.10+
-   **LLM**: Google Gemini (via `llama-index-llms-gemini`)
-   **Vector Store**: ChromaDB (via `llama-index-vector-stores-chroma`)
-   **Framework**: LlamaIndex
-   **Frontend**: Streamlit

## Prerequisites

-   Python 3.10 or higher
-   A Google Cloud Project with the Gemini API enabled
-   A Google API Key

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**:
    - Create a `.env` file in the root directory.
    - Add your Google API key:
        ```env
        GOOGLE_API_KEY=your_api_key_here
        ```

## Usage

1.  **Add Data**:
    - Place your text documents (e.g., `.txt`, `.md`) in the `data/` directory.
    - The application will automatically index these files on startup.

2.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```

3.  **Interact**:
    - Open your browser to the URL shown (usually `http://localhost:8501`).
    - Start chatting with your documents!

## Troubleshooting

-   **404 Model Not Found**: If you see an error about the model not being found, ensure your `rag_engine.py` is using a supported model name like `models/gemini-flash-latest` or `models/gemini-pro`.
-   **First Run Delay**: The first time you run the app, it will download the embedding model (approx. 1.5GB). This may take a few minutes depending on your internet connection.