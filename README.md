# EchoMind
A Voice-First AI Assistant That Asks Before It Answers

EchoMind is a voice-enabled AI assistant designed to prioritize clarity over guesswork. Instead of immediately responding to incomplete queries, EchoMind intelligently asks clarifying questions, maintains conversational memory, and summarizes long interactions — all through a seamless voice-to-voice experience.

---

## Features

- Voice input and output using ElevenLabs (Speech-to-Text and Text-to-Speech)
- Clarifying questions when user input is incomplete or ambiguous
- Conversation memory with user-controlled persistence
- Automatic summarization when conversations become long
- End-to-end voice → reasoning → voice interaction
- Simple and lightweight Streamlit interface

---

## Tech Stack

- Frontend: Streamlit
- Speech Processing: ElevenLabs
- Large Language Model: Google Gemini (via LangChain)
- Language: Python
- Environment Management: python-dotenv

---

## Project Structure

.
├── app.py                # Streamlit application
├── chat_feature.py       # LLM logic, memory, summarization
├── requirements.txt
├── .env.example
└── README.md

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/your-username/echomind.git  
cd echomind

### 2. Create a virtual environment (recommended)

python -m venv venv  
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure environment variables

Create a `.env` file using the template below:

GOOGLE_API_KEY=your_google_api_key  
ELEVENLABS_API_KEY=your_elevenlabs_api_key

---

## Run the Application

streamlit run app.py

Open your browser at:

http://localhost:8501

---

## How It Works

1. The user speaks a query through the microphone.
2. Audio is transcribed using ElevenLabs.
3. The assistant checks for missing or ambiguous information.
4. If required, it asks clarifying questions before answering.
5. Once sufficient context is available, the assistant responds.
6. The response is converted back to natural-sounding speech.
7. Conversation memory is optionally stored and summarized when it grows large.

---

## Why EchoMind?

Most voice assistants respond instantly, even when critical context is missing. EchoMind behaves more like a thoughtful conversational partner — it listens carefully, asks when unsure, and answers only when it understands.

---

## What’s Next

- Tool-based actions such as web search and document analysis
- Improved memory prioritization strategies
- Reduced voice latency for faster interactions
- API-based deployment for integration with other applications

---

## License

This project is released under the MIT License.
