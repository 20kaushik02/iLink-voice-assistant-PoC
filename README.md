# iLink Digital PoC - Voice Assistant for Field Planning

![architecture diagram](./docs/architecture%20diagram.svg)

## Tech Stack

- Core
  - LLM - Gemini 2.5 Flash
  - RAG
    - Vector database - Qdrant
    - Embedding model - all-MiniLM-L6-v2
- Interface
  - Web app - Streamlit framework
  - Speech-to-text - OpenAI Whisper
  - Text-to-speech - Google Translate TTS (gTTS)
- Document corpus example
  - MSHA program policy manuals - [msha.gov](https://www.msha.gov/compliance-and-enforcement/compliance-assistance/program-policy-manual)
