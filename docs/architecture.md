# System Architecture

![architecture diagram](./architecture%20diagram.svg)

## Tech Stack

- Core
  - LLM - [Gemini 2.5 Flash (API)](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash) (replaceable with better models)
  - RAG
    - Vector database - [Qdrant (local)](https://qdrant.tech/qdrant-vector-database/) (replaceable)
    - Embedding model - [all-MiniLM-L6-v2 (local)](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) (replaceable with better models)
- Interface
  - Web application interface - [Streamlit app framework](https://streamlit.io/)
  - Speech-to-text - [OpenAI Whisper (local)](https://github.com/openai/whisper)
  - Text-to-speech - [Google Translate TTS](https://gtts.readthedocs.io/en/latest/) (replaceable with better models)
- Sample dataset
  - Document corpus: MSHA program policy manuals - [msha.gov](https://www.msha.gov/compliance-and-enforcement/compliance-assistance/program-policy-manual) - field manual documents in PDF format

## Flow

1. User records voice input (Streamlit).
2. Audio sent to backend → Whisper transcribes speech.
3. Transcribed text passed to LLM (Gemini) with optional retrieved context (RAG system).
4. LLM response → TTS (gTTS/local).
5. Audio response played back in frontend.

## Getting Started

### Prerequisites

- Python 3.12 and `uv` package manager
- Docker Compose
- Gemini API key
- System requirements: GPU + CUDA driver (modify `torch` version as needed, switch to CPU-only version if no GPU available)

### Installation

- Install dependencies

```sh
uv sync
docker compose -f ./docker/docker-compose.yml pull
```

- Set `GEMINI_API_KEY` environment variable through the shell or a `.env` file at project root
- Spin up vector database

```sh
docker compose -f ./docker/docker-compose.yml up -d
```

### Indexing documents

Run the indexer script to ingest the sample documents in the `data/docs` folder

```sh
uv run ./src/rag/indexer.py
```

### Run app

```sh
uv run streamlit run ./src/main.py
```
